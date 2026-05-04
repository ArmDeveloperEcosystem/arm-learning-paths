---
title: Vectorize the Adler-32 inner loop with SVE intrinsics
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why the b accumulator is hard to vectorize

The NMAX inner loop is now:

```c
for (size_t i = 0; i < n; i++) {
    a += data[i];
    b += a;
}
```

Vectorizing the `a` accumulator is straightforward: load a vector of bytes, sum them all, add to `a`. The `b` accumulator is harder. Each byte's contribution to `b` depends on how many bytes come after it in the block. If you process N bytes at once, `data[0]` contributes N times to `b`, `data[1]` contributes N-1 times, and so on.

Ask your AI assistant to help you think through this.

### ASK AI: about how to vectorize the loop

Ask your assistant:

```text
How can I vectorize the inner loop of the NMAX version using SVE? Provide a detailed explanation for how to do it and teach me about the intrinsics used. 
```

A sample response is:

```output
Vectorizing the Adler-32 NMAX Inner Loop with SVE                                                                                 
                                                                                                                                    
  Starting Point                                                                                                                    
                                                                                                                                    
  Your scalar NMAX inner loop:                                                                                                      
                                                                                                                                    
  for (size_t i = 0; i < n; i++) {                                                                                                  
      a += data[i];                                                                                                                 
      b += a;                                                                                                                       
  }                                                                                                                                 
                                                                                                                                    
  a is a running sum of bytes. b is a running sum of a. The dependency of b on a at every step makes this look serial — but we can  
  reformulate the math to break that dependency.                                                                                    
                                                                                                                                    
  The Mathematical Insight                                                                                                          
                                                                                                                                    
  Consider a chunk of n bytes: d[0], d[1], ..., d[n-1]. Expanding what b accumulates:                                               
                                                                                                                                    
  After d[0]:  b += a + d[0]                                                                                                        
  After d[1]:  b += a + d[0] + d[1]                                                                                                 
  ...                                                                                                                               
  After d[n-1]: b += a + d[0] + d[1] + ... + d[n-1]                                                                                 
                                                                                                                                    
  Summing all contributions:                                                                                                        
                                                                                                                                    
  b_total = n * a_in  +  (n)*d[0] + (n-1)*d[1] + ... + (1)*d[n-1]                                                                   
                                                                                                                                    
  So b is the sum of two things:                                                                                                    
                                                                                                                                    
  1. n * a_in — the initial value of a multiplied by the chunk length                                                               
  2. A weighted sum of the data bytes, where byte at position i has weight (n - i) — its distance from the end of the chunk         
                                                                                                                                    
  And a is simply:                                                                                                                  
                                                                                                                                    
  a_total = a_in + d[0] + d[1] + ... + d[n-1]                                                                                       
                                                                                                                                    
  Both the plain sum and the weighted sum can be computed in parallel across vector lanes. The key SVE instruction that makes this  
  efficient is `svdot` — a dot product that multiplies pairs of uint8_t values, widens to uint32_t, and accumulates, all in one     
  instruction.                                                                                                                      
                                                                                                                                    
  SVE Implementation Strategy                                                                                                       
                                                                                                                                    
  Step 1: Build a descending weight vector                                                                                          
                                                                                                                                    
  We need weights [n, n-1, n-2, ..., n-vl+1] for the first iteration, then subtract vl each iteration so the weights keep descending
  across the full chunk:                                                                                                            
                                                                                                                                    
  svuint8_t weights = svindex_u8((uint8_t)n, (uint8_t)-1);                                                                          
                                                                                                                                    
  svindex_u8(base, step) creates a vector where lane k = base + k * step. With base = n and step = -1 (which wraps to 255 in uint8, 
  but the arithmetic works out modulo 256), this gives [n, n-1, n-2, ...].                                                          
                                                                                                                                    
  For a chunk of 24 bytes with vl = 8, the weights across three iterations would be:                                                
                                                                                                                                    
  Iteration 0: weights = [24, 23, 22, 21, 20, 19, 18, 17]                                                                           
  Iteration 1: weights = [16, 15, 14, 13, 12, 11, 10,  9]                                                                           
  Iteration 2: weights = [ 8,  7,  6,  5,  4,  3,  2,  1]                                                                           
                                                                                                                                    
  Each byte gets multiplied by exactly its distance from the end — matching the formula.                                            
                                                                                                                                    
  Step 2: The vectorized loop                                                                                                       
                                                                                                                                    
  svuint32_t a_vec = svdup_u32(0);                                                                                                  
  svuint32_t b_vec = svdup_u32(0);                                                                                                  
                                                                                                                                    
  for (size_t i = 0; i < n; i += vl) {                                                                                              
      svbool_t pg = svwhilelt_b8((uint64_t)i, (uint64_t)n);                                                                         
      svuint8_t bytes = svld1_u8(pg, &data[i]);                                                                                     
                                                                                                                                    
      b_vec = svdot_u32(b_vec, bytes, weights);                                                                                     
      a_vec = svdot_n_u32(a_vec, bytes, 1);                                                                                         
                                                                                                                                    
      weights = svsub_n_u8_x(svptrue_b8(), weights, (uint8_t)vl);                                                                   
  }                                                                                                                                 
                                                                                                                                    
  Let's walk through each line:                                                                                                     
                                                                                                                                    
  `svwhilelt_b8(i, n)` — Creates a predicate (bitmask) where lane k is active if i + k < n. For full iterations this is all-true.   
  For the final iteration, it masks off lanes past the end of the data. This eliminates the need for a scalar tail loop — SVE's     
  predication handles the remainder natively.                                                                                       
                                                                                                                                    
  `svld1_u8(pg, &data[i])` — Predicated load of bytes. Active lanes load from memory; inactive lanes produce zero. This is safe even
  if data + i would read past the buffer for inactive lanes.                                                                        
                                                                                                                                    
  `svdot_u32(b_vec, bytes, weights)` — This is the powerhouse. It takes two uint8_t vectors, multiplies corresponding elements,     
  groups the products in sets of 4, sums each group with widening to uint32_t, and accumulates into b_vec. Visually for one group of
  4:                                                                                                                                
                                                                                                                                    
  b_vec[k] += bytes[4k]*weights[4k] + bytes[4k+1]*weights[4k+1]                                                                     
            + bytes[4k+2]*weights[4k+2] + bytes[4k+3]*weights[4k+3]                                                                 
                                                                                                                                    
  This computes the weighted sum for b directly — each byte multiplied by its distance-from-end weight.                             
                                                                                                                                    
  `svdot_n_u32(a_vec, bytes, 1)` — Same dot product, but the second operand is the scalar 1 broadcast to all lanes. This effectively
  becomes a widening sum: each group of 4 bytes is summed and accumulated into a uint32_t lane. It computes the simple byte sum for 
  a.                                                                                                                                
                                                                                                                                    
  `svsub_n_u8_x(svptrue_b8(), weights, vl)` — Subtract vl from every weight lane. After processing vl bytes, the next batch of bytes
  is vl positions closer to the end, so their weights are vl less. The _x suffix means "don't care about inactive lanes" — fastest  
  form.                                                                                                                             
                                                                                                                                    
  Step 3: Horizontal reduction and scalar fixup                                                                                     
                                                                                                                                    
  b += a * (uint32_t)n;                                                                                                             
  a += (uint32_t)svaddv_u32(svptrue_b32(), a_vec);                                                                                  
  b += (uint32_t)svaddv_u32(svptrue_b32(), b_vec);                                                                                  
                                                                                                                                    
  a %= MOD_ADLER;                                                                                                                   
  b %= MOD_ADLER;                                                                                                                   
                                                                                                                                    
  `svaddv_u32(pred, vec)` — Horizontal reduction: sums all active uint32_t lanes into a single scalar. We use this to collapse both 
  vector accumulators back to scalars.                                                                                              
                                                                                                                                    
  The b += a * n line accounts for the n * a_in term from our formula — the initial value of a contributed to b at every byte       
  position, but the vector loop only computed the weighted data sum.                                                                
                                                                                                                                    
  Note the ordering: b is updated with a * n before a is modified, because we need the original a_in value.        
```

The response introduces `svindex_u32`, which creates a vector with a starting value and a step:

```c
// Creates [N, N-1, N-2, ..., N-vl+1] where vl is the vector length
svuint32_t weights = svindex_u32((uint32_t)vl, (uint32_t)-1);
```

Combined with `svdot`, this computes the weighted sum in a single instruction. The `svdot_u32` intrinsic multiplies corresponding 8-bit elements from two vectors and accumulates the products into 32-bit lanes:

```c
// b_vec += data_bytes * weights (dot product, 4 bytes per 32-bit lane)
b_vec = svdot_u32(b_vec, data_u8, weights_u8);
```

This step can be confusing at first. The key is that `svdot` works on groups of four 8-bit elements per 32-bit lane. You need to prepare the weight vector in 8-bit form to match.

This is the skeleton. The full implementation requires careful handling of the weight vector for partial vectors at the loop tail.

You can continue learning by asking questions and coding. You can also use your AI assistant to check your code and explain it.

It's unlikely that just asking your assistant to write the code using SVE intrinsics will function correctly with best performance.

## The complete SVE implementation

Create `adler32-sve.c`. This is the full implementation based on the concepts you've learned:

```c
/*
 *  Adler-32 with SVE vectorization and NMAX modulo deferral
 */
#include <stdint.h>
#include <stddef.h>
#include <arm_sve.h>

#define MOD_ADLER 65521
#define NMAX      5552

uint32_t adler32(const uint8_t *data, size_t len)
{
    uint32_t a = 1;
    uint32_t b = 0;

    const uint64_t vl = svcntb();

    while (len > 0) {
        size_t n = len < NMAX ? len : NMAX;
        len -= n;

        svuint32_t a_vec = svdup_u32(0);
        svuint32_t b_vec = svdup_u32(0);

        /*
         * Descending weights in u8: [n, n-1, n-2, ..., n-vl+1].
         * Byte at position i within the block gets weight (n - i),
         * matching how many times it contributes to b.
         */
        svuint8_t weights = svindex_u8((uint8_t)n, (uint8_t)-1);

        for (size_t i = 0; i < n; i += vl) {
            svbool_t pg = svwhilelt_b8((uint64_t)i, (uint64_t)n);
            svuint8_t bytes = svld1_u8(pg, &data[i]);

            /* b += data[i]*w[0] + data[i+1]*w[1] + ... (weighted sum) */
            b_vec = svdot_u32(b_vec, bytes, weights);

            /* a += data[i] + data[i+1] + ... (simple sum via dot with 1) */
            a_vec = svdot_n_u32(a_vec, bytes, 1);

            /* Decrease all weights by vl for next iteration */
            weights = svsub_n_u8_x(svptrue_b8(), weights, (uint8_t)vl);
        }

        data += n;

        /*
         * a_vec lanes each hold partial sums of groups of 4 bytes.
         * b_vec lanes hold partial weighted sums.
         * The existing 'a' contributed to b for each of the n bytes.
         */
        b += a * (uint32_t)n;
        a += (uint32_t)svaddv_u32(svptrue_b32(), a_vec);
        b += (uint32_t)svaddv_u32(svptrue_b32(), b_vec);

        a %= MOD_ADLER;
        b %= MOD_ADLER;
    }

    return (b << 16) | a;
}
```

## Update the Makefile for SVE

Update your `Makefile` to compile the SVE version with the required flags:

```makefile
CC      = gcc
CFLAGS  = -O3 -mcpu=native -flto -Wall -Wextra
LDFLAGS = -flto
TARGET  = adler32-test

# Change this line to switch implementations:
#IMPL    = adler32-simple.c
#IMPL  = adler32-nmax.c
IMPL  = adler32-sve.c

$(TARGET): $(IMPL) adler32-test.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $(IMPL) adler32-test.c

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: run clean
```

## Build and verify correctness

Build and run the correctness test first:

```bash
make clean && make run
```

The expected output starts with:

```output
Correctness: adler32("Wikipedia") = 0x11E60398 [PASS]

Performance:
  1 KB          1024 bytes  100000 iters     4.086 ms   23897.6 MB/s  checksum=0xFF69063C
  10 KB        10240 bytes   10000 iters     4.439 ms   21997.2 MB/s  checksum=0x34F60D73
  100 KB      102400 bytes    1000 iters     4.436 ms   22015.3 MB/s  checksum=0xAE3DD74C
  1 MB       1048576 bytes     100 iters     4.719 ms   21192.0 MB/s  checksum=0xB0C34B08
  10 MB     10485760 bytes      10 iters     4.743 ms   21084.6 MB/s  checksum=0x649EF1B1
```

## What you've learned and what's next

In this section:

- You learned how to use `svindex_u32` to create position-weight vectors
- You used `svdot` to compute the weighted sum for the `b` accumulator
- You built a complete, vector-length-agnostic SVE implementation

In the final section, you'll benchmark the SVE version against the scalar and NMAX baselines, and look at the generated assembly to understand what the CPU is actually executing.
