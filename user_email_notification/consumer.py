import pika, os, django
from helper import fire_email

#To communicate with django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_email_notification.settings")
django.setup()

params = pika.URLParameters("amqps://yeuhviyy:NA5qJVEXTwsaptRMHZ0VRByfNzHn2OjS@beaver.rmq.cloudamqp.com/yeuhviyy")
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="test_queue")

def callback(ch, method, properties, body):
    print('Received in user notification. . . ')
    print(f'Message: {body.decode("utf-8")}')

    fire_email(body.decode("utf-8"))

channel.basic_consume('test_queue', callback, auto_ack=True)
print("Started consuming . . ")

channel.start_consuming()
channel.close()
