# periodic.py
# from apps.dashboard.task import send_notifiction
from __future__ import absolute_import, unicode_literals
from datetime import datetime
# from celery.task import task
from celery import shared_task
from celery.app.base import app_has_custom
from django.http.response import HttpResponse 
from django.core.mail import send_mail
from django.conf import settings
from celery import Celery
from django.apps import apps


app = Celery('task', broker="redis://localhost:6379/0")

# @app.task
# def see_you():
#     print("I am  poonam!")


# app.conf.beat_schedule = {
#     "run-in-5-seconds-task": {
#         "task": "task.see_you",
#         "schedule": 5.0
#     }
# }


@shared_task
def asset_create_mail():
    subject = f'Regarding Asset Added'
    message = f'Hi , New Asset Added to Techbox'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['poornima.thoughtwin@gmail.com',]
    send_mail( subject, message, email_from, recipient_list,fail_silently=False,)


