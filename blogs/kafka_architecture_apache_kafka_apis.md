
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
- [References](#references)

<!-- /TOC -->

<img src="img/kafka_apis.png"  alt="Tech Stacks">
<br/>

# Kafka Architecture – Apache Kafka APIs
Apache Kafka Architecture has four core APIs, 
* [Producer API](#1-producer-api)
* [Consumer API](#2-consumer-api)
* [Streams API](#3-streams-api)
* [Connector API](#4-connector-api)

**__Let’s discuss them one by one__**

## 1. Producer API
In order to publish a stream of records to one or more Kafka topics, the Producer API allows an application. 

```bash
# Manually assign a list of TopicPartitions to this consumer.
assign(partitions)


# Get the TopicPartitions currently assigned to this consumer.
assignment()

# Get the first offset for the given partitions.
beginning_offsets(partitions)

# Return True if the bootstrap is connected.
bootstrap_connected()

close(autocommit=True)
# Close the consumer, waiting indefinitely for any needed cleanup.

# Commit offsets to kafka, blocking until success or error.
commit(offsets=None)

# Commit offsets to kafka asynchronously, optionally firing callback.
commit_async(offsets=None, callback=None)


# Get the last committed offset for the given partition.
committed(partition, metadata=False)

# Get the last offset for the given partitions. The last offset of a partition is the offset of the upcoming message, i.e. the offset of the last available message + 1.
end_offsets(partitions)

# Last known highwater offset for a partition.
highwater(partition)

# Get metrics on consumer performance.
metrics(raw=False)

# Look up the offsets for the given partitions by timestamp. The returned offset for each partition is the earliest offset whose timestamp is greater than or equal to the given timestamp in the corresponding partition.
offsets_for_times(timestamps)

# This method first checks the local metadata cache for information about the topic. If the topic is not found (either because the topic does not exist, the user is not authorized to view the topic, or the metadata cache is not populated), then it will issue a metadata update call to the cluster.
partitions_for_topic(topic)

# Suspend fetching from the requested partitions.
pause(*partitions)

Future calls to poll() will not return any records from these partitions until they have been resumed using resume().

Note: This method does not affect partition subscription. In particular, it does not cause a group rebalance when automatic assignment is used.


# Get the partitions that were previously paused using pause().
paused()

# Fetch data from assigned topics / partitions.
poll(timeout_ms=0, max_records=None, update_offsets=True)

# Get the offset of the next record that will be fetched
position(partition)

# Resume fetching from the specified (paused) partitions.
resume(*partitions)

# Manually specify the fetch offset for a TopicPartition.
seek(partition, offset)

seek_to_beginning(*partitions)
# Seek to the oldest available offset for partitions.

# Seek to the most recent available offset for partitions.
seek_to_end(*partitions)

# Subscribe to a list of topics, or a topic regex pattern.
subscribe(topics=(), pattern=None, listener=None)

# Get the current topic subscription.
subscription()

```

Read details about [Producer API](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html) for python.

## 2. Consumer API
This API permits an application to subscribe to one or more topics and also to process the stream of records produced to them.

```bash
# Manually assign a list of TopicPartitions to this consumer.
assign(partitions)

# Get the TopicPartitions currently assigned to this consumer.
assignment()

# Get the first offset for the given partitions.
beginning_offsets(partitions)

# Return True if the bootstrap is connected.
bootstrap_connected()

# Close the consumer, waiting indefinitely for any needed cleanup.
close(autocommit=True)

# Commit offsets to kafka, blocking until success or error.
commit(offsets=None)

# Commit offsets to kafka asynchronously, optionally firing callback.
commit_async(offsets=None, callback=None)

# Get the last committed offset for the given partition.
committed(partition, metadata=False)

# Get the last offset for the given partitions. The last offset of a partition is the offset of the 
# upcoming message, i.e. the offset of the last available message + 1.
end_offsets(partitions)

# Last known highwater offset for a partition.
highwater(partition)

# Get metrics on consumer performance.
metrics(raw=False)

# Look up the offsets for the given partitions by timestamp. 
# The returned offset for each partition is the earliest offset whose timestamp is greater than or 
# equal to the given timestamp in the corresponding partition.
offsets_for_times(timestamps)

# This method first checks the local metadata cache for information about the topic. 
# If the topic is not found (either because the topic does not exist, the user is not authorized to view the topic, 
# or the metadata cache is not populated), then it will issue a metadata update call to the cluster.
partitions_for_topic(topic)

# Suspend fetching from the requested partitions.
pause(*partitions)

# Get the partitions that were previously paused using pause().
paused()

# Fetch data from assigned topics / partitions.

# Records are fetched and returned in batches by topic-partition. On each poll, 
# consumer will try to use the last consumed offset as the starting offset and fetch sequentially. 
# The last consumed offset can be manually set through seek() or automatically set as the last committed 
# offset for the subscribed list of partitions.
poll(timeout_ms=0, max_records=None, update_offsets=True)

# Get the offset of the next record that will be fetched
position(partition)

# Resume fetching from the specified (paused) partitions.
resume(*partitions)

# Manually specify the fetch offset for a TopicPartition.
seek(partition, offset)

# Seek to the oldest available offset for partitions.
seek_to_beginning(*partitions)

# Seek to the most recent available offset for partitions.
seek_to_end(*partitions)

# Subscribe to a list of topics, or a topic regex pattern.
subscribe(topics=(), pattern=None, listener=None)

# Get the current topic subscription.
subscription()

# Get all topics the user is authorized to view. This will always issue a remote call to the cluster to fetch the latest information.
topics()


```

## 3. Streams API
Moreover, to act as a stream processor, consuming an input stream from one or more 
topics and producing an output stream to one or more output topics, effectively 
transforming the input streams to output streams, the streams API permits an application.

```bash

```

## 4. Connector API
While it comes to building and running reusable producers or consumers that connect Kafka topics to 
existing applications or data systems, we use the Connector API. For example, a connector to a relational 
database might capture every change to a table.

```bash
# Alter configuration parameters of one or more Kafka resources.
alter_configs(config_resources)

# Close the KafkaAdminClient connection to the Kafka broker.
close()

# Create a list of ACLs
create_acls(acls)

# Create additional partitions for an existing topic.
create_partitions(topic_partitions, timeout_ms=None, validate_only=False)

# Create new topics in the cluster.
create_topics(new_topics, timeout_ms=None, validate_only=False)

# Delete a set of ACLs
delete_acls(acl_filters)

# Delete topics from the cluster.
delete_topics(topics, timeout_ms=None)


# Describe a set of ACLs
describe_acls(acl_filter)

# Fetch configuration parameters for one or more Kafka resources.
describe_configs(config_resources, include_synonyms=False)

# Describe a set of consumer groups.
describe_consumer_groups(group_ids, group_coordinator_id=None, include_authorized_operations=False)

# Fetch Consumer Offsets for a single consumer group.
list_consumer_group_offsets(group_id, group_coordinator_id=None, partitions=None)

# List all consumer groups known to the cluster.
list_consumer_groups(broker_ids=None)


```

# References
* https://data-flair.training/blogs/kafka-architecture/
* https://kafka-python.readthedocs.io/en/master/apidoc/modules.html

