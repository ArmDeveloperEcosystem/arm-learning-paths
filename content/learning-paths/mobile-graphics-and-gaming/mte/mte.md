---
# User change
title: Create and compile an example C application to explore Arm MTE 
description: "Create and compile a C example on AArch64 Linux to prepare for exploring Arm Memory Tagging Extension (MTE)."

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## What Arm MTE is

The Arm Memory Tagging Extension (MTE) is a security feature built into Armv8.5-A and Armv9-A processors. MTE detects buffer overflow errors and use-after-free errors in software. These memory safety issues are the primary source of vulnerabilities.

MTE is helpful for many types of software. It improves the Linux kernel as well as Linux and Android applications.

To learn more about MTE, read the article [Memory safety: How Arm Memory Tagging Extension addresses this industry-wide security challenge](https://www.arm.com/blogs/blueprint/memory-safety-arm-memory-tagging-extension).

The example uses Ubuntu 22.04. You can use other recent versions of Linux.

## Before you begin

Ensure you have an AArch64 Linux machine.

On the machine, install the metapackage that includes software tools for building the example C program:

```console
sudo apt install build-essential -y
```

Hardware availability for MTE is limited. If your processor doesn't support MTE, you can run the example application using [QEMU](https://www.qemu.org/). 

Install `qemu-user` if your processor doesn't support MTE:

```console
sudo apt install qemu-user -y
```

## Create and build the example

Review the comments in the source code to see how MTE works.

The code demonstrates how to:

- Find out if the processor supports MTE
- Enable synchronous MTE
- Allocate memory with MTE enabled
- Access memory with the default tag of 0
- Generate a random tag and use it for the lock on the memory and the key on the pointer
- Access memory with the generated tag
- Access memory beyond the 16-byte granule and confirm MTE detects a mismatch

To create and build the example, follow these steps:

1. Use a text editor to copy and paste the following C code into a file named `mte-example.c`:

```c
/*
 * Memory Tagging Extension (MTE) example for Linux
 *
 * Compile with gcc and use -march=armv8.5-a+memtag
 *    gcc mte-example.c -o mte-example -march=armv8.5-a+memtag
 *
 * Compilation should be done on a recent Arm Linux machine for the .h files to include MTE support.
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/auxv.h>
#include <sys/mman.h>
#include <sys/prctl.h>

/*
 * Insert a random logical tag into the given pointer.
 * IRG instruction.
 */
#define insert_random_tag(ptr) ({                       \
        uint64_t __val;                                 \
        asm("irg %0, %1" : "=r" (__val) : "r" (ptr));   \
        __val;                                          \
})

/*
 * Set the allocation tag on the destination address.
 * STG instruction.
 */
#define set_tag(tagged_addr) do {                                      \
        asm volatile("stg %0, [%0]" : : "r" (tagged_addr) : "memory"); \
} while (0)

int main(void) 
{
    unsigned char *ptr;   // pointer to memory for MTE demonstration

    /* 
     * Use the architecture dependent information about the processor 
     * from getauxval() to check if MTE is available.  
     */
    if (!((getauxval(AT_HWCAP2)) & HWCAP2_MTE)) 
    {
        printf("MTE is not supported\n");
        return EXIT_FAILURE;
    }
    else
    {
        printf("MTE is supported\n");
    }
                
    /*
     * Enable MTE with synchronous checking
     */
    if (prctl(PR_SET_TAGGED_ADDR_CTRL, 
              PR_TAGGED_ADDR_ENABLE | PR_MTE_TCF_SYNC | (0xfffe << PR_MTE_TAG_SHIFT),
              0, 0, 0)) 
    {
            perror("prctl() failed");
            return EXIT_FAILURE;
    }

    /*
     * Allocate 1 page of memory with MTE protection
     */
    ptr = mmap(NULL, sysconf(_SC_PAGESIZE), PROT_READ | PROT_WRITE | PROT_MTE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (ptr == MAP_FAILED) 
    {
        perror("mmap() failed");
        return EXIT_FAILURE;
    }

    /*
     * Print the pointer value with the default tag (expecting 0)
     */
    printf("pointer is %p\n", ptr);

    /* 
     * Write the first 2 bytes of the memory with the default tag
     */
    ptr[0] = 0x41;
    ptr[1] = 0x42;

    /*
     * Read back to confirm the writes
     */
    printf("ptr[0] = 0x%hhx ptr[1] = 0x%hhx\n", ptr[0], ptr[1]);

    /* 
     * Generate a random tag and store it for the address (IRG instruction)
     */
    ptr = (unsigned char *) insert_random_tag(ptr);

    /* 
     * Set the key on the pointer to match the lock on the memory  (STG instruction)
     */
    set_tag(ptr);

    /*
     * Print the pointer value with the new tag
     */
    printf("pointer is now %p\n", ptr);

    /* 
     * Write the first 2 bytes of the memory again, with the new tag
     */
    ptr[0] = 0x43;
    ptr[1] = 0x44;

    /*
     * Read back to confirm the writes
     */
    printf("ptr[0] = 0x%hhx ptr[1] = 0x%hhx\n", ptr[0], ptr[1]);

    /*
     * Write to memory beyond the 16 byte granule (offsest 0x10)
     * MTE should generate an exception
     * If the offset is less than 0x10 no SIGSEGV will occur.
     */
    printf("Expecting SIGSEGV...\n");
    ptr[0x10] = 0x55;

    /* 
     * Program only reaches this if no SIGSEGV occurs
     */
    printf("...no SIGSEGV was received\n");

    return EXIT_FAILURE;
}
```

2. Compile the example using `gcc`:

```console
gcc mte-example.c -o mte-example -march=armv8.5-a+memtag
```

The executable `mte-example` is now ready to run.

## What you've accomplished and what's next

You've created and compiled the `mte-example` executable.

Next, you'll run the executable to observe the example's behavior.
