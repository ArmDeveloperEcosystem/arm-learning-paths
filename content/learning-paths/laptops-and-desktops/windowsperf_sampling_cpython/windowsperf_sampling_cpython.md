---
layout: learningpathall
title: CPython Sampling Example Overview
weight: 2
---

# CPython Sampling Example

In this example, you will build a debug build of CPython from sources and then execute simple instructions in the Python interactive mode to obtain WindowsPerf sampling results from a CPython runtime image.

## Introduction

In this learning path, you will use sampling to determine CPython program "hot" locations provided by frequencies of PMU events specified by the user.

There are basically two models for using performance monitoring hardware:
* the counting model, for obtaining aggregate counts of occurrences of special events
* the sampling model, for determining the frequencies of event occurrences produced by program locations at the function, basic block, and/or instruction levels

WindowsPerf support both. 

{{% notice Note %}}
This example does not include information about the methodology used to determine the PMU events in this learning path.
{{% /notice %}}

You will try two ways of sampling with WindowsPerf via the `sample` and `record` commands.

## Before you begin

For this learning path you will need:
* A Windows on Arm (ARM64) native machine with preinstalled WindowsPerf (both driver and `wperf` CLI tool). See [WindowsPerf Install Guide](/install-guides/wperf/) for more details.
* x64 Windows build machine which we will use to cross-build CPython for ARM64 target.
  * Pre-installed  [Visual Studio 2022 Community Edition](https://visualstudio.microsoft.com/vs/) with LLVM support:
    * Go to the Visual Studio 2022 Community installer. Under Modify > Individual Components > search "clang".
    * install "C++ Clang Compiler..." and "MSBuild support for LLVM...".
* Basic knowledge of git and Python.
  * See [Install Git on Windows](https://github.com/git-guides/install-git#install-git-on-windows) for more details.
* Basic knowledge of Windows Remote Desktop use. Please read [How to use Remote Desktop](https://support.microsoft.com/en-us/windows/how-to-use-remote-desktop-5fe128d5-8fb1-7a23-3b8a-41e636865e8c) for more details.

### CPython cross-build on x64 machine targeting ARM64

CPython is an open-source project. There is native support in CPython for Windows on Arm starting with version 3.11. In this learning path you will use a debug build of CPython. For this, you will build [CPython](https://github.com/python/cpython) locally from sources in debug mode on an x86_64 machine and cross-compile it for an ARM64 target. 

Use the Visual Studio `Developer Command Prompt for VS 2022` which is already set up in the VS environment. Go to Start and search for "Developer Command Prompt for VS 2022".
You should see a prompt as shown below:

```console
**********************************************************************
** Visual Studio 2022 Developer Command Prompt v17.7.6
** Copyright (c) 2022 Microsoft Corporation
**********************************************************************

C:\Program Files\Microsoft Visual Studio\2022\Community>
```

{{% notice Note %}}
Please use `Developer Command Prompt for VS 2022` with all of the below steps.
{{% /notice %}}

#### Clone CPython source code

```command
git clone git@github.com:python/cpython.git
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
This step is optional, but please remember that you may encounter build issues unrelated to this example. For example, the CPython mainline source code that you've just checked out is not stable. Therefore, we recommend that you checkout SHA to avoid any unexpected issues.
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

The folder cpython\PCBuild contains `build.bat` build script you will use to build CPython from sources. Build CPython with debug symbols by invoking the `-d` command line option and select the ARM64 target with `-p ARM64`.

{{% notice Note %}}
Make sure you are using `Developer Command Prompt for VS 2022`.
{{% /notice %}}

```console
cd PCBuild
build.bat -d -p ARM64
```
The output will be similar to:

```console
Downloading nuget...
Installing Python via nuget...

...

  python.c
  python.vcxproj -> C:\<path>\cpython\PCbuild\arm64\python_d.exe
  Wrote C:\<path>\cpython\PCbuild\arm64\LICENSE.txt
  WinMain.c
  pythonw.vcxproj -> C:\<path\cpython\PCbuild\arm64\pythonw_d.exe

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:59.50
```

{{% notice Note %}}
The folder cpython\PCbuild\arm64 should contain all the executables built in this process. You will use `python_d.exe` in this example.
{{% /notice %}}

#### Setting up the ARM64 environment

{{% notice Note %}}
All the following steps are done on a native ARM64 Windows on Arm machine.
{{% /notice %}}

You will now move to a Windows on Arm (ARM64) native machine and perform the following steps:
* Copy the built CPython executables and libraries
* Execute the CPython interactive console to make sure all is set up

##### Copy the prebuilt CPython to an ARM64 machine

1. Create a new example directory on the ARM64 machine:

    ```console
    mkdir LearningPath
    ```

2. Copy the PCBuild\arm64 directory from your x86_64 build machine to the LearningPath directory on your ARM64 machine.

{{% notice Note %}}
You can use the Remote Desktop to copy a whole directory between two Windows machines with simple Ctrl+C / Ctrl+V.
{{% /notice %}}

3. Copy the Lib directory from your x86_64 build machine to the LearningPath directory on your ARM64 machine.

4. Your directory structure on ARM64 machine should look like this:

    ```
    LearningPath
    |
    ├───Lib
    └───PCBuild
        └───arm64
    ```

##### Execute interactive mode to make sure all the CPython dependencies and libraries are loaded

On your Windows ARM64 machine, open a command prompt and run:

```console
cd LearningPath\PCPuild\arm64
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
