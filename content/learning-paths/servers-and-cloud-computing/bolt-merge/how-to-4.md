---
title: BOLT the Libraries separately
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
### Step 1: Instrument Shared Libraries (e.g., libcrypto, libssl)

If system libraries like `/usr/lib/libssl.so` are stripped, rebuild OpenSSL from source with relocations:

```bash
git clone https://github.com/openssl/openssl.git
cd openssl
./config -O2 -Wl,--emit-relocs --prefix=$HOME/bolt-libs/openssl
make -j$(nproc)
make install
```

---

### Step 2: BOLT-Instrument libssl.so.3

Use `llvm-bolt` to instrument `libssl.so.3`:

```bash
llvm-bolt $HOME/bolt-libs/openssl/lib/libssl.so.3 \\
  -instrument \\
  -o $HOME/bolt-libs/openssl/lib/libssl.so.3.instrumented \\
  --instrumentation-file=libssl-readwrite.fdata \\
  --instrumentation-sleep-time=5 \\
  --instrumentation-no-counters-clear \\
  --instrumentation-wait-forks
```

Then launch MySQL using the **instrumented shared library** and run a **read+write** sysbench test to populate the profile:

---

### Step 3: Optimize 'libssl.so' Using Its Profile

After running the read+write test, ensure `libssl-readwrite.fdata` is populated.


Run BOLT on the uninstrumented `libssl.so` with the collected read-write profile:

```bash
llvm-bolt /path/to/libssl.so.3 \\
  -o /path/to/libssl.so.optimized \\
  -data=/path/to/prof-instrumentation-libssl-readwrite.fdata \\
  -reorder-blocks=ext-tsp \\
  -reorder-functions=hfsort \\
  -split-functions \\
  -split-all-cold \\
  -split-eh \\
  -dyno-stats \\
  --print-profile-stats
```

---

### Step 3: Replace the Library at Runtime

Copy the optimized version over the original and export the path:

```bash
cp /path/to/libssl.so.optimized /path/to/libssl.so.3
export LD_LIBRARY_PATH=/path/to/
```

This ensures MySQL will dynamically load the optimized `libssl.so`.

---

### Step 4: Run Final Workload and Validate Performance

Start the BOLT-optimized MySQL binary and link it against the optimized `libssl.so`. Run the combined workload:

```bash
taskset -c 9 ./src/sysbench \\
  --db-driver=mysql \\
  --mysql-host=127.0.0.1 \\
  --mysql-db=bench \\
  --mysql-user=bench \\
  --mysql-password=bench \\
  --mysql-port=3306 \\
  --tables=8 \\
  --table-size=10000 \\
  --threads=1 \\
  src/lua/oltp_read_write.lua run
```

---

In the next step, you'll optimize an additional critical external library (`libcrypto.so`) using BOLT, following a similar process as `libssl.so`. Afterward, you'll interpret performance results to validate and compare optimizations across baseline and merged
 scenarios.

### Step 1: BOLT optimization for 'libcrypto.so'

Follow these steps to instrument and optimize `libcrypto.so`:

#### Instrument `libcrypto.so`:

```bash
llvm-bolt /path/to/libcrypto.so.3 \\
  -instrument \\
  -o /path/to/libcrypto.so.3.instrumented \\
  --instrumentation-file=libcrypto-readwrite.fdata \\
  --instrumentation-sleep-time=5 \\
  --instrumentation-no-counters-clear \\
  --instrumentation-wait-forks
```

Run MySQL under the read-write workload to populate `libcrypto-readwrite.fdata`:

```bash
export LD_LIBRARY_PATH=/path/to/libcrypto-instrumented
taskset -c 9 ./src/sysbench \\
  --db-driver=mysql \\
  --mysql-host=127.0.0.1 \\
  --mysql-db=bench \\
  --mysql-user=bench \\
  --mysql-password=bench \\
  --mysql-port=3306 \\
  --tables=8 \\
  --table-size=10000 \\
  --threads=1 \\
  src/lua/oltp_read_write.lua run
```

#### Optimize the `libcrypto.so` library:

```bash
llvm-bolt /path/to/original/libcrypto.so.3 \\
  -o /path/to/libcrypto.so.optimized \\
  -data=libcrypto-readwrite.fdata \\
  -reorder-blocks=ext-tsp \\
  -reorder-functions=hfsort \\
  -split-functions \\
  -split-all-cold \\
  -split-eh \\
  -dyno-stats \\
  --print-profile-stats
```

Replace the original at runtime:

```bash
cp /path/to/libcrypto.so.optimized /path/to/libcrypto.so.3
export LD_LIBRARY_PATH=/path/to/
```

Run a final validation workload to ensure functionality and measure performance improvements.

