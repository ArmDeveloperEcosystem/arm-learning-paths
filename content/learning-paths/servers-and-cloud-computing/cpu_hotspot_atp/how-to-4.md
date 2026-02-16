---
title: Optimize
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now we can leverage the insights surfaced by ATP to focus the optimizations around the hottest functions. Looking at the source code, we understand the the hypotenuse function, `__hypot`, is being invoked to calculate the absolute value of a complex number. 

We can also see that the number of iterations is of the absolute value is limited by the loop boundary, MAX_ITERATIONS. Our first optimization could be to reduce MAX_ITERATIONS. This is defined as 1024 a static const integer in the `Mandelbrot.h` header. We could half this to 512 and assess the perceived image quality on our fractal.

```cpp
public:
...
    static const int MAX_ITERATIONS = (1<<10);
...

```



Looking at the change in image quality, there is neglible difference.

![comparison](./comparison.jpg)

## Running hottest function on many cores

Fortunately, our loop does not contain any loop-carried dependencies, where the result of an iterations depends on a future or previous iteration. As such we can parallelize our hot function to fun on multiple threads if our CPU has multiple cores. 

The repository contains a parallel version in the main branch. 

```bash
git checkout main
```

This branch parallelized the `Mandelbrot::draw` function, which is earlier function in the stack that eventually calls the `__hypot` function. 

Build the example and run with 16 threads.

```bash
./build.sh
./builds/mandelbrot-parallel 16
```

To assess the change, we can compare with a previous run. Looking under the `Run Details` tab, we can see the execution time has reduced from 58s with 1 thread to 9s with 16 threads.

![exec-change](./comparison-time.jpg)

The percentage point of samples has not changed significantly, but we see with 64 threads the % of sampling landing on the `Mandelbrot::draw` function has reduced by 7%. This suggests that if we want to further improve the execution time, further optimizations on the `Mandelbrot::draw` function will yield the greatest benefit. 

![flame-graph-comparison](./flame-graph-comparison.jpg)


## Summary

