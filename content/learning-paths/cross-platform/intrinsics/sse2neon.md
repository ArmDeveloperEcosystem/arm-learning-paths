---
layout: learningpathall
title: Using sse2neon to port code to Arm
weight: 4
---

## sse2neon 

The [sse2neon project](https://github.com/DLTcollab/sse2neon) is a quick way to get C/C++ applications compiling and running on Arm. The `sse2neon.h` header file provides NEON implementations for x64 intrinsics so no further source code changes are needed. 

Each intrinsic is replaced with NEON code and so will run on an appropriate Arm platform.

## Porting with sse2neon

To make this application compile and run on Arm there are three steps.

- Adjust the SSE specific header file usage for the Arm architecture
- Include `sse2neon.h` to map the intrinsics to NEON instructions
- Change the g++ compiler flags for the Arm architecture

Here is the new code (`neon.cpp`). The only change is related to the include files.

```cpp { file_name="neon.cpp" }
#include <iostream>

#ifdef __SSE2__
  #include <emmintrin.h>
#else
  #ifdef __aarch64__
    #include "sse2neon.h"
  #else
    #warning SSE2 support is not available. Code will not compile
  #endif
#endif

int main(int argc, char **argv)
{
    __m128 a = _mm_set_ps(4.0, 3.0, 2.0, 1.0);
    __m128 b = _mm_set_ps(8.0, 7.0, 6.0, 5.0);

    __m128 c = _mm_add_ps(a, b);

    float d[4];
    _mm_storeu_ps(d, c);

    std::cout << "result equals " << d[0] << "," << d[1]
              << "," << d[2] << "," << d[3] << std::endl;

    return 0;
}
```
This can be compiled and run on your Arm instance using the commands below.

Install `wget` and `g++` compiler, and use appropriate `g++` command options:

```bash { target="arm64v8/ubuntu:latest" }
sudo apt install -y wget g++
wget https://raw.githubusercontent.com/DLTcollab/sse2neon/master/sse2neon.h
g++ -O2 -I. -march=armv8.2-a+fp16+rcpc+dotprod+crypto --std=c++14 neon.cpp -o neon
```
Run the code:
```bash { target="arm64v8/ubuntu:latest"; command_line="user@localhost | 2" }
./neon
```
and observe the output:
```output
result equals 6,8,10,12
```
