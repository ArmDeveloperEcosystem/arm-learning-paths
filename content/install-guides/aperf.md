---
layout: installtoolsall
minutes_to_complete: 15
author: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://github.com/aws/aperf
test_images:
- ubuntu:latest
test_maintenance: true
title: APerf
tool_install: true
weight: 1
---

APerf is an open source command line tool maintained by AWS. It helps you monitor and debug performance on Linux systems by collecting a wide range of performance-related system metrics and data that traditionally require multiple tools, such as `perf`, `sysstat`, and `sysctl`.

APerf collects system data and saves it in an archive. It then generates a static HTML report from one or more archives to visualize the data. When you generate the report, APerf analyzes the data to automatically detect potential performance issues. You can open the report in a browser to view all collected data and analytical findings.

## Install APerf

This guide provides a quick solution to install APerf on Arm Linux and get started.

## Before you begin

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

{{% notice Note %}} If you see a different result, you are not using an Arm computer running 64-bit Linux. APerf can only run on Linux.{{% /notice %}}

To allow APerf to collect PMU (Processor Monitoring Unit) metrics without sudo or root permissions, set `/proc/sys/kernel/perf_event_paranoid` to -1:

```bash
sudo sysctl -w kernel.perf_event_paranoid=-1
```

To use APerf's CPU profiling option (`--profile`), install the `perf` binary. See the [Perf for Linux on Arm](/install-guides/perf) install guide for instructions. 

For kernel address visibility, set `/proc/sys/kernel/kptr_restrict` to 0:

```bash
sudo sysctl -w kernel.kptr_restrict=0
```

To use APerf's Java profiling option (`--profile-java`), install the [async-profiler](https://github.com/async-profiler/async-profiler) tool.

## Download and install APerf
The easiest way to install APerf is to download a release from GitHub and extract it.

Visit the [releases page](https://github.com/aws/aperf/releases/) to see available releases.

You can download a release from the command line:

```bash { target="ubuntu:latest" }
wget https://github.com/aws/aperf/releases/download/v1.0.0/aperf-v1.0.0-aarch64.tar.gz
```

Extract the release:

```bash { target="ubuntu:latest" }
tar xvfz aperf-v1.0.0-aarch64.tar.gz
```

Add the path to `aperf` in your `.bashrc` file.

```console
echo 'export PATH="$PATH:$HOME/aperf-v1.0.0-aarch64"' >> ~/.bashrc
source ~/.bashrc
```

Alternatively, you can copy the `aperf` executable to a directory already in your search path.

```bash { target="ubuntu:latest" }
sudo cp aperf-v1.0.0-aarch64/aperf /usr/local/bin
```

Confirm `aperf` is installed by printing the version:

```bash { target="ubuntu:latest" }
aperf --version
```

The output should print the version:

```output
aperf 1.0.0 (4cf8d28)
```

## Verify APerf is working

To confirm APerf is working, start a collection run with the default settings. The default interval is 1 second, and the default period is 10 seconds.

Run the following command to start data collection:

```console
aperf record -r test_1
```

After 10 seconds, the collection completes. APerf creates a directory named `test_1` and a tar file named `test_1.tar.gz`.

If you need CPU profiling, add the `--profile` flag. For Java profiling, add the `--profile-java` flag.

### How do I create and view a report?

Generate a report from the recorded data:

```console
aperf report -r test_1 -n test_report
```

APerf creates a directory named `test_report` and a tar file named `test_report.tar.gz`. The tar file is useful when you want to copy the report to another machine.

To view the report, open the `index.html` file in the `test_report/` directory using a web browser. Press `Ctrl+O` on Linux and Windows, or `⌘+O` on macOS.

The report's home page displays system information from the APerf run, followed by analytical findings that highlight potential performance issues:

![APerf report home page showing system information and analytical findings alt-txt#center](/install-guides/_images/aperf_report_home.webp "APerf report home page")

You can browse through all collected data using the navigation panel on the left.

To learn more about a specific metric, select the info button next to it to open the help panel:

![APerf report help panel showing detailed metric information alt-txt#center](/install-guides/_images/aperf_report_help_panel.webp "APerf report help panel")

### How do I compare multiple runs?

To demonstrate comparing multiple runs, create a second run with `aperf record`:

```console
aperf record -r test_2
```

Similarly, after 10 seconds the collection completes, and APerf produces a directory named `test_2` and a tar file named `test_2.tar.gz`.

Generate a report that includes both runs. The first run in the `-r` arguments becomes the base run for automatic comparisons:

```console
aperf report -r test_1 test_2 -n compare_report
```

APerf creates a directory named `compare_report` and a tar file named `compare_report.tar.gz`.

Open the `index.html` file in the `compare_report/` directory using a web browser. 

Because the report includes multiple runs, APerf compares all runs against the base run and displays statistical findings on the home page:

![APerf report home page showing statistical comparisons between multiple runs alt-text#center](/install-guides/_images/aperf_report_statistical_findings.png "APerf report statistical findings")

When you view metric graphs, APerf aligns graphs of the same metric from different runs side by side for easy comparison:

![APerf report showing aligned metric graphs from multiple runs for comparison alt-text#center](/install-guides/_images/aperf_report_aligned_graphs.png "APerf report aligned graphs")

### How do I view reports from a remote system?

If you're working on a remote system or cloud instance without a desktop environment, you can view APerf reports in your local browser by running a web server on the remote machine.

Navigate to the directory containing the report and the `index.html` file:

```console
cd test_report
```

Start a simple HTTP server:

```console
python -m http.server 3000
```

The server starts on port 3000. Make sure this port is open in your firewall or security group settings.

Open a web browser on your local machine and navigate to:

```output
http://<remote-ip-address>:3000
```

Replace `<remote-ip-address>` with the IP address of your remote system.

The APerf report opens in your browser without needing to copy files to your local machine.

You're now ready to use APerf for performance analysis on your Arm Linux system.

