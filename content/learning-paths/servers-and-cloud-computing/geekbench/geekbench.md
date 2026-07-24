---
layout: learningpathall
title: Download and run Geekbench
weight: 2
---

When selecting Arm-based hardware, you might need a way to compare different systems and select a hardware configuration for your workload. Running benchmarks on different systems with different configurations is a good way to get more information about system performance.

[Geekbench](https://www.geekbench.com/index.html) is a cross-platform benchmark that makes it easy to measure system performance. This Learning Path uses Geekbench 7, the latest version, with a [preview build available for Linux on Arm](https://www.geekbench.com/preview/). You can check the Geekbench [downloads](https://www.geekbench.com/download/) area for additional operating system options.

Geekbench provides a single-core score and a multi-core score. It also reports individual performance scores for specific tests. You can use the scores to compare different systems and different configurations. A higher score is better.

A purchased [license](https://www.primatelabs.com/store/) unlocks additional features.

## Before you begin

You'll need a local Arm platform or an [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider. Geekbench 7 requires Ubuntu 22.04 LTS or later.

Older versions are also available on the [Geekbench preview downloads page](https://www.geekbench.com/preview/): Geekbench 6 requires Ubuntu 18.04 LTS or later and Geekbench 5 requires Ubuntu 16.04 LTS or later.

## Download

Download the Geekbench 7 Linux/AArch64 preview binary using `wget`. Check the [Geekbench preview downloads page](https://www.geekbench.com/preview/) for newer versions.

Install `wget` to use for the download:

```bash
sudo apt install -y wget
```

Download and extract the archive:

```bash
wget https://cdn.geekbench.com/Geekbench-7.0.0-LinuxARMPreview.tar.gz
tar -xf Geekbench-7.0.0-LinuxARMPreview.tar.gz
```

## Run

There is no need for a browser or Linux desktop to run the benchmark. The Linux command line is all you need.

Navigate to the extracted directory and run the `geekbench7` benchmark.

```bash
cd Geekbench-7.0.0-LinuxARMPreview
./geekbench7
```

Geekbench runs a series of single-core and multi-core tests. When complete, Geekbench uploads the results automatically and provides a link to the results. The output is similar to:

```output
Uploading results to the Geekbench Browser. This could take a minute or two
depending on the speed of your internet connection.

Upload succeeded. Visit the following link and view your results online:

  https://browser.geekbench.com/v7/cpu/<id>
```

## Save your results

You can create an account on [Geekbench browser](https://browser.geekbench.com) and save the results from your runs. This makes it easy to run Geekbench on a variety of systems and see your results together and compare them. You can add notes to the results to help remember information about each run.

The output includes a claim link to add the result to your profile. The expected output is:

```output
Visit the following link and add this result to your profile:

  https://browser.geekbench.com/v7/cpu/<id>/claim?key=<key>
```

## Verify your results

Open the results URL in a browser. You should see a page with your system information, a single-core score, and a multi-core score. If both scores appear, Geekbench ran successfully.

A higher score indicates better performance. You can compare your result against other Arm systems in the [Geekbench Browser](https://browser.geekbench.com).

## Summary

You've installed and run Geekbench 7 on an Arm Linux system and saved your results for comparison. Use the Geekbench Browser to compare scores across different Arm instance types and configurations to help determine the best hardware for your workload.
