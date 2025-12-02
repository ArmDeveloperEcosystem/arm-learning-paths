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
title: AWS Perf (APerf)
tool_install: true
weight: 1
---

APerf (AWS Perf) is an open source command line performance analysis tool which saves time by collecting information which is normally collected by multiple tools such as `perf`, `sysstat`, and `sysctl`.

APerf was created by AWS to help with Linux performance analysis.

In addition to the CLI, APerf includes an HTML view to visualize the collected data.

## What should I do before I begin installing APerf?

APerf works on Linux, and is available as a single binary.

APerf works best if `perf` is installed. Refer to the [Perf for Linux on Arm](/install-guides/perf) install guide for instructions.

This article provides a quick solution to install APerf on Arm Linux and get started.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## How do I download and install APerf?

The easiest way to install APerf is to download a release from GitHub, extract it, and setup your `PATH` environment variable or copy the executable to a directory already in your search path.

Visit the [releases page](https://github.com/aws/aperf/releases/) to see a list of available releases.

You can also download a release from the command line:

```bash { target="ubuntu:latest" }
wget https://github.com/aws/aperf/releases/download/v0.1.15-alpha/aperf-v0.1.15-alpha-aarch64.tar.gz
```

Extract the release:

```bash { target="ubuntu:latest" }
tar xvfz aperf-v0.1.15-alpha-aarch64.tar.gz
```

Add the path to `aperf` in your `.bashrc` file.

```console
echo 'export PATH="$PATH:$HOME/aperf-v0.1.15-alpha-aarch64"' >> ~/.bashrc
source ~/.bashrc
```

Alternatively, you can copy the `aperf` executable to a directory already in your search path.

```bash { target="ubuntu:latest" }
sudo cp aperf-v0.1.15-alpha-aarch64/aperf /usr/local/bin
```

Confirm `aperf` is installed by printing the version:

```bash { target="ubuntu:latest" }
aperf --version
```

The output should print the version:

```output
aperf 0.1.0 (4b910d2)
```

## How do I verify APerf is working?

### How do I create and view a report?

To confirm APerf is working, start it for 10 seconds and take a sample every 1 second.

```console
sudo aperf record -i 1 -p 10 -r run1 --profile
```

After 10 seconds `aperf` completes and you see a directory named `run1` and a tar file named `run1.tar.gz`.

Next, generate a report from the recorded data:

```console
sudo aperf report -r run1 -n report1
```

The name of the report is `report1` and you will see a `report1` directory and a tar file named `report1.tar.gz`.

The tar files are useful if you want to copy them to another machine.

Using a web browser, open the file `index.html` in the `report1/` directory. To open the file use `Ctrl+O` for Linux and Windows and use `⌘+O` for macOS.

The report is now visible in the browser.

There are a number of tabs on the left side showing the collected data.

You can browse the data and see what has been collected.

![APerf #center](/install-guides/_images/aperf0.webp)

{{% notice Note %}}
The Kernel Config and Sysctl Data tabs are blank unless you click No.
{{% /notice %}}

### How do I create and view a report containing 2 runs?

To demonstrate comparing 2 runs, create a second run with `aperf record`:

```console
sudo aperf record -i 1 -p 10 -r run2 --profile
```

After 10 seconds `aperf` completes and you see a directory named `run2` and a tar file named `run2.tar.gz`.

Generate a report with both the first and second runs included:

```console
sudo aperf report -r run1 -r run2 -n compare
```

The name of the report is `compare` and you will see a `compare` directory and a tar file named `compare.tar.gz`.

Open the `index.html` file in the `compare/` directory to see the 2 runs side by side.

A screenshot is shown below:

![APerf #center](/install-guides/_images/aperf.webp)

### How do I use an HTTP server to view reports?

If you are doing performance analysis on a remote system or cloud instance without a remote desktop, you can view the APerf reports from your local browser by running a simple web server on the remote machine.

In the directory with the report data and the `index.html` file run a simple web server:

```console
python -m http.server 3000
```

Make sure port 3000 is open on the remote system and enter the IP address of the remote system followed by `:3000` in your browser address bar.

You will see the same APerf report, and avoid the need to copy files to your local machine from the remote system for viewing.

You are ready to use APerf for performance analysis on your Arm Linux system.
