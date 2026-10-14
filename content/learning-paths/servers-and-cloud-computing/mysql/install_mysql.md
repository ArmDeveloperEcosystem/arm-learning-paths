---
# User change
title: Configure MySQL on an Arm-based Linux server

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  MySQL installation options

If you're using a cloud service like Amazon Relational Database Service (RDS), the installation of MySQL is handled by those services. However, if you're working with a bare metal or cloud node, there are a few different installation options. The following steps are for configuring MySQL on an Arm Linux server running Ubuntu or Debian.

For other installation approaches, see [Chapter 2 Installing MySQL](https://dev.mysql.com/doc/refman/8.1/en/installing.html) in the MySQL documentation.

## Before you begin

Ensure that you're using 


## Install MySQL with APT 


## Connect to Database

Installations of MySQL will also install a CLI client application called `mysql`. Once a database is up and running, this tool can be used to connect to the database and make sure it is working. Review the [instructions](https://dev.mysql.com/doc/refman/8.1/en/mysql.html) on how to use the `mysql` CLI tool.

Shown below is sample output of what you should see when you connect to the database successfully.

```output
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 14
Server version: 8.0.32-0ubuntu0.22.04.2 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

### Sample MySQL Commands

There are plenty of resources that explain how to do basic interactions with a MySQL database. That said, a few basic command examples are shown below.

Create a data base:

```console
create DATABASE arm_test;
```

List available databases:

```console { output_lines = "2-11" }
show databases;
+--------------------+
| Database           |
+--------------------+
| arm_test           |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.10 sec)
```

Access the database:

```console { output_lines = "2" }
use arm_test;
Database changed
```

List tables in the database:

```console { output_lines= "2" }
show tables;
Empty set (0.09 sec)
```

Create a table:

```console { output_lines= "2" }
create table book(name char(10),id varchar(10));
Query OK, 0 rows affected (0.12 sec)
```

Insert values into the table:

```console { output_lines= "2,3" }
insert into book(name,id) values ('Abook','10'),('Bbook','20'),('Cbook','20'),('Dbook','30'),('Ebook','45'),('Fbook','40'),('Gbook','69');
Query OK, 7 rows affected (0.11 sec)
Records: 7  Duplicates: 0  Warnings: 0
```
Display information about the table:
```console { output_lines= "2-8" }
describe book;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| name  | char(10)    | YES  |     | NULL    |       |
| id    | varchar(10) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.10 sec)
```

Access the content of the table:

```console { output_lines= "2-13" }
select * from book;
+--------+------+
| name   | id   |
+--------+------+
| Abook  | 10   |
| Bbook  | 20   |
| Cbook  | 20   |
| Dbook  | 30   |
| Ebook  | 45   |
| Fbook  | 40   |
| Gbook  | 69   |
+--------+------+
7 rows in set (0.09 sec)
```
