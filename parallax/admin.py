from django.contrib import admin
from .models import *


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Parallax)
class ParallaxAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
