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

The AWS A1 instance uses Cortex-A72, **without LSE**. This can also be done on any Cortex-A53 or Cortex-A72 system. 

On Ubuntu 26.04 the default gcc version is 15.2.0. Check this by running:

```bash
gcc --version
```

The output is:

```output
gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0
Copyright (C) 2025 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

GCC 10.1 and later enable `-moutline-atomics` by default and generate a helper function that checks at runtime whether LSE is available.

Now compile the application without outline atomics:

```bash
gcc -g atomic.c -fverbose-asm -mno-outline-atomics -o a1 -march=armv8-a -lpthread
objdump -S a1 > a1.dis
```

Review the disassembly file `a1.dis` and check the instructions for incrementing acnt. The sequence is:

- Address of acnt is loaded into x0
- Value of acnt is loaded into w2 using load exclusive
- Add 1 to acnt
- Store exclusive to write the new value
- Check if the store succeed and if not loop back to 0x988 and load again

Run the following command to see the instructions used to increment `acnt`

```bash { command_line="user@localhost | 2-14"}
cat a1.dis | grep -i "++acnt" -A 12
        ++acnt;
 970:   52800020        mov     w0, #0x1                        // #1
 974:   b9001fe0        str     w0, [sp, #28]
 978:   b9401fe0        ldr     w0, [sp, #28]
 97c:   2a0003e1        mov     w1, w0
 980:   90000100        adrp    x0, 20000 <__data_start>
 984:   91005000        add     x0, x0, #0x14
 988:   885ffc02        ldaxr   w2, [x0]
 98c:   0b010042        add     w2, w2, w1
 990:   8803fc02        stlxr   w3, w2, [x0]
 994:   35ffffa3        cbnz    w3, 988 <f+0x60>
 998:   2a0203e0        mov     w0, w2
 99c:   b90023e0        str     w0, [sp, #32]
```

### 1st Generation Arm AGI CPU

This example is run on a 1st generation Arm AGI CPU **with LSE**. You can also use another Neoverse N1 or later system, such as an AWS T4g instance.

Compile the same application:
 
```bash
gcc -g atomic.c -fverbose-asm -mno-outline-atomics -o agi -march=armv8.2-a -lpthread
objdump -S agi > agi.dis
```

Review the file agi.dis and check the instructions for incrementing acnt. The sequence is:

- Address of acnt is loaded into x0
- Value of acnt is updated using a single instruction to add 1 to a word in memory ([ldaddal](https://developer.arm.com/documentation/111108/2026-03/Base-Instructions/LDADD--LDADDA--LDADDAL--LDADDL--Atomic-add-on-word-or-doubleword-)).

Run the following command to see the instructions used to increment `acnt` on the AGI CPU. 

```bash { command_line="user@localhost | 2-11"}
cat agi.dis | grep -i "++acnt" -A 9
        ++acnt;
 920:   52800020        mov     w0, #0x1                        // #1
 924:   b9001fe0        str     w0, [sp, #28]
 928:   b9401fe0        ldr     w0, [sp, #28]
 92c:   2a0003e1        mov     w1, w0
 930:   90000100        adrp    x0, 20000 <__data_start>
 934:   91005000        add     x0, x0, #0x14
 938:   b8e10002        ldaddal w1, w2, [x0]
 93c:   0b010040        add     w0, w2, w1
 940:   b90023e0        str     w0, [sp, #32]
```

Staying on the same Arm Linux machine with LSE, compile the application with outline atomics by omitting the `-mno-outline-atomics` flag:

```bash
gcc -g atomic.c -o agi.outline -lpthread
objdump -S agi.outline > outline.dis
```

Review the file outline.dis and see that the instruction to increment acnt is now a branch to something called __aarch64_ldadd4_acq_rel at address 0xb80:

```output
 a04:	9400005f 	bl	b80 <__aarch64_ldadd4_acq_rel>
 ```

The code for both the load exclusive sequence and the atomic instruction are present as shown in the disassembly snippet below. The section of instructions before the first ret instruction is run on the agi and the following instructions are run on the A1. This binary will run on both instances with no changes. In exchange for this flexibility there is the overhead to take a branch and run the correct code path.

```console
0000000000000b80 <__aarch64_ldadd4_acq_rel>:
 b80:	d503245f 	bti	c
 b84:	90000110 	adrp	x16, 20000 <__data_start>
 b88:	39407210 	ldrb	w16, [x16, #28]
 b8c:	34000070 	cbz	w16, b98 <__aarch64_ldadd4_acq_rel+0x18>
 b90:	b8e00020 	ldaddal	w0, w0, [x1]
 b94:	d65f03c0 	ret
 b98:	2a0003f0 	mov	w16, w0
 b9c:	885ffc20 	ldaxr	w0, [x1]
 ba0:	0b100011 	add	w17, w0, w16
 ba4:	880ffc31 	stlxr	w15, w17, [x1]
 ba8:	35ffffaf 	cbnz	w15, b9c <__aarch64_ldadd4_acq_rel+0x1c>
 bac:	d65f03c0 	ret
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

To check for atomic instructions in applications run objdump on the agi executable:

```bash
objdump -d agi | grep -i 'cas\|casp\|swp\|ldadd\|stadd\|ldclr\|stclr\|ldeor\|steor\|ldset\|stset\|ldsmax\|stsmax\|ldsmin\|stsmin\|ldumax\|stumax\|ldumin\|stumin' | wc -l
```

The above command will report a count of 1 instruction, the `ldaddal` instruction.

To check whether applications contain load exclusives and store exclusives run this command on the A1 executable. It will report a count of 2.

```bash
objdump -d a1 | grep -i 'ldxr\|ldaxr\|stxr\|stlxr' | wc -l
```

Running on the agi.outline executable which supports both architectures will report both types of instructions. 

Another way to confirm an executable supports both architectures is to run the command:

```bash
nm agi.outline | grep __aarch64_have_lse_atomics | wc -l
```

If it returns a 1 then it was compiled with outline-atomics.

## Summary

Large System Extensions introduce atomic instructions to improve performance for Arm systems with many processors. When migrating applications to Neoverse it helps to have an understanding of compilers, compiler options, and libraries. Also, think about the strategy for an application supporting only Neoverse or also including support for processors which don't include LSE.

