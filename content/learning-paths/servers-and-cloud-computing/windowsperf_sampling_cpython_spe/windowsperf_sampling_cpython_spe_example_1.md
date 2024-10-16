---
layout: learningpathall
title: WindowsPerf sample using SPE example
weight: 3
---

## Example 1: Sampling of CPython calculating Googolplex using SPE

{{% notice Note %}}
All the steps in these following sections are done on a native ARM64 Windows on Arm machine.
{{% /notice %}}

You will use the pre-built [CPython](https://github.com/python/cpython) binaries targeting ARM64 from sources in the debug mode from the previous step and then complete the following:
- Pin `python_d.exe` interactive console to an arbitrary CPU core, calculate `10^10^100` expression, a large integer number [Googolplex](https://en.wikipedia.org/wiki/Googolplex) to stress the CPython application and get a simple workload.
- Run counting and sampling to obtain some simple event information.

### Pin the new CPython process to a CPU core 1

Use the Windows `start` command to execute and pin `python_d.exe` process to CPU core number 1. Below command is executing computation intensive calculations of `10^10^100`, a [Googolplex](https://en.wikipedia.org/wiki/Googolplex) number, with CPython.

```command
start /affinity 2 cpython\PCbuild\arm64\python_d.exe -c 10**10**100
```

{{% notice Note %}}
The [start](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start) command line switch `/affinity <hexaffinity>` applies the specified processor affinity mask (expressed as a hexadecimal number) to the new application. In our example decimal `2` is `0x02` or `0b0010`. This value denotes core no. `1` as `1` is a first bit in the mask, where the mask is indexed from `0` (zero).
{{% /notice %}}

You can use the Windows Task Manager to confirm that `python_d.exe` is running on CPU core no. 1.

### SPE introduces new option for command line switch -e arm_spe_0//

Users can specify SPE filters using the `-e` command line option with `arm_spe_0//`. We've introduced the `arm_spe_0/*/` notation for the `sample` and `record` command, where `*` represents a comma-separated list of supported filters. Currently, we support filters such as `store_filter=`, `load_filter=`, and `branch_filter=`, or their short equivalents like `st=`, `ld=`, and `b=`. Use `0` or `1` to disable or enable a given filter. For example:

```output
arm_spe_0/branch_filter=1/
arm_spe_0/load_filter=1,branch_filter=0/
arm_spe_0/ld=1,branch_filter=0/
arm_spe_0/st=0,ld=0,b=1/
```

#### Filtering sample records

SPE register `PMSFCR_EL1.FT` enables filtering by operation type. When enabled `PMSFCR_EL1.{ST, LD, B}` define the collected types:
- `ST` enables collection of store sampled operations, including all atomic operations.
- `LD` enables collection of load sampled operations, including atomic operations that return a value to a register.
- `B` enables collection of branch sampled operations, including direct and indirect branches and exception returns.

### Sampling using SPE the CPython application running the Googolplex calculation on CPU core 1

Below command will sample already running process `python_d.exe` (denoted with `--image_name python_d.exe`) on CPU core no. 1. SPE filter `ld=1` enables collection of load sampled operations, including atomic operations that return a value to a register.

```command
wperf sample -e arm_spe_0/ld=1/ --pe_file cpython\PCbuild\arm64\python_d.exe --image_name python_d.exe -c 1
```

{{% notice  Note%}}
You can use the same sampling `--annotate` and `--disassemble` command line interface of WindowsPerf with SPE extension. See example outputs below.
{{% /notice %}}

Please wait a few seconds for the samples to arrive from the Kernel driver and then press `Ctrl+C` to stop sampling. You should see:

```output
base address of 'python_d.exe': 0x7ff765fe1288, runtime delta: 0x7ff625fe0000
sampling ....eee....eCtrl-C received, quit counting... done!

Performance counter stats for core 1, no multiplexing, kernel mode excluded, on Arm Limited core implementation:
note: 'e' - normal event, 'gN' - grouped event with group number N, metric name will be appended if 'e' or 'g' comes from it

         counter value  event name        event idx  event note
         =============  ==========        =========  ==========
        29,337,387,738  cycle             fixed      e
        76,433,491,476  sample_pop        0x4000     e
                    18  sample_feed       0x4001     e
                     7  sample_filtrate   0x4002     e
                     0  sample_collision  0x4003     e
======================== sample source: LOAD_STORE_ATOMIC-LOAD-GP/retired+level1-data-cache-access+tlb_access, top 50 hot functions ========================
        overhead  count  symbol
        ========  =====  ======
           85.71      6  x_mul:python312_d.dll
           14.29      1  unknown
          100.00%     7  top 2 in total

               9.853 seconds time elapsed
```

{{% notice  Note%}}
You can close the command line window with `python_d.exe` running when you have finished sampling. Sampling will also automatically end when the sample process has finished.
{{% /notice %}}


#### SPE sampling output

- In the above example, you can see that the majority of "overhead" is generated by `python_d.exe` executable resides inside the `python312_d.dll` DLL, in `x_mul` symbol.
- SPE sampling output contains also PMU events for SPE registered during sampling:
  - `sample_pop` - Statistical Profiling sample population. Counts statistical profiling sample population, the count of all operations that could be sampled but may or may not be chosen for sampling.
  - `sample_feed` - Statistical Profiling sample taken. Counts statistical profiling samples taken for sampling.
  - `sample_filtrate` - Statistical Profiling sample taken and not removed by filtering. Counts statistical profiling samples taken which are not removed by filtering.
  - `sample_collision` - Statistical Profiling sample collided with previous sample. Counts statistical profiling samples that have collided with a previous sample and so therefore not taken.
- Note that in sampling `....eee....e` is a progressing printout where:
  - character `.` represents a SPE sample payload received from the WindowsPerf Kernel driver and
  - character `e` represents an unsuccessful attempt (empty SPE fill buffer) to fetch the whole sample payload.

{{% notice  Note%}}
You can also output `wperf sample` command in JSON format. Use the `--json` command line option to enable the JSON output.
Use the `-v` command line option `verbose` to add more information about sampling.
{{% /notice %}}

#### Example output with annotate enabled

Command line option `--annotate` enables translating addresses taken from samples in sample/record mode into source code line numbers.

```console
wperf sample -e arm_spe_0/ld=1/ --annotate --pe_file cpython\PCbuild\arm64\python_d.exe --image_name python_d.exe -c 1
```

```output
base address of 'python_d.exe': 0x7ff765fe1288, runtime delta: 0x7ff625fe0000
sampling ....ee.Ctrl-C received, quit counting...e done!

Performance counter stats for core 1, no multiplexing, kernel mode excluded, on Arm Limited core implementation:
note: 'e' - normal event, 'gN' - grouped event with group number N, metric name will be appended if 'e' or 'g' comes from it

         counter value  event name        event idx  event note
         =============  ==========        =========  ==========
        15,579,045,952  cycle             fixed      e
        40,554,143,220  sample_pop        0x4000     e
                    10  sample_feed       0x4001     e
                     2  sample_filtrate   0x4002     e
                     0  sample_collision  0x4003     e
======================== sample source: LOAD_STORE_ATOMIC-LOAD-GP/retired+level1-data-cache-access+tlb_access, top 50 hot functions ========================
x_mul:python312_d.dll
        line_number  hits  filename
        ===========  ====  ========
        3,590        2     C:\path\to\cpython\Objects\longobject.c

        overhead  count  symbol
        ========  =====  ======
          100.00      2  x_mul:python312_d.dll
          100.00%     2  top 1 in total

               5.199 seconds time elapsed
```

Note: Above SPE sampling pass recorded:
- function `x_mul:python312_d.dll`:
  - in source file `C:\path\to\cpython\Objects\longobject.c`, line `3590` as a hot-spot for `load_filter` enabled.

#### Example output with disassemble enabled

Command line option `--disassemble` enables disassemble output on sampling mode. Implies `--annotate`.

```console
wperf sample -e arm_spe_0/ld=1/ --disassemble --pe_file cpython\PCbuild\arm64\python_d.exe --image_name python_d.exe -c 1
```

```output
base address of 'python_d.exe': 0x7ff765fe1288, runtime delta: 0x7ff625fe0000
sampling ......eCtrl-C received, quit counting... done!

Performance counter stats for core 1, no multiplexing, kernel mode excluded, on Arm Limited core implementation:
note: 'e' - normal event, 'gN' - grouped event with group number N, metric name will be appended if 'e' or 'g' comes from it

         counter value  event name        event idx  event note
         =============  ==========        =========  ==========
        13,193,499,134  cycle             fixed      e
        34,357,259,935  sample_pop        0x4000     e
                     8  sample_feed       0x4001     e
                     4  sample_filtrate   0x4002     e
                     0  sample_collision  0x4003     e
======================== sample source: LOAD_STORE_ATOMIC-LOAD-GP/retired+level1-data-cache-access+tlb_access, top 50 hot functions ========================
x_mul:python312_d.dll
        line_number  hits  filename                                                        instruction_address  disassembled_line
        ===========  ====  ========                                                        ===================  =================
        3,591        2     C:\path\to\cpython\Objects\longobject.c  4043b4                 address  instruction
                                                                                           =======  ===========
                                                                                           4043a8   ldr   x8, [sp, #0x10]
                                                                                           4043ac   and   x8, x8, #0x3fffffff
                                                                                           4043b0   mov   w8, w8
                                                                                           4043b4   ldr   x9, [sp, #0x20]
                                                                                           4043b8   str   w8, [x9]
                                                                                           4043bc   ldr   x8, [sp, #0x20]
                                                                                           4043c0   add   x8, x8, #0x4
                                                                                           4043c4   str   x8, [sp, #0x20]
        3,589        1     C:\path\to\cpython\Objects\longobject.c  404360                 address  instruction
                                                                                           =======  ===========
                                                                                           40435c   ldr   x9, [sp, #0x108]
                                                                                           404360   ldr   x8, [sp, #0x58]
                                                                                           404364   cmp   x8, x9
                                                                                           404368   b.hs  0x18040440c <_PyCrossInterpreterData_UnregisterClass+0x3fc680>

v_isub:python312_d.dll
        line_number  hits  filename                                                        instruction_address  disassembled_line
        ===========  ====  ========                                                        ===================  =================
        1,603        1     C:\path\to\cpython\Objects\longobject.c  402a60                 address  instruction
                                                                                           =======  ===========
                                                                                           402a60   ldr   w8, [sp, #0x10]
                                                                                           402a64   and   w8, w8, #0x1
                                                                                           402a68   str   w8, [sp, #0x10]

        overhead  count  symbol
        ========  =====  ======
           75.00      3  x_mul:python312_d.dll
           25.00      1  v_isub:python312_d.dll
          100.00%     4  top 2 in total

               4.422 seconds time elapsed
```

Note: Above SPE sampling pass recorded:
- function `x_mul:python312_d.dll`:
  - in source file `C:\path\to\cpython\Objects\longobject.c`, line `3591`, instruction `ldr   x9, [sp, #0x20]` at address `0x4043b4` as potential hot-spot.
  - in source file `C:\path\to\cpython\Objects\longobject.c`, line `3589`, instruction `ldr   x8, [sp, #0x58]` at address `0x404360` as potential hot-spot.
- Function `v_isub:python312_d.dll`:
  - in source file `C:\path\to\cpython\Objects\longobject.c`, line `1603`, instruction `ldr   w8, [sp, #0x10]` at address `0x402a60` as potential hot-spot.
