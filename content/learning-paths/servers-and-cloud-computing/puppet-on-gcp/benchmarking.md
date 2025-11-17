---
title: Puppet Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


##  Puppet Benchmark on GCP SUSE Arm64 VM

This guide explains how to perform a **Puppet standalone benchmark** on a **Google Cloud Platform (GCP) SUSE Linux Arm64 VM**.  
It measures Puppet’s local execution performance without requiring a Puppet Master.


### Prerequisites
Ensure that Puppet is installed and functioning correctly:

```console
puppet --version
```
Output:
```output
8.10.0
```

### Create a Benchmark Manifest
Create a directory and a simple manifest file:

```console
cd ~
mkdir -p ~/puppet-benchmark
cd ~/puppet-benchmark
vi benchmark.pp
```

Add the following content to the `benchmark.pp`:

```puppet
notify { 'Benchmark Test':
  message => 'Running Puppet standalone benchmark.',
}
```

- **notify** is a built-in Puppet resource type that displays a message during catalog application (like a print or log message).
- **'Benchmark Test'** is the title of the resource — a unique identifier for this notify action.
- **message => 'Running Puppet standalone benchmark.'** specifies the text message Puppet will print when applying the manifest.

### Run the Benchmark Command
This step runs Puppet in standalone mode using the `apply` command to execute the benchmark manifest locally while measuring execution time and performance statistics.

```console
time puppet apply benchmark.pp --verbose
```
This executes the manifest locally and outputs timing statistics.

You should see an output similar to:
```output
Notice: Compiled catalog for danson-puppet-2.c.arm-deveco-stedvsl-prd.internal in environment production in 0.01 seconds
Info: Using environment 'production'
Info: Applying configuration version '1763407825'
Notice: Running Puppet standalone benchmark.
Notice: /Stage[main]/Main/Notify[Benchmark Test]/message: defined 'message' as 'Running Puppet standalone benchmark.'
Notice: Applied catalog in 0.01 seconds

real    0m1.054s
user    0m0.676s
sys     0m0.367s
```

### Benchmark Metrics Explanation

- **Compiled catalog** → Puppet compiled your manifest into an execution plan.  
- **Applied catalog** → Puppet executed the plan on your system.  
- **real** → Total elapsed wall time (includes CPU + I/O).  
- **user** → CPU time spent in user-space.  
- **sys** → CPU time spent in system calls.  

### Benchmark results
The above results were executed on a `c4a-standard-4` (4 vCPU, 16 GB memory) Axiom Arm64 VM in GCP running SuSE:

| **Metric / Log** | **Output** |
|-------------------|------------|
| Compiled catalog | 0.01 seconds |
| Environment | production |
| Applied catalog | 0.01 seconds |
| real | 0m1.054s |
| user | 0m0.676s |
| sys | 0m0.367s |

### Puppet benchmarking summary

- **Catalog compilation:** Completed in just **0.01 seconds**, showing excellent processing speed on **Arm64**.
- **Environment:** Executed smoothly under the **production** environment.
- **Configuration version:** Recorded as **1763407825**, confirming successful version tracking.
- **Catalog application:** Finished in **0.01 seconds**, demonstrating very low execution latency.
- **Real time:** Total runtime of **1.054 seconds**, reflecting efficient end.
