---
layout: learningpathall
title: Setup 
weight: 3
---


## Before you begin

For this Learning Path, you will need:

* A Windows on Arm (AArch64) native machine with pre-installed WindowsPerf; both the driver and `wperf` CLI tool. See the [WindowsPerf Install Guide](/install-guides/wperf/) for more details.
  
  {{% notice Note %}}
The [WindowsPerf release 3.8.0](https://github.com/arm-developer-tools/windowsperf/releases/tag/3.8.0) includes a separate build with support for Arm SPE enabled. To install this version, download the release asset, and you will find WindowsPerf SPE build in the `SPE/` subdirectory.
{{% /notice %}}
* [Visual Studio](/install-guides/vs-woa/) installed.
* [Git](/install-guides/git-woa/) installed.
* A CPU that supports the Arm SPE extension. 

### How do I check if my Arm CPU supports the Arm SPE extension?

You can check your CPU compatibility using the WindowsPerf command-line tool. 

#### SPE hardware support detection:

You can check if WindowsPerf detects SPE support with the `wperf test` command. 

Run the command below and if the `spe_device.version_name` property shows `FEAT_SPE`, it means that WindowsPerf can use the SPE features. 

```console
wperf test
```

Here an example output for a system with SPE support:

```output
        Test Name                                           Result
        =========                                           ======
...
        spe_device.version_name                             FEAT_SPE
```

#### How do I check if the WindowsPerf binaries and driver support SPE?

{{% notice Note %}}
Currently, the WindowsPerf support of SPE is in development, and not all versions of WindowsPerf enable SPE support. Some WindowsPerf releases might contain separate binaries with SPE support enabled.
{{% /notice %}}

You can check the feature string `FeatureString` of both `wperf` and `wperf-driver` with `wperf --version` command:

```console
wperf --version
```

The output should be similar to:

```output
        Component     Version  GitVer          FeatureString
        =========     =======  ======          =============
        wperf         3.8.0    6d15ddfc        +etw-app+spe
        wperf-driver  3.8.0    6d15ddfc        +trace+spe
```

If the `FeatureString` for both `wperf` and `wperf-driver` contains `+spe`, the SPE features of WindowsPerf are available for you to use.

### Build CPython for AArch64

Perform the build steps below on your Windows on Arm system.

CPython is an open-source project, which includes native support for Windows on Arm starting with version 3.11. 

The SPE features demonstrated here use a debug build of CPython. You can build [CPython](https://github.com/python/cpython) locally from sources in debug mode.

Open a Visual Studio `Developer Command Prompt for VS 2022` command prompt. You can find this from Windows **Start** by searching for **Developer Command Prompt for VS 2022**.

When you open the command prompt, you will see output similar to:

```output
**********************************************************************
** Visual Studio 2022 Developer Command Prompt v17.7.6
** Copyright (c) 2022 Microsoft Corporation
**********************************************************************

C:\Program Files\Microsoft Visual Studio\2022\Community>
```

{{% notice Note %}}
For the remaining steps, use **Developer Command Prompt for VS 2022**. 
{{% /notice %}}

You can build CPython locally in debug mode using the `build.bat` script. 

#### Clone CPython source code

Obtain the CPython source code from GitHub:

```command
git clone https://github.com/python/cpython.git
```

The output from this command is similar to:

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

#### Checkout CPython with a specific SHA

{{% notice Note %}}
This step is optional, but you might encounter build issues unrelated to this example if the CPython mainline source code is not stable. It is best to checkout a specific SHA to avoid any unexpected issues and to ensure you are working off the same code base.
{{% /notice %}}

Use a specific CPython commit to match the output for this example:

```console
cd cpython
git checkout 1ff81c0cb67215694f084e51c4d35ae53b9f5cf9
```
The output is similar to:

```output
Updating files: 100% (2774/2774), done.
Note: switching to '1ff81c0cb67215694f084e51c4d35ae53b9f5cf9'.
...
```

#### Build CPython from sources

The `build.bat` script builds CPython from sources. Build CPython with debug symbols by invoking the `-d` command line option, and selecting the ARM64 target with `-p ARM64`.

Make sure you are using **Developer Command Prompt for VS 2022**.

Change to the `PCbuild` directory, and run the build command:

```console
cd PCbuild
build.bat -d -p ARM64
```

The output is similar to:

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

The folder `cpython\PCbuild\arm64` contains the executables built in this process. 

You will use `python_d.exe` to run Python.

##### Execute interactive mode to make sure all the CPython dependencies and libraries are loaded

Continue at the same command prompt, and test that Python runs correctly:

```console
cd arm64
python_d.exe
```

You can see CPython being invoked in interactive mode:

```output
Python 3.12.0a6+ (heads/main:1ff81c0cb6, Mar 14 2023, 16:26:50) [MSC v.1935 64 bit (ARM64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Type `quit()` to exit CPython.

Your environment is now ready to use WindowsPerf with SPE on CPython. 
