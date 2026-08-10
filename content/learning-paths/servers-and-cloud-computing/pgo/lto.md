---
title: Build AArch64 code with LTO
description: Build and verify Full-LTO and Thin-LTO AArch64 binaries with Clang, then inspect their LLVM bitcode.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What LTO is

Link-Time Optimization (LTO) enables optimization across source file boundaries during the link stage. Without LTO, the compiler optimizes each source file independently before the linker combines the resulting object files. As a result, the optimizer can't make optimization decisions based on the whole program.

For more information, see the [LLVM Link Time Optimization](https://llvm.org/docs/LinkTimeOptimization.html) design documentation.

## Compare Full-LTO and Thin-LTO

LLVM supports two main LTO modes: Full-LTO and Thin-LTO.

Both modes make Clang emit LLVM bitcode during compilation. The difference is how LLVM performs optimization during the link stage.

Full-LTO merges all input bitcode into a single LLVM module. LLVM then optimizes the program as one unit before generating native code. This gives the optimizer a complete view of the program, but it can increase link time and memory usage.

Thin-LTO keeps the build more scalable. Each compiled module includes a compact summary. During the link stage, LLVM combines these summaries into a global index and determines which functions to import across module boundaries. LLVM then optimizes each module in parallel.
Thin-LTO also supports incremental builds by caching compilation results and rebuilding only the modules whose generated code changes.

## Build with LTO

LTO is disabled by default. Use `-flto=full` to enable Full-LTO or `-flto=thin` to enable Thin-LTO. If you specify `-flto` without a value, Clang uses Full-LTO.

Build the example in each mode. Pass the same LTO option during compilation and linking. The `-fuse-ld=lld` option selects the LLVM linker:

{{< tabpane code=true >}}
  {{< tab header="Full-LTO" language="bash">}}
clang++ -O3 -flto=full -c bsort.cpp -o out/bsort.lto.full.o
clang++ -O3 -flto=full -fuse-ld=lld out/bsort.lto.full.o -o out/bsort.lto.full
  {{< /tab >}}
  {{< tab header="Thin-LTO" language="bash">}}
clang++ -O3 -flto=thin -c bsort.cpp -o out/bsort.lto.thin.o
clang++ -O3 -flto=thin -fuse-ld=lld out/bsort.lto.thin.o -o out/bsort.lto.thin
  {{< /tab >}}
{{< /tabpane >}}


## Verify the LTO object files

Use `llvm-bcanalyzer` on each object file to verify that it contains LLVM bitcode and identify its LTO mode. Thin-LTO bitcode contains a `GLOBALVAL_SUMMARY_BLOCK`. Full-LTO bitcode contains a `FULL_LTO_GLOBALVAL_SUMMARY_BLOCK`.

{{< tabpane code=true >}}
  {{< tab header="Full-LTO" language="bash" output_lines="2-4">}}
llvm-bcanalyzer -dump out/bsort.lto.full.o | grep 'SUMMARY_BLOCK'
  <FULL_LTO_GLOBALVAL_SUMMARY_BLOCK NumWords=56 BlockCodeSize=4>
  </FULL_LTO_GLOBALVAL_SUMMARY_BLOCK>
  Block ID #24 (FULL_LTO_GLOBALVAL_SUMMARY_BLOCK):
  {{< /tab >}}
  {{< tab header="Thin-LTO" language="bash" output_lines="2-4">}}
llvm-bcanalyzer -dump out/bsort.lto.thin.o | grep 'SUMMARY_BLOCK'
  <GLOBALVAL_SUMMARY_BLOCK NumWords=56 BlockCodeSize=4>
  </GLOBALVAL_SUMMARY_BLOCK>
  Block ID #20 (GLOBALVAL_SUMMARY_BLOCK):
  {{< /tab >}}
{{< /tabpane >}}

The block names confirm that Clang created the expected type of LTO bitcode. Run both linked binaries to check that they complete successfully:

```bash
./out/bsort.lto.full
./out/bsort.lto.thin
```

## What you've accomplished and what's next

You've now built and run the example with Full-LTO and Thin-LTO. You've also inspected the object files to verify each LTO mode.

Next, you'll collect sampled profile data and use it to build the application with S-PGO and Thin-LTO.
