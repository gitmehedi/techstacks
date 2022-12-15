<div align="center">
    <img src="img/logo.png" height="320" width="830" alt="Tech Stacks">
    <h1>PostgreSQL</h1>
    <strong>PostgreSQL, also known as Postgres, is a free and open-source relational database management system</strong>
</div>

<!-- TOC -->
  * [Introduction](#introduction)
  * [Installation](#installation)
    * [Ubuntu](#ubuntu)
      * [Prerequisite](#prerequisite)
    * [Docker](#docker)
      * [Prerequisite](#prerequisite)
  * [Tutorials](#tutorials)
* [References](#references)
<!-- TOC -->


## Introduction
[PostgreSQL](https://www.postgresql.org/), also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance. It was originally named POSTGRES, referring to its origins as a successor to the Ingres database developed at the University of California, Berkeley.

## Installation
[PostgreSQL Installation](https://www.postgresql.org/download/) depends on operating system like linux,ubuntu,mac,windows. We will install in major os.


### Ubuntu
You will need an Ubuntu 20.04 server with a non-root superuser account. And following command

#### Prerequisite
* Ubuntu 20.04

Install Postgresql on 
```bash
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql
```
> Mention postgres version or otherwise it will install latest version

### Docker
#### Prerequisite
* Ubuntu 20.04
* [Docker](https://hub.docker.com/_/postgres)

Run docker compose command to run kafka
```bash
$ docker compose -f postgresql.yaml -d
```

## Tutorials
### 1. Create Database User in PostgreSQL
To Create new database need to login in to postgresql database
```bash
# login into database 
$ sudo -u postgres psql
```
Create a database with name `PG_DATABASE`
```bash
> create database <database_name>
$ create database PG_DATABASE
```

Create a database user with name `DJANGO` with password `mypass`
```bash
> create user with <database_username> with encrypted password '<database_password>';
$ create user with DJANGO with encrypted password 'mypass';
```

Grant all grant all privileges on database `PG_DATABASE` to user `DJANGO`;
```bash
> grant all privileges on database <database_username> to <database_name>;
$ grant all privileges on database PG_DATABASE to DJANGO;
```
> One nice thing about PGSQL is it comes with some utility binaries like createuser and createdb. So we will be making use of that.

Create a User `DJANGO` and set password with `mypass`
```bash
# Create a database user
> sudo -u postgres createuser <database_username>
$ sudo -u postgres createuser DJANGO

# Set password for the user
> alter user <username> with encrypted password '<password>';
$ alter user DJANGO with encrypted password 'mypass';

# Granting privileges on database
> grant all privileges on database <dbname> to <username> ;
$ grant all privileges on database DJANGO to mypass ;
```

Create a Database with name `PG_DATABASE`
```bash

```
# References
- https://www.postgresql.org/download/linux/ubuntu/
- https://hub.docker.com/_/postgres
- https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e