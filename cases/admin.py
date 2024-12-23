from django.contrib import admin
from .models import *


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
