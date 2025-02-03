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


class Banner(models.Model):
    description = models.CharField(max_length=255, help_text="Banner description")
    image = models.ImageField(
        upload_to='images/banners',
        help_text="Banner image",
    )

    class Meta:
        verbose_name = 'Banner'

    def __str__(self):
        return self.description[:50]


class Partner(models.Model):
    name = models.CharField(max_length=255, help_text="Partner name")
    image = models.FileField(
        upload_to='images/partners',
        help_text="Partner logo",
        validators=[validate_image_or_vector]
    )

    class Meta:
        verbose_name = 'Partner'

    def __str__(self):
        return self.name
