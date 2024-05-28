---
title: About Eigen
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Eigen

Eigen is a very popular open source C++ template Linear Algebra library. It is designed to provide high-performance implementations of common mathematical operations that involve vectors, matrices and tensors.

It also provides a way to add custom implementations for related algorithms. It tries to be generic enough to cover almost every use case, but at the same time it also offers optimal performance on all the supported architectures.

Historically, [Eigen started off as a sub project of KDE by Benoît Jacob and Gael Guennebaud to help with common linear algebra operations for some KDE and KOffice projects](https://macresearch.org/interview-eigen-matrix-library/).

Because of a clever use of templates and partial template specialization in C++, Eigen has been able to provide almost the same high level algorithms on all architectures, by including implementations of basic primitive operations for all major SIMD engines.

Current implementations include:
* SSE/AVX/AVX2/AVX512 for Intel/AMD CPUs
* Neon/ASIMD, SVE for Arm CPUs
* Altivec/VSX for PowerPC/POWER CPUs
* Z Vector for IBM s390x CPUs
* MSA for MIPS CPUs

It has also been ported to SYCL and CUDA backends and more ports are in progress.

## Where is it used

Eigen is a very useful library and its usefulness is proven by the number of projects that are using it. 
[The list of projects that are using Eigen](https://eigen.tuxfamily.org/index.php?title=Main_Page#Projects_using_Eigen) is rich but here are a few high profile ones:

* [Tensorflow](https://www.tensorflow.org/) - An open source software library for Machine Intelligence
* [Celestia](https://celestiaproject.space/) - The 3D astronomical visualization application Celestia (all orbital and geometric calculations are done with Eigen)
* [ATLAS](https://home.cern/science/experiments/atlas) - The ATLAS experiment at the LHC (Large Hadron Collider) at CERN
* [Quantum++](https://github.com/softwareQinc/qpp) - A modern C++ general purpose quantum computing library

* [Robotic OS](https://www.ros.org/) - Robotic Operating System
* [MeshLab](https://www.meshlab.net/) - an opensource software for the processing and editing of unstructured 3D triangular meshes and point cloud
* [Topology Toolkit (TTK)](https://topology-tool-kit.github.io/) - an open-source library and software collection for topological data analysis in scientific visualization

KOffice:
* [Calligra](https://calligra.org/) - the spreadsheet module
* [Krita](https://krita.org/en/) - a professional free and open-source painting program

## Eigen Features

As mentioned, Eigen provides the fundamentals for almost all linear algebra operations, vectors and matrices to begin with, but also tensors, for usage in your C++ programs.
Eigen defines relevant classes and all the primitive operations that are possible with these objects, which you can use as building blocks for more complicated mathematical expressions.

Here are some basic classes:

### Matrix

First of all, the fundamental block of Linear Algebra is the Matrix.

Almost all operations involve at least one matrix and these matrices can be of 1D or 2D and of variable types.
The types in Eigen can be one of `int`, `float`, `double` or even `complex` numbers. Recently 16-bit integers support was also added if the hardware allows it.

The generic type is `Matrix`:

```C++
Matrix<typename Scalar, int RowsAtCompileTime, int ColsAtCompileTime>
```

Note the `AtCompileTime` suffix in the type definition. This type is for matrices with known dimensions at compile time. For dynamic-size matrices there is a different type: `MatrixX`.

But there are aliases that you can use for common cases, here are some examples:

```C++
typedef Matrix<float, 2, 2> Matrix2f;
typedef Matrix<int, 3, 3> Matrix3i;
typedef Matrix<double, 4, 4> Matrix4d;
typedef Matrix<std::complex<double>, 4, 4> Matrix4cd;
...
```

For a complete list check [here](https://libeigen.gitlab.io/docs/group__matrixtypedefs.html).

### Vector

As you might remember from your Math classes, a Vector can be defined as a one-dimensional matrix and in Eigen it is defined exactly as that:

```C++
typedef Matrix<float, 2, 1> Vector2f;
typedef Matrix<double, 3, 1> Vector3d;
typedef Matrix<int, 4, 1> Vector4i;
typedef Matrix<std::complex<float>, 4, 1> Vector4cf;
```

These are the *column* vectors, however, there are also types for *row* vectors, named accordingly:

```C++
typedef Matrix<float, 1, 2> RowVector2f;
typedef Matrix<double, 1, 3> RowVector3d;
typedef Matrix<int, 1, 4> RowVector4i;
typedef Matrix<std::complex<float>, 1, 4> RowVector4cf;
```

All basic mathematical operations and major known functions are defined on top of those classes.

There are more specialized classes for both storage types, like the `Tensor` class and operations, like FFT, Solvers, etc. in the `unsupported` folder.

In this Learning Path you are are going to test Eigen with a few examples with emphasis on Arm CPUs, but for full documentation and a list of all supported types and operations on them, you should read the [Eigen documentation](https://libeigen.gitlab.io/docs/).

## Numerical Solvers

Apart from basic vector and matrix types, Eigen also provides built-in methods for numerical solving on those matrices.

This Learning Path will not go into depth as to what exactly those solvers do, as that is beyond its scope, but rest assured that numerical solvers are actually very useful not only for a standpoint of Mathematics, but also actual applications that you are probably using in one way or the other, possibly without knowing it. Things like 3D, Video, Audio, Machine Learning/Deep Learning heavily use Linear Algebra and tools like Eigen are *extremely useful* because they provide the necessary fundamentals and with the necessary performance optimizations that would otherwise be too difficult to implement from the start.

Eigen provides many solvers, like LLT, LDLT, Partial and Full Pivot LU decompositions, etc. Check the [full list](https://libeigen.gitlab.io/docs/group__TopicLinearAlgebraDecompositions.html).

For example, doing LU decomposition of a 2D matrix, in Eigen it is as simple as

```C++
#include <iostream>

#include <Eigen/LU>    // provides LU decomposition
#include <Eigen/Dense> // provides random matrices

using namespace Eigen;

int main()
{
  MatrixXd A = MatrixXd::Random(5, 5);
  MatrixXd B = MatrixXd::Random(5, 3);
  MatrixXd X = A.lu().solve(B);
  std::cout << "A: " << std::endl << A << std::endl;
  std::cout << "B: " << std::endl << B << std::endl;
  std::cout << "X: " << std::endl << X << std::endl;
}
```

You will now compile and run the above file to see what it actually does.

Save the above file as `eigen-test1.cpp`.

Before you can compile it though, you need to either install `Eigen` using a package in your Linux distribution or clone it from a git repository.
Installing it from a distribution can be as simple as doing

```bash
$ apt install libeigen3-dev
```

on Debian based distributions, which will install the latest stable version in your distribution.
However, if you want to use the latest version you will probably have to use git:

```bash
$ git clone https://gitlab.com/libeigen/eigen
```

This will clone the project in a folder called `eigen` in your current directory. Assuming you will use this directory to save your test programs, you can compile the above program like this:

```bash
$ g++ -O3 -DNDEBUG eigen-test1.cpp -o eigen-test1 -I/usr/include/eigen3
```

if you are using a packaged installation, as Eigen is installed in the `/usr/include/eigen3`. In case you are using a git clone you need to replace that with `-Ieigen` in the compiler options above like this:

```bash
$ g++ -O3 -DNDEBUG eigen-test1.cpp -o eigen-test1 -Ieigen
```

And then you can run the example:

```bash
$ ./eigen-test1
A:
   0.696235    0.927654    0.432106   -0.498144   -0.216464
   0.205189    0.445064   -0.046008   -0.727247    0.852317
  -0.414795   -0.632501    0.134119    0.740165    0.834695
    0.33421   0.0241114   -0.159573   -0.756752   -0.833781
  -0.469531   0.0722581 -0.00985718    0.740565    -0.77815
B:
 -0.757623   0.858701  -0.553856
 -0.711254  -0.316277  -0.601805
 -0.467268   0.429178  -0.489601
0.00720412 -0.0105883  -0.481724
  0.220277   0.498262  0.0916964
X:
  3.99517  -3.03234   5.95177
 0.387929 -0.467882    1.0183
 -5.69195     5.487  -7.80526
   2.8392   -1.7979   4.30394
 0.116448 -0.634634  0.580386
 ```

This essentially solves the equation `A⋅X = B`.

Eigen is a powerful library but this is not a tutorial on Eigen, rather it's a very small introduction and demonstration of the performance gains you can get on Arm.
In the next section you will see more Eigen examples and in particular how they perform on Arm.
