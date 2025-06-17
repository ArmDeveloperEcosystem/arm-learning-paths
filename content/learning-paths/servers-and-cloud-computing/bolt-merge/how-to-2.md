---
title: Instrument MySQL with BOLT 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, you will use BOLT to instrument the MySQL application binary and to collect profile data for specific workloads. 

The collected profiles will be merged with others and used to optimize the application's code layout.

## Build mysqld from source 

Follow these steps to build the MySQL server (`mysqld`) from source:

Install the required dependencies:

```bash
sudo apt update
sudo apt install -y build-essential cmake libncurses5-dev libssl-dev libboost-all-dev bison pkg-config libaio-dev libtirpc-dev git
```

Download the MySQL source code. You can change to another version in the `checkout` command below if needed. 

```bash
git clone https://github.com/mysql/mysql-server.git
cd mysql-server
git checkout mysql-8.4.5
```

Configure the build for debug:

```bash
mkdir build && cd build
cmake ..  -DCMAKE_BUILD_TYPE=RelWithDebInfo -DWITH_DEBUG=1 -DCMAKE_C_FLAGS="-fno-omit-frame-pointer" \
  -DCMAKE_CXX_FLAGS="-fno-omit-frame-pointer" -DCMAKE_POSITION_INDEPENDENT_CODE=OFF \
  -DCMAKE_EXE_LINKER_FLAGS="-Wl,--emit-relocs" \
  -DCMAKE_EXE_LINKER_FLAGS="-no-pie"
```

Build mysqld:

```bash
make -j$(nproc)
```

After the build completes, the `mysqld` binary is located at `$HOME/mysql-server/build/runtime_output_directory/mysqld`

{{% notice Note %}}
You can run `mysqld` directly from the build directory as shown, or run `make install` to install it system-wide. For testing and instrumentation, running from the build directory is usually preferred.
{{% /notice %}} 

After building mysqld, install MySQL server and client utilities system-wide:

```bash
sudo make install
```

This will make the `mysql` client and other utilities available in your PATH.

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

## Instrument the binary with BOLT

Use `llvm-bolt` to create an instrumented version of the binary:

```bash
llvm-bolt $HOME/mysql-server/build/runtime_output_directory/mysqld \
  -instrument \
  -o $HOME/mysql-server/build/runtime_output_directory/mysqld.instrumented \
  --instrumentation-file=$HOME/mysql-server/build/profile-readonly.fdata \
  --instrumentation-sleep-time=5 \
  --instrumentation-no-counters-clear \
  --instrumentation-wait-forks
```

### Explanation of key options

- `-instrument`: Enables profile generation instrumentation
- `--instrumentation-file`: Path where the profile output will be saved
- `--instrumentation-wait-forks`: Ensures the instrumentation continues through forks (important for daemon processes)


## Start the instrumented MySQL server

Before running the workload, start the instrumented MySQL server in a separate terminal. You may need to initialize a new data directory if this is your first run:

```bash
# Initialize a new data directory (if needed)
$HOME/mysql-server/build/runtime_output_directory/mysqld.instrumented --initialize-insecure --datadir=$HOME/mysql-bolt-data

# Start the instrumented server
# On an 8-core system, use available cores (e.g., 6 for mysqld, 7 for sysbench)
taskset -c 6 $HOME/mysql-server/build/runtime_output_directory/mysqld.instrumented \
  --datadir=$HOME/mysql-bolt-data \
  --socket=$HOME/mysql-bolt.sock \
  --port=3306 \
  --user=$(whoami) &
```

Adjust `--datadir`, `--socket`, and `--port` as needed for your environment. Make sure the server is running and accessible before proceeding.

## Install sysbench

You will need sysbench to generate workloads for MySQL. On most Arm Linux distributions, you can install it using your package manager:

```bash
sudo apt update
sudo apt install -y sysbench
```

Alternatively, see the [sysbench GitHub page](https://github.com/akopytov/sysbench) for build-from-source instructions if a package is not available for your platform.

## Create a test database and user

For sysbench to work, you need a test database and user. Connect to the MySQL server as the root user (or another admin user) and run:

```bash
mysql -u root --socket=$HOME/mysql-bolt.sock
```

Then, in the MySQL shell:

```sql
CREATE DATABASE IF NOT EXISTS bench;
CREATE USER IF NOT EXISTS 'bench'@'localhost' IDENTIFIED BY 'bench';
GRANT ALL PRIVILEGES ON bench.* TO 'bench'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

## Run the instrumented binary under a feature-specific workload

Use a workload generator to stress the binary in a feature-specific way. For example, to simulate **read-only traffic** with sysbench:

```bash
taskset -c 7 sysbench \
  --db-driver=mysql \
  --mysql-host=127.0.0.1 \
  --mysql-db=bench \
  --mysql-user=bench \
  --mysql-password=bench \
  --mysql-port=3306 \
  --tables=8 \
  --table-size=10000 \
  --threads=1 \
  /usr/share/sysbench/oltp_read_only.lua run
```

{{% notice Note %}}
On an 8-core system, cores are numbered 0-7. Adjust the `taskset -c` values as needed for your system. Avoid using the same core for both mysqld and sysbench to reduce contention.
{{% /notice %}} 


The `.fdata` file defined in `--instrumentation-file` will be populated with runtime execution data.

## Verify the profile was created

After running the workload:

```bash
ls -lh $HOME/mysql-server/build/profile-readonly.fdata
```

You should see a non-empty file. This file will later be merged with other profiles (e.g., for write-only traffic) to generate a complete merged profile.

