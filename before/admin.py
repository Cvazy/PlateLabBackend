from django.contrib import admin
from .models import *
from django import forms
from django.contrib import admin

admin.site.register(Parameters)


class SwiperElementsInline(admin.TabularInline):
    model = SwiperElement
    extra = 1


class ProductListItemsInline(admin.TabularInline):
    model = ItemFromProductList
    extra = 1


@admin.register(Restaurant)
class CaseAdmin(admin.ModelAdmin):
    inlines = [SwiperElementsInline, ProductListItemsInline]


class PartnerAdminForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'

    def clean_image_icon(self):
        image = self.cleaned_data.get('image')
        if image:
            validate_image_or_vector(image)
        return image


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    form = PartnerAdminForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "image":
            kwargs["widget"] = forms.ClearableFileInput(attrs={"accept": "image/*"})
        return super().formfield_for_dbfield(db_field, **kwargs)
