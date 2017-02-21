from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class PostSaveCalled(Exception):
    pass


class CustomModel(models.Model):
    class Meta:
        app_label = 'tests'


@receiver(post_save, sender=CustomModel)
def raise_exception(*args, **kwargs):
    raise PostSaveCalled()
