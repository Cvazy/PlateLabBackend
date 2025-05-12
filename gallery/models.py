from django.db import models


class Gallery(models.Model):
    description = models.CharField(max_length=255, help_text="Object description")
    image = models.ImageField(upload_to='images/', help_text="Object image")
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Gallery'
        ordering = ['order']

    def __str__(self):
        return self.description[:50]