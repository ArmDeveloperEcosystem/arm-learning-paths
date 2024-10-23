---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Streamline CLI Tools

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- profiling
- profiler
- Linux
- Server
- Neoverse

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

author_primary: Julie Gaskin

### Link to official documentation
official_docs: https://developer.arm.com/documentation/109847/latest/

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

The Streamline CLI tools are native command-line tools that are designed to run directly on an Arm server running Linux. The tools provide a software profiling methodology that gives you clear and actionable performance data. You can use this data to guide the optimization of the heavily used functions in your software.

## Platform support

Streamline CLI tools are supported with the following host operating systems running on an Arm AArch64 host machine:

* Amazon Linux 2023 or newer
* Debian 10 or newer
* RHEL 8 or newer
* Ubuntu 20.04 or newer

Streamline CLI tools are supported on the following Arm CPUs:

* Arm Neoverse N1
* Arm Neoverse N2
* Arm Neoverse V1

## Before you begin

Use the Arm Sysreport utility to determine whether your system configuration supports hardware-assisted profiling. Follow the instructions in [Get ready for performance analysis with Sysreport][1] to discover how to download and run this utility.

[1]: https://learn.arm.com/learning-paths/servers-and-cloud-computing/sysreport/

The `perf counters` entry in the generated report indicates how many CPU counters are available. The `perf sampling` entry indicates if SPE is available. You will achieve the best profiles in systems with at least 6 available CPU counters and SPE.

The Streamline CLI tools can be used in systems without any CPU counters, but can only return a basic hot-spot profile based on time-based sampling.
No top-down methodology metrics will be available.

The Streamline CLI tools can give top-down metrics in systems with as few as 3 available CPU counters. The effective sample rate for each metric will be lower, because you need to time-slice the counters to capture all of the requested metrics. This means that you need to run your application for longer to get the same number of samples for each metric. Metrics that require more input counters than are available cannot be captured.

The Streamline CLI tools can be used without SPE. Load operation data source metrics will not be available, and branch mispredict metrics might be less
accurate.

## Building your application

Before you can capture a software profile you must build your application with debug information. This enables the profiler to map instruction addresses back to specific functions in your source code. For C and C++ you do this by passing the `-g` option to the compiler.

Arm recommends that you profile an optimized release build of your application, as this ensures you are profiling a realistic code workload. For C and C++ you do this by passing the `-O2` or `-O3` option to the compiler. However, it is recommended that you disable invasive optimization techniques, such as link-time optimization (LTO), because they heavily restructure the code and make the profile difficult to understand.

If you are using the `workflow_topdown_basic option`, ensure that your application workload is at least 20 seconds long, in order to give the core time to capture all of the metrics needed. This time increases linearly as you add more metrics to capture.

## Using Python scripts

The Python scripts provided with Streamline CLI tools require Python 3.8 or later, and depend on several third-party modules. We recommend creating a Python virtual environment containing these modules to run the tools. 

Create a virtual environment:

```sh
# From Bash
python3 -m venv sl-venv
source ./sl-venv/bin/activate
```

The prompt of your terminal has (sl-venv) as a prefix indicating the virtual environment is active.

{{% notice Note%}}
The instructions assume that you run all Python commands from inside the virtual environment.
{{% /notice %}}

## Installing the tools {.reference}

The Streamline CLI tools are available as a standalone download to enable easy integration in to server workflows.

To download the latest version of the tool and extract it to the current working directory you can use our download utility script:

```sh
wget https://artifacts.tools.arm.com/arm-performance-studio/Streamline_CLI_Tools/get-streamline-cli.py
python3 get-streamline-cli.py install
python3 -m pip install -r ./streamline_cli_tools/bin/requirements.txt
```

If you want to add the Streamline tools to your search path:

```sh
export PATH=$PATH:$PWD/streamline_cli_tools/bin
```

The script can also be used to download a specific version, or install to a user-specified directory:

* To list all available versions:

    ```sh
    python3 get-streamline-cli.py list
    ```

* To download, but not install, a specific version:

    ```sh
    python3 get-streamline-cli.py download --tool-version <version>
    ```

* To download and install a specific version:

    ```sh
    python3 get-streamline-cli.py install --tool-version <version>
    ```

* To download and install to a specific directory

    ```sh
    python3 get-streamline-cli.py install --install-dir <path>
    ```

For manual download, you can find all available releases here:

```sh
https://artifacts.tools.arm.com/arm-performance-studio/Streamline_CLI_Tools/
```

## Applying the kernel patch

For best results, we provide a Linux kernel patch that modifies the behavior of Linux perf to improve support for capturing function-attributed top-down metrics on Arm systems. This patch provides two new capabilities:

* It allows a new thread to inherit the perf counter group configuration of its parent.
* It decouples the perf event-based sampling window size from the overall sample rate. This allows strobed mark-space sampling patterns where the tool can capture a small window without using a high sample rate.

Without the patch it is possible to capture profiles. However, not all capture options are available and capturing top-down metrics will rely on high
frequency sampling. The following options are available:

* System-wide profile with top-down metrics.
* Single threaded application profile with top-down metrics.
* Multi-process/thread application profile **without** top-down metrics.

With the patch applied, it is possible to collect the following profiles:

* System-wide profile with top-down metrics.
* Single threaded application profile with top-down metrics.
* Multi-process/thread application profile **with** top-down metrics.

The following instructions show you how to install the patch on Amazon Linux 2023.
You might need to adapt them slightly to other Linux distributions.

### Manual application to the source tree

To apply the patch to the latest 6.7 kernel, you can use `git`:

```sh
git apply v6.7-combined.patch
```

or `patch`:

```sh
patch -p 1 -i v6.7-combined.patch
```

### Manual application to an RPM-based distribution

Follow these steps to integrate these patches into an RPM-based distribution's kernel:

1. Install the RPM build tools:

    ```sh
    sudo yum install rpm-build rpmdevtools
    ```

1. Remove any existing `rpmbuild` directory, renaming as appropriate:

    ```sh
   rm -fr rpmbuild
    ```

1. Fetch the kernel sources:

    ```sh
    yum download --source kernel
    ```

1. Install the sources binary:

    ```sh
   rpm -i kernel-<VERSION>.src.rpm
    ```

1. Enter the `rpmbuild` directory that is created:

    ```sh
    cd rpmbuild
    ```

1. Copy the patch into the correct location. Replace the 9999 patch number with the next available patch number in the sequence:

    ```sh
    cp vX.Y-combined.patch SOURCES/9999-strobing-patch.patch
    ```

1. Open the specs file in your preferred editor:

    ```sh
   nano SPECS/kernel.spec
    ```

1. Search for the list of patches starting with `Patch0001`, and append the line for the new patch to the end of the list. Replace 9999 with the patch number used earlier:

    ```sh
   Patch9999: 9999-strobing-patch.patch
    ```

1. Search for the list of patch apply steps starting with `ApplyPatch`, and append the line for the new patch to the end of the list. Replace 9999 with the patch number used earlier:

    ```sh
   ApplyPatch 9999-strobing-patch.patch
    ```

1. Save the changes and exit the editor.

1. Install the build dependencies:

    ```sh
    sudo dnf builddep SPECS/kernel.spec
    ```

1. Build the kernel and other rpms:

    ```sh
   rpmbuild -ba SPECS/kernel.spec
    ```

1. Install the built packages:

    ```sh
   sudo rpm -ivh --force RPMS/aarch64/*.rpm
    ```

1. Reboot the system:

    ```sh
   sudo reboot
    ```

1. Validate that the patch has been applied correctly:

    ```sh
   ls -l /sys/bus/event_source/devices/*/format/strobe_period
    ```

    This should list at least one CPU PMU device supporting the strobing  features, for example:

    ```output
   /sys/bus/event_source/devices/armv8_pmuv3_0/format/strobe_period
    ```

You are now ready to use Streamline CLI Tools. Refer to [Profiling for Neoverse with Streamline CLI Tools](/learning-paths/servers-and-cloud-computing/profiling-for-neoverse/) to get started.
