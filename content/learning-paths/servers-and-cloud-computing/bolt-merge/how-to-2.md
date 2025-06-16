---
title: BOLT Optimization - First feature
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, you will use BOLT to instrument the MySQL application binary and to collect profile data for specific workloads. 

The collected profiles will be merged with others and used to optimize the application's code layout.

### Build the uninstrumented binary

Make sure your application binary is:

- Built from source (e.g., `mysqld`)
- Unstripped, with symbol information available
- Compiled with frame pointers enabled (`-fno-omit-frame-pointer`)

You can verify this with:

```bash
readelf -s /path/to/mysqld | grep main
```

If the symbols are missing, rebuild the binary with debug info and no stripping.

### Step 2: Instrument the binary with BOLT

Use `llvm-bolt` to create an instrumented version of the binary:

```bash
llvm-bolt /path/to/mysqld \\
  -instrument \\
  -o /path/to/mysqld.instrumented \\
  --instrumentation-file=/path/to/profile-readonly.fdata \\
  --instrumentation-sleep-time=5 \\
  --instrumentation-no-counters-clear \\
  --instrumentation-wait-forks
```

### Explanation of key options

- `-instrument`: Enables profile generation instrumentation
- `--instrumentation-file`: Path where the profile output will be saved
- `--instrumentation-wait-forks`: Ensures the instrumentation continues through forks (important for daemon processes)

---

### Step 3: Run the instrumented binary under a feature-specific workload

Use a workload generator to stress the binary in a feature-specific way. For example, to simulate **read-only traffic** with sysbench:

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
  src/lua/oltp_read_only.lua run
```

> Adjust this command as needed for your workload and CPU/core binding.

The `.fdata` file defined in `--instrumentation-file` will be populated with runtime execution data.

---

### Step 4: Verify the profile was created

After running the workload:

```bash
ls -lh /path/to/profile-readonly.fdata
```

You should see a non-empty file. This file will later be merged with other profiles (e.g., for write-only traffic) to generate a complete merged profile.

