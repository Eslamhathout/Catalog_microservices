from django.conf import settings
from django.core.mail import send_mail
from helper import get_random_user_email

class SendMail:
    def __init__(self):
        self.subject = 'New Product Added'

    def fire_message(self, message):
        recipients  = [get_random_user_email()]
        print(f"Sending notification email to: {recipients}")
        return send_mail(self.subject, message, settings.EMAIL_SENDER, recipients, fail_silently=False)
