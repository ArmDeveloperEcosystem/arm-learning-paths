---
title: Implement scalar and SVE2 MATCH search
description: Build scalar and SVE2 MATCH search functions for byte and halfword arrays on an Arm server.
weight: 3
layout: "learningpathall"
---

## Set up your environment

To implement scalar and Scalable Vector Extension 2 (SVE2) MATCH search, you need:

- An Arm-based cloud instance with SVE2 support or an Arm AGI CPU platform running Ubuntu 24.04
- GCC compiler with SVE support

Start by setting up your environment:

```bash
sudo apt-get update
sudo apt-get install -y build-essential gcc g++
```

An effective way to achieve optimal performance on Arm is not only through optimal flag usage, but also by using the most recent compiler version. The Learning Path was tested with GCC 13, which is the default version on Ubuntu 24.04. You can use newer versions of GCC.

Create a directory for your implementations:

```bash
mkdir -p sve2_match_demo
cd sve2_match_demo
```

## Implement search algorithms

To understand the alternatives, implement three versions of the search function.

### Create a generic scalar implementation

Create a generic implementation in C that checks each element individually against each key. 

Open an editor of your choice and copy the following code into a file named `sve2_match_demo.c`:

```c
#include <arm_sve.h>
#include <inttypes.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int search_generic_u8(const uint8_t *hay, size_t n, const uint8_t *keys,
                      size_t nkeys) {
  for (size_t i = 0; i < n; ++i) {
    uint8_t v = hay[i];
    for (size_t k = 0; k < nkeys; ++k)
      if (v == keys[k]) return 1;
  }
return 0;
}

int search_generic_u16(const uint16_t *hay, size_t n, const uint16_t *keys,
                       size_t nkeys) {
  for (size_t i = 0; i < n; ++i) {
    uint16_t v = hay[i];
    for (size_t k = 0; k < nkeys; ++k)
      if (v == keys[k]) return 1;
  }
  return 0;
}
```

The `search_generic_u8()` and `search_generic_u16()` functions both return 1 immediately when a match is found in the inner loop.

### Create an SVE2 MATCH implementation

Next, create an implementation that uses SVE2 MATCH instructions to process multiple elements in parallel.

Add the following code to the same source file:

```c
int search_sve2_match_u8(const uint8_t *hay, size_t n, const uint8_t *keys,
                         size_t nkeys) {
  if (nkeys == 0) return 0;
  const size_t VL = svcntb();
  if (nkeys > VL) return search_generic_u8(hay, n, keys, nkeys);
  svbool_t pg = svptrue_b8();
  uint8_t tmp[256];
  for (size_t i = 0; i < VL; ++i) tmp[i] = keys[i % nkeys];
  svuint8_t keyvec = svld1(pg, tmp);
  size_t i = 0;
  for (; i + VL <= n; i += VL) {
    svuint8_t block = svld1(pg, &hay[i]);
    if (svptest_any(pg, svmatch_u8(pg, block, keyvec))) return 1;
  }
  for (; i < n; ++i) {
    uint8_t v = hay[i];
    for (size_t k = 0; k < nkeys; ++k)
      if (v == keys[k]) return 1;
  }
  return 0;
}

int search_sve2_match_u16(const uint16_t *hay, size_t n, const uint16_t *keys,
                          size_t nkeys) {
  if (nkeys == 0) return 0;
  const size_t VL = svcnth();
  if (nkeys > VL) return search_generic_u16(hay, n, keys, nkeys);
  svbool_t pg = svptrue_b16();
  uint16_t tmp[128];
  for (size_t i = 0; i < VL; ++i) tmp[i] = keys[i % nkeys];
  svuint16_t keyvec = svld1(pg, tmp);
  size_t i = 0;
  for (; i + VL <= n; i += VL) {
    svuint16_t block = svld1(pg, &hay[i]);
    if (svptest_any(pg, svmatch_u16(pg, block, keyvec))) return 1;
  }
  for (; i < n; ++i) {
    uint16_t v = hay[i];
    for (size_t k = 0; k < nkeys; ++k)
      if (v == keys[k]) return 1;
  }
  return 0;
}
```

The SVE MATCH implementation with the `search_sve2_match_u8()` and `search_sve2_match_u16()` functions provides an efficient vectorized search approach. The implementation:

  - Uses SVE2's specialized MATCH instruction to compare multiple elements against multiple keys in parallel.
  - Leverages hardware-specific vector length through `svcntb()` for scalability.
  - Falls back to the generic scalar version if the number of keys, `nkeys`, exceeds the hardware-specific vector length.
  - Prepares a vector of search keys that's compared against blocks of data.
  - Processes data in vector-sized chunks with early termination when matches are found.
  - Falls back to scalar code for remainder elements.

### Create an optimized SVE2 MATCH implementation

Next, add loop unrolling and prefetching to further improve performance.

Add the following code to the same source file:

```c
int search_sve2_match_u8_unrolled(const uint8_t *hay, size_t n, const uint8_t *keys,
                                 size_t nkeys) {
  if (nkeys == 0) return 0;
  const size_t VL = svcntb();
  if (nkeys > VL) return search_generic_u8(hay, n, keys, nkeys);

  svbool_t pg = svptrue_b8();

  // Prepare key vector
  uint8_t tmp[256] __attribute__((aligned(64)));
  for (size_t i = 0; i < VL; ++i) tmp[i] = keys[i % nkeys];
  svuint8_t keyvec = svld1(pg, tmp);

  size_t i = 0;
  // Process 4 vectors per iteration
  for (; i + 4*VL <= n; i += 4*VL) {
    // Prefetch data ahead
    __builtin_prefetch(&hay[i + 16*VL], 0, 0);

    svuint8_t block1 = svld1(pg, &hay[i]);
    svuint8_t block2 = svld1(pg, &hay[i + VL]);
    svuint8_t block3 = svld1(pg, &hay[i + 2*VL]);
    svuint8_t block4 = svld1(pg, &hay[i + 3*VL]);

    svbool_t match1 = svmatch_u8(pg, block1, keyvec);
    svbool_t match2 = svmatch_u8(pg, block2, keyvec);
    svbool_t match3 = svmatch_u8(pg, block3, keyvec);
    svbool_t match4 = svmatch_u8(pg, block4, keyvec);

    if (svptest_any(pg, match1) || svptest_any(pg, match2) ||
        svptest_any(pg, match3) || svptest_any(pg, match4))
      return 1;
  }

  // Process remaining vectors one at a time
  for (; i + VL <= n; i += VL) {
    svuint8_t block = svld1(pg, &hay[i]);
    if (svptest_any(pg, svmatch_u8(pg, block, keyvec))) return 1;
  }

  // Handle remainder
  for (; i < n; ++i) {
    uint8_t v = hay[i];
    for (size_t k = 0; k < nkeys; ++k)
      if (v == keys[k]) return 1;
  }
  return 0;
}

// Optimized 16-bit version with unrolling
int search_sve2_match_u16_unrolled(const uint16_t *hay, size_t n, const uint16_t *keys,
                                  size_t nkeys) {
  if (nkeys == 0) return 0;
  const size_t VL = svcnth();
  if (nkeys > VL) return search_generic_u16(hay, n, keys, nkeys);
  svbool_t pg = svptrue_b16();

  // Prepare key vector
  uint16_t tmp[128] __attribute__((aligned(64)));
  for (size_t i = 0; i < VL; ++i) tmp[i] = keys[i % nkeys];
  svuint16_t keyvec = svld1(pg, tmp);

  size_t i = 0;
  // Process 4 vectors per iteration
  for (; i + 4*VL <= n; i += 4*VL) {
    // Prefetch data ahead
    __builtin_prefetch(&hay[i + 16*VL], 0, 0);

    svuint16_t block1 = svld1(pg, &hay[i]);
    svuint16_t block2 = svld1(pg, &hay[i + VL]);
    svuint16_t block3 = svld1(pg, &hay[i + 2*VL]);
    svuint16_t block4 = svld1(pg, &hay[i + 3*VL]);

    svbool_t match1 = svmatch_u16(pg, block1, keyvec);
    svbool_t match2 = svmatch_u16(pg, block2, keyvec);
    svbool_t match3 = svmatch_u16(pg, block3, keyvec);
    svbool_t match4 = svmatch_u16(pg, block4, keyvec);

    if (svptest_any(pg, match1) || svptest_any(pg, match2) ||
        svptest_any(pg, match3) || svptest_any(pg, match4))
      return 1;
  }

  // Process remaining vectors one at a time
  for (; i + VL <= n; i += VL) {
    svuint16_t block = svld1(pg, &hay[i]);
    if (svptest_any(pg, svmatch_u16(pg, block, keyvec))) return 1;
  }

  // Handle remainder
  for (; i < n; ++i) {
    uint16_t v = hay[i];
    for (size_t k = 0; k < nkeys; ++k)
      if (v == keys[k]) return 1;
  }
  return 0;
}
```

The implementation:

   - Processes four vectors per iteration instead of just one and stops immediately when any match is found in any of the four vectors.
   - Uses prefetching (`__builtin_prefetch`) to reduce memory latency.
   - Leverages the `svmatch_u8` and `svmatch_u16` instructions to efficiently compare each element against multiple keys in a single operation.
   - Aligns memory to 64-byte boundaries for better memory access performance.

## What you've accomplished and what's next

You've added three search approaches for both 8-bit and 16-bit elements to `sve2_match_demo.c`. 

Next, you'll add a benchmark harness, compile the program, and compare their results.
