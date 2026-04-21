---
title: Set up your environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install dependencies

Ensure that you're using an Arm Linux system (`aarch64`), such as an AWS Graviton-based Amazon EC2 instance running Amazon Linux 2023. This Learning Path has been tested on an AWS Graviton 3 `c7g.metal` EC2 instance with 64 Neoverse V1 cores. You can use other Arm Linux distributions. If you use a different distribution, replace `dnf` with your package manager, such as `apt` on Ubuntu or Debian.

On an Arm Linux system, install the following packages:

```bash
sudo dnf update -y
sudo dnf install -y git cmake g++ environment-modules python3 python3-pip
```

## Install Arm Performix

Arm Performix is a desktop application that connects to your remote Arm Linux target over SSH to capture and display profiling data. You need to install Performix on your local machine (Windows, macOS, or Linux). When you configure your new target, Performix copies the required software to the target. You don't need to install anything on the target for Performix.

For more information about installing Performix on your local machine, see the [Arm Performix install guide](/install-guides/performix/).

## Install Arm Performance Libraries

Install the prebuilt Arm Performance Libraries on your Arm Linux system using the following commands:

```bash
wget https://developer.arm.com/-/cdn-downloads/permalink/Arm-Performance-Libraries/Version_26.01/arm-performance-libraries_26.01_rpm_gcc.tar -O /tmp/armpl.tar
cd /tmp && tar xf armpl.tar
cd /tmp/arm-performance-libraries_26.01_rpm
sudo bash arm-performance-libraries_26.01_rpm.sh --accept

echo 'export ARMPL_DIR=/opt/arm/armpl_26.01_gcc' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=$ARMPL_DIR/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
echo 'export C_INCLUDE_PATH=$ARMPL_DIR/include:$C_INCLUDE_PATH' >> ~/.bashrc
```

Update your environment variables:

```bash
cd ~/
source ~/.bashrc
```
For more information about installing the libraries on other operating systems or Linux distributions, see the [Arm Performance Libraries install guide](/install-guides/armpl/).

## Clone the repository

In this Learning Path, you'll work with a data-processing example. The example simulates a common analytics pattern: generating random 2D point data, filtering points within a rectangular window, and computing a distance metric. You'll use it as a baseline to profile and then optimize with OpenRNG and Arm Performance Libraries.

Clone the example repository:

```bash
git clone https://github.com/arm-education/Data-Processing-Example.git
cd Data-Processing-Example
```

## What you've accomplished and what's next

In this section, you:
- Installed the required system dependencies on your Arm Linux system
- Installed Arm Performix on your local machine for remote profiling
- Installed Arm Performance Libraries and configured environment variables
- Cloned the data-processing example repository

Next, you'll examine what the example does and run the visualization helper to understand the baseline workload before profiling.
