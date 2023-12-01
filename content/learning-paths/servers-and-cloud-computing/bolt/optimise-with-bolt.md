---
title: Optimise with BOLT
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Optimise with BOLT

##### Requirements

- `perf2bolt` and `llvm-bolt` on the path. See [BOLT](/install-guides/bolt/) for how to install.
- Executable
- `perf.data` containing executable profiling information

##### Steps

1. Use `perf2bolt` to convert the `perf.data` file into a `perf.fdata` format file
2. Use `llvm-bolt` to optimise the executable using the `perf.fdata` file 

## Convert perf.data

`perf2bolt` has 2 different aggregation methods (Basic & Branch) when coverting `perf.data` into a `perf.fdata`. Choosing which aggregation method to use depends upon the perf recording method. All 3 (Samples, ETM & SPE) can be converted using the Basic aggregation but only ETM can use Branch aggregation.

Branch aggregation it should be the prefered option. It will created a `perf.fdata` file with more information than Basic aggregation and this can improve the performance gains from optimisation.

Note that `perf2bolt` will run a few `perf script` commands and store the result in temporary files. These are deleted when `perf2bolt` exits but the files can get quite large. See [Appendix A - Perf Record Size Rates](../appendix-a/) for more information.

### Basic Aggregation

Basic aggregation looks at all instruction pointers that were recorded and then counts up how many times each one was recorded. The instruction pointers reference to code in the executable and by counting how many times each was run BOLT can find which code is run most often i.e hot path.

```bash { target="ubuntu:latest" }
perf2bolt -p perf.data -o perf.fdata ./executable -nl
```

### Branch Aggregation

Branch aggregation finds all the branches that were recorded. A branch can be a function call but it can also be the jump from if statements or loops, it is best to think of branches as changes in control flow and may not match exactly back onto the code due to how the compiler originally generated the code. From the list of branches we count up how many times each branch occured. From this BOLT can find which code sections are on the hot path and which sections are closly related.

The `--itrace` argument is required with to decode the instruction trace from the ETM records.

```bash { target="ubuntu:latest" }
perf2bolt -p perf.data -o perf.fdata ./executable --itrace=l64i1us
```

## Optimise Executable with BOLT

The final step is to generate a new executable using the `perf.fdata`.

```bash { target="ubuntu:latest" }
llvm-bolt ./executable -o ./new_executable -data perf.fdata -reorder-blocks=ext-tsp -reorder-functions=hfsort -split-functions -split-all-cold -split-eh -dyno-stats
```

See the BOLT README section on [Optimizing Bolts Performance](https://github.com/llvm/llvm-project/tree/main/bolt#optimizing-bolts-performance) for more info on how to use BOLT.
