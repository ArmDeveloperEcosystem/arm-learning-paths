---
title: Instrument shared libraries with BOLT
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you'll learn how to instrument and optimize shared libraries, and specifically, `libssl.so` and `libcrypto.so` using BOLT. These libraries are used by MySQL, and optimizing them can improve overall performance. You'll rebuild OpenSSL from source to include symbol information, then collect profiles and apply BOLT optimizations.

## Instrument Shared Libraries 

### Prepare instrumentable versions

If system libraries like `/usr/lib/libssl.so` are stripped, rebuild OpenSSL from source with relocations:

```bash
cd $HOME
git clone https://github.com/openssl/openssl.git
cd openssl
./config -O2 -Wl,--emit-relocs --prefix=$HOME/bolt-libs/openssl
make -j$(nproc)
make install
```

### Instrument libssl.so

Use `llvm-bolt` to instrument `libssl.so.3`:

```bash
llvm-bolt $HOME/bolt-libs/openssl/lib/libssl.so.3 \
  -instrument \
  -o $HOME/bolt-libs/openssl/lib/libssl.so.3.instrumented \
  --instrumentation-file=$HOME/bolt-libs/openssl/lib/libssl-readwrite.fdata \
  --instrumentation-sleep-time=5 \
  --instrumentation-no-counters-clear \
  --instrumentation-wait-forks \
  2>&1 | tee $HOME/mysql-server/bolt-instrumentation-libssl.log
```

Launch MySQL with the instrumented `libssl.so` and run a read+write Sysbench test to populate the profile

### Optimize libssl using the profile

After running the read+write test, ensure `libssl-readwrite.fdata` is populated.

Run BOLT on the uninstrumented `libssl.so` using the collected read+write profile:

```bash
llvm-bolt $HOME/bolt-libs/openssl/lib/libssl.so.3 \
  -o $HOME/bolt-libs/openssl/lib/libssl.so.optimized \
  -data=$HOME/bolt-libs/openssl/lib/libssl-readwrite.fdata \
  -reorder-blocks=ext-tsp \
  -reorder-functions=hfsort \
  -split-functions \
  -split-all-cold \
  -split-eh \
  -dyno-stats \
  --print-profile-stats \
  2>&1 | tee $HOME/mysql-server/build/bolt-libssl.log
```

### Replace the library at runtime

Copy the optimized version over the original and export the path:

```bash
# Set LD_LIBRARY_PATH in the terminal before launching mysqld in order for mysqld to pick the optimized library.
cp $HOME/bolt-libs/openssl/libssl.so.optimized $HOME/bolt-libs/openssl/lib/libssl.so.3
export LD_LIBRARY_PATH=$HOME/bolt-libs/openssl/lib

# You can confirm that mysqld is loading your optimized library with:
LD_LIBRARY_PATH=$HOME/bolt-libs/openssl/ 
ldd build/bin/mysqld | grep libssl
```

{{% notice tip %}}
Setting `LD_LIBRARY_PATH` ensures that MySQL dynamically links to the optimized shared library at runtime. This does not permanently override system libraries.
{{% /notice %}}

It should show:

```output
libssl.so.3 => /home/ubuntu/bolt-libs/openssl/libssl.so.3
```

This ensures MySQL will dynamically load the optimized `libssl.so`.

### Run the final workload and validate performance

Start the BOLT-optimized MySQL binary and link it against the optimized `libssl.so`. Run the combined workload:

```bash
# On an 8-core system, use available cores (e.g., 7 for sysbench)
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
  src/lua/oltp_read_write.lua run
```


In the next step, you'll optimize an additional critical external library (`libcrypto.so`) using BOLT, following a similar process as `libssl.so`. Afterward, you'll interpret performance results to validate and compare optimizations across baseline and merged scenarios.

### Optimize libcrypto.so with BOLT

Follow these steps to instrument and optimize `libcrypto.so`:

### Instrument libcrypto.so

```bash
llvm-bolt $HOME/bolt-libs/openssl/libcrypto.so.3 \
  -instrument \
  -o $HOME/bolt-libs/openssl/lib/libcrypto.so.3.instrumented \
  --instrumentation-file=$HOME/bolt-libs/openssl/lib/libcrypto-readwrite.fdata \
  --instrumentation-sleep-time=5 \
  --instrumentation-no-counters-clear \
  --instrumentation-wait-forks \
  2>&1 | tee $HOME/mysql-server/bolt-instrumentation-libcrypto.log
```
Launch MySQL using the instrumented shared library and run a read+write Sysbench test to populate the profile.

### Optimize libcrypto using the profile
After running the read+write test, ensure `libcrypto-readwrite.fdata` is populated.

Run BOLT on the uninstrumented libcrypto.so using the collected read+write profile to generate an optimized library:
```bash
llvm-bolt $HOME/bolt-libs/openssl/lib/libcrypto.so.3 \
  -o $HOME/bolt-libs/openssl/lib/libcrypto.so.optimized \
  -data=libcrypto-readwrite.fdata \
  -reorder-blocks=ext-tsp \
  -reorder-functions=hfsort \
  -split-functions \
  -split-all-cold \
  -split-eh \
  -dyno-stats \
  --print-profile-stats \
  2>&1 | tee $HOME/mysql-server/build/bolt-libcrypto.log
```

Replace the original at runtime:

```bash
# Set LD_LIBRARY_PATH in the terminal before launching mysqld in order for mysqld to pick the optimized library.
cp $HOME/bolt-libs/openssl/libcrypto.so.optimized $HOME/bolt-libs/openssl/lib/libcrypto.so.3
export LD_LIBRARY_PATH=$HOME/bolt-libs/openssl/

# You can confirm that mysqld is loading your optimized library with:
LD_LIBRARY_PATH=$HOME/bolt-libs/openssl/ ldd build/bin/mysqld | grep libcrypto
```

It should show:

```output
libcrypto.so.3 => /home/ubuntu/bolt-libs/openssl/libcrypto.so.3 
```

Run a final validation workload to ensure functionality and measure performance improvements.
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
  src/lua/oltp_read_write.lua run
```
