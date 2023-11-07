---
title: Another example with SVE2
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example 2: SVE2 unleashed

Let's try another example, one from [gcc restrict pointer examples](https://www.gnu.org/software/c-intro-and-ref/manual/html_node/restrict-Pointer-Example.html):

```C
void process_data (const char *in, char *out, size_t size)
{
  for (int i = 0; i < size; i++)
    out[i] = in[i] + in[i + 1];
}
```

This example will be easier to demonstrate with SVE2. We found gcc 13 to have a better result than clang; this is the output of `gcc-13 -O3 -march=armv9-a`:

```
process_data:
        cbz     x2, .L1
        add     x5, x0, 1
        cntb    x3
        sub     x4, x1, x5
        sub     x3, x3, #1
        cmp     x4, x3
        bls     .L6
        mov     w4, w2
        mov     x3, 0
        whilelo p0.b, wzr, w2
.L4:
        ld1b    z0.b, p0/z, [x0, x3]
        ld1b    z1.b, p0/z, [x5, x3]
        add     z0.b, z0.b, z1.b
        st1b    z0.b, p0, [x1, x3]
        incb    x3
        whilelo p0.b, w3, w4
        b.any   .L4
.L1:
        ret
.L6:
        mov     x3, 0
.L3:
        ldrb    w4, [x5, x3]
        ldrb    w6, [x0, x3]
        add     w4, w4, w6
        strb    w4, [x1, x3]
        add     x3, x3, 1
        cmp     x2, x3
        bne     .L3
        ret
```

Do not worry about each instruction in the assembly here, but notice that gcc has added 2 loops, one that uses the SVE2 `while*` instructions to the processing (.L4) and one scalar loop (.L3). The latter is executed in case there is any pointer aliasing (basically, if there is any overlap between the memory pointers). Let's try adding `restrict` to pointer `in`:

```C
void process_data (const char *restrict in, char *out, size_t size)
{
  for (int i = 0; i < size; i++)
    out[i] = in[i] + in[i + 1];
}
```

This is now the output from gcc-13:
```
process_data:
        cbz     x2, .L1
        add     x5, x0, 1
        mov     w4, w2
        mov     x3, 0
        whilelo p0.b, wzr, w2
.L3:
        ld1b    z1.b, p0/z, [x0, x3]
        ld1b    z0.b, p0/z, [x5, x3]
        add     z0.b, z0.b, z1.b
        st1b    z0.b, p0, [x1, x3]
        incb    x3
        whilelo p0.b, w3, w4
        b.any   .L3
.L1:
        ret
```

This is a huge improvement! The code size is down from 30 lines to 14, less than half of the original size. In both cases, note that the main loop (`.L4` in the former case, `.L3` in the latter) is exactly the same, but the entry and exit code of the function is very much simplified. The compiler was able to distinguish that the memory pointed by `in` does not overlap with memory pointed by `out`, it was able to simplify the code by eliminating the scalar loop, and also remove the associated code that checked if it needed to enter it.

Why is this important if the main loop is still the same?

If your function is going to be called once and run over tens of billions of elements, then saving a few instructions before and after the main loop does not really matter.

But, if your function is going to be called on smaller sizes or even *billions* of times, then saving a few instructions in this function means we are saving a few *billions* of instructions in total, which means less time spent running on the CPU and less energy wasted.
