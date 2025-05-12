from django.contrib import admin
from django.utils.html import format_html
from .models import *
from django import forms
from django.http import JsonResponse
from django.db import models
from django.urls import path, reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import json
import logging
import traceback

logger = logging.getLogger(__name__)


class RawFileWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return format_html('<input type="file" name="{}" multiple>', name)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ['image_preview']
    fields = ['image', 'caption', 'order', 'image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "Нет изображения"
    
    image_preview.short_description = 'Предпросмотр'
    
    class Media:
        js = (
            'admin/js/cases_sortable.js',
        )


class CaseAdminForm(forms.ModelForm):
    multiple_images = forms.FileField(widget=RawFileWidget(), required=False, label="Загрузить несколько изображений сразу")
    
    class Meta:
        model = Case
        fields = ['restaurant_name', 'description']


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    form = CaseAdminForm
    inlines = [ImageInline]
    list_display = ('restaurant_name', 'description', 'image_count')
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:case_id>/update-image-order/', 
                self.admin_site.admin_view(self.update_image_order_view), 
                name='cases_case_update_image_order'),
        ]
        return custom_urls + urls
    
    def update_image_order_view(self, request, case_id):
        if request.method == "POST":
            try:
                logger.info(f"Processing update_image_order for case {case_id}")
                
                try:
                    case = Case.objects.get(pk=case_id)
                except Case.DoesNotExist:
                    logger.error(f"Case with id {case_id} does not exist")
                    return JsonResponse({'status': 'error', 'message': f'Case with id {case_id} does not exist'}, status=404)
                
                positions = []
                
                form_positions = request.POST.getlist('positions[]')
                if form_positions:
                    positions = form_positions
                    logger.info(f"Found positions in FormData: {positions}")
                
                if not positions and request.content_type == 'application/json':
                    try:
                        body_data = json.loads(request.body.decode('utf-8'))
                        json_positions = body_data.get('positions', [])
                        if json_positions:
                            positions = json_positions
                            logger.info(f"Found positions in JSON body: {positions}")
                    except Exception as e:
                        logger.error(f"Failed to parse JSON body: {str(e)}")
                
                if not positions:
                    logger.error("No positions found in request")
                    return JsonResponse({'status': 'error', 'message': 'No positions provided'}, status=400)
                
                try:
                    position_ids = [int(pid) for pid in positions]
                except (ValueError, TypeError) as e:
                    logger.error(f"Invalid position IDs: {str(e)}")
                    return JsonResponse({'status': 'error', 'message': f'Invalid position IDs: {str(e)}'}, status=400)
                
                images = list(Image.objects.filter(album_id=case_id, id__in=position_ids))
                if len(images) != len(position_ids):
                    found_ids = [img.id for img in images]
                    missing_ids = [pid for pid in position_ids if pid not in found_ids]
                    logger.error(f"Some image IDs not found or not in this case: {missing_ids}")
                    return JsonResponse({
                        'status': 'error', 
                        'message': f'Missing or invalid image IDs: {missing_ids}', 
                        'found_ids': found_ids,
                        'position_ids': position_ids
                    }, status=400)
                
                for i, image_id in enumerate(position_ids):
                    Image.objects.filter(id=image_id, album_id=case_id).update(order=i)
                    
                logger.info(f"Updated order for {len(position_ids)} images")
                return JsonResponse({'status': 'ok'})
            except Exception as e:
                logger.error(f"Error updating image order: {str(e)}")
                logger.error(traceback.format_exc())
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)
    
    def image_count(self, obj):
        return obj.images.count()
    
    image_count.short_description = 'Количество изображений'
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        multiple_images = request.FILES.getlist('multiple_images')
        if multiple_images:
            max_order = Image.objects.filter(album=obj).aggregate(max_order=models.Max('order'))['max_order'] or 0
            
            for i, image_file in enumerate(multiple_images):
                Image.objects.create(
                    album=obj,
                    image=image_file,
                    caption='',
                    order=max_order + i + 1
                )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('album', 'caption', 'image_preview', 'order')
    list_filter = ('album',)
    list_editable = ('order',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "Нет изображения"
    
    image_preview.short_description = 'Предпросмотр'
