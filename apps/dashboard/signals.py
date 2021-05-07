from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Asset,AssetAssign,Employee
from django.core.mail import send_mail
from django.conf import settings
from apps.dashboard.task import asset_create_mail

@receiver(post_save, sender=Asset) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        asset_create_mail()
     


@receiver(post_save, sender=AssetAssign) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        asset_create_mail()
     

#......................................................................................



