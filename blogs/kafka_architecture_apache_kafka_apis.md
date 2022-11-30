
<div align="center">
    <h1>Kafka Architecture – Apache Kafka APIs</h1>
    <strong>Kafka Architecture – Apache Kafka APIs</strong>
</div>
<br/>

<!-- TOC -->

- [Kafka Architecture – Apache Kafka APIs](#kafka-architecture--apache-kafka-apis)
    - [Producer API](#producer-api)
    - [Consumer API](#consumer-api)
    - [Streams API](#streams-api)
    - [Connector API](#connector-api)
- [References:](#references)

<!-- /TOC -->

<img src="img/kafka_apis.png"  alt="Tech Stacks">
<br/>

# Kafka Architecture – Apache Kafka APIs
Apache Kafka Architecture has four core APIs, 
* Producer API
* Consumer API
* Streams API
* Connector API

**__Let’s discuss them one by one__**

## 1. Producer API
In order to publish a stream of records to one or more Kafka topics, the Producer API allows an application. 

## 2. Consumer API
This API permits an application to subscribe to one or more topics and also to process the stream of records produced to them.

## 3. Streams API
Moreover, to act as a stream processor, consuming an input stream from one or more topics and producing an output stream to one or more output topics, effectively transforming the input streams to output streams, the streams API permits an application.

## 4. Connector API
While it comes to building and running reusable producers or consumers that connect Kafka topics to existing applications or data systems, we use the Connector API. For example, a connector to a relational database might capture every change to a table.


# References:
* https://data-flair.training/blogs/kafka-architecture/