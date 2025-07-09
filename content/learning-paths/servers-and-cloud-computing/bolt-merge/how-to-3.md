---
title: Run a new workload using BOLT and merge the results
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, you’ll collect profile data for a write-heavy workload and merge it with the read-heavy profile from the previous step. The merged profile captures a broader set of execution behaviors for optimizing the final binary.

## Run a write-only workload for the application binary

You can reuse the previously built MySQL binary or generate a new instrumented variant if needed.

Use the same BOLT-instrumented MySQL binary and drive it with a write-only workload to capture `profile-writeonly.fdata`

For this you can reuse the existing instrumented binary, rename .fdata appropriately for read and write workloads or run llvm-bolt with new file target. 
```bash
llvm-bolt $HOME/mysql-server/build/bin/mysqld \
  -instrument \
  -o $HOME/mysql-server/build/bin/mysqldwriteonly.instrumented \
  --instrumentation-file=$HOME/mysql-server/build/profile-writeonly.fdata \
  --instrumentation-sleep-time=5 \
  --instrumentation-no-counters-clear \
  --instrumentation-wait-forks \
  2>&1 | tee $HOME/mysql-server/bolt-instrumentation-writeonly.log
```

## Run the write-only workload

Run Sysbench using the write-only Lua script to generate a workload profile:

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
  src/lua/oltp_write_only.lua run
```

Make sure that the `--instrumentation-file` points to `profile-writeonly.fdata` to collect the write-only profile.

## Reset the dataset after profiling

After running each benchmark, cleanly shut down the MySQL server reset the in-memory dataset to ensure the next run starts in a consistent state:

```bash
./bin/mysqladmin -u root shutdown ; rm -rf /dev/shm/dataset ; cp -R data/ /dev/shm/dataset
```
### Check that both profiles exist

Verify that the following `.fdata` files have been generated:

```bash
ls -lh $HOME/mysql-server/build/profile-readonly.fdata
ls -lh $HOME/mysql-server/build/profile-writeonly.fdata
```
### Merge the read and write profiles

Both `.fdata` files should now exist and contain valid data:

- `profile-readonly.fdata`
- `profile-writeonly.fdata`

### Merge the Feature Profiles

Use `merge-fdata` to combine the feature-specific profiles into one comprehensive `.fdata` file:

```bash
merge-fdata $HOME/mysql-server/build/profile-readonly.fdata $HOME/mysql-server/build/profile-writeonly.fdata \
  -o $HOME/mysql-server/build/profile-merged.fdata
```

Output:

```
Using legacy profile format.
Profile from 2 files merged.
```

This creates a single merged profile (`profile-merged.fdata`) covering both read-only and write-only workload behaviors.

### Verify the Merged Profile

Confirm the merged profile file exists and is non-empty:

```bash
ls -lh $HOME/mysql-server/build/profile-merged.fdata
```

### Optimize the binary using the merged profile

Use LLVM-BOLT to generate the final optimized binary using the merged `.fdata` file:

```bash
llvm-bolt $HOME/mysql-server/build/bin/mysqld \
  -o $HOME/mysql-server/build/bin/mysqldreadwrite_merged.bolt_instrumentation \
  -data=$HOME/mysql-server/build/profile-merged.fdata \
  -reorder-blocks=ext-tsp \
  -reorder-functions=hfsort \
  -split-functions \
  -split-all-cold \
  -split-eh \
  -dyno-stats \
  --print-profile-stats \
  2>&1 | tee $HOME/mysql-server/build/bolt-readwritemerged-opt.log
```

This command optimizes the binary layout based on the merged workload profile, creating a single binary (`mysqldreadwrite_merged.bolt_instrumentation`) that is optimized across both features.


