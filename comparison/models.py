from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Comparison(models.Model):
    title = models.CharField(max_length=128, verbose_name="Title")
    photo_for_difference = models.ImageField(
        upload_to='images/difference',
        help_text="Photos for differences. Important! Upload png images for background transparency"
    )
    price_per_photo = CKEditor5Field(verbose_name="Price per Photo")
    convenience_for_restaurants = CKEditor5Field(verbose_name="Convenience for Restaurants")
    style_and_customization = CKEditor5Field(verbose_name="Style & Customization")

    class Meta:
        verbose_name = 'Comparison'

    def __str__(self):
        return self.title
