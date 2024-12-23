from django.db import models


class Footer(models.Model):
    title = models.CharField(max_length=255, help_text="Footer title")
    description = models.CharField(max_length=255, help_text="Footer description")

    class Meta:
        verbose_name = "Footer Information"

    def __str__(self):
        return self.title


class Network(models.Model):
    name = models.CharField(max_length=255, help_text="Network name")
    link = models.CharField(max_length=255, help_text="Network link")
    image_icon = models.ImageField(upload_to='images/networks', help_text="Network icon")

    class Meta:
        verbose_name = "Network"

    def __str__(self):
        return self.name
