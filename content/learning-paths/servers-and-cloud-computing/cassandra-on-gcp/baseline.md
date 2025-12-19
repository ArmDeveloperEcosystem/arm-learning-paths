---
title: Test Cassandra baseline functionality
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

Now that Cassandra is installed on your GCP C4A Arm virtual machine, verify that it's running and functioning properly.

## Start Cassandra

Run Cassandra in the background:

```console
cassandra -R
```

The `-R` flag allows Cassandra to run in the background as a daemon. The first startup may take 30–60 seconds as it initializes.

Check logs to ensure Cassandra started successfully:

```console
tail -f ~/cassandra/logs/system.log
```

Look for the message "Startup complete", which indicates Cassandra is fully initialized.

## Check Cassandra status

```console
nodetool status
```

The output is similar to:

```output
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address    Load        Tokens  Owns (effective)  Host ID                               Rack
UN  127.0.0.1  162.51 KiB  16      100.0%            78774686-39f3-47e7-87c3-3abc4f02a835  rack1
```

For a single-node setup, the output should indicate that the node is Up (U) and Normal (N), confirming that your Cassandra instance is running and ready to accept queries.

## Connect with CQLSH

`cqlsh` is the interactive command-line shell for Cassandra that allows you to run Cassandra Query Language (CQL) commands.

```console
cqlsh
```

You'll enter the CQL (Cassandra Query Language) shell.

## Create a keyspace

A keyspace in Cassandra is similar to a database in SQL systems. Create a simple keyspace `testks` with a replication factor of 1 (suitable for a single-node setup):

```sql
CREATE KEYSPACE testks WITH replication = {'class':'SimpleStrategy','replication_factor' : 1};
```

Verify the keyspace was created:

```sql
DESCRIBE KEYSPACES;
```

The output is similar to:

```output
cqlsh> DESCRIBE KEYSPACES;

system       system_distributed  system_traces  system_virtual_schema
system_auth  system_schema       system_views   testks
```

## Create a table

Create a `users` table with three columns:

```sql
USE testks;

CREATE TABLE users (
   id UUID PRIMARY KEY,
   name text,
   age int
);
```

## Insert data

Insert two sample rows into the `users` table. The `uuid()` function generates a unique identifier for each row:

```sql
INSERT INTO users (id, name, age) VALUES (uuid(), 'Alice', 30);
INSERT INTO users (id, name, age) VALUES (uuid(), 'Bob', 25);
```

## Query data

Retrieve all rows from the `users` table:

```sql
SELECT * FROM users;
```

The output is similar to:

```output
 id                                   | age | name
--------------------------------------+-----+-------
 c08dafde-17f0-4a4a-82b8-54455bb07836 |  25 |   Bob
 d47eb93c-3988-4aa1-bc85-9561500a6893 |  30 | Alice

(2 rows)
```

This baseline test verifies that Cassandra 5.0.5 is installed and running correctly on the VM, confirming node status, CQLSH connectivity, and basic database operations.

Press `Ctrl-D` to exit the Cassandra Query Shell. 
