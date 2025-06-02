---
title: Matrix transpose
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you will build and run C and Rust examples to perform a matrix transpose. 
 
Shown below is a simple program in C that does a matrix transpose operation on a 4x4 matrix of `uint16_t` elements. Copy and save the contents in a file named `transpose1.c`:

```C
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <arm_neon.h>

#define N 4

void init_vec(uint16_t *A) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      A[i*N + j] = 4*i + j + 1;
    }
  }
}

void print_vec(uint16_t *A) {
  printf("A[] = \n");
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      printf("%02x ", A[i*N + j]);
    }
    printf("\n");
  }
}

void transpose_s16_4x4(int16_t *a) {
  int16x4_t va[N];
  va[0] = vld1_s16(&a[0]);
  va[1] = vld1_s16(&a[4]);
  va[2] = vld1_s16(&a[8]);
  va[3] = vld1_s16(&a[12]);

  const int16x4x2_t b0 = vtrn_s16(va[0], va[1]);
  const int16x4x2_t b1 = vtrn_s16(va[2], va[3]);

  const int32x2x2_t c0 = vtrn_s32(vreinterpret_s32_s16(b0.val[0]),
                                  vreinterpret_s32_s16(b1.val[0]));
  const int32x2x2_t c1 = vtrn_s32(vreinterpret_s32_s16(b0.val[1]),
                                  vreinterpret_s32_s16(b1.val[1]));

  vst1_s16(&a[0], vreinterpret_s16_s32(c0.val[0]));
  vst1_s16(&a[4], vreinterpret_s16_s32(c1.val[0]));
  vst1_s16(&a[8], vreinterpret_s16_s32(c0.val[1]));
  vst1_s16(&a[12], vreinterpret_s16_s32(c1.val[1]));
}

int main() {
    int16_t A[N*N];

    init_vec(A);
    print_vec(A);
    transpose_s16_4x4(A);
    print_vec(A);
}
```

Compile the program as follows:

```bash 
gcc -O3 transpose1.c -o transpose1
```
Run the program:
```bash
./transpose1
```
The output should look like the following:
```output
A[] =
0001 0002 0003 0004
0005 0006 0007 0008
0009 000a 000b 000c
000d 000e 000f 0010
A[] =
0001 0005 0009 000d
0002 0006 000a 000e
0003 0007 000b 000f
0004 0008 000c 0010
```

Note the special data types `int16x4x2_t` and `int32x2x2_t` which are used by the transpose `vtrn_s16` and `vtrn_s32` respectively. The pairs denote that there are going to be two instructions executed with a specific outcome. The corresponding assembly instructions executed are `trn1`/`trn2` for the first intrinsic and `zip1`/`zip2` for the second intrinsic.

Generate the disassembly output as per below:
```bash
objdump -S transpose1
```
The disassembly output of the `transpose_s16_4x4` function should look like the following:
```asm
00000000000008f0 <transpose_s16_4x4>:
 8f0:   6d400c00        ldp     d0, d3, [x0]
 8f4:   6d411001        ldp     d1, d4, [x0, #16]
 8f8:   0e432802        trn1    v2.4h, v0.4h, v3.4h
 8fc:   0e436800        trn2    v0.4h, v0.4h, v3.4h
 900:   0e442823        trn1    v3.4h, v1.4h, v4.4h
 904:   0e446821        trn2    v1.4h, v1.4h, v4.4h
 908:   0e833844        zip1    v4.2s, v2.2s, v3.2s
 90c:   0e837842        zip2    v2.2s, v2.2s, v3.2s
 910:   0e813803        zip1    v3.2s, v0.2s, v1.2s
 914:   0e817800        zip2    v0.2s, v0.2s, v1.2s
 918:   6d000c04        stp     d4, d3, [x0]
 91c:   6d010002        stp     d2, d0, [x0, #16]
 920:   d65f03c0        ret
```

This looks fairly straightforward with the expected sequence of instructions.

Now create an equivalent program implemented in Rust. Save the contents shown below in a file named `transpose2.rs`:

```Rust
const N : usize = 4;

fn main() {
    let mut a: [i16; N*N] = [0; N*N];

    init_vec(&mut a);
    print_vec(&a);
    transpose_s16_4x4(&mut a);
    print_vec(&a);
}

fn init_vec(a: &mut [i16; N*N]) -> () {
    for i in 0..N {
        for j in 0..N {
            a[i*N + j] = (4*i + j + 1) as i16;
        }
    }
}

fn print_vec(a: &[i16; N*N]) -> () {
    println!("A[] =");
    for i in 0..N {
        for j in 0..N {
            print!("{:02x} ", a[i*N + j]);
        }
        println!();
    }
}

#[inline(never)]
fn transpose_s16_4x4(a: &mut [i16]) -> () {
    #[cfg(target_arch = "aarch64")]
    {
        use std::arch::is_aarch64_feature_detected;
        if is_aarch64_feature_detected!("neon") {
            return unsafe { transpose_s16_4x4_asimd(a) };
        }
    }
    // Scalar implementation should be included here as fallback
}

#[cfg(target_arch = "aarch64")]
#[target_feature(enable = "neon")]
unsafe fn transpose_s16_4x4_asimd(a: &mut [i16]) -> () {
    use std::arch::aarch64::*;
    let va: [int16x4_t; N] = [ vld1_s16(&a[0]), vld1_s16(&a[4]), vld1_s16(&a[8]), vld1_s16(&a[12]) ];

    let b0 : int16x4x2_t = vtrn_s16(va[0], va[1]);
    let b1 : int16x4x2_t = vtrn_s16(va[2], va[3]);

    let c0 : int32x2x2_t = vtrn_s32(vreinterpret_s32_s16(b0.0),
                                    vreinterpret_s32_s16(b1.0));
    let c1 : int32x2x2_t = vtrn_s32(vreinterpret_s32_s16(b0.1),
                                    vreinterpret_s32_s16(b1.1));

    vst1_s16(&mut a[0], vreinterpret_s16_s32(c0.0));
    vst1_s16(&mut a[4], vreinterpret_s16_s32(c1.0));
    vst1_s16(&mut a[8], vreinterpret_s16_s32(c0.1));
    vst1_s16(&mut a[12], vreinterpret_s16_s32(c1.1));
}
```

You will note two important differences here:

* Initialization of the `int16x4_t va` array at the start of the `transpose_s16_4x4_asimd` function.
  - In C you can just declare the variable `va` and the compiler will not complain. The compiler knows that the SIMD variable will be immediately initialized by the respective load instructions `vld1q_s16`.
  - In Rust this is not the case, as the compiler insists on *all* variables being initialized on definition. It is much better to initialize the array with all elements right at the beginning (you could do that in C as well but it's not enforced unlike in Rust).
* meta-vector constructs such as `int16x4x2_t` and `int32x2x2_t` are defined as structs in C with each element as the corresponding element of the nested array `val[]`. In Rust, however, they are defined as tuples, and each element is accessed directly as `0` or `1` in these cases, e.g., `b0.0` and `c1.1`.

Compile the program as follows:

```bash 
rustc -O transpose2.rs
```

Run the program:
```bash
./transpose2
```

The output should look similar to the below:
```output
A[] =
A[] =
0001 0002 0003 0004
0005 0006 0007 0008
0009 000a 000b 000c
000d 000e 000f 0010
A[] =
0001 0005 0009 000d
0002 0006 000a 000e
0003 0007 000b 000f
0004 0008 000c 0010
```
Generate the disassembly output:
```bash
objdump -S transpose2
```

The disassembly output of the Rust implementation of `transpose_s16_4x4_asimd` is shown below:

```asm
00000000000064b0 <_ZN10transpose217transpose_s16_4x417ha75632bf6146b962E>:
    64b0:       6d400400        ldp     d0, d1, [x0]
    64b4:       6d410c02        ldp     d2, d3, [x0, #16]
    64b8:       0e412804        trn1    v4.4h, v0.4h, v1.4h
    64bc:       0e416800        trn2    v0.4h, v0.4h, v1.4h
    64c0:       0e432845        trn1    v5.4h, v2.4h, v3.4h
    64c4:       0e436841        trn2    v1.4h, v2.4h, v3.4h
    64c8:       0e853882        zip1    v2.2s, v4.2s, v5.2s
    64cc:       0e813803        zip1    v3.2s, v0.2s, v1.2s
    64d0:       0e857884        zip2    v4.2s, v4.2s, v5.2s
    64d4:       0e817800        zip2    v0.2s, v0.2s, v1.2s
    64d8:       6d000c02        stp     d2, d3, [x0]
    64dc:       6d010004        stp     d4, d0, [x0, #16]
    64e0:       d65f03c0        ret
```
As you would expect this matches the C disassembly.

In the next section, you will look at a more complex example.
