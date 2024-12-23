from django.db import models
from django.core.validators import MinValueValidator


class Pricing(models.Model):
    min_photo_qnt = models.IntegerField(
        help_text="Minimum number of photos",
        validators=[MinValueValidator(1)]
    )
    max_photo_qnt = models.IntegerField(
        help_text="Maximum number of photos (leave blank if not applicable)",
        null=True,
        blank=True
    )
    price = models.IntegerField(
        help_text='Price per photo',
        validators=[MinValueValidator(1)],
        default=1
    )

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.max_photo_qnt is not None and self.min_photo_qnt > self.max_photo_qnt:
            raise ValidationError("Minimum number of photos cannot be greater than the maximum.")

    class Meta:
        verbose_name = "Pricing"

    def __str__(self):
        if self.max_photo_qnt is None:
            return f"{self.min_photo_qnt}+ photos"
        return f"{self.min_photo_qnt} - {self.max_photo_qnt} photos"
