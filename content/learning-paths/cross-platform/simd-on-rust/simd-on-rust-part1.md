---
title: Arm SIMD on Rust
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Differences with programming with intrinsics in C and Rust

As per the Arm Community blog post about [Neon Intrinsics in Rust](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/rust-neon-intrinsics), there are some differences between C and Rust when programming with intrinsics which are listed in the blog and which will be expanded on in this Learning Path with code examples.

We start with an example that uses Arm Advanced SIMD (Neon) intrinsics in C. Create a file named `average_neon.c` with the contents shown below. This program computes the average value of every pair of elements in 2 arrays:

```C
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <arm_neon.h>

#define N 32

void init_vec(float *restrict A, float *restrict B, size_t n) {
    for (size_t i=0; i < N; i++) {
        A[i] = 2.0  * (i+1);
        B[i] = -3.0 * (i+3);
    }
}

void average_vec(float *restrict C, float *restrict A, float *restrict B, size_t n) {
    float32x4_t half = vdupq_n_f32(0.5f);
    for (size_t i=0; i < n; i+= 4) {
        float32x4_t va = vld1q_f32(&A[i]);
        float32x4_t vb = vld1q_f32(&B[i]);
        float32x4_t vc = vaddq_f32(va, vb);
        vc = vmulq_f32(vc, half);
        vst1q_f32(&C[i], vc);
    }
}

void print_vec(float *restrict A, float *restrict B, float *restrict C, size_t n) {
    for (size_t i=0; i < N; i++) {
        printf("A[%i] = %4.2f, B[%i] = %4.2f -> C[%d] = %4.2f\n", i, A[i], i, B[i], i, C[i]);
    }
}

int main() {
    float A[N], B[N], C[N];

    init_vec(A, B, N);
    average_vec(C, A, B, N);
    print_vec(A, B, C, N);
}
```

Compile the code as follows:

```bash
gcc -O3 -fno-inline average_neon.c -o average_neon
```
Now run the program as follows:

```bash
./average_neon
```
The output should look like the following:

```output
A[0] = 2.00, B[0] = -9.00 -> C[0] = -3.50
A[1] = 4.00, B[1] = -12.00 -> C[1] = -4.00
A[2] = 6.00, B[2] = -15.00 -> C[2] = -4.50
A[3] = 8.00, B[3] = -18.00 -> C[3] = -5.00
A[4] = 10.00, B[4] = -21.00 -> C[4] = -5.50
A[5] = 12.00, B[5] = -24.00 -> C[5] = -6.00
A[6] = 14.00, B[6] = -27.00 -> C[6] = -6.50
A[7] = 16.00, B[7] = -30.00 -> C[7] = -7.00
...
```

Note that the `-fno-inline` option was passed to the compiler. Use this option to prevent the C compiler from inlining the `average_vec` function. This is needed to compare the disassembly output of the `average_vec` function from the C version against the disassembly output from the Rust version. 

Generate the disassembly output from the C version as shown below:

```bash
objdump -S average_neon
```

The output should look like the following:

```asm
0000000000000870 <average_vec>:
 870:   b4000203        cbz     x3, 8b0 <average_vec+0x40>
 874:   4f03f402        fmov    v2.4s, #5.000000000000000000e-01
 878:   d1000464        sub     x4, x3, #0x1
 87c:   d2800003        mov     x3, #0x0                        // #0
 880:   d342fc84        lsr     x4, x4, #2
 884:   91000484        add     x4, x4, #0x1
 888:   d37cec84        lsl     x4, x4, #4
 88c:   d503201f        nop
 890:   3ce36820        ldr     q0, [x1, x3]
 894:   3ce36841        ldr     q1, [x2, x3]
 898:   4e21d400        fadd    v0.4s, v0.4s, v1.4s
 89c:   6e22dc00        fmul    v0.4s, v0.4s, v2.4s
 8a0:   3ca36800        str     q0, [x0, x3]
 8a4:   91004063        add     x3, x3, #0x10
 8a8:   eb03009f        cmp     x4, x3
 8ac:   54ffff21        b.ne    890 <average_vec+0x20>  // b.any
 8b0:   d65f03c0        ret
```

Now create the equivalent Rust example of the C program, first without using SIMD intrinsics. Save the contents in a file named `average1.rs` as per below:

```Rust
const N : usize = 32;

fn main() {
    let mut a: [f32; N] = [0.0; N];
    let mut b: [f32; N] = [0.0; N];
    let mut c: [f32; N] = [0.0; N];

    init_vec(&mut a, &mut b);
    average_vec(&mut c, &a, &b);
    print_vec(&a, &b, &c);
}

fn init_vec(a: &mut [f32], b: &mut [f32]) -> () {
    for i in 0..a.len() {
        a[i] =  2.0_f32 * ((i+1) as f32);
        b[i] = -3.0_f32 * ((i+3) as f32);
    }
}

fn average_vec(c: &mut [f32], a: &[f32], b: &[f32]) -> () {
    for i in 0..c.len() {
        c[i] =  0.5_f32 * (a[i] + b[i]);
    }
}

fn print_vec(a: &[f32], b: &[f32], c: &[f32]) -> () {
    for i in 0..c.len() {
        println!("A[{i}] = {}, B[{i}] = {} -> C[{i}] = {}", a[i], b[i], c[i]);
    }
}
```

Compile it using the `rustc` compiler:

```bash 
rustc -O average1.rs
```

Run the program as follows:
```bash
./average1
```

The output should look like the following:

```output
A[0] = 2, B[0] = -9 -> C[0] = -3.5
A[1] = 4, B[1] = -12 -> C[1] = -4
A[2] = 6, B[2] = -15 -> C[2] = -4.5
A[3] = 8, B[3] = -18 -> C[3] = -5
A[4] = 10, B[4] = -21 -> C[4] = -5.5
A[5] = 12, B[5] = -24 -> C[5] = -6
A[6] = 14, B[6] = -27 -> C[6] = -6.5
A[7] = 16, B[7] = -30 -> C[7] = -7
...
```

The outputs shown from these 2 versions are the same apart from the formatting.

This particular example is not very complicated but you will notice some key differences between C and Rust already:

* Uninitialized variables - mutable/immutable arguments passed to the functions are not a concern for a C developer creating a proof of concept program. This is not the case with Rust programming, which forces the developer to think about these things right from the start. This usually means that it takes longer to write a simple program in Rust but you can be certain that this program will not suffer from trivial bugs such as buffer overflows, out of bounds, illegal conversions etc.
* Conversions/Castings need to be explicit, e.g., `2.0_f32 * ((i+1) as f32)`.
* There is no need to pass size as a parameter as Rust includes size information in its arrays.

Note that this program is not written in the most optimal way for Rust. It is just a 'port' of the C program into Rust with the minimal changes needed to compile and run.

The next step is to use SIMD intrinsics in your Rust program for the averaging loop. Replace the previous `average_vec` function with the function shown below and save the updated contents in a file named `average2.rs` as shown below:

```Rust
#[inline(never)]
fn average_vec(c: &mut [f32], a: &[f32], b: &[f32]) -> () {
    #[cfg(target_arch = "aarch64")]
    {
        use std::arch::is_aarch64_feature_detected;
        if is_aarch64_feature_detected!("neon") {
            return unsafe { average_vec_asimd(c, a, b) };
        }
    }
    // Generic scalar loop
    for i in 0..c.len() {
        c[i] =  0.5_f32 * (a[i] + b[i]);
    }
}

#[cfg(target_arch = "aarch64")]
#[target_feature(enable = "neon")]
unsafe fn average_vec_asimd(c: &mut [f32], a: &[f32], b: &[f32]) -> () {
    use std::arch::aarch64::*;

    let half : float32x4_t = vdupq_n_f32(0.5_f32);
    for i in (0..c.len()).step_by(4) {
        let va: float32x4_t = vld1q_f32(&a[i]);
        let vb: float32x4_t = vld1q_f32(&b[i]);
        let vc: float32x4_t = vmulq_f32(vaddq_f32(va, vb), half);
        vst1q_f32(&mut c[i], vc);
    }
}
```

Now compile it using the `rustc` compiler as shown below:

```bash
rustc -O average2.rs
```

Run the program as follows:
```bash
./average2
```
The output should look like the following:

```output
A[0] = 2, B[0] = -9 -> C[0] = -3.5
A[1] = 4, B[1] = -12 -> C[1] = -4
A[2] = 6, B[2] = -15 -> C[2] = -4.5
A[3] = 8, B[3] = -18 -> C[3] = -5
A[4] = 10, B[4] = -21 -> C[4] = -5.5
A[5] = 12, B[5] = -24 -> C[5] = -6
A[6] = 14, B[6] = -27 -> C[6] = -6.5
A[7] = 16, B[7] = -30 -> C[7] = -7
...
```

The results are the same but let's look at some of the differences:

* You need to use `target_arch` and `target_feature` to use specific hardware extensions. This is Rust's feature detection which is explained in more detail in the next section.
* All definitions and functions need to be enabled with `use`, either selectively, for example `use std::arch::aarch64::float32x4_t` or with a wildcard `use std::arch::aarch64::*`. If in doubt, use the latter.
* You will notice `#[inline(never)]` in the definition of `average_vec`. This is to let the compiler know that it should not inline this function because you will compare the disassembly against the C version.

Now generate the disassembly output for `average2`as follows:

```bash
objdump -S average2
```

The disassembly for the `average_vec` function should look like this:

```asm
00000000000069c4 <_ZN8average211average_vec17h7214a2d335bcab6cE>:
    69c4:       4f0167e0        movi    v0.4s, #0x3f, lsl #24
    69c8:       aa1f03e8        mov     x8, xzr
    69cc:       3ce86821        ldr     q1, [x1, x8]
    69d0:       3ce86842        ldr     q2, [x2, x8]
    69d4:       4e22d421        fadd    v1.4s, v1.4s, v2.4s
    69d8:       6e20dc21        fmul    v1.4s, v1.4s, v0.4s
    69dc:       3ca86801        str     q1, [x0, x8]
    69e0:       91004108        add     x8, x8, #0x10
    69e4:       f140051f        cmp     x8, #0x1, lsl #12
    69e8:       54ffff21        b.ne    69cc <_ZN8average211average_vec17h7214a2d335bcab6cE+0x8>  // b.any
    69ec:       d65f03c0        ret
```

Apart from some minor differences, you will notice that the main loop is the same with the 2 x `ldr` instructions followed by `fadd`, `fmul` and an `str`.

### Feature detection in Rust

Using SIMD intrinsics in Rust is only possible if the specific features of the architecture that enables these intrinsics is enabled.

This can only happen in the architecture-specific portion of the code marked by `#[cfg(target_arch = "aarch64")]`. This code will only be compiled for that particular `target_arch` which means that you might have to provide some architecture-independent implementations that will work in the other architectures to make your code portable.

Feature detection in particular refers to minor extensions in the ISA that are not covered by the main `target_arch` detection. For example, in the case of AArch64, there is the `dotprod` extension that includes intrinsics such as `vdotq_u32`. The equivalent check in C would be something like the following:

```C
#if defined(__ARM_FEATURE_DOTPROD)
(implementation using dotprod instructions)
#else
(alternative implementation)
#endif
```

A [full list of current extensions for Arm](https://doc.rust-lang.org/std/arch/macro.is_aarch64_feature_detected.html) is available, and the [full list of supported intrinsics](https://doc.rust-lang.org/core/arch/aarch64/index.html) is also documented.

## An alternative way with Rust using std::simd

In the introduction you read about 2 ways to carry out SIMD programming with Rust, `std::arch` and `std::simd`. You implemented the first approach. Now you can create an equivalent program in Rust using the `std::simd` approach.

Shown below is the same program modified to use `std::simd`. Replace the functions in `average2.rs` with the following and save the updated contents in a file name `average3.rs`:

```Rust
#[inline(never)]
fn average_vec(c: &mut [f32], a: &[f32], b: &[f32]) -> () {
    #[cfg(target_arch = "aarch64")]
    {
        return unsafe { average_vec_asimd(c, a, b) };
    }
}

#[cfg(target_arch = "aarch64")]
#[target_feature(enable = "neon")]
unsafe fn average_vec_asimd(c: &mut [f32], a: &[f32], b: &[f32]) -> () {
    let half = f32x4::splat(0.5_f32);
    for i in (0..c.len()).step_by(4) {
        let va: f32x4 = f32x4::from_slice(&a[i..i+4]);
        let vb: f32x4 = f32x4::from_slice(&b[i..i+4]);
        let vc: f32x4 = (va + vb) * half;
        vc.copy_to_slice(&mut c[i..i+4]);
    }
}
```

Add the following lines at the top of the file as follows:

```Rust
#![feature(portable_simd)]
use std::simd::*;
```

Now compile the code as shown below:

```bash
rustc -O average3.rs
```
Run the program as per below:
```
./average3
```

The output should look like the following:
```output
A[0] = 2, B[0] = -9 -> C[0] = -3.5
A[1] = 4, B[1] = -12 -> C[1] = -4
A[2] = 6, B[2] = -15 -> C[2] = -4.5
A[3] = 8, B[3] = -18 -> C[3] = -5
A[4] = 10, B[4] = -21 -> C[4] = -5.5
A[5] = 12, B[5] = -24 -> C[5] = -6
A[6] = 14, B[6] = -27 -> C[6] = -6.5
A[7] = 16, B[7] = -30 -> C[7] = -7
```
Now generate the disassembly for `average3`:

```bash
objdump -S average3
```
The disassembly output for `average_vec` using `std::simd` should look like the following:

```asm
00000000000069c4 <_ZN8average311average_vec17h154eda43e5fca9f1E>:
    69c4:       4f0167e0        movi    v0.4s, #0x3f, lsl #24
    69c8:       aa1f03e8        mov     x8, xzr
    69cc:       3ce86821        ldr     q1, [x1, x8]
    69d0:       3ce86842        ldr     q2, [x2, x8]
    69d4:       4e22d421        fadd    v1.4s, v1.4s, v2.4s
    69d8:       6e20dc21        fmul    v1.4s, v1.4s, v0.4s
    69dc:       3ca86801        str     q1, [x0, x8]
    69e0:       91004108        add     x8, x8, #0x10
    69e4:       f140051f        cmp     x8, #0x1, lsl #12
    69e8:       54ffff21        b.ne    69cc <_ZN8average311average_vec17h154eda43e5fca9f1E+0x8>  // b.any
    69ec:       d65f03c0        ret
```

You will see that the disassembly output is exactly the same as the version using `std::arch`. The only difference is that the second version will work on other architectures as well.

However, there are some caveats: some operations may benefit from using specialized intrinsics that are not easily mapped in an architecture-agnostic method. In such cases, you might have to choose performance over portability. 
