---
title: Integer and floating-point conversions
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

There are two types of data type conversions, explicit and implicit. 

## Explicit Conversions

Explicit conversions are done on purpose because you, the developer, understand the algorithm and your expectations of the results. Explicit conversions can be used to balance performance and accuracy. 

You would use explicit conversions when you want an algorithm to be processed using integer types but you need an accurate calculation to be done with floats or doubles. 

This is typically the case with video and audio codecs (where most calculations are done using integer arithmetic) but extra precision is needed in some places. To gain precision, calculations are evaluated using floats or doubles and then **explicitly** converted back to integers. 

Below is an example taken from the [libvpx project](https://github.com/webmproject/libvpx/blob/main/vpx_dsp/add_noise.c#L41). 

It shows a function to generate an image using auto-generated noise from a gaussian distribution function.

The code is shown for illustration only, do not try to build or run it. The relevant BSD license of the libvpx library is appended at the end of this section.

```C
/*
 *  Copyright (c) 2015 The WebM project authors. All Rights Reserved.
 *
 *  Use of this source code is governed by a BSD-style license
 *  that can be found in the LICENSE file in the root of the source
 *  tree. An additional intellectual property rights grant can be found
 *  in the file PATENTS.  All contributing project authors may
 *  be found in the AUTHORS file in the root of the source tree.
 */

static double gaussian(double sigma, double mu, double x) {
  return 1 / (sigma * sqrt(2.0 * 3.14159265)) *
         (exp(-(x - mu) * (x - mu) / (2 * sigma * sigma)));
}

int vpx_setup_noise(double sigma, int8_t *noise, int size) {
  int8_t char_dist[256];
  int next = 0, i, j;

  // set up a 256 entry lookup that matches gaussian distribution
  for (i = -32; i < 32; ++i) {
    const int a_i = (int)(0.5 + 256 * gaussian(sigma, 0, i));
    if (a_i) {
      for (j = 0; j < a_i; ++j) {
        if (next + j >= 256) goto set_noise;
        char_dist[next + j] = (int8_t)i;
      }
      next = next + j;
    }
  }
...
}
```

The `gaussian()` function uses only `double` and there are no conversions involved. 

However, the next function `vpx_setup_noise()`, uses the `gaussian()` function and does an explicit conversion from `double` to `int`:

```C
    const int a_i = (int)(0.5 + 256 * gaussian(sigma, 0, i));
```

There is also an implicit conversion here on the constant 256, but implicit conversions are covered in a future section. 

The compiler generates the code that calculates the expressions using double arithmetic and then explicitly converts the results to integers, using conversion instructions. 

The assembly output of the code is below:

```as
gaussian:
        stp     x29, x30, [sp, -32]!
        mov     x29, sp
        str     d8, [sp, 16]
        fmov    d8, d0
        fsub    d0, d2, d1
        fadd    d1, d8, d8
        fnmul   d0, d0, d0
        fmul    d1, d1, d8
        fdiv    d0, d0, d1
        bl      exp
        adrp    x0, .LC0
        ldr     d1, [x0, #:lo12:.LC0]
        fmul    d8, d8, d1
        fmov    d1, 1.0e+0
        fdiv    d1, d1, d8
        ldr     d8, [sp, 16]
        ldp     x29, x30, [sp], 32
        fmul    d0, d1, d0
        ret
vpx_setup_noise:
        stp     x29, x30, [sp, -336]!
        mov     x29, sp
        stp     x21, x22, [sp, 32]
        mov     x22, x0
        adrp    x0, .LC1
        stp     d8, d9, [sp, 48]
        fmov    d8, d0
        mov     w21, w1
        ldr     d9, [x0, #:lo12:.LC1]
        stp     x19, x20, [sp, 16]
        mov     w20, -32
        mov     w19, 0
        str     d10, [sp, 64]
        fmov    d10, 5.0e-1
.L9:
        scvtf   d2, w20
        movi    d1, #0
        fmov    d0, d8
        bl      gaussian
        fmadd   d0, d0, d9, d10
        fcvtzs  w1, d0
        cbz     w1, .L5
        add     x0, sp, 80
        mov     x2, 0
        add     x3, x0, w19, sxtw
        b       .L4
...
```

You can see the source code and its disassembly from GCC and Clang using [Compiler Explorer (also called godbolt)](https://godbolt.org/z/cTM8d3dq5)

Notice that before and after the call to `gaussian`: `bl gaussian`, two conversion instructions are called: 

```as
scvtf   d2, w20
```
and

```as
fcvtzs w1, d0
```

These instructions convert the value between a double register (`d0` and `d2`) from/to an integer value in registers (`w1` and `w20`).

Conversion is done on purpose and is controlled but, when dealing with performance critical software, such conversions can be costly and should be avoided unless there is no alternative.

The second type of conversions are called implicit and are harder to track.

## Implicit Conversions

When a conversion is not explicitly stated it is called implicit. In general, it's a conversion that the compiler issues when there is an operation involving two (or more) elements of different data types.

In that case, the compiler has to convert one of the values to the same datatype as the other, as most operations require elements of the same type.

{{% notice Note %}}
There are some conversion exceptions, for example, the `SADDW`/`UADDW` Advanced SIMD instructions which add elements of different widths. Such instructions do not require any kind of conversion. 
{{% /notice %}}

Here is a generic operation:

```
C = A OP B
```

where `OP` can be any operation that will translate to one or more assembly instructions, addition, subtraction, multiplication, or division.

Depending on the data types the conversion can be either a promotion, a demotion or a conversion between types of a different nature (float to integer or integer to float).

### Promotions

When one of the data types involved in the operation changes to a larger size data type of the same nature, it is called a promotion. For example, when `A` is `int8_t` and `B` is `int32_t` and `C` is also `int32_t` we have a promotion of `A` to `int32_t`.

Here is a list of possible data type promotions:

| Data type (stdint.h)  | Promoted to                                            |
| -------------------- | ----------- | ----------- | ----------- | ------------- |
|             int8_t   |   int16_t   |   int32_t   |   int64_t   |    int128_t*  |
|            int16_t   |             |   int32_t   |   int64_t   |    int128_t*  |
|            int32_t   |             |             |   int64_t   |    int128_t*  |
|            int64_t   |             |             |             |    int128_t*  |
|            fp16**    |             |    float    |   double    |  long double* |
|            bf16**    |             |    float    |   double    |  long double* |
|            float     |             |             |   double    |  long double* |
|            double    |             |             |             |  long double* |

(`*`) depends on the actual compiler support
(`**`) depends on hardware support

Similar promotions take place for unsigned integers.

### Demotions

If `A` is `float` and `B` is `double` but `C` is `float` then it is called a demotion.

This is a risky conversion, as bits are lost and it should be avoided unless you understand exactly what is happening.

Unfortunately, this is where the programming language matters. In some cases, C++ will catch such a demotion (called a *narrowing conversion* in C++) and will issue a relevant warning,

The C language does not provide such a warning. The C compiler will not issue a warning and it's easy for a conversion bug to creep into your code. Sometimes conversion errors can be very hard to detect.

Even with C++ there is a catch as the compiler will only issue such a warning when using bracket initialization, not assignment between values. You will see this in detail in the next section.

Here is a list for possible demotions:

| Data type (stdint.h)  | Demoted to                                             |
| -------------------- | ----------- | ----------- | ----------- | ------------- |
|            int16_t   |   int8_t    |             |             |               |
|            int32_t   |   int8_t    |   int16_t   |             |               |
|            int64_t   |   int8_t    |   int16_t   |   int32_t   |               |
|            fp16**    |             |    float    |   double    |  long double* |
|            bf16**    |             |    float    |   double    |  long double* |
|            float     |             |             |   double    |  long double* |
|            double    |             |             |             |  long double* |

Again unsigned integers are demoted to similar types.

(`*`) depends on the actual compiler support
(`**`) depends on hardware support

### Type conversions

You might argue that conversion of an `int16_t` to `float` or `double` is a promotion but it's not that simple.

While a demotion does not always need an instruction to take place, a promotion usually requires an instruction to zero or sign-extend the contents of a register. However, this can be achieved using other ways as well. When the compiler detects a specific pattern, it can skip the zero/sign-extend instructions and solve the problem by mere shuffling/rearranging the bytes. 

An example of skipping an instruction is shown below:

```C
void promotetest1 (unsigned long *a, unsigned int *b)
{
  for (int i = 0; i < 4; i++)
    a[i] = b[i];
}

void promotetest2 (long *a, int *b)
{
  for (int i = 0; i < 4; i++)
    a[i] = b[i];
}
```

The assembly output for this would be:

```as
promotetest1:
        ldr     q31, [x1]
        movi    v30.4s, 0
        zip1    v29.4s, v31.4s, v30.4s
        zip2    v30.4s, v31.4s, v30.4s
        stp     q29, q30, [x0]
        ret

promotetest2:
        ldr     q31, [x1]
        sxtl    v30.2d, v31.2s
        sxtl2   v31.2d, v31.4s
        stp     q30, q31, [x0]
        ret
```

The promotion here for function `promotetest1()` is achieved by a clever use of `zip1` and `zip2` instructions. No sign-extend instructions are used. However, the instructions `stxl` and `stxl2` are used in the `prootetest2()` example to sign-extend. 

Similarly, consider the equivalent demotion tests:

```C
void demotetest1 (long *a, int *b)
{
  for (int i = 0; i < 4; i++)
    b[i] = a[i];
}

void demotetest2 (unsigned long *a, unsigned int *b)
{
  for (int i = 0; i < 4; i++)
    b[i] = a[i];
}
```

Both are compiled to the following assembly:

```as
demotetest1:
        ldp     q31, q30, [x0]
        uzp1    v30.4s, v31.4s, v30.4s
        str     q30, [x1]
        ret
demotetest2:
        ldp     q31, q30, [x0]
        uzp1    v30.4s, v31.4s, v30.4s
        str     q30, [x1]
        ret
```

When an integer is converted to a floating point number, or vice-versa, there is **always** a conversion instruction involved. And it's almost always more costly than a mere copy.

Here is a list of the possible conversions:

| Data type (stdint.h)  | Converted to                                           |
| -------------------- | ----------- | ----------- | ----------- | ------------- |
|    int8_t, uint8_t   |   fp16**    |   bf16**    |   float     |     double    |
|  int16_t, uint16_t   |   fp16**    |   bf16**    |   float     |     double    |
|  int32_t, uint32_t   |             |             |   float     |     double    |
|  int64_t, uint64_t   |             |             |   float     |     double    |
|            fp16**    |   int8_t    |    int16_t* |   int32_t   |     int64_t   |
|            bf16**    |   int8_t*   |    int16_t* |   int32_t   |     int64_t   |
|            float     |   int8_t*   |    int16_t* |   int32_t*  |     int64_t*  |
|            double    |   int8_t*   |    int16_t* |   int32_t*  |     int64_t*  |

(`*`) Target range is limited and there might be truncation involved
(`**`) depends on hardware support

In the next section you will learn more about the potential issues in floating-point conversions.

## libvpx LICENSE

```
Copyright (c) 2010, The WebM Project authors. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

  * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

  * Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in
    the documentation and/or other materials provided with the
    distribution.

  * Neither the name of Google, nor the WebM Project, nor the names
    of its contributors may be used to endorse or promote products
    derived from this software without specific prior written
    permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
