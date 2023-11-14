---
layout: learningpathall
title: CPython Sampling Example Overview
weight: 2
---

# CPython Sampling Example

In this example you will build a debug build of CPython from sources and execute simple instructions in Python interactive mode to obtain WindowsPerf sampling results from CPython runtime image.

## Introduction

There are basically two models of using performance monitoring hardware:
* the `counting model`, for obtaining aggregate counts of occurrences of special events and
* the `sampling model`, for determining the frequencies of event occurrences produced by program locations at the function, basic block, and/or instruction levels.

`WindowsPerf` support both. In this learning path you will use `sampling` to determine CPython program "hot" locations determined by frequencies of PMU event specified by user.

{{% notice Note %}}
This example do not include information about methodology used to determine PMU events used to guide this sampling example.
{{% /notice %}}

You will try two ways of sampling with `WindowsPerf`: `sample` and `record` command.

## Before you begin

For this learning path you will need:
* Windows on Arm (ARM64) native machine with preinstalled `WindowsPerf` (both driver and `wperf` CLI tool). See [WindowsPerf Install Guide](/install-guides/wperf/) for more details.
* `x64` Windows build machine we will use to cross-build CPython for ARM64 target.
  * Pre-installed  [Visual Studio 2022 Community Edition](https://visualstudio.microsoft.com/vs/) with LLVM support:
    * Go to `Visual Studio 2022 Community` installer under `Modify` -> `Individual Components` -> search `"clang"`.
    * install `"C++ Clang Compiler..."` and `"MSBuild support for LLVM..."`.
* Basic knowledge of `git` and `Python`.
  * See [Install Git on Windows](https://github.com/git-guides/install-git#install-git-on-windows) for more details.
* Basic knowledge of Windows Remote Desktop use. Please read [How to use Remote Desktop](https://support.microsoft.com/en-us/windows/how-to-use-remote-desktop-5fe128d5-8fb1-7a23-3b8a-41e636865e8c) for more details.

### CPython cross-build on x64 machine targeting ARM64

CPython is an open-source project. There is native support in CPython for Windows on Arm starting with version 3.11. But in this learning path you will use a debug build of CPython. For this, you will build [CPython](https://github.com/python/cpython) locally from sources in debug mode on an `x86_64` machine and cross-compile it for a `ARM64` target. 

Use Visual Studio `Developer Command Prompt for VS 2022` command line prompt which is already set up VS environment. Go to `Start` and search for `"Developer Command Prompt for VS 2022"`.
You should see a prompt as shown below:

```console
**********************************************************************
** Visual Studio 2022 Developer Command Prompt v17.7.6
** Copyright (c) 2022 Microsoft Corporation
**********************************************************************

C:\Program Files\Microsoft Visual Studio\2022\Community>
```

{{% notice Note %}}
Please use `Developer Command Prompt for VS 2022` with all below steps.
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

{{% notice Note %}}
This step is optional, but please remember that you may encounter build issues unrelated to this example. For example CPython mainline source code you've just checked out is not stable. We recommend you checkout above SHA to avoid unexpected issues.
{{% /notice %}}

#### Build CPython from sources

Folder `cpython\PCBuild` contains `build.bat` build script you will use to build CPython from sources. Build CPython with debug symbols by invoking `-d` command line option and select `ARM64` target with `-p ARM64`.

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
Folder `cpython\PCbuild\arm64` should contain all executables build in this process. You will use `python_d.exe` in this example.
{{% /notice %}}

#### Setting up ARM64 environment

{{% notice Note %}}
All steps going forward are done on native ARM64 Windows on Arm machine.
{{% /notice %}}

You will now move to a Windows on Arm (ARM64) native machine and perform the following steps:
* Copy there built CPython executables and libraries and
* Execute CPython interactive console to make sure all is set up.

##### Copy prebuilt CPython to ARM64 machine

1. Create a new example directory on `ARM64` machine:

    ```console
    mkdir LearningPath
    ```

2. Copy the `PCBuild\arm64` directory from your `x86_64` build machine to the `LearningPath` directory on your `ARM64` machine.

{{% notice Note %}}
You can use `Remote Desktop` to copy whole directory between two Windows machines with simple `Ctrl+C` / `Ctrl+V`.
{{% /notice %}}

3. Copy the `Lib` directory from your `x86_64` build machine to the `LearningPath` directory on you `ARM64` machine.

4. Your directory structure on `ARM64` machine should look like this:

    ```
    LearningPath
    |
    ├───Lib
    └───PCBuild
        └───arm64
    ```

##### Execute interactive mode to make sure all CPython dependencies and libraries are loaded

On your Windows `ARM64` machine, open a command prompt and run:

```console
cd LearningPath\PCPuild\arm64
python_d.exe
```
You should see CPython being invoked interactive mode:

```output
Python 3.12.0a6+ (heads/main:1ff81c0cb6, Mar 14 2023, 16:26:50) [MSC v.1935 64 bit (ARM64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

{{% notice Note %}}
Your environment should now be fully set up and you are ready to move to the next step.
{{% /notice %}}
