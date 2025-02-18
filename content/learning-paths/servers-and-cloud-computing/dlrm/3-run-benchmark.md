---
title: Run the benchmark
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark script

The repository contains a bash script to run the benchmark. At a glance, these are the steps it goes through:

- Sets up MLPerf repositories within the container.
- Dumps the model from existing model weights if not already available.
- Calibrates the INT8 model from the dumped model if it has not been previously generated.
- Executes the offline benchmark test, generating terabyte-scale binary data files during the process.

```bash
cd $HOME/dlrm_docker_setup
./run_dlrm_benchmark.sh int8

# fp32 offline test
./run_dlrm_benchmark.sh fp32
```

## Save output files

You may want to save the final model and data files to run on smaller servers. You can use `scp` to achieve this.

From your long-term storage machine, run the following command. You need to update the parameters before running.

```
scp -i <key-pair> <username>@<ipaddress>:/remote/path/to/file $HOME/model/int8/
```
where `key-pair` is the key-pair used for the larger instance, `username` and `ipaddress` the corresponding access points, and the two paths are the source and destination paths respectively.

Save the following files for long-term storage.

```console
$HOME/model/aarch64_dlrm_int8.pt
$HOME/model/dlrm-multihot-pytorch.pt
$HOME/data/terabyte_processed_test_v2_dense.bin
$HOME/data/terabyte_processed_test_v2_label_sparse.bin
```

To run the INT8 model, an instance with 250 GB of RAM and 500 GB of disk space is enough. For example, the following instance types:


|         CSP           |  Instance type |
| --------------------- | -------------- |
| Google Cloud Platform | c4a-highmem-32 |
| Amazon Web Services   | r8g.8xlarge    |
| Microsoft Azure       | TODO           |

For example, you can re-run the offline INT8 benchmark by cloning the repository to the smaller instance and the following command.
```bash
./run_main.sh offline int8
```

## Understanding the results

As a final step, have a look at the results generated in a text file.
```bash
cat $HOME/results/int8/mlperf_log_summary.txt
```

It should look something like this. Note the ....

```output
================================================
MLPerf Results Summary
================================================
SUT name : PyFastSUT
Scenario : Offline
Mode     : PerformanceOnly
Samples per second: 1434.8
Result is : VALID
  Min duration satisfied : Yes
  Min queries satisfied : Yes
  Early stopping satisfied: Yes

================================================
Additional Stats
================================================
Min latency (ns)                : 124022373
Max latency (ns)                : 883187615166
Mean latency (ns)               : 442524059715
50.00 percentile latency (ns)   : 442808926434
90.00 percentile latency (ns)   : 794977004363
95.00 percentile latency (ns)   : 839019402197
97.00 percentile latency (ns)   : 856679847578
99.00 percentile latency (ns)   : 874336993877
99.90 percentile latency (ns)   : 882255616119

================================================
Test Parameters Used
================================================
samples_per_query : 1267200
target_qps : 1920
target_latency (ns): 0
max_async_queries : 1
min_duration (ms): 600000
max_duration (ms): 0
min_query_count : 1
max_query_count : 0
qsl_rng_seed : 6023615788873153749
sample_index_rng_seed : 15036839855038426416
schedule_rng_seed : 9933818062894767841
accuracy_log_rng_seed : 0
accuracy_log_probability : 0
accuracy_log_sampling_target : 0
print_timestamps : 0
performance_issue_unique : 0
performance_issue_same : 0
performance_issue_same_index : 0
performance_sample_count : 204800
```