---
title: Geekbench
description: Install and run Geekbench 7 on Arm Linux systems to benchmark single-core and multi-core CPU performance.
author: Jason Andrews
minutes_to_complete: 15
official_docs: https://www.geekbench.com/preview/

additional_search_terms:
- benchmark
- linux
- Neoverse

test_images:
- ubuntu:latest
test_maintenance: true

weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

When selecting Arm-based hardware, you might need a way to compare different systems and select a hardware configuration for your workload. Running benchmarks on different systems with different configurations is a good way to get more information about system performance.

[Geekbench](https://www.geekbench.com/index.html) is a cross-platform benchmark that makes it easy to measure system performance. You'll install Geekbench 7, the latest version, with a [preview build available for Linux on Arm](https://www.geekbench.com/preview/). For additional operating system options, see the [Geekbench downloads page](https://www.geekbench.com/download/).

Geekbench provides a single-core score and a multi-core score. It also reports individual performance scores for specific tests. You can use the scores to compare different systems and different configurations. A higher score is better.

You can unlock additional features with a purchased [license](https://www.primatelabs.com/store/).

## Before you begin

You'll need a local Arm platform or an [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider. Geekbench 7 requires Ubuntu 22.04 LTS or later.

Older versions are also available on the [Geekbench preview downloads page](https://www.geekbench.com/preview/): Geekbench 6 requires Ubuntu 18.04 LTS or later and Geekbench 5 requires Ubuntu 16.04 LTS or later.

## Download the Geekbench binary

Download the Geekbench 7 Linux/AArch64 preview binary using `wget`. Check the [Geekbench preview downloads page](https://www.geekbench.com/preview/) for newer versions.

Install `wget` for the download:

```bash
sudo apt install -y wget
```

{{% notice Note %}}
The following commands use Geekbench version 7.0.0. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see the [Geekbench preview downloads page](https://www.geekbench.com/preview/).
{{% /notice %}}

Download and extract the archive using `wget`:

```bash
wget https://cdn.geekbench.com/Geekbench-7.0.0-LinuxARMPreview.tar.gz
tar -xf Geekbench-7.0.0-LinuxARMPreview.tar.gz
```

## Verify the Geekbench installation

Verify the installation by running the `geekbench7` benchmark.

### Run the benchmark

You don't need a browser or Linux desktop to run the benchmark. The Linux command line is all you need.

Navigate to the extracted directory and run the `geekbench7` benchmark:

```bash
cd Geekbench-7.0.0-LinuxARMPreview
./geekbench7
```

Geekbench runs a series of single-core and multi-core tests. When complete, Geekbench uploads the results automatically and provides a link to the results.

The output is similar to:

```output
Uploading results to the Geekbench Browser. This could take a minute or two
depending on the speed of your internet connection.

Upload succeeded. Visit the following link and view your results online:

  https://browser.geekbench.com/v7/cpu/<id>
```

### Save the benchmark results

You can create an account on the [Geekbench Browser](https://browser.geekbench.com) and save the results from your runs. Creating an account makes it easy to run Geekbench on a variety of systems and see your results together and compare them. You can add notes to the results to help remember information about each run.

The output includes a claim link to add the result to your profile.

The output is similar to:

```output
Visit the following link and add this result to your profile:

  https://browser.geekbench.com/v7/cpu/<id>/claim?key=<key>
```

### Verify your results

Open the results URL in a browser. You should see a page with your system information, a single-core score, and a multi-core score. If both scores appear, Geekbench ran successfully.

A higher score indicates better performance. You can compare your result against other Arm systems in the [Geekbench Browser](https://browser.geekbench.com).

## Next steps

You've installed and run Geekbench 7 on an Arm Linux system and saved your results for comparison. Use the Geekbench Browser to compare scores across different Arm instance types and configurations to help determine the best hardware for your workload.
