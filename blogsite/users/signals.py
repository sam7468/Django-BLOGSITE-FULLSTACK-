from django.db.models.signals import post_save #signal triggered when USer created
from django.contrib.auth.models import User #sender
from django.dispatch import receiver #receiver
from .models import Profile


@receiver(post_save, sender=User)
def createprofile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveprofile(sender,instance,**kwargs):
    instance.profile.save()