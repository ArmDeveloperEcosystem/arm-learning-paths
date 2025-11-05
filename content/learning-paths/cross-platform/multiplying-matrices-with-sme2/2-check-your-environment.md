---
title: Test your SME2 development environment
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll verify that your environment is ready for SME2 development. This is your first hands-on task and confirms that the toolchain, hardware (or emulator), and compiler are set up correctly.

## Build the code examples

Use the `make` command to compile all examples and generate assembly listings:

{{< tabpane code=true >}}
  {{< tab header="Native SME2 support" language="bash" output_lines="2-19">}}
make
/opt/homebrew/opt/llvm/bin/clang -O2 -Wall -std=c99 -march=native+sme2 -DBAREMETAL=0   -o hello hello.c
/opt/homebrew/opt/llvm/bin/clang -O2 -Wall -std=c99 -march=native+sme2 -DBAREMETAL=0 -c -o sme2_check.o sme2_check.c
/opt/homebrew/opt/llvm/bin/clang -O2 -Wall -std=c99 -march=native+sme2 -DBAREMETAL=0 -c -o misc.o misc.c
/opt/homebrew/opt/llvm/bin/clang -O2 -Wall -std=c99 -march=native+sme2   -o sme2_check sme2_check.o misc.o
/opt/homebrew/opt/llvm/bin/clang -O2 -Wall -std=c99 -march=native+sme2 -DBAREMETAL=0 -DIMPL=asm -c -o main_asm.o main.c
/opt/homebrew/opt/llvm/bin/clang -O2 -Wall -std=c99 -march=native+sme2 -DBAREMETAL=0 -c -o matmul_asm.o matmul_asm.c
/opt/homebrew/opt/llvm/bin/clang -Wall -march=native+sve+sme2 -DBAREMETAL=0 -c -o matmul_asm_impl.o matmul_asm_impl.S
/opt/homebrew/opt/llvm/bin/clang -Wall -march=native+sve+sme2 -DBAREMETAL=0 -c -o preprocess_l_asm.o preprocess_l_asm.S
/opt/homebrew/opt/llvm/bin/clang -O2 -Wall -std=c99 -c -o matmul_vanilla.o matmul_vanilla.c
/opt/homebrew/opt/llvm/bin/clang -O2 -Wall -std=c99 -c -o preprocess_vanilla.o preprocess_vanilla.c
/opt/homebrew/opt/llvm/bin/clang -O2 -Wall -std=c99 -march=native+sme2   -o sme2_matmul_asm main_asm.o matmul_asm.o matmul_asm_impl.o preprocess_l_asm.o matmul_vanilla.o preprocess_vanilla.o misc.o
/opt/homebrew/opt/llvm/bin/clang -O2 -Wall -std=c99 -march=native+sme2 -DBAREMETAL=0 -DIMPL=intr -c -o main_intr.o main.c
/opt/homebrew/opt/llvm/bin/clang -O2 -Wall -std=c99 -march=native+sme2 -DBAREMETAL=0 -c -o matmul_intr.o matmul_intr.c
/opt/homebrew/opt/llvm/bin/clang -O2 -Wall -std=c99 -march=native+sme2   -o sme2_matmul_intr main_intr.o matmul_intr.o matmul_vanilla.o preprocess_vanilla.o misc.o
/opt/homebrew/opt/llvm/bin/llvm-objdump --demangle -d hello > hello.lst
/opt/homebrew/opt/llvm/bin/llvm-objdump --demangle -d sme2_check > sme2_check.lst
/opt/homebrew/opt/llvm/bin/llvm-objdump --demangle -d sme2_matmul_asm > sme2_matmul_asm.lst
/opt/homebrew/opt/llvm/bin/llvm-objdump --demangle -d sme2_matmul_intr > sme2_matmul_intr.lst
  {{< /tab >}}

  {{< tab header="Emulated SME2 support" language="bash" output_lines="2-19">}}
docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v2 make
clang -O2 -Wall -std=c99 --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -DBAREMETAL=1 -nostartfiles -lcrt0-semihost -lsemihost -nostartfiles -lcrt0-semihost -lsemihost -Wl,--defsym=__boot_flash=0x80000000 -Wl,--defsym=__flash=0x80001000 -Wl,--defsym=__ram=0x81000000 -T picolibc.ld -o hello hello.c
clang -O2 -Wall -std=c99 --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -DBAREMETAL=1 -c -o sme2_check.o sme2_check.c
clang -O2 -Wall -std=c99 --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -DBAREMETAL=1 -c -o misc.o misc.c
clang -O2 -Wall -std=c99 --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -nostartfiles -lcrt0-semihost -lsemihost -nostartfiles -lcrt0-semihost -lsemihost -Wl,--defsym=__boot_flash=0x80000000 -Wl,--defsym=__flash=0x80001000 -Wl,--defsym=__ram=0x81000000 -T picolibc.ld -o sme2_check sme2_check.o misc.o
clang -O2 -Wall -std=c99 --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -DBAREMETAL=1 -DIMPL=asm -c -o main_asm.o main.c
clang -O2 -Wall -std=c99 --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -DBAREMETAL=1 -c -o matmul_asm.o matmul_asm.c
clang -Wall --target=aarch64-none-elf -march=armv9.4-a+sme2 -DBAREMETAL=1 -c -o matmul_asm_impl.o matmul_asm_impl.S
clang -Wall --target=aarch64-none-elf -march=armv9.4-a+sme2 -DBAREMETAL=1 -c -o preprocess_l_asm.o preprocess_l_asm.S
clang -O2 -Wall -std=c99 --target=aarch64-none-elf -fno-exceptions -fno-rtti -mno-unaligned-access -c -o matmul_vanilla.o matmul_vanilla.c
clang -O2 -Wall -std=c99 --target=aarch64-none-elf -fno-exceptions -fno-rtti -mno-unaligned-access -c -o preprocess_vanilla.o preprocess_vanilla.c
clang -O2 -Wall -std=c99 --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -nostartfiles -lcrt0-semihost -lsemihost -nostartfiles -lcrt0-semihost -lsemihost -Wl,--defsym=__boot_flash=0x80000000 -Wl,--defsym=__flash=0x80001000 -Wl,--defsym=__ram=0x81000000 -T picolibc.ld -o sme2_matmul_asm main_asm.o matmul_asm.o matmul_asm_impl.o preprocess_l_asm.o matmul_vanilla.o preprocess_vanilla.o misc.o
clang -O2 -Wall -std=c99 --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -DBAREMETAL=1 -DIMPL=intr -c -o main_intr.o main.c
clang -O2 -Wall -std=c99 --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -DBAREMETAL=1 -c -o matmul_intr.o matmul_intr.c
clang -O2 -Wall -std=c99 --target=aarch64-none-elf -march=armv9.4-a+sme2 -fno-exceptions -fno-rtti -mno-unaligned-access -nostartfiles -lcrt0-semihost -lsemihost -nostartfiles -lcrt0-semihost -lsemihost -Wl,--defsym=__boot_flash=0x80000000 -Wl,--defsym=__flash=0x80001000 -Wl,--defsym=__ram=0x81000000 -T picolibc.ld -o sme2_matmul_intr main_intr.o matmul_intr.o matmul_vanilla.o preprocess_vanilla.o misc.o
llvm-objdump --demangle -d hello > hello.lst
llvm-objdump --demangle -d sme2_check > sme2_check.lst
llvm-objdump --demangle -d sme2_matmul_asm > sme2_matmul_asm.lst
llvm-objdump --demangle -d sme2_matmul_intr > sme2_matmul_intr.lst
  {{< /tab >}}
{{< /tabpane >}}

The `make` command performs the following tasks:
- It builds four executables: `hello`, `sme2_check`, `sme2_matmul_asm`, and
  `sme2_matmul_intr`.
- It creates the assembly listings for the four executables: `hello.lst`,
  `sme2_check.lst`, `sme2_matmul_asm.lst`, and `sme2_matmul_intr.lst`.

  These targets compile and link all example programs and generate disassembly listings for inspection.

At any point, you can clean the directory of all the files that have been built
by invoking `make clean`:

{{< tabpane code=true >}}
  {{< tab header="Native SME2 support" language="bash" output_lines="2">}}
  make clean
  rm hello sme2_check sme2_matmul_asm sme2_matmul_intr hello.lst sme2_check.lst sme2_matmul_asm.lst sme2_matmul_intr.lst *.o
  {{< /tab >}}

  {{< tab header="Emulated SME2 support" language="bash" output_lines="2">}}
  docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v2 make clean
  rm hello sme2_check sme2_matmul_asm sme2_matmul_intr hello.lst sme2_check.lst sme2_matmul_asm.lst sme2_matmul_intr.lst *.o
  {{< /tab >}}
{{< /tabpane >}}

## Run a Hello World program

The very first program that you should run is the famous "Hello, world!" example
that will tell you if your environment is set up correctly.

The source code is contained in `hello.c` and looks like this:

```C { line_numbers="true" }
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    printf("Hello, world !\n");
    return EXIT_SUCCESS;
}
```

Run the `hello` program with:

{{< tabpane code=true >}}
  {{< tab header="Native SME2 support" language="bash" output_lines="2">}}
  ./hello
  Hello, world !
  {{< /tab >}}

  {{< tab header="Emulated SME2 support" language="bash" output_lines="2-4">}}
  docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v2 ./run-fvp.sh hello
  Hello, world !

  Info: /OSCI/SystemC: Simulation stopped by user.
  {{< /tab >}}
{{< /tabpane >}}

In the emulated case, you may see that the FVP prints out extra lines. The key confirmation is the presence of "Hello, world!" in the output. It demonstrates that the generic code can be compiled and executed.

## Check SME2 availability

You will now run the `sme2_check` program, which verifies that SME2 works as expected. This checks both the compiler and the CPU (or the emulated CPU) are properly supporting SME2.

The `sme2_check` program verifies that SME2 is available and working. It confirms:

* The compiler supports SME2 (via __ARM_FEATURE_SME2)

* The system or emulator reports SME2 capability

* Streaming mode works as expected

The source code is found in `sme2_check.c`:

```C { line_numbers="true" }
#include "misc.h"

#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>

#ifdef __ARM_FEATURE_SME2
#include <arm_sme.h>
#else
#error __ARM_FEATURE_SME2 is not defined
#endif

__arm_locally_streaming void function_in_streaming_mode() {
    printf("In streaming_mode: %d, SVL: %" PRIu64 " bits\n",
           __arm_in_streaming_mode(), svcntb() * 8);
}

int main(int argc, char *argv[]) {

#if BAREMETAL == 1
    setup_sme_baremetal();
#endif

    if (!display_cpu_features()) {
        printf("SME2 is not supported on this CPU.\n");
        exit(EXIT_FAILURE);
    }

    printf("Checking initial in_streaming_mode: %d\n",
           __arm_in_streaming_mode());

    printf("Switching to streaming mode...\n");

    function_in_streaming_mode();

    printf("Switching back from streaming mode...\n");

    printf("Checking in_streaming_mode: %d\n", __arm_in_streaming_mode());

    return EXIT_SUCCESS;
}
```

The ``__ARM_FEATURE_SME2`` macro (line 7) is provided by the compiler when it
targets an SME-capable target, which is specified with the ``+sme2``
architectural feature in ``-march=armv9.4-a+sme2`` (emulated environment) or
``-march=native+sme2`` command line option to ``clang`` in file ``Makefile``.

The ``arm_sme.h`` file included at line 8 is part of the Arm C Library Extension
([ACLE](https://arm-software.github.io/acle/main/)). The ACLE provides types and
function declarations to enable C/C++ programmers to make the best possible use
of the Arm architecture. You can use the SME-related part of the library, but it
does also provide support for Neon or other Arm architectural extensions.

In order to run in a baremetal environment (like the one being used in the
emulated SME2 support), where no operating system has done the setup of the
processor for the user land programs, an additional step is required to turn
SME2 on. This is the purpose of the ``setup_sme_baremetal()`` call at line 21.
In environments where SME2 is natively supported, nothing needs to be done,
which is why the execution of this function is conditioned by the ``BAREMETAL``
macro. ``BAREMETAL`` is set to 1 in the ``Makefile`` when the FVP is targeted,
and set to 0 otherwise. The body of the ``setup_sme_baremetal`` function is
defined in ``misc.c``.

The ``sme2_check`` program then displays whether SVE, SME and SME2 are supported
at line 24. The checking of SVE, SME and SME2 is done differently depending on
``BAREMETAL``. This platform specific behavior is abstracted by the
``display_cpu_features()``:
- In baremetal mode, our program has access to system registers and can inspect system registers for SME2 support. The program will print the SVE field of the ``ID_AA64PFR0_EL1`` system register and the SME field of the ``ID_AA64PFR1_EL1`` system register.
- In non baremetal mode, on an Apple platform the program needs to use a higher
  level API call.

The body of the ``display_cpu_features`` function is defined in ``misc.c``.

If SME2 is not available, ``sme2_check`` will emit a diagnostic message (line
25) and exit (line 26).

``sme2_check`` will then print the initial streaming mode state at line 29
(which is expected to be 0), then will switch to streaming mode (line 34) when
invoking function ``function_in_streaming_mode`` to show the Streaming Vector
Length (a.k.a ``SVL``), and then switch back to non streaming mode (when
returning from ``function_in_streaming_mode``). Function
``function_in_streaming_mode`` is defined at line 13. Note that it has been
annotated with the ``__arm_locally_streaming`` attribute, which instructs the
compiler to automatically switch to streaming mode when invoking this function.
Streaming mode will be discussed in more depth in the next section.

Look for the following confirmation messages in the output:

{{< tabpane code=true >}}
  {{< tab header="Native SME2 support" language="bash" output_lines="2-9">}}
  ./sme2_check
  HAS_SVE: 0
  HAS_SME: 1
  HAS_SME2: 1
  Checking initial in_streaming_mode: 0
  Switching to streaming mode...
  In streaming_mode: 1, SVL: 512 bits
  Switching back from streaming mode...
  Checking in_streaming_mode: 0
  {{< /tab >}}

  {{< tab header="Emulated SME2 support" language="bash" output_lines="2-12">}}
  docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v2 ./run-fvp.sh sme2_check
  ID_AA64PFR0_EL1     : 0x1101101131111112
    - SVE       : 0x00000001
  ID_AA64PFR1_EL1     : 0x0000101002000001
    - SME       : 0x00000002
  Checking has_sme: 1
  Checking initial in_streaming_mode: 0
  Switching to streaming mode...
  In streaming_mode: 1, SVL: 512 bits
  Switching back from streaming mode...
  Checking in_streaming_mode: 0

  Info: /OSCI/SystemC: Simulation stopped by user.
  {{< /tab >}}
{{< /tabpane >}}

You've now confirmed that your environment can compile and run SME2 code, and that SME2 features like streaming mode are working correctly. You're ready to continue to the next section and start working with SME2 in practice.
