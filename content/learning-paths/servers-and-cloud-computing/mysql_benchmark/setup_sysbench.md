---
title: "Build and run Sysbench"
weight: 3
layout: "learningpathall"
---

You can build and run Sysbench on the second Arm Linux system to benchmark the MySQL server.

This system is called the client.

You will need at least 30 GB of disk space on the client system.

## Build and install the MySQL server

Because MySQL libraries are needed by Sysbench, you will need to build and install the MySQL server on the client system as well. 

You do not need to configure and run MySQL, just the build and install steps.

Refer to [Setup, configure, and run MySQL server](/learning-paths/servers-and-cloud-computing/mysql_benchmark/setup_mysql_server) to build and install MySQL server and provide the required libraries to Sysbench on the client system. 


## Build and install Sysbench

Use the commands below to build and install Sysbench:

```console
git clone https://github.com/akopytov/sysbench
cd sysbench
```

Configure, build, and install Sysbench using:

```console
./autogen.sh
./configure --with-mysql-includes=$HOME/mysql_install_8.0.33/include  --with-mysql-libs=$HOME/mysql_install_8.0.33/lib
make -j $(nproc)
sudo make install
```

## Open MySQL port on the server system

Make sure that port 3003 is open on the server system so that the Sysbench client can connect. If the machines are on the same local network, no action is needed. If you are using cloud instances, you will need to adjust the security group settings to open port 3003 for traffic originating from the client system.

## Run benchmarks with Sysbench

To make it easier to run Sysbench, a script is provided below. 

Using a text editor, copy the contents below into a file named `run_sysbench.sh`:


```
#!/bin/bash

die() {
	echo $1
	exit 1
}

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:mysql_install_8.0.33/lib   # please replace it

SERVERIP=$1
MODE=$2   #oltp_write_only or oltp_read_only
#sync && echo 3 > /proc/sys/vm/drop_caches

WARMUP_TIME=60
RUN_TIME=300

NTHREAD=256

time=$(date "+%Y%m%d-%H:%M:%S")
echo "${time} $MODE Testing Ali config on mysql-8.0.25: nthread ${NTHREAD}"

sysbench $MODE \
	--db-ps-mode=auto \
	--mysql-host=$SERVERIP \
	--mysql-port=3003 \
	--mysql-user=sysbench \
	--mysql-password=password \
	--mysql-db=sysdb \
	--tables=100 \
	--table_size=400000 \
	--time=300 \
	--report-interval=1 \
	--threads=64 \
	cleanup || die "failed to cleanup"
echo "===> finish cleanup"
sleep 1

sysbench $MODE \
	--db-ps-mode=auto \
	--mysql-host=$SERVERIP \
	--mysql-port=3003 \
	--mysql-user=sysbench \
	--mysql-password=password \
	--mysql-db=sysdb \
	--tables=100 \
	--table_size=400000 \
	--time=300 \
	--report-interval=1 \
	--threads=64 \
	prepare || die "failed to prepare"
echo "===> finish prepare"
sleep 1

sysbench $MODE \
	--db-ps-mode=auto \
	--mysql-host=$SERVERIP \
	--mysql-port=3003 \
	--mysql-user=sysbench \
	--mysql-password=password \
	--mysql-db=sysdb \
	--tables=100 \
	--table_size=400000 \
	--warmup-time=${WARMUP_TIME} \
	--time=${RUN_TIME} \
	--report-interval=10 \
	--threads=${NTHREAD} \
	run || die "failed to run"

echo "===> finish run"
sleep 1
```

Make the script executable:

```console
chmod +x run_sysbench.sh
```

You can now start Sysbench by running the script. 

Provide the IP address of the server system as the first argument and the mode as the second argument:

```
./run_sysbench.sh [MySQL-server-ip] [oltp_write_only | oltp_read_only]
```

The final output for the `oltp_read_only` test will be similar to:

```output
SQL statistics:
    queries performed:
        read:                            16015671
        write:                           0
        other:                           2288042
        total:                           18303713
    transactions:                        1144147 (3810.48 per sec.)
    queries:                             18303713 (60958.94 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      3810.4831
    time elapsed:                        300.2631s
    total number of events:              1144147

Latency (ms):
         min:                                    5.91
         avg:                                   67.14
         max:                                  318.55
         95th percentile:                       78.60
         sum:                             76816641.30

Threads fairness:
    events (avg/stddev):           4469.3086/284.51
    execution time (avg/stddev):   300.0650/0.04

===> finish run
```
