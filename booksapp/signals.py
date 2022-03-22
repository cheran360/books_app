from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string 
from django.utils.html import strip_tags
import requests

def send_mailer(instance):
    username = instance.username
    template = render_to_string('emailContent.html', {'username':username})
    text_content = strip_tags(template)

    email = EmailMultiAlternatives(
        "Booksapp",
        text_content,
        settings.EMAIL_HOST_USER,
        [instance.email]
    )
    email.attach_alternative(template, "text/html")

    email.fail_silently = False
    email.send()

@receiver(post_save, sender=Email)
def create_email(sender ,instance, created, **kwargs):
  send_mailer(instance)

@receiver(post_save, sender=Email)
def update_email(sender ,instance, created, **kwargs):

  if created == False:
    send_mailer(instance)