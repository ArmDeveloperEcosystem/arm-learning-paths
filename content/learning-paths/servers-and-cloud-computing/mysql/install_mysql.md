---
# User change
title: "Install, Configure, and Check MySQL"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  MySQL Tuning

If you already know how to deploy a MySQL database. You might want to skip this learning path, and instead explore the [Learn how to Tune MySQL](/learning-paths/servers-and-cloud-computing/mysql_tune) learning path. That learning path covers how to get more performance out of an Arm based MySQL server.

##  Arm deployment options

There are numerous ways to deploy MySQL on Arm. Bare metal, cloud VMs, or the various SQL services that cloud providers offer. If you already have an Arm system, you can skip over this subsection and continue reading.

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

##  MySQL Documentation

MySQL server is a large project with many features. The [MySQL Reference Manual](https://dev.mysql.com/doc/refman/8.1/en/) should be explored. Make sure you are looking at the documentation for the version of MySQL you are working with.

##  MySQL installation options

If using a cloud service like AWS RDS, then the installation of MySQL is handled by those services. However, if working with a bare metal or cloud node, there are a few different [installation options](https://dev.mysql.com/doc/refman/8.1/en/installing.html). You should decide what approach you want to take for installing MySQL after reviewing the documentation.

##  MySQL Server Configuration

Getting MySQL server up and running is easy. This is because the default out of box configuration will work. However, this out of box configuration is most likely under optimized. In fact, a [graph](/learning-paths/servers-and-cloud-computing/mysql_tune/tuning/) of the performance difference between an out of box MySQL server and a tuned server is shown in the [Learn how to Tune MySQL](/learning-paths/servers-and-cloud-computing/mysql_tune/) learning path. That said, for the purpose of learning, it's ok to start with the out of box configuration. Once you have that working, you should read the [MySQL server configuration documentation](https://dev.mysql.com/doc/refman/8.1/en/mysqld-server.html), and follow the [Learn how to Tune MySQL](/learning-paths/servers-and-cloud-computing/mysql_tune) learning path.

## Connect to Database

Installations of MySQL will also install a CLI client application called `mysql`. Once a database is up and running, this tool can be used to connect to the database and make sure it is working. Review the [instructions](https://dev.mysql.com/doc/refman/8.1/en/mysql.html) on how to use the `mysql` CLI tool.

Below is a sample output of what you should see when you connect to the database successfully.

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

There are plenty of resources that explain how to do basic interactions with a MySQL database. It's suggested that the reader search for these resources on their own. That said, a few basic command examples are shown below.

Create a data base.
```
create DATABASE arm_test;
```

List available databases.

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

Access the database.

```console { output_lines = "2" }
use arm_test;
Database changed
```

List tables in the database.

```console { output_lines= "2" }
show tables;
Empty set (0.09 sec)
```

Create a table.

```console { output_lines= "2" }
create table book(name char(10),id varchar(10));
Query OK, 0 rows affected (0.12 sec)
```

Insert values into the table.

```console { output_lines= "2,3" }
insert into book(name,id) values ('Abook','10'),('Bbook','20'),('Cbook','20'),('Dbook','30'),('Ebook','45'),('Fbook','40'),('Gbook','69');
Query OK, 7 rows affected (0.11 sec)
Records: 7  Duplicates: 0  Warnings: 0
```
Display information about the table.
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

Access the content of the table.

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