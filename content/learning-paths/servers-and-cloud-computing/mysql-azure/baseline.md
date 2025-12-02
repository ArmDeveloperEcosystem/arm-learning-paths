---
title: Validate MySQL functionality on Azure Arm64
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The benefits of validation 

After installing MySQL on your Azure Cobalt 100 Arm64 VM, run a functional test to confirm that the database is operational and ready for use. Beyond checking service status, validation ensures the following:

- MySQL is processing queries correctly
- Users can authenticate
- The environment is correctly configured for cloud workloads

## Start MySQL 

Ensure MySQL is running and configured to start on boot by running the following:

```console
sudo systemctl start mysql
sudo systemctl enable mysql
```
You’ve now validated that MySQL is running correctly and can store, retrieve, and organize data on your Azure Cobalt 100 Arm64 virtual machine. This confirms your environment is ready for development or production workloads. 

## Connect to MySQL 

Connect using the MySQL client:

```console
mysql -u admin -p
```
This opens the MySQL client and connects as the new user (admin), prompting you to enter the admin password.

## Show and use a database

Once you’ve connected successfully with your new user, the next step is to create and interact with a database. This verifies that your MySQL instance is not only accessible but also capable of storing and organizing data.

Run the following commands inside the MySQL shell:

```sql
CREATE DATABASE baseline_test;
SHOW DATABASES;
USE baseline_test;
SELECT DATABASE();
```

- `CREATE DATABASE baseline_test;` - creates a new database named baseline_test
- `SHOW DATABASES;` - lists all available databases
- `USE baseline_test;` - switches to the new database
- `SELECT DATABASE();` - confirms the current database in use

You should see output similar to:

```output
mysql> CREATE DATABASE baseline_test;
Query OK, 1 row affected (0.01 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| baseline_test      |
| benchmark_db       |
| information_schema |
| mydb               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
7 rows in set (0.00 sec)

mysql> USE baseline_test;
Database changed
mysql> SELECT DATABASE();
+---------------+
| DATABASE()    |
+---------------+
| baseline_test |
+---------------+
1 row in set (0.00 sec)
```
You created a new database named `baseline_test`, verified its presence with `SHOW DATABASES`, and confirmed it is the active database using `SELECT DATABASE()`.

## Create and show a table

After creating and selecting a database, the next step is to define a table, which represents how your data will be structured. In MySQL, tables are the core storage objects where data is inserted, queried, and updated.
Run the following inside the `baseline_test` database:

```sql
CREATE TABLE test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    value INT
);
SHOW TABLES;
```

- `CREATE TABLE` - defines a new table named test_table
  - `id` - primary key with auto-increment
  - `name` - string field up to 50 characters
  - `value` - integer field
- `SHOW TABLES;` - lists all tables in the current database

You should see output similar to:

```output
Query OK, 0 rows affected (0.05 sec)

mysql> SHOW TABLES;
+-------------------------+
| Tables_in_baseline_test |
+-------------------------+
| test_table              |
+-------------------------+
1 row in set (0.00 sec)
```
You successfully created the table `test_table` in the `baseline_test` database and verified its existence using `SHOW TABLES`.

## Insert sample data

Once the table is created, you can populate it with sample rows. This validates that MySQL can handle write operations and that the underlying storage engine is working properly.

Run the following SQL command inside the baseline_test database:
```sql
INSERT INTO test_table (name, value) 
VALUES 
('Alice', 100), 
('Bob', 200), 
('Charlie', 300);
```
- `INSERT INTO test_table (name, value)` - specifies which table and columns to insert into
- `VALUES` - provides three rows of data

After inserting data into `test_table`, you can confirm the write operation succeeded by retrieving the rows with:

```sql
SELECT * FROM test_table;
```
- `SELECT *` - retrieves all columns
- `FROM test_table` - selects from the test_table

You should see output similar to:

```output
mysql> SELECT * FROM test_table;
+----+---------+-------+
| id | name    | value |
+----+---------+-------+
|  1 | Alice   |   100 |
|  2 | Bob     |   200 |
|  3 | Charlie |   300 |
+----+---------+-------+
3 rows in set (0.00 sec)
```
This confirms that rows were successfully inserted, the auto-increment primary key (id) is working correctly and the query engine can read data from disk or memory and return results instantly.

The functional test was successful. The test_table contains the expected three rows (Alice, Bob, and Charlie) with their respective values. This confirms that MySQL is working correctly on your Cobalt 100 Arm-based VM, completing the installation and validation phase.
