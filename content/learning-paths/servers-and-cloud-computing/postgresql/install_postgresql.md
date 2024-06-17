---
# User change
title: "How do I install, configure, and check PostgreSQL?"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## What should I consider before installing PostgreSQL?

In this section you will learn about different options to install, configure and check your PostgreSQL database. If you already know how to deploy a PostgreSQL database, you can skip this learning path, and instead explore the [Learn how to Tune PostgreSQL](/learning-paths/servers-and-cloud-computing/postgresql_tune/) learning path. 

## What are the PostgreSQL Arm deployment options?

There are numerous ways to deploy PostgreSQL on Arm. Bare metal, cloud VMs, or the various SQL services that cloud providers offer. If you already have an Arm system, you can skip over this subsection and continue reading.

* Arm Cloud VMs
  * [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp) learning path
  * [AWS EC2](https://aws.amazon.com/ec2/)
    * [Deploy Arm Instances on AWS using Terraform](/learning-paths/servers-and-cloud-computing/aws-terraform) learning path
  * [Azure VMs](https://azure.microsoft.com/en-us/products/virtual-machines/)
    * [Deploy Arm virtual machines on Azure with Terraform](/learning-paths/servers-and-cloud-computing/azure-terraform) learning path
  * [GCP Compute Engine](https://cloud.google.com/compute)
    * [Deploy Arm virtual machines on Google Cloud Platform (GCP) using Terraform](/learning-paths/servers-and-cloud-computing/gcp) learning path
  * [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
* MySQL services
  * [AWS RDS](https://aws.amazon.com/rds)
    * Simply select an Arm based instance for deployment
* Additional options are listed in the [Get started with Servers and Cloud Computing](/learning-paths/servers-and-cloud-computing/intro) learning path

##  How do I learn about PostgreSQL?

PostgreSQL is a large project with many features. It is recommended that the [PostgreSQL documentation](https://www.postgresql.org/docs/current/index.html) be explored.

## PostgreSQL installation options

If you are using a cloud service like AWS RDS, then the installation of PostgreSQL is handled by those services. However, if you are working with a bare metal or cloud node, there are a few different [installation options](https://www.postgresql.org/docs/current/install-binaries.html). You should decide what approach you want to take for installing PostgreSQL after reviewing the documentation.

## What is the best way of configuring the PostgreSQL Server?

Getting PostgreSQL up and running is easy. This is because the default out of box configuration will work. However, this default configuration is most likely under optimized. A graph of the performance difference between an out of box PostgreSQL database and a tuned database is shown in the [Learn how to Tune PostgreSQL](/learning-paths/servers-and-cloud-computing/postgresql_tune/tuning) learning path. For the purpose of learning, it’s ok to start with the default configuration. Once you have that working, you should read the [PostgreSQL server configuration documentation](https://www.postgresql.org/docs/current/index.html) , and follow the [Learn how to Tune PostgreSQL](/learning-paths/servers-and-cloud-computing/postgresql_tune/) learning path.

## How do I get the PostgreSQL Build Configuration?

It can be helpful to know the build configuration of an installation of PostgreSQL. Run `pg_config` to get this information. Shown below is an example output:

```output
BINDIR = /usr/lib/postgresql/14/bin
DOCDIR = /usr/share/doc/postgresql-doc-14
HTMLDIR = /usr/share/doc/postgresql-doc-14
INCLUDEDIR = /usr/include/postgresql
PKGINCLUDEDIR = /usr/include/postgresql
INCLUDEDIR-SERVER = /usr/include/postgresql/14/server
LIBDIR = /usr/lib/aarch64-linux-gnu
PKGLIBDIR = /usr/lib/postgresql/14/lib
LOCALEDIR = /usr/share/locale
MANDIR = /usr/share/postgresql/14/man
SHAREDIR = /usr/share/postgresql/14
SYSCONFDIR = /etc/postgresql-common
PGXS = /usr/lib/postgresql/14/lib/pgxs/src/makefiles/pgxs.mk
CONFIGURE =  '--build=aarch64-linux-gnu' '--prefix=/usr' '--includedir=${prefix}/include' '--mandir=${prefix}/share/man' '--infodir=${prefix}/share/info' '--sysconfdir=/etc' '--localstatedir=/var' '--disable-option-checking' '--disable-silent-rules' '--libdir=${prefix}/lib/aarch64-linux-gnu' '--runstatedir=/run' '--disable-maintainer-mode' '--disable-dependency-tracking' '--with-tcl' '--with-perl' '--with-python' '--with-pam' '--with-openssl' '--with-libxml' '--with-libxslt' '--mandir=/usr/share/postgresql/14/man' '--docdir=/usr/share/doc/postgresql-doc-14' '--sysconfdir=/etc/postgresql-common' '--datarootdir=/usr/share/' '--datadir=/usr/share/postgresql/14' '--bindir=/usr/lib/postgresql/14/bin' '--libdir=/usr/lib/aarch64-linux-gnu/' '--libexecdir=/usr/lib/postgresql/' '--includedir=/usr/include/postgresql/' '--with-extra-version= (Ubuntu 14.8-0ubuntu0.22.04.1)' '--enable-nls' '--enable-thread-safety' '--enable-debug' '--enable-dtrace' '--disable-rpath' '--with-uuid=e2fs' '--with-gnu-ld' '--with-gssapi' '--with-ldap' '--with-pgport=5432' '--with-system-tzdata=/usr/share/zoneinfo' 'AWK=mawk' 'MKDIR_P=/bin/mkdir -p' 'PROVE=/usr/bin/prove' 'PYTHON=/usr/bin/python3' 'TAR=/bin/tar' 'XSLTPROC=xsltproc --nonet' 'CFLAGS=-g -O2 -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security' 'LDFLAGS=-Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now' '--enable-tap-tests' '--with-icu' '--with-llvm' 'LLVM_CONFIG=/usr/bin/llvm-config-14' 'CLANG=/usr/bin/clang-14' '--with-lz4' '--with-systemd' '--with-selinux' 'build_alias=aarch64-linux-gnu' 'CPPFLAGS=-Wdate-time -D_FORTIFY_SOURCE=2' 'CXXFLAGS=-g -O2 -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security'
CC = gcc
CPPFLAGS = -Wdate-time -D_FORTIFY_SOURCE=2 -D_GNU_SOURCE -I/usr/include/libxml2
CFLAGS = -Wall -Wmissing-prototypes -Wpointer-arith -Wdeclaration-after-statement -Werror=vla -Wendif-labels -Wmissing-format-attribute -Wimplicit-fallthrough=3 -Wcast-function-type -Wformat-security -fno-strict-aliasing -fwrapv -fexcess-precision=standard -Wno-format-truncation -Wno-stringop-truncation -moutline-atomics -g -g -O2 -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security
CFLAGS_SL = -fPIC
LDFLAGS = -Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now -L/usr/lib/llvm-14/lib -Wl,--as-needed
LDFLAGS_EX = 
LDFLAGS_SL = 
LIBS = -lpgcommon -lpgport -lselinux -llz4 -lxslt -lxml2 -lpam -lssl -lcrypto -lgssapi_krb5 -lz -lreadline -lm 
VERSION = PostgreSQL 14.8
```

The switches CFLAGS, CXXFLAGS, and LDFLAGS listed in the `CONFIGURE` line can be very helpful if you plan to build PostgreSQL from source. Tuning compilation options is discussed in the [Learn how to Tune PostgreSQL](/learning-paths/servers-and-cloud-computing/postgresql_tune/tuning) learning path.

## How do I connect to the PostgreSQL database? 

Installations of PostgreSQL will also install a CLI client application called [`psql`](https://www.postgresql.org/docs/current/app-psql.html). Once a database is up and running, this tool can be used to connect to the database and make sure it is working. Review the [instructions](https://www.postgresql.org/docs/15/tutorial-accessdb.html) on how to use the `psql` CLI tool.

Below is sample output of what you should see when you connect to the database successfully.
```output
psql (15.2)
Type "help" for help.

postgres=# 
```

## What are some sample PostgreSQL Commands?

Create a new database using the command shown:

```console
postgres=# create database testdb;
CREATE DATABASE
```

List all databases: 
```console
postgres=# \l
                                             List of databases
   Name    |  Owner   | Encoding | Collate |  Ctype  | ICU Locale | Locale Provider |   Access privileges   
-----------+----------+----------+---------+---------+------------+-----------------+-----------------------
 postgres  | postgres | UTF8     | C.UTF-8 | C.UTF-8 |            | libc            | 
 template0 | postgres | UTF8     | C.UTF-8 | C.UTF-8 |            | libc            | =c/postgres          +
           |          |          |         |         |            |                 | postgres=CTc/postgres
 template1 | postgres | UTF8     | C.UTF-8 | C.UTF-8 |            | libc            | =c/postgres          +
           |          |          |         |         |            |                 | postgres=CTc/postgres
 testdb    | postgres | UTF8     | C.UTF-8 | C.UTF-8 |            | libc            | 
(4 rows)
```

Switch to the new databases:

```console
postgres=# \c testdb;
You are now connected to database "testdb" as user "postgres".
```

Create a new table in the database:
```console
postgres=# CREATE TABLE company ( emp_name VARCHAR, emp_dpt VARCHAR);
CREATE TABLE
```

Display the database tables: 
```console
postgres=# \dt;
          List of relations
 Schema |  Name   | Type  |  Owner   
--------+---------+-------+----------
 public | company | table | postgres
(1 row)
```

Insert data into the table:
```console
postgres=# INSERT INTO company VALUES ('Herry', 'Development'), ('Tom', 'Testing'),('Ankit', 'Sales'),('Manoj', 'HR'),('Noy', 'Presales');
INSERT 0 5
```

Print the contents of the table:
```console
postgres=# select * from company;
 emp_name |   emp_dpt   
----------+-------------
 Herry    | Development
 Tom      | Testing
 Ankit    | Sales
 Manoj    | HR
 Noy      | Presales
(5 rows)
```
Using these sample commands shown above you have successfully validated your installation of PostgreSQL database.
