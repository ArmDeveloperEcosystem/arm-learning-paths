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

APerf is an open source command line tool maintained by AWS. It aims to assist users with performance monitoring and debugging on Linux systems. It collects a wide range of performance-related system metrics or data, whose collections traditionally require multiple tools, such as `perf`, `sysstat`, and `sysctl`. 

The collected data are written into an archive, and APerf can generate a static HTML report from one or more archives to visualize the data. When generating the report, APerf also performs analysis on the data to automatically detect potential performance issues. Users can open the report in the browser to view all collected data and analytical findings.

## What should I do before I begin installing APerf?

This article provides a quick solution to install APerf on Arm Linux and get started.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux. Note that APerf can only run on Linux.

To allow APerf to collect PMU (Processor Monitoring Unit) metrics without sudo or root permissions, set `/proc/sys/kernel/perf_event_paranoid` to -1, or run 
```bash
sudo sysctl -w kernel.perf_event_paranoid=-1
```

To use APerf's CPU profiling option (`--profile`), install the `perf` binary. Refer to the [Perf for Linux on Arm](/install-guides/perf) install guide for instructions. For kernel address visibility, set `/proc/sys/kernel/kptr_restrict` to 0, or run 
```bash
sudo sysctl -w kernel.kptr_restrict=0
```

To use APerf's Java profiling option (`--profile-java`), install the [async-profiler](https://github.com/async-profiler/async-profiler) tool.

## How do I download and install APerf?

The easiest way to install APerf is to download a release from GitHub, extract it, and setup your `PATH` environment variable or copy the executable to a directory already in your search path.

Visit the [releases page](https://github.com/aws/aperf/releases/) to see a list of available releases.

You can also download a release from the command line:

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

## How do I verify APerf is working?

### How do I create and view a report?

To confirm APerf is working, start a new collection run that collects data every 1 second for 10 seconds, which are the default interval and period. Add the `--profile` or `--profile-java` flags if needed.

```console
aperf record -r test_1
```

After 10 seconds the collection completes, and APerf produces a directory named `test_1` and a tar file named `test_1.tar.gz`.

Next, generate a report from the recorded data:

```console
aperf report -r test_1 -n test_report
```

The name of the report is `test_report`, and you will see directory named `test_report` and a tar file named `test_report.tar.gz`.

The tar files are useful if you want to copy them to another machine.

Using a web browser, open the file `index.html` in the `test_report/` directory. To open the file use `Ctrl+O` for Linux and Windows and use `⌘+O` for macOS.

In the report's home page, you can see the system information of the APerf run, followed by all analytical findings that list out potential performance issues:

![APerf report home #center](/install-guides/_images/aperf_report_home.png)

You can browse through all data using the navigation panel at the left.

If you want to learn more about a metric, click the "info" button by it and open the help panel:

![APerf report help panel #center](/install-guides/_images/aperf_report_help_panel.png)

### How do I create and view a report containing 2 runs?

To demonstrate comparing 2 runs, create a second run with `aperf record`:

```console
aperf record -r test_2
```

Similarly, after 10 seconds the collection completes, and APerf produces a directory named `test_2` and a tar file named `test_2.tar.gz`.

Generate a report with both the first and second runs included (note that the first run in the `-r` arguments will be used as the base run for any automatic comparisons):

```console
aperf report -r test_1 test_2 -n compare_report
```

The name of the report is `compare_report`, and APerf produces a directory named `compare_report` and a tar file named `compare_report.tar.gz`.

Open the `index.html` file in the `compare_report/` directory. Since multiple runs are included in the report, APerf compares the data in all runs against the base run, and generates the statistical findings in the home page:

![APerf report statistical findings #center](/install-guides/_images/aperf_report_statistical_findings.png)

When viewing the metric graphs, graphs of the same metric in two runs are aligned together:

![APerf report aligned graphs #center](/install-guides/_images/aperf_report_aligned_graphs.png)

### How do I use an HTTP server to view reports?

If you are doing performance analysis on a remote system or cloud instance without a remote desktop, you can view the APerf reports from your local browser by running a simple web server on the remote machine.

In the directory with the report data and the `index.html` file run a simple web server:

```console
python -m http.server 3000
```

Make sure port 3000 is open on the remote system and enter the IP address of the remote system followed by `:3000` in your browser address bar.

You will see the same APerf report, and avoid the need to copy files to your local machine from the remote system for viewing.

You are ready to use APerf for performance analysis on your Arm Linux system.
