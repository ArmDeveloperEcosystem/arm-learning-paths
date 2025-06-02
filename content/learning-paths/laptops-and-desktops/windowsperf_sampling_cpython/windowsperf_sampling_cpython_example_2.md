---
layout: learningpathall
title: WindowsPerf record example
weight: 4
---

## Example 2: Using the `record` command to simplify things

The `record` command spawns the process and pins it to the core specified by the `-c` option. You can either use `--pe_file` to let WindowsPerf know which process to spawn or simply add the process to spawn at the very end of the `wperf` command. 

This simplifies the steps presented in the previous example.

If you want to pass command line arguments to your application, you can call them after all of the WindowsPerf options. All command line arguments are going to be passed
verbatim to the program that is being spawned. If you want to execute the CPython example above using this approach, you could just type:

```command
wperf record -e ld_spec:100000 -c 1 --timeout 30 -- python_d.exe -c 10**10**100
```

{{% notice  Note%}}
This command will automatically spawn the process `python_d.exe -c 10**10**100` (and pass command line options to it), sample for 30 seconds with `--timeout 30` event `ld_spec` with sample frequency of `100000`.
{{% /notice %}}

You should see the same output from this command as in the previous section.
