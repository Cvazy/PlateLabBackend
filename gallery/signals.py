import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Gallery


@receiver(post_delete, sender=Gallery)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        image_path = instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
