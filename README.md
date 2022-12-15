<div align="center">
    <img src="img/logo.jpg" height="320" width="830" alt="Tech Stacks">
    <h1>Django</h1>
    <strong>Django is a free and open-source, Python-based web framework that follows the model–template–views architectural pattern.</strong>
</div>

<!-- TOC -->
* [Introduction](#introduction)
* [Installation](#installation)
* [References](#references)
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


## 2. The Model Layer
- Models: Introduction to models | Field types | Indexes | Meta options | Model class
- QuerySets: Making queries | QuerySet method reference | Lookup expressions
- Model instances: Instance methods | Accessing related objects
- Migrations: Introduction to Migrations | Operations reference | SchemaEditor | Writing migrations
- Advanced: Managers | Raw SQL | Transactions | Aggregation | Search | Custom fields | Multiple databases | Custom lookups | Query Expressions | Conditional Expressions | Database Functions
- Other: Supported databases | Legacy databases | Providing initial data | Optimize database access | PostgreSQL specific features

## 3. The View Layer
- The basics: URLconfs | View functions | Shortcuts | Decorators | Asynchronous Support
- Reference: Built-in Views | Request/response objects | TemplateResponse objects
- File uploads: Overview | File objects | Storage API | Managing files | Custom storage
- Class-based views: Overview | Built-in display views | Built-in editing views | Using mixins | API reference | Flattened index
- Advanced: Generating CSV | Generating PDF
- Middleware: Overview | Built-in middleware classes

## 4. The Template Layer
- The basics: Overview
- For designers: Language overview | Built-in tags and filters | Humanization
- For programmers: Template API | Custom tags and filters | Custom template backend

## 5. Forms
- The basics: Overview | Form API | Built-in fields | Built-in widgets
- Advanced: Forms for models | Integrating media | Formsets | Customizing validation

## 6. The Development Process
- Settings: Overview | Full list of settings
- Applications: Overview
- Exceptions: Overview
- django-admin and manage.py: Overview | Adding custom commands
- Testing: Introduction | Writing and running tests | Included testing tools | Advanced topics
- Deployment: Overview | WSGI servers | ASGI servers | Deploying static files | Tracking code errors by email | Deployment checklist

## 7. The Admin
- Admin site
- Admin actions
- Admin documentation generator

## 8. Security
- Security overview
- Disclosed security issues in Django
- Clickjacking protection
- Cross Site Request Forgery protection
- Cryptographic signing
- Security Middleware

## 9. Internationalization and Localization
- Overview | Internationalization | Localization | Localized web UI formatting and form input
- Time zones

## 10. Performance and Optimization
- Performance and optimization overview

## 11. Geographic Framework
- GeoDjango intends to be a world-class geographic web framework. Its goal is to make it as easy as possible to build GIS web applications and harness the power of spatially enabled data.

## 12. Common Web Application Tools
- Authentication: Overview | Using the authentication system | Password management | Customizing authentication | API Reference
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

## 13. Other Core Functionalities
- Conditional content processing
- Content types and generic relations
- Flatpages
- Redirects
- Signals
- System check framework
- The sites framework
- Unicode in Django

## 14. The Django Open-source Project
- Community: How to get involved | The release process | Team organization | The Django source code repository | Security policies | Mailing lists
- Design philosophies: Overview
- Documentation: About this documentation
- Third-party distributions: Overview
- Django over time: API stability | Release notes and upgrading instructions | Deprecation Timeline

# References
- https://docs.djangoproject.com/en/4.0/
- https://docs.djangoproject.com/en/4.0/contents/


