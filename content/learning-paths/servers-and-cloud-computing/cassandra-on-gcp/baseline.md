---
title: Apache Cassandra baseline testing on Google Axion C4A Arm Virtual machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


Since Cassandra has been successfully installed on your GCP C4A Arm virtual machine, follow these steps to verify that it is running and functioning properly.

## Baseline Testing for Apache Cassandra

This guide helps verify the installation and perform baseline testing of **Apache Cassandra**.

## Start Cassandra

Run Cassandra in the background:

```console
cassandra -R
```

The `-R` flag allows Cassandra to run in the background as a daemon, so you can continue using the terminal. The first startup may take **30–60 seconds** as it initializes the necessary files and processes.

Check logs to ensure Cassandra started successfully:

```console
tail -f ~/cassandra/logs/system.log
```
Look for the message **"Startup complete"**, which indicates Cassandra is fully initialized.

### Check Cassandra Status
```console
nodetool status
```
You should see an output similar to:

```output
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address    Load        Tokens  Owns (effective)  Host ID                               Rack
UN  127.0.0.1  162.51 KiB  16      100.0%            78774686-39f3-47e7-87c3-3abc4f02a835  rack1
```
The `nodetool status` command displays the health and status of your Cassandra node(s). For a single-node setup, the output should indicate that the node is **Up (U)** and **Normal (N)**. This confirms that your Cassandra instance is running and ready to accept queries.

### Connect with CQLSH (Cassandra Query Shell)
**cqlsh** is the interactive command-line shell for Cassandra. It allows you to run Cassandra Query Language (CQL) commands to interact with your database, create keyspaces and tables, insert data, and perform queries.

```console
cqlsh
```
You’ll enter the CQL (Cassandra Query Language) shell.

### Create a Keyspace (like a database)
A **keyspace** in Cassandra is similar to a database in SQL systems. Here, we create a simple keyspace `testks` with a **replication factor of 1**, meaning data will only be stored on one node (suitable for a single-node setup).

```sql
CREATE KEYSPACE testks WITH replication = {'class':'SimpleStrategy','replication_factor' : 1};
```
Check if created:

```sql
DESCRIBE KEYSPACES;
```

You should see an output similar to:

```output
cqlsh> DESCRIBE KEYSPACES;

system       system_distributed  system_traces  system_virtual_schema
system_auth  system_schema       system_views   testks
```

### Create a Table
Tables in Cassandra are used to store structured data. This step creates a `users` table with three columns: `id` (unique identifier), `name` (text), and `age` (integer). The `id` column is the primary key.

```sql
USE testks;

CREATE TABLE users (
   id UUID PRIMARY KEY,
   name text,
   age int
);
```

### Insert Data
We insert two sample rows into the `users` table. The `uuid()` function generates a unique identifier for each row, which ensures that every user entry has a unique primary key.

```sql
INSERT INTO users (id, name, age) VALUES (uuid(), 'Alice', 30);
INSERT INTO users (id, name, age) VALUES (uuid(), 'Bob', 25);
```

### Query Data
This command retrieves all rows from the `users` table. Successful retrieval confirms that data insertion works correctly and that queries return expected results.

```sql
SELECT * FROM users;
```

You should see an output similar to:

```output
 id                                   | age | name
--------------------------------------+-----+-------
 c08dafde-17f0-4a4a-82b8-54455bb07836 |  25 |   Bob
 d47eb93c-3988-4aa1-bc85-9561500a6893 |  30 | Alice

(2 rows)
```

This baseline test verifies that Cassandra 5.0.5 is installed and running correctly on the VM. It confirms the node status, allows connection via `cqlsh`, and ensures basic operations like creating a keyspace, table, inserting, and querying data work as expected.

Please now press "Ctrl-D" to exit the Cassandra Query Shell. 
