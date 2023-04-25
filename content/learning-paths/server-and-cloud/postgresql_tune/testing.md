---
# User change
title: "Testing PostgreSQL Tunings"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Testing PostgreSQL Optimizations

Skip this section if you already have a performance test methodology for your `PostgreSQL` deployment. 

This section presents a method for testing `PostgreSQL` using HammerDB TPROC-C. This is useful information if you do not already have an established test methodology. To understand the impact of tuning on specific use cases and deployments, it is recommended that you develop a performance test strategy that reflects your use cases.

## Before you begin

You will need a physical machine or cloud node with [`PostgreSQL`](https://www.postgresql.org/) installed and configured.
      
## About HammerDB

[HammerDB](https://www.hammerdb.com/) is a database benchmarking tool. It can test `PostgreSQL`, MySQL, MariaDB, Db2, & SQL Server. It offers two benchmark types; TPROC-C and TPROC-H. TPROC-C models the TPC-C benchmark, while TPROC-H models the TPC-H benchmark. We will only discuss TPROC-C which is an [Online Transactional Processing](https://www.hammerdb.com/docs/ch03s01.html) style of workload. TPROC-C simulates a company that processes customer orders and manages the warehouses which contain the products the company sells.

You can use this topic as a primer on how to run HammerDB. 

To learn more about HammerDB refer to the [documentation](https://www.hammerdb.com/document.html).

## Installing HammerDB

Follow the [installation instructions](https://www.hammerdb.com/docs/ch01.html) to install HammerDB.

## Running tests using the GUI

You can use TCL scripts to run HammerDB in an automated fashion. 

It is also possible to run a HammerDB test using the GUI. 

If you are interested in running HammerDB tests through a GUI, read the [Quick Start](https://www.hammerdb.com/docs/ch02.html) guide.


## Running tests using TCL scripts

The [CLI and command documentation](https://www.hammerdb.com/docs/ch09s08.html) contains information on how to setup and run TCL script based tests. 

The example in the documentation is for MySQL. The example below is for testing `PostgreSQL`.

The script creates a test database with 1000 warehouses. 

The user count is set to 128 to help populate the database faster. Use stored procedures (pg_storedprocs) instead of functions (default) because this is [recommended for PostgrSQL version v11 and above](https://www.hammerdb.com/docs/ch04s03.html#d0e1734). 

1. Use a text editor to save the code below in a file named `test.tcl`

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
hammerdbcli auto test.tcl
```

The next script will run 6 iterations of the the TPROC-C test. 

It will run the test with 8, 16, 32, 64, 128, and 256 users. Each test iteration will ramp for 3 minutes, then run the actual test for 15 minutes. 

3. Use a text editor to save the code below in a file named `test2.tcl`

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
hammerdbcli auto test2.tcl
```

The above scripts can be used as a starting point for testing. You can adjust the scripts to create scenarios that are closer to your use case. 

## Running tests against a pool of PostgreSQL nodes

You can run tests against a `PostgreSQL` cluster. 

The cluster could consist of a primary (RW) node and two secondary (RO) nodes. 

Look into using the connect pool feature of HammerDB in the [documentation](https://www.hammerdb.com/docs/ch04s06.html#d0e2280). 

