from django.db import models


class Gallery(models.Model):
    description = models.CharField(max_length=255, help_text="Object description")
    image = models.ImageField(upload_to='images/', help_text="Object image")

    class Meta:
        verbose_name = 'Gallery'

    def __str__(self):
        return self.description[:50]