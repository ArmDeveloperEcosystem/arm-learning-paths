---
title: Eigen on Arm, part1
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You have already read that Eigen has been ported to Neon/ASIMD in the past and recently to SVE. We are going to investigate how we can use Eigen to get best performance on Arm systems with those SIMD engines.

## Example 1, Arbitrary-size Matrix sum of all elements

This is a small example, in order to demonstrate the benefits of Eigen's vectorization with some simple expressions on matrices. It will first construct a large random matrix of 100 x 100 `float` elements and it will perform some simple operation for `N` iterations on it. In the end it will return the sum of all the elements of the final matrix as a `double`.

```C++
#include <iostream>

#include <Eigen/Dense> // provides dense

#define N 100000

using namespace Eigen;

int main()
{
  double final_sum = 0.0;
  MatrixXf m = MatrixXf::Random(100, 100);
  MatrixXf i2 = MatrixXf::Identity(100, 100);
  for (int i = 0; i < N; i++) {
    final_sum += (m * i2 * N).sum();
  }
  std::cout << "Final matrix sum: " << final_sum << std::endl;
}
```

Save this program as `eigen-test2.cpp` and compile it. But before you try the actual performance with SIMD enabled, let's first try without it.

To do that, you need to pass a definition to the compiler to instruct Eigen to disable vectorization, `-DEIGEN_DONT_VECTORIZE`:

```bash
$ g++ -O3 -DEIGEN_DONT_VECTORIZE eigen-test2.cpp -o eigen-test2 -Ieigen
```

and run the test with `time` (your results may vary depending on your CPU):

```bash
$ time ./eigen-test2
Final matrix sum: -1.13038e+12

real    0m22.872s
user    0m22.872s
sys     0m0.000s
```

### Testing on ASIMD

To compare with the SIMD (ASIMD/NEON in the case of Arm), just remove that define from compilation and run the same way:

```bash
$ g++ -O3 eigen-test2.cpp -o eigen-test2 -Ieigen
$ time ./eigen-test2
Final matrix sum: -1.13038e+12

real    0m4.933s
user    0m4.933s
sys     0m0.000s
```

That is a speed up of 4.63x, which is quite impressive! Let's try with SVE enabled to see if there is any difference.

### Testing on SVE

Those tests were run on the same SVE-capable system so you should be able to make a comparison.
Eigen currently needs a few extra options passed to the compiler:

```bash
$ g++ -O3 -march=armv8-a+sve -msve-vector-bits=<SVESIZE>> -DEIGEN_ARM64_USE_SVE eigen-test2.cpp -o eigen-test2 -Ieigen
```

Eigen needs `-DEIGEN_ARM64_USE_SVE` to be passed to enable the code that is specific for SVE.

The compiler needs `-march=armv8-a+sve` to produce assembly code for SVE-capable systems. You might replace that with `-march=armv9-a` on SVE2 systems.

Finally, Eigen currently does not support runtime detection of SVE vector widths, which depends on the particular CPU, so you need to pass the option `-msve-vector-bits=<SVESIZE>` to force the compiler to assume a particular SVE hardware vector size.

Now run the test:

This particular CPU has 128-bits SVE vector size, so replacing `SVESIZE` above with 128 and compiling you should be able to run the test:

```bash
 time ./eigen-test2
Final matrix sum: -1.13038e+12

real    0m5.366s
user    0m5.362s
sys     0m0.004s
```

It's not as good as ASIMD but it's quite close. You have to remember that SVE optimizations in many projects are quite early and there is a reason that Eigen does not have the SVE backend enabled by default on such CPUs. You should expect the performance to improve drastically, especially when used in conjunction with existing ASIMD instructions.

Before you see the next example, let's check what would happen if we test a different SVE vector width, eg 256, would the program crash? If you recompile the test with `SVESIZE=256` and rerun on the same 128-bit SVE system, this is what you will get:

```bash
$ time ./eigen-test2
Final matrix sum: 0

real    0m11.647s
user    0m11.647s
sys     0m0.000s
```

This is interesting. First, you will obviously note that the result is wrong (zero), and it takes almost double the time to calculate. This is something to keep in mind in general when forcing the SVE vector width at compile time. The instructions are the same, so you will not get an Illegal Instruction exception (`SIGILL`) but there is going to be UB (Undefined Behaviour) if the program is not designed to cope for such cases -which our little test does not.

In general, you should avoid forcing a vector size for SVE, unless there is no alternative.

You should note here, that such mathematical operations totally benefit from actual larger SVE vector sizes, eg. 256, 512-bits or even more, such as the ones on the Fujitsu A64FX super computers, which have SVE vectors of 512-bits.

Let's try another example.
