---
title: Understand Instruction Mix
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run Instruction Mix

Our previous Topdown analysis identified that our application used no Single-Instruction Multiple Data (SIMD) operations, which points to an optimization opportunity. Let's run the Instruction Mix recipe to learn more. The Recipe launch panel for Instruction Mix looks very similar to Topdown's, without options to specify which metrics to collect. Once again, be sure to spell out the full path to the workload.

![instruction-mix-config.jpg](instruction-mix-config.jpg)

The results below confirm a high number of integer and floating point math operations, and no SIMD operations. The Insights box on the right suggests vectorization as a path forward, with several possible root causes and a Next Steps section directing to other Learning Paths.

![instruction-mix-results.jpg](instruction-mix-results.jpg)

## Vectorize!

<!-- TODO - link to CPU hotspots LP -->
The Cpu Hotspots recipe can tell us which functions take the most time. `Mandelbrot::draw` and its inner function `Mandelbrot::getIterations` consumes a lot of runtime, so I've asked an LLM to try vectorizing that for my platform. It's done a fair job in https://github.com/bccbrendan/Mandelbrot-Example/tree/simd-instructions 

After running Instruction Mix again, we can see integer and floating point operations have been drastically reduced, replaced by a smaller amount of SIMD instructions. Exactly what we wanted!

![instruction-mix-simd-results.jpg](instruction-mix-simd-results.jpg)

Using the 'Compare' feature at the top, we can overlay these runs to see the change in each category in one view.

![instruction-mix-diff-results.jpg](instruction-mix-diff-results.jpg)

The execution time is significantly improved as well, nearly 4x!
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
