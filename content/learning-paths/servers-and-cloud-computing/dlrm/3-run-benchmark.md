---
title: Run the benchmark
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you will run the benchmark and inspect the results.

## Build PyTorch

You will use a commit hash of the the `Tool-Solutions` repository to set up a Docker container with PyTorch. It will includes releases of PyTorch which enhance the performance of ML frameworks on Arm.

```bash
cd $HOME
git clone https://github.com/ARM-software/Tool-Solutions.git
cd $HOME/Tool-Solutions/
git checkout f606cb6276be38bbb264b5ea64809c34837959c4
```

The `build.sh` script builds a wheel and a Docker image containing a PyTorch wheel and dependencies. It then runs the MLPerf container which is used for the benchmark in the next section. This script takes around 20 minutes to finish.

```bash
cd ML-Frameworks/pytorch-aarch64/
./build.sh
```

You now have everything set up to analyze the performance. Proceed to the next section to run the benchmark and inspect the results.

## Run the benchmark

 A repository is set up to run the next steps. This collection of scripts streamlines the process of building and running the DLRM (Deep Learning Recommendation Model) benchmark from the MLPerf suite inside a Docker container, tailored for Arm-based systems.

Start by cloning it.

 ```bash
 cd $HOME
 git clone https://github.com/ArmDeveloperEcosystem/dlrm-mlperf-lp.git
 ```

The main script is the `run_dlrm_benchmark.sh`. At a glance, it automates the full workflow of executing the MLPerf DLRM benchmark by performing the following steps:

* Initializes and configures MLPerf repositories within the container.
* Applies necessary patches (from `mlperf_patches/`) and compiles the MLPerf codebase inside the container.
* Converts pretrained weights into a usable model format.
* Performs INT8 calibration if needed.
* Executes the offline benchmark test, generating large-scale binary data during runtime.

```bash
cd dlrm-mlperf-lp
./run_dlrm_benchmark.sh int8
```

The script can take an hour or more to run.

{{% notice Note %}}

To run the `fp32` offline test, it's recommended to use the pre-generated binary data files from the int8 tests. You will need a CSP instance with enough RAM. For this purpose, the AWS `r8g.24xlarge` is recommended. After running the `int8` test, save the files in the `model` and `data` directories, and copy them to the instance intended for the `fp32` benchmark.
{{% /notice %}}

## Understanding the results

As a final step, have a look at the results generated in a text file.

The DLRM model optimizes the Click-Through Rate (CTR) prediction. It is a fundamental task in online advertising, recommendation systems, and search engines. Essentially, the model estimates the probability that a user will click on a given ad, product recommendation, or search result. The higher the predicted probability, the more likely the item is to be clicked. In a server context, the goal is to observe a high through-put of these probabilities.

```bash
cat $HOME/results/int8/mlperf_log_summary.txt
```

Your output should contain a `Samples per second`, where each sample tells probability of the user clicking a certain ad.

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

On successfully running the benchmark, you’ve gained practical experience in evaluating large-scale AI recommendation systems in a reproducible and efficient manner—an essential skill for deploying and optimizing AI workloads on modern platforms.