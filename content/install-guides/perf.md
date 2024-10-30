---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Perf for Linux on Arm (LinuxPerf)

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- perf
- profiling
- profiler
- Linux
- WSL

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author_primary: Jason Andrews

### Link to official documentation
official_docs: https://perf.wiki.kernel.org/index.php/Main_Page

test_images:
- ubuntu:latest
test_maintenance: true

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Linux Perf is a command line performance analysis tool. The source code is part of the Linux kernel and Perf is connected to the `perf_events` kernel interface. Perf is used to count events from hardware and software and to identify hot spots.

Perf can be used on a wide variety of Arm Linux systems including laptops, desktops, cloud virtual machines, Windows on Arm with WSL (Windows Subsystem for Linux), and ChromeOS with Linux enabled.

Perf is best installed using a Linux package manager, but if a suitable package is not available you can build it from source code. Both situations are covered below.

## Before you begin

Follow the instructions below to install Perf on an Arm Linux system.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

Perf is dependent on the version of the Linux kernel.

To find your version run:

```bash
uname -r
```

The output will be a string with the first two numbers providing the major and minor kernel version numbers.

For example:

```output
5.15.0-79-generic
```

This indicates kernel version 5.15.

## Install Perf

The Perf source code is part of the Linux kernel source tree.

There are two ways to install Perf on Arm Linux machines:
- Use a [Linux package manager](#packman)
- Build the [source code](#source)

### Use a Linux package manager {#packman}

If a package exists for your specific kernel version you can install Perf using the package manager.

Use the tabs below and copy the commands for your Linux package manager:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
sudo apt update && sudo apt install linux-tools-generic linux-tools-$(uname -r) -y
  {{< /tab >}}
  {{< tab header="Debian/Raspberry Pi OS" language="bash">}}
sudo apt install linux-perf -y
  {{< /tab >}}
  {{< tab header="AL2023/Fedora" language="bash">}}
sudo dnf install perf -y
  {{< /tab >}}
{{< /tabpane >}}

If the package manager completes successfully you can skip the next section and proceed to [test](#test) Perf.

If the package manager does not complete successfully, it usually means there was no package available for your specific kernel version as shown by `uname -r`.

There are hundreds of packages, and the package name must match the output of `uname -r` exactly. This is most common on Arm single board computers (SBCs) where the Linux kernel has been customized.

If there is no match, you can install Perf using the source code as described in the next [section](#source).

### Build the source code {#source}

If there is no package available for your kernel version you can build Perf from source code.

Building Perf from source requires `gcc`, `flex`, `bison`, `git`, and `make`. Install these on your system.

For Debian and Ubuntu run:

```bash
sudo apt install gcc flex bison make git -y
```

Use `git` to get the source code. Use `--branch` to specify the Linux kernel source tree closest to your kernel version.

For example, if your kernel version is 5.15, use:

```bash
git clone --depth=1 --branch v5.15  git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git
```

Change to the `linux` directory and build:

```bash
cd linux
make -C tools/perf
```

If the build succeeds, a ready to use `perf` executable is available at `tools/perf/perf`

You can copy it to a location in your search path or run it from the current location.

To copy it use:

```console
sudo cp tools/perf/perf /usr/local/bin
```

## Test Perf {#test}

Regardless of how you installed Perf, run the `version` command:

```bash
perf version
```

The output will be similar to:

```output
perf version 5.15.116
```

You can also try the `list` command to confirm `perf` is working as expected:

```bash
perf list
```

Perf is installed correctly if you see a list of events similar to the output below:

```output
List of pre-defined events (to be used in -e or -M):

  cpu-cycles OR cycles                               [Hardware event]

  alignment-faults                                   [Software event]
  bpf-output                                         [Software event]
  cgroup-switches                                    [Software event]
  context-switches OR cs                             [Software event]
  cpu-clock                                          [Software event]
  cpu-migrations OR migrations                       [Software event]
  dummy                                              [Software event]
  emulation-faults                                   [Software event]
  major-faults                                       [Software event]
  minor-faults                                       [Software event]
  page-faults OR faults                              [Software event]
  task-clock                                         [Software event]

  duration_time                                      [Tool event]
  user_time                                          [Tool event]
  system_time                                        [Tool event]


branch:
  br_mis_pred
       [Mispredicted or not predicted branch speculatively executed]
  br_pred
       [Predictable branch speculatively executed]
```

Perf is not working correctly if you see output similar to the messages below. To fix the errors you need to [build Perf from source](#source).

Error #1:

```output
WARNING: perf not found for kernel 5.15.90.1-microsoft

  You may need to install the following packages for this specific kernel:
    linux-tools-5.15.90.1-microsoft-standard-WSL2
    linux-cloud-tools-5.15.90.1-microsoft-standard-WSL2

  You may also want to install one of the following packages to keep up to date:
    linux-tools-standard-WSL2
    linux-cloud-tools-standard-WSL2
```

Error #2:

```output
/usr/bin/perf: line 13: exec: perf_5.15: not found
E: linux-perf-5.15 is not installed.
```

### Generate a test Perf report

Generate a simple Perf report. For example:
```console
perf stat -a pwd
```
The `pwd` command output will be shown as well as the report:
```output
Performance counter stats for 'system wide':

              2.72 msec cpu-clock                 #    2.205 CPUs utilized
                14      context-switches          #    5.147 K/sec
                 2      cpu-migrations            #  735.277 /sec
                76      page-faults               #   27.941 K/sec
           2380757      cycles                    #    0.875 GHz
           2651708      instructions              #    1.11  insn per cycle
   <not supported>      branches
             15058      branch-misses

       0.001233481 seconds time elapsed
```

If you see an error similar to:
```output
Access to performance monitoring and observability operations is limited.
```
You will need to modify the [PMU access permissions](#access).

### PMU access permission {#access}

On some systems, using Perf to access hardware counters is restricted by the value of `/proc/sys/kernel/perf_event_paranoid`

Typically the value must be 2 or less to collect Perf metrics.


|perf_event_paranoid |	Description  |
|--------------------|---------------|
|3	| Disable use of Perf events     |
|2	| Allow only user-space measurements |
|1	| Allow kernel and user-space measurements |
|0	| Allow access to CPU-specific data but not raw trace‐point samples |
|-1 | No restrictions |


To set this until the next reboot, run the following command:

```bash
sudo sysctl -w kernel.perf_event_paranoid=2
```

To permanently set the paranoid level, add the following line to the file `/etc/sysctl.conf`

```console
kernel.perf_event_paranoid=2
```

### Additional Perf commands

There are five common commands used in performance analysis.

* **stat** provides performance counter statistics for the overall execution of a program

* **record** samples the program and records the samples into a data file (perf.data by default)

* **report** generates a report of where the samples occurred

* **annotate** displays the annotated code showing the source and assembly code for the samples

### Arm PMU driver

Arm systems use a kernel driver to expose PMU hardware counters. The driver needs to be enabled in the Linux kernel in order to collect the hardware events.

To check if the driver is running use the `dmesg` command:

```bash
sudo dmesg | grep "PMU driver"
```

{{% notice Note%}}
Depending on your system, you might need to use `sudo` to run the `dmesg` command.
{{% /notice %}}

If you see output similar to the message below, the Arm PMU driver is installed.

```output
[    0.046063] hw perfevents: enabled with armv8_pmuv3_0 PMU driver, 3 counters available
```

The number of counters available could be between 1 and 7 depending on processor types and virtualization.

If you see multiple instances of the PMU driver, it means the hardware is a [big.LITTLE](https://www.arm.com/en/technologies/big-little) system with different processors, each has it's own PMU.

If the message is not in the kernel message log, check both the PMU driver device tree entry and the kernel configuration parameters listed above.

The important kernel parameters are:

```output
CONFIG_HAVE_PERF_EVENTS=y
CONFIG_PROFILING=y
CONFIG_PERF_EVENTS=y
CONFIG_ARM_PMU=y
CONFIG_HW_PERF_EVENTS=y
```

You are now ready to use Perf on your Arm Linux system.
