---
title: An introduction to integer and floating-point data types
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Integer and floating-point data types are supported by all modern computer architectures. Every programming language uses data types in a different way but the operations and the range limits of each data type remain the same.

Below is a summary of the data types and their ranges together with the C standard integer aliases. You should review this list before learning about the peculiarities involved in converting between types.

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

There are also 128-bit integer types but hardware support exists only in a few systems with limited operations. Most compilers support 128-bit arithmetic emulation using 64-bit integers (gcc has `__int128_t`). Types may change in the future as big integer arithmetic is particularly useful in cryptography.

## Floating-point types

### Representation in IEEE-754

[Wikipedia](https://en.wikipedia.org/wiki/Single-precision_floating-point_format) provides an excellent overview of the 32-bit floating point number representation. A short summary is provided below. 

Every real number is represented **in approximation** by the closest 32-bit floating point number:

`(-1)^s * 2^(E-127) * (1 + Sum_i b_i 2^(-i)))`

A similar expression exists for the 64-bit floating-point number (`double` data type). 

Here are the characteristics for `float` and `double`:

| Data type (cstdint)  | size (bytes) |  sign  | exponent (bits) | mantissa (bits)   |    lowest value   |   minimum value   |   maximum value   |
| -------------------- | ------------ | ------ | --------------  | ----------------- | ----------------- | ----------------- | ----------------- |
|             float    |       4      |    1   |        8        |        23         |      -3.40282e+38 |       1.17549e-38 |       3.40282e+38 |
|            double    |       8      |    1   |       11        |        52         |     -1.79769e+308 |      2.22507e-308 |      1.79769e+308 |

In practice, this means that real numbers that are very close could be represented by the same floating-point number. If you assign a real number value to a float data type and immediately print it, the result might not be the same real number that you originally assigned.

An example is provided below to clarify exactly what this means. 

Use a text editor to save the C program below in a file named `floattest.c`:

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

Compile and run the program:

```bash
gcc -o floattest floattest.c
./floattest
```

The output is:

```output
x = 0.99999982118607, 0x3f7ffffd
x = 0.99999988079071, 0x3f7ffffe
x = 0.99999994039536, 0x3f7fffff
```

This small program demonstrates how the binary 32-bit values correspond to floating point numbers. 

First, notice that the initial value of `x` is not `0.9999998` that was originally assigned. It is now the closest float `0.99999982118607` with a hex value of `0x3f7ffffd`. 

Second, even though the program prints 14 decimal digits, the resolution of the float datatype is definitely not 14 digits.

A difference of the last hex digit corresponds to a difference in the 8th decimal digit. 

You can try a different scale and see what happens. 

Change the value of `x` and the `while` statement as shown below:

```C
...
		float x = 0.9999998e5;
...
        while (x < 1.0e5f) {
...
```

Compile and run again:

```bash
gcc -o floattest floattest.c
./floattest
```

The output is now:

```output
x = 99999.97656250000000, 0x47c34ffd
x = 99999.98437500000000, 0x47c34ffe
x = 99999.99218750000000, 0x47c34fff
```

Notice that the initial value of `x` is not the one that you assigned, but the closest float value. The hex value `0x47c34ffd` corresponds to `99999.9765625`. 


Here, the difference is in the 2nd decimal digit. After the 7th decimal digit, all the rest are zeroes! This is because 32-bit floating point numbers offer up to 7 decimal digits of precision only.

A similar point can be made for doubles but because the precision is twice that of 32-bit floats, you get 14 decimal digits of precision.

{{% notice Summary %}}
You are not dealing with real numbers, but approximate representations of real numbers using limited precision data types. 

If you assign a real number value to a float data type, the result might not be the same real number you assigned.
{{% /notice %}}

If your calculations require full precision, then you should be looking at arbitrary precision libraries such as [The GNU Multiple Precision Arithmetic Library](https://gmplib.org/). 

### Other floating-point data types: FP16, BF16, and FP8

The recent popularity in Machine Learning/Deep Learning (ML/DL) models have created the need for smaller data types. 

These data types have a far smaller range than 32-bit float or 64-bit doubles but offer twice or 4 times the number of elements in the same number of bytes. 

For example, you can fit 2 `fp16`/`bf16` elements and 4 `fp8` elements in the same space as a 32-bit `float` number.

Here is a list of the basic traits of the `fp8` (the 2 most important variants), `fp16` and `bf16`.

| Data type (cstdint)  | size (bytes) |  sign  | exponent (bits) | mantissa (bits)   |    lowest value   |   minimum value   |   maximum value   |
| -------------------- | ------------ | ------ | --------------  | ----------------- | ----------------- | ----------------- | ----------------- |
|          fp8 (e4m3)  |       1      |    1   |        4        |         3         |            -240.0 |       0.001953125 |             240.0 |
|          fp8 (e5m2)  |       1      |    1   |        5        |         2         |          -57344.0 | 1.52587890625e-05 |           57344.0 |
|              fp16    |       2      |    1   |        5        |        10         |          -65504.0 |           5.96e−8 |           65504.0 |
|              bf16    |       2      |    1   |        8        |         7         |          -3.4e+38 |          1.17e-38 |           3.4e+38 |

You may be wondering why there are two 16-bit floating point data types. The primary reason is `bf16` can be easily assigned to and from a normal 32-bit float because they have the same number of exponent bits and the same range, just less precision. This is important for performance reasons because you do not need to use a separate instruction to convert between the types.

The `fp8` variants are not covered in this Learning Path as there is no compiler support in C or C++ for either variant on current CPUs. As of today, support for these types exists strictly for GPUs using special languages and tools.

Recent Arm CPUs with SVE and SVE2 do support BF16 in hardware, so these are very relevant.

Now that you have a basic understanding of floating-point numbers and their bit representations, you can learn more about integer-float conversions.
