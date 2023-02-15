---
# User change
title: "Testing PostgreSQL Tunings"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Testing PostgreSQL Optimizations

Skip this section if you already have a performance test methodology for your PostgreSQL deployment. 

This section presents a method for testing PostgreSQL using HammerDB TPROC-C. We present this here in case readers do not already have an established test methodology. To really understand the impact of tuning on specific use cases and deployments, we recommend that readers develop a performance test strategy that reflects their use cases.

## Prerequisites

* Physical machine(s) or cloud node(s) with [PostgreSQL](https://www.postgresql.org/) installed and configured
      
## About HammerDB

[HammerDB](https://www.hammerdb.com/) is a database benchmarking tool. It can test PostgreSQL, MySQL, MariaDB, Db2, & SQL Server. It offers two benchmark types; TPROC-C and TPROC-H. TPROC-C models the TPC-C benchmark, while TPROC-H models the TPC-H benchmark. We will only discuss TPROC-C which is an [Online Transactional Processing](https://www.hammerdb.com/docs/ch03s01.html) style of workload. TPROC-C simulates a company that processes customer orders and manages the warehouses which contain the products the company sells.

In the following sections we will give a short primer on how to run HammerDB. We leave understanding HammerDB in more detail to the reader. A great place to learn more about HammerDB is their [documentation](https://www.hammerdb.com/document.html).

## Installing HammerDB

Following the HammerDB [installation instructions](https://www.hammerdb.com/docs/ch01.html).

## Running Tests Via GUI

At Arm, we tend to use TCL scripts for running HammerDB in an automated fashion. However, it is possible to run a HammerDB test using the GUI. If you are interested in running HammerDB tests through a GUI, we suggest reading the [Quick Start](https://www.hammerdb.com/docs/ch02.html) guide.

## Running Tests Via TCL Script

The [CLI & Scripted Commands documentation](https://www.hammerdb.com/docs/ch09s08.html) contains information on how to setup and run TCL script based tests. The example in the documentation is for MySQL. Below, we show an example for testing PostgreSQL.

The below will create a test database with 1000 warehouses. We select 128 users to help populate the database faster. We also use stored procedures (pg_storedprocs) instead of functions (default) because this is [recommended for PostgrSQL version v11 and above](https://www.hammerdb.com/docs/ch04s03.html#d0e1734). We leave understanding all of the parameters in the script as an exercise for the reader.

```

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

The above script can be executed by running the following:
```

hammerdbcli auto <tcl_scirpt_name>
```

The following script will run 6 iterations of the the TPROC-C test. It will run the test with 8, 16, 32, 64, 128, and 256 users. Each test iteration will ramp for 3 minutes, then run the actual test for 15 minutes. We leave understanding all of the parameters in the script as an exercise for the reader.

```

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

The above scripts can be used as a starting point for the reader's testing. We strongly recommend that these scripts be adjusted to create scenarios that are more similar to the reader's use case.

## Running Tests Against a Pool of PostgreSQL Nodes

If the reader is interested in running tests against a PostgreSQL cluster. For example, a cluster comprised of a primary (RW) node and two secondary (RO) nodes. We suggest looking into using the connect pool feature of HammerDB in the [documentation](https://www.hammerdb.com/docs/ch04s06.html#d0e2280). Note that when we tested the connect pool feature, it appeared to only work with functions and not stored procedures (like we used in the example above).
