---
title: Connect to MySQL and verify the database
description: Connect to a MySQL container, create a database and table, and verify that MySQL stores and retrieves data.
weight: 3
layout: "learningpathall"
---

## Connect to MySQL

After starting the MySQL container, you can connect to MySQL and create a database.

Open the MySQL client in the running container:

```bash
docker exec -it mysql-arm mysql -uroot -p
```

Enter the root password. After a successful connection, you'll see a `mysql>` prompt.

## Create a database

At the `mysql>` prompt, create the sample database:

```console
CREATE DATABASE arm_test;
```

MySQL should report `Query OK`.

## Verify the database

List the databases and confirm that `arm_test` appears:

```console
SHOW DATABASES;
```

The output is similar to:

```output
+--------------------+
| Database           |
+--------------------+
| arm_test           |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```

Select the sample database:

```console
USE arm_test;
```

The client should report `Database changed`. 

Check that the new database has no tables:

```console
SHOW TABLES;
```

The expected output is `Empty set`.

Create a sample table:

```console
CREATE TABLE book(name CHAR(10), id VARCHAR(10));
```

Insert sample rows:

```console
INSERT INTO book(name,id) VALUES ('Abook','10'),('Bbook','20'),('Cbook','20'),('Dbook','30'),('Ebook','45'),('Fbook','40'),('Gbook','69');
```

Inspect the table structure and its contents:

```console
DESCRIBE book;
SELECT * FROM book;
```

The output is similar to:

```output
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| name  | char(10)    | YES  |     | NULL    |       |
| id    | varchar(10) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.01 sec)

+-------+------+
| name  | id   |
+-------+------+
| Abook | 10   |
| Bbook | 20   |
| Cbook | 20   |
| Dbook | 30   |
| Ebook | 45   |
| Fbook | 40   |
| Gbook | 69   |
+-------+------+
7 rows in set (0.00 sec)
```

## What you've accomplished

You've verified that the MySQL container accepts connections and can store and retrieve data.

You can now use this database for your own application. To learn how to optimize a MySQL server on Arm, see the [Tune MySQL performance on Arm-based platforms](/learning-paths/servers-and-cloud-computing/mysql_tune/) Learning Path.
