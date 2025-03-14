import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Comparison


@receiver(post_delete, sender=Comparison)
def delete_image(sender, instance, **kwargs):
    if instance.photo_for_difference:
        image_path = instance.photo_for_difference.path
        if os.path.exists(image_path):
            os.remove(image_path)
