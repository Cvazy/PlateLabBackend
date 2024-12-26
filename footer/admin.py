from django.contrib import admin
from .models import *

from django import forms
from django.contrib import admin
from .models import Network


class NetworkAdminForm(forms.ModelForm):
    class Meta:
        model = Network
        fields = '__all__'

    def clean_image_icon(self):
        image_icon = self.cleaned_data.get('image_icon')
        if image_icon:
            validate_image_or_vector(image_icon)
        return image_icon


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    form = NetworkAdminForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "image_icon":
            kwargs["widget"] = forms.ClearableFileInput(attrs={"accept": "image/*"})
        return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Footer)
