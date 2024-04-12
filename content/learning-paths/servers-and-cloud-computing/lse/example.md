---
# User change
title: "Large System Extensions (LSE) Example"
weight: 3

layout: "learningpathall"

---

## Try Large System Extensions (LSE) using an example C program

You can build and run an example to learn more and find out if the compiler is generating LSE instructions. 

Below is an [example program from cppreference.com](https://en.cppreference.com/w/c/language/atomic). 

Use a text editor of your choice to save the example program in a file called `atomic.c` on your Arm Linux computer. 

```cpp
#include <stdio.h>
#include <threads.h>
#include <stdatomic.h>
 
atomic_int acnt;
int cnt;
 
int f(void* thr_data)
{
    for(int n = 0; n < 1000; ++n) {
        ++cnt;
        ++acnt;
    }
    return 0;
}
 
int main(void)
{
    thrd_t thr[10];
    for(int n = 0; n < 10; ++n)
        thrd_create(&thr[n], f, NULL);
    for(int n = 0; n < 10; ++n)
        thrd_join(thr[n], NULL);
 
    printf("The atomic counter is %u\n", acnt);
    printf("The non-atomic counter is %u\n", cnt);
}
```
The atomic_int C data type is used to indicate that accesses to the acnt variable must be atomic.

The results on different AWS instance types are shown below. You can also try this on any Arm Linux computer. 

### A1 Instance

The AWS A1 instance uses Cortex-A72, without LSE. This can also be done on any Cortex-A53 or Cortex-A72 system. 

On Ubuntu 20.04 the default gcc version is 9.4.0. Check this by running:

```bash
gcc --version
```

The output is:

```output
gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

Now compile the application:

```bash
gcc -g atomic.c -o a1 -march=armv8-a -lpthread
objdump -S a1 > a1.dis
```

Review the disassembly file `a1.dis` and check the instructions for incrementing acnt. The sequence is:

- Address of acnt is loaded into x0
- Value of acnt is loaded into w1 using load exclusive
- Add 1 to acnt
- Store exclusive to write the new value
- Check if the store succeed and if not loop back to 0x998 and load again

Here is a snippet of the disassembly performing this sequence:

```output
994:   f947e400        ldr     x0, [x0, #4040]
998:   885ffc01        ldaxr   w1, [x0]
99c:   0b020021        add     w1, w1, w2
9a0:   8803fc01        stlxr   w3, w1, [x0]
9a4:   35ffffa3        cbnz    w3, 998 <f+0x5c>
```


### T4g Instance

The AWS T4g instance with Graviton2 uses Neoverse N1 with LSE. You can also use similar machines with Neoverse N1.

Compile the same application on a T4g instance:
 
```bash
gcc -g atomic.c -o t4g -march=armv8.2-a -lpthread
objdump -S t4g > t4g.dis
```

Review the file t4g.dis and check the instructions for incrementing acnt. The sequence is:

- Address of acnt is loaded into x0
- Value of acnt is updated using a single instruction to add 1 to a word in memory

Here is a snippet of the disassembly performing this sequence:

```output
994:   f947e400        ldr     x0, [x0, #4040]
998:   b8e10002        ldaddal w1, w2, [x0]
```

Staying on the T4g instance, compile the application with outline-atomics:

```console
gcc -g atomic.c -o t4g.outline  -moutline-atomics -lpthread
objdump -S t4g.outline > outline.dis
```

Review the file outline.dis and see that the instruction to increment acnt is now a branch to something called __aarch64_ldadd4_acq_rel at address 0xb90:

```output
 a24:   9400005b        bl      b90 <__aarch64_ldadd4_acq_rel>
```

The code for both the load exclusive sequence and the atomic instruction are present as shown in the disassembly snippet below. The section of instructions before the first ret instruction is run on the T4g and the following instructions are run on the A1. This binary will run on both instances with no changes. In exchange for this flexibility there is the overhead to take a branch and run the correct code path.

```console
0000000000000b90 <__aarch64_ldadd4_acq_rel>:
 b90:   d503245f        bti     c
 b94:   d0000090        adrp    x16, 12000 <__data_start>
 b98:   39404610        ldrb    w16, [x16, #17]
 b9c:   34000070        cbz     w16, ba8 <__aarch64_ldadd4_acq_rel+0x18>
 ba0:   b8e00020        ldaddal w0, w0, [x1]
 ba4:   d65f03c0        ret
 ba8:   2a0003f0        mov     w16, w0
 bac:   885ffc20        ldaxr   w0, [x1]
 bb0:   0b100011        add     w17, w0, w16
 bb4:   880ffc31        stlxr   w15, w17, [x1]
 bb8:   35ffffaf        cbnz    w15, bac <__aarch64_ldadd4_acq_rel+0x1c>
 bbc:   d65f03c0        ret
```

As a final check, move back to the A1 instance and compile for `armv8.2-a` architecture. The atomic instruction is illegal on the Cortex-A72 and fails.

```bash
gcc -g atomic.c -o a1 -march=armv8.2-a -lpthread
./a1
```

The result is:

```output
Illegal instruction (core dumped)
```

## How can I find out if my application has atomic instructions?

To check for atomic instructions in applications run objdump on the T4g executable:

```bash
objdump -d t4g | grep -i 'cas\|casp\|swp\|ldadd\|stadd\|ldclr\|stclr\|ldeor\|steor\|ldset\|stset\|ldsmax\|stsmax\|ldsmin\|stsmin\|ldumax\|stumax\|ldumin\|stumin' | wc -l
```

The above command will report a count of 1 instruction, the `ldaddal` instruction.

To check whether applications contain load exclusives and store exclusives run this command on the A1 executable. It will report a count of 2.

```bash
objdump -d a1 | grep -i 'ldxr\|ldaxr\|stxr\|stlxr' | wc -l
```

Running on the t4g.outline executable which supports both architectures will report both types of instructions. 

Another way to confirm an executable supports both architectures is to run the command:

```bash
nm t4g.outline | grep __aarch64_have_lse_atomics | wc -l
```

If it returns a 1 then it was compiled with outline-atomics.

## Summary

Large System Extensions introduce atomic instructions to improve performance for Arm systems with many processors. When migrating applications to Neoverse it helps to have an understanding of compilers, compiler options, and libraries. Also, think about the strategy for an application supporting only Neoverse or also including support for processors which don't include LSE.

