---
# User change
title: "Compile for SVE"
weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## GNU

### C

```bash
gcc -march=armv8-a+sve myapp.c -o myapp_c.out
```

### Fortran

```bash
gfortran -march=armv8-a+sve myapp.f90 -o myapp_f90.out
```

### Autovectorization

With GCC autovectorization is enabled with the `-03` option. To disable autovectorization, use `-fno-tree-vectorize`.

Compare the output with autovectorization (left) and without (right):

{{< godbolt width="100%" height="400px" mode="diff" lopt="-O3 -march=armv8-a -fno-tree-vectorize" ropt="-O3 -march=armv8-a+sve" src="int fun(double * restrict a, double * restrict b, int size)\n{\n  for (int i=0; i < size; ++i)\n  {\n    b[i] += a[i];\n  }\n}" >}}

Note the use of double-word register _d0_, _d1_ when disabling vectorization instead of SVE registers _z0.d_ and _z1_.

### Compiler insights

With GCC, the option `-fopt-info-vec` returns what loops were vectorized. To return what loop failed to vectorize, use `-fopt-info-vec-missed`.

{{< godbolt width="100%" height="400px" mode="output" opt="-O3 -march=armv8-a+sve -fopt-info-vec" src="int fun(double * restrict a, double * restrict b, int size)\n{\n  for (int i=0; i < size; ++i)\n  {\n    b[i] += a[i];\n  }\n}" >}}

Note that the compiler reports the vectorization of the loop line 3.

### Use Arm Performance Libraries

The Arm Performance Libraries include generic and target-specific SVE optimizations of common math operations used in HPC. To link your application with the libraries and GCC, use the predefined environment variables ARMPL_INCLUDES and ARMPL_LIBRARIES set by the Arm Performance Libraries module files provided:

```bash
gcc -O3 -march=armv8-a+sve -I $ARMPL_INCLUDES dgemm.c -o dgemm.out -L $ARMPL_LIBRARIES -larmpl
```

## Arm Compiler for Linux

### C

```bash
armclang -march=armv8-a+sve myapp.c -o myapp_c.out
```

### Fortran

```bash
armflang -march=armv8-a+sve myapp.f90 -o myapp_f90.out
```

### Compiling for a specific SVE target with Arm Compiler for Linux

When compiling on the SVE-capable target, you can use `-march=native`. Otherwise, the following options are also available:

```console
-mcpu=neoverse-v1
-mcpu=neoverse-n2
-mcpu=a64fx
```

### Autovectorization

With Arm Compiler for Linux autovectorization is enabled with the `-02` option and above. To disable autovectorization, use `-fno-vectorize`.

### Compiler insights

With Arm Compiler for Linux, the option `-Rpass=vector` and `-Rpass=sve-loop-vectorize` return what loops were vectorized. To return what loop failed to vectorize, use `-Rpass-missed=vector`.

### Use Arm Performance Libraries

Using the Arm Performance Libraries with Arm Compiler for Linux is straightforward: the flag `-armpl=sve` ensures the SVE version of the library is used.

```bash
armclang -O3 -march=armv8-a+sve -armpl=sve dgemm.c -o dgemm.out
```
