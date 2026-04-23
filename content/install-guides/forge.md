---
additional_search_terms:
- forge
- ddt
- map
- performance reports
- allinea
author: Florent Lebeau
layout: installtoolsall
minutes_to_complete: 15
description: Install Linaro Forge on Arm Linux (aarch64) to access the DDT parallel debugger, MAP profiler, and Performance Reports tools for HPC application development.
multi_install: false
multitool_install_part: false
official_docs: https://www.linaroforge.com/documentation/
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
title: Linaro Forge
tool_install: true
weight: 1
---

[Linaro Forge](https://www.linaroforge.com/) is a server and High Performance Computing (HPC) development tool suite for C, C++, Fortran, and Python high-performance code on Linux.

Linaro Forge consists of the following:
* [Linaro DDT](https://www.linaroforge.com/linaro-ddt/) for parallel high-performance application debugging
* [Linaro MAP](https://www.linaroforge.com/linaro-map/) for performance profiling and optimization advice
* [Linaro Performance Reports](https://www.linaroforge.com/linaro-performance-reports/) for summarizing and characterizing both scalar and MPI application performance

## Platforms supported by Linaro Forge

Linaro Forge runs on Linux hosts and multiple architectures. For a full list of supported configuration, see the Linaro Forge [documentation](https://docs.linaroforge.com/latest/html/forge/supported_platforms/reference_table.html).

This install guide assumes that you have access to an Arm AArch64 platform running Ubuntu Linux.

## Download Linaro Forge

Download and extract the appropriate installation package: 

{{% notice Note %}}
The following command uses Linaro Forge version 25.1.3. The same command works with other versions. Replace the file used in this step with the file for your version of choice. To find the latest version, see [Linaro Forge Downloads](https://www.linaroforge.com/downloadForge/).
{{% /notice %}}

```bash { target="ubuntu:latest" }
sudo apt install wget
wget https://downloads.linaroforge.com/25.1.3/linaro-forge-25.1.3-linux-aarch64.tar
tar -xf linaro-forge-25.1.3-linux-aarch64.tar
```

## Install Linaro Forge

The installation steps depend on the operating system of your machine. 

### Install Linaro Forge on a Linux host

Run the installer from the command line:

```console
./textinstall.sh [--accept-license] [install_dir]
```

If no install directory is specified, you'll be prompted to specify a directory when the installer runs.

To install to the default directory non-interactively:

```bash { target="ubuntu:latest" }
linaro-forge-25.1.3-linux-aarch64/textinstall.sh --accept-license /home/ubuntu/linaro/forge/25.1.3
```

### Install Linaro Forge on macOS (remote client only)

Drag and drop the client application bundle icon into the Applications directory.

### Install Linaro Forge on Windows (remote client only)

Run the Windows file executable to install the Linaro Forge Remote Client.

### Run the graphical installer for Linaro Forge

Optionally, you can run the installer executable with a graphical interface:

```console
cd linaro-forge-25.1.3-linux-aarch64/
./installer
```

## Set up the product license for Linaro Forge

To debug or profile with Linaro Forge, you need a license file installed on the machine running the tools.

For license-specific setup instructions, see the Linaro Forge [documentation](https://docs.linaroforge.com/latest/html/forge/forge/licensing/index.html).

You don't need to install a license file for a locally installed Linaro Forge Remote Client. Linaro Forge uses the license of the remote system when it connects.

You can find [free trial licenses](https://www.linaroforge.com/freeTrial/) to try out Linaro Forge.

## Get started with Linaro Forge

After installing Linaro Forge, you can use it to debug programs and profile applications. You can also generate performance reports.

### Debug using Linaro DDT

When compiling the program that you want to debug, you need to add the debug flag to your compile command. For most compilers, this is `-g`.

Turn off compiler optimizations as they can produce unexpected results when debugging.

You can launch Linaro Forge's debugging tool, Linaro DDT, with the `ddt` command. For Message Passing Interface (MPI) applications, you can prefix the mpirun/mpiexec command normally used to run in parallel:

```console
ddt mpirun -n 128 myapp
```

This startup method is called *Express Launch* and is the quickest way to get started. If your MPI is not supported by *Express Launch*, you can run the following command instead:

```console
ddt -n 128 myapp
```

These commands will launch the Linaro DDT GUI. When running on a HPC cluster, you may need to debug on compute nodes where this may not be possible. In this case, you can start the GUI on the frontend node with the `ddt` command. After that, when running or submitting a job to the compute nodes, use `ddt --connect` :

With *Express Launch*:

```console
ddt --connect mpirun -n 128 myapp
```

Without *Express Launch*:

```console
ddt --connect -n 128 myapp
```

This mode is called *Reverse Connect*. A window will appear in the GUI when the application runs to notify of the incoming request.

### Profile an application with Linaro MAP

In most cases, if your program is already compiled with debugging symbols (`-g`), you don't need to recompile it to profile it with Linaro Forge. However, in some cases, it might need to be relinked. For more information, see [Linking](https://developer.arm.com/documentation/101136/latest/MAP/Get-started-with-MAP/Prepare-a-program-for-profiling).

Rather than profiling a debug build, you should keep optimization flags enabled when profiling. This will give more representative results.

Linaro Forge's profiling tool, Linaro MAP, can be launched with the `map` command to launch the GUI. When running on a HPC cluster with MPI, you should use `map --profile` when running or submitting a job to the compute nodes.

With *Express Launch*:

```console
map --profile mpirun -n 128 myapp
```

Without *Express Launch*:

```console
map --profile -n 128 myapp
```

When the application terminates, a `*.map` file will be created in the current directory with profiling results. This file can then be opened from the GUI launched on the frontend node or with the following command:

```console
map myapp_128p_<timestamp>.map
```

### Generate performance reports with Linaro Forge

Linaro Forge's reporting tool Linaro Performance Reports is designed to run on unmodified production executables, so in general no preparation step is necessary. However, there is one important exception: Statically linked applications require additional libraries at the linking step. For more information, see [user guide](https://developer.arm.com/documentation/101136/latest/Performance-Reports/Run-real-programs).

Linaro Performance Reports doesn't use a GUI. Instead, it produces HTML and TXT files when the application terminates to summarize the application behavior. To use the tool on MPI applications:

With *Express Launch*:

```console
perf-report mpirun -n 128 myapp
```

Without *Express Launch*:

```console
perf-report -n 128 myapp
```
Two files `myapp_128p_<timestamp>.html` and `myapp_128p_<timestamp>.txt` will be created in the current directory.

You're now ready to use Linaro Forge.
