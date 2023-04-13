---
# User change
title: "Debug your application"

weight: 3 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Build options for debugging

Edit the file in `src/make.def` and change the following line to disable compiler optimizations and add debugging symbols:

```makefile
CFLAGS = -O0 -g
```

### Enable address sanitizer

To check for memory issues such as out-of-bound array accesses, you can enable the compiler's address sanitizer:

```makefile
CFLAGS = -O0 -g -fsanitize=address
```

## Build

Select your version C/Fortran/Python of the application in `src`, then build the application with:

```bash {  command_line="user@localhost" }
make
```

## Run

Select your version C/Fortran/Python of the application in `src`, then run the application with:

```bash {  command_line="user@localhost" }
mpirun ./mmult
```

or using Python

```bash {  command_line="user@localhost" }
mpirun python ./mmult.py
```

The matrix size can be set with an extra argument, e.g.

```bash {  command_line="user@localhost" }
mpirun ./mmult 1024
```

or using Python

```bash {  command_line="user@localhost" }
mpirun python ./mmult.py -s 1024
```

If you have enabled the compiler's address sanitizer, a report will be output when the application terminates. Look out for ERROR messages reporting out-of-bounds array accesses.


### Use a parallel debugger

Parallelism can introduce specific bugs such as race conditions or deadlocks. To control the parallel execution and visualize the source code, a parallel debugger such as [Linaro DDT](/install-guides/forge/) can help. 

In the same folder previously selected, run the C/Fortran application in parallel with:

```bash {  command_line="user@localhost" }
ddt mpirun ./mmult
```

or using Python

```bash {  command_line="user@localhost" }
ddt mpirun python ./mmult.py
```

This command will launch a GUI. Control options enable to run the application and investigate the bug.

## Fix the application

To fix the application, you can apply the following patch.

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
