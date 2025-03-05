---
title: Overview and setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

DLRM is a machine learning model designed for recommendation systems, like the ones used by streaming services or online stores. It helps predict what a user might like using embedding layers that turn categories into useful numerical representations, and multilayer perceptrons (MLPs) that process continuous data. The real magic happens in the feature interaction step, where DLRM figures out which factors matter most when making recommendations.

Arm Neoverse V2 is built for high-performance computing, making it a great fit for machine learning workloads. Unlike traditional CPUs, it's designed with energy efficiency and scalability in mind, which means it can handle AI tasks without consuming excessive power. It also includes advanced vector processing and memory optimizations, which help speed up AI model training and inference. Another advantage? Many cloud providers, like AWS and GCP, now offer Arm-based instances, making it easier to deploy ML models at a lower cost. Whether you’re training a deep learning model or running large-scale inference workloads, Neoverse V2 is optimized to deliver solid performance while keeping costs under control.

Running MLPerf benchmarks on Arm’s Neoverse V2 platform assesses how well models like DLRM perform on this architecture.

## Configure developer environment

Before you can run the benchmark, you will need an Arm-based Cloud Service Provider (CSP) instance. See examples in the table below. These instructions have been tested on Ubuntu 22.04.

|         CSP           |  Instance type |
| --------------------- | -------------- |
| Google Cloud Platform | c4a-highmem-72 |
| Amazon Web Services   | r8g.16xlarge   |

### Verify Python installation
Make sure Python is installed by running the following and making sure a version is printed.

```bash
python3 --version
```

```output
Python 3.12.6
```

## Install Docker

Start by adding the official Docker GPG key to your system’s APT keyrings directory:

```bash
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Run the following command to add the official Docker repository to your system’s APT sources list:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

After adding the repository, refresh the package index to ensure the latest versions are available:

```bash
sudo apt-get update
```
Now, install the necessary dependencies, including Docker and related components:
```bash
sudo apt-get install ca-certificates curl docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin make -y
```

This ensures that Docker and its dependencies are correctly set up on your system.

{{% notice Note %}}
If you run into permission issues with Docker, try running the following:

```bash
sudo usermod -aG docker $USER
newgrp docker
```
{{% /notice %}}

With your development environment set up, you can move on to download the model.