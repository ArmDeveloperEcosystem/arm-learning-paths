---
title: Understand Instruction Mix
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run Instruction Mix

Our previous Topdown analysis identified that our application used no Single-Instruction Multiple Data (SIMD) operations, which points to an optimization opportunity. Let's run the Instruction Mix recipe to learn more. The Recipe launch panel for Instruction Mix looks very similar to Topdown's, without options to specify which metrics to collect. Once again, be sure to spell out the full path to the workload. This Mandelbrot example is native C++ code, not Java or .Net, so there's no need to collect managed code stacks.

![instruction-mix-config.jpg](instruction-mix-config.jpg)


The results below confirm a high number of integer and floating point math operations, and no SIMD operations. The Insights box on the right suggests vectorization as a path forward, with several possible root causes and a Next Steps section directing to other Learning Paths.

![instruction-mix-results.jpg](instruction-mix-results.jpg)

## Vectorize!

<!-- TODO - link to CPU hotspots LP -->
The Cpu Hotspots recipe can tell us which functions take the most time. `Mandelbrot::draw` and its inner function `Mandelbrot::getIterations` consumes a lot of runtime, so I've asked an LLM to try vectorizing that for my platform. It's done a fair job in https://github.com/bccbrendan/Mandelbrot-Example/tree/simd-instructions 
<!-- TODO - provide easier, more permanent link to vectorized code -->

After running Instruction Mix again, we can see integer and floating point operations have been drastically reduced, replaced by a smaller amount of SIMD instructions. Exactly what we wanted!

![instruction-mix-simd-results.jpg](instruction-mix-simd-results.jpg)

## Asses Improvements

Since we're doing multiple experiments, this is a good time to start giving our runs meaningful nicknames so we can organize them.
![rename-run.jpg](rename-run.jpg)

Using the 'Compare' feature at the top right of the an entry in the Runs view, we can select another run of the same recipe to compare results. 
![compare-with-box.jpg](compare-with-box.jpg)
This selection box will let you pick any run of the same recipe type. (Again, it's good to have meaningful run nicknames for this). The ⇅ arrows swap which of the two runs is considered the "baseline" and which is "current".

Once we've picked our two runs, we'll see them overlaid to see the change in each category in one view.

![instruction-mix-diff-results.jpg](instruction-mix-diff-results.jpg)

The execution time is significantly improved as well, nearly a 4x speedup.
```bash
$ time builds/mandelbrot-parallel-no-simd 1
Number of Threads = 1

real    0m31.326s
user    0m31.279s
sys     0m0.011s

$ time builds/mandelbrot-parallel 1
Number of Threads = 1

real    0m8.362s
user    0m8.331s
sys     0m0.016s
```

## Topdown Results Comparison

The Topdown recipe also supports a 'Compare' view showing the change in percentage points of each stage and instruction type.
![topdown-simd-results-diff.jpg](topdown-simd-results-diff.jpg)

We see now that the Load and Store operations dominate about 70% of the program's execution time. Insights offers several explainations as many different issues could be contributing root causes.
```
The CPU spends a larger share of cycles stalled in the backend, meaning execution or memory resources cannot complete work fast enough. This is a cycle-based measure (percentage of stalled cycles).

POSSIBLE CAUSES

- Slow memory access, for example, L2 cache misses or Dynamic Random-Access Memory (DRAM) misses
- Contention in execution pipelines, for example, the Arithmetic Logic Unit (ALU) or load/store units
- Poor data locality
- Excessive branching
- Instruction dependencies that create pipeline bubbles
```

We'll try adding some optimizing flags to the compiler to aggressively unroll loops.
```bash
    # build.sh
    CXXFLAGS=(
        --std=c++11
        -O3
        -mcpu=neoverse-n1+crc+crypto
        -ffast-math
        -funroll-loops
        -flto
        -DNDEBUG
    )
```

The runtime is again improved greatly. an additional 11x speedup over the SIMD implementation with default compiler flags.

```sh
time ./builds/mandelbrot-parallel 1
Number of Threads = 1

real    0m0.743s
user    0m0.724s
sys     0m0.014s
```

And with another Topdown measurement we see the Loads and Stores all but eliminated. SIMD floating point operations dominate the execution - an indication that our application is now well tuned to maximize the data flow to the floating point execution units.
The program is still generating the same output, but we're reduced the runtime from 31s to <1s - a 43x speedup!