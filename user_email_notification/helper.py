import random
from django.conf import settings
from django.core.mail import send_mail
import os, django

#To communicate with django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_email_notification.settings")
django.setup()

def get_random_user_email():
    from users.models import User
    users = User.objects.all()
    random_user = random.choices(users)[0]
    return random_user.email

def fire_email(message):
    subject = "New product added"
    recipients  = [get_random_user_email()]
    print(f"Sending notification email to: {recipients}")
    return send_mail(subject, message, settings.EMAIL_SENDER, recipients)
