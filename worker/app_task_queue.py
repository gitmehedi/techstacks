import pika,time

print(' Connecting to server ...')

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
except pika.exceptions.AMQPConnectionError as exc:
    print("Failed to connect to RabbitMQ service. Message wont be sent.")

channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

print(' Waiting for messages...')


def callback(ch, method, properties, body):
    print(" Received %s" % body.decode())
    time.sleep(body.count(b'.'))
    print(" Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()