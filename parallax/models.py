from django.db import models


class Parallax(models.Model):
    up_title = models.CharField(max_length=200, verbose_name="Up Parallax Title text")
    down_title = models.CharField(max_length=200, verbose_name="Down Parallax Title text")
    image = models.ImageField(upload_to='images/parallax', verbose_name="Central Image For Magnification")

    class Meta:
        verbose_name = "Parallax"

    def __str__(self):
        return f"{self.up_title} {self.down_title}"


class Image(models.Model):
    album = models.ForeignKey(
        Parallax,
        on_delete=models.CASCADE,
        related_name='gallery',
        verbose_name="Parallax gallery"
    )
    image = models.ImageField(upload_to='images/parallax', verbose_name="Parallax Image")
    caption = models.CharField(max_length=200, blank=True, verbose_name="Parallax Image caption")

    class Meta:
        verbose_name = "Parallax image"

    def __str__(self):
        return f"Image in {self.album.up_title} {self.album.down_title} ({self.caption})"
