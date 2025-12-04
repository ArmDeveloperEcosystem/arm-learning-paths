---
title: Benchmark Puppet
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


##  Benchmark Puppet on a GCP SUSE Arm64 VM

This guide explains how to perform a Puppet standalone benchmark on a Google Cloud Platform (GCP) SUSE Linux Arm64 VM. It measures Puppet’s local execution performance without requiring a Puppet Master.


## Prerequisites
Ensure that Puppet is installed and functioning correctly:

```console
puppet --version
```
Output:
```output
8.10.0
```

## Create a benchmark manifest
Create a directory and a simple manifest file:

```console
cd ~
mkdir -p ~/puppet-benchmark
cd ~/puppet-benchmark
```

Use an editor to create the following content in a file named `benchmark.pp`:

```puppet
notify { 'Benchmark Test':
  message => 'Running Puppet standalone benchmark.',
}
```

### Explore the code 

Here is a breakdown of the key elements in the `benchmark.pp` manifest to help you understand how Puppet processes and displays information during the benchmark:

- `notify` is a built-in Puppet resource type that displays a message during catalog application (like a print or log message).
- `Benchmark Test` is the title of the resource. It's a unique identifier for this notify action.
- `message => 'Running Puppet standalone benchmark.'` specifies the text message Puppet prints when applying the manifest.


## Run the benchmark command
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

## Interpret the benchmark metrics
Here is a breakdown of the key benchmark metrics you will see in the output:

- `Compiled catalog`: Puppet parsed your manifest and generated a catalog, which is an execution plan describing the desired system state. This metric shows how quickly Puppet can process and prepare your configuration for application. Fast compilation times indicate efficient manifest design and good platform performance.
- `Applied catalog`: Puppet applied the compiled catalog to your VM, making the necessary changes to reach the desired state. This value reflects how quickly Puppet can enforce configuration changes on your Arm64 system. Low application times suggest minimal system overhead and effective resource management.
- `real`: This is the total elapsed wall-clock time from start to finish of the `puppet apply` command. It includes all time spent running the process, waiting for I/O, and any other delays. Lower real times mean faster end-to-end execution, which is important for automation and scaling.
- `user`: This measures the amount of CPU time spent executing user-space code (Puppet and Ruby processes) during the benchmark. High user time relative to real time can indicate CPU-bound workloads, while lower values suggest efficient code execution.
- `sys`: This is the CPU time spent in system (kernel) calls, such as file operations or network access. Lower sys times are typical for lightweight manifests, while higher values may indicate more intensive system interactions or I/O operations.

## Benchmark results

The following table summarizes the benchmark metrics collected from running Puppet on a `c4a-standard-4` (4 vCPU, 16 GB memory) Axiom Arm64 VM in Google Cloud Platform (GCP) with SUSE Linux. These results provide a baseline for evaluating Puppet’s performance on Arm64 infrastructure. Use this data to compare against other VM types or architectures, and to identify areas for further optimization.

| Metric / Log   | Output    |
|--------------------|--------------|
| Compiled catalog   | 0.01 seconds |
| Environment        | production   |
| Applied catalog    | 0.01 seconds |
| real               | 0m1.054s     |
| user               | 0m0.676s     |
| sys                | 0m0.367s     |

These metrics reflect efficient catalog compilation and application times, as well as low system overhead, demonstrating the strong performance of Puppet on Arm64-based GCP VMs.

## Review Puppet benchmarking results

Confirm that your benchmark output matches the expected metrics for catalog compilation, application, and system resource usage. If your results differ significantly, investigate VM resource allocation, manifest complexity, or system load. Use these metrics to validate Puppet performance on Arm64 and identify opportunities for further optimization.

These benchmark results demonstrate that catalog compilation completed in only 0.01 seconds, highlighting the processing speed of the Arm64 platform. The benchmark ran smoothly in the production environment, and the configuration version was successfully recorded as 1763407825. Catalog application also finished in 0.01 seconds, indicating very low execution latency. The total runtime was 1.054 seconds, which reflects efficient overall performance for Puppet on an Arm64 SUSE VM in Google Cloud Platform.

This benchmarking method is useful for validating Puppet performance after migration to Arm64, or when optimizing infrastructure for cost and speed. For more advanced benchmarking, consider automating multiple runs, collecting metrics over time, and comparing results with x86-based VMs to quantify the benefits of Arm64 on GCP.
