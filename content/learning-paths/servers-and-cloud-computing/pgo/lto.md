---
title: Build with LTO
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is LTO?

Link-Time Optimization (LTO) enables optimization across source file boundaries during the link stage. Without LTO, the compiler optimizes each source file independently before the linker combines the resulting object files. As a result, the optimizer cannot make optimization decisions based on the whole program.

For more information, see the [LLVM Link Time Optimization](https://llvm.org/docs/LinkTimeOptimization.html) design documentation.

## Full vs Thin-LTO

LLVM supports two main LTO modes: Full-LTO and Thin-LTO.

Both modes make Clang emit LLVM bitcode during compilation. The difference is how LLVM performs optimization during the link stage.

Full-LTO merges all input bitcode into a single LLVM module. LLVM then optimizes the program as a single unit before generating native code.
This gives the optimizer a complete view of the program, but it can increase link time and memory usage.

Thin-LTO keeps the build more scalable. Each compiled module includes a compact summary. During the link stage, LLVM combines these summaries into a global index, determines which functions to import across module boundaries, and then optimizes each module in parallel.
Thin-LTO also supports incremental builds by caching compilation results and rebuilding only the modules whose generated code changes.

## Build with LTO

LTO is disabled by default. Use `-flto=full` to enable Full-LTO or `-flto=thin` to enable Thin-LTO.
If you specify `-flto` without a value, Clang uses Full-LTO. The following commands use `-fuse-ld=lld` to select the LLVM linker.

{{< tabpane code=true >}}
  {{< tab header="Full-LTO" language="bash">}}
clang -O3 -flto=full -c bsort.cpp -o out/bsort.lto.full.o
clang -O3 -flto=full -fuse-ld=lld out/bsort.lto.full.o -o out/bsort.lto.full
  {{< /tab >}}
  {{< tab header="Thin-LTO" language="bash">}}
clang -O3 -flto=thin -c bsort.cpp -o out/bsort.lto.thin.o
clang -O3 -flto=thin -fuse-ld=lld out/bsort.lto.thin.o -o out/bsort.lto.thin
  {{< /tab >}}
{{< /tabpane >}}


## Verify the LTO object files

Use the bitcode analyzer (`llvm-bcanalyzer`) on an object file to verify that it contains LLVM bitcode and to identify the LTO mode.
For Thin-LTO, look for `GLOBALVAL_SUMMARY_BLOCK`. For Full-LTO, look for `FULL_LTO_GLOBALVAL_SUMMARY_BLOCK`.

{{< tabpane code=true >}}
  {{< tab header="Full-LTO" language="bash" output_lines="2-4">}}
llvm-bcanalyzer -dump bsort.lto.full.o | grep 'SUMMARY_BLOCK'
  <FULL_LTO_GLOBALVAL_SUMMARY_BLOCK NumWords=56 BlockCodeSize=4>
  </FULL_LTO_GLOBALVAL_SUMMARY_BLOCK>
  Block ID #24 (FULL_LTO_GLOBALVAL_SUMMARY_BLOCK):
  {{< /tab >}}
  {{< tab header="Thin-LTO" language="bash" output_lines="2-4">}}
llvm-bcanalyzer -dump bsort.lto.thin.o | grep 'SUMMARY_BLOCK'
  <GLOBALVAL_SUMMARY_BLOCK NumWords=56 BlockCodeSize=4>
  </GLOBALVAL_SUMMARY_BLOCK>
  Block ID #20 (GLOBALVAL_SUMMARY_BLOCK):
  {{< /tab >}}
  {{< tab header="No LTO" language="bash" output_lines="2">}}
llvm-bcanalyzer -dump bsort.nolto.o
llvm-bcanalyzer: Invalid record at top-level
  {{< /tab >}}
{{< /tabpane >}}

## What you've learned and what's next

You've built the example with Full-LTO and Thin-LTO and verified that each build uses the expected LTO mode.

Next, you'll collect sampled profile data and use it to build the application with S-PGO and Thin-LTO.
