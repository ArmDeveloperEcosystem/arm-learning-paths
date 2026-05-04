---
title: Benchmark and analyze the results
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Compare the results

Your numbers will vary by processor. Compare against the two baselines you recorded earlier:

| Implementation | Approx. throughput | Speedup vs. scalar |
|---|---|---|
| Scalar (original) | ~380 MB/s | 1x |
| Scalar NMAX | ~2,000 MB/s | ~5x |
| SVE | ~21,000 MB/s | ~55x |

The SVE version is roughly 10x faster than the NMAX scalar version, and about 55x faster than the original. The exact ratio depends on your SVE vector length. You can also use a Graviton3 instance to try on a processor with 256-bit SVE vectors and compare the results. The 256-bit vector length on Graviton3 shows faster performance than the 128-bit vector length on Graviton4, but Graviton3 is slower than Graviton4 on the scalar versions.

## Ask about the assembly

Understanding the generated assembly helps you verify that the compiler is producing the instructions you expect.

### ASK AI: about the inner loop assembly code

Ask your assistant:

```text
disassemble ~/adler32-sve/adler32-test and explain the assembly code for the inner loop.  
```

The response explains the mapping of the C code to the assembly instructions, explains the intrinsics used.

A partial example response is:

```output
Summary                                                                                                                           
                                                                                                                                    
  The entire inner loop is just 7 instructions per vector-width of bytes:                                                           
                                                                                                                                    
  ┌──────────────────┬───────────────────────────────────────┐                                                                      
  │ Instruction      │ Purpose                               │                                                                      
  ├──────────────────┼───────────────────────────────────────┤                                                                      
  │ `whilelo`        │ Generate predicate for this iteration │                                                                      
  │ `ld1b`           │ Predicated load of bytes              │                                                                      
  │ `add` (scalar)   │ Advance loop counter                  │                                                                      
  │ `udot` (weights) │ Weighted sum for `b`                  │                                                                      
  │ `udot` (ones)    │ Simple sum for `a`                    │                                                                      
  │ `add` (vector)   │ Decrement weights                     │                                                                      
  │ `cmp` + `b.hi`   │ Loop control                          │                                                                      
  └──────────────────┴───────────────────────────────────────┘
```

To see the actual assembly, disassemble the binary:

```bash
objdump -d adler32-test | grep -A 40 "<adler32>"
```

Look for the `WHILELT` and `UDOT` instructions in the inner loop. If you see them, the SVE code path is active.

## Ask about debugging and performance tuning

You can also use your AI assistant to debug any issues or clarify performance, but be careful, it is easy to divert into an endless loop of trial and error as today's assistants can easily make things worse.

## What you've accomplished

You've completed the full optimization journey for Adler-32 on Arm Neoverse using an AI Assistant and the Arm MCP server:

1. You started with a simple scalar implementation and measured its baseline performance
2. You used the Arm MCP server to learn SVE concepts such as predicates, widening loads, dot products, and reductions without looking up documentation 
3. You applied the NMAX modulo-deferral technique to restructure the algorithm for vectorization
4. You built a vector-length-agnostic SVE implementation that works correctly on any SVE-capable processor
5. You measured a performance improvement and learned how to read the generated assembly

## Apply this process to your own code

The process you followed here applies directly to other scalar loops in your own projects:

1. Establish a correctness test and a performance baseline before changing anything
2. Ask your AI assistant to guide you and keep explaining along the way
3. Use the Arm MCP server to look up the specific intrinsics you need, one concept at a time
4. Validate correctness before measuring performance
5. Compare against each intermediate version to understand where the speedup comes from

The Arm MCP server's intrinsics reference covers all SVE and SVE2 intrinsics. As you encounter more complex loops, you can use the same question-and-answer approach to find the right intrinsics for your specific data types and operations.
