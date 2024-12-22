from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Comparison(models.Model):
    title = models.CharField(max_length=128, verbose_name="Title")
    price_per_photo = CKEditor5Field(verbose_name="Price per Photo")
    convenience_for_restaurants = CKEditor5Field(verbose_name="Convenience for Restaurants")
    style_and_customization = CKEditor5Field(verbose_name="Style & Customization")
    consistency = CKEditor5Field(verbose_name="Consistency")
    adaptability_for_seasonal_menus = CKEditor5Field(verbose_name="Adaptability for Seasonal Menus")

    class Meta:
        verbose_name = 'Comparison'

    def __str__(self):
        return self.title
