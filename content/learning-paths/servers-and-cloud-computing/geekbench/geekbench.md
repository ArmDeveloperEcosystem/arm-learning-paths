---
layout: learningpathall
title: Download and run Geekbench
weight: 2
---

When selecting Arm-based hardware, you may need a way to compare different systems and select a hardware configuration for your workload. Running benchmarks on different systems with different configurations is a good way to get more information about system performance.

[Geekbench](https://www.geekbench.com/index.html) is a cross-platform benchmark that makes it easy to measure system performance. [Preview Versions](https://www.geekbench.com/preview/) are available for Linux on Arm. You can check the Geekbench [downloads](https://www.geekbench.com/download/) area for additional operating system options.

Geekbench provides a single-core score and a multi-core score, as well as individual performance scores for specific tests. You can use the scores to compare different systems and different configurations. A higher score is better.

Additional features are available with a purchased [license](https://www.primatelabs.com/store/).

## Before you begin

You will need a local Arm platform or an [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider. Geekbench 5 requires `Ubuntu 16.04 LTS` or later and Geekbench 6 requires `Ubuntu 18.04 LTS` or later.

## Download

[Preview Versions](https://www.geekbench.com/preview/) of Geekbench 5 and Geekbench 6 binaries are available to download. You can check there for newer versions. You can download versions using `wget` as shown below.

1. Install `wget` to use for the download:

```bash
sudo apt install -y wget
```

2. Download, extract the archive:

```bash
wget https://cdn.geekbench.com/Geekbench-6.5.0-LinuxARMPreview.tar.gz
tar -xf Geekbench-6.5.0-LinuxARMPreview.tar.gz
```

## Run

There is no need for a browser or Linux desktop to run the benchmark. The Linux command line is all you need.

Navigate to the extracted directory and run the `geekbench6` benchmark.

```bash
cd Geekbench-6.5.0-LinuxARMPreview
./geekbench6
```

A number of single-core and multi-core tests are run. When complete, Geekbench uploads the results automatically and provides a link to the results. The output is similar to:

```output
Uploading results to the Geekbench Browser. This could take a minute or two
depending on the speed of your internet connection.

Upload succeeded. Visit the following link and view your results online:

  https://browser.geekbench.com/v6/cpu/<id>
```

## Save your results

You can create an account on [Geekbench browser](https://browser.geekbench.com) and save the results from your runs. This makes it easy to run Geekbench on a variety of systems and see your results together and compare them. You can add notes to the results to help remember information about each run.

The output includes a claim link to add the result to your profile. The expected output is:

```output
Visit the following link and add this result to your profile:

  https://browser.geekbench.com/v6/cpu/<id>/claim?key=<key>
```
