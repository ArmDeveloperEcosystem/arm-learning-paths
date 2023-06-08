---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Linaro Forge

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
  - forge
  - ddt
  - map
  - performance reports
  - allinea

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author_primary: Florent Lebeau

### Link to official documentation
official_docs: https://www.linaroforge.com/documentation/

author_primary: Florent Lebeau

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Linaro Forge](https://www.linaroforge.com/) is a server and HPC development tool suite for C, C++, Fortran, and Python high performance code on Linux.

Linaro Forge consists of
* [Linaro DDT](https://www.linaroforge.com/linaroDdt/) for parallel high-performance application debugging
* [Linaro MAP](https://www.linaroforge.com/linaroMap/) for performance profiling and optimization advice, and
* [Linaro Performance Reports](https://docs.linaroforge.com/22.1.3/html/101136_arm-forge-user-guide/performance_reports/index.html) for summarizing and characterizing both scalar and MPI application performance.

## Supported platforms

Linaro Forge runs on Linux and multiple architectures.

| Architecture | Operating systems | MPI | Compilers | Accelerators |
| ------------ | ----------------- | --- | --------- | ------------ |
| Armv8 (AArch64) | Red Hat Enterprise Linux / CentOS 7 and 8 <br />SuSE Linux Enterprise Server 12 and 15 <br />Ubuntu 16.04 to 20.04 | Cray MPT <br />HPE MPI <br />MPICH <br />MVAPICH2 <br />Open MPI 3 to 4 | Arm Compiler for Linux <br />Cray Compiling Environment <br />GNU C/C++/Fortran Compiler <br />NVIDIA HPC (PGI) Compiler | Nvidia CUDA Toolkit 11.0 to 11.1 |
| Intel and AMD (x86_64) | Red Hat Enterprise Linux/CentOS 7 and 8 <br />SuSE Linux Enterprise Server 12 and 15 <br />Ubuntu 16.04 to 20.04 | Cray MPT <br />HPE MPI <br />Intel MPI <br />MPICH <br />MVAPICH2 <br />Open MPI 3 to 4 | Cray Compiling Environment <br />GNU C/C++/Fortran Compiler <br />Intel Parallel Studio <br />NVIDIA HPC (PGI) Compiler | Nvidia CUDA Toolkit 9.0 to 11.1 |
| IBM Power (ppc64le) | Red Hat Enterprise Linux/CentOS 7 and 8 | IBM Spectrum MPI <br />Open MPI 3 to 4 | GNU C/C++/Fortran Compiler <br />IBM XL Compiler <br />NVIDIA HPC (PGI) Compiler | Nvidia CUDA Toolkit 9.2 to 11.1 |

Linaro Forge provides native remote clients for other operating systems to connect to your cluster where you can run, debug, profile, edit, and compile your application files.

| Architecture | Operating systems |
| ------------ | ----------------- |
| Armv8 (AArch64) | MacOS 10.13 (High Sierra), and above. <br /> Any of the Linux platforms listed above. |
| Intel and AMD (x86_64) | MacOS 10.13 (High Sierra), and above. <br />Any of the Linux platforms listed above. <br /> Windows 7 and above. |

## Download 

Download the installation package from [Linaro Forge Downloads](https://www.linaroforge.com/downloadForge/)

## Install on Linux

Extract the installation package and run the installer executable with these commands:

```bash
tar xf arm-forge-<version>-linux-<arch>.tar
cd arm-forge-<version>-linux-<arch>
```

For example, on an Arm machine:

```bash
tar xf arm-forge-22.1.4-linux-aarch64.tar
cd arm-forge-22.1.4-linux-aarch64
```

Run the installer and follow the steps. 

To install with the graphical installer, run:

```bash
./installer
```

To install with the text-mode installer, run:

```bash
./textinstall.sh
```

## Install on MacOS (remote client only)

Drag and drop the client application bundle icon into the Applications directory

## Install on Windows (remote client only)

Run the Windows file executable to install the Linaro Forge Remote Client

## Setting up the product license

You must install a license file on a machine running Linaro Forge tools to debug or profile. Setup instructions can be found [License Server User Guide](https://docs.linaroforge.com/22.1.3/html/101169_arm-licence-server-user-guide/index.html).

You do not need to install a license file on a machine running Linaro Forge Remote Client for connecting remotely to Linaro Forge tools on a remote system.

[Free trial licenses](https://www.linaroforge.com/freeTrial/) are available for you try out Linaro Forge.

## Get started

### Debugging

When compiling the program that you want to debug, you must add the debug flag to your compile command. For most compilers this is `-g`.

You should turn off compiler optimizations as they can produce unexpected results when debugging.

Linaro Forge's debugging tool, Linaro DDT, can be launched with the `ddt` command. For MPI applications, you can prefix the mpirun/mpiexec command normally used to run in parallel:

```bash
ddt mpirun -n 128 myapp
```

This startup method is called *Express Launch* and is the simplest way to get started. If your MPI is not supported by *Express Launch*, you can run the following instead:

```bash
ddt -n 128 myapp
```

These commands will launch Linaro DDT GUI. When running on a HPC cluster, you may need to debug on compute nodes where this may not be possible. In this case, you can start the GUI on the frontend node with the `ddt` command and when running or submitting a job to the compute nodes use `ddt --connect` :

With *Express Launch*:
```bash
ddt --connect mpirun -n 128 myapp
```

Without *Express Launch*:
```bash
ddt --connect -n 128 myapp
```

This mode is called *Reverse Connect*. A window will appear in the GUI when the application runs to notify of the incoming request.

### Profiling

In most cases, if your program is already compiled with debugging symbols (`-g`), you do not need to recompile your program to profile it with Linaro Forge. However, in some cases it might need to be relinked (see the [Linking](https://developer.arm.com/documentation/101136/latest/MAP/Get-started-with-MAP/Prepare-a-program-for-profiling)).

Typically you should keep optimization flags enabled when profiling (rather than profiling a debug build). This will give more representative results.

Linaro Forge's profiling tool, Linaro MAP, can be launched with the `map` command to launch the GUI. When running on a HPC cluster with MPI, you should use `map --profile` when running or submitting a job to the compute nodes:

With *Express Launch*:
```bash
map --profile mpirun -n 128 myapp
```

Without *Express Launch*:
```bash
map --profile -n 128 myapp
```

A *.map file will be created in the current directory with profiling results when the application terminates. This file can be then open from the GUI launched on the frontend node or with the following command:
```bash
map myapp_128p_<timestamp>.map
```

### Reporting

Linaro Forge's reporting tool Linaro Performance Reports is designed to run on unmodified production executables, so in general no preparation step is necessary. However, there is one important exception: statically linked applications require additional libraries at the linking step (see [user guide](https://developer.arm.com/documentation/101136/latest/Performance-Reports/Run-real-programs)).

Linaro Performance Reports does not use a GUI. Instead, it produces HTML and TXT files when the application terminates to summarize the application behavior. Here is how to use the tool on MPI applications

With *Express Launch*:
```bash
perf-report mpirun -n 128 myapp
```

Without *Express Launch*:
```bash
perf-report -n 128 myapp
```
Two files `myapp_128p_<timestamp>.html` and `myapp_128p_<timestamp>.txt` will be created in the current directory.

Linaro Forge is now installed and ready to use. 
