---
title: "Build an example application"
weight: 3
layout: "learningpathall"
---

## Example application: DynamoRIO stride benchmark

The white paper presents a micro-benchmark from the DynamoRIO project. The stride benchmark is a pointer chasing algorithm that accesses values in a 16 MB array, with the array position being determined by the pointer being chased. The pointer position is a function of a constant value set in the array before the pointer chasing function begins.

The original source code is at https://github.com/DynamoRIO/dynamorio/blob/master/clients/drcachesim/tests/stride_benchmark.cpp

The code below is slightly modified to increase the number of iterations so that it runs longer for performance analysis.

1. Use a text editor to copy the code below into a text file named `stride.cpp`:

```C++
/* **********************************************************
 * Copyright (c) 2018-2023 Google LLC  All rights reserved.
 * **********************************************************/

/*
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * * Redistributions of source code must retain the above copyright notice,
 *   this list of conditions and the following disclaimer.
 *
 * * Redistributions in binary form must reproduce the above copyright notice,
 *   this list of conditions and the following disclaimer in the documentation
 *   and/or other materials provided with the distribution.
 *
 * * Neither the name of Google, Inc. nor the names of its contributors may be
 *   used to endorse or promote products derived from this software without
 *   specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL GOOGLE LLC OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
 * DAMAGE.
 */


#include <stdint.h>
#include <string.h>
#include <iostream>

#define MEM_BARRIER() __asm__ __volatile__("" ::: "memory")

int
main(int argc, const char *argv[])
{
    // Cache line size in bytes.
    const int kLineSize = 64;
    // Number of cache lines skipped by the stream every iteration.
    const int kStride = 7;
    // Number of 1-byte elements in the array.
    const size_t kArraySize = 16 * 1024 * 1024;
    // Number of iterations in the main loop.
    const int kIterations = 2000000000;
    // The main vector/array used for emulating pointer chasing.
    unsigned char *buffer = new unsigned char[kArraySize];
    memset(buffer, kStride, kArraySize);

    // Add a memory barrier so the call doesn't get optimized away or
    // reordered with respect to callers.
    MEM_BARRIER();

    int position = 0;

    // Here the code will pointer chase through the array skipping forward
    // kStride cache lines at a time. Since kStride is an odd number, the main
    // loop will touch different cache lines as it wraps around.
    for (int loop = 0; loop < kIterations; ++loop) {
        #if defined(ENABLE_PREFETCH) && defined (DIST)
            const int prefetch_distance = DIST * kStride * kLineSize;
            __builtin_prefetch(&buffer[position + prefetch_distance], 0, 0);
        #endif

        position += (buffer[position] * kLineSize);
        position &= (kArraySize - 1);
    }

    // Add a memory barrier so the call doesn't get optimized away or
    // reordered with respect to callers.
    MEM_BARRIER();

    std::cerr << "Value = " << position << std::endl;

    return 0;
}
```


2. Compile the application:

```console
g++ -g -O3 stride.cpp -o stride
```

Using `-g` provides source code information later for `perf report`.

3. Run the application:

```console
./stride
```

The program runs for about 10-20 seconds, depending on your hardware, and the expected output is:

```output
Value = 12779520
```

The next section demonstrates how to collect metrics for performance analysis.