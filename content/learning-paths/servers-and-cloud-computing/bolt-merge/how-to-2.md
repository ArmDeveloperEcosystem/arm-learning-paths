---
title: Instrument MySQL with BOLT 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, you'll use BOLT to instrument the MySQL application binary and to collect profile data for specific workloads. 

The collected profiles will be merged with others and used to optimize the application's code layout.

## Build mysqld from source 

Follow these steps to build the MySQL server (`mysqld`) from source:

Install the required dependencies:

```bash
sudo apt update
sudo apt install -y build-essential cmake libncurses5-dev libssl-dev libboost-all-dev \ 
                  bison pkg-config libaio-dev libtirpc-dev git ninja-build liblz4-dev
```

Download the MySQL source code. You can change to another version in the `checkout` command below if needed. 

```bash
git clone https://github.com/mysql/mysql-server.git
cd mysql-server
git checkout mysql-8.0.37
```

Configure the build for debug:

```bash
mkdir build && cd build
cmake .. -DCMAKE_C_FLAGS="-O3 -march=native -Wno-enum-constexpr-conversion -fno-reorder-blocks-and-partition" \
   -DCMAKE_CXX_FLAGS="-O3 -march=native -Wno-enum-constexpr-conversion -fno-reorder-blocks-and-partition" \
   -DCMAKE_CXX_LINK_FLAGS="-Wl,--emit-relocs" -DCMAKE_C_LINK_FLAGS="-Wl,--emit-relocs" -G Ninja \
   -DWITH_BOOST=$HOME/boost -DDOWNLOAD_BOOST=On -DWITH_ZLIB=bundled -DWITH_LZ4=system -DWITH_SSL=system
```

Build MySQL:

```bash
ninja
```

After the build completes, the `mysqld` binary is located at `$HOME/mysql-server/build/runtime_output_directory/mysqld`

{{% notice Note %}}
You can run `mysqld` directly from the build directory as shown, or run `make install` to install it system-wide. For testing and instrumentation, running from the build directory is usually preferred.
{{% /notice %}} 

After building mysqld, install MySQL server and client utilities system-wide:

```bash
sudo ninja install
```

This will make the `mysql` client and other utilities available in your PATH.

```bash
echo 'export PATH="$PATH:/usr/local/mysql/bin"' >> ~/.bashrc
source ~/.bashrc
```

Ensure the binary is unstripped and includes debug symbols for BOLT instrumentation.

To work with BOLT, your application binary should be:

- Built from source
- Unstripped, with symbol information available
- Compiled with frame pointers enabled (`-fno-omit-frame-pointer`)

You can verify this with:

```bash
readelf -s $HOME/mysql-server/build/runtime_output_directory/mysqld | grep main
```

The partial output is:

```output
 23837: 000000000950dfe8     8 OBJECT  GLOBAL DEFAULT   27 mysql_main
 34522: 000000000915bfd0     8 OBJECT  GLOBAL DEFAULT   26 server_main_callback
 42773: 00000000051730e4    80 FUNC    GLOBAL DEFAULT   13 _Z18my_main_thre[...]
 44882: 000000000357dc98    40 FUNC    GLOBAL DEFAULT   13 main
 61046: 0000000005ffd5c0    40 FUNC    GLOBAL DEFAULT   13 _Z21record_main_[...]
```

If the symbols are missing, rebuild the binary with debug info and no stripping.


## Prepare MySQL server before running workloads

Before running the workload, you may need to initialize a new data directory if this is your first run:

```bash
# Initialize a new data directory 
# Run this from the root of your MySQL source directory (e.g. $HOME/mysql-server). This creates an empty database in the data/ directory.
bin/mysqld --initialize-insecure --datadir=data
```

Start the instrumented server. On an 8-core system, use available cores (e.g., 2 for mysqld, 7 for sysbench). Run the command from build directory.

```bash
taskset -c 2 ./bin/mysqld \
  --datadir=data \
  --max-connections=64 \
  --back-log=10000 \
  --innodb-buffer-pool-instances=128 \
  --innodb-file-per-table \
  --innodb-sync-array-size=1024 \
  --innodb-flush-log-at-trx-commit=1 \
  --innodb-io-capacity=5000 \
  --innodb-io-capacity-max=10000 \
  --tmp-table-size=16M \
  --max-heap-table-size=16M \
  --log-bin=1 \
  --sync-binlog=1 \
  --innodb-stats-persistent \
  --innodb-read-io-threads=4 \
  --innodb-write-io-threads=4 \
  --key-buffer-size=16M \
  --max-allowed-packet=16M \
  --max-prepared-stmt-count=2000000 \
  --innodb-flush-method=fsync \
  --innodb-log-buffer-size=64M \
  --read-buffer-size=262144 \
  --read-rnd-buffer-size=524288 \
  --binlog-format=MIXED \
  --innodb-purge-threads=1 \
  --table-open-cache=8000 \
  --table-open-cache-instances=16 \
  --open-files-limit=1048576 \
  --default-authentication-plugin=mysql_native_password
```

Adjust `--datadir`, `--socket`, and `--port` as needed for your environment. Make sure the server is running and accessible before proceeding.

With the database running, open a second terminal to create a benchmark User and third terminal to run the client commands. 

In the new terminal, navigate to the build directory:

```bash
cd $HOME/mysql-server/build
```

## Create Benchmark User and Database 

Run once after initializing MySQL for the first time:
```bash
bin/mysql -u root <<< "
CREATE USER 'bench'@'localhost' IDENTIFIED BY 'bench';
CREATE DATABASE bench;
GRANT ALL PRIVILEGES ON *.* TO 'bench'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;"
```

This sets up the bench user and the bench database with full privileges. Do not repeat this before every test — it is only required once.

## Reset Benchmark Database Between Runs 

This clears all existing tables and data from the bench database, giving you a clean slate for sysbench prepare without needing to recreate the user or reinitialize the datadir.

```bash
bin/mysql -u root <<< "DROP DATABASE bench; CREATE DATABASE bench;"
```

## Install and build sysbench

In a third terminal, run the commands below if you have not run sysbench yet. 

```bash
git clone https://github.com/akopytov/sysbench.git
cd sysbench
./autogen.sh
./configure
make -j$(nproc)
export LD_LIBRARY_PATH=/usr/local/mysql/lib/
```

Use `./src/sysbench` for running benchmarks unless installed globally.

## Create a dataset with sysbench

Run `sysbench` with the `prepare` option:

```bash
./src/sysbench \
  --db-driver=mysql \
  --mysql-host=127.0.0.1 \
  --mysql-db=bench \
  --mysql-user=bench \
  --mysql-password=bench \
  --mysql-port=3306 \
  --tables=8 \
  --table-size=10000 \
  --threads=1 \
  src/lua/oltp_read_write.lua prepare
```

## Shutdown MySQL and snapshot dataset for fast reuse 

Do these steps once at the start from MySQL source directory

```bash
bin/mysqladmin -u root shutdown
mv data data-orig
```

This saves the populated dataset before benchmarking.

```bash
rm -rf /dev/shm/dataset
cp -R data-orig/ /dev/shm/dataset
```

From MySQL source directory,

```bash
ln -s /dev/shm/dataset/ data
```

This links the MySQL --datadir to a fast in-memory copy, ensuring every test starts from a clean, identical state.

## Instrument the binary with BOLT

Use `llvm-bolt` to create an instrumented version of the binary:

```bash
llvm-bolt $HOME/mysql-server/build/bin/mysqld \
  -instrument \
  -o $HOME/mysql-server/build/bin/mysqldreadonly.instrumented \
  --instrumentation-file=$HOME/mysql-server/build/profile-readonly.fdata \
  --instrumentation-sleep-time=5 \
  --instrumentation-no-counters-clear \
  --instrumentation-wait-forks \
  2>&1 | tee $HOME/mysql-server/bolt-instrumentation-readonly.log
```

### Explanation of key options

- `-instrument`: Enables profile generation instrumentation
- `--instrumentation-file`: Path where the profile output will be saved
- `--instrumentation-wait-forks`: Ensures the instrumentation continues through forks (important for daemon processes)

## Run the instrumented binary under a feature-specific workload

Start the MySQL instrumented binary in first terminal. 

Use a workload generator to stress the binary in a feature-specific way. For example, to simulate **read-only traffic** with sysbench:

```bash
taskset -c 7 ./src/sysbench \
  --db-driver=mysql \
  --mysql-host=127.0.0.1 \
  --mysql-db=bench \
  --mysql-user=bench \
  --mysql-password=bench \
  --mysql-port=3306 \
  --tables=8 \
  --table-size=10000 \
  --forced-shutdown \
  --report-interval=60 \
  --rand-type=uniform \
  --time=5 \
  --threads=1 \
  --simple-ranges=1 \
  --distinct-ranges=1 \
  --sum-ranges=1 \
  --order-ranges=1 \
  --point-selects=10 \
  src/lua/oltp_read_only.lua run
```

{{% notice Note %}}
On an 8-core system, cores are numbered 0-7. Adjust the `taskset -c` values as needed for your system. Avoid using the same core for both mysqld and sysbench to reduce contention. You can increase this time (e.g., --time=5 or --time=300) for more statistically meaningful profiling and better .fdata data.
{{% /notice %}} 

The `.fdata` file defined in `--instrumentation-file` will be populated with runtime execution data.

After completing each benchmark run (e.g. after sysbench run), you must cleanly shut down the MySQL server and reset the dataset to ensure the next test starts from a consistent state.
```bash
bin/mysqladmin -u root shutdown ; rm -rf /dev/shm/dataset ; cp -R data/ /dev/shm/dataset
```

## Verify the profile was created

After running the workload:

```bash
ls -lh $HOME/mysql-server/build/profile-readonly.fdata
```

You should see a non-empty file. This file will later be merged with other profiles (e.g., for write-only traffic) to generate a complete merged profile.

