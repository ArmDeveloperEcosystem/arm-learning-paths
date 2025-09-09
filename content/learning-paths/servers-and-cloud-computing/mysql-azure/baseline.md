---
title: Validate MySQL
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run a functional test of MySQL on Azure Cobalt 100 

After installing MySQL on your Arm64 virtual machine, you can perform simple baseline testing to validate that MySQL runs correctly and produces the expected output.

### Start MySQL 

Make sure MySQL is running: 

```console
sudo systemctl start mysql
sudo systemctl enable mysql
```
### Connect to MySQL 

```console
mysql -u admin -p
```
Opens the MySQL client and connects as the new user(admin), prompting you to enter the admin password.

### Show and use Database

```sql
CREATE DATABASE baseline_test;
SHOW DATABASES;
USE baseline_test;
SELECT DATABASE();
```

- `CREATE DATABASE baseline_test;` - Creates a new database named baseline_test.
- `SHOW DATABASES;` - Lists all available databases.
- `USE baseline_test;` - Switches to the new database.
- `SELECT DATABASE();` - Confirms the current database in use.

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
You created a new database named **baseline_test**, verified its presence with `SHOW DATABASES`, and confirmed it is the active database using `SELECT DATABASE()`.

### Create and show Table

```sql
CREATE TABLE test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    value INT
);
```

- `CREATE TABLE` - Defines a new table named test_table.
  - `id` - Primary key with auto-increment.
  - `name` - String field up to 50 characters.
  - `value` - Integer field.
- `SHOW TABLES;` - Lists all tables in the current database.

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
You successfully created the table **test_table** in the `baseline_test` database and verified its existence using `SHOW TABLES`.

### Insert Sample Data

```sql
INSERT INTO test_table (name, value) 
VALUES 
('Alice', 100), 
('Bob', 200), 
('Charlie', 300);
```
- `INSERT INTO test_table (name, value)` - Specifies which table and columns to insert into.
- `VALUES` - Provides three rows of data.

After inserting, you can check the data with:

```sql
SELECT * FROM test_table;
```
- `SELECT *` - Retrieves all columns.
- `FROM test_table` - Selects from the test_table.

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

The functional test was successful — the **test_table** contains three rows (**Alice, Bob, and Charlie**) with their respective values, confirming MySQL is working 
correctly.
