---
layout: learningpathall
title: CPython Sampling Example Overview
weight: 2
---

# CPython Sampling Example

In this example we will build CPython from sources and execute simple instructions in Python interactive mode to obtain WindowsPerf sampling results from CPython runtime image.

## Introduction

There are basically two models of using performance monitoring hardware:
* the `counting model`, for obtaining aggregate counts of occurrences of special events and 
* the `sampling model`, for determining the frequencies of event occurrences produced by program locations at the function, basic block, and/or instruction levels.

In this example we will use `sampling` to determine CPython program "hot" locations determined by frequencies of PMU event specified by user.

{{% notice Note %}}
This example do not include information about methodology used to determine PMU events used to guide this sampling example.
{{% /notice %}}

In short we will:

* Build [CPython](https://github.com/python/cpython) binaries targeting ARM64 from sources in debug mode.
* Pin `python_d.exe` interactive console to arbitrary CPU core.
* Try to calculate absurdly large integer number [Googolplex](https://en.wikipedia.org/wiki/Googolplex) to stress CPython application and get a simple workload.
* Run counting and sampling to obtain some simple event information.

Please note that we will present you two ways of sampling with `WindowsPerf`: `sample` and `record` command.

## Prerequisites

For this example you will need:
* Windows on Arm (ARM64) native machine with preinstalled `WindowsPerf` (both driver and `wperf` CLI tool).
* `x64` build machine we will use to cross-build CPython for ARM64 target.
  * Pre-installed  [Visual Studio 2022 Community Edition](https://visualstudio.microsoft.com/vs/).
* Basic knowledge of `git` and `Python`.

### CPython cross-build on x64 machine targeting ARM64

CPython is an open-source project. Let's build [CPython](https://github.com/python/cpython) locally from sources in debug mode. We will in this example cross-compile CPython to the `ARM64` target. IN below example build machine is `x64`.

#### Clone locally CPython source code

```command
git clone git@github.com:python/cpython.git
```

```console
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

For this example we want you to use same CPython commit we are using so that your sampling example output matches this example.

```
cd cpython
git checkout 1ff81c0cb67215694f084e51c4d35ae53b9f5cf9
```

```console
Updating files: 100% (2774/2774), done.
Note: switching to '1ff81c0cb67215694f084e51c4d35ae53b9f5cf9'.
...
```

{{% notice Note %}}
This step is optional, but please remember that you may encounter build issues unrelated to this example. For example CPython bleeding edge source code you've just checked out is not stable. We recommend you checkout above SHA to avoid unexpected issues.
{{% /notice %}}

#### Build CPython from sources

Folder `cpython\PCBuild` contains `build.bat` build script we will use to build CPython from sources. We will build CPython with debug symbols by invoking `-d` command line option and select `ARM64` target with `-p ARM64`.

```command
cd PCBuild
build.bat -d -p ARM64
```


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
Folder `cpython\PCbuild\arm64` should contain all executables build in this process. We will focus on `python_d.exe` application in our example.
{{% /notice %}}

#### Setting up ARM64 environment

```command
arm64>python_d.exe
```

```console
Python 3.12.0a6+ (heads/main:1ff81c0cb6, Mar 14 2023, 16:26:50) [MSC v.1935 64 bit (ARM64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
