---
title: Inlining Intrinsics
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example with Dot product

As we referred to the the `dotprod` extension earlier, let's continue with an example around these intrinsics, a program that calculates the Sum of Absolute Differences (SAD) of a 32x32 array of 8-bit unsigned integers (`uint8_t`) using the `vdotq_u32` intrinsic:

```C
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <arm_neon.h>

#define N 32

void init_vec(uint8_t *A, uint8_t *B, int w, int h) {
  for (int i = 0; i < h; i++) {
    printf("A[%d] = [ ", i);
    for (int j = 0; j < w; j++) {
      A[i*w + j] = i + j;
      printf("%02x ", A[i*w + j]);
    }
    printf("]\n");
    printf("B[%d] = [ ", i);
    for (int j = 0; j < w; j++) {
      B[i*w + j] = (i + j) & 4;
      printf("%02x ", B[i*w + j]);
    }
    printf("]\n");
  }
}

uint32_t sad_neon(const uint8_t *a, const uint8_t *b, int w, int h) {
  uint32x4_t sum = vdupq_n_u32(0);

  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j+= 16) {
      uint8x16_t a = vld1q_u8(a[i*w + j]);
      uint8x16_t b = vld1q_u8(b[i*w + j]);
      uint8x16_t diff = vabdq_u8(a, b);
      sum = vdotq_u32(sum, diff, vdupq_n_u8(1));
    }
  }

  return vaddvq_u32(sum);
}

int main() {
    uint8_t A[N*N], B[N*N];

    init_vec(A, B, N, N);
    uint32_t sad = sad_neon(A, B, N, N);
    printf("sad = %x\n", sad);
}
```

Save this file as `dotprod1.c`. Compile with the following command and run it:

```bash { output_lines = "3-12" }
gcc -O3 -march=armv8.2-a+dotprod dotprod1.c -o dotprod1
./dotprod1
A[0] = [ 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f ]
B[0] = [ 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 ]
A[1] = [ 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 20 ]
B[1] = [ 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 ]
...
A[30] = [ 1e 1f 20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d ]
B[30] = [ 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 ]
A[31] = [ 1f 20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e ]
B[31] = [ 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 ]
sad = 7400
```

Note the extra compiler flag `-march=armv8.2-a+dotprod`. This is to enable the code generation for `dotprod` instructions, otherwise the compiler will not be aware of these instructions and will fail to compile any code that uses them.

Here is the assembly code of the `sad_neon` function as displayed by `objdump -S dotprod1`:

```asm
0000000000000a10 <sad_neon>:
 a10:   7100007f        cmp     w3, #0x0
 a14:   5400030d        b.le    a74 <sad_neon+0x64>
 a18:   4f000402        movi    v2.4s, #0x0
 a1c:   93407c46        sxtw    x6, w2
 a20:   4f00e423        movi    v3.16b, #0x1
 a24:   52800005        mov     w5, #0x0                        // #0
 a28:   d2800004        mov     x4, #0x0                        // #0
 a2c:   7100005f        cmp     w2, #0x0
 a30:   5400012d        b.le    a54 <sad_neon+0x44>
 a34:   d503201f        nop
 a38:   3ce46800        ldr     q0, [x0, x4]
 a3c:   3ce46821        ldr     q1, [x1, x4]
 a40:   91004084        add     x4, x4, #0x10
 a44:   6e217400        uabd    v0.16b, v0.16b, v1.16b
 a48:   6e839402        udot    v2.4s, v0.16b, v3.16b
 a4c:   6b04005f        cmp     w2, w4
 a50:   54ffff4c        b.gt    a38 <sad_neon+0x28>
 a54:   110004a5        add     w5, w5, #0x1
 a58:   8b060000        add     x0, x0, x6
 a5c:   8b060021        add     x1, x1, x6
 a60:   6b05007f        cmp     w3, w5
 a64:   54fffe21        b.ne    a28 <sad_neon+0x18>  // b.any
 a68:   4eb1b840        addv    s0, v2.4s
 a6c:   1e260000        fmov    w0, s0
 a70:   d65f03c0        ret
 a74:   4f000402        movi    v2.4s, #0x0
 a78:   4eb1b840        addv    s0, v2.4s
 a7c:   1e260000        fmov    w0, s0
 a80:   d65f03c0        ret
 ```

You will note the use of the `uabd` and `udot` assembly instructions that correspond to the `vabdq_u8`/`vdotq_u32` intrinsics.

Now observe the equivalent Rust program using the same `std::arch` `dotprod` intrinsics:

```Rust
#![feature(stdarch_neon_dotprod)]

const N : usize = 32;

fn main() {
    let mut a: [u8; N*N] = [0; N*N];
    let mut b: [u8; N*N] = [0; N*N];

    init_vec(&mut a, &mut b, N, N);
    let sad : u32 = sad_vec(&a, &b, N, N);
    println!("sad = {:x}", sad);
}

fn init_vec(a: &mut [u8], b: &mut [u8], w: usize, h: usize) -> () {
    for i in 0..h {
        print!("A[{}] = [ ", i);
        for j in 0..w {
            a[i*w + j] = (i + j) as u8;
            print!("{:02x} ", a[i*w +j]);
        }
        println!("]");
        print!("B[{}] = [ ", i);
        for j in 0..w {
            b[i*w + j] = ((i + j) & 4) as u8;
            print!("{:02x} ", b[i*w +j]);
        }
        println!("]");
    }
}

#[inline(never)]
fn sad_vec(a: &[u8], b: &[u8], w: usize, h: usize) -> u32 {
    #[cfg(target_arch = "aarch64")]
    {
        use std::arch::is_aarch64_feature_detected;
        if is_aarch64_feature_detected!("neon") {
            return unsafe { sad_vec_asimd(a, b, w, h) };
        }
    }
    // Scalar implementation should be included here as fallback
    return 0
}

#[cfg(target_arch = "aarch64")]
#[target_feature(enable = "neon")]
unsafe fn sad_vec_asimd(a: &[u8], b: &[u8], w: usize, h: usize) -> u32 {
    use std::arch::aarch64::*;

    let mut sum : uint32x4_t = vdupq_n_u32(0);

    for i in 0..h {
        for j in (0..w).step_by(16) {
            let va: uint8x16_t = vld1q_u8(&a[i*w + j]);
            let vb: uint8x16_t = vld1q_u8(&b[i*w + j]);
            let diff: uint8x16_t = vabdq_u8(va, vb);
            sum = vdotq_u32(sum, diff, vdupq_n_u8(1));
        }
    }
    return vaddvq_u32(sum);
}
```

More or less the same comments apply here. The use of intrinsics is pretty straightforward as it looks very similar to the C implementation.

Save this file under `dotprod2.rs`, compile it and run it:

```bash { output_lines = "3-10" }
rustc -O dotprod2.rs
./dotprod2
A[0] = [ 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f ]
B[0] = [ 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 ]
A[1] = [ 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 20 ]
B[1] = [ 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 ]
...
A[30] = [ 1e 1f 20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d ]
B[30] = [ 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 ]
A[31] = [ 1f 20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e ]
B[31] = [ 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 04 00 00 00 00 04 04 04 ]
sad = 7400
```

As you can see both executables produce the same output, so at least the code is correct.

Now observe the generated assembly using `objdump -S dotprod2`

```asm
0000000000006394 <_ZN4core9core_arch10arm_shared4neon9generated9vdotq_u3217h5c7bc8d63e4a993fE>:
    6394:       3dc00000        ldr     q0, [x0]
    6398:       3dc00021        ldr     q1, [x1]
    639c:       3dc00042        ldr     q2, [x2]
    63a0:       6e829420        udot    v0.4s, v1.16b, v2.16b
    63a4:       3d800100        str     q0, [x8]
    63a8:       d65f03c0        ret

0000000000006690 <_ZN8dotprod27sad_vec17h827a107d303290b5E>:
    6690:       d101c3ff        sub     sp, sp, #0x70
    6694:       f90023fe        str     x30, [sp, #64]
    6698:       a90557f6        stp     x22, x21, [sp, #80]
    669c:       a9064ff4        stp     x20, x19, [sp, #96]
    66a0:       aa0103f3        mov     x19, x1
    66a4:       aa0003f4        mov     x20, x0
    66a8:       6f00e400        movi    v0.2d, #0x0
    66ac:       4f00e423        movi    v3.16b, #0x1
    66b0:       aa1f03f5        mov     x21, xzr
    66b4:       aa1f03e8        mov     x8, xzr
    66b8:       3ce86a81        ldr     q1, [x20, x8]
    66bc:       3ce86a62        ldr     q2, [x19, x8]
    66c0:       91004116        add     x22, x8, #0x10
    66c4:       910003e8        mov     x8, sp
    66c8:       910043e0        add     x0, sp, #0x10
    66cc:       910083e1        add     x1, sp, #0x20
    66d0:       6e227421        uabd    v1.16b, v1.16b, v2.16b
    66d4:       9100c3e2        add     x2, sp, #0x30
    66d8:       3d800fe3        str     q3, [sp, #48]
    66dc:       ad0087e0        stp     q0, q1, [sp, #16]
    66e0:       97ffff2d        bl      6394 <_ZN4core9core_arch10arm_shared4neon9generated9vdotq_u3217h5c7bc8d63e4a993fE>
    66e4:       4f00e423        movi    v3.16b, #0x1
    66e8:       3dc003e0        ldr     q0, [sp]
    66ec:       f10082df        cmp     x22, #0x20
    66f0:       aa1603e8        mov     x8, x22
    66f4:       54fffe21        b.ne    66b8 <_ZN8dotprod27sad_vec17h827a107d303290b5E+0x28>  // b.any
    66f8:       910006b5        add     x21, x21, #0x1
    66fc:       91008273        add     x19, x19, #0x20
    6700:       91008294        add     x20, x20, #0x20
    6704:       f10082bf        cmp     x21, #0x20
    6708:       54fffd61        b.ne    66b4 <_ZN8dotprod27sad_vec17h827a107d303290b5E+0x24>  // b.any
    670c:       4eb1b800        addv    s0, v0.4s
    6710:       a9464ff4        ldp     x20, x19, [sp, #96]
    6714:       a94557f6        ldp     x22, x21, [sp, #80]
    6718:       f94023fe        ldr     x30, [sp, #64]
    671c:       1e260000        fmov    w0, s0
    6720:       9101c3ff        add     sp, sp, #0x70
    6724:       d65f03c0        ret
```

You might notice something strange. Where there should be a `udot` instruction there is a `bl` which indicates a branch, and we see that the `udot` instruction is indeed called in another function, which does the loads again.

This certainly seems counter-intuitive and difficult to comprehend. The reason for this is that in contrast to C, Rust treats the intrinsics like normal functions.

Like functions, inlining them is not always guaranteed. If it is possible to inline the intrinsic, then code generation and performance is almost the same as the one you get using C. If however, it is not possible, then you will find that the same code in Rust performs much worse due to this exact reason.

Because of this, you have to be vigilant that your SIMD Rust code generates the expected assembly. So, how can you fix this behaviour and get the generated code that you expect?

As you have already seen, Rust is quite peculiar about the enabled target features. In this case, you have to remember to add that `dotprod` is the required target feature that you want to use. So first you have to change it in the function `sad_vec_asimd`:

```Rust
#[cfg(target_arch = "aarch64")]
#[target_feature(enable = "dotprod")]
unsafe fn sad_vec_asimd(a: &[u8], b: &[u8], w: usize, h: usize) -> u32 {
```

Remember that `neon` is implied with `dotprod` so there is no need to add it as well.

Secondly, you also need to add the `#!feature` for the module's code generation at the top of the file:

```Rust
#![feature(stdarch_neon_dotprod)]
```

Save the file again and recompile as before.

```bash
rustc -O dotprod2.rs
```

Let's look at the assembly output once more:

```asm
000000000000667c <_ZN8dotprod213sad_vec_asimd17h2989b6ba09be74edE>:
    667c:       6f00e400        movi    v0.2d, #0x0
    6680:       4f00e421        movi    v1.16b, #0x1
    6684:       aa1f03e8        mov     x8, xzr
    6688:       8b080009        add     x9, x0, x8
    668c:       8b08002a        add     x10, x1, x8
    6690:       91008108        add     x8, x8, #0x20
    6694:       ad401542        ldp     q2, q5, [x10]
    6698:       f110011f        cmp     x8, #0x400
    669c:       ad401123        ldp     q3, q4, [x9]
    66a0:       6e227462        uabd    v2.16b, v3.16b, v2.16b
    66a4:       6e819440        udot    v0.4s, v2.16b, v1.16b
    66a8:       6e257482        uabd    v2.16b, v4.16b, v5.16b
    66ac:       6e819440        udot    v0.4s, v2.16b, v1.16b
    66b0:       54fffec1        b.ne    6688 <_ZN8dotprod213sad_vec_asimd17h2989b6ba09be74edE+0xc>  // b.any
    66b4:       4eb1b800        addv    s0, v0.4s
    66b8:       1e260000        fmov    w0, s0
    66bc:       d65f03c0        ret
```

This output is much better and we see that the compile automatically unrolled the loop twice because it was able to figure out that the number of iterations was small. Increasing the iterations will probably disable aggressive unrolling but it will at least inline the intrinsics properly.

In the next section you will learn one more important thing you need to know about the use of SIMD intrinsics in Rust.
