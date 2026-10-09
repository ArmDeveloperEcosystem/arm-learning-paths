---
# User change
title: Test PostgreSQL tuning with HammerDB
description: Learn how to use HammerDB TPROC-C as a repeatable PostgreSQL workload when evaluating tuning changes.

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Measure PostgreSQL tuning changes

Use this section if you need a repeatable way to test PostgreSQL changes. If you already have a performance test methodology for your PostgreSQL deployment, use that instead.

HammerDB TPROC-C is one option for comparing a baseline with a tuned configuration. It does not replace a performance test that reflects your application's SQL statements, data size, client concurrency, and latency requirements.

## Before you begin

You need a physical system or cloud instance with [PostgreSQL](https://www.postgresql.org/) installed and configured, plus enough storage and memory for the test database.
      
## About HammerDB

[HammerDB](https://www.hammerdb.com/) is a database performance test tool that supports PostgreSQL, MySQL, MariaDB, Db2, and SQL Server. It provides TPROC-C and TPROC-H workloads. TPROC-C models an [online transaction processing](https://www.hammerdb.com/docs/ch03s01.html) workload based on TPC-C, while TPROC-H models a decision-support workload based on TPC-H.

TPROC-C and TPROC-H results are not official TPC-C or TPC-H benchmark results. If you need a TPC-C or TPC-H result, run the corresponding official TPC benchmark and follow its rules.

This Learning Path uses TPROC-C, which simulates a company processing customer orders and managing warehouses containing the products it sells.

For more information, see the [HammerDB documentation](https://www.hammerdb.com/document.html).

## Installing HammerDB

Follow the [installation instructions](https://www.hammerdb.com/docs/ch01.html) to install HammerDB.

## Running tests using the GUI

You can use TCL scripts to run HammerDB automatically.

You can also run a HammerDB test with the GUI.

If you are interested in running HammerDB tests through a GUI, read the [Quick Start](https://www.hammerdb.com/docs/ch02.html) guide.


## Running tests using TCL scripts

The [CLI and command documentation](https://www.hammerdb.com/docs/ch09s08.html) explains how to set up and run TCL-script-based tests.

The example in the documentation is for MySQL. The example below is for testing `PostgreSQL`.

The script creates a test database with 1000 warehouses.

The user count is set to 128 to populate the database faster. It uses stored procedures (`pg_storedprocs`) instead of functions because HammerDB recommends this option for PostgreSQL version 11 and later.

1. Use a text editor to save the code below in a file named `build.tcl`

Replace `postgresql_host_ip` with your IP address. 

```console
#!/bin/tclsh
dbset db pg
dbset bm TPROC-C
diset connection pg_host <postgresql_host_ip>
diset connection pg_port 5432
diset tpcc pg_storedprocs true
diset tpcc pg_count_ware 1000
diset tpcc pg_num_vu 128
diset tpcc pg_raiseerror true
buildschema
```

2. Execute the script:

```console
hammerdbcli auto build.tcl
```

The next script runs six TPROC-C test iterations.

It runs with 8, 16, 32, 64, 128, and 256 users. Each iteration ramps for three minutes and then runs for 15 minutes.

3. Use a text editor to save the code below in a file named `test.tcl`

Replace `postgresql_host_ip` with your IP address. 

```console
#!/bin/tclsh
dbset db pg
dbset bm TPROC-C
diset connection pg_host <postgresql_host_ip>
diset connection pg_port 5432
diset connection pg_sslmode disable
diset tpcc pg_timeprofile true
diset tpcc pg_storedprocs true
diset tpcc pg_count_ware 1000
diset tpcc pg_num_vu 128
diset tpcc pg_driver timed
diset tpcc pg_rampup 3
diset tpcc pg_duration 15
diset tpcc pg_raiseerror true
loadscript

puts "Start Test(s)"
foreach z { 8 16 32 64 128 256 } {
puts "Testing with $z users"
vuset vu $z
vuset iterations 1
vuset logtotemp 1
vuset unique 1
vucreate
vurun
runtimer 7200
vudestroy
after 5000
}
puts "Tests complete"
```

4. Execute the script:

```console
hammerdbcli auto test.tcl
```

Use these scripts as a starting point. Adjust the data size, user count, ramp time, duration, and SQL execution mode to create a workload closer to your use case.

## Running tests against a pool of PostgreSQL nodes

You can run tests against a PostgreSQL cluster.

The cluster can consist of a primary read/write node and one or more read-only standby nodes.

See the [HammerDB connection pool documentation](https://www.hammerdb.com/docs/ch04s06.html#d0e2280) for cluster testing options.

## What you've learned

You've learned how to use HammerDB TPROC-C as a repeatable PostgreSQL test workload.

Use the same workload, system configuration, and measurement process before and after each tuning change so you can attribute the result to the change you made.
