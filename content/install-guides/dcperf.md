---
title: DCPerf
author: Kieran Hejmadi
minutes_to_complete: 20
official_docs: https://github.com/facebookresearch/DCPerf?tab=readme-ov-file#install-and-run-benchmarks

additional_search_terms:
- linux
- Neoverse

test_images:
- ubuntu:22.04
test_maintenance: false

layout: installtoolsall
multi_install: false
multitool_install_part: false
tool_install: true
weight: 1
---

## Introduction

DCPerf is an open source benchmarking and microbenchmarking suite, originally developed by Meta, that faithfully replicates the characteristics of various general-purpose data center workloads. DCPerf stands out for its accurate replication of microarchitectural behaviors, such as cache misses and branch mispredictions, that many other benchmarking tools overlook.

DCPerf generates performance data to inform procurement decisions. You can also use it for regression testing to detect changes in the environment, such as kernel and compiler changes. 

You can install DCPerf on Arm-based servers. The examples below have been tested on an AWS `c7g.metal` instance running Ubuntu 22.04 LTS. 

{{% notice Note %}}
When running on a server provided by a cloud service, you have limited access to some parameters, such as UEFI settings, which can affect performance. 
{{% /notice %}}

## Install Prerequisites

To get started, install the required software:

```bash
sudo apt update
sudo apt install -y python-is-python3 python3-pip python3-venv git
```

It is recommended that you install Python packages in a Python virtual environment. 

Set up your virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```
If requested, restart the recommended services. 

Install the required packages:

```bash
pip3 install click pyyaml tabulate pandas
```

Clone the repository:

```bash
git clone https://github.com/facebookresearch/DCPerf.git
cd DCPerf
```

## Running the MediaWiki Benchmark

DCPerf offers many benchmarks. See the official documentation for the benchmark of your choice. 

One example is the MediaWiki benchmark, designed to faithfully reproduce the workload of the Facebook social networking site. 

Install HipHop Virtual Machine (HHVM), a virtual machine used to execute the web application code.

```bash
wget https://github.com/facebookresearch/DCPerf/releases/download/hhvm/hhvm-3.30-multplatform-binary-ubuntu.tar.xz
tar -Jxf hhvm-3.30-multplatform-binary-ubuntu.tar.xz
cd hhvm
sudo ./pour-hhvm.sh
export LD_LIBRARY_PATH="/opt/local/hhvm-3.30/lib:$LD_LIBRARY_PATH"
```

Confirm `hhvm` is available. The `hhvm` binary is located in the `DCPerf/hhvm/aarch64-ubuntu22.04/hhvm-3.30/bin` directory. 

```bash
hhvm --version
# Return to the DCPerf root directory
cd ..
```

You should see output similar to:

```output
HipHop VM 3.30.12 (rel)
Compiler: 1704922878_080332982
Repo schema: 4239d11395efb06bee3ab2923797fedfee64738e
```

Confirm security-enhanced Linux (SELinux) is disabled with the following commands: 

```bash
sudo apt install selinux-utils
getenforce
```

You should see the following response: 

```output
Disabled
```

If you do not see the `Disabled` output, see your Linux distribution documentation for information about how to disable SELinux.

You can automatically install all dependencies for each benchmark using the `install` argument with the `benchpress_cli.py` command-line script.   

```console
sudo ./benchpress_cli.py install oss_performance_mediawiki_mlp
```

This step might take several minutes to complete, depending on your system's download and setup speed.

## Run the MediaWiki Benchmark

For the sake of brevity, you can provide the duration and timeout arguments using a `JSON` dictionary with the `-i` argument:

```console
sudo ./benchpress_cli.py run oss_performance_mediawiki_mlp -i '{
  "duration": "30s",
  "timeout": "1m"
}'
```

While the benchmark is running, you can monitor CPU activity and observe benchmark-related processes using the `top` command.

When the benchmark is complete, a `benchmark_metrics_*` directory is created within the `DCPerf` directory, containing a `JSON` file for the system specs and another for the metrics.

For example, the metrics file lists the following:

```output
  "metrics": {
    "Combined": {
      "Nginx 200": 1817810,
      "Nginx 404": 79019,
      "Nginx 499": 3,
      "Nginx P50 time": 0.036,
      "Nginx P90 time": 0.056,
      "Nginx P95 time": 0.066,
      "Nginx P99 time": 0.081,
      "Nginx avg bytes": 158903.93039183,
      "Nginx avg time": 0.038826036781319,
      "Nginx hits": 1896832,
      "Wrk RPS": 3160.65,
      "Wrk failed requests": 79019,
      "Wrk requests": 1896703,
      "Wrk successful requests": 1817684,
      "Wrk wall sec": 600.1,
      "canonical": 0
    },
    "score": 2.4692578125
```

## Understanding the Benchmark Results

The metrics file contains several key performance indicators from the benchmark run:


- **Nginx 200, 404, 499**: The number of HTTP responses with status codes 200 (success), 404 (not found), and 499 (client closed request) returned by the Nginx web server during the test.
- **Nginx P50/P90/P95/P99 time**: The response time percentiles (in seconds) for requests handled by Nginx. For example, P50 is the median response time, P99 is the time under which 99% of requests completed.
- **Nginx avg bytes**: The average number of bytes sent per response.
- **Nginx avg time**: The average response time for all requests.
- **Nginx hits**: The total number of requests handled by Nginx.
- **Wrk RPS**: The average number of requests per second (RPS) generated by the `wrk` load testing tool.
- **Wrk failed requests**: The number of requests that failed during the test.
- **Wrk requests**: The total number of requests sent by `wrk`.
- **Wrk successful requests**: The number of requests that completed successfully.
- **Wrk wall sec**: The total wall-clock time (in seconds) for the benchmark run.
- **score**: An overall performance score calculated by DCPerf, which can be used to compare different systems or configurations.

{{% notice Note %}}
 `wrk` is a modern HTTP benchmarking tool used to generate load and measure web server performance. It is widely used for benchmarking because it can produce significant load and provides detailed statistics. For more information, see [wrk's GitHub page](https://github.com/wg/wrk).
{{% /notice %}}

These metrics help you evaluate the performance and reliability of the system under test. Higher values for successful requests and RPS, and lower response times, generally indicate better performance. The score provides a single value for easy comparison across runs or systems.

## Next Steps 

- Use the results to compare performance across different systems, hardware configurations, or after making system changes (e.g., kernel or compiler updates).
- Consider tuning system parameters or trying different DCPerf benchmarks to further evaluate your environment.
- Explore the other DCPerf benchmarks 
