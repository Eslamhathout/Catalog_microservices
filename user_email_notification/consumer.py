import pika
from helper import fire_email
from decouple import config


url = config("MQ_URL", "your mq URL")
params = pika.URLParameters(url)
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
