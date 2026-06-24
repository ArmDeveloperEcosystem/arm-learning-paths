---
# User change
title: "Compile for SVE"
weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Compiling for SVE with GNU

Below are example commands to compile an application with support for SVE instructions using the GNU Toolchain:

### C 

For GCC, use the following command:

```bash
gcc -march=armv8-a+sve myapp.c -o myapp_c.out
```

### Fortran

For Fortran, use the following command:

```bash
gfortran -march=armv8-a+sve myapp.f90 -o myapp_f90.out
```

### Autovectorization

With GCC autovectorization is fully enabled with high-level `-03` option or manually with the `-ftree-vectorize` flag. To disable autovectorization, use `-fno-tree-vectorize` compiler option.

Compare the disassembly of a simple program shown below with and without the use of autovectorization:

{{< godbolt width="100%" height="400px" mode="diff" lopt="-O3 -march=armv8-a -fno-tree-vectorize" ropt="-O3 -march=armv8-a+sve" src="int fun(double * restrict a, double * restrict b, int size)\n{\n  for (int i=0; i < size; ++i)\n  {\n    b[i] += a[i];\n  }\n}" >}}

Note the use of double-word register `d0`, `d1` instead of SVE registers `z0.d` and `z1` when you disable vectorization.

{{% notice Autovectorization on the Arm AGI CPU %}}

If specifically targeting the 1st generation Arm AGI CPU, the `-mcpu=armagicpu` defintion was added in [GCC 16.1.0](https://github.com/gcc-mirror/gcc/commit/0f5f728854d2ea93e6806a8632c04383502b0386). As of May 2026, this is the same as the `-march=neoverse-v3ae` option available from [GCC 15](https://gcc.gnu.org/gcc-15/changes.html) onwards. However, in the future there may be differences between `neoverse-v3ae` and `armagicpu`.

As such, we recommend installing the latest version of GCC/G++ if you are targeting the Arm AGI CPU. Use the `-mcpu=native` flag if compiling on the target machine or `-mcpu=armagicpu` if cross compiling. 

{{% /notice %}}

### Compiler insights

With GCC, the use of compiler option `-fopt-info-vec` returns which loops were vectorized. To return which loop failed to vectorize, use the `-fopt-info-vec-missed` compiler option.

{{< godbolt width="100%" height="400px" mode="output" opt="-O3 -march=armv8-a+sve -fopt-info-vec" src="int fun(double * restrict a, double * restrict b, int size)\n{\n  for (int i=0; i < size; ++i)\n  {\n    b[i] += a[i];\n  }\n}" >}}

In this example, the compiler reports the vectorization of loop line 3.

### Use Arm Performance Libraries

The Arm Performance Libraries include generic and target-specific SVE optimizations of common math operations used in HPC. To link your application with these libraries and GCC, use the predefined environment variables `ARMPL_INCLUDES` and `ARMPL_LIBRARIES`. The environment variables are set by the Arm Performance Libraries module files.

Refer to the [Arm Performance Libraries install guide](/install-guides/armpl/) for more information.

```bash
gcc -O3 -march=armv8-a+sve -I $ARMPL_INCLUDES dgemm.c -o dgemm.out -L $ARMPL_LIBRARIES -larmpl
```

## Compiling for SVE with Arm toolchain for Linux (ATfL)

Shown below are example commands to compile an application with support for SVE instructions using Arm toolchain for Linux:

### Arm C/C++ Compiler

```bash
armclang -march=armv8-a+sve myapp.c -o myapp_c.out
```

### Arm Fortran Compiler

```bash
armflang -march=armv8-a+sve myapp.f90 -o myapp_f90.out
```

### Compiling for a specific SVE target with Arm Toolchain for Linux 

If you are compiling for a SVE-capable target, you can use the `-march=native` compiler option. To target specific CPUs with SVE support, use the `-mcpu` option:

CPU       | Flag    
----------|---------
Neoverse-N1 | `-mcpu=neoverse-n1` 
Neoverse-V1 | `-mcpu=neoverse-v1`
Neoverse-V2 | `-mcpu=neoverse-v2`
Neoverse-V3 | `-mcpu=neoverse-v3`
Arm AGI CPU (first generation)* | `-mcpu=neoverse-v3ae` (as of ATfL 22.1.0)

{{% notice Please Note %}}

Support for the 1st generation Arm AGI CPU, based on the Neoverse V3-AE core, is expected to be added in LLVM version 23. Once available, ATfL is expected to support this target through the dedicated compiler option `-mcpu=armagicpu`.

If you are targeting the Arm AGI CPU, we recommend using the latest available version of ATfL to ensure support for the most recent compiler optimizations and features.

{{% /notice %}}

### Autovectorization

With Arm toolchain for Linux autovectorization is enabled with the `-02` option and above. To disable autovectorization, use `-fno-vectorize`.

### Compiler insights

With Arm toolchain for Linux, the option `-Rpass=vector` and `-Rpass=sve-loop-vectorize` return which loops were vectorized. To return the loops that failed to vectorize, use `-Rpass-missed=vector`.

### Use Arm Performance Libraries

To use Arm Performance Libraries with Arm toolchain for Linux use the `-armpl=sve` option. This ensures the SVE version of the library is used. Example command shown here:

```bash
armclang -O3 -march=armv8-a+sve -armpl=sve dgemm.c -o dgemm.out
```
