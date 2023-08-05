import pika

params = pika.URLParameters("amqps://yeuhviyy:NA5qJVEXTwsaptRMHZ0VRByfNzHn2OjS@beaver.rmq.cloudamqp.com/yeuhviyy")
connection = pika.BlockingConnection(params)
channel = connection.channel()


channel.exchange_declare("test_exchange")
channel.queue_declare(queue="test_queue")
channel.queue_bind("test_queue", "test_exchange", "catalog")


def publish(product_name):
    channel.basic_publish(exchange='test_exchange', routing_key='catalog', body=product_name)

    print("MESSAGE SENT")
