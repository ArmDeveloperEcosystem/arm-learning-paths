---
title: Run a new workload using BOLT and merge the results
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Next, you will collect profile data for a **write-heavy** workload and merge the results with the **read-heavy** workload in the previous section. 

## Run Write-Only Workload for Application Binary

Use the same BOLT-instrumented MySQL binary and drive it with a write-only workload to capture `profile-writeonly.fdata`:

```bash
# On an 8-core system, use available cores (e.g., 7 for sysbench)
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
  /usr/share/sysbench/oltp_write_only.lua run
```

Make sure that the `--instrumentation-file` is set appropriately to save `profile-writeonly.fdata`.


### Verify the Second Profile Was Generated

```bash
ls -lh $HOME/mysql-server/build/profile-writeonly.fdata
```

Both `.fdata` files should now exist and contain valid data:

- `profile-readonly.fdata`
- `profile-writeonly.fdata`

### Merge the Feature Profiles

Use `merge-fdata` to combine the feature-specific profiles into one comprehensive `.fdata` file:

```bash
merge-fdata $HOME/mysql-server/build/profile-readonly.fdata $HOME/mysql-server/build/profile-writeonly.fdata \
  -o $HOME/mysql-server/build/profile-merged.fdata
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

### Verify the Merged Profile

Check the merged `.fdata` file:

```bash
ls -lh $HOME/mysql-server/build/profile-merged.fdata
```

### Generate the Final Binary with the Merged Profile

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


