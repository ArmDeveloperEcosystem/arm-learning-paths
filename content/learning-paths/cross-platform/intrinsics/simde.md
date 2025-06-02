---
layout: learningpathall
title: Use SIMD Everywhere to port code to Arm
weight: 5
---

## SIMD Everywhere

[SIMD Everywhere (SIMDe)](https://github.com/simd-everywhere/simde) is another way to get C/C++ applications with intrinsics running on Arm.

Like `sse2neon` it is a header-only library which makes porting code to other architectures easy. 

If the code being migrated has `MMX` or `SSE` code then either `sse2neon` or `SIMDe` can be used, but if it contains `AVX` then `SIMDe` is needed.

## Porting with SIMD Everywhere

To make the example application compile and run on Arm there are four steps:
- Identify the appropriate header file from SIMDe (use the table in the [SIMDEverywhere wiki](https://wiki.debian.org/SIMDEverywhere) to find the right portable header)
- Define `SIMDE_ENABLE_NATIVE_ALIASES` macro before the include to enable original `_mm` intrinsics to be recognized
- Replace the x86-specific header file with the SIMDe one to map the intrinsics to NEON instructions
- Change the g++ compiler flags for the Arm architecture

{{% notice Note %}}
The use of `SIMDE_ENABLE_NATIVE_ALIASES` is not recommended for large projects.

It is recommended to rename the intrinics with `simde` prepended. For example, change `_mm_set_ps` to `simde_mm_set_ps` in the below.

Using the `simde` prefix is recommended for new code.
{{% /notice %}}  

The appropriate header file for `emmintrin.h` is `simde/x86/sse2.h`

Here is the new code (`neon.cpp`). The only change is related to the include files, and the definition of `SIMDE_ENABLE_NATIVE_ALIASES`.

```cpp { file_name="neon.cpp" }
#include <iostream>

#define SIMDE_ENABLE_NATIVE_ALIASES

#if defined(__SSE2__) || defined(__aarch64__)
  #include "simde/x86/sse2.h"
#else
  #warning SSE2/NEON support is not available. Code will not compile.
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

Install `wget`, `git`, and `g++` compiler, and use appropriate `g++` command options:

```bash { target="arm64v8/ubuntu:latest" }
sudo apt install -y git g++ wget
git clone https://github.com/simd-everywhere/simde.git
g++ -O2 -I simde/ -march=armv8.2-a+fp16+rcpc+dotprod+crypto --std=c++14 neon.cpp -o neon
```

Run the code:
```bash { target="arm64v8/ubuntu:latest" }
./neon
```
and observe the output:
```output
result equals 6,8,10,12
```

## Further reading

For more information on the use of `SIMDe`, see the below blog.

* [Porting to Arm Intrinsics with SIMDe](https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/porting-to-arm-intrinsics-with-simde)
