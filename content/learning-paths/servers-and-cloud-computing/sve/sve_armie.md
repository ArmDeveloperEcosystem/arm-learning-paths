---
# User change
title: "Run SVE without capable hardware"

weight: 4 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

There are two ways to run SVE instructions if you don't have SVE capable hardware: QEMU and the Arm Instruction Emulator (ArmIE). Each of these is covered below. 

The steps shown are for an Arm v8-A system with Ubuntu 22.04 and no SVE support. 

## Example code

The example code adds two 127 double-precision arrays.

Use a text editor to copy the code below and save it in a file named `sve_add.c`

```c  { line_numbers = "true" }
#include <stdlib.h>
#include <stdio.h>

#ifndef SIZE
#define SIZE 127
#endif

void fun(double * restrict a, double * restrict b, int size)
{
  for (int i=0; i < size; ++i)
  {
    b[i] += a[i];
  }
}

int main() 
{
  int i;

  double *a=(double *)malloc(sizeof(double)*SIZE);
  double *b=(double *)malloc(sizeof(double)*SIZE);

  fun(a, b, SIZE);

  printf("Done.\n");
}
```

### Compile

Compile the applications using the commands shown:

{{< tabpane >}}
  {{< tab header="GNU" >}}
  gcc -march=armv8-a+sve -O3 -fopt-info-vec sve_add.c -o sve_add.exe
  {{< /tab >}}
  {{< tab header="Arm Compiler for Linux" >}}
  armclang --march=armv8-a+sve -O3 -Rpass=vector sve_add.c -o sve_add.exe
  {{< /tab >}}
{{% /tabpane %}}

### Run

Run the application on the Arm Linux host:

```bash {  command_line="user@localhost | 2"  }
./sve_add.exe
Illegal instruction (core dumped)
```

An illegal instruction message confirms the host does not support SVE. 

## QEMU 

You can run applications containing SVE instructions without SVE capable hardware using [QEMU](https://www.qemu.org/), a generic and open source machine emulator and virtualizer.

Install `qemu-user` to run the example on processors which do not support SVE:

```bash {  command_line="user@localhost" }
sudo apt install qemu-user -y
```

Run the example application with a vector length of 256 bits, note that the vector length is specified in bytes rather than bits:

```bash {  command_line="user@localhost | 2"  }
qemu-aarch64 -cpu max,sve-default-vector-length=32 ./sve_add.exe
Done.
```

The application now runs and prints the expected message.

## Arm Instruction Emulator

You can also run the application containing SVE instructions using the the Arm Instruction Emulator.

Download and install the [Arm Instruction Emulator](https://developer.arm.com/downloads/-/arm-instruction-emulator) (see [installation instructions](/install-guides/armie) ) on any Arm v8-A system. The Arm Instruction Emulator intercepts and emulates unsupported SVE instructions. It also support plugins for application analysis.

{{% notice Note %}}
The Arm Instruction Emulator has been deprecated. It is still available for download, but there is no active development. 
{{% /notice %}}

## Arm Instruction Emulator Usage

Now run the application with ArmIE as shown:

```bash {  command_line="user@localhost" }
armie -msve-vector-bits=256 -- ./sve_add.exe
```
Armie requires the `-msve-vector-bits` parameter to specify the SVE vector length.

## Plugins
Armie has plugins you can use to analyze your application.

### Count SVE instructions

The `libinscount_emulated.so` plugin reports the amount of executed instructions. Run the command below and check the output:

```bash {  command_line="user@localhost | 2-4"  }
armie -msve-vector-bits=256 -i libinscount_emulated.so  -- ./sve_add.exe
Client inscount is running
Done.
146163 instructions executed of which 193 were emulated instructions
```

Increasing the vector width from 256 to 512 divides the amount of emulated SVE instructions by two as shown:

```bash {  command_line="user@localhost | 2-4"  }
armie -msve-vector-bits=512 -i libinscount_emulated.so  -- ./sve_add.exe
Client inscount is running
Done.
146051 instructions executed of which 97 were emulated instructions
```

### SVE instruction breakdown

To get more information on which instruction are executed, the `libopcodes_emulated.so` plugin can be used as shown:

```bash {  command_line="user@localhost" }
armie -msve-vector-bits=512 -i libopcodes_emulated.so -- ./sve_add.exe
```

Undecoded instructions are stored in a file with the format `undecoded.APP.PID.log`. To decode them, use the script `enc2instr.py`, provided with Armie. 
This script requires llvm-mc and python 2.7. Install, using the command shown:

```bash {  command_line="user@localhost" }
sudo apt install llvm python
```

This example command processes the results:

```bash {  command_line="user@localhost" }
awk -F" : " '{print $2}' undecoded.sve_add.exe.175166.log | LLVM_MC=$(which llvm-mc) ./enc2instr.py | awk -F" : " '{print $2}' > decoded.log && paste undecoded.sve_add.exe.175166.log decoded.log
```

Which gives the following output:

```output
       16 : 0xe5e14000  st1d { z0.d }, p0, [x0, x1, lsl #3]
       16 : 0xa5e14260  ld1d { z0.d }, p0/z, [x19, x1, lsl #3]
       16 : 0xa5e14001  ld1d { z1.d }, p0/z, [x0, x1, lsl #3]
       16 : 0x65c10000  fadd z0.d, z0.d, z1.d
       16 : 0x25e31c20  whilelo p0.d, x1, x3
       16 : 0x04f0e3e1  incd x1
        1 : 0x25e21fe0  whilelo p0.d, xzr, x2
```

In this list, see SVE instructions identified in the previous tutorial  [Compile for SVE](/learning-paths/servers-and-cloud-computing/sve/sve_compile/). In the main loop, they are executed 16 times to compute the addition of 127 array elements (16 batches of 512-bit SVE instructions).

### Trace SVE memory accesses on specific code sections

#### Specify region of interest (RoI)

The RoI allows to limit the amount of data generated by tracing. Add the following macros as shown in the code snippet below:

```c  { line_numbers="true",highlight_lines="1,2,6,11" }
#define __START_TRACE() { asm volatile (".inst 0x2520e020"); }
#define __STOP_TRACE() { asm volatile (".inst 0x2520e040"); }

void fun(double * restrict a, double * restrict b, int size)
{
  __START_TRACE()
  for (int i=0; i < size; ++i)
  {
    b[i] += a[i];
  }
  __STOP_TRACE()
}
```

### Rebuild application and trace memory accesses

Rebuild the application and add the options `-a -roi` to Armie to filter data for the RoI:

```bash {  command_line="user@localhost" }
armie -e libmemtrace_sve_512.so -i libinstrace_emulated.so -a -roi -- ./sve_add.exe
```

Using `libmemtrace_sve_512.so` and `libinstrace_emulated.so` will generate two data files `instrace.APP.PID.log` and `sve-memtrace.APP.PID.log`. `instrace.APP.PID.log` traces all instructions executed. `sve-memtrace.APP.PID.log` only captures information about SVE memory accesses.

To filter data of interest, run the following commands:

```bash {  command_line="user@localhost" }
sed -i "/\(,0$\|;\)/d" instrace.sve_add.exe.235921.0000.log
sed -i '1d;$d' sve-memtrace.sve_add.exe.235921.log
awk -F"," '{print $2}' instrace.sve_add.exe.235921.0000.log | LLVM_MC=$(which llvm-mc) ./enc2instr.py | awk -F" : " '{print $2}' > mem.log && paste sve-memtrace.sve_add.exe.235921.log mem.log
```

The output will look like this:

```output
1, -1042929472, 0, 0, 64, 0xffff81d096a0, 0xffff81cf66d8        ld1d { z1.d }, p0/z, [x0, x1, lsl #3]
2, -1042929472, 0, 0, 64, 0xffff81d092a0, 0xffff81cf66dc        ld1d { z0.d }, p0/z, [x19, x1, lsl #3]
3, -1042929472, 0, 1, 64, 0xffff81d096a0, 0xffff81cf66e4        st1d { z0.d }, p0, [x0, x1, lsl #3]
[...]
43, -1042929472, 0, 0, 64, 0xffff81d09a20, 0xffff81cf66d8       ld1d { z1.d }, p0/z, [x0, x1, lsl #3]
44, -1042929472, 0, 0, 64, 0xffff81d09620, 0xffff81cf66dc       ld1d { z0.d }, p0/z, [x19, x1, lsl #3]
45, -1042929472, 0, 1, 64, 0xffff81d09a20, 0xffff81cf66e4       st1d { z0.d }, p0, [x0, x1, lsl #3]
46, -1042929472, 0, 0, 56, 0xffff81d09a60, 0xffff81cf66d8       ld1d { z1.d }, p0/z, [x0, x1, lsl #3]
47, -1042929472, 0, 0, 56, 0xffff81d09660, 0xffff81cf66dc       ld1d { z0.d }, p0/z, [x19, x1, lsl #3]
48, -1042929472, 0, 1, 56, 0xffff81d09a60, 0xffff81cf66e4       st1d { z0.d }, p0, [x0, x1, lsl #3]
```

You can identify 16 batches of 512-bit SVE load and stores. All of them are unpredicated and handle 64 bytes, except the last iteration which handles 56 bytes to compute elements indexes [120-126].
