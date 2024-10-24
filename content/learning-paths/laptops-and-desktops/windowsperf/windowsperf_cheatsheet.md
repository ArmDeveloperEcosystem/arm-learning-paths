---
layout: learningpathall
title: WindowsPerf cheat sheet
weight: 2
---

# WindowsPerf cheat sheet

The cheat sheet for the `wperf` command line tool focuses specifically on counting and sampling commands. It includes `wperf stat` for counting occurrences of specific PMU events and `wperf sample` and `wperf record` for sampling PMU event. Each command is explained with practical example.

## WindowsPerf cheat sheet (PMU Counting Examples)

- Count events `inst_spec`, `vfp_spec`, `ase_spec` and `ld_spec` on core #0 for 3 seconds:

```command
wperf stat -e inst_spec,vfp_spec,ase_spec,ld_spec -c 0 --timeout 3
```

- Count metric `imix` (metric events will be grouped) and additional event `l1i_cache` on core #7 for 10.5 seconds:

```command
wperf stat -m imix -e l1i_cache -c 7 --timeout 10.5
```

- Count in timeline mode (output counting to CSV file) metric `imix` 3 times on core #1 with 2 second intervals (delays between counts). Each count will last 5 seconds:

```command
wperf stat -m imix -c 1 -t -i 2 -n 3 --timeout 5
```

## WindowsPerf cheat sheet (PMU Sampling Examples)

- Launch and pin `python_d.exe –c 10**10**100` to core no. 1 and sample given image name:

```command
start /affinity 2 python_d.exe -c 10**10**100
wperf sample -e ld_spec:100000 -c 1 --pe_file python_d.exe --image_name python_d.exe
```

Same workflow can be wrapped with `wperf record` command, see example below:

- Launch `python_d.exe -c 10**10**100` process and start sampling event `ld_spec` with frequency `100000` on core no. 1 for 30 seconds.

```command
wperf record -e ld_spec:100000 -c 1 --timeout 30 -- python_d.exe -c 10**10**100
```

{{% notice Hint%}}
Add `--annotate` or `--disassemble` to `wperf record` command line parameters to increase sampling "resolution".
{{% /notice %}}

## WindowsPerf cheat sheet (SPE Examples)

Use Arm SPE optional extension to sample on core no. 1 process `python_d.exe`. SPE filter `load_filter` / `ld` enables collection of load sampled operations, including atomic operations that return a value to a register.

Note: Double-dash operator `--` can be used with SPE as well to launch the process.

```command
wperf record -e arm_spe_0/ld=1/ -c 1 -– python_d.exe -c 10**10**100
```

Above command can be replaces by below two commands:

```command
start /affinity 2 python_d.exe -c 10**10**100
wperf sample -e arm_spe_0/ld=1/ -c 1 --pe_file python_d.exe --image_name python_d.exe
```

{{% notice Hint%}}
Add `--annotate` or `--disassemble` to `wperf record` command line parameters to increase sampling "resolution".
{{% /notice %}}
