---
title: An introduction to Integer and Floating-point data types
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

These data types are supported by all modern computer architectures, so most concepts mentioned here are applicable whether you are programming for Arm or x86 CPUs. 
Furthermore, keep in mind that even though every programming language uses them in a different way, the principles remain the same, the operations and the range limits of each datatype remain the same.

We will briefly mention the data types and their ranges together with the C StdInt aliases, before we explain the peculiarities in converting between these types.

## Integer types

| Data type (cstdint)  | size (bytes) |      minimum value   |     maximum value     |     range    |
| -------------------- | ------------ | -------------------- | --------------------- | -------------|
|             int8_t   |       1      |                 -128 |                  +127 |      2^8     |
|            uint8_t   |       1      |                    0 |                  +255 |      2^8     |
|            int16_t   |       2      |               -32768 |                +32767 |     2^16     |
|           uint16_t   |       2      |                    0 |                +65535 |     2^16     |
|            int32_t   |       4      |          -2147483648 |           +2147483647 |     2^32     |
|           uint32_t   |       4      |                    0 |           +4294967295 |     2^32     |
|            int64_t   |       8      | -9223372036854775808 |  +9223372036854775807 |     2^64     |
|           uint64_t   |       8      |                    0 | +18446744073709551615 |     2^64     |

There also exist 128-bit integer types, but hardware support for them exists only in few systems in limited operations. Most compilers support 128-bit arithmetic emulation using 64-bit integers (gcc has `__int128_t`). That will probably change in the future as big integer arithmetic is particularly useful in cryptography.

## Floating-point types

### Representation in IEEE-754

[Wikipedia](https://en.wikipedia.org/wiki/Single-precision_floating-point_format) gives an excellent overview of the 32-bit floating point number representation, but let's give a short summary.

Every real number is represented **in approximation** by the closest 32-bit floating point number:

`(-1)^s * 2^(E-127) * (1 + Sum_i b_i 2^(-i)))`

A similar expression exists for the 64-bit floating-point number, a.k.a. `double`. Here are the characteristics for both `float`/`double`:

| Data type (cstdint)  | size (bytes) |  sign  | exponent(bits) | mantissa (bits)   |    lowest value   |   minimum value   |   maximum value   |
| -------------------- | ------------ | ------ | -------------- | ----------------- | ----------------- | ----------------- | ----------------- |
|             float    |       4      |    1   |        8       |        23         |      -3.40282e+38 |       1.17549e-38 |       3.40282e+38 |
|            double    |       8      |    1   |       11       |        52         |     -1.79769e+308 |      2.22507e-308 |      1.79769e+308 |

In practice this means that real numbers that are very close could be represented by the same floating-point number, and in the same manner, if you assign a real number value to a float data type and print it back,
the result might not be the same real number you assigned.

This might sound confusing, let's give a few examples to clarify, consider the following C program:

```C
#include <math.h>
#include <stdio.h>
#include <stdint.h>

int main() {
    float x = 0.9999998;
    uint32_t *x_ptr = (uint32_t *)(&x);

    while (x < 1.0f) {
        printf("x = %4.14f, 0x%08x\n", x, *x_ptr);
        (*x_ptr)++;
    }
}
```

```bash
$ gcc -o floattest floattest.c
$ ./floattest
x = 0.99999982118607, 0x3f7ffffd
x = 0.99999988079071, 0x3f7ffffe
x = 0.99999994039536, 0x3f7fffff
```

What this small program does is to demonstrate how the binary 32-bit values correspond to floating point numbers. First, notice that the initial value of `x` is not `0.9999998` that you assigned but the closest float `0.99999982118607` with hex value `0x3f7ffffd`. Second, even though it prints 14 decimal digits, the resolution of the float datatype is definitely not 14 digits!
A difference of the last bit corresponds to a difference in the 8th decimal digit. Let's see what happens if you try a different scale, by changing the value of `x`:

```C
...
		float x = 0.9999998e5;
...
        while (x < 1.0e5f) {
...
```

Recompile and run again:

```bash
$ gcc -o floattest floattest.c
$ ./floattest
x = 99999.97656250000000, 0x47c34ffd
x = 99999.98437500000000, 0x47c34ffe
x = 99999.99218750000000, 0x47c34fff
```

Notice that again the initial value of `x` is not the one that you assigned but closest float value, `0x47c34ffd` that corresponds to `99999.9765625`. So, exactly what was mentioned before, *if you assign a real number value to a float data type, the result might not be the same real number you assigned*.

Here, the difference appears in the 2nd decimal digit. And you see that after the 7th decimal digit, all the rest are zeroes! That is because 32-bit floating point numbers offer up to 7 decimal digits of precision only.

A similar point can be made for double, but because the precision is double that of 32-bit floats, you can get 14 decimal digits of precision.

As a general rule, you have to remember: for calculations that require precision, you are not dealing with real numbers, but approximate representations of real numbers using limited precision data types. If your calculations require full precision, then you should probably be looking at arbitrary precision libraries like `gmp`.

### FP16 vs BF16 vs FP8

With the recent popularity in Machine Learning/Deep Learning (ML/DL) models that are so important for AI research, smaller data types have emerged, these have far smaller range than 32-bit float and 64-bit doubles, but
offer twice or 4 times the number of elements in the same number of bytes. For example, you can fit 2 x `fp16`/`bf16` elements and 4 x `fp8` elements in the same space a 32-bit `float` number takes.

Here is a list the basic traits of the fp8 (2 most important variants) and fp16/bf16.

| Data type (cstdint)  | size (bytes) |  sign  | exponent(bits) | mantissa (bits)   |    lowest value   |   minimum value   |   maximum value   |
| -------------------- | ------------ | ------ | -------------- | ----------------- | ----------------- | ----------------- | ----------------- |
|          fp8 (e4m3)  |       1      |    1   |        4       |         3         |            -240.0 |       0.001953125 |             240.0 |
|          fp8 (e5m2)  |       1      |    1   |        5       |         2         |          -57344.0 | 1.52587890625e-05 |           57344.0 |
|              fp16    |       2      |    1   |        5       |        10         |          -65504.0 |           5.96e−8 |           65504.0 |
|              bf16    |       2      |    1   |        8       |         7         |          -3.4e+38 |          1.17e-38 |           3.4e+38 |

Why are there two 16-bit floating point data types? Well, there are historical reasons for that, but suffice to say that bf16 has an added bonus of being easily assignable to and from a normal 32-bit float -as they have the same number of exponent bits, so the same range, just less precision. This is very important for performance reasons, as you will not need to actually use a separate instruction to convert between the types.

We will leave the `fp8` variants out of this learning path, as there is actually no compiler support in C or C++ for either variant on current CPUs. At the time of writing, support for these types exists strictly for GPUs using special languages and tools (eg CUDA). 

On the other hand, modern Arm CPUs with SVE/SVE2 do support BF16 in hardware, so these are very relevant.

Now that you have a basic understanding of floating-point numbers and their bit representations, let's move on to the actual topic, integer-float conversions.