---
layout: learningpathall
title: CPython Sampling Example
weight: 4
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

## Prerequisites

For this example you will need:
* Windows on Arm (ARM64) machine with preinstalled `WindowsPerf` (both driver and `wperf` CLI tool).
* `x64` build machine we will use to cross-build CPython for ARM64 target.
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

## Example 1: Sampling of CPython calculating GooglePlex

### Pin new CPython process to CPU core #1

Use Windows `start` command to execute and pin `python_d.exe` (CPython interactive console) to CPU core number `1`.

```command
start /affinity 2 python_d.exe
```

{{% notice Note %}}
[start](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start) command line switch `/affinity <hexaffinity>` applies the specified processor affinity mask (expressed as a hexadecimal number) to the new application. In our example decimal `2` is `0x02` or `0b0010`. This value denotes core no. 1 as 1 is a 1st bit in the mask, where the mask is indexed from 0 (zero).
{{% /notice %}}

Newly created command line window will open with:
```console
Python 3.12.0a6+ (heads/main:1ff81c0cb6, Mar 14 2023, 16:26:50) [MSC v.1935 64 bit (ARM64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Check with Windows `Task Manager` if `python_d.exe` is running on CPU core #1. Newly created `CPython` interactive window will allow us to execute example workloads.
In the below example we will calculate a very large integer `10^10^100`.

### Executing computation intensive calculation with CPython

Type in CPython interactive window [Googolplex](https://en.wikipedia.org/wiki/Googleplex) formula `10**10**100` and press enter.

```command
>>> 10**10**100
```

{{% notice Note %}}
Above calculation will not terminate before the heat death of the universe. So we have plenty of time to execute WindowsPerf sampling.
{{% /notice %}}

### Sampling CPython application running Googolplex calculation on CPU core 1

Let's sample the `ld_spec` event. Please note that you can specify the process image name and PDB file name with `--pdb_file python_d.pdb` and `--image_name python_d.exe`. In our case `wperf` is able to deduce image name (same as PE file name) and PDB file from PR file name.

{{% notice Note %}}
Arm PMU event `ls_spec` corresponds to operation speculatively executed, `load`.
{{% /notice %}}

We can stop sampling by pressing `Ctrl-C` in the `wperf` console or we can end the process we are sampling.

```command
wperf sample -e ld_spec:100000 --pe_file python_d.exe -c 1
```
Please wait few seconds for samples to arrive from Kernel driver and press `Ctrl+C` to stop sampling. You should see:
```console
base address of 'python_d.exe': 0x7ff6e0a41270, runtime delta: 0x7ff5a0a40000
sampling ....e.e.e.e.e.eCtrl-C received, quit counting... done!
======================== sample source: ld_spec, top 50 hot functions ========================
 75.39%       579  x_mul:python312_d.dll
  6.51%        50  v_isub:python312_d.dll
  5.60%        43  _Py_atomic_load_32bit_impl:python312_d.dll
  3.12%        24  v_iadd:python312_d.dll
  2.60%        20  PyErr_CheckSignals:python312_d.dll
  2.08%        16  unknown
  1.17%         9  x_add:python312_d.dll
  0.91%         7  _Py_atomic_load_64bit_impl:python312_d.dll
  0.52%         4  _Py_ThreadCanHandleSignals:python312_d.dll
  0.52%         4  _PyMem_DebugCheckAddress:python312_d.dll
  0.26%         2  read_size_t:python312_d.dll
  0.13%         1  _Py_DECREF_SPECIALIZED:python312_d.dll
  0.13%         1  k_mul:python312_d.dll
  0.13%         1  _PyErr_CheckSignalsTstate:python312_d.dll
  0.13%         1  write_size_t:python312_d.dll
  0.13%         1  _PyObject_Malloc:python312_d.dll
  0.13%         1  pymalloc_alloc:python312_d.dll
  0.13%         1  pymalloc_free:python312_d.dll
  0.13%         1  _PyObject_Init:python312_d.dll
  0.13%         1  _PyMem_DebugRawFree:python312_d.dll
  0.13%         1  _PyLong_New:python312_d.dll
```

In the above example we can see that the majority of code executed by CPython's `python_d.exe` executable resides inside the `python312_d.dll` DLL.

Note that in `sampling ....e.e.e.e.e.` is a progressing printout where:
* character '`.`' represents sample payload (of 128 samples) received from the WindowsPerf Kernel driver and
* '`e`' represents an unsuccessful attempt to fetch whole sample payload.

{{% notice  Note%}}
You can also output `wperf sample` command in JSON format. Use `--json` command line option to enable JSON output.
{{% /notice %}}

{{% notice  Note%}}
Verbose mode in sampling: we've also added extra prints for verbose mode. Use `-v` command line option to add more information about sampling.
{{% /notice %}}
