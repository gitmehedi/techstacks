<div align="center">
    <img src="img/logo.png" height="320" width="830" alt="Tech Stacks">
    <h1>PostgreSQL</h1>
    <strong>PostgreSQL, also known as Postgres, is a free and open-source relational database management system</strong>
</div>


- [Introduction](#introduction)
- [Installation](#installation)
  - [Ubuntu](#ubuntu)
    - [Prerequisite](#prerequisite)
  - [Docker](#docker)
    - [Prerequisite](#prerequisite-1)
- [Tutorials](#tutorials)
  - [1. Create Database User](#1-create-database-user)
    - [Examples](#examples)
  - [2. ALTER Database User Properties](#2-alter-database-user-properties)
    - [Examples](#examples-1)
  - [3. Create Database](#3-create-database)
    - [Examples](#examples-2)
  - [4. Grant Database Permission](#4-grant-database-permission)
  - [5. Essential Postgres Database Command](#5-essential-postgres-database-command)
- [PostgreSQL Help Command Tools](#postgresql-help-command-tools)
  - [PSQL](#psql)
    - [CREATEDB](#createdb)
    - [CREATEUSER](#createuser)
- [References](#references)



# Introduction
[PostgreSQL](https://www.postgresql.org/), also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance. It was originally named POSTGRES, referring to its origins as a successor to the Ingres database developed at the University of California, Berkeley.

# Installation
[PostgreSQL Installation](https://www.postgresql.org/download/) depends on operating system like linux,ubuntu,mac,windows. We will install in major os.

## Ubuntu
You will need an Ubuntu 20.04 server with a non-root superuser account. And following command

### Prerequisite
* [Ubuntu 20.04](https://ubuntu.com/download/desktop/thank-you?version=22.04.1&architecture=amd64)

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

## Docker
### Prerequisite
* [Ubuntu 20.04](https://ubuntu.com/download/desktop/thank-you?version=22.04.1&architecture=amd64)
* [Docker](https://hub.docker.com/_/postgres)

Run docker compose command to run kafka
```bash
$ docker compose -f postgresql.yaml -d
```



# Tutorials

## 1. Create Database User

Database user Create template
```shell
CREATE USER username
    [ WITH
     [ SYSID uid ]
     [ PASSWORD 'password' ] ]
    [ CREATEDB   | NOCREATEDB ] [ CREATEUSER | NOCREATEUSER ]
    [ IN GROUP     groupname [, ...] ]
    [ VALID UNTIL  'abstime' ]
```

### Examples

Create user `odoo` 
```shell
$ CREATE USER odoo;
```

Create a database user with name `odoo` with password `mypass`
```shell
$ CREATE USER odoo with password "123456";

$ CREATE USER odoo with encrypted password "123456";
```

Create an account where the user can create databases
```shell
$ CREATE USER manuel WITH PASSWORD 'jw8s0F4' CREATEDB
```
Create a user with a password, whose account is valid until the end of 2001. Note that after one second has ticked in 2002, the account is not valid:
```shell
$ CREATE USER miriam WITH PASSWORD 'jw8s0F4' VALID UNTIL 'Jan 1 2002';
```

Create database_username with utility binaries like `createuser`
```bash
# Create a database user
> sudo -u postgres createuser <database_username>
$ sudo -u postgres createuser DJANGO
```

> Details are [here..](https://www.postgresql.org/docs/7.0/sql-createuser.htm)

## 2. ALTER Database User Properties

Database user Alter template
```shell
ALTER USER name [ [ WITH ] option [ ... ] ]

where option can be:

    CREATEDB | NOCREATEDB
    | CREATEUSER | NOCREATEUSER 
    | [ ENCRYPTED | UNENCRYPTED ] PASSWORD 'password' 
    | VALID UNTIL 'abstime'
```


### Examples
Change a user's password:
```shell
$ ALTER USER odoo WITH PASSWORD 'hu8jmn3';
$ ALTER USER odoo WITH encrypted PASSWORD 'hu8jmn3';
```

Change the expiration date of the user's password:
```shell
$ ALTER USER manuel VALID UNTIL 'Jan 31 2030';
```

Change a password expiration date, specifying that the password should expire at midday on 4th May 2005 using the time zone which is one hour ahead of UTC:
```shell
$ ALTER USER chris VALID UNTIL 'May 4 12:00:00 2005 +1';
```

Make a password valid forever:
```shell
$ ALTER USER fred VALID UNTIL 'infinity';
```

Give a user the ability to create other users and new databases:
```shell
$ ALTER USER miriam CREATEUSER CREATEDB;
```
> Details are [here..](https://www.postgresql.org/docs/8.0/sql-alteruser.html)

## 3. Create Database

Create Database
```shell
CREATE DATABASE name
    [ WITH ] [ OWNER [=] user_name ]
           [ TEMPLATE [=] template ]
           [ ENCODING [=] encoding ]
           [ STRATEGY [=] strategy ] ]
           [ LOCALE [=] locale ]
           [ LC_COLLATE [=] lc_collate ]
           [ LC_CTYPE [=] lc_ctype ]
           [ ICU_LOCALE [=] icu_locale ]
           [ ICU_RULES [=] icu_rules ]
           [ LOCALE_PROVIDER [=] locale_provider ]
           [ COLLATION_VERSION = collation_version ]
           [ TABLESPACE [=] tablespace_name ]
           [ ALLOW_CONNECTIONS [=] allowconn ]
           [ CONNECTION LIMIT [=] connlimit ]
           [ IS_TEMPLATE [=] istemplate ]
           [ OID [=] oid ]
```

### Examples

To create a new database:
```shell
$ CREATE DATABASE lusiadas;
```

To create a database sales owned by user salesapp with a default tablespace of salesspace:
```shell
$ CREATE DATABASE PG_DATABASE OWNER DJANGO TABLESPACE salesspace;
```


To Create new database need to login in to postgresql database
```shell
# login into database 
$ sudo -u postgres psql
```



Create database with utility binaries like `createdb`
```shell
> createdb <database_name> --owner <database_username>
$ createdb PG_DATABASE --owner DJANGO
```

## 4. Grant Database Permission

Grant all grant all privileges on database `PG_DATABASE` to user `DJANGO`;
```bash
> grant all privileges on database <database_username> to <database_name>;
$ grant all privileges on database PG_DATABASE to DJANGO;
```

## 5. Essential Postgres Database Command

** 1. Login PostgreSQL database using command line_**
```bash
$ psql -d {database_name} -U {username_of_database}
```

** 2. List all database in PostgreSQL_**
```bash
database_name=#\l
```

** 3. List all database user in PostgreSQL_**
```bash
database_name=#\du+
```


# PostgreSQL Help Command Tools
## PSQL
```bash
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

### CREATEDB
```bash
$ createdb --help

createdb creates a PostgreSQL database.

Usage:
  createdb [OPTION]... [DBNAME] [DESCRIPTION]

Options:
  -D, --tablespace=TABLESPACE  default tablespace for the database
  -e, --echo                   show the commands being sent to the server
  -E, --encoding=ENCODING      encoding for the database
  -l, --locale=LOCALE          locale settings for the database
      --lc-collate=LOCALE      LC_COLLATE setting for the database
      --lc-ctype=LOCALE        LC_CTYPE setting for the database
  -O, --owner=OWNER            database user to own the new database
  -T, --template=TEMPLATE      template database to copy
  -V, --version                output version information, then exit
  -?, --help                   show this help, then exit

Connection options:
  -h, --host=HOSTNAME          database server host or socket directory
  -p, --port=PORT              database server port
  -U, --username=USERNAME      user name to connect as
  -w, --no-password            never prompt for password
  -W, --password               force password prompt
  --maintenance-db=DBNAME      alternate maintenance database

By default, a database with the same name as the current user is created.

Report bugs to <pgsql-bugs@lists.postgresql.org>.
PostgreSQL home page: <https://www.postgresql.org/>

```

### CREATEUSER
```bash
$ createuser --help

createuser creates a new PostgreSQL role.

Usage:
  createuser [OPTION]... [ROLENAME]

Options:
  -c, --connection-limit=N  connection limit for role (default: no limit)
  -d, --createdb            role can create new databases
  -D, --no-createdb         role cannot create databases (default)
  -e, --echo                show the commands being sent to the server
  -g, --role=ROLE           new role will be a member of this role
  -i, --inherit             role inherits privileges of roles it is a
                            member of (default)
  -I, --no-inherit          role does not inherit privileges
  -l, --login               role can login (default)
  -L, --no-login            role cannot login
  -P, --pwprompt            assign a password to new role
  -r, --createrole          role can create new roles
  -R, --no-createrole       role cannot create roles (default)
  -s, --superuser           role will be superuser
  -S, --no-superuser        role will not be superuser (default)
  -V, --version             output version information, then exit
  --interactive             prompt for missing role name and attributes rather
                            than using defaults
  --replication             role can initiate replication
  --no-replication          role cannot initiate replication
  -?, --help                show this help, then exit

Connection options:
  -h, --host=HOSTNAME       database server host or socket directory
  -p, --port=PORT           database server port
  -U, --username=USERNAME   user name to connect as (not the one to create)
  -w, --no-password         never prompt for password
  -W, --password            force password prompt

Report bugs to <pgsql-bugs@lists.postgresql.org>.
PostgreSQL home page: <https://www.postgresql.org/>
```

# References
- https://www.postgresql.org/download/linux/ubuntu/
- https://hub.docker.com/_/postgres
- https://angrybite.wordpress.com/2019/09/08/install-pgadmin-4-on-linux-mint/
- http://www.postgresqltutorial.com/postgresql-administration/
- http://www.postgresqltutorial.com/postgresql-alter-database/
- http://www.postgresqltutorial.com/postgresql-reset-password/
- https://www.postgresql.org/docs/current/static/sql-alterdatabase.html
- https://stackoverflow.com/questions/22483555/give-all-the-permissions-to-a-user-on-a-db
- https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e