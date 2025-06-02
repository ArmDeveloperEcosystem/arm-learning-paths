---
title: Eigen on Arm
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example 2: Matrix Multiplication

Use a text editor to save the program below in a file named `eigen-test3.cpp`:

```C++
#include <iostream>

#include <Eigen/Dense> // provides dense

#define N 100

using namespace Eigen;

int main()
{
  MatrixXd A = MatrixXd::Random(512, 512);
  MatrixXd B = MatrixXd::Random(512, 512);
  MatrixXd C = MatrixXd::Zero(512, 512);
  for (int i = 0; i < N; i++) {
    C += A * B;
  }
  std::cout << "C.norm(): " << C.norm() << std::endl;
}
```

This example performs `N` Matrix multiplications and additions. It uses the `FMA` instructions in most CPUs. It performs this operation on large 512 x 512 matrices and prints the `norm()` of the final matrix, which should be the same on both ASIMD and SVE versions.

As before, you can first compile and run with vectorization disabled to establish a reference level for performance.

```bash  { output_lines = "3-7" }
g++ -O3 -DNDEBUG -DEIGEN_DONT_VECTORIZE eigen-test3.cpp -o eigen-test3 -Ieigen
time ./eigen-test3
C.norm(): 384919

real    0m2.806s
user    0m2.794s
sys     0m0.012s
```

### Testing on ASIMD

Now, build with ASIMD backend, by removing the `-DEIGEN_DONT_VECTORIZE` option from the compiler invocation.

```bash  { output_lines = "3-7" }
g++ -O3 -DNDEBUG eigen-test3.cpp -o eigen-test3 -Ieigen
time ./eigen-test3
C.norm(): 384919

real    0m1.288s
user    0m1.280s
sys     0m0.008s
```

The results vary depending on the CPU and system you are using. 

The output above is from an SVE2 platform and shows 2.17x improvement in performance. An Ampere Altra CPU shows 3.55x performance improvement and 3.14x on Apple Silicon with an M3 CPU. There are many variables including the size of the caches, and the level of parallelism in the vector units - which equates to how many units are in the CPU and how many SIMD instructions can be executed in parallel.

### Testing on SVE

You can also compile and run with SVE enabled:

```bash  { output_lines = "3-7" }
g++ -O3 -DNDEBUG -march=armv8-a+sve -msve-vector-bits=128 -DEIGEN_ARM64_USE_SVE eigen-test3.cpp -o eigen-test3 -Ieigen
 time ./eigen-test3
C.norm(): 384919

real    0m1.751s
user    0m1.747s
sys     0m0.004s
```

You again see that the SVE build is slower than the ASIMD.

The SVE implementation is still experimental and performance is expected to improve in the future.

## Example 3: Vector 3D Rotation

This example creates an initial random normalized vector `v1`.

Then it creates `N` random normalized vectors, rotates them `π/4` around the `z` axis, adds them to the initial vector, and takes the dot product of the initial and the resulting vector.

Finally, it prints the sum of all the dot products.

Use a text editor to save the program below in a file named `eigen-test4.cpp`:

```C++
#include <iostream>

#include <Eigen/Dense> // provides dense

#define N 100000000

using namespace Eigen;

int main()
{
  Vector3f v1 = Vector3f::Random().normalized();
  std::cout << "Vector v1: " << std::endl;
  std::cout << v1 << std::endl;
  double sdp = 0.0;
  AngleAxisf aa = AngleAxisf(M_PI_4f, Vector3f::UnitZ());
  Quaternionf q{aa.toRotationMatrix()};
  for (int i=0; i < N; i++) {
    Vector3f v2 = Vector3f::Random().normalized();
    sdp += v1.dot(v1 + q * v2);
  }
  std::cout << "Sum of Dot Products: " << sdp << std::endl;
}
```

Use the same process to build and run without vectorization:

```bash  { output_lines = "3-11" }
g++ -O3 -DNDEBUG -DEIGEN_DONT_VECTORIZE eigen-test4.cpp -o eigen-test4 -Ieigen
time ./eigen-test4
Vector v1:
 -0.664879
  0.745716
-0.0429305
Sum of Dot Products: 9.99953e+07

real    0m5.957s
user    0m5.957s
sys     0m0.000s
```

### Testing on ASIMD

As before, remove the `-DEIGEN_DONT_VECTORIZE` from the compile command:

```bash  { output_lines = "3-11" }
g++ -O3 -DNDEBUG eigen-test4.cpp -o eigen-test4 -I../eigen
time ./eigen-test4
Vector v1:
 -0.664879
  0.745716
-0.0429305
Sum of Dot Products: 9.99953e+07

real    0m5.636s
user    0m5.636s
sys     0m0.000s
```

This is interesting; enabling vectorization doesn't improve performance, which can be due to multiple reasons.

[Optimize SIMD code with vectorization-friendly data layout](/learning-paths/cross-platform/vectorization-friendly-data-layout/a-more-complex-problem-revisited/) explains that performance on operations involving data like 3D coordinates might benefit from changing the way data is structured.

One thing to mention is that with the `-O3` flag, autovectorization is enabled by default in recent GCC and Clang compilers, so even if you disable explicit vectorization in Eigen, the compiler still tries to attempt to vectorize the code. 

In the time period that Eigen was developed, autovectorization was completely out of the question and was almost unreachable in all but the most trivial cases. However, the recent compilers are more advanced and prove to be even better in some cases, such as this one, where the type of object is not optimally designed for vectorization.

### Testing on SVE

Compile and run the example with SVE:

```bash  { output_lines = "3-11" }
g++ -O3 -DNDEBUG -march=armv9-a -msve-vector-bits=128 -DEIGEN_ARM64_USE_SVE eigen-test4.cpp -o eigen-test4 -Ieigen
 time ./eigen-test4
Vector v1:
 -0.664879
  0.745716
-0.0429305
Sum of Dot Products: 9.99953e+07

real    0m5.718s
user    0m5.718s
sys     0m0.000s
```

Interestingly, SVE performs about the same as the other versions.

You are now ready to build one of the high profile applications that use Eigen with SVE enabled. This application is TensorFlow!
