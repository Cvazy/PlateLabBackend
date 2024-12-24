from django.contrib import admin
from .models import SMTPSettings


@admin.register(SMTPSettings)
class SMTPSettingsAdmin(admin.ModelAdmin):
    list_display = ('admin_email', 'smtp_user', 'smtp_host', 'smtp_port')
