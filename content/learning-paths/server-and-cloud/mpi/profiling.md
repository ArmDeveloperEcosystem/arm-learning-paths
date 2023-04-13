---
# User change
title: "Optimize your code"
weight: 4 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Build options for profiling

Edit the file in `src/make.def` and make sure the code is compiled with debugging symbols `-g`, e.g.:

```makefile
CFLAGS = -O0 -g
```

Note that `-O0` disables compiler optimizations.

## Build

Select your version C/Fortran/Python of the application in `src`, then build the application with:

```bash {  command_line="user@localhost" }
make
```

## Run and profile your application

Install the Linux perf tools, e.g. on Ubuntu:

```bash {  command_line="user@localhost" }
sudo apt-get install linux-tools-common linux-tools-generic linux-tools-`uname -r`
```

and profile with:

```bash {  command_line="user@localhost" }
perf stat mpirun ./mmult 1024
```

This will provide information on a few hardware counter events as well as the elapsed time. First, we are going to investigate the amount of cycles per instruction. If low (less than 1), this indicates inefficiency.

### Use a parallel profiler

In the same folder previously selected, run the C/Fortran application in parallel with [Linaro MAP](/install-guides/forge/) :

```bash {  command_line="user@localhost" }
map mpirun ./mmult 1024
```

or using Python

```bash {  command_line="user@localhost" }
map mpirun python ./mmult.py -s 1024
```

This command will launch a GUI, and profiling result will be displayed as a timeline and annotated code.

## Enable compiler optimizations

Edit the file in `src/make.def` to turn compiler optimizations on and report on vectorized loops: 

{{< tabpane >}}
  {{< tab header="GNU" >}}
  CFLAGS = -Ofast -g -fopt-info-vec
  {{< /tab >}}
  {{< tab header="Arm Compiler for Linux" >}}
  CFLAGS = -Ofast -g -Rpass=vector
  {{< /tab >}}
{{% /tabpane %}}


Then, rebuild the application before profiling again:

```bash {  command_line="user@localhost" }
make clean && make
```

## Investigate cache misses

To go further, we can specify hardware counter events to collect. For example, we can investigate memory access issues with:

```bash {  command_line="user@localhost" }
perf stat -e cache-misses,cache-references mpirun ./mmult 1024
```

If this ratio is high, memory access may be suboptimal. We can annotate the code where cache misses happen with the following perf commands:

```bash {  command_line="user@localhost" }
perf record -e cache-misses mpirun ./mmult 1024
perf report
```

## Optimize memory accesses

This patch will help the application benefit from the CPU caches:

```patch
--- ./src/C/mmult.c
+++ ./src/C/mmult.c
@@ -64,7 +64,7 @@
 
       for(int k=0; k<sz; k++)
       {
-        res += A[i*sz+k]*B[k*sz*j];
+        res += A[i*sz+k]*B[k*sz+j];
       }
 
       C[i*sz+j] += res;


--- ./src/F90/mmult.F90
+++ ./src/F90/mmult.F90
@@ -174,7 +174,7 @@
       do j=1,sz
         res=0.0
         do k=1,sz
-         res=A(k,i)*B(j,k+res)
+         res=A(k,i)*B(j,k)+res
         end do
         C(j,i)=res+C(j,i)
       end do


--- ./src/make.def
+++ ./src/make.def
@@ -18,6 +18,6 @@
 FC = mpif90

 # Define additional compilation flags
-CFLAGS =
+CFLAGS = -O0 -g
 LFLAGS =


--- ./src/Py/F90/mmult.F90
+++ ./src/Py/F90/mmult.F90
@@ -30,7 +30,7 @@
       do j=1,sz
         res=0.0
         do k=1,sz
-         res=A(k,i)*B(j,k+res)
+         res=A(k,i)*B(j,k)+res
         end do
         C(j,i)=res+C(j,i)
       end do


--- ./src/Py/C/mmult.c
+++ ./src/Py/C/mmult.c
@@ -29,7 +29,7 @@

       for(int k=0; k<sz; k++)
       {
-        res += A[i*sz+k]*B[k*sz*j];
+        res += A[i*sz+k]*B[k*sz+j];
       }

       C[i*sz+j] += res;
```

## Use optimized routines

Install BLAS libraries, e.g. on Ubuntu:

```bash {  command_line="user@localhost" }
sudo apt-get install libblas-dev
```

And apply this patch to use the optimized routine instead of the hand-written matrix multiplication.

```patch
--- ./src/C/mmult.c
+++ ./src/C/mmult.c
@@ -20,6 +20,7 @@
 #include <string.h>
 #include <mpi.h>
 #include <math.h>
+#include <cblas.h>
 
 #define DEFAULT_FN "res_C.mat"
 #define DEFAULT_SIZE 64
@@ -161,7 +161,7 @@
 
   printf("%d: Processing...\n", mr);
   
-  mmult(sz, nproc, mat_a, mat_b, mat_c);
+  cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, sz/nproc, sz, sz, 1.0, mat_a, sz, mat_b, sz, 1.0, mat_c, sz);
   
   if(mr == 0)
   {


--- ./src/F90/mmult.F90
+++ ./src/F90/mmult.F90
@@ -107,7 +107,10 @@

   print *,mr,": Processing..."

-  call mmult(sz, nproc, mat_a, mat_b, mat_c)
+  call DGEMM('N','N', sz, sz/nproc, sz, 1.0D0, &
+             mat_b, sz, &
+             mat_a, sz, 1.0D0, &
+             mat_c, sz)

   if(mr==0) then
     print *,mr,": Receiving result matrix..."


--- ./src/make.def
+++ ./src/make.def
@@ -18,6 +18,6 @@
 FC = mpif90

 # Define additional compilation flags
-CFLAGS = -Ofast -g
-LFLAGS =
+CFLAGS = -Ofast -g -I/usr/include/aarch64-linux-gnu
+LFLAGS = -L/usr/lib/aarch64-linux-gnu/blas -lblas -Wl,-rpath=/usr/lib/aarch64-linux-gnu/blas
```

### Use Arm Performance Library

Download Arm Performance Library [here](https://developer.arm.com/downloads/-/arm-performance-libraries), and edit `src/make.def` before rebuilding the application:

```makefile
CFLAGS = -Ofast -g -I $ARMPL_INCLUDES
LDFLAGS = -L $ARMPL_LIBRARIES -larmpl
```

## Summary

The graphs below summarize the optimizations on the C version of the application, when using 1, 2 or 4 processes on AWS Graviton 2.

![Graph](https://raw.githubusercontent.com/armflorentlebeau/arm_hpc_tools_trial/master/.github/data/graph.png)

## Next Steps

We have optimized the compute kernel of this example and we have new bottlenecks. Optimized versions of the application don't scale as we increase the number of processes. Data transfers and IO are now dominant in the application: using more processors to compute the workload doesn't reduce the execution time linearly. A [parallel profiler](https://youtu.be/zIITp7ZqZXI) can help optimize the code further.
