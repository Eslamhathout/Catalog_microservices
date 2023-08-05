import pika
from decouple import config


url = config("MQ_URL", "your mq URL")
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()


channel.exchange_declare("test_exchange")
channel.queue_declare(queue="test_queue")
channel.queue_bind("test_queue", "test_exchange", "catalog")


def publish(product_name):
    channel.basic_publish(exchange='test_exchange', routing_key='catalog', body=product_name)

    print("MESSAGE SENT")
