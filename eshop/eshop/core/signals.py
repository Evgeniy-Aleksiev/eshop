from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from eshop.profiles.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):

    if created:
        if instance.is_superuser:
            instance.is_verified = True
            instance.save()

        profile = Profile(
            user=instance,
        )

        default_username = instance.email.split('@')[0]

        if Profile.objects.filter(username=default_username).exists():
            default_username += str(instance.pk)
        profile.username = default_username
        profile.save()
