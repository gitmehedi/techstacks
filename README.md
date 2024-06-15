<div align="center">
    <img src="img/logo.jpg" height="320" width="830" alt="Tech Stacks">
    <h1>Django</h1>
    <strong>Django is a free and open-source, Python-based web framework that follows the model–template–views architectural pattern.</strong>
</div>

<!-- TOC -->
* [Introduction](#introduction)
* [Installation](#installation)
  * [Ubuntu](#ubuntu)
  * [Docker](#docker)
  * [Kubernetes](#kubernetes)
* [Django Documentation](#django-documentation)
  * [1. Getting Started](#1-getting-started)
    * [Creating a Project](#creating-a-project)
    * [The Development Server](#the-development-server)
    * [Creating the App](#creating-the-app)
    * [Database Setup](#database-setup)
* [Blogs](#blogs)
  * [1. Django User Authentication](#1-django-user-authentication)
    * [Create a new User](#create-a-new-user)
    * [Create a superuser](#create-a-superuser)
    * [Changing passwords](#changing-passwords)
    * [Authenticating a User](#authenticating-a-user)
    * [Logout a User](#logout-a-user)
    * [References](#references)
  * [2. User Permission Model](#2-user-permission-model)
    * [Permission Model Fields](#permission-model-fields)
    * [Assigning Permissions to Users](#assigning-permissions-to-users)
    * [Checking the User Permissions](#checking-the-user-permissions)
    * [Set Permission in Views](#set-permission-in-views)
    * [Set Custom Permission](#set-custom-permission)
  * [3. User Group Model](#3-user-group-model)
    * [Group Models Fields](#group-models-fields)
    * [Creating a Group](#creating-a-group)
    * [Assigning Permissions to a Group](#assigning-permissions-to-a-group)
    * [Adding Users to a Group](#adding-users-to-a-group)
    * [Checking Group Membership](#checking-group-membership)
  * [4. AbstractUser Model](#4-abstractuser-model)
    * [AbstractUser Model Fields](#abstractuser-model-fields)
    * [Extending the AbstractUser Model](#extending-the-abstractuser-model)
  * [5. Deploy Django Application in Production](#5-deploy-django-application-in-production)
    * [Prerequisite](#prerequisite)
    * [Installation and Configuration](#installation-and-configuration)
* [Django Site Documentation](#django-site-documentation)
  * [2. The Model Layer](#2-the-model-layer)
  * [3. The View Layer](#3-the-view-layer)
  * [4. The Template Layer()](#4-the-template-layer--)
  * [5. Forms](#5-forms)
  * [6. The Development Process](#6-the-development-process)
  * [7. The Admin](#7-the-admin)
  * [8. Security](#8-security)
  * [9. Internationalization and Localization](#9-internationalization-and-localization)
  * [10. Performance and Optimization](#10-performance-and-optimization)
  * [11. Geographic Framework](#11-geographic-framework)
  * [12. Common Web Application Tools](#12-common-web-application-tools)
  * [13. Other Core Functionalities](#13-other-core-functionalities)
  * [14. The Django Open-source Project](#14-the-django-open-source-project)
* [References](#references-1)
<!-- TOC -->

# Introduction

# Installation

Depending on operating system [Django Installation](https://www.djangoproject.com/download/) varies process.

## Ubuntu

Install on ubuntu

```bash
$ pip install Django==4.1.4
```

## Docker

```bash
$ docker run --name some-django-app -p 8000:8000 -d my-django-app
```

## Kubernetes

# Django Documentation

## 1. Getting Started

Check Python Version

```bash
$ python --version
> Python 3.10.6
```

Check Django Version

```bash
$ python -m django --version
> 4.0
```

### Creating a Project

```bash
$ django-admin startproject mysite
```

```html
mysite/
manage.py
mysite/
__init__.py
settings.py
urls.py
asgi.py
wsgi.py
```

> Changing the port  
> $ python manage.py runserver 8080

### The Development Server

```bash
$ python manage.py runserver
```

### Creating the App

```bash
$ python manage.py startapp polls
```

```html
polls/
__init__.py
admin.py
apps.py
migrations/
__init__.py
models.py
tests.py
views.py
```

**_Projects vs. apps_**
> What’s the difference between a project and an app? An app is a web application that does
> something – e.g., a blog system, a database of public records or a small poll app.
> A project is a collection of configuration and apps for a particular website.
> A project can contain multiple apps. An app can be in multiple projects.

### Database Setup

Create a database in postgresql

```bash
$ psql -h <hostname> -p <port> -U <database_username> -d <database_name>
> psql -h localhost -p 5432 -U odoo -d DJANGO_BLOG
```

# Blogs

## 1. Django User Authentication

In django, the user model is a built-in feature provided by `django.contrib.auth` that handles
user functionality

- `authentication`
- `authorization`
- `login`
- `logout`
- `create_user`
- `User`

The default `User` Model provided by Django has several fields which store user information. You can create custom user
model if the default user model doesn't meet your requirements.
User models contains several fields

- username
- password
- email
- first_name
- last_name
- is_active
- is_staff
- is_superuser
- last_login
- date_joined

Function we can do with django user model

### Create a new User

Django user model `User` can create new user or singup for new user

```shell
from django.contrib.auth import models

# create new user or signup new user
user = models.User.Objects.create_user({
  username= 'john',
  email= 'john@email.com',
  password= 'complex_password',
})

# Accessing user fields
print(user.username)
print(user.email)
print(user.is_active)
```

### Create a superuser

To create a superuser in django, commandline instruction is more used than functional creation

```shell
# regular user creation command
$ python manage.py createsuper

# specify username and email 
$ python manage.py createsuperuser --username=joe --email=joe@example.com
```

> Note: Before run superuser command, activate virtual environment for this project

### Changing passwords

Django provides `set_password()` for changing the password programmatically

```shell
from django.contrib.auth.models import User

def password_change_view(request):
    user = User.objects.get(username="john")
    user.set_password('new password')
    user.save()
```

### Authenticating a User

After signup or creating a new user, authentication is first step to login in the system
To implement authentication following steps are necessary

```shell
from django.contrib.auth import authentication,login

def authentication_view(reuqest):
    username = request.POST['username']
    password = request.POST['password']
    
    user = authentication(request,username=username,password=password)
    
    if user is not None:
        login(request,user)
        # Redirect to a successful page
    else:
        # Return an invalid login error message
```

### Logout a User

Django provides a logout function for logout from django application

```shell
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page
```

### References

- https://docs.djangoproject.com/en/5.0/topics/auth/default/#user-objects

## 2. User Permission Model

Django permission system is designed to manage user access control by defining what users can and can't do. It is built
into the `django.contrib.auth` framework and works along with `user` and `group` model. Permission can be assigned to
individual `users` or `group` of users

### Permission Model Fields

Following fields are available in permission model

- name: A human readable name for the permission.
- codename: A unique identifier for the permission.
- content-type: Links the permission to a specific model.

### Assigning Permissions to Users

You can assign permission to users directly using the `user_permissions` attribute

```shell
from django.contrib.auth import User,Permission

# get a user
user = User.Objects.get(username='john')

# assign the permission to the user
permission = Permission.Objects.get(codename='can_publish')
user.user_permissions.add(permission)
```

### Checking the User Permissions

Check if a user has a specific permission using the  `has_perm` method

```shell
if user.has_perm('blog.can_publish'):
    print("User has the permission")
else:
    print("User does not have the permission")
```

### Set Permission in Views

You can use the `permission_required` decorator to restrict access to views based on permissions.

```shell
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('blog.can_publish', raise_exception=True)
def permission_view(request):
    return render(request, 'permission_template.html')
```

### Set Custom Permission

If the default permissions(`add, change, delete, view`) are not sufficient, you can define custom permissions are in
your models.

```shell
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        permission = [
          ('can_publish','Can Publish'),
          ('can_view_statistics','Can View Statistics'),
        ]
```

## 3. User Group Model

In Django, the Group model is part of the `django.contrib.auth` module and is used group users and manage permissions
collectively. By assigning permission to a group, you can manage what `users` within that group can or can't do without
having to set permissions individually for each user.

### Group Models Fields

- name: The name of the Group
- permissions: The permission assign to a group. Each permission specifies what actions members of the group can
  perform.

### Creating a Group

You can create a group using the Django admin interface or using this code

```shell
from django.contrib.auth import Group

# create a new group
editors_group = Group.objects.create(name='Editors')
```

### Assigning Permissions to a Group

Permissions can be assigned to a group, allowing all users in that group to inherit those permissions.

```shell
from django.contrib.auth.models import Group, Permissions

# create a new group
editors_group = Groups.objects.create(name='Editors')

# get the permission
permission = Permissions.objects.get(codename='can_publish')

# assign the permission to the group
editors_group.permission.add(permission)
```

### Adding Users to a Group

Users can be added to groups, and they will inherit all permissions assigned to the group.

```shell
from django.contrib.auth.models import Group,Users,Permission

# create a new group
editors_group = Group.objects.create(name='Editors')

# get a user
user = User.objects.create(name='john')

# add the user to the group
editors_group.user_set.add(user)
```

### Checking Group Membership

You can check if a user is part of a group

```shell
from django.shortcuts import render

def my_view(request):
    if request.user.group.filter(name='Editors').exists():
        print("User is an editor")
    else:
        print("User is not a editor")
    
    return render(request, "index.html")
```

## 4. AbstractUser Model

AbstractUser is base class provided by Django for creating custom user models. This class is useful when you want to
extend the default user model by adding extra fields or methods, rather than starting from scratch.

### AbstractUser Model Fields

This AbstractUser Model include various fields

- username
- first_name
- last_name
- email
- password
- is_staff
- is_active
- is_superuser
- last_login
- date_joined

### Extending the AbstractUser Model

1. Define the Custom User model in `models.py`

```shell
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharFeild(max_length=15, blank=True)
    address = models.CharFeild(max_length=225, blank=True)
    
    def __str__(self):
        return self.username
```

2. In your settings, specify the custom user model by setting AUTH_USER_MODEL

```shell
AUTH_USER_MODEL = 'myapp.CustomUser'
```

3. Create and Apply Migrations

```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

4. Create a custom admin class to handle the custom user model in the admin interface.

```shell
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .model import CustomUser

@admin.register(CustomUser):
class CustomUserAdmin(UserAdmin):
    model= CustomUser
    fieldsets = UserAdmin.fieldsets + (
      (None, {'fields': ('phone_number','address')})
    )
    fieldsets = UserAdmin.add_fieldsets + (
      (None, {'fields': ('phone_number','address')})
    )
    list_display = ['username','email','first_name','last_name','is_staff','phone_number','address']
```

## 5. Deploy Django Application in Production

Development of Django application with default settings helps developer for faster development with proper `debug`
message. But in production it will helps unwanted user with inside information and regular user will annoyed due to
unnecessary information.

So deploy application in production has some major prerequisite and instruction to follow

### Prerequisite

- Ubuntu/Linux
- Python (3.12)
- Django 5.0 LTS
- PostgresSQL 14.0
- Nginx
- Certbot

> Note: Version mentioned with software are changed according to time and dependency.

### Installation and Configuration

<h3> Install Ubuntu/Linux </h3>

Choose VM or provider to install desired Ubuntu version

```shell
$ apt update -y
$ lsb_release -a
```

<h3> Install Python and Virtual Environment </h3>

Install Python in OS

```shell
$ apt update -y
```

Install Virtual Environment and configure it

```shell
# install virtual environment package for ubuntu
$ sudo apt-get install -y python3-venv

# create virtual environment to your desired location
$ python3 -m venv /path/<folder_name>

# activate virtual environment for project
$ source /path/<folder_name>/bin/activate
```

<h3> Install Django </h3>
Django is python based web application framework which is in the latest version Django==5.0. It also need to install in virtual environment.

```shell
$ pip install Django==5.0
```

<h3> Install PostgresSQL </h3>
PostgreSQL version 14.0

```shell
$ sudo apt-get install postgresql@14
```

<h3> Install NGINX </h3>

```shell
$ apt-get update -y
$ apt-get install nginx -y
```

<h3>Install Certbot</h3>

To install Certbot it also depends on several package and configuration, which are given in details

```shell
$ sudo apt-get update -y
$ sudo apt install snapd -y
$ sudo snap install core; snap refresh core
$ sudo snap install --classic certbot
$ sudo apt-get install python3-certbot-nginx -y
```

Configure Nginx and Certbot

Create a nginx file for FotoNut domain in /etc/nginx/sites-available/api.apps.conf and content of the file will be

```nginx configuration
server {
        listen 80;
        server_name fnb.leanmonk.com;

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

Create a symbolic link for FotoNut application using ln

```shell
# create symbolic link
$ ln -s /etc/nginx/sites-available/fnb.fotonut.conf /etc/nginx/sites-enabled/fnb.fotonut.conf

# check configuration link
$ nginx -t

# reload nginx configuration
$ nginx -s reload

# restart nginx for impose all changed configuration
$ systemctl restart nginx
```

Configure SSL for FotoNut application using certbot

```shell
$ sudo certbot --nginx -d fnb.leanmonk.com --noninteractive --agree-tos --email info.fotonut@fotonut.com --redirect
```

Automatic SSL certificate renewal crontab job

```shell
$ sudo crontab -e

# Add the following line to the end of the file:
30 4 1 * * sudo cerbot renew --quiet
```

# Django Site Documentation

## 2. [The Model Layer](https://docs.djangoproject.com/en/4.2/#the-model-layer)

- Models: Introduction to models | Field types | Indexes | Meta options | Model class
- QuerySets: Making queries | QuerySet method reference | Lookup expressions
- Model instances: Instance methods | Accessing related objects
- Migrations: Introduction to Migrations | Operations reference | SchemaEditor | Writing migrations
- Advanced: Managers | Raw SQL | Transactions | Aggregation | Search | Custom fields | Multiple databases | Custom
  lookups | Query Expressions | Conditional Expressions | Database Functions
- Other: Supported databases | Legacy databases | Providing initial data | Optimize database access | PostgreSQL
  specific features

## 3. [The View Layer](https://docs.djangoproject.com/en/4.2/#the-view-layer)

- The basics: URLconfs | View functions | Shortcuts | Decorators | Asynchronous Support
- Reference: Built-in Views | Request/response objects | TemplateResponse objects
- File uploads: Overview | File objects | Storage API | Managing files | Custom storage
- Class-based views: Overview | Built-in display views | Built-in editing views | Using mixins | API reference |
  Flattened index
- Advanced: Generating CSV | Generating PDF
- Middleware: Overview | Built-in middleware classes

## 4. [The Template Layer()](https://docs.djangoproject.com/en/4.2/#the-template-layer)

- The basics: Overview
- For designers: Language overview | Built-in tags and filters | Humanization
- For programmers: Template API | Custom tags and filters | Custom template backend

## 5. [Forms](https://docs.djangoproject.com/en/4.2/#forms)

- The basics: Overview | Form API | Built-in fields | Built-in widgets
- Advanced: Forms for models | Integrating media | Formsets | Customizing validation

## 6. [The Development Process](https://docs.djangoproject.com/en/4.2/#the-development-process)

- Settings: Overview | Full list of settings
- Applications: Overview
- Exceptions: Overview
- django-admin and manage.py: Overview | Adding custom commands
- Testing: Introduction | Writing and running tests | Included testing tools | Advanced topics
- Deployment: Overview | WSGI servers | ASGI servers | Deploying static files | Tracking code errors by email |
  Deployment checklist

## 7. [The Admin](https://docs.djangoproject.com/en/4.2/#the-admin)

- Admin site
- Admin actions
- Admin documentation generator

## 8. [Security](https://docs.djangoproject.com/en/4.2/#security)

- Security overview
- Disclosed security issues in Django
- Clickjacking protection
- Cross Site Request Forgery protection
- Cryptographic signing
- Security Middleware

## 9. [Internationalization and Localization](https://docs.djangoproject.com/en/4.2/#performance-and-optimization)

- Overview | Internationalization | Localization | Localized web UI formatting and form input
- Time zones

## 10. [Performance and Optimization](https://docs.djangoproject.com/en/4.2/#performance-and-optimization)

- Performance and optimization overview

## 11. [Geographic Framework](https://docs.djangoproject.com/en/4.2/#geographic-framework)

- GeoDjango intends to be a world-class geographic web framework. Its goal is to make it as easy as possible to build
  GIS web applications and harness the power of spatially enabled data.

## 12. [Common Web Application Tools](https://docs.djangoproject.com/en/4.2/#common-web-application-tools)

- Authentication: Overview | Using the authentication system | Password management | Customizing authentication | API
  Reference
- Caching
- Logging
- Sending emails
- Syndication feeds (RSS/Atom)
- Pagination
- Messages framework
- Serialization
- Sessions
- Sitemaps
- Static files management
- Data validation

## 13. [Other Core Functionalities](https://docs.djangoproject.com/en/4.2/#other-core-functionalities)

- Conditional content processing
- Content types and generic relations
- Flatpages
- Redirects
- Signals
- System check framework
- The sites framework
- Unicode in Django

## 14. [The Django Open-source Project](https://docs.djangoproject.com/en/4.2/#the-django-open-source-project)

- Community: How to get involved | The release process | Team organization | The Django source code repository |
  Security policies | Mailing lists
- Design philosophies: Overview
- Documentation: About this documentation
- Third-party distributions: Overview
- Django over time: API stability | Release notes and upgrading instructions | Deprecation Timeline

# References

- https://docs.djangoproject.com/en/4.0/
- https://docs.djangoproject.com/en/4.0/contents/


