from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=255, help_text="About us title")
    description = models.CharField(max_length=255, help_text="About us description")

    class Meta:
        verbose_name = "About us"
        verbose_name_plural = "About us"

    def __str__(self):
        return self.title
