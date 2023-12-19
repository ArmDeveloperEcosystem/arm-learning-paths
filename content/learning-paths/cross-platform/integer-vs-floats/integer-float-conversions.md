---
title: Integer <-> Floats Conversions
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Explicit Conversions

Explicit conversions are done on purpose, because you -the developer- know the algorithm and your expectations of the results. You typically would use explicit conversions when, for example, for performance reasons you would want an algorithm to be processed using integer but you need an accurate calculation done with floats or doubles. This is typically the case with video/audio codecs, where most calculations are done using integer arithmetic, but in some places where extra precision is needed, the calculations are evaluated using floats/doubles and then **explicitly** converted back to int. 

Let's see an example taken from [libvpx project](https://github.com/webmproject/libvpx/blob/main/vpx_dsp/add_noise.c#L41), a function to generate an image using auto generated noise from a gaussian distribution function:

```C
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

The `gaussian` function is undoubtably `double` only, no conversion involved here. However, the next function `vpx_setup_noise`, uses that function and does an explicit conversion from `double` to `int`:

```C
    const int a_i = (int)(0.5 + 256 * gaussian(sigma, 0, i));
```

Actually there is also an implicit conversion here with the number `256`, but we'll cover implicit conversions in more detail later. What the compiler will do in this case is generate first the code that calculates the expressions using double arithmetic and then explicitly convert the results to integer, using the relevant instruction (eg `fcvtzs`). For completeness, the assembly output of this code snippet is the following:

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

You can see the full code and its dissassembly in the [godbolt full link](https://godbolt.org/z/cTM8d3dq5))

Notice that before and after the call to `gaussian`: `bl gaussian`, two conversion instructions are called: 

```as
scvtf   d2, w20
```
and

```as
fcvtzs w1, d0
```

which do exactly that, convert the value between register `d0` (a double register) from/to an integer value in registers `w1`, `w20`.

Now, in this particular case this conversion is done on purpose and controlled but when dealing with performance critical software, such conversions can be costly and should be avoided unless there is no other alternative.
But the situation at least is clear with explicit conversions, implicit ones are a bit harder to track.

## Implicit Conversions

When a conversion is not explicitly stated by the user, then it's an implicit one. In general it's a conversion that the compiler issues when there is an operation involving two (or more) elements of different datatypes.
In that case, the compiler has to convert one of the values to the same datatype as the other, as most of the operations involve elements of the same size -with some exceptions, like for example the `SADDW`/`UADDW` Advanced SIMD instructions which add elements of different widths. Such instructions do not require any kind of conversion. But let's consider the generic operation:

```
C = A OP B
```

where `OP` can be any operation that the compiler will translate into one or more assembly instructions, addition, subtraction, multiplication, division, etc.
Depending on the datatypes the conversion can be either a promotion, a demotion, or a conversion between types of different nature (eg float to integer or integer to float).

### Promotions

When one of the datatype involved in the operation changes to a larger size datatype of the same nature, it is called a promotion. For example, when `A` is `int8_t` and `B` is `int32_t` and `C` is also `int32_t` we have a promotion of `A` to `int32_t`.

This is a list of possible datatype promotions:

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

Respectively, if `A` is `float` and `B` is `double` but `C` is `float` then we have a demotion.
This is actually a very risky conversion, as bits are lost and it is discouraged and should be avoided unless in specific circumstances when you know exactly what you are doing.
Unfortunately, this is where the programming language matters. In some cases, C++ will catch such a demotion (called a *narrowing conversion* in C++) and will issue a relevant warning,
C does not allow for such a warning. The C compiler will not issue a warning and it's easy for a conversion bug to creep in your code, and sometimes these can be very hard to detect bugs.
Even on C++ there is a catch however, the compiler will only issue such a warning when using bracket initialization, not assignment between values. You will have a chance to see this in detail in the next section.

Here is a similar list for possible demotions:

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

Some might argue that conversion of an `int16_t` to `float` or `double` is a promotion, but it's not as simple as that. While a demotion does not always need any instruction to take place, usually a promotion requires an instruction to zero or sign-extend the contents of a register. However this can be achieved using other ways also, when the compiler can detect a specific pattern it can skip those zero/sign-extend instructions and solve the problem by mere shuffling/rearrangements on the bytes. For example, this example demonstrates it:

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

The promotion here for function `promotetest1` is achieved by a clever use of `zip1`/`zip2` instructions. No sign-extend instruction involved. However, the instructions `stxl`/`stxl2` are used in the second example. 
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

However when an integer is converted to a floating point number, or vice-versa, there is **always** a conversion instruction involved. And it's almost always more costly than a mere copy.

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

It is time to take a close look at the potential issues in those floating-point conversions.