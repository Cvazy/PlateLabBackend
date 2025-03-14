from django.core.validators import MinValueValidator
from django.db import models
import mimetypes
from django.core.exceptions import ValidationError


def validate_image_or_vector(file):
    mime_type, _ = mimetypes.guess_type(file.name)
    allowed_mime_types = [
        'image/jpeg', 'image/png', 'image/gif', 'image/svg+xml'
    ]
    if mime_type not in allowed_mime_types:
        raise ValidationError(f'Unsupported file type: {mime_type}. Allowed types are JPEG, PNG, GIF, and SVG.')


class Parameters(models.Model):
    name = models.CharField(max_length=200, verbose_name="Parameter Name")
    start_value = models.PositiveIntegerField(
        help_text="Start parameter value",
        validators=[MinValueValidator(1)]
    )
    end_value = models.PositiveIntegerField(
        help_text="End parameter value",
        validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = "Parameter"

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=200, verbose_name="Restaurant Name")
    swiper_title = models.CharField(max_length=200, verbose_name="Restaurant Swiper Title")
    items_list_title = models.CharField(max_length=200, verbose_name="Restaurant Items List Title")

    class Meta:
        verbose_name = "Restaurant"

    def __str__(self):
        return self.name


class SwiperElement(models.Model):
    item = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='swiper_items',
        verbose_name="Swiper block elements"
    )
    item_name = models.CharField(max_length=200, verbose_name="Swiper Element Name")
    image = models.ImageField(upload_to='images/before/swiper', verbose_name="Swiper Element Image")
    caption = models.CharField(max_length=200, blank=True, verbose_name="Image caption")
    price = models.PositiveIntegerField(
        help_text="Item Price",
        validators=[MinValueValidator(0.1)]
    )
    min_cal_value = models.PositiveIntegerField(
        help_text="Minimum position Cal",
        validators=[MinValueValidator(1)]
    )
    max_cal_value = models.PositiveIntegerField(
        help_text="Maximum position Cal (leave blank if not applicable)",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Swiper Element"

    def __str__(self):
        return f"{self.item_name}"


class ItemFromProductList(models.Model):
    item = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='product_list_items',
        verbose_name="Item From Product List"
    )
    item_name = models.CharField(max_length=200, verbose_name="Product List Element Name")
    image = models.ImageField(upload_to='images/before/items_list', verbose_name="Product List Element Image")
    caption = models.CharField(max_length=200, blank=True, verbose_name="Image caption")
    price = models.PositiveIntegerField(
        help_text="Item Price",
        validators=[MinValueValidator(0.1)]
    )
    min_cal_value = models.PositiveIntegerField(
        help_text="Minimum position Cal",
        validators=[MinValueValidator(1)]
    )
    max_cal_value = models.PositiveIntegerField(
        help_text="Maximum position Cal (leave blank if not applicable)",
        null=True,
        blank=True
    )
    description = models.TextField(help_text="Item description")

    class Meta:
        verbose_name = "Item From The Product List"

    def __str__(self):
        return f"{self.item_name}"


class Partner(models.Model):
    name = models.CharField(max_length=255, help_text="Partner name")
    image = models.FileField(
        upload_to='images/before/partners',
        help_text="Partner logo",
        validators=[validate_image_or_vector]
    )

    class Meta:
        verbose_name = 'Partner'

    def __str__(self):
        return self.name
