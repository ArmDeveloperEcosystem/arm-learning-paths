---
title: Test your SME2 development environment
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll verify that your environment is ready for SME2
development. This is your first hands-on task and confirms that the toolchain,
hardware (or emulator), and compiler are set up correctly.

## Build the code examples

Make sure your current working directory is `code-examples/learning-paths/cross-platform/multiplying-matrices-with-sme2`.

Use the `cmake` command to configure the project. Note that for native builds,
you may have (as shown in the example) to tell `cmake` which `clang` to use as
it would otherwise find the default one from the system (which might not be
suitable). If you system `clang` is recent enough, omit the `CC=...`
part of the `cmake` invocation.

{{< tabpane code=true >}}

{{< tab header="Native SME2 support" language="bash" output_lines="2-12">}}
CC=/opt/homebrew/Cellar/llvm/21.1.4/bin/clang cmake -G Ninja -S . -B build-native -DCMAKE_BUILD_TYPE:STRING=Release
-- The C compiler identification is Clang 21.1.4
-- The ASM compiler identification is Clang with GNU-like command-line
-- Found assembler: /opt/homebrew/Cellar/llvm/21.1.4/bin/clang
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /opt/homebrew/Cellar/llvm/21.1.4/bin/clang - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Configuring done (0.8s)
-- Generating done (0.0s)
-- Build files have been written to: .../multiplying-matrices-with-sme2/build-native
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash" output_lines="2-12">}}
cmake -G Ninja  -S . -B build-android -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_TOOLCHAIN_FILE:STRING="$NDK/build/cmake/android.toolchain.cmake" -DANDROID_ABI:STRING=arm64-v8a -DANDROID_PLATFORM:STRING=android-24 -DANDROID_STL:STRING=c++_static -DCMAKE_BUILD_TYPE:STRING=Release
-- The C compiler identification is Clang 21.0.0
-- The ASM compiler identification is Clang with GNU-like command-line
-- Found assembler: .../Library/Android/sdk/ndk/29.0.14206865/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: .../Library/Android/sdk/ndk/29.0.14206865/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Configuring done (1.1s)
-- Generating done (0.0s)
-- Build files have been written to: .../multiplying-matrices-with-sme2/build-android
{{< /tab >}}

{{< tab header="Emulated SME2 support" language="bash" output_lines="2-19">}}
docker run --rm -v "$PWD:/work" armswdev/sme2-learning-path:sme2-environment-v3 cmake -G Ninja -S . -B build-baremetal -DCMAKE_TOOLCHAIN_FILE:STRING=cmake/baremetal-toolchain.cmake -DCMAKE_BUILD_TYPE:STRING=Release
-- Using ATfE from: /tools/ATfE-21.1.1-Linux-AArch64
-- Using ATfE from: /tools/ATfE-21.1.1-Linux-AArch64
-- The C compiler identification is Clang 21.1.1
-- The ASM compiler identification is Clang with GNU-like command-line
-- Found assembler: /tools/ATfE-21.1.1-Linux-AArch64/bin/clang
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /tools/ATfE-21.1.1-Linux-AArch64/bin/clang - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Configuring done (0.3s)
-- Generating done (0.0s)
-- Build files have been written to: /work/build-baremetal
{{< /tab >}}

{{< /tabpane >}}

Then build all the examples with `ninja`:

{{< tabpane code=true >}}

{{< tab header="Native SME2 support" language="bash" output_lines="2-3">}}
ninja -C build-native/
ninja: Entering directory `build-native/'
[19/19] Linking C executable sme2_matmul_intr
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash" output_lines="2-3">}}
ninja -C build-android/
ninja: Entering directory `build-android/'
[19/19] Linking C executable sme2_matmul_asm
{{< /tab >}}

{{< tab header="Emulated SME2 support" language="bash" output_lines="2-21">}}
docker run --rm -v "$PWD:/work" armswdev/sme2-learning-path:sme2-environment-v3 ninja -C build-baremetal/
ninja: Entering directory `build-baremetal/'
[1/19] Building ASM object CMakeFiles/sme2_matmul_asm.dir/preprocess_l_asm.S.obj
[2/19] Building ASM object CMakeFiles/sme2_matmul_asm.dir/matmul_asm_impl.S.obj
[3/19] Building C object CMakeFiles/hello.dir/hello.c.obj
[4/19] Building C object CMakeFiles/sme2_matmul_asm.dir/matmul_vanilla.c.obj
[5/19] Building C object CMakeFiles/sme2_matmul_asm.dir/preprocess_vanilla.c.obj
[6/19] Building C object CMakeFiles/sme2_matmul_intr.dir/matmul_vanilla.c.obj
[7/19] Building C object CMakeFiles/sme2_matmul_intr.dir/preprocess_vanilla.c.obj
[8/19] Linking C executable hello
[9/19] Building C object CMakeFiles/sme2_matmul_asm.dir/matmul_asm.c.obj
[10/19] Building C object CMakeFiles/sme2_check.dir/sme2_check.c.obj
[11/19] Building C object CMakeFiles/sme2_matmul_intr.dir/main.c.obj
[12/19] Building C object CMakeFiles/sme2_matmul_asm.dir/main.c.obj
[13/19] Building C object CMakeFiles/sme2_check.dir/misc.c.obj
[14/19] Building C object CMakeFiles/sme2_matmul_asm.dir/misc.c.obj
[15/19] Building C object CMakeFiles/sme2_matmul_intr.dir/misc.c.obj
[16/19] Building C object CMakeFiles/sme2_matmul_intr.dir/matmul_intr.c.obj
[17/19] Linking C executable sme2_check
[18/19] Linking C executable sme2_matmul_asm
[19/19] Linking C executable sme2_matmul_intr
{{< /tab >}}

{{< /tabpane >}}

The `ninja` command performs the following tasks:
- It builds four executables: `hello`, `sme2_check`, `sme2_matmul_asm`, and
  `sme2_matmul_intr`.
- It creates the assembly listings for the four executables: `hello.lst`,
  `sme2_check.lst`, `sme2_matmul_asm.lst`, and `sme2_matmul_intr.lst`.


At any point, you can clean the directory of all the files that have been built
by invoking `ninja` with the `clean` target:

{{< tabpane code=true >}}

{{< tab header="Native SME2 support" language="bash" output_lines="2-4">}}
ninja -C build-native/ clean
ninja: Entering directory `build-native'
[1/1] Cleaning all built files...
Cleaning... 19 files.
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash" output_lines="2-4">}}
ninja -C build-android/ clean
ninja: Entering directory `build-android/'
[1/1] Cleaning all built files...
Cleaning... 19 files.
{{< /tab >}}

{{< tab header="Emulated SME2 support" language="bash" output_lines="2-4">}}
docker run --rm -v "$PWD:/work" armswdev/sme2-learning-path:sme2-environment-v3 ninja -C build-baremetal/ clean
ninja: Entering directory `build-baremetal/'
[1/1] Cleaning all built files...
Cleaning... 19 files.
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
./build-native/hello
Hello, world !
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash" output_lines="2,5">}}
adb push build-android/hello /data/local/tmp
build-android/hello: 1 file pushed, 0 skipped. 14.6 MB/s (7544 bytes in 0.000s)
adb shell chmod 755 /data/local/tmp/hello
adb shell /data/local/tmp/hello
Hello, world !
{{< /tab >}}

{{< tab header="Emulated SME2 support" language="bash" output_lines="2-4">}}
docker run --rm -v "$PWD:/work" armswdev/sme2-learning-path:sme2-environment-v3 ./run-fvp.sh build-baremetal/hello
Hello, world !

Info: /OSCI/SystemC: Simulation stopped by user.
{{< /tab >}}

{{< /tabpane >}}

In the emulated case, you will notice that the FVP prints out extra lines. The key confirmation is the presence of "`Hello, world!`" in the output: it demonstrates that the generic code can be compiled and executed.

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

The `__ARM_FEATURE_SME2` macro (line 7) is provided by the compiler when it
targets an SME-capable target, which is specified with the `+sme2`
architectural feature in `-march=armv9.4-a+sme2` (emulated environment) or
`-march=native+sme2` command line option to `clang` in the `CMakeLists.txt`
(or in `cmake/baremetal-toolchain.cmake` for the emulated SME2 case).

The `arm_sme.h` file included at line 8 is part of the Arm C Library Extension
([ACLE](https://arm-software.github.io/acle/main/)). The ACLE provides types and
function declarations to enable C/C++ programmers to make the best possible use
of the Arm architecture. You can use the SME-related part of the library, but it
does also provide support for Neon or other Arm architectural extensions.

In order to run in a baremetal environment (like the one being used in the
emulated SME2 support), where no operating system has done the setup of the
processor for the user land programs, an additional step is required to turn
SME2 on. This is the purpose of the `setup_sme_baremetal()` call at line 21.
In environments where SME2 is natively supported, nothing needs to be done,
which is why the execution of this function is conditioned by the `BAREMETAL`
macro. `BAREMETAL` is set to 1 in the `cmake/baremetal-toolchain.cmake` when the FVP is targeted,
and set to 0 otherwise. The body of the `setup_sme_baremetal` function is
defined in `misc.c`.

The `sme2_check` program then displays whether SVE, SME and SME2 are supported
at line 24. The checking of SVE, SME and SME2 is done differently depending on
`BAREMETAL`. This platform specific behavior is abstracted by the
`display_cpu_features()`:
- In baremetal mode, our program has access to system registers and can inspect system registers for SME2 support. The program will print the SVE field of the `ID_AA64PFR0_EL1` system register and the SME field of the `ID_AA64PFR1_EL1` system register.
- In non baremetal mode, on an Apple platform the program needs to use a higher
  level API call.

The body of the `display_cpu_features` function is defined in `misc.c`.

If SME2 is not available, `sme2_check` will emit a diagnostic message (line
25) and exit (line 26).

`sme2_check` will then print the initial streaming mode state at line 29
(which is expected to be 0), then will switch to streaming mode (line 34) when
invoking function `function_in_streaming_mode` to show the Streaming Vector
Length (a.k.a `SVL`), and then switch back to non streaming mode (when
returning from `function_in_streaming_mode`). Function
`function_in_streaming_mode` is defined at line 13. Note that it has been
annotated with the `__arm_locally_streaming` attribute, which instructs the
compiler to automatically switch to streaming mode when invoking this function.
Streaming mode will be discussed in more depth in the next section.

Look for the following confirmation messages in the output:

{{< tabpane code=true >}}

{{< tab header="Native SME2 support" language="bash" output_lines="2-9">}}
./build-native/sme2_check
HAS_SVE: 0
HAS_SME: 1
HAS_SME2: 1
Checking initial in_streaming_mode: 0
Switching to streaming mode...
In streaming_mode: 1, SVL: 512 bits
Switching back from streaming mode...
Checking in_streaming_mode: 0
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash" output_lines="2,5-12">}}
adb push build-android/sme2_check /data/local/tmp
build-android/sme2_check: 1 file pushed, 0 skipped. 29.7 MB/s (19456 bytes in 0.001s)
adb shell chmod 755 /data/local/tmp/sme2_check
adb shell /data/local/tmp/sme2_check
HAS_SVE: 1
HAS_SME: 1
HAS_SME2: 1
Checking initial in_streaming_mode: 0
Switching to streaming mode...
In streaming_mode: 1, SVL: 512 bits
Switching back from streaming mode...
Checking in_streaming_mode: 0
{{< /tab >}}

{{< tab header="Emulated SME2 support" language="bash" output_lines="2-13">}}
docker run --rm -v "$PWD:/work" armswdev/sme2-learning-path:sme2-environment-v3 ./run-fvp.sh build-baremetal/sme2_check
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
