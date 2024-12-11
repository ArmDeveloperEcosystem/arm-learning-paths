---
layout: learningpathall
title: WindowsPerf record using SPE example
weight: 4
---

## Example 2: Using the `record` command to simplify things

- The `record` command spawns the process and pins it to the core specified by the `-c` option. 
- A double-dash (`--`) is a syntax used in shell commands to signify end of command options and beginning of positional arguments. In other words, it separates `wperf` CLI options from arguments that the command operates on. Use `--` to separate `wperf.exe` command line options from the process you want to spawn followed by its verbatim arguments.

```console
wperf record -e arm_spe_0/ld=1/ -c 1 --timeout 5 -- cpython\PCbuild\arm64\python_d.exe -c 10**10**100
```

{{% notice  Note%}}
You can use the same sampling `--annotate` and `--disassemble` command line interface of WindowsPerf with SPE extension.
{{% /notice %}}

The WindowsPerf `record` command is versatile, allowing you to start and stop the sampling process easily. It also simplifies the command line syntax, making it user-friendly and efficient.

Example 2 can be replaced by these two commands:

```console
start /affinity 2 cpython\PCbuild\arm64\python_d.exe -c 10**10**100
wperf sample -e arm_spe_0/ld=1/ --pe_file cpython\PCbuild\arm64\python_d.exe --image_name python_d.exe -c 1
```

## Summary

WindowsPerf is a versatile performance analysis tool that can support both software (with CPU PMU events) and hardware sampling (with SPE extension). The type of sampling it can perform depends on the availability of the Arm Statistical Profiling Extension (SPE) in the ARM64 CPU. If the Arm SPE extension is present, WindowsPerf can leverage hardware sampling to provide detailed performance insights. Otherwise, it will rely on software sampling to gather performance data. This flexibility ensures that WindowsPerf can adapt to different hardware configurations and still deliver valuable performance metrics.

Use `wperf sample`, a sampling mode, for determining the frequencies of event occurrences produced by program locations at the function, basic block, and/or instruction levels.

Use `wperf record`, same as sample but also automatically spawns the process and pins it to the core specified by `-c`. Process name is defined by COMMAND. User can pass verbatim arguments to the process.
