from django.db import models
import mimetypes
from django.core.exceptions import ValidationError


class Footer(models.Model):
    title = models.CharField(max_length=255, help_text="Footer title")
    description = models.CharField(max_length=255, help_text="Footer description")

    class Meta:
        verbose_name = "Footer Information"

    def __str__(self):
        return self.title


def validate_image_or_vector(file):
    mime_type, _ = mimetypes.guess_type(file.name)
    allowed_mime_types = [
        'image/jpeg', 'image/png', 'image/gif', 'image/svg+xml'
    ]
    if mime_type not in allowed_mime_types:
        raise ValidationError(f'Unsupported file type: {mime_type}. Allowed types are JPEG, PNG, GIF, and SVG.')


class Network(models.Model):
    name = models.CharField(max_length=255, help_text="Network name")
    link = models.CharField(max_length=255, help_text="Network link")
    image_icon = models.FileField(
        upload_to='images/networks',
        help_text="Network icon",
        validators=[validate_image_or_vector]
    )

    class Meta:
        verbose_name = "Network"

    def __str__(self):
        return self.name
