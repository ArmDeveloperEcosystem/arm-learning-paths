---
layout: learningpathall
title: WindowsPerf Record using SPE 
weight: 6
---

## Record CPython using SPE

You can use the `record` command to spawn the Python process and pin it to the core specified by the `-c` option. 

A double-dash (`--`) syntax in shell commands signifies the end of command options and beginning of positional arguments. 

This means that it separates the `wperf` CLI options from the arguments passed to the profiled program called `python_d.exe`. 

Run the `record` command with SPE to collect load events from SPE:

```console
wperf record -e arm_spe_0/ld=1/ -c 1 --timeout 5 -- cpython\PCbuild\arm64\python_d.exe -c 10**10**100
```

You can use the same `--annotate` and `--disassemble` command line arguments with the SPE extension.

The WindowsPerf `record` command is versatile, allowing you to start and stop the sampling process easily. It also simplifies the command-line syntax, making it user-friendly and efficient.

The example above can be replaced by these two commands:

```console
start /affinity 2 cpython\PCbuild\arm64\python_d.exe -c 10**10**100
wperf sample -e arm_spe_0/ld=1/ --pe_file cpython\PCbuild\arm64\python_d.exe --image_name python_d.exe -c 1
```

