---
title: FAQ
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## FAQ

### Which record method should I use?

If you can record ETM on your Arm Computer you should use that. It will generate branch samples that can't be recorded with Samples or SPE and will get maximum performance gains. If ETM is unavailable use SPE and then Samples.

### What can I do about the larged perf.data files ETM generates?

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
