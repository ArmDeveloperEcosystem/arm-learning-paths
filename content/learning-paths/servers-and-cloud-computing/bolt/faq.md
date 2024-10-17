---
title: FAQ
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

A set of frequently asked questions is below.

### Which recording method should I use?

If you can record ETM on your Arm Linux system you should use it. It will generate branch samples that can't be recorded with samples or SPE and will provide maximum performance gains. If ETM is not available then use SPE. If neither is available then use samples.

### What can I do about the large perf.data files ETM generates?

You can use ETM AutoFDO which uses trace strobing to record small slices and will output much smaller files compared to ETM. See [Using ETM AutoFDO](/learning-paths/servers-and-cloud-computing/bolt/bolt-etm/#using-etm-autofdo) section for more details. Otherwise you can use SPE or Samples. SPE also generates large files.

### What should I run when collecting performance profile?

You should run the executable in the way that it is usually used. If it is run in a different way then BOLT's optimizations may hurt instead of help.

### What should I do if my executable is input dependent?

You can either find an input that covers all possible input cases. If this is not possible there are 2 other solutions. 

If you know which inputs go down which path you can record profiles for multiple cases and then create an optimized executable for each case. Then when you get input you need to pick which executable to run.

Another solution is to collect profiles for a range of inputs, generate a `.fdata` file for each one using `perf2bolt` and then combine these `.fdata` files into one file and that can used to by BOLT.

For example, collect profiles with different inputs:

```bash { target="ubuntu:latest" }
perf record -e cycles:u -o perf1.data -- ./executable abc
perf record -e cycles:u -o perf2.data -- ./executable def
perf record -e cycles:u -o perf3.data -- ./executable ghi
```

Convert each case to the `.fdata` format:

```bash { target="ubuntu:latest" }
perf2bolt -p perf1.data -o perf1.fdata -nl ./executable
perf2bolt -p perf2.data -o perf2.fdata -nl ./executable
perf2bolt -p perf3.data -o perf3.fdata -nl ./executable
```

Combine the `.fdata` files into a single file: 

```bash { target="ubuntu:latest" }
merge-fdata *.fdata > combined.fdata
```

Run BOLT to optimize and create the new executable based on `combined.fdata`:

```bash { target="ubuntu:latest" }
llvm-bolt ./executable -o ./new_executable -data combined.fdata -reorder-blocks=ext-tsp -reorder-functions=hfsort -split-functions -split-all-cold -split-eh -dyno-stats
```

### How do I verify BOLT optimized my executable?

The easiest way to check is look at the names of the sections in the new executable because BOLT adds a few new sections with bolt in the name.

```bash { target="ubuntu:latest" }
objdump -h ./new_executable | grep bolt
```

If you see the `.bolt` sections you know this is the new executable:

```output
 12 .bolt.org.text 0000243c  0000000000000a80  0000000000000a80  00000a80  2**3
 15 .bolt.org.eh_frame_hdr 00000184  00000000000034c8  00000000000034c8  000034c8  2**2
 16 .bolt.org.eh_frame 0000056c  0000000000003650  0000000000003650  00003650  2**3
 30 .note.bolt_info 000000b0  0000000000000000  0000000000000000  00404bfc  2**0
```

Check the original executable to see that these sections didn't exist there before.

```bash { target="ubuntu:latest" }
objdump -h ./executable | grep bolt
```

The output should be empty.

### How do I check if the new BOLT executable has improved performance?

You can check if it takes less time to run. This is fine for applications which run for some time, performing some operations and then exit but if it is a service and is just waiting for new input there are other methods check it has been improved.

#### Use the time command

Use the `time` command to see how long each executable took and see if it has reduced.

For example, run both executables:

```bash { target="ubuntu:latest" }
time ./executable
time ./new_executable
```

```output
real    1m54.578s
user    1m51.222s
sys     0m2.700s

real    1m30.844s
user    1m26.917s
sys     0m2.853s
```

The `new_executable` ran for 23.8 seconds less.

#### Use Perf Stat

Perf stat can be used to measure time and record event counters.

For example, run both executables:

```bash { target="ubuntu:latest" }
perf stat -e task-clock,instructions,cycles,l1i_cache_refill,branch-misses -- ./executable
perf stat -e task-clock,instructions,cycles,l1i_cache_refill,branch-misses -- ./new_executable
```

```output
Performance counter stats for './executable':

         113326.10 msec task-clock                       #    0.994 CPUs utilized
      617222198064      instructions                     #    2.09  insn per cycle
      294642055705      cycles                           #    2.600 GHz
        9510653199      l1i_cache_refill                 #   83.923 M/sec
         852678168      branch-misses

     114.041719245 seconds time elapsed

     110.326924000 seconds user
       2.998557000 seconds sys

Performance counter stats for './new_executable':

          89683.53 msec task-clock                       #    0.989 CPUs utilized
      611936207251      instructions                     #    2.62  insn per cycle
      233172220555      cycles                           #    2.600 GHz
        2335713484      l1i_cache_refill                 #   26.044 M/sec
         473958601      branch-misses

      90.675836385 seconds time elapsed
```

These results also show how long each executable took to complete. BOLT rearranges the code in the executable into hot spots and that should reduce the number of instruction cache misses (l1i_cache_refill) and branch misses.
