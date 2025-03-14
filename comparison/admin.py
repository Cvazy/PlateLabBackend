from django.contrib import admin
from .models import Comparison
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms


class ComparisonForm(forms.ModelForm):
    class Meta:
        model = Comparison
        fields = '__all__'
        widgets = {
            'price_per_photo': CKEditor5Widget(),
            'convenience_for_restaurants': CKEditor5Widget(),
            'style_and_customization': CKEditor5Widget(),
        }


class ComparisonAdmin(admin.ModelAdmin):
    form = ComparisonForm


admin.site.register(Comparison, ComparisonAdmin)
