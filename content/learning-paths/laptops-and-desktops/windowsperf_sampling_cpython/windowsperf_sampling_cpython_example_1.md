---
layout: learningpathall
title: WindowsPerf sample example
weight: 3
---

## Example 1: Sampling of CPython calculating Googolplex

{{% notice Note %}}
All steps in this sections are done on a native ARM64 Windows on Arm machine.
{{% /notice %}}

You will use the pre-built [CPython](https://github.com/python/cpython) binaries targeting `ARM64` from sources in debug mode from the previous step and:
* Pin `python_d.exe` interactive console to an arbitrary CPU core.
* Calculate a large integer number [Googolplex](https://en.wikipedia.org/wiki/Googolplex) to stress the CPython application and get a simple workload.
* Run counting and sampling to obtain some simple event information.

### Pin new CPython process to CPU core #1

Use Windows `start` command to execute and pin `python_d.exe` (CPython interactive console) to CPU core number `1`.

```command
start /affinity 2 python_d.exe
```

{{% notice Note %}}
[start](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start) command line switch `/affinity <hexaffinity>` applies the specified processor affinity mask (expressed as a hexadecimal number) to the new application. In our example decimal `2` is `0x02` or `0b0010`. This value denotes core no. 1 as 1 is a 1st bit in the mask, where the mask is indexed from 0 (zero).
{{% /notice %}}

This command will bring up CPython in interactive mode:

```output
Python 3.12.0a6+ (heads/main:1ff81c0cb6, Mar 14 2023, 16:26:50) [MSC v.1935 64 bit (ARM64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can use the Windows `Task Manager` to confirm that `python_d.exe` is running on CPU core #1. Newly created `CPython` interactive window will allow us to execute example workloads.

In the example below, you will calculate a very large integer `10^10^100`.

### Executing computation intensive calculation with CPython

In the CPython interactive window, type in the [Googolplex](https://en.wikipedia.org/wiki/Googolplex) number `10**10**100` and press enter.

```console
10**10**100
```

{{% notice Note %}}
This calculation will not terminate as it will take forever. So we have plenty of time to execute WindowsPerf sampling.
{{% /notice %}}

### Sampling CPython application running Googolplex calculation on CPU core 1

You can now sample the Arm PMU event `ld_spec` which corresponds to the speculatively executed load operation. Please note that you can specify the process image name and PDB file name with `--pdb_file python_d.pdb` and `--image_name python_d.exe`. In our case `wperf` is able to deduce image name (same as PE file name) and PDB file from PR file name.

You can stop sampling by pressing `Ctrl-C` in the `wperf` console or you can end the process you are sampling.

```command
wperf sample -e ld_spec:100000 --pe_file python_d.exe -c 1
```
Please wait few seconds for samples to arrive from Kernel driver and press `Ctrl+C` to stop sampling. You should see:

```output
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

{{% notice  Note%}}
You can close command line window with `python_d.exe` running when you finish sampling. Sampling will also automatically end when sample process finishes.
{{% /notice %}}

In the above example you can see that the majority of code executed by CPython's `python_d.exe` executable resides inside the `python312_d.dll` DLL.

Note that in `sampling ....e.e.e.e.e.` is a progressing printout where:
* character '`.`' represents sample payload (of 128 samples) received from the WindowsPerf Kernel driver and
* '`e`' represents an unsuccessful attempt to fetch whole sample payload.

{{% notice  Note%}}
You can also output `wperf sample` command in JSON format. Use `--json` command line option to enable JSON output.
Use `-v` command line option `verbose` to add more information about sampling
{{% /notice %}}

