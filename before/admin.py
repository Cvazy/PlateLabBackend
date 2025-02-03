from django.contrib import admin
from .models import *

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
