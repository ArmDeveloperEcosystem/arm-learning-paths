---
title: FAQ
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## FAQ

### Which record method should I use?

If you can record ETM on your Arm Linux system you should use that. It will generate branch samples that can't be recorded with Samples or SPE and will get maximum performance gains. If ETM is unavailable use SPE and then Samples.

### What can I do about the large perf.data files ETM generates?

You can use ETM AutoFDO that records small slices of ETM trace and will output much smaller files compared to ETM over the same time. Otherwise you can use SPE or Samples although SPE also generates large files.

### What should I run when collecting performance profile?

You should run the executable in a way that it is usually used. If it is run in an abnormal way BOLTs optimisations may hurt instead of help.

### What should I do if my executable is input dependent?

You can either find an input that covers all possible input cases. If this is not possible there are 2 other solutions. 

If you know which inputs go down which path you can record profiles for all these cases and then create an optimisted executable for each one. Then when you get input you need to pick with executable to run.

Another solution is to collect profiles for a range of inputs, generate a `.fdata` file for each one using `perf2bolt` and then combine these `.fdata` files into one file and that can used to by BOLT.

Collect profiles with different inputs

```bash { target="ubuntu:latest" }
perf record -e cycles:u -o perf1.data -- ./executable abc
perf record -e cycles:u -o perf2.data -- ./executable def
perf record -e cycles:u -o perf3.data -- ./executable ghi
```

Convert to `.fdata` format

```bash { target="ubuntu:latest" }
perf2bolt -p perf1.data -o perf1.fdata -nl ./executable
perf2bolt -p perf2.data -o perf2.fdata -nl ./executable
perf2bolt -p perf3.data -o perf3.fdata -nl ./executable
```

Combine `.fdata`

```bash { target="ubuntu:latest" }
merge-fdata *.fdata > combined.fdata
```

Optimise executable with `combined.fdata`

```bash { target="ubuntu:latest" }
llvm-bolt ./executable -o ./new_executable -data combined.fdata -reorder-blocks=ext-tsp -reorder-functions=hfsort -split-functions -split-all-cold -split-eh -dyno-stats
```

### How do I verify BOLT has optimised my executable?

You can check if it takes less time to run. This is fine for applications which run for some time, performing some operations and then exit but if it is a service and is just waiting for new input there are other methods check it has been improved.

#### Time

Use `time` to see how long each executable took and see if it has reduced.

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

#### Perf Stat

Perf stat can be used to measure time and record event counters.

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

These results also show how long each executable took to complete. BOLT rearranges the code in the executable into hot spots and that should reduce the number of instuction cache misses (l1i_cache_refill) and branch misses.
