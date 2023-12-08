---
title: "Setup, configure, and run MySQL server"
weight: 2
layout: "learningpathall"
---

You can run MySQL server on the first Arm Linux system. Ubuntu 22.04 is used, but other Linux distributions and Ubuntu versions may also work. 


Follow the instructions below to build, install, configure, and run MySQL server. 

This system is called the server.

You will need at least 100 Gb of disk space on the server system.

## Install the required packages

In order to build MySQL server, install the following packages:

```console
sudo apt install git make automake libtool bison pkg-config cmake g++ openssl libssl-dev libncurses5-dev libtirpc-dev rpcsvc-proto libaio-dev libssl-dev -y
```

## Create a mysql user

MySQL server can't be run as root. 

You can create a mysql user, use your own password instead of `mysql*pw`:

```console
sudo useradd -s /bin/bash -m mysql && sudo adduser mysql sudo && echo "mysql:mysql*pw" | sudo chpasswd
```

Change to the `mysql` user, enter the password when prompted:

```console
su - mysql
```

## Download boost

Boost is needed to build MySQL server. To build MySQL server 8.0.33, boost_1_77_0 is needed.

Download Boost:

```console
wget https://boostorg.jfrog.io/artifactory/main/release/1.77.0/source/boost_1_77_0.tar.gz && tar xzvf boost_1_77_0.tar.gz
```

## Build and install MySQL server

Run the commands below to build and install MySQL server:

```
git clone https://github.com/mysql/mysql-server && cd mysql-server
git checkout mysql-8.0.33
git submodule update --recursive
mkdir build ; cd build
cmake -DCMAKE_C_FLAGS="-g -O3 -mcpu=native -flto" -DCMAKE_CXX_FLAGS="-g -O3 -mcpu=native -flto" -DCMAKE_INSTALL_PREFIX=/home/mysql/mysql_install_8.0.33 -DWITH_BOOST=/home/mysql/boost_1_77_0/ ..
make -j $(nproc)
make -j $(nproc) install
```

## Create a MySQL configuration file

To configure MySQL server, you need to create the `my.cnf` config file.

Use a text editor to create a file named `/home/mysql/mysql_install_8.0.33/my.cnf` with the contents:

```
[mysqld]
character_set_server = utf8
collation_server = utf8_general_ci
max_heap_table_size = 67108864
max_allowed_packet = 1073741824
thread_stack = 262144
interactive_timeout = 7200
wait_timeout = 86400
sort_buffer_size = 2097152
read_buffer_size = 1048576
read_rnd_buffer_size = 256K
join_buffer_size = 1048576
net_buffer_length = 16384
thread_cache_size = 100
ft_min_word_len = 4
transaction_isolation = READ-COMMITTED
tmp_table_size = 2097152
core-file
skip_name_resolve
skip_ssl
 
default_authentication_plugin = mysql_native_password
max_connections = 5000
max_user_connections = 5000
max_prepared_stmt_count = 1728000
 
binlog_cache_size = 1048576
max_binlog_size = 500M
sync_binlog = 1000
binlog_format = ROW
gtid_mode = ON
enforce-gtid-consistency = 1
 
innodb_flush_log_at_trx_commit = 2
innodb_buffer_pool_instances = 8
innodb_buffer_pool_size = 12884901888
innodb_file_per_table
innodb_log_buffer_size = 16M
innodb_log_file_size = 16384M
innodb_log_files_in_group = 2
innodb_max_dirty_pages_pct = 75
innodb_flush_method = O_DIRECT
innodb_lock_wait_timeout = 50
innodb_doublewrite = 1
innodb_rollback_on_timeout = OFF
innodb_autoinc_lock_mode = 2
innodb_purge_threads = 1
innodb_lru_scan_depth = 1024
innodb_open_files = 2000
 
table_open_cache = 2048
table_open_cache_instances = 8
 
innodb_read_io_threads = 4
innodb_write_io_threads = 4
innodb_io_capacity = 20000
innodb_io_capacity_max = 40000
 
autocommit = ON
innodb_deadlock_detect = ON
event_scheduler = OFF
performance_schema = OFF
 
loose_thread_pool_enabled = OFF
loose_thread_pool_size = 4
loose_innodb_rds_flashback_task_enabled = OFF
loose_innodb_undo_retention = 0

```

## Start MySQL server

Run the commands below to start MySQL server:

```
export MYSQL_HOME=/home/mysql/mysql_install_8.0.33
export MYSQL_BIN=$MYSQL_HOME/bin
export MYSQL_PLUGIN=$MYSQL_HOME/lib/plugin
export MYSQL_DATA=$MYSQL_HOME/data
export MYSQL_PORT=3003
rm -rf $MYSQL_DATA && mkdir $MYSQL_DATA
$MYSQL_BIN/mysqld  --initialize-insecure --basedir=$MYSQL_HOME --datadir=$MYSQL_DATA --default_authentication_plugin=mysql_native_password --log-error-verbosity=3
$MYSQL_BIN/mysqld \
                        --defaults-file=$MYSQL_HOME/my.cnf \
                        --basedir=$MYSQL_HOME \
                        --datadir=$MYSQL_DATA \
                        --socket=$MYSQL_HOME/mysql.sock \
                        --port=$MYSQL_PORT \
                        --log-error=$MYSQL_HOME/log.err \
                        --log-error-verbosity=3 \
                        --secure-file-priv="" \
                        --plugin-dir=$MYSQL_PLUGIN \
                        --user=mysql \
                        2>&1 &
sleep 10 # make sure $MYSQL_HOME/mysql.sock is created
$MYSQL_BIN/mysql \
                -S $MYSQL_HOME/mysql.sock \
                -uroot \
                -e "use mysql; \
                update user set user.Host='%' where user.User='root'; \
                FLUSH PRIVILEGES; \
                CREATE DATABASE IF NOT EXISTS sysdb; \
                create user sysbench@'%' identified by 'password'; \
                grant all privileges on sysdb.* to sysbench@'%';"
```


## Stop MySQL server

If you want to stop MySQL server after benchmarking is done, you can use the commands:

```
$MYSQL_BIN/mysql -S $MYSQL_HOME/mysql.sock -uroot -e "DROP DATABASE sysdb;"
$MYSQL_BIN/mysqladmin -S $MYSQL_HOME/mysql.sock -uroot shutdown
```
