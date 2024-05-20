---
title: Eigen on Arm, part2
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example 2, matrix multiplication

Consider this program:

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

This example does `N` Matrix multiplications and additions -so that it will utilize the `FMA` instructions in most CPUs. It will perform this operations on large 512 x 512 matrices and it will print the `norm()` of the final matrix -which should be the same on both ASIMD and SVE versions.

Save this file as `eigen-test3.cpp`. Again, let's first compile and run with vectorization disabled to establish a reference level for performance.

```bash
$ g++ -O3 -DEIGEN_DONT_VECTORIZE eigen-test3.cpp -o eigen-test3 -Ieigen
$ time ./eigen-test3
C.norm(): 384919

real    0m2.806s
user    0m2.794s
sys     0m0.012s
```

### Testing on ASIMD

Now, let's build with ASIMD backend, as before, just remove the `-DEIGEN_DONT_VECTORIZE` option from the compiler invocation.

```bash
$ g++ -O3 eigen-test3.cpp -o eigen-test3 -Ieigen
$ time ./eigen-test3
C.norm(): 384919

real    0m1.288s
user    0m1.280s
sys     0m0.008s
```

The result depends largely on the platform tested.

On this SVE2 platform we got 2.17x improvement in performance, on an Ampere Altra CPU we got 3.55x performance improvement and 3.14x on an Apple M3 CPU. It depends on the size of the caches, the level of parallelism in the Vector Units (how many units in the CPU and how many SIMD instructions can be executed in parallel).

### Testing on SVE

You will now compile and run with SVE enabled:

```bash
$ g++ -O3 -march=armv8-a+sve -msve-vector-bits=128 -DEIGEN_ARM64_USE_SVE eigen-test3.cpp -o eigen-test3 -Ieigen
$ time ./eigen-test3
C.norm(): 384919

real    0m1.751s
user    0m1.747s
sys     0m0.004s
```

You again see that the SVE build is slower than the ASIMD.

We will note that SVE implementation is still experimental and this is expected to change.

## Example 3, Vector 3D Rotation

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

This example creates an initial random normalized vector `v1`.

Then it creates `N` random normalized vectors, rotates them `π/4` around the `z` axis, adds them to the initial vector and takes the dot product of the initial and the resulting vector.

Finally it prints the sum of all the dot products.

Now, save this file as `eigen-test4.cpp`. Similarly, we built first without vectorization and run the binary:

```bash
$ g++ -O3 -DEIGEN_DONT_VECTORIZE eigen-test4.cpp -o eigen-test4 -Ieigen
$ time ./eigen-test4
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

As before, just remove the `-DEIGEN_DONT_VECTORIZE` from the command line.

```bash
$ g++ -O3 eigen-test4.cpp -o eigen-test4 -I../eigen
$ time ./eigen-test4
Vector v1:
 -0.664879
  0.745716
-0.0429305
Sum of Dot Products: 9.99953e+07

real    0m5.636s
user    0m5.636s
sys     0m0.000s
```

This is interesting, enabling vectorization doesn't give us actually that much better performance as we expected, which can be due to multiple reasons.

In the [Vectorization-Friendly Data Layout Learning Path](https://learn.arm.com/learning-paths/cross-platform/vectorization-friendly-data-layout/a-more-complex-problem-revisited/) it was explained that performance on operations involving data like 3D coordinates may be benefitted from changing the way this data is structured.

One thing that should be also mentioned is that with `-O3` flag, autovectorization is enabled by default in recent GCC and Clang compilers, so even if you disable explicit vectorization in Eigen, the compiler will still try to attempt to vectorize the code. In the period that Eigen was developed, that was completely out of the question and autovectorization was almost unreachable in all but the most trivial cases. However, the recent compilers are much more advanced and they can prove to be even better in some cases like this one where the type of object is not optimally designed for vectorization, as you have already seen in the *Vectorization-Friendly Data Layout Learning Path*.

### Testing on SVE

```bash
$ g++ -O3 -march=armv9-a -msve-vector-bits=128 -DEIGEN_ARM64_USE_SVE eigen-test4.cpp -o eigen-test4 -Ieigen
$ time ./eigen-test4
Vector v1:
 -0.664879
  0.745716
-0.0429305
Sum of Dot Products: 9.99953e+07

real    0m5.718s
user    0m5.718s
sys     0m0.000s
```

Interestingly, SVE performs very similarly to the other versions.

You are now ready to build one of the high profile applications that use Eigen with SVE enabled. This application will be Tensorflow!

Proceed to the next section to learn how to do this.
