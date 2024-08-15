---
additional_search_terms:
- forge
- ddt
- map
- performance reports
- allinea
author_primary: Florent Lebeau
layout: installtoolsall
minutes_to_complete: 15
multi_install: false
multitool_install_part: false
official_docs: https://www.linaroforge.com/documentation/
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
test_status:
- passed
title: Linaro Forge
tool_install: true
weight: 1
---

[Linaro Forge](https://www.linaroforge.com/) is a server and HPC development tool suite for C, C++, Fortran, and Python high performance code on Linux.

Linaro Forge consists of
* [Linaro DDT](https://www.linaroforge.com/linaro-ddt/) for parallel high-performance application debugging
* [Linaro MAP](https://www.linaroforge.com/linaro-map/) for performance profiling and optimization advice, and
* [Linaro Performance Reports](https://www.linaroforge.com/linaro-performance-reports/) for summarizing and characterizing both scalar and MPI application performance.

## Supported platforms

Linaro Forge runs on Linux hosts and multiple architectures. See the Linaro Forge [documentation](https://docs.linaroforge.com/latest/html/forge/supported_platforms/reference_table.html) for a full list of supported configurations.

This install guide assumes an Arm AArch64 platform running Ubuntu Linux.

## Download 

Download and extract the appropriate installation package from [Linaro Forge Downloads](https://www.linaroforge.com/downloadForge/).

```bash { target="ubuntu:latest" }
sudo apt install wget
wget https://downloads.linaroforge.com/24.0.3/linaro-forge-24.0.3-linux-aarch64.tar
tar -xf linaro-forge-24.0.3-linux-aarch64.tar
```

## Installation

### Linux host

Run the installer from the command line with:

```console
./textinstall.sh [--accept-license] [install_dir]
```

If no install directory is specified, you will be prompted to specify this while the installer runs.

To install to the default directory, non-interactively:

```bash { target="ubuntu:latest" }
linaro-forge-24.0.3-linux-aarch64/textinstall.sh --accept-license /home/ubuntu/linaro/forge/24.0.3
```

### Install on macOS (remote client only)

Drag and drop the client application bundle icon into the Applications directory.

### Install on Windows (remote client only)

Run the Windows file executable to install the Linaro Forge Remote Client.

### Graphical installer

Optionally, you can run the installer executable with a graphical interface. 

```bash 
cd linaro-forge-24.0.3-linux-aarch64/
./installer
```

## Setting up the product license

You must install a license file on a machine running Linaro Forge tools to debug or profile.

See the Linaro Forge [documentation](https://docs.linaroforge.com/latest/html/forge/forge/licensing/index.html) for set up instructions depending on the type of license you have.

You do not need to install a license file on a machine running Linaro Forge Remote Client for connecting remotely to Linaro Forge tools on a remote system.

[Free trial licenses](https://www.linaroforge.com/freeTrial/) are available for you try out Linaro Forge.

## Get started

### Debugging

When compiling the program that you want to debug, you must add the debug flag to your compile command. For most compilers this is `-g`.

You should turn off compiler optimizations as they can produce unexpected results when debugging.

Linaro Forge's debugging tool, Linaro DDT, can be launched with the `ddt` command. For MPI applications, you can prefix the mpirun/mpiexec command normally used to run in parallel:

```console
ddt mpirun -n 128 myapp
```

This startup method is called *Express Launch* and is the simplest way to get started. If your MPI is not supported by *Express Launch*, you can run the following instead:

```console
ddt -n 128 myapp
```

These commands will launch Linaro DDT GUI. When running on a HPC cluster, you may need to debug on compute nodes where this may not be possible. In this case, you can start the GUI on the frontend node with the `ddt` command and when running or submitting a job to the compute nodes use `ddt --connect` :

With *Express Launch*:

```console
ddt --connect mpirun -n 128 myapp
```

Without *Express Launch*:

```console
ddt --connect -n 128 myapp
```

This mode is called *Reverse Connect*. A window will appear in the GUI when the application runs to notify of the incoming request.

### Profiling

In most cases, if your program is already compiled with debugging symbols (`-g`), you do not need to recompile your program to profile it with Linaro Forge. However, in some cases it might need to be relinked (see the [Linking](https://developer.arm.com/documentation/101136/latest/MAP/Get-started-with-MAP/Prepare-a-program-for-profiling)).

Typically you should keep optimization flags enabled when profiling (rather than profiling a debug build). This will give more representative results.

Linaro Forge's profiling tool, Linaro MAP, can be launched with the `map` command to launch the GUI. When running on a HPC cluster with MPI, you should use `map --profile` when running or submitting a job to the compute nodes:

With *Express Launch*:

```console
map --profile mpirun -n 128 myapp
```

Without *Express Launch*:

```console
map --profile -n 128 myapp
```

A *.map file will be created in the current directory with profiling results when the application terminates. This file can be then open from the GUI launched on the frontend node or with the following command:

```console
map myapp_128p_<timestamp>.map
```

### Performance Reports

Linaro Forge's reporting tool Linaro Performance Reports is designed to run on unmodified production executables, so in general no preparation step is necessary. However, there is one important exception: statically linked applications require additional libraries at the linking step (see [user guide](https://developer.arm.com/documentation/101136/latest/Performance-Reports/Run-real-programs)).

Linaro Performance Reports does not use a GUI. Instead, it produces HTML and TXT files when the application terminates to summarize the application behavior. Here is how to use the tool on MPI applications

With *Express Launch*:

```console
perf-report mpirun -n 128 myapp
```

Without *Express Launch*:

```console
perf-report -n 128 myapp
```
Two files `myapp_128p_<timestamp>.html` and `myapp_128p_<timestamp>.txt` will be created in the current directory.

Linaro Forge is now installed and ready to use. 
