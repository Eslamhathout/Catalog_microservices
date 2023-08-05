import random
from users.models import User
from django.conf import settings
from django.core.mail import send_mail


def get_random_user_email():
    users = User.objects.all()
    random_user = random.choices(users)[0]
    return random_user.email

def fire_email(message):
    subject = "New product added"
    recipients  = [get_random_user_email()]
    print(f"Sending notification email to: {recipients}")
    return send_mail(subject, message, settings.EMAIL_SENDER, recipients)
