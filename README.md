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
  * [Create a Nginx Configuration](#create-a-nginx-configuration)
* [Blogs](#blogs)
  * [Blog 1: Starting, Stopping, and Reloading Configuration](#blog-1-starting-stopping-and-reloading-configuration)
  * [Blog 2: Configuration File’s Structure](#blog-2-configuration-files-structure)
  * [Blog 3: Setting Up a Simple Proxy Server](#blog-3-setting-up-a-simple-proxy-server)
  * [Blog 4: Setting Up FastCGI Proxying](#blog-4-setting-up-fastcgi-proxying)
  * [Blog 5: Configure SSL for Nginx Configuration](#blog-5-configure-ssl-for-nginx-configuration)
* [References](#references)
<!-- TOC -->

# Introduction

Nginx (pronounced "engine x") is a web server that can also be used as a reverse proxy, load balancer, mail proxy and
HTTP cache. The software was created by Russian developer Igor Sysoev and publicly released in 2004.Nginx is free and
open-source software, released under the terms of the 2-clause BSD license. A large fraction of web servers use Nginx,
often as a load balancer.

Application of Nginx

- Reverse Proxy
- Load balancer
- Mail Proxy
- HTTP Cache

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

Nginx configuration files are located in the `/etc/nginx` directory. The main configuration file is `nginx.conf`, which
includes other configuration files located in the `conf.d` directory.

Another way, you can get all the individual configuration file in `/etc/nginx/sites-available` and you will get
symbolic file for every active configuration in `/etc/nginx/sites-enabled/` directory.

```shell
$ sudo vi /etc/nginx/nginx.conf 
```

As we already mention our individual configuration file location `/etc/nginx/sites-available`. So now we need to create
a new configuration file for a subdomain `api.mapleshub.com` then the configuration file name would be
following `api.mapleshub.com.conf`.
> Note: There is no strict convention about filename convention, so we can write all configuration file in one file or
> we can separate it different file. But separate file technique will help you to organize more efficiently when you
> need to debug.

## Create a Nginx Configuration

Create a nginx configuration for `api.mapleshub.com.conf` and configuration will be used as reverse proxy
in `/etc/nginx/sites-available/api.mapleshub.com.conf` location.

```shell
server {
        listen 80;
        server_name api.mapleshub.com;

        client_body_buffer_size 200K;
        client_header_buffer_size 2k;
        client_max_body_size 100M;
        large_client_header_buffers 3 1k;

        client_body_timeout 5s;
        client_header_timeout 5s;

        location = /favicon.ico { access_log off; log_not_found off; }

        location /static {
                alias /fotonut/backend/staticfiles;
        }

        location /media {
                alias /fotonut/backend/media;
        }

        location / {
                include proxy_params;
                proxy_pass http://unix:/run/fnb.sock;
        }
}

```

> Note:This configuration file is for `Django` in production.

Create A symbolic file for the configuration file `api.mapleshub.com.conf`

```shell
$ ln -s /etc/nginx/sites-available/api.mapleshub.com.conf /etc/nginx/sites-enabled/
```

Verify our configuration file is valid or not

```shell
$ nginx -t
```

If everything goes well then reload the configuration file

```shell
$ nginx -s reload
```

Restart `nginx` for activating our configuration

```shell
$ systemctl restart nginx
```

# Blogs

## Blog 1: Starting, Stopping, and Reloading Configuration

To start nginx, run the executable file. Once nginx is started, it can be controlled by invoking the executable with the
-s parameter. Use the following syntax:

```shell 
nginx -s signal
```

Where signal may be one of the following:

- stop — fast shutdown
- quit — graceful shutdown
- reload — reloading the configuration file
- reopen — reopening the log files
  For example, to stop nginx processes with waiting for the worker processes to finish serving current requests, the
  following command can be executed:

```shell 
nginx -s quit
```

> This command should be executed under the same user that started nginx.

Changes made in the configuration file will not be applied until the command to reload configuration is sent to nginx or
it is restarted. To reload configuration, execute:

```shell 
nginx -s reload
```

Once the master process receives the signal to reload configuration, it checks the syntax validity of the new
configuration file and tries to apply the configuration provided in it. If this is a success, the master process starts
new worker processes and sends messages to old worker processes, requesting them to shut down. Otherwise, the master
process rolls back the changes and continues to work with the old configuration. Old worker processes, receiving a
command to shut down, stop accepting new connections and continue to service current requests until all such requests
are serviced. After that, the old worker processes exit.

A signal may also be sent to nginx processes with the help of Unix tools such as the kill utility. In this case a signal
is sent directly to a process with a given process ID. The process ID of the nginx master process is written, by
default, to the nginx.pid in the directory /usr/local/nginx/logs or /var/run. For example, if the master process ID is
1628, to send the QUIT signal resulting in nginx’s graceful shutdown, execute:

```shell 
kill -s QUIT 1628
```

For getting the list of all running nginx processes, the ps utility may be used, for example, in the following way:

```shell 
ps -ax | grep nginx
```

For more information on sending signals to nginx, see Controlling nginx.

## Blog 2: Configuration File’s Structure

An important web server task is serving out files (such as images or static HTML pages). You will implement an example
where, depending on the request, files will be served from different local directories: /data/www (which may contain
HTML files) and /data/images (containing images). This will require editing of the configuration file and setting up of
a server block inside the http block with two location blocks.

First, create the `/data/www` directory and put an index.html file with any text content into it and create
the `/data/images` directory and place some images in it.

Next, open the configuration file. The default configuration file already includes several examples of the server block,
mostly commented out. For now comment out all such blocks and start a new server block:

```shell
http {
    server {
    }
}
```

Generally, the configuration file may include several server blocks distinguished by ports on which they listen to and
by server names. Once nginx decides which server processes a request, it tests the URI specified in the request’s header
against the parameters of the location directives defined inside the server block.

Add the following location block to the server block:

```shell
location / {
    root /data/www;
}
```

This location block specifies the “/” prefix compared with the URI from the request. For matching requests, the URI will
be added to the path specified in the root directive, that is, to `/data/www`, to form the path to the requested file on
the local file system. If there are several matching location blocks nginx selects the one with the longest prefix. The
location block above provides the shortest prefix, of length one, and so only if all other location blocks fail to
provide a match, this block will be used.

Next, add the second location block:

```shell
location /images/ {
    root /data;
}
```

It will be a match for requests starting with `/images/` (location / also matches such requests, but has shorter
prefix).

The resulting configuration of the server block should look like this:

```shell
server {
    location / {
        root /data/www;
    }

    location /images/ {
        root /data;
    }
}
```

This is already a working configuration of a server that listens on the standard port 80 and is accessible on the local
machine at http://localhost/. In response to requests with URIs starting with /images/, the server will send files from
the /data/images directory. For example, in response to the http://localhost/images/example.png request nginx will send
the /data/images/example.png file. If such file does not exist, nginx will send a response indicating the 404 error.
Requests with URIs not starting with /images/ will be mapped onto the /data/www directory. For example, in response to
the http://localhost/some/example.html request nginx will send the /data/www/some/example.html file.

To apply the new configuration, start nginx if it is not yet started or send the reload signal to the nginx’s master
process, by executing:

```shell
nginx -s reload
```

In case something does not work as expected, you may try to find out the reason in `access.log` and `error.log` files in
the
directory `/usr/local/nginx/logs` or `/var/log/nginx`.

## Blog 3: Setting Up a Simple Proxy Server

One of the frequent uses of nginx is setting it up as a proxy server, which means a server that receives requests,
passes them to the proxied servers, retrieves responses from them, and sends them to the clients.

We will configure a basic proxy server, which serves requests of images with files from the local directory and sends
all other requests to a proxied server. In this example, both servers will be defined on a single nginx instance.

First, define the proxied server by adding one more server block to the nginx’s configuration file with the following
contents:

```shell
server {
    listen 8080;
    root /data/up1;

    location / {
    }
}
```

This will be a simple server that listens on the port 8080 (previously, the listen directive has not been specified
since the standard port 80 was used) and maps all requests to the `/data/up1` directory on the local file system. Create
this directory and put the index.html file into it. Note that the root directive is placed in the server context. Such
root directive is used when the location block selected for serving a request does not include its own root directive.

Next, use the server configuration from the previous section and modify it to make it a proxy server configuration. In
the first location block, put the `proxy_pas`s directive with the protocol, name and port of the proxied server
specified
in the parameter (in our case, it is http://localhost:8080):

```shell
server {
    location / {
        proxy_pass http://localhost:8080;
    }

    location /images/ {
        root /data;
    }
}
```

We will modify the second location block, which currently maps requests with the `/images/` prefix to the files under
the
`/data/images` directory, to make it match the requests of images with typical file extensions. The modified location
block looks like this:

```shell
location ~ \.(gif|jpg|png)$ {
    root /data/images;
}
```

The parameter is a regular expression matching all URIs ending with .gif, .jpg, or .png. A regular expression should be
preceded with ~. The corresponding requests will be mapped to the `/data/images` directory.

When nginx selects a location block to serve a request it first checks location directives that specify prefixes,
remembering location with the longest prefix, and then checks regular expressions. If there is a match with a regular
expression, nginx picks this location or, otherwise, it picks the one remembered earlier.

The resulting configuration of a proxy server will look like this:

```shell
server {
    location / {
        proxy_pass http://localhost:8080/;
    }

    location ~ \.(gif|jpg|png)$ {
        root /data/images;
    }
}
```

This server will filter requests ending with .gif, .jpg, or .png and map them to the `/data/images` directory (by adding
URI to the root directive’s parameter) and pass all other requests to the proxied server configured above.

To apply new configuration, send the reload signal to nginx as described in the previous sections.

There are many more directives that may be used to further configure a proxy connection.

## Blog 4: Setting Up FastCGI Proxying

nginx can be used to route requests to FastCGI servers which run applications built with various frameworks and
programming languages such as PHP.

The most basic nginx configuration to work with a FastCGI server includes using the `fastcgi_pass` directive instead of
the `proxy_pass` directive, and `fastcgi_param` directives to set parameters passed to a FastCGI server. Suppose the
FastCGI
server is accessible on `localhost:9000`. Taking the proxy configuration from the previous section as a basis, replace
the
proxy_pass directive with the fastcgi_pass directive and change the parameter to `localhost:9000`. In PHP, the
`SCRIPT_FILENAME` parameter is used for determining the script name, and the `QUERY_STRING` parameter is used to pass
request parameters. The resulting configuration would be:

```shell
server {
    location / {
        fastcgi_pass localhost:9000;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param QUERY_STRING $query_string;
    }
    location ~ \.(gif|jpg|png)$ {
        root /data/images;
    }
}
```

This will set up a server that will route all requests except for requests for static images to the proxied server
operating on localhost:9000 through the FastCGI protocol.

## Blog 5: Configure SSL for Nginx Configuration

To Configure a `ssl` certificate for free you may use `certbot`. Certbot can be available to install for free. To
install and configure `certbot` follow those commands

```shell
$ sudo apt-get update -y
$ sudo apt install snapd -y
$ sudo snap install core; snap refresh core
$ sudo snap install --classic certbot
$ sudo apt-get install python3-certbot-nginx -y
```

Configure `SSL` for `api.mapleshub.com.conf` configuration file which used for domain `api.mapleshub.com` using certbot

```shell
$ sudo certbot --nginx -d api.mapleshub.com --noninteractive --agree-tos --email your_email_name@email_provider.com --redirect
```

Automatic SSL certificate renewal crontab job

Open crontab with following command:

```shell
$ sudo crontab -e
```

Add the following line to the end of the file:

```shell
$ 30 4 1 * * sudo cerbot renew --quiet
```

# References
- https://nginx.org/en/docs/beginners_guide.html
- https://tecadmin.net/installing-nginx-on-linux

