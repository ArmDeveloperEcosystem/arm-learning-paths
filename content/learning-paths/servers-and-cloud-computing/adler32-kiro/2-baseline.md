---
title: Set up the project and establish a baseline
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

To get started, you need an Arm Linux system with SVE support. Suitable cloud instances include AWS Graviton3 or Graviton4, Microsoft Cobalt 100, or Google Axion. The examples in this Learning Path were tested on Ubuntu 26.04.

You also need an AI coding assistant with the Arm MCP server configured. Supported assistants include [GitHub Copilot](/install-guides/github-copilot/), [Kiro CLI](/install-guides/kiro-cli/), [Claude Code](/install-guides/claude-code/), [Gemini CLI](/install-guides/gemini/), and [Codex CLI](/install-guides/codex-cli/). See the [Arm MCP server Learning Path](/learning-paths/servers-and-cloud-computing/arm-mcp-server/) for setup instructions.

{{< notice Note >}}
The AI responses shown are samples. Your AI assistant may word responses differently, include more or less detail, or structure the output differently depending on the tool and model you are using. Focus on the key concepts rather than the exact wording.
{{< /notice >}}

Start by installing the required software and check your system includes SVE.

Install GCC and GNU Make:

```bash
sudo apt install gcc make -y
```

Confirm your system has SVE by checking the CPU flags:

```bash
lscpu | grep -i sve
```

The output should include `sve` in the flags list:

```output
Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm sb paca pacg dcpodp sve2 sveaes svepmull svebitperm svesha3 flagm2 frint svei8mm svebf16 i8mm bf16 dgh rng bti
```

If `sve` does not appear, the system does not support SVE and the final implementation in this Learning Path won't run correctly.

## Create the project files

On your Arm Neoverse system, create a working directory and add the source files.

```bash
mkdir adler32-sve && cd adler32-sve
```

Use an editor to copy the scalar implementation to `adler32-simple.c`:

```c
/*
 *  Adler-32 checksum — simple scalar C implementation
 */
#include <stdint.h>
#include <stddef.h>

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

Create the test and benchmark harness in `adler32-test.c`:

```c
/*
 *  Adler-32 test and benchmark harness
 */
#include <stdint.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

extern uint32_t adler32(const uint8_t *data, size_t len);

static void fill_random(uint8_t *buf, size_t len, uint32_t seed)
{
    for (size_t i = 0; i < len; i++) {
        seed = seed * 1103515245 + 12345;
        buf[i] = (uint8_t)(seed >> 16);
    }
}

static double time_sec(void)
{
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}

static int test_known_vectors(void)
{
    /* RFC 1950: adler32("Wikipedia") = 0x11E60398 */
    const uint8_t wiki[] = "Wikipedia";
    uint32_t got = adler32(wiki, 9);
    uint32_t expect = 0x11E60398;

    printf("Correctness: adler32(\"Wikipedia\") = 0x%08X ", got);
    if (got == expect) {
        printf("[PASS]\n");
        return 0;
    } else {
        printf("[FAIL] expected 0x%08X\n", expect);
        return 1;
    }
}

static void benchmark(const char *label, size_t size, int iters)
{
    uint8_t *data = malloc(size);
    if (!data) { perror("malloc"); exit(1); }
    fill_random(data, size, (uint32_t)size);

    volatile uint32_t sink = adler32(data, size);
    (void)sink;

    double t0 = time_sec();
    for (int i = 0; i < iters; i++)
        sink = adler32(data, size);
    double elapsed = time_sec() - t0;

    double mb = (double)size * iters / (1024.0 * 1024.0);
    printf("  %-8s  %8zu bytes  %6d iters  %8.3f ms  %8.1f MB/s  checksum=0x%08X\n",
           label, size, iters, elapsed * 1000.0, mb / elapsed, sink);

    free(data);
}

int main(void)
{
    int fail = test_known_vectors();
    if (fail) return 1;

    printf("\nPerformance:\n");
    benchmark("1 KB",   1024,           100000);
    benchmark("10 KB",  10 * 1024,       10000);
    benchmark("100 KB", 100 * 1024,       1000);
    benchmark("1 MB",   1024 * 1024,       100);
    benchmark("10 MB",  10 * 1024 * 1024,   10);

    return 0;
}
```

Create a `Makefile`:

```makefile
CC      = gcc
CFLAGS  = -O3 -mcpu=native -flto -Wall -Wextra
LDFLAGS = -flto
TARGET  = adler32-test
SRCS    = adler32-simple.c adler32-test.c

$(TARGET): $(SRCS)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $(SRCS)

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: run clean
```

The `-mcpu=native` flag tells GCC to optimize for the exact CPU you're running on, which enables SVE code generation on Neoverse processors that have SVE.

### ASK AI: about compiler flags

Before running anything, ask your AI assistant to confirm that your build setup is correct for SVE.

```text
My Makefile uses `-O3 -mcpu=native`. Does this enable SVE code generation on a Neoverse processor? Do I need any special flags for SVE intrinsics?
```

A sample response is:

```output
Good question. Let me check what CPU is on your remote system and look up the relevant details. 

Here's the full picture:                                                                                                          
                                                                                                                                    
Yes, `-O3 -mcpu=native` enables SVE code generation on your system. Your Neoverse-V2 processor supports SVE and SVE2, and GCC 15.2
with -mcpu=native resolves to armv9-a+sve2-aes+sve2-bitperm+sve2-sha3+.... I confirmed the compiler is already auto-vectorizing   
with SVE instructions (4 SVE instructions emitted for a simple dot-product loop).                                                 
                                                                                                                                    
For SVE intrinsics, you need:                                                                                                     
                                                                                                                                    
1. No extra compiler flags — -mcpu=native already enables SVE/SVE2. You don't need to add -march=armv8-a+sve separately (that     
   would actually be a downgrade from what -mcpu=native gives you on this CPU).                                                      
2. Include the header in your source files:                                                                                       
                                                                                                                                    
     #include <arm_sve.h>                                                                                                           
                                                                                                                                    
That's it. Your current Makefile flags are correct for both auto-vectorized SVE code and hand-written SVE intrinsics.             
                                                                                                                                    
One caveat: since -mcpu=native detects the build machine's CPU, binaries built this way may not run on older Arm processors (e.g.,
Neoverse-N1/Graviton2). If portability matters, use -mcpu=neoverse-v2 explicitly to make the target clear.                        
                                                                                                                                    
For more on SVE programming, Arm has a good learning path: Port Code to Arm SVE                                                   
(https://learn.arm.com/learning-paths/servers-and-cloud-computing/sve/).         
```

The response explains that `-mcpu=native` enables SVE. It also provides useful info about running on other systems and confirm special flags, such as `-march=armv8-a+sve` are not needed. The response also tells you to include `<arm_sve.h>`.

You also notice the reference to a Learning Path about SVE at the end. This confirms the Arm MCP server is consulted on answering the question.

This is good information you'll need when you create the SVE source later.

## Build and run the baseline

Build and run the scalar version:

```bash
make run
```

The output is similar to:

```output
Correctness: adler32("Wikipedia") = 0x11E60398 [PASS]

Performance:
  1 KB          1024 bytes  100000 iters   255.619 ms     382.0 MB/s  checksum=0x37B4063C
  10 KB        10240 bytes   10000 iters   252.763 ms     386.4 MB/s  checksum=0x5FA40D73
  100 KB      102400 bytes    1000 iters   255.239 ms     382.6 MB/s  checksum=0x2378D74C
  1 MB       1048576 bytes     100 iters   261.659 ms     382.2 MB/s  checksum=0x058B4B08
  10 MB     10485760 bytes      10 iters   262.388 ms     381.1 MB/s  checksum=0x285FF1B1
```

Your numbers will differ depending on your specific Neoverse processor and memory configuration. Make a note of the MB/s values for the 1 MB and 10 MB cases, as these are your baseline numbers to compare against after each optimization.

### ASK AI: about auto-vectorization

Now ask your AI assistant a question that many developers wonder about:

```text
Can GCC auto-vectorize my adler32 function with SVE if I just use `-mcpu=native`? What would prevent auto-vectorization?
```

A sample response is:

```output
No, GCC cannot auto-vectorize your adler32 function. It tried every vector mode (including SVE's VNx* modes) and failed on all of 
  them.                                                                                                                             
                                                                                                                                    
  The report tells us exactly why: "not vectorized: unsupported use in stmt" on line 16.                                            
                                                                                                                                    
  The problem is the modulo operation inside the loop:                                                                              
                                                                                                                                    
  a = (a + data[i]) % MOD_ADLER;   // ← loop-carried dependency + modulo                                                            
  b = (b + a) % MOD_ADLER;          // ← depends on 'a' above, also modulo                                                          
                                                                                                                                    
  Two things kill auto-vectorization here:                                                                                          
                                                                                                                                    
  1. Loop-carried dependency chain: Each iteration's b depends on the current iteration's a, and each a depends on the previous a.  
  The compiler can't compute multiple iterations in parallel because every result feeds into the next.                              
  2. Modulo by a non-power-of-2: % 65521 is an integer division/remainder — there's no cheap SIMD equivalent. The compiler can't    
  vectorize this operation across lanes.                                                                                            
                                                                                                                                    
  This is why hand-written SVE intrinsics are valuable here. The standard trick is to:                                              
                                                                                                                                    
  - Defer the modulo — accumulate partial sums across SVE lanes without reducing mod 65521 every iteration, only applying the modulo
  periodically (every ~5552 bytes, the largest safe batch before uint32_t overflow).                                                
  - Break the dependency — use vector lanes to accumulate a and b contributions independently, then reduce at the end.       
```

The response explains that the modulo operation in every iteration (`% MOD_ADLER`) is the main blocker. The compiler can't easily prove that the intermediate values won't overflow in a way that changes the result when operations are reordered. The loop-carried dependency between iterations also makes it difficult.

Since auto-vectorization won't work, you need to restructure the algorithm before SVE can be applied effectively. The restructuring is explained in the next two sections.

## What you've learned and what's next

In this section:

- You created the scalar Adler-32 implementation and benchmark harness
- You recorded your baseline performance numbers
- You learned that auto-vectorization won't work 

In the next section, you'll use the Arm MCP server to learn the core SVE concepts you need before writing any intrinsics code.
