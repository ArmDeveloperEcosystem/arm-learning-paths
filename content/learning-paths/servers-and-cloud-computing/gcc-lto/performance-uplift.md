---
title: Potential Gains
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Comparing Performance

The potential benefits to be gained from the use of LTO can be highlighted via performance comparison of the Specint2017 benchmark run on a Neoverse V2 CPU, compiled with and without LTO using GCC 15.1.

There was an uplift in the geometric mean of scores across different benchmarks, wherein we see an improvement of ~3.4%, with the biggest winners being`gmcf` (+11%), `deepsjeng` (9.9%), `leela` (6.6%).

![SPECint LTO performance gains#center](specint_lto_improv.png "Figure 1. Performance uplift to Specint2017")

### Code-size Considerations

As demonstrated above the overall performance of many executables is greatly improved by the optimization, but this is not the only obeservable gain to be had as a consequence of the optimization.

As shown in figure 2, the use of LTO can have considerable impact on the final code size of the resulting executable.

![SPECint LTO code size reduction#center](specint_lto_size.png "Figure 2. Code size reduction to Specint2017")

#### Potential Code Size Reduction

One example where LTO can lead to a decrease in code size is cross-translation-unit dead code elimination, made possible by the global visibility of functions and variables and their uses in an executable. Without link-time information, non-`static` functions and variables are treated conservatively and kept around in the binary, in case of uses at link-time. With LTO, a final decision can be made and unused functions and variables eliminated.

#### Potential Code Size Increase

While the this global visibility of the code can often lead to a shrinking of the resulting binary, other choices deemed profitable by the compler can lead to an increase in code size. For example:

- Knowing a loop will execute `n` times in particular instances may lead to more loop unrolling than otherwise.
- Knowing a function regularly calls another (smaller) function may cause the compiler to inline the callee into the caller's body.

While all these decisions inherently lead to an increase in code size it is worth noting that while, just like inter-procedural constant propagation mentioned earlier, these transformations may be valid and beneficial in 90% of a function's use, we must retain compatibility with the remaining 10% of use cases.  In order for the compiler to optimize functions as per highly-recurrent use cases, it makes clones of the functions it wishes to transform such that the original function form is still present for use in less frequent cases. Where this is done, the resultant code duplication can further increase code size.
