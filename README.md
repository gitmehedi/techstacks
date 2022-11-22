<div align="center">
    <img src="blogs/img/logo.png" height="320" width="830" alt="Tech Stacks">
    <h1>Tech Stacks</h1>
    <strong>A tech stack is the combination of technologies a company uses to build and run an application or project.</strong>
</div>

<br/>    


<!-- TOC -->

- [Introduction](#introduction)
- [Installation](#installation)
    - [Ubuntu](#ubuntu)
        - [Prerequisite](#prerequisite)
    - [Docker](#docker)
        - [Prerequisite](#prerequisite)
- [Tutorials](#tutorials)
    - [1. Set Default Credentials for Git](#1-set-default-credentials-for-git)
- [References:](#references)

<!-- /TOC -->

## Introduction
[Kafka](https://kafka.apache.org/) Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.

## Installation
[Kafka installation](https://kafka.apache.org/quickstart) depends on operating system like linux,ubuntu,mac,windows. We will installing in major os.


### Ubuntu
You will need an Ubuntu 20.04 server with a non-root superuser account. And following command

#### Prerequisite
* Ubuntu 20.04
* [Java 8 /Java 11](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-20-04)  


**STEP 1: GET KAFKA**  
First, download and extract the kafka version
```bash
$ wget https://dlcdn.apache.org/kafka/3.3.1/kafka_2.13-3.3.1.tgz
$ tar -xzf kafka_2.13-3.3.1.tgz
$ cd kafka_2.13-3.3.1
```

**STEP 2: START THE KAFKA ENVIRONMENT**  
Apache Kafka can be started using ZooKeeper 

Kafka with ZooKeeper

```bash
# Start the ZooKeeper service
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```

Open another terminal session and run:
```bash
# Start the Kafka broker service
$ bin/kafka-server-start.sh config/server.properties
```

### Docker
#### Prerequisite
* Ubuntu 20.04
* [Docker](https://docs.docker.com/desktop/install/ubuntu/)
* [Docker Composer](https://docs.docker.com/desktop/install/ubuntu/)

Run docker compose command to run kafka
```bash
$ docker compose -f zk_kafka.yaml -d
```

## Tutorials
### [1. Set Default Credentials for Git](blogs/set_default_credentials_for_git.md)



## References:
* https://kafka.apache.org/
* https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-20-04
* https://www.conduktor.io/kafka/how-to-start-kafka-using-docker
* https://github.com/conduktor/kafka-stack-docker-compose
* https://github.com/confluentinc/examples
* https://docs.confluent.io/platform/current/platform-quickstart.html#ce-docker-quickstart
* https://raw.githubusercontent.com/confluentinc/cp-all-in-one/7.3.0-post/cp-all-in-one/docker-compose.yml
* https://docs.confluent.io/platform/current/platform-quickstart.html#ce-docker-quickstart
