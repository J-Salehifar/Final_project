from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()