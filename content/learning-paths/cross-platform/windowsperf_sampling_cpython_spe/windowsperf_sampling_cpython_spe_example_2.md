---
layout: learningpathall
title: WindowsPerf record using SPE example
weight: 4
---

## Example 2: Record CPython using SPE

You can use the `record` command to spawn the Python process and pin it to the core specified by the `-c` option. 

A double-dash (`--`) syntax in shell commands signifies the end of command options and beginning of positional arguments. In other words, it separates the `wperf` CLI options from the arguments passed to the profiled program, `python_d.exe`. 

Run the `record` command with SPE to collect load events from SPE:

```console
wperf record -e arm_spe_0/ld=1/ -c 1 --timeout 5 -- cpython\PCbuild\arm64\python_d.exe -c 10**10**100
```

You can use the same `--annotate` and `--disassemble` command line arguments the SPE extension.

The WindowsPerf `record` command is versatile, allowing you to start and stop the sampling process easily. It also simplifies the command line syntax, making it user-friendly and efficient.

The example above can be replaced by these two commands:

```console
start /affinity 2 cpython\PCbuild\arm64\python_d.exe -c 10**10**100
wperf sample -e arm_spe_0/ld=1/ --pe_file cpython\PCbuild\arm64\python_d.exe --image_name python_d.exe -c 1
```

## Summary

WindowsPerf is a versatile performance analysis tool supporting both software (with CPU PMU events) and hardware sampling (with the SPE extension). 

The type of sampling it can perform depends on the availability of the Arm Statistical Profiling Extension (SPE) in the CPU. If the Arm SPE extension is present, WindowsPerf can leverage hardware sampling to provide detailed performance insights. Otherwise, it will rely on software sampling to gather performance data. This flexibility ensures that WindowsPerf can adapt to different hardware configurations and still deliver valuable performance metrics.

Use `wperf sample`, sampling mode, for determining the frequencies of event occurrences produced by program locations at the function, basic block, and/or instruction levels.

Use `wperf record`, is the same as sample, but also automatically spawns the process and pins it to the core specified by `-c`. You can use `record` to pass verbatim arguments to the process.
