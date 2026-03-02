from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User


@receiver(post_save, sender=User)
def set_staff_for_superuser(sender, instance, **kwargs):
    if instance.is_superuser and not instance.is_staff:
        instance.is_staff = True
        instance.save(update_fields=['is_staff'])
