from django.contrib import admin
from .models import Gallery
from django.utils.html import format_html
from django import forms
from django.shortcuts import render, redirect
from django.urls import path, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.db import models
import logging

logger = logging.getLogger(__name__)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'description', 'order')
    list_editable = ('order',)
    list_display_links = ('image_preview',)
    change_list_template = "gallery/gallery_changelist.html"
    
    class Media:
        css = {
            'all': ('https://code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css',)
        }
        js = (
            'https://cdn.jsdelivr.net/npm/sortablejs@1.15.0/Sortable.min.js',
            'admin/js/gallery_sortable.js',
        )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "Нет изображения"
    
    image_preview.short_description = 'Предпросмотр'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('bulk-upload/', 
                self.admin_site.admin_view(self.bulk_upload_view), 
                name='gallery_bulk_upload'),
            path('update-order/', 
                self.admin_site.admin_view(self.update_order_view), 
                name='gallery_update_order'),
        ]
        return custom_urls + urls
    
    def update_order_view(self, request):
        if request.method == "POST":
            try:
                positions = request.POST.getlist('positions[]')
                if not positions:
                    return JsonResponse({'status': 'error', 'message': 'No positions provided'}, status=400)
                
                galleries = Gallery.objects.filter(id__in=positions)
                if len(galleries) != len(positions):
                    found_ids = [img.id for img in galleries]
                    missing_ids = [pid for pid in positions if int(pid) not in found_ids]
                    return JsonResponse({
                        'status': 'error', 
                        'message': f'Missing or invalid gallery IDs: {missing_ids}', 
                    }, status=400)
                
                for i, gallery_id in enumerate(positions):
                    Gallery.objects.filter(id=gallery_id).update(order=i)
                    
                return JsonResponse({'status': 'ok'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)
    
    def bulk_upload_view(self, request):
        """Обработчик для загрузки множества изображений через HTML-форму"""
        if request.method == 'POST':
            # Получаем данные напрямую из запроса
            description = request.POST.get('description', '')
            files = request.FILES.getlist('files')
            
            # Проверяем, что все необходимые поля заполнены
            if not description:
                messages.error(request, "Необходимо указать описание для изображений")
                return render(request, 'gallery/bulk_upload.html', {
                    'title': 'Загрузка множества изображений в галерею',
                    'opts': self.model._meta,
                })
            
            if not files:
                messages.error(request, "Необходимо выбрать файлы для загрузки")
                return render(request, 'gallery/bulk_upload.html', {
                    'title': 'Загрузка множества изображений в галерею',
                    'opts': self.model._meta,
                })
            
            try:
                # Получаем максимальный order для корректного добавления
                max_order = Gallery.objects.aggregate(max_order=models.Max('order'))['max_order'] or 0
                
                # Создаем объекты для каждого файла
                count = 0
                for i, file_obj in enumerate(files):
                    logger.info(f"Processing file {i+1}/{len(files)}: {file_obj.name}")
                    
                    # Создаем объект галереи
                    Gallery.objects.create(
                        description=description,
                        image=file_obj,
                        order=max_order + i + 1
                    )
                    count += 1
                
                messages.success(request, f'Успешно загружено {count} изображений')
                return HttpResponseRedirect("../")
            except Exception as e:
                logger.error(f"Error uploading images: {str(e)}")
                messages.error(request, f"Произошла ошибка при загрузке изображений: {str(e)}")
                return render(request, 'gallery/bulk_upload.html', {
                    'title': 'Загрузка множества изображений в галерею',
                    'opts': self.model._meta,
                })
        else:
            # Отображаем форму для GET-запроса
            return render(request, 'gallery/bulk_upload.html', {
                'title': 'Загрузка множества изображений в галерею',
                'opts': self.model._meta,
            })


admin.site.register(Gallery, GalleryAdmin)
