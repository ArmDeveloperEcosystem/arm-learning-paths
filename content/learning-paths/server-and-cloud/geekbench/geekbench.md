---
layout: learningpathall
title: Download and run Geekbench
weight: 2
---

When creating a cloud instance, users may struggle to select an appropriate configuration for their workloads. Simple benchmarking runs on different configurations is a good idea to help you decide.

[Geekbench](https://www.geekbench.com/index.html) is a cross-platform benchmark that easily measures your system's performance. Preview builds for Arm were provided in [Geekbench 5.4](https://www.geekbench.com/blog/2021/03/geekbench-54/). Newer versions may be available, check the Geekbench [downloads](https://www.geekbench.com/download/) section for latest information.

It provides an overall score (for both single and multi-core configuration), as well as individual performance scores for specific tests, which can easily be compared against other configurations (higher is better).

Additional features are available with a purchased [license](https://www.primatelabs.com/store/).

## Prerequisites

You will need a local Arm platform or an [Arm based instance](/learning-paths/server-and-cloud/csp/) from your cloud service providers, running an appropriate operating system (at time of writing, `Ubuntu 16.04 LTS` or later).

## Fetch pre-built binaries
The binaries are available to download from the Geekbench website directly. Check the website for the latest link. The below is for the 5.4 preview build.

Once downloaded `untar` the archive, and navigate into its directory:
```bash
sudo apt install -y tar wget
wget https://cdn.geekbench.com/Geekbench-5.4.0-LinuxARMPreview.tar.gz
tar -xf Geekbench-5.4.0-LinuxARMPreview.tar.gz
```
## Run benchmark
Run the `geekbench5` benchmark.
```bash
cd Geekbench-5.4.0-LinuxARMPreview
./geekbench5
```
It will run a number of single-core and multi-core tests. When complete, it will upload your results to the [Geekbench browser](https://browser.geekbench.com) and provide a link to the specific results for your platform.

You can browse other platform scores, or repeat your test with other cloud configurations to see how they compare. We also encourage you to compare against servers build with other architectures.