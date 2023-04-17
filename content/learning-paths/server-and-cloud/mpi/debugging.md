---
# User change
title: "Debug your application"

weight: 3 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

A parallel matrix multiplication application is located in the `src` directory. 

It is implemented in C, Fortran, and Python. Each implementation has a bug and does not work without modification. 

You can debug the application using a variety of tools. 

## Build options for debugging

1. Navigate to the `src` directory:

```bash
cd src
```

2. Modify the compiler settings

Use a text editor to modify `make.def` 

Add the `CFLAGS` as shown below to disable compiler optimizations and add debugging symbols:

```makefile
CFLAGS = -O0 -g -fsanitize=address
```

These `CFLAGS` also make it easier to find memory issues such as out-of-bound array accesses. 

## Build

Select the implementation you would like to use: C, Fortran, or Python. 

1. Navigate to the sub-directory

For example, for C:

```bash
cd  C
```


2. Build the application

```bash 
make
```

## Run

Run the application with `mpirun`. There are slight differences for Python so use the commands below.

The matrix size can be set with an argument to the application. It is set to 1024 below.

- for C and Fortran:

```bash 
mpirun ./mmult 1024
```

- for Python

```bash 
mpirun python3 ./mmult.py -s 1024
```

Because the program has an error and the address sanitizer is on you will see output similar to:

```output
0: Size of the matrices: 1024x1024
1: Receiving matrices...
0: Initializing matrices...
0: Sending matrices...
0: Processing...
1: Processing...
=================================================================
==11429==ERROR: AddressSanitizer: heap-buffer-overflow on address 0xffffa12fc800 at pc 0xaaaae6e817fc bp 0xffffe865be40 sp 0xffffe865be60
READ of size 8 at 0xffffa12fc800 thread T0
=================================================================
==11430==ERROR: AddressSanitizer: heap-buffer-overflow on address 0xffffaa0fc800 at pc 0xaaaac30417fc bp 0xffffd2b0eaf0 sp 0xffffd2b0eb10
READ of size 8 at 0xffffaa0fc800 thread T0
    #0 0xaaaae6e817f8 in mmult /home/ubuntu/arm_hpc_tools_trial/src/C/mmult.c:67
    #1 0xaaaae6e822b0 in main /home/ubuntu/arm_hpc_tools_trial/src/C/mmult.c:164
    #0 0xaaaac30417f8 in mmult /home/ubuntu/arm_hpc_tools_trial/src/C/mmult.c:67
    #2 0xffffab84ce0c in __libc_start_main (/lib/aarch64-linux-gnu/libc.so.6+0x20e0c)
    #3 0xaaaae6e814a0  (/home/ubuntu/arm_hpc_tools_trial/src/C/mmult+0x14a0)

```

The output above is truncated and you may find it difficult to isolate the source of the buffer overflow. 

### Use a parallel debugger

Parallelism can introduce specific bugs such as race conditions or deadlocks. To control the parallel execution and visualize the source code, a parallel debugger such as Linaro DDT can help. 

It is also easier to identify the exact source of the error using DDT.

Run the same implementation you used above, but with `ddt`: 

- for C and Fortran:

```bash 
ddt mpirun ./mmult 1024
```

- for Python

```bash
ddt mpirun python ./mmult.py -s 1024
```

The `ddt` command will launch a GUI. 

You can use it to control the options used to run application and to investigate the bug.

## Fix the application

Navigate back up to the `arm_hpc_tools_trial` directory for this section. 

To fix the application, you can apply a patch.

1. Create a patch file

Use a text editor to create a new file in the `arm_hpc_tools_trial` directory named `p1` and copy the contents below into the file.

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
-CFLAGS = -O0 -g -fsanitize=address
+CFLAGS = 
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

2. Run the patch command:

```bash
patch -p0 < p1
```

## Run the fixed application

Repeat the build and run steps above and confirm the application run correctly. 

```bash
cd src/C
make clean
make 
mpirun ./mmult 1024
```

Wait for the `mmult` application to complete without any errors. 

Continue to learn about profiling a parallel application.
