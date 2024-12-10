---
layout: learningpathall
title: CPython Sampling with SPE Example Overview
weight: 2
---

# CPython Sampling with SPE Example

In this example, you will build a debug build of CPython from sources and then execute simple instructions in the Python interactive mode to obtain WindowsPerf sampling results from a CPython runtime image.

## The Arm Statistical Profiling Extension Introduction

The Arm Statistical Profiling Extension (SPE) is a feature defined as part of the Armv8-A architecture, starting from version 8.2. It provides non-invasive, hardware-based statistical sampling for CPUs. Unlike the Performance Monitor Unit (PMU), SPE is a different module that integrates the sampling process into the instruction execution process within the CPU's pipelines.

SPE is particularly useful for performance analysis and optimization, as it provides detailed insights into the behavior of the CPU during execution. This can help identify performance bottlenecks and optimize software for better efficiency.

## Introduction

You will use sampling to determine CPython program "hot" locations provided by Arm Statistical Profiling Extension (SPE).

WindowsPerf added support (in `record` command) for the [Arm Statistical Profiling Extension (SPE)](https://developer.arm.com/documentation/101136/22-1-3/MAP/Arm-Statistical-Profiling-Extension--SPE-). SPE is an optional feature in ARMv8.2 hardware that allows CPU instructions to be sampled and associated with the source code location where that instruction occurred.

{{% notice Note %}}
Currently SPE is available on Windows On Arm in Test Mode only!
{{% /notice %}}

## Before you begin

For this learning path you will need:
* A Windows on Arm (ARM64) native machine with pre-installed WindowsPerf (both driver and `wperf` CLI tool). See [WindowsPerf Install Guide](/install-guides/wperf/) for more details.
  * Note: The [WindowsPerf release 3.8.0](https://github.com/arm-developer-tools/windowsperf/releases/tag/3.8.0) includes a separate build with Arm SPE (Statistical Profiling Extension) support enabled. To install this version download release asset and you will find WindowsPerf SPE build in the `SPE/` subdirectory.
* CPU must support Arm SPE extension, an optional feature in ARMv8.2 hardware - we will show you how to check your CPU compatibility using WindowsPerf command-line tool.
* Basic knowledge of git and Python.
  * See [Install Git on Windows](https://github.com/git-guides/install-git#install-git-on-windows) for more details.

### How to check if your ARM64 CPU supports Arm SPE extension

#### SPE hardware support detection:

You can check if your system supports SPE or if WindowsPerf can detect SPE with `wperf test` command. See below an example of `spe_device.version_name property` value on system with SPE:

```console
wperf test
```

```output
        Test Name                                           Result
        =========                                           ======
...
        spe_device.version_name                             FEAT_SPE
```

#### How do I know if your WindowsPerf binaries and driver support optional SPE?

{{% notice Note %}}
Currently WindowsPerf support of SPE is in development, not all versions of WindowsPerf enable SPE support. Some WindowsPerf releases may contain separate binaries with SPE support enables.
{{% /notice %}}

You can check feature string `FeatureString` of both `wperf` and `wperf-driver` with `wperf --version` command:

```console
wperf --version
```

```output
        Component     Version  GitVer          FeatureString
        =========     =======  ======          =============
        wperf         3.8.0    6d15ddfc        +etw-app+spe
        wperf-driver  3.8.0    6d15ddfc        +trace+spe
```

If `FeatureString` for both components (`wperf` and `wperf-driver`) contains `+spe` (and `spe_device.version_name` contains `FEAT_SPE`) you are good to go!

### Build CPython targeting ARM64

Note: all steps are done on Windows on Arm system with ARM64 CPU.

CPython is an open-source project. There is native support in CPython for Windows on Arm starting with version 3.11. In this learning path you will use a debug build of CPython. For this, you will build [CPython](https://github.com/python/cpython) locally from sources in the debug mode on an x86_64 machine and cross-compile it for an ARM64 target. 

{{% notice Note %}}
Use the Visual Studio `Developer Command Prompt for VS 2022` which is already set up in the VS environment. Go to Start and search for "Developer Command Prompt for VS 2022".
{{% /notice %}}

You should see a prompt as shown below:

```output
**********************************************************************
** Visual Studio 2022 Developer Command Prompt v17.7.6
** Copyright (c) 2022 Microsoft Corporation
**********************************************************************

C:\Program Files\Microsoft Visual Studio\2022\Community>
```

{{% notice Note %}}
Please use `Developer Command Prompt for VS 2022` with all of the next steps.
{{% /notice %}}

---

Let's build CPython locally in debug mode using the `build.bat` script. You have the option to build CPython directly on your ARM64 machine or cross-compile it on an x64 machine. Below is an example demonstrating how to build it on an ARM64 machine.

#### Clone CPython source code

```command
git clone https://github.com/python/cpython.git
```

The output from this command will be similar to:

```output
Cloning into 'cpython'...
remote: Enumerating objects: 990145, done.
remote: Counting objects: 100% (43119/43119), done.
remote: Compressing objects: 100% (896/896), done.
remote: Total 990145 (delta 42673), reused 42290 (delta 42223), pack-reused 947026
Receiving objects: 100% (990145/990145), 527.93 MiB | 14.28 MiB/s, done.
Resolving deltas: 100% (792463/792463), done.
Updating files: 100% (4647/4647), done.
```

#### Checkout CPython at specific SHA

{{% notice Note %}}
This step is optional, but please remember that you may encounter build issues unrelated to this example as the CPython mainline source code that you've just checked out is not stable. Therefore, we recommend that you check out SHA to avoid any unexpected issues and to ensure you are working off the same code base.
{{% /notice %}}

Use a specific CPython commit to match the sampling output in this example:

```console
cd cpython
git checkout 1ff81c0cb67215694f084e51c4d35ae53b9f5cf9
```
The output will be similar to:

```output
Updating files: 100% (2774/2774), done.
Note: switching to '1ff81c0cb67215694f084e51c4d35ae53b9f5cf9'.
...
```

#### Build CPython from sources

The folder `cpython\PCbuild` contains the `build.bat` script you will use to build CPython from sources. Build CPython with debug symbols by invoking the `-d` command line option and select the ARM64 target with `-p ARM64`.

{{% notice Note %}}
Make sure you are using `Developer Command Prompt for VS 2022`.
{{% /notice %}}

```console
cd PCbuild
build.bat -d -p ARM64
```
The output will be similar to:

```output
Downloading nuget...
Installing Python via nuget...

...

  python.c
  python.vcxproj -> C:\\path\to\cpython\PCbuild\arm64\python_d.exe
  Wrote C:\path\to\cpython\PCbuild\arm64\LICENSE.txt
  WinMain.c
  pythonw.vcxproj -> C:\path\to\cpython\PCbuild\arm64\pythonw_d.exe

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:59.50
```

{{% notice Note %}}
The folder `cpython\PCbuild\arm64` should contain all the executables built in this process. You will use `python_d.exe` in this example.
{{% /notice %}}

##### Execute interactive mode to make sure all the CPython dependencies and libraries are loaded

On your Windows ARM64 machine, open a command prompt and run:

```console
cd c:\path\to\cpython\PCbuild\arm64
python_d.exe
```
You should see CPython being invoked in interactive mode:

```output
Python 3.12.0a6+ (heads/main:1ff81c0cb6, Mar 14 2023, 16:26:50) [MSC v.1935 64 bit (ARM64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

{{% notice Note %}}
Your environment should now be fully set up and you are ready to move on to the next step.
{{% /notice %}}
