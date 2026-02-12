---
title: About Eigen
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Eigen?

Eigen is a popular, open source C++ template linear algebra library. It provides high-performance implementations of common mathematical operations that involve vectors, matrices, and tensors.

It also provides a way to add custom implementations for related algorithms. It is generic enough to cover almost every use case, but at the same time offers optimal performance on all supported architectures.

Eigen began as a sub-project of KDE by Benoît Jacob and Gael Guennebaud, to help with common linear algebra operations for some KDE and KOffice projects. To learn more about this, you can read [Interview: Eigen Matrix Library](https://macresearch.org/interview-eigen-matrix-library/). 

Through a clever application of templates and partial template specialization in C++, Eigen has been able to provide almost the same high level algorithms on all architectures, by including implementations of basic primitive operations for all major SIMD engines.

Current implementations include:

* SSE/AVX/AVX2/AVX512 for Intel/AMD CPUs.
* Neon/ASIMD, SVE for Arm CPUs.
* Altivec/VSX for PowerPC/POWER CPUs.
* Z Vector for IBM s390x CPUs.
* MSA for MIPS CPUs.

It has also been ported to SYCL and CUDA backends and further ports are in progress.

## Where is Eigen used?

Eigen is a useful library and its success is proven by the number of projects that use it. 
[The list of projects using Eigen](https://libeigen.gitlab.io/#projects-using-eigen) is rich, but here are a few high profile projects:

* [TensorFlow](https://www.tensorflow.org/) - an open source software library for Machine Intelligence.
* [Celestia](https://celestiaproject.space/) - the 3D astronomical visualization application Celestia (all orbital and geometric calculations are done with Eigen).
* [ATLAS](https://home.cern/science/experiments/atlas) - the ATLAS experiment at the LHC (Large Hadron Collider) at CERN.
* [Quantum++](https://github.com/softwareQinc/qpp) - a modern C++ general purpose quantum computing library.

* [Robotic OS](https://www.ros.org/) - Robotic Operating System.
* [MeshLab](https://www.meshlab.net/) - an open source software project for processing and editing unstructured 3D triangular meshes and point cloud.
* [Topology Toolkit (TTK)](https://topology-tool-kit.github.io/) - an open source library and software collection for topological data analysis in scientific visualization.

KOffice:
* [Calligra](https://calligra.org/) - the spreadsheet module.
* [Krita](https://krita.org/en/) - a professional free and open source painting program.

## What are the features of Eigen?

Eigen provides the fundamentals for almost all linear algebra operations, vectors, and matrices, but also tensors, for use in your C++ programs.

Eigen defines relevant classes and all the primitive operations possible with these objects, that you can use as building blocks for more complicated mathematical expressions.

Here are some basic classes:

### Matrix

The fundamental block of linear algebra is the Matrix.

Almost all operations involve at least one matrix and these matrices can be of 1D, 2D, or of variable types.
The types in Eigen can be `int`, `float`, `double`, or `complex` numbers. Recently, 16-bit integer support was added, and can be used if the hardware allows it.

The generic type is `Matrix`:

```C++
Matrix<typename Scalar, int RowsAtCompileTime, int ColsAtCompileTime>
```

Note the `AtCompileTime` suffix in the type definition. This type is for matrices with known dimensions at compile time. For dynamic-size matrices there is a different type: `MatrixX`.

There are aliases that you can use for common cases. Here are some examples:

```C++
typedef Matrix<float, 2, 2> Matrix2f;
typedef Matrix<int, 3, 3> Matrix3i;
typedef Matrix<double, 4, 4> Matrix4d;
typedef Matrix<std::complex<double>, 4, 4> Matrix4cd;
```

For a complete list, refer to [Global matrix typedefs](https://libeigen.gitlab.io/docs/group__matrixtypedefs.html).

### Vector

A vector can be defined as a one-dimensional matrix and in Eigen it is defined as exactly that:

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

All basic mathematical operations and major known functions are defined on top of these classes.

There are more specialized classes for both storage types, like the `Tensor` class and operations, like FFT and Solvers, in the `unsupported` folder.

In this Learning Path, you will test Eigen using a few examples with emphasis on Arm CPUs. For full documentation and a list of all supported types and operations on them, see the [Eigen documentation](https://libeigen.gitlab.io/docs/).

## Numerical Solvers

Besides basic vector and matrix types, Eigen also provides built-in methods for numerical solving on the matrices.

This Learning Path does not go into depth on what the solvers do, but the numerical solvers are useful not only from the standpoint of Mathematics, but also as applications that you are likely using in one way or the other, possibly without knowing. 

Areas such as 3D, Video, Audio, and Machine Learning/Deep Learning heavily use linear algebra and tools like Eigen are *extremely useful* because they provide the necessary fundamentals with the necessary performance optimizations that would otherwise be too difficult to implement.

Eigen provides many solvers such as LLT, LDLT, Partial, and Full Pivot LU decompositions. For the complete list, check [Catalogue of dense decompositions](https://libeigen.gitlab.io/docs/group__TopicLinearAlgebraDecompositions.html).

For example, LU decomposition of a 2D matrix can be done with Eigen. 

Use a text editor to save the code below in a file named `eigen-test1.cpp`:

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

You can now compile and run the above code to see what it does.

Before you can compile it, you need to install `Eigen` using either a Linux package manager or clone the source code from the Git repository.

For Debian-based distributions, you can install Eigen by running:

```bash
sudo apt install libeigen3-dev -y
```

Package managers install the latest *stable* version for your Linux distribution, but if you want to use the very latest version you can use Git:

```bash
git clone https://gitlab.com/libeigen/eigen
```

This will clone the project in a folder called `eigen` in your current directory. 

If you installed Eigen with a package manager, you can compile the above program like this:

```bash
g++ -O3 -DNDEBUG eigen-test1.cpp -o eigen-test1 -I/usr/include/eigen3
```

If you installed Eigen using Git, you can compile the above program like this:

```bash
g++ -O3 -DNDEBUG eigen-test1.cpp -o eigen-test1 -Ieigen
```

Regardless of how you installed Eigen, you can run the example: 

```bash
./eigen-test1
```

The expected output is:

```output
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

This solves the equation `A⋅X = B`.

Eigen is a powerful library, but this is not a tutorial on Eigen, it's an introduction and demonstration of the performance gains you can get on Arm.

In the next section you will see more Eigen examples and in particular how they perform on Arm.
