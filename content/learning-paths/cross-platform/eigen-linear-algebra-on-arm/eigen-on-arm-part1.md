---
title: Eigen examples
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You have learned that Eigen has been ported to Neon/ASIMD in the past and recently to SVE. Now you are going to investigate how to use Eigen to get best performance on Arm systems with SIMD engines.

## Example 1: Arbitrary-Size Matrix Sum of all Elements

This example demonstrates the benefits of Eigen's vectorization with some simple expressions on matrices. It first constructs a large random matrix of 100 x 100 `float` elements, and performs some simple operation for `N` iterations on it. Finally, it returns the sum of all the elements of the final matrix as a `double`.

Use a text editor to save the program below in a file named `eigen-test2.cpp`:

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


Before you try it with SIMD enabled, first try it without.

To do that, you need to pass a define to the compiler to instruct Eigen to disable vectorization: `-DEIGEN_DONT_VECTORIZE`.

Compile the program using:

```bash
g++ -O3 -DNDEBUG -DEIGEN_DONT_VECTORIZE eigen-test2.cpp -o eigen-test2 -Ieigen
```

Run the test with `time`. Your results might vary depending on your CPU and system:

{{% notice Note %}}
Only the commands are copied from the box below if you use the Copy button. The remainder is the output and is not copied.
{{% /notice %}}

```bash  { output_lines = "2-6" }
time ./eigen-test2
Final matrix sum: -1.13038e+12

real    0m22.872s
user    0m22.872s
sys     0m0.000s
```

### Testing on ASIMD

To compare with the SIMD (ASIMD/NEON in the case of Arm), remove the define from compilation and run the same way:


```bash  { output_lines = "3-7" }
g++ -O3 -DNDEBUG eigen-test2.cpp -o eigen-test2 -Ieigen
time ./eigen-test2
Final matrix sum: -1.13038e+12

real    0m4.933s
user    0m4.933s
sys     0m0.000s
```

This is a speed up of 4.63x, which is impressive! Next, try with SVE enabled to see if there is any difference.

### Testing on SVE

Those tests were run on the same SVE-capable system so you should be able to make a comparison.
Eigen currently needs a few extra options passed to the compiler:

```bash
g++ -O3 -DNDEBUG -march=armv8-a+sve -msve-vector-bits=<SVESIZE>> -DEIGEN_ARM64_USE_SVE eigen-test2.cpp -o eigen-test2 -Ieigen
```

Eigen needs `-DEIGEN_ARM64_USE_SVE` to be passed to enable the code that is specific for SVE.

The compiler needs `-march=armv8-a+sve` to produce assembly code for SVE-capable systems. You might replace that with `-march=armv9-a` on SVE2 systems.

Finally, Eigen currently does not support runtime detection of SVE vector widths, which depends on the particular CPU, so you need to pass the option `-msve-vector-bits=<SVESIZE>` to force the compiler to assume a particular SVE hardware vector size.

This particular CPU has 128-bits SVE vector size, so replacing `SVESIZE` above with 128 and compiling you should be able to run the test:

Now run the test:

```bash  { output_lines = "2-6" }
time ./eigen-test2
Final matrix sum: -1.13038e+12

real    0m5.366s
user    0m5.362s
sys     0m0.004s
```

It's not as good as ASIMD but it's close. You have to remember that SVE optimizations in many projects are still early and performance will continue to improve over time. This is why Eigen does not have the SVE backend enabled by default. You should expect the performance to improve in the future, especially when used in conjunction with existing ASIMD instructions.

Before you move to the next example, you can check what happens if you try a different SVE vector width, 256. Would the program crash? If you recompile the test with `SVESIZE=256` and rerun on the same 128-bit SVE system, this is the result:

```bash  { output_lines = "2-6" }
time ./eigen-test2
Final matrix sum: 0

real    0m11.647s
user    0m11.647s
sys     0m0.000s
```

This is interesting. First, you will note that the result is wrong (zero), and it takes almost double the time to calculate. This is something to keep in mind in general when forcing the SVE vector width at compile time. The instructions are the same, so you will not get an Illegal Instruction exception (`SIGILL`), but there is going to be UB (Undefined Behavior) if the program is not designed to cope for such cases. 

In general, you should avoid forcing a vector size for SVE, unless there is no alternative.

Mathematical operations benefit from processors with larger SVE vector sizes, such as 256 bits, 512 bits or even more. The Fujitsu A64FX super computer has SVE vectors of 512-bits, and will be much faster for these calculations.

In the next section you can try another example.
