# RabbitMQ Documentations




## Introduction

RabbitMQ is a message broker. It accepts, stores, and forwards binary blobs of data ‒ messages.

RabbitMQ, and messaging in general, uses some jargon.  
* **Producer:** A program that sends messages is a producer.
* **Queue:** Messages flow through RabbitMQ and your applications, they can only be stored inside a queue. 
A queue is only bound by the host's memory & disk limits, it's essentially a large message buffer. Many producers can send messages that go to one queue, and many consumers can try to receive data from one queue.
* **Consumer:** A consumer is a program that mostly waits to receive messages.

### Producer
Steps to follow to send message to RabbitMQ Server
* Establish connection to rabbitMQ server
* Establish channel using connection references
* Declare a queue in RabbitMQ server (queue created only once)
* Publish message to declared queue through exchange
* Close RabbitMQ Server connection

Producer steps implemented using `python` language and using [`pika`](https://pika.readthedocs.io/en/stable/) recommended library
```bash
# establish connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# establish channel
channel = connection.channel()

# declare a message queue
channel.queue_declare(queue='hello')

# publish message through exchange
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

# close connection
connection.close()
```

### Consumer
Steps to follow in receive message from RabbitMQ Server

* Establish connection to rabbitMQ server
* Establish channel using connection references
* Declare a queue in RabbitMQ server (queue created only once)
* Declare a consume callback function to receive message
* Start message consuming process

Producer steps implemented using `python` language and using [`pika`](https://pika.readthedocs.io/en/stable/) recommended library

```bash
# establish connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# establish channel
channel = connection.channel()

# declare a message queue
channel.queue_declare(queue='hello')

# define callback function which was declared by consumer
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    
# declare callback function with message queue
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

# consuming process start
channel.start_consuming()
```

__**Note:**__ Until unless consumer receive messages it will stores on message queue.


## Work Queue (Task Queue)

This concept is especially useful in web applications where 
it's impossible to handle a complex task during a short HTTP request window.

### Round-robin Dispatching
RabbitMQ will send each message to the next consumer, in sequence. 
On average every consumer will get the same number of messages. 
This way of distributing messages is called round-robin.

### Message acknowledgment
RabbitMQ delivers message to the consumer, it immediately marks it for deletion. 
In this case, if you terminate a worker, the message it was just processing is lost. 
The messages that were dispatched to this particular worker but were not yet handled are also lost.

In order to make sure a message is never lost, RabbitMQ supports message acknowledgments. 
An ack(nowledgement) is sent back by the consumer to tell RabbitMQ that a particular message had been received, 
processed and that RabbitMQ is free to delete it.

### Message Durability
When RabbitMQ quits or crashes it will forget the queues and messages unless you tell it not to. 
Two things are required to make sure that messages aren't lost: we need to mark both the queue and 
messages as durable.

* First, we need to make sure that the queue will survive a RabbitMQ node restart. 
In order to do so, we need to declare it as durable `derable=True`:
```channel.queue_declare(queue='hello', durable=True)```  
This queue_declare change needs to be applied to both the producer and consumer code.

### Fair dispatch
RabbitMQ just dispatches a message when the message enters the queue. 
It doesn't look at the number of unacknowledged messages for a consumer. 
It just blindly dispatches every n-th message to the n-th consumer.

don't dispatch a new message to a worker until it has processed and acknowledged the previous one. 
Instead, it will dispatch it to the next worker that is not still busy.
```bash
channel.basic_qos(prefetch_count=1)
```

So now current producer and receiver will be 
```bash
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(" [x] Sent %r" % message)
connection.close()
```

And current worker will be 

```bash
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
```

__Note__: Using message acknowledgments and prefetch_count you can set up a work queue. The durability options let the tasks survive even if RabbitMQ is restarted.

## Publish and Subscribe

When a message send to multiple consumers, and multiple consume will 
receive the same message, this pattern is known as "publish/subscribe".

### Exchanges
So far we have learned how basic rabbitmq application works
* A producer is a user application that sends messages.
* A queue is a buffer that stores messages.
* A consumer is a user application that receives messages.

An exchange, receives message from producer and pushed those message to 
queue depending on rules for what are defined by the exchange type.  
There are few exchage types available
* Direct
* Topic
* Headers
* Fanout

Declare an exchange
```bash
channel.exchange_declare(exchange='logs', 
                         exchange_type='fanout')
```

If we rewrite our producer then it might be looks like below
```bash
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
```


