import pika
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'OK'


@app.route('/create-job/<msg>')
def add(msg):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")
        return 'None'

    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=msg,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))

    connection.close()
    return " ___ Sent: %s \n" % msg


@app.route('/publish-job/<msg>')
def add(msg):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")
        return 'None'

    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=msg
                          )

    connection.close()
    return " ___ Message Publish: %s \n" % msg


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
