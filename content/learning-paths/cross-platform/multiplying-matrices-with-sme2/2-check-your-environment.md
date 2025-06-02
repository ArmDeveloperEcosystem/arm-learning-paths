---
title: Test your environment
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you will check that your environment is all set up and ready to develop with SME2. This will be your first hands-on experience with the environment.

## Compile the examples

First, compile the example code with Clang:

```BASH { output_lines="2-19" }
docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v1 make
clang --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -nostartfiles -lcrt0-semihost -lsemihost -Wl,--defsym=__boot_flash=0x80000000 -Wl,--defsym=__flash=0x80001000 -Wl,--defsym=__ram=0x81000000 -T picolibc.ld -o hello hello.c
clang --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -c -o sme2_check.o sme2_check.c
clang --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -c -o misc.o misc.c
clang --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -nostartfiles -lcrt0-semihost -lsemihost -Wl,--defsym=__boot_flash=0x80000000 -Wl,--defsym=__flash=0x80001000 -Wl,--defsym=__ram=0x81000000 -T picolibc.ld -o sme2_check sme2_check.o misc.o
clang --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -DIMPL=asm -c -o main_asm.o main.c
clang --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -c -o matmul_asm.o matmul_asm.c
clang --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -c -o matmul_asm_impl.o matmul_asm_impl.S
clang --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -c -o preprocess_l_asm.o preprocess_l_asm.S
clang --target=aarch64-none-elf  -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -c -o matmul_vanilla.o matmul_vanilla.c
clang --target=aarch64-none-elf  -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -c -o preprocess_vanilla.o preprocess_vanilla.c
clang --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -nostartfiles -lcrt0-semihost -lsemihost -Wl,--defsym=__boot_flash=0x80000000 -Wl,--defsym=__flash=0x80001000 -Wl,--defsym=__ram=0x81000000 -T picolibc.ld -o sme2_matmul_asm main_asm.o matmul_asm.o matmul_asm_impl.o preprocess_l_asm.o matmul_vanilla.o preprocess_vanilla.o misc.o
clang --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -DIMPL=intr -c -o main_intr.o main.c
clang --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -c -o matmul_intr.o matmul_intr.c
clang --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -O2 -Wall -std=c99 -nostartfiles -lcrt0-semihost -lsemihost -Wl,--defsym=__boot_flash=0x80000000 -Wl,--defsym=__flash=0x80001000 -Wl,--defsym=__ram=0x81000000 -T picolibc.ld -o sme2_matmul_intr main_intr.o matmul_intr.o matmul_vanilla.o preprocess_vanilla.o misc.o
llvm-objdump --demangle -d hello > hello.lst
llvm-objdump --demangle -d sme2_check > sme2_check.lst
llvm-objdump --demangle -d sme2_matmul_asm > sme2_matmul_asm.lst
llvm-objdump --demangle -d sme2_matmul_intr > sme2_matmul_intr.lst
```

 Executed within the docker ``armswdev/sme2-learning-path:sme2-environment-v1`` environment, the ``make`` command performs the following tasks:

- It builds four executables: ``hello``, ``sme2_check``, ``sme2_matmul_asm``, and ``sme2_matmul_intr``.
- It creates the assembly listings for the four executables: ``hello.lst``, ``sme2_check.lst``, ``sme2_matmul_asm.lst``, and ``sme2_matmul_intr.lst``.

{{% notice Note %}}
At any point, you can clean the directory of all the files that have been built by invoking ``make clean``:

```BASH
$ docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v1 make clean
```
{{% /notice %}}

## Basic checks

The very first program that you should run is the famous "Hello, world !" example that
will tell you if your environment is set up correctly. 

The source code is contained in ``hello.c`` and looks like this:

```C
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    printf("Hello, world !\n");
    return EXIT_SUCCESS;
}
```

Run the FVP simulation of the ``hello`` program with:

```BASH { output_lines="2-4" }
docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v1 ./run-fvp.sh hello
Hello, world !

Info: /OSCI/SystemC: Simulation stopped by user.
```

The important line here is "``Hello, world !``" as it demonstrates that the generic code
can be compiled and run on the FVP.

## SME2 checks

You will now run the ``sme2_check`` program, which checks that SME2 works as
expected, in both the compiler and in the FVP. 

The source code is found in
``sme2_check.c``:

```C
#include <stdio.h>
#include <stdlib.h>

#include "misc.h"

#ifdef __ARM_FEATURE_SME2
#include <arm_sme.h>
#else
#error __ARM_FEATURE_SME2 is not defined
#endif

#define get_cpu_ftr(regId, feat, msb, lsb)                                     \
    ({                                                                         \
        unsigned long __val;                                                   \
        __asm__("mrs %0, " #regId : "=r"(__val));                              \
        printf("%-20s: 0x%016lx\n", #regId, __val);                            \
        printf("  - %-10s: 0x%08lx\n", #feat,                                  \
               (__val >> lsb) & ((1 << (msb - lsb)) - 1));                     \
    })

int main(int argc, char *argv[]) {
    get_cpu_ftr(ID_AA64PFR0_EL1, SVE, 35, 32);
    get_cpu_ftr(ID_AA64PFR1_EL1, SME, 27, 24);

    int n = 0;
#ifdef __ARM_FEATURE_SME2
    setup_sme();
    n = svcntb() * 8;
#endif
    if (n) {
        printf("SVE is available with length %d\n", n);
    } else {
        printf("SVE is unavailable.\n");
        exit(EXIT_FAILURE);
    }

    printf("Checking has_sme: %d\n", __arm_has_sme());
    printf("Checking in_streaming_mode: %d\n", __arm_in_streaming_mode());

    printf("Starting streaming mode...\n");
    __asm__("smstart");

    printf("Checking in_streaming_mode: %d\n", __arm_in_streaming_mode());

    printf("Stopping streaming mode...\n");
    __asm__("smstop");

    printf("Checking in_streaming_mode: %d\n", __arm_in_streaming_mode());

    return EXIT_SUCCESS;
}
```

The ``sme2_check`` program displays the SVE field of the ``ID_AA64PFR0_EL1`` system register and the SME field of the ``ID_AA64PFR1_EL1`` system register. It will then check if SVE and SME are available, then finally will switch into streaming mode and back from streaming mode.  

The ``__ARM_FEATURE_SME2`` macro is provided by the compiler when it targets an SME-capable target, which is specified with the ``-march=armv9.4-a+sme2`` command line option to ``clang`` in
file ``Makefile``. 

The ``arm_sme.h`` include file is part of the Arm C Library
Extension ([ACLE](https://arm-software.github.io/acle/main/)). 

The ACLE provides types and function declarations to enable C/C++ programmers to make the best possible use of the Arm architecture. You can use the SME-related part of the library, but it does also provide support for Neon or other Arm architectural extensions.

```BASH
docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v1 ./run-fvp.sh sme2_check
```

The output should be similar to:

```TXT
ID_AA64PFR0_EL1     : 0x1101101131111112
  - SVE       : 0x00000001
ID_AA64PFR1_EL1     : 0x0000101002000001
  - SME       : 0x00000002
SVE is available with length 512
Checking has_sme: 1
Checking in_streaming_mode: 0
Starting streaming mode...
Checking in_streaming_mode: 1
Stopping streaming mode...
Checking in_streaming_mode: 0

Info: /OSCI/SystemC: Simulation stopped by user.
```

You have now checked that the code can be compiled and run with full SME2 support, and are all set to move to the next section.
