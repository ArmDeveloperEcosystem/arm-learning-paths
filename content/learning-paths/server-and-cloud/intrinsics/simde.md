---
layout: learningpathall
title: Using SIMD Everywhere to port intrinsics to Neoverse
weight: 5
---

## Using SIMD Everywhere

The [SIMD Everywhere](https://github.com/simd-everywhere/simde) is another way to get C/C++ applications with intrinsics running on Arm Neoverse. Like sse2neon it is a header-only library which makes porting code to other architectures easy. 

If the code being migrated has MMX or SSE code then either library can work, but if it contains AVX then SIMDe is needed. 

To make the example application compile and run on Neoverse there are three steps.

The matching header file for emmintrin.h in SIMDe file is simde/x86/sse2.h

- Identify the appropriate header file from SIMDe 
- Include the header file to map the intrinsics to NEON instructions 
- Use the SIMDE_ENABLE_NATIVE_ALIASES to enable original _mm intrinsics to be recognized
- Change the g++ compiler flags for the Arm architecture

Here is the new program. The only change is related to the include files.

```cpp { file_name="neon.cpp" }
#include <iostream>

#define SIMDE_ENABLE_NATIVE_ALIASES
#ifdef __SSE2__
  #include <emmintrin.h>
#else
  #ifdef __aarch64__
    #include "simde/x86/sse2.h"
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

Assuming the new file is renamed to be neon.cpp this version can be compiled and run on the Arm architecture using the commands below. Install git, the g++ compiler and use these options recommended for Neoverse-N1.

```bash { target="arm64v8/ubuntu:latest" }
sudo apt install -y git g++
git clone https://github.com/simd-everywhere/simde.git
g++ -O2 -I simde/ -march=armv8.2-a+fp16+rcpc+dotprod+crypto --std=c++14 neon.cpp -o neon
```

Execute and check the program output:

```bash { target="arm64v8/ubuntu:latest"; command_line="user@localhost | 2" }
./neon
result equals 6,8,10,12
```

The SIMDE_ENABLE_NATIVE_ALIASES macro is not recommended for large projects. Instead, SIMDe recommends to change the intrinics and add "simde" in front of them.

This means change _mm_set_ps to be simde_mm_set_ps. Using the simde prefix is recommended for new code.