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

DCPerf is an open source benchmarking and microbenchmarking suite, originally developed by Meta, that faithfully replicates the characteristics of various general purpose data center workloads. One of the key differentiators to alternate benchmarking software is the fidelity of micro-architectural behaviour replicated by DCPerf, for example, cache misses, branch misprediction rate etc. 

The use cases of running DCPerf are to generate performance data to inform procurement decision and regression testing for changes in environment, such as kernel and compiler changes. This installation guide is to install DCPerf on Arm-based servers. This example has been tested on a AWS `c7g.metal` instance running Ubuntu 22.04 LTS. 

Please Note: When running on a server provided by a cloud service provided, you will have limit access to change parameters such as BIOS settings which can impact performance. 

## Install Prerequisites

Enter the default daemons to restart if asked.

```bash
sudo apt update
sudo apt install -y python3-pip git
sudo pip3 install click pyyaml tabulate pandas
```

Clone the repostory

```bash
git clone https://github.com/facebookresearch/DCPerf.git
cd DCPerf
```


## Running a the MediaWiki Benchmark

DCPerf offers many benchmarks, please refer the official documentation for the benchmark of your choice. In this example we will run the MediaWiki benchmark. The MediaWiki benchmark is designed to faithfully reproduce the workload of the facebook social networking site. First install the dependency.

```bash
wget https://github.com/facebookresearch/DCPerf/releases/download/hhvm/hhvm-3.30-multplatform-binary-ubuntu.tar.xz
tar -Jxf hhvm-3.30-multplatform-binary-ubuntu.tar.xz
cd hhvm
sudo ./pour-hhvm.sh
export LD_LIBRARY_PATH="/opt/local/hhvm-3.30/lib:$LD_LIBRARY_PATH"
```

Confirm `hhvm` is available with no link time issues. `hhvm` will be available in the `DCPerf/hhvm/aarch64-ubuntu22.04/hhvm-3.30/bin` directory. 

```bash
hhvm --version
```

You should see an output like the following with no errors. 

```output
HipHop VM 3.30.12 (rel)
Compiler: 1704922878_080332982
Repo schema: 4239d11395efb06bee3ab2923797fedfee64738e
```

Confirm security-enhanced Linux (SELinux) is disabled with the following commands. 

```bash
sudo apt install selinux-utils
getenforce
```

You should see the following response. If you do not see the `Disabled` output. Please refer to your distributions documentation on how to disable before proceeding.

```output
Disabled
```


The `install` argument to the `benchpress_cli.py` command line script can be used to automatially install all dependencies for each benchmark.  

```bash
sudo ./benchpress_cli.py install oss_performance_mediawiki_mlp
```

Please note this can take several minutes to do all the required steps. 


## Run the MediaWiki Benchmark

For sake of brevity we will pass in duration and timeout arguments through a `JSON` dictionary with the `-i` argument. 

```bash
sudo ./benchpress_cli.py run oss_performance_mediawiki_mlp -i '{
  "duration": "30s",
  "timeout": "1m"
}'
```

Whilst the benchmark is running you will be able to observe the various processes occupying the CPU.


Once the benchmark is complete, within the `DCPerf` directory a `benchmark_metrics_*` directory will be created with a `JSON` file for the system specs and metrics respectively. 
For example, the metrics file will list the 

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
