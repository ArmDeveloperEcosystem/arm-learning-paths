---
title: Setup and Input
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---


### Environment setup
On your AArch64 Linux bare-metal instance, navigate to your home directory (or another empty working directory) and create a file named `bsort.cpp` with the following content:

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_LEN 10000
#define FUNC_COPIES 5
volatile bool Cond = false;
#define COND() (__builtin_expect(Cond, true))

#define NOPS(N) \
  asm volatile( \
      ".rept %0\n" \
      "nop\n" \
      ".endr\n" \
      : : "i"(N) : "memory")

// Swap functionality plus some cold blocks.
#define SWAP_FUNC(ID) \
    static __attribute__((noinline)) \
    void swap##ID(int *left, int *right) { \
        if (COND()) NOPS(300); \
        int tmp = *left; \
        if (COND()) NOPS(300); else *left = *right; \
        if (COND()) NOPS(300); else *right = tmp; \
    }

// Aligned at 16KiB
#define COLD_FUNC(ID) \
    static __attribute__((noinline, aligned(16384), used)) \
    void cold_func##ID(void) { \
        asm volatile("nop"); \
    }

// Create copies of swap, and interleave with big chunks of cold code.
SWAP_FUNC(1) COLD_FUNC(1)
SWAP_FUNC(2) COLD_FUNC(2)
SWAP_FUNC(3) COLD_FUNC(3)
SWAP_FUNC(4) COLD_FUNC(4)
SWAP_FUNC(5) COLD_FUNC(5)

typedef void (*swap_fty)(int *, int *);
static swap_fty const swap_funcs[FUNC_COPIES] = {
    swap1, swap2, swap3, swap4, swap5
};


/* Sorting Logic */
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

void sort_array(int *data) {
    for (int i = 0; i < ARRAY_LEN; ++i) {
        data[i] = rand();
    }
    bubble_sort(data, ARRAY_LEN);
}

/* Timers, helpers, and main */
static struct timespec timer_start;
static inline void start_timer(void) {
    clock_gettime(CLOCK_MONOTONIC, &timer_start);
}

static inline void stop_timer(void) {
    struct timespec timer_end;
    clock_gettime(CLOCK_MONOTONIC, &timer_end);
    long long ms = (timer_end.tv_sec - timer_start.tv_sec) * 1000LL +
                   (timer_end.tv_nsec - timer_start.tv_nsec) / 1000000LL;
    printf("%lld ms ", ms);
}

static void print_first_last(const int *data, int n) {
    if (n <= 0)
        return;

    const int first = data[0];
    const int last = data[n - 1];
    printf("(first=%d last=%d)\n", first, last);
}

int main(void) {
    srand(0);
    printf("Bubble sorting %d elements\n", ARRAY_LEN);
    int data[ARRAY_LEN];

    start_timer();
    sort_array(data);
    stop_timer();

    print_first_last(data, ARRAY_LEN);
    return 0;
}
```

The [last section](#why-bubble-sort) explains why this tutorial uses BubbleSort as the demonstration workload.

Create the following directories to organize generated files from this example:
```bash
mkdir -p out prof heatmap
```
- **out**: Stores output binaries
- **prof**: Stores profile data
- **heatmap**: Stores heatmap visualizations and related metrics

### Compile the input program {#compile}
Next, compile the input program.  
Because BOLT and other profile-guided optimization pipelines often involve multiple build stages, you will refer to this initial binary as the **stage-0 binary**.

For this example, you must preserve the original function order from the source file. 
Small programs like this one are simple enough that modern compilers may reorder functions automatically to improve instruction locality, even without profile data. That behavior rarely affects large real-world applications, but it can occur in this example. To ensure the program retains its intentionally poor layout, pass specific options to the compiler and linker.

BOLT works with both LLVM and GNU toolchains.
GNU (gcc) provides a flag that preserves the original order: `-fno-toplevel-reorder`.  
LLVM Clang does not provide an equivalent flag, so it relies on a symbol ordering file that explicitly defines the initial function layout. You can find the file used in this tutorial here: 
You can find this file here: [orderfile.txt](../orderfile.txt).

Both approaches are shown below.
Compile with your preferred toolchain, and ensure that relocations are enabled.
We explain why they matter [later](#why-relocations) in this tutorial.

{{< tabpane code=true >}}
  {{< tab header="GNU" language="bash">}}
mkdir -p out
gcc bsort.cpp -o out/bsort -O3 -Wl,--emit-relocs -fno-toplevel-reorder
  {{< /tab >}}
  {{< tab header="LLVM" language="bash">}}
mkdir -p out
clang bsort.cpp -o out/bsort -O3 -fuse-ld=lld -ffunction-sections -Wl,--emit-relocs -Wl,--symbol-ordering-file=orderfile.txt
  {{< /tab >}}
{{< /tabpane >}}

### Verify the function order
We now verify that the compiler preserved the original function order.
We do this by inspecting the symbols in the `.text` section.
The output should list the swap and cold functions interleaved, matching their order in the source file.

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


### Verify the presence of relocations
We now verify that the binary includes relocations.
This can be seen by checking for `.rel*.*` entries in the section table, such as `.rela.text`.

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


### Why relocations are important {#why-relocations}
BOLT relies on relocations to update references after it changes the code layout.
Without relocations, BOLT is severely limited. For example, function reordering is disabled, which makes code layout optimizations ineffective.

Because BOLT runs post-link, it may need to adjust locations that the linker patched in the original binary.
Relocations describe these locations, so they must be preserved for BOLT to be able to apply its full set of layout optimizations.


### Why Bubble Sort?
Bubble Sort keeps this tutorial simple.
The code is in one file, has no external dependencies, and runs in a few seconds under instrumentation with a small, fixed workload.
In its original form it is not a good candidate for code layout optimization.
To make it one, we add **cold code** blocks between hot paths.
This reduces code locality, which BOLT improves later.

The code below shows the changes we introduced to reduce code locality.

The main sort function is shown below. It rotates through 5 copies of the swap function, selecting a different one each time a swap is performed.
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

Each swap function is defined using a macro and includes some nop instructions on a cold path.
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

To further reduce code locality, we place larger cold functions between hot ones.
These cold functions are also defined using a macro and consist entirely of nop instructions.
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
