from django.db import models
from .constants import SMTP_HOST_CHOICES


class SMTPSettings(models.Model):
    smtp_host = models.CharField(max_length=255, choices=SMTP_HOST_CHOICES, default='smtp.yandex.ru')
    smtp_port = models.PositiveIntegerField(default=587)
    smtp_user = models.CharField(max_length=255)
    smtp_password = models.CharField(max_length=255)
    smtp_use_tls = models.BooleanField(default=True)
    admin_email = models.EmailField()

    def __str__(self):
        return f"SMTP Settings for {self.smtp_host}"

    class Meta:
        verbose_name = "SMTP Settings"
        verbose_name_plural = "SMTP Settings"
