---
title: Run the benchmark
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll run a modified version of the [MLPerf benchmark for DLRM](https://github.com/mlcommons/inference_results_v4.0/tree/main/closed/Intel/code/dlrm-v2-99.9/pytorch-cpu-int8) and inspect the results.

You'll use a nightly PyTorch wheel that features optimizations designed to improve the performance of recommendation models on Arm.


## Run the benchmark

The scripts to set up and run the benchmark are included for your convenience in a repository. This collection of scripts streamlines the process of building and running the DLRM (Deep Learning Recommendation Model) benchmark from the MLPerf suite tailored for Arm-based systems.

Start by cloning the repository:

 ```bash
 cd $HOME
 git clone https://github.com/ArmDeveloperEcosystem/dlrm-mlperf-lp.git
 ```

Set the environment variables to point to the downloaded data and model weights:

```
export DATA_DIR=$HOME/data
export MODEL_DIR=$HOME/model
```

You can now run the main script `run_dlrm_benchmark.sh`. This script automates the full workflow of executing the MLPerf DLRM benchmark by performing the following steps:

* Initializes and configures the MLPerf repositories.
* Applies required patches (from `mlperf_patches/`) and compiles the MLPerf codebase.
* Leverages PyTorch nightly wheel `torch==2.8.0.dev20250324+cpu` with the Arm performance improvements.
* Converts pretrained weights into a usable model format.
* Performs INT8 calibration if needed.
* Executes the offline benchmark test, generating large-scale binary data during runtime.

```bash
cd dlrm-mlperf-lp
./run_dlrm_benchmark.sh int8
```

The benchmark process can take an hour or more to complete.

{{% notice Note %}}

For the `fp32` offline test, it's recommended to use the pre-generated binary data files from the int8 tests. You will need a CSP instance with sufficient RAM. For this purpose, the AWS `r8g.24xlarge` is recommended. After running the `int8` test, save the files in the `model` and `data` directories, and copy them to the instance intended for the `fp32` benchmark.
{{% /notice %}}

## Reading the results

Once the script completes, look at the results to evaluate performance.

The DLRM model optimizes the Click-Through Rate (CTR) prediction. This is a fundamental task in online advertising, recommendation systems, and search engines. Essentially, the model estimates the probability of a user clicking on an ad, product recommendation, or search result. The higher the predicted probability, the more likely the item is to be clicked. In a server context, the goal is to observe a high throughput of these probabilities.

The output is also saved in a log file:

```bash
cat $HOME/results/int8/mlperf_log_summary.txt
```

Your output should contain a `Samples per second` entry, where each sample tells probability of the user clicking a certain ad.

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

By successfully running the benchmark, you've gained practical experience in evaluating large-scale AI recommendation systems in a reproducible and efficient manner, an essential skill for deploying and optimizing AI workloads on modern platforms.
