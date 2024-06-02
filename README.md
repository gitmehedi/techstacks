<div align="center">
    <img src="img/logo.jpeg" height="320" width="830" alt="Nginx Logo">
    <h1>NGINX</h1>
    <strong>Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.</strong>
</div>

<!-- TOC -->
* [Introduction](#introduction)
* [Installation](#installation)
  * [Prerequisites](#prerequisites)
  * [Steps of Installation](#steps-of-installation)
    * [Step 1: Update System](#step-1-update-system)
    * [Step 2: Install Nginx](#step-2-install-nginx)
    * [Step 3: Verify Nginx Installation](#step-3-verify-nginx-installation)
    * [Step 4: Start and Enable Nginx Service](#step-4-start-and-enable-nginx-service)
    * [Step 5: Configure Firewall](#step-5-configure-firewall)
    * [Step 6: Manage Nginx Process](#step-6-manage-nginx-process)
* [Configuration](#configuration)
* [Blogs](#blogs)
* [Questions](#questions)
* [References](#references)
<!-- TOC -->

# Introduction

Nginx (pronounced "engine x") is a web server that can also be used as a reverse proxy, load balancer, mail proxy and
HTTP cache. The software was created by Russian developer Igor Sysoev and publicly released in 2004.Nginx is free and
open-source software, released under the terms of the 2-clause BSD license. A large fraction of web servers use Nginx,
often as a load balancer.

> note: for more information you can check in here (<https://en.wikipedia.org/wiki/Nginx>)

# Installation

Nginx is wide used in technology world, so there every corner and operating system has provision to install nginx in
their system. But for wide use of Linux as a server we also implement the process in Linux

## Prerequisites

- Linux (Ubuntu 22.04)
- Root Access

## Steps of Installation

### Step 1: Update System

Before installing Nginx, it is recommended that you update your system to ensure that all the packages are up to date.

For debian-based systems

```shell
$ sudo apt-get update -y
```

For RHEL-based system

```shell
$ sudo yum update -y
```

### Step 2: Install Nginx

Once the system is updated, the next step is to install Nginx.

For Debian/Ubuntu, run:

```shell
$ sudo apt-get install nginx -y
```

For Debian/Ubuntu, run

```shell
$ sudo yum install nginx -y
```

### Step 3: Verify Nginx Installation

To verify that Nginx has been installed correctly, check its version.

```shell
$ nginx -v

# Output 
nginx version: nginx/1.18.0 (Ubuntu)
```

### Step 4: Start and Enable Nginx Service

Start the Nginx service and enable it to start up at system boot.

```shell
$ sudo systemctl start nginx 
$ sudo systemctl enable nginx 
```

### Step 5: Configure Firewall

If you’re using a firewall, you need to allow connections to Nginx.

On Ubuntu/Debian with UFW, run

```shell
$ sudo ufw allow 'Nginx HTTP' 
$ sudo ufw reload 
```

On CentOS/RHEL with firewalld, use

```shell
$ sudo firewall-cmd --permanent --zone=public --add-service=http 
$ sudo firewall-cmd --reload 
```

### Step 6: Manage Nginx Process

To stop your web server:

```shell
$ sudo systemctl stop nginx 
```

To start the web server when it is stopped:

```shell
$ sudo systemctl start nginx 
```

To restart the service:

```shell
$ sudo systemctl restart nginx 
```

To reload Nginx without dropping connections (useful for configuration changes):

```shell
$ sudo systemctl reload nginx 
```

By default, Nginx is set to start automatically when the server boots. To disable this behavior:

```shell
$ sudo systemctl disable nginx 
```

To re-enable the service to start up at boot:

```shell
$ sudo systemctl enable nginx 
```

# Configuration

# Blogs

# Questions

# References

- <https://nginx.org/en/docs/beginners_guide.html>
