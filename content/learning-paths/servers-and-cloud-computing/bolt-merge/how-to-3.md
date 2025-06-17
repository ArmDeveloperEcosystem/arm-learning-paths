---
title: BOLT Optimization - Second Feature & BOLT Merge to combine 
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, you'll collect profile data for a **write-heavy** workload and also **instrument external libraries** such as `libcrypto.so` and `libssl.so` used by the application (e.g., MySQL).


### Step 1: Run Write-Only Workload for Application Binary

Use the same BOLT-instrumented MySQL binary and drive it with a write-only workload to capture `profile-writeonly.fdata`:

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
  src/lua/oltp_write_only.lua run
```

Make sure that the `--instrumentation-file` is set appropriately to save `profile-writeonly.fdata`.
---
### Step 2: Verify the Second Profile Was Generated

```bash
ls -lh /path/to/profile-writeonly.fdata
```

Both `.fdata` files should now exist and contain valid data:

- `profile-readonly.fdata`
- `profile-writeonly.fdata`

---

### Step 3: Merge the Feature Profiles

Use `merge-fdata` to combine the feature-specific profiles into one comprehensive `.fdata` file:

```bash
merge-fdata /path/to/profile-readonly.fdata /path/to/profile-writeonly.fdata \\
  -o /path/to/profile-merged.fdata
```

**Example command from an actual setup:**

```bash
/home/ubuntu/llvm-latest/build/bin/merge-fdata prof-instrumentation-readonly.fdata prof-instrumentation-writeonly.fdata \\
  -o prof-instrumentation-readwritemerged.fdata
```

Output:

```
Using legacy profile format.
Profile from 2 files merged.
```

This creates a single merged profile (`profile-merged.fdata`) covering both read-only and write-only workload behaviors.

---

### Step 4: Verify the Merged Profile

Check the merged `.fdata` file:

```bash
ls -lh /path/to/profile-merged.fdata
```

---
### Step 5: Generate the Final Binary with the Merged Profile

Use LLVM-BOLT to generate the final optimized binary using the merged `.fdata` file:

```bash
llvm-bolt build/bin/mysqld \\
  -o build/bin/mysqldreadwrite_merged.bolt_instrumentation \\
  -data=/home/ubuntu/mysql-server-8.0.33/sysbench/prof-instrumentation-readwritemerged.fdata \\
  -reorder-blocks=ext-tsp \\
  -reorder-functions=hfsort \\
  -split-functions \\
  -split-all-cold \\
  -split-eh \\
  -dyno-stats \\
  --print-profile-stats 2>&1 | tee bolt_orig.log
```

This command optimizes the binary layout based on the merged workload profile, creating a single binary (`mysqldreadwrite_merged.bolt_instrumentation`) that is optimized across both features.


