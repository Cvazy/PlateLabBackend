from django.db import models


class Case(models.Model):
    restaurant_name = models.CharField(max_length=200, verbose_name="Restaurant Name")
    description = models.TextField(blank=True, verbose_name="Restaurant description")

    class Meta:
        verbose_name = "Case"

    def __str__(self):
        return self.restaurant_name


class Image(models.Model):
    album = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='images', verbose_name="Case")
    image = models.ImageField(upload_to='images/cases', verbose_name="Case image")
    caption = models.CharField(max_length=200, blank=True, verbose_name="Image caption")

    class Meta:
        verbose_name = "Case image"

    def __str__(self):
        return f"Image in {self.album.restaurant_name} ({self.caption})"
