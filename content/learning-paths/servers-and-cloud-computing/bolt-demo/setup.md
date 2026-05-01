---
title: Prepare your environment
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Set up your environment
On your AArch64 Linux machine, navigate to your home directory (or another empty working directory) and download the `bsort.cpp` source file:

```bash
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/servers-and-cloud-computing/bolt-demo/bsort.cpp
```

The [Why Bubble Sort?](#why-bubble-sort) section explains why BubbleSort is used as the demonstration workload.

Create the following directories to organize generated files from this example:
```bash
mkdir -p out prof heatmap
```
- **out**: Stores output binaries
- **prof**: Stores profile data
- **heatmap**: Stores heatmap visualizations and related metrics

## Compile the input program {#compile}
Next, compile the input program.  
Because BOLT and other profile-guided optimization pipelines often involve multiple build stages, you will refer to this initial binary as the **stage-0 binary**.

For this example, you must preserve the original function order from the source file. 
Small programs like this one are simple enough that modern compilers may reorder functions automatically to improve instruction locality, even without profile data. That behavior rarely affects large real-world applications, but it can occur in this example. To ensure the program retains its intentionally poor layout, pass specific options to the compiler and linker.

BOLT works with both LLVM and GNU toolchains.
GNU (gcc) provides a flag that preserves the original order: `-fno-toplevel-reorder`.  
LLVM Clang does not provide an equivalent flag, so it relies on a symbol ordering file that explicitly defines the initial function layout. Using a file editor of your choice copy the contents below into a file named `orderfile.txt`. 
```txt
_ZL5swap1PiS_
_ZL10cold_func1v
_ZL5swap2PiS_
_ZL10cold_func2v
_ZL5swap3PiS_
_ZL10cold_func3v
_ZL5swap4PiS_
_ZL10cold_func4v
_ZL5swap5PiS_
_ZL10cold_func5v
```

Both approaches to compile the binary are shown. Compile with your preferred toolchain, and ensure that relocations are enabled.
You will look at why relocations matter [later](#why-relocations) in this Learning Path.

{{< tabpane code=true >}}
  {{< tab header="GNU" language="bash">}}
gcc bsort.cpp -o out/bsort -O3 -Wl,--emit-relocs -fno-toplevel-reorder
  {{< /tab >}}
  {{< tab header="LLVM" language="bash">}}
clang bsort.cpp -o out/bsort -O3 -fuse-ld=lld -ffunction-sections -Wl,--emit-relocs -Wl,--symbol-ordering-file=orderfile.txt
  {{< /tab >}}
{{< /tabpane >}}

## Verify the function order
Verify that the compiler preserved the intended function order by inspecting the symbols in the `.text` section of the binary.
Run the following command:

{{< tabpane code=true >}}
  {{< tab header="GNU" language="bash" output_lines="2-13">}}
  objdump --syms --demangle out/bsort | grep ".text" | grep ")" | sort
    0000000000014000 l     F .text  0000000000000e4c              swap1(int*, int*)
    0000000000018000 l     F .text  0000000000000008              cold_func1()
    0000000000018008 l     F .text  0000000000000e4c              swap2(int*, int*)
    000000000001c000 l     F .text  0000000000000008              cold_func2()
    000000000001c008 l     F .text  0000000000000e4c              swap3(int*, int*)
    0000000000020000 l     F .text  0000000000000008              cold_func3()
    0000000000020008 l     F .text  0000000000000e4c              swap4(int*, int*)
    0000000000024000 l     F .text  0000000000000008              cold_func4()
    0000000000024008 l     F .text  0000000000000e4c              swap5(int*, int*)
    0000000000028000 l     F .text  0000000000000008              cold_func5()
    0000000000028158 g     F .text  00000000000000c0              bubble_sort(int*, int)
    0000000000028218 g     F .text  00000000000000d8              sort_array(int*)
  {{< /tab >}}
  {{< tab header="LLVM" language="bash" output_lines="2-13">}}
  llvm-objdump --syms --demangle out/bsort | grep ".text" | grep ")" | sort
    0000000000014000 l     F .text  0000000000000e4c swap1(int*, int*)
    0000000000018000 l     F .text  0000000000000008 cold_func1()
    0000000000018008 l     F .text  0000000000000e4c swap2(int*, int*)
    000000000001c000 l     F .text  0000000000000008 cold_func2()
    000000000001c008 l     F .text  0000000000000e4c swap3(int*, int*)
    0000000000020000 l     F .text  0000000000000008 cold_func3()
    0000000000020008 l     F .text  0000000000000e4c swap4(int*, int*)
    0000000000024000 l     F .text  0000000000000008 cold_func4()
    0000000000024008 l     F .text  0000000000000e4c swap5(int*, int*)
    0000000000028000 l     F .text  0000000000000008 cold_func5()
    0000000000028158 g     F .text  00000000000000c0 bubble_sort(int*, int)
    0000000000028218 g     F .text  00000000000000d8 sort_array(int*)
  {{< /tab >}}
{{< /tabpane >}}

The output should show the **swap** and **cold** functions interleaved.  
This layout matches the order in the source file and creates poor instruction locality, which makes the program a good candidate for BOLT optimization.

## Verify the presence of relocations
Verify that the binary contains relocation information.  
BOLT relies on relocation records to safely modify the binary layout after linking.

Check the ELF section table and confirm that relocation sections such as `.rela.text` appear in the output.

{{< tabpane code=true >}}
  {{< tab header="GNU" language="bash" output_lines="2-13">}}
    readelf -S out/bsort | grep .rel
        [ 9] .rela.dyn         RELA             0000000000000520  00000520
        [10] .rela.plt         RELA             0000000000000658  00000658
        [20] .data.rel.ro      PROGBITS         0000000000038560  00018560
        [23] .relro_padding    NOBITS           0000000000038750  00018750
        [28] .rela.text        RELA             0000000000000000  000187b8
        [29] .rela.eh_frame    RELA             0000000000000000  00018ea8
        [30] .rela.init        RELA             0000000000000000  00019058
        [31] .rela.data        RELA             0000000000000000  00019070
        [32] .rela.fini_array  RELA             0000000000000000  00019088
        [33] .rela.init_array  RELA             0000000000000000  000190a0
        [35] .rela.data.rel.ro RELA             0000000000000000  00019158
  {{< /tab >}}
  {{< tab header="LLVM" language="bash" output_lines="2-12">}}
    llvm-readelf -S out/bsort | grep .rel
        [ 9] .rela.dyn         RELA            0000000000000520 000520 000138 18   A  4   0  8
        [10] .rela.plt         RELA            0000000000000658 000658 0000c0 18  AI  4  26  8
        [20] .data.rel.ro      PROGBITS        0000000000038560 018560 000028 00  WA  0   0  8
        [23] .relro_padding    NOBITS          0000000000038750 018750 0008b0 00  WA  0   0  1
        [28] .rela.text        RELA            0000000000000000 0187b8 0006f0 18   I 36  14  8
        [29] .rela.eh_frame    RELA            0000000000000000 018ea8 0001b0 18   I 36  12  8
        [30] .rela.init        RELA            0000000000000000 019058 000018 18   I 36  15  8
        [31] .rela.data        RELA            0000000000000000 019070 000018 18   I 36  24  8
        [32] .rela.fini_array  RELA            0000000000000000 019088 000018 18   I 36  18  8
        [33] .rela.init_array  RELA            0000000000000000 0190a0 000018 18   I 36  19  8
        [35] .rela.data.rel.ro RELA            0000000000000000 019158 000078 18   I 36  20  8
  {{< /tab >}}
{{< /tabpane >}}

Look for relocation sections such as **`.rela.text`** in the output. Their presence confirms that the linker preserved relocation information required by BOLT.

## Why relocations are important {#why-relocations}
BOLT uses relocation records to update references after it changes the code layout. When BOLT reorders functions or basic blocks, it must update addresses used by instructions such as calls, branches, and references to code or data. Relocation records identify these locations in the binary so that BOLT can safely rewrite them.
Without relocations, BOLT cannot reliably adjust these references. As a result, many optimizations become unavailable. For example, BOLT disables function reordering when relocation information is missing, which prevents most code layout optimizations.

Because BOLT operates on fully linked binaries, it must modify addresses that the linker already resolved. Relocations preserve the information needed to update those addresses correctly.

## Why Bubble Sort?
Bubble Sort is a simple program with all the code in one file. The program has no external dependencies, and runs in a few seconds under instrumentation with a small, fixed workload.
In its original form, the program does not benefit much from code layout optimization. To create a more interesting example, instruction locality is intentionally reduced.
We introduce **cold code paths** between frequently executed code. These cold blocks separate hot instructions in memory and degrade spatial locality. BOLT later improves performance by reorganizing the binary so that hot code paths appear closer together.

The code below shows how the program was modified to reduce code locality.

The main sort function rotates through five copies of the swap function. Each time the algorithm performs a swap, it selects the next swap implementation in a round-robin fashion.
```cpp  { line_numbers=true linenos=table line_start=48 }
void bubble_sort(int *a, int n) {
    if (n <= 1)
        return;

    int end = n - 1;
    int swapped = 1;
    unsigned idx = 0;

    while (swapped && end > 0) {
        swapped = 0;
        // pick a different copy of the swap function, in a round-robin fashion
        // and call it.
        for (int i = 1; i <= end; ++i) {
            if (a[i] < a[i - 1]) {
                auto swap_func = swap_funcs[idx++];
                idx %= FUNC_COPIES;
                swap_func(&a[i - 1], &a[i]);
                swapped = 1;
            }
        }
        --end;
    }
}
```
Each swap function is defined using a macro and contains a small cold path that includes several nop instructions.

```cpp  { line_numbers=true linenos=table line_start=18 }
#define SWAP_FUNC(ID) \
    static __attribute__((noinline)) \
    void swap##ID(int *left, int *right) { \
        if (COND()) NOPS(300); \
        int tmp = *left; \
        if (COND()) NOPS(300); else *left = *right; \
        if (COND()) NOPS(300); else *right = tmp; \
    }
```

To further reduce code locality, we place larger cold functions between frequently executed functions. These cold functions occupy space in the instruction layout and push hot code farther apart in memory.
We define these cold functions using a macro. Each function contains only a nop instruction and does not participate in the program’s hot execution path.
```cpp  { line_numbers=true linenos=table line_start=28 }
#define COLD_FUNC(ID) \
    static __attribute__((noinline, aligned(16384), used)) \
    void cold_func##ID(void) { \
        asm volatile("nop"); \
    }
```

We use the above two macros to interleave the hot and cold functions in the binary.
Locality is reduced because each call uses a different swap function with large cold code regions placed between them.
```cpp  { line_numbers=true linenos=table line_start=35 }
SWAP_FUNC(1) COLD_FUNC(1)
SWAP_FUNC(2) COLD_FUNC(2)
SWAP_FUNC(3) COLD_FUNC(3)
SWAP_FUNC(4) COLD_FUNC(4)
SWAP_FUNC(5) COLD_FUNC(5)
```

## What you've learned and what's next

You've compiled the BubbleSort example program with intentionally poor code locality and verified that the binary contains the necessary relocation information. The program is now ready for profiling and optimization.

Next, you'll learn how to identify whether this program is a good candidate for BOLT optimization by analyzing its performance metrics.
