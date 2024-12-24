from django.core.mail import send_mail
from django.conf import settings
from .models import SMTPSettings


def send_custom_email(subject, message, recipient_list):
    try:
        smtp_settings = SMTPSettings.objects.first()

        if not smtp_settings:
            raise Exception("SMTP settings are not configured.")

        settings.EMAIL_HOST = smtp_settings.smtp_host
        settings.EMAIL_PORT = smtp_settings.smtp_port
        settings.EMAIL_USE_TLS = smtp_settings.smtp_use_tls
        settings.EMAIL_HOST_USER = smtp_settings.smtp_user
        settings.EMAIL_HOST_PASSWORD = smtp_settings.smtp_password
        settings.DEFAULT_FROM_EMAIL = smtp_settings.smtp_user

        send_mail(
            subject,
            message,
            smtp_settings.smtp_user,
            recipient_list,
            fail_silently=False,
        )
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")
        raise e
