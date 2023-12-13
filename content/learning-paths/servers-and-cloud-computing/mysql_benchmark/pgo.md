---
title: Enable profile-guided optimizaton for MySQL
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Profile-guided optimization (PGO) is a compiler optimization technique which uses profile data to improve performance. It is available in popular compilers, including GCC and Clang. 

This section shows how to use PGO on MySQL server with GCC.

In the previous step, you installed MySQL server in `/home/mysql/mysql_install_8.0.33`

This section creates two more installations of MySQL server, one to collect profile information, and another to use the profile data to achieve increased performance. 

## Rebuild MySQL server with profile generate enabled

Reconfigure the same source directory, but use a new installation directory for the build. 

This configuration adds `-DFPROFILE_GENERATE=ON` telling the compiler to capture a profile.

This results in a second installation of MySQL at `mysql_install_8.0.33_profile`

Do the build and install:

```console
cd $HOME/mysql-server
rm -rf build ; mkdir build ; cd build
cmake -DCMAKE_C_FLAGS="-g -O3 -march=native -mcpu=native -flto" -DCMAKE_CXX_FLAGS="-g -O3 -mcpu=native -flto" -DCMAKE_INSTALL_PREFIX=/home/mysql/mysql_install_8.0.33_profile -DWITH_BOOST=/home/mysql/boost_1_77_0/ -DFPROFILE_GENERATE=ON ..
make -j $(nproc)
make install
```

## Run Sysbench (to collect PGO profile data)

Stop the first build (if it is still running on your machine):

```console
$MYSQL_BIN/mysql -S $MYSQL_HOME/mysql.sock -uroot -e "DROP DATABASE sysdb;"
$MYSQL_BIN/mysqladmin -S $MYSQL_HOME/mysql.sock -uroot shutdown
```

Copy the configuration file from the first installation over to the second installation:

```console
cp $HOME/mysql_install_8.0.33/my.cnf $HOME/mysql_install_8.0.33_profile/
```

Set the first environment variable to the new installation location and start MySQL with the second installation: 

```console
export MYSQL_HOME=/home/mysql/mysql_install_8.0.33_profile
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

Run Sysbench on the client system again with the IP address of the server system.

```
./run_sysbench.sh [MySQL-server-ip] [oltp_write_only | oltp_read_only]
```

When Sysbench completes, uou will see a number of files with the `.gcda` extension which were created in the directory `mysql-server/build-profile-data`.

The profile data for PGO is now available.

## Rebuild MySQL server with profile use enabled

Reconfigure the same source directory again. 

This creates a new installation directory at `mysql_8.0.33_gcc_11.3.0_pgo`. This configuration adds `-DFPROFILE_USE=ON` telling the compiler to use the profile data from the previous run.

Do the build and install:

```console
cd $HOME/mysql-server
rm -rf build ; mkdir build ; cd build
cmake -DCMAKE_C_FLAGS="-g -O3 -march=native -mcpu=native -flto" -DCMAKE_CXX_FLAGS="-g -O3 -mcpu=native -flto" -DCMAKE_INSTALL_PREFIX=/home/mysql/mysql_install_8.0.33_pgo -DWITH_BOOST=/home/mysql/boost_1_77_0/ -DFPROFILE_USE=ON ..
make -j $(nproc)
make install
```

## Run Sysbench (with the PGO installation)

Stop the second build:

```console
$MYSQL_BIN/mysql -S $MYSQL_HOME/mysql.sock -uroot -e "DROP DATABASE sysdb;"
$MYSQL_BIN/mysqladmin -S $MYSQL_HOME/mysql.sock -uroot shutdown
```

Copy the configuration file from the first build over to the third build (the configuration file is the same in all cases):

```console
cp $HOME/mysql_install_8.0.33/my.cnf $HOME/mysql_install_8.0.33_pgo/
```

Set the first environment variable to the new installation location and start MySQL with the third installation: 

```console
export MYSQL_HOME=/home/mysql/mysql_install_8.0.33_pgo
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

Run Sysbench on the client system again with the IP address of the server system.

```
./run_sysbench.sh [MySQL-server-ip] [oltp_write_only | oltp_read_only]
```

You have now run with the PGO installation and will see increased performance.

## Test Environment

You can now do a full test sequence to see the performance impact of PGO.

The test environment setup from Alibaba ECS is shown below:

| C/S    | OS                   | Kernel                  | GCC    | cores  | RAM   |
| :----- | :------------------  | :---------------------- | :---   | :----- | :-----|
| Server |  Ubuntu 22.04.2 LTS  | 5.15.0-76-generic       | 11.4.0 | 8      | 32G   |
| Client |  Alibaba Cloud Linux | 5.10.134-14.al8.aarch64 | N/A    | 32     | 128G  |


You can run your own testing on Arm servers. Your results may be different, depending on the hardware configuration and the software version details.

## Test Results

Here is the the sequence used to run the testing:

1. reboot server
2. start MySQL server which doesn't enable PGO
3. run write test
4. run read test
5. repeat step 1-4 for another 2 times
6. reboot server
7. start MySQL server which enables PGO
8. run write test
9. run read test
10. repeat step 6-9 for another 2 times

### Write test results without PGO

Here are the results for 3 rounds of the write test without PGO:

```output

Throughput:

    events/s (eps):                      7837.0387

    time elapsed:                        300.0977s

    total number of events:              2351876

Throughput:

    events/s (eps):                      7616.9932

    time elapsed:                        300.0844s

    total number of events:              2285740

Throughput:

    events/s (eps):                      7893.9496

    time elapsed:                        300.0817s

    total number of events:              2368829

```

### Read test results without PGO

Here are the results for 3 rounds of the read test without PGO:

```output

Throughput:

    events/s (eps):                      3768.8060

    time elapsed:                        300.1503s

    total number of events:              1131208

Throughput:

    events/s (eps):                      3688.1464

    time elapsed:                        300.1504s

    total number of events:              1106998

Throughput:

    events/s (eps):                      3774.9087

    time elapsed:                        300.1509s

    total number of events:              1133042
```

### Write test results (+13.4%, +16.7%, +11.8%) with PGO

Below are the results for 3 rounds of the write test with PGO. 

The performance improved 13.4%, 16.7%, 11.8% for each round compared to non-PGO test.

```output

Throughput:

    events/s (eps):                      8891.5023

    time elapsed:                        300.0943s

    total number of events:              2668288

Throughput:

    events/s (eps):                      8892.7030

    time elapsed:                        300.0876s

    total number of events:              2668589

Throughput:

    events/s (eps):                      8831.1063

    time elapsed:                        300.0857s

    total number of events:              2650088
```

### Read test results (+25.9%, +20.9%, +16.4%) with PGO

Below are the results for 3 rounds of the read test with PGO. 

The performance improved 25.9%, 20.9%, 16.4% for each round compared to non-PGO test.

```output
Throughput:

    events/s (eps):                      4746.7576

    time elapsed:                        300.1492s

    total number of events:              1424735

Throughput:

    events/s (eps):                      4460.4811

    time elapsed:                        300.1489s

    total number of events:              1338808

Throughput:

    events/s (eps):                      4395.7754

    time elapsed:                        300.1699s

    total number of events:              1319479
```

You have now installed and run MysQL server compiled with PGO for improved performance.