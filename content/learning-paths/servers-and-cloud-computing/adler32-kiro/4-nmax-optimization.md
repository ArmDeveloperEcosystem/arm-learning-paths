---
title: Defer the modulo with the NMAX optimization
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why modulo operations block vectorization

Look at the original scalar loop again:

```c
for (size_t i = 0; i < len; i++) {
    a = (a + data[i]) % MOD_ADLER;
    b = (b + a) % MOD_ADLER;
}
```

The `% MOD_ADLER` operation runs on every single byte. Division is expensive, and doing it 10 million times for a 10 MB buffer is a significant cost. More importantly, it prevents vectorization because each iteration depends on the modulo-reduced result of the previous one.

The standard solution is to defer the modulo. Of course, you might not see this immediately, but may be able to ask a question about optimizing Adler-32. 

### ASK AI: about the cost of modulo operations

Ask your assistant:

```text
Are there any common techniques to optimize adler-32 and reduce modulo operations?
```

A sample output is:

```output
The deferred modulo trick                                                                                                         
                                                                                                                                    
  Instead of % 65521 every byte, you accumulate freely for a batch of bytes, then apply the modulo once at the end of the batch.    
  This replaces N expensive divisions with N cheap additions + 1 division.                                                          
                                                                                                                                    
  How many bytes before overflow?                                                                                                   
                                                                                                                                    
  We need to find the maximum batch size n where neither a nor b can overflow a uint32_t (max value 2³² - 1 = 4,294,967,295).       
                                                                                                                                    
  For `a`: worst case is every byte = 255, and a starts at its max post-modulo value (65520):                                       
                                                                                                                                    
  a_max = 65520 + 255 * n                                                                                                           
                                                                                                                                    
  For `b`: b accumulates the running sum of a values. Worst case, b starts at 65520 and each a value is as large as possible:       
                                                                                                                                    
  b_max = 65520 + Σ(65520 + 255*k) for k=1..n                                                                                       
        = 65520 + 65520*n + 255*n*(n+1)/2                                                                                           
                                                                                                                                    
  b overflows first because it grows quadratically. Solving for b_max ≤ 2³² - 1:                                                    
                                                                                                                                    
  65520 + 65520*n + 255*n*(n+1)/2 ≤ 4,294,967,295                                                                                   
                                                                                                                                    
  This gives n = 5552.                                                                                                              
                                                                                                                                    
  The standard block size                                                                                                           
                                                                                                                                    
  5552 bytes is the universally used batch size in optimized Adler-32 implementations (zlib, chromium, etc.). The loop structure    
  becomes:                                                                                                                          
                                                                                                                                    
  uint32_t a = 1, b = 0;                                                                                                            
                                                                                                                                    
  while (len > 0) {                                                                                                                 
      size_t block = (len < 5552) ? len : 5552;                                                                                     
      len -= block;                                                                                                                 
                                                                                                                                    
      // Fast inner loop — no modulo here                                                                                           
      for (size_t i = 0; i < block; i++) {                                                                                          
          a += *data++;                                                                                                             
          b += a;                                                                                                                   
      }                                                                                                                             
                                                                                                                                    
      // Modulo once per block                                                                                                      
      a %= MOD_ADLER;                                                                                                               
      b %= MOD_ADLER;                                                                                                               
  }                                                                                                                                 
                                                                                                                                    
  The payoff                                                                                                                        
                                                                                                                                    
  ┌─────────────────────────────┬──────────────────────────────────┐                                                                
  │ Approach                    │ Modulo operations for 64KB input │                                                                
  ├─────────────────────────────┼──────────────────────────────────┤                                                                
  │ Per-byte modulo             │ 65,536 × 2 = **131,072**         │                                                                
  │ Deferred (5552-byte blocks) │ 12 × 2 = **24**                  │                                                                
  └─────────────────────────────┴──────────────────────────────────┘                                                                
                                                                                                                                    
  That's a ~5,400x reduction in modulo operations. And the inner loop is now just additions — which is exactly what SVE svdot and   
  svadd can vectorize.        
```

The response explains the NMAX technique. The key insight is that you can accumulate many bytes before the intermediate values overflow a 32-bit integer, as long as you apply the modulo periodically.

## Implement the scalar NMAX version

Before adding SVE, implement the NMAX optimization using scalar values. This is a useful intermediate step: it lets you verify the optimization is correct and measure its impact independently of vectorization.

Create `adler32-nmax.c`:

```c
/*
 *  Adler-32 with NMAX modulo deferral — scalar optimization
 */
#include <stdint.h>
#include <stddef.h>

#define MOD_ADLER 65521
#define NMAX      5552   /* max bytes before b overflows uint32_t */

uint32_t adler32(const uint8_t *data, size_t len)
{
    uint32_t a = 1;
    uint32_t b = 0;

    while (len > 0) {
        size_t n = len < NMAX ? len : NMAX;
        len -= n;

        /* inner loop: no modulo */
        for (size_t i = 0; i < n; i++) {
            a += data[i];
            b += a;
        }
        data += n;

        a %= MOD_ADLER;
        b %= MOD_ADLER;
    }

    return (b << 16) | a;
}
```

The structure is now an outer loop that processes NMAX-byte blocks, and an inner loop with no modulo at all. The modulo only runs once per 5552 bytes instead of once per byte.

## Update the Makefile to test the NMAX version

Update your `Makefile` to make it easy to switch between implementations:

```makefile
CC      = gcc
CFLAGS  = -O3 -mcpu=native -flto -Wall -Wextra
LDFLAGS = -flto
TARGET  = adler32-test

# Change this line to switch implementations:
# IMPL    = adler32-simple.c
IMPL  = adler32-nmax.c

$(TARGET): $(IMPL) adler32-test.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $(IMPL) adler32-test.c

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: run clean
```

Edit the Makefile to use `adler32-nmax.c` and build and run with the NMAX version:

```bash
make clean && make run
```

The output is similar to:

```output
Correctness: adler32("Wikipedia") = 0x11E60398 [PASS]

Performance:
  1 KB          1024 bytes  100000 iters    49.180 ms    1985.7 MB/s  checksum=0x37B4063C
  10 KB        10240 bytes   10000 iters    48.925 ms    1996.0 MB/s  checksum=0x5FA40D73
  100 KB      102400 bytes    1000 iters    48.893 ms    1997.4 MB/s  checksum=0x2378D74C
  1 MB       1048576 bytes     100 iters    50.012 ms    1999.5 MB/s  checksum=0x058B4B08
  10 MB     10485760 bytes      10 iters    50.097 ms    1996.1 MB/s  checksum=0x285FF1B1
```

This is a substantial improvement over the original scalar version, achieved simply by removing the per-byte modulo. Make a note of these numbers as your new intermediate baseline.

In this section:

- You learned why deferring the modulo is safe and how to calculate the NMAX bound
- You implemented the scalar NMAX optimization and measured a significant speedup
- You now have a clean inner loop with no modulo which is the right structure for SVE vectorization

The inner loop of the NMAX version is now a simple accumulation loop. In the next section, you'll vectorize it with SVE intrinsics.
