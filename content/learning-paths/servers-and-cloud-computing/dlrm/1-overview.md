---
title: Overview and setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

DLRM is a machine learning model designed for recommendation systems, like those powering streaming services or online stores. It helps predict what a user might like, using embedding layers that convert categories into useful numerical representations, and multilayer perceptrons (MLPs) to process continuous data. The real magic happens in the feature interaction step, where DLRM figures out the most influential factors for making recommendations.

### Arm Neoverse CPUs

The Arm Neoverse V2 CPU is built for high-performance computing, making it ideal for machine learning workloads. Unlike traditional CPUs, it offers energy efficiency and scalability, ensuring it can handle AI tasks without excessive power consumption. It also includes advanced vector processing and memory optimizations, which help speed up AI model training and inference. Plus, with many cloud providers, such as AWS and GCP, offering Arm-based instances, deploying ML models becomes more cost-effective.

### About the benchmark

In this Learning Path, you'll learn how to evaluate the performance of the [DLRM using the MLPerf Inference suite](https://github.com/mlcommons/inference/tree/master/recommendation/dlrm_v2/pytorch) in the _Offline_ scenario. The Offline scenario is a test scenario where large batches of data are processed all at once, rather than in real-time. It simulates large-scale, batch-style inference tasks commonly found in recommendation systems for e-commerce, streaming, and social platforms.

You will run tests that measure throughput (samples per second) and latency, providing insights into how efficiently the model runs on the target system. By using MLPerf’s standardized methodology, you'll gain reliable insights that help compare performance across different hardware and software configurations — highlighting the system’s ability to handle real-world, data-intensive AI workloads.

## Configure your environment

Before you can run the benchmark, you'll need an Arm-based instance from a Cloud Service Provider (CSP). The instructions in this Learning Path have been tested on the two Arm-based instances listed below running Ubuntu 22.04.

|         CSP           |  Instance type |
| --------------------- | -------------- |
| Google Cloud Platform | c4a-highmem-72 |
| Amazon Web Services   | r8g.16xlarge   |

### Verify Python installation
On your running Arm-based instance, make sure Python is installed by running the following command and checking the version:

```bash
python3 --version
```

The version is printed:

```output
Python 3.10.12
```

With your development environment set up, you can move on to downloading and running the model.
