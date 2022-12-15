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

## PSQL Help 
```html
$ psql --help

psql is the PostgreSQL interactive terminal.

Usage:
  psql [OPTION]... [DBNAME [USERNAME]]

General options:
  -c, --command=COMMAND    run only single command (SQL or internal) and exit
  -d, --dbname=DBNAME      database name to connect to (default: "root")
  -f, --file=FILENAME      execute commands from file, then exit
  -l, --list               list available databases, then exit
  -v, --set=, --variable=NAME=VALUE
                           set psql variable NAME to VALUE
                           (e.g., -v ON_ERROR_STOP=1)
  -V, --version            output version information, then exit
  -X, --no-psqlrc          do not read startup file (~/.psqlrc)
  -1 ("one"), --single-transaction
                           execute as a single transaction (if non-interactive)
  -?, --help[=options]     show this help, then exit
      --help=commands      list backslash commands, then exit
      --help=variables     list special variables, then exit

Input and output options:
  -a, --echo-all           echo all input from script
  -b, --echo-errors        echo failed commands
  -e, --echo-queries       echo commands sent to server
  -E, --echo-hidden        display queries that internal commands generate
  -L, --log-file=FILENAME  send session log to file
  -n, --no-readline        disable enhanced command line editing (readline)
  -o, --output=FILENAME    send query results to file (or |pipe)
  -q, --quiet              run quietly (no messages, only query output)
  -s, --single-step        single-step mode (confirm each query)
  -S, --single-line        single-line mode (end of line terminates SQL command)

Output format options:
  -A, --no-align           unaligned table output mode
      --csv                CSV (Comma-Separated Values) table output mode
  -F, --field-separator=STRING
                           field separator for unaligned output (default: "|")
  -H, --html               HTML table output mode
  -P, --pset=VAR[=ARG]     set printing option VAR to ARG (see \pset command)
  -R, --record-separator=STRING
                           record separator for unaligned output (default: newline)
  -t, --tuples-only        print rows only
  -T, --table-attr=TEXT    set HTML table tag attributes (e.g., width, border)
  -x, --expanded           turn on expanded table output
  -z, --field-separator-zero
                           set field separator for unaligned output to zero byte
  -0, --record-separator-zero
                           set record separator for unaligned output to zero byte

Connection options:
  -h, --host=HOSTNAME      database server host or socket directory (default: "/var/run/postgresql")
  -p, --port=PORT          database server port (default: "5432")
  -U, --username=USERNAME  database user name (default: "root")
  -w, --no-password        never prompt for password
  -W, --password           force password prompt (should happen automatically)
```
# References
- https://www.postgresql.org/download/linux/ubuntu/
- https://hub.docker.com/_/postgres
- https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e