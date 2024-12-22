from django.db import models


class Gallery(models.Model):
    description = models.CharField(max_length=255, help_text="Описание объекта")
    image = models.ImageField(upload_to='images/', help_text="Изображение объекта")

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Изображения из галереии'

    def __str__(self):
        return self.description[:50]