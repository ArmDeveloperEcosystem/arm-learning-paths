---
title: Understand the Adler-32 algorithm and optimization approach
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The optimization task

In this Learning Path, you'll take a simple scalar implementation of the Adler-32 checksum algorithm written in C and incrementally optimize it to use Arm Scalable Vector Extension (SVE) intrinsics. The final SVE version runs significantly faster than the original scalar code on Neoverse processors.

This Learning Path is different from a typical optimization tutorial. Rather than starting with a finished SVE implementation, you'll use an AI coding assistant connected to the Arm MCP server to guide you through each step. You'll ask questions, look up intrinsics, understand the algorithm's constraints, and build the solution piece by piece.

AI coding assistants are not yet able to generate optimized code, but you can use them to guide your learning and the implementation details. By working this way, you can maintain and explain the code and arrive at optimized solutions, mirroring what you'd do on your own projects.

## The Adler-32 algorithm

Adler-32 is a checksum algorithm used to verify data integrity. It's used in the zlib compression format. The algorithm is fast, simple, and a good candidate for vectorization because its inner loop processes one byte at a time.

The algorithm maintains two 16-bit accumulators, `A` and `B`:

- `A` starts at 1 and accumulates the sum of all input bytes
- `B` accumulates the running sum of all `A` values

Both are taken modulo 65521, the largest prime number smaller than 2^16. The final checksum is `(B << 16) | A`.

The scalar implementation is as follows:

```c
#define MOD_ADLER 65521

uint32_t adler32(const uint8_t *data, size_t len)
{
    uint32_t a = 1;
    uint32_t b = 0;

    for (size_t i = 0; i < len; i++) {
        a = (a + data[i]) % MOD_ADLER;
        b = (b + a) % MOD_ADLER;
    }

    return (b << 16) | a;
}
```

This loop has two characteristics that make it interesting to vectorize:

- The `a` accumulator is a sum that parallelizes well
- The `b` accumulator depends on the running value of `a` after each byte, which makes it harder to vectorize

You'll learn how SVE intrinsics solve both of these challenges.

## The role of the Arm MCP server

The Arm MCP server gives your AI coding assistant access to Arm-specific knowledge, including the full SVE intrinsics reference. When you ask about specific intrinsics such as `svdot` or `svwhilelt`, the assistant queries the MCP server and returns the exact function signature, pseudocode, and required compiler flags.

This means you don't need to keep referring to the intrinsics reference material. You can ask questions in plain language and get precise, actionable answers grounded in Arm documentation.


## What you've learned and what's next

You now understand the Adler-32 algorithm and how you can use the Arm MCP server to optimize the algorithm to use SVE intrinsics.

Next, you'll set up the project and establish a performance baseline for the scalar implementation. 
