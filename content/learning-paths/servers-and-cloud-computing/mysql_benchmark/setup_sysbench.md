---
title: "Setup sysbench client"
weight: 3
layout: "learningpathall"
---

## About the page
This page describes the steps to setup sysbench client to benchmark MySQL server. Please note the steps should
be performed in the client side.


## Build and install MySQL server
Since MySQL libs are need by sysbench, please refer to [Setup MySQL server](../setup_mysql_server) to build and install MySQL server so that sysbench could
locate the libs of MySQL.


## Build and install sysbench
Please follow the steps to build and install sysbench:
```
$ git clone https://github.com/akopytov/sysbench
$ ./autogen.sh
$ ./configure --with-mysql-includes=[path-to-mysql-server-install]/include --with-mysql-libs=[path-to-mysql-server-install]/lib
$ make -j $(nproc)
$ sudo make install

```

## Run benchmark with sysbench
In order to run sysbench with better user experience, please use the following script to run (saved as run_sysbench.sh):
```
#!/bin/bash

die() {
	echo $1
	exit 1
}

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:[path-to-mysql-server-install]/lib   # please replace it

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

And then run sysbench with:
```
$ ./run_sysbench.sh [MySQL-server-ip] [oltp_write_only | oltp_read_only]
```

