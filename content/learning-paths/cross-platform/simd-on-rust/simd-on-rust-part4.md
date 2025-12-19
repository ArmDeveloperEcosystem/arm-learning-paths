---
title: A more complicated example
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you will create a function that implements the common operation `fdct_round_shift(a * c1 +/- b * c2)`. This operation is the basis of many discrete cosine transform (DCT) algorithms used in multiple video codecs, including VP9, AV1, etc.

It is called a 'butterfly' operation in DCT and it is defined as the following:

```C
#define ROUND_POWER_OF_TWO(value, n) (((value) + (1 << ((n)-1))) >> (n))
#define fdct_round_shift(input) ROUND_POWER_OF_TWO(input, DCT_CONST_BITS)
```

where `DCT_CONST_BITS` is defined with the value `14` for many codecs.

SIMD implementations are able to calculate both the expressions `fdct_round_shift(a * c1 + b * c2)` and `fdct_round_shift(a * c1 - b * c2)` in a single function, for 8 x 16-bit pixel elements, reusing computations and saving multiple instructions in the process.

Here is what one implementation looks like, as [taken from the `libvpx` video codec library](https://chromium.googlesource.com/webm/libvpx/+/refs/heads/main/vpx_dsp/arm/fdct_neon.h):

```C
#define DCT_CONST_BITS 14

// fdct_round_shift(a * c1 +/- b * c2)
// Variant that performs normal implementation on half vector
// more accurate does 32-bit processing, takes and returns 16-bit values
// returns narrowed results
static INLINE void butterfly_two_coeff_half(const int16x4_t a,
                                            const int16x4_t b,
                                            const tran_coef_t c1,
                                            const tran_coef_t c2,
                                            int16x4_t *add, int16x4_t *sub) {
  const int32x4_t a1 = vmull_n_s16(a, c1);
  const int32x4_t a2 = vmull_n_s16(a, c2);
  const int32x4_t sum = vmlal_n_s16(a1, b, c2);
  const int32x4_t diff = vmlsl_n_s16(a2, b, c1);
  *add = vqrshrn_n_s32(sum, DCT_CONST_BITS);
  *sub = vqrshrn_n_s32(diff, DCT_CONST_BITS);
}
```

The above algorithm uses the widening versions of `mul` which is `mull`. This will take 16-bit quantities and produce a 32-bit product. In this case, the initial half of the 4x16-bit vectors produce products in 4 x 32-bit vectors, `a1`, `a2`. These vectors hold the quantities for the first part of the expression `a * c1` and `a * c2`.

Next the `vmlal_n_s16` and `vmlsl_n_s16` intrinsics are used which produce the quantities `a * c1 + b * c2` or `a * c1 - b * c2` respectively.

Finally, the rounding to the power of two is performed using a single intrinsic `vqrshrn_n_s32` which also narrows the results to half the original size. In effect this calls the `SQRSHRN` instruction which performs exactly the `ROUND_POWER_OF_TWO` operation, shifting right by `DCT_CONST_BITS`. The results are placed in the respective pointer variables, as C does not allow returning a pair of values.

### A complete DCT 4x4 example

Copy the following program which includes the function above and save it in a file named `butterfly1.c`:

```C
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <arm_neon.h>

#define N 4
#define DCT_CONST_BITS 14

static const int16_t cospi_8_64 = 15137;
static const int16_t cospi_16_64 = 11585;
static const int16_t cospi_24_64 = 6270;

void init_vec(int16_t *A) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      A[i*N + j] = 4*i + j + 1;
    }
  }
}

void print_vec(int16_t *A) {
  printf("A[] = \n");
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      printf("%04x ", (uint16_t)(A[i*N + j]));
    }
    printf("\n");
  }
}

// fdct_round_shift((a +/- b) * c)
// Variant that performs normal implementation on half vector
// more accurate does 32-bit processing, takes and returns 16-bit values
// returns narrowed results
static inline void butterfly_one_coeff_half(const int16x4_t a,
                                            const int16x4_t b,
                                            const int16_t c,
                                            int16x4_t *add, int16x4_t *sub) {
  const int32x4_t a32 = vmull_n_s16(a, c);
  const int32x4_t sum = vmlal_n_s16(a32, b, c);
  const int32x4_t diff = vmlsl_n_s16(a32, b, c);
  *add = vqrshrn_n_s32(sum, DCT_CONST_BITS);
  *sub = vqrshrn_n_s32(diff, DCT_CONST_BITS);
}

// fdct_round_shift(a * c1 +/- b * c2)
// Variant that performs normal implementation on half vector
// more accurate does 32-bit processing, takes and returns 16-bit values
// returns narrowed results
static inline void butterfly_two_coeff_half(const int16x4_t a,
                                            const int16x4_t b,
                                            const int16_t c1,
                                            const int16_t c2,
                                            int16x4_t *add, int16x4_t *sub) {
  const int32x4_t a1 = vmull_n_s16(a, c1);
  const int32x4_t a2 = vmull_n_s16(a, c2);
  const int32x4_t sum = vmlal_n_s16(a1, b, c2);
  const int32x4_t diff = vmlsl_n_s16(a2, b, c1);
  *add = vqrshrn_n_s32(sum, DCT_CONST_BITS);
  *sub = vqrshrn_n_s32(diff, DCT_CONST_BITS);
}

static inline void transpose_s16_4x4d(int16x4_t *a0, int16x4_t *a1,
                                      int16x4_t *a2, int16x4_t *a3) {
  const int16x4x2_t b0 = vtrn_s16(*a0, *a1);
  const int16x4x2_t b1 = vtrn_s16(*a2, *a3);

  const int32x2x2_t c0 = vtrn_s32(vreinterpret_s32_s16(b0.val[0]),
                                  vreinterpret_s32_s16(b1.val[0]));
  const int32x2x2_t c1 = vtrn_s32(vreinterpret_s32_s16(b0.val[1]),
                                  vreinterpret_s32_s16(b1.val[1]));

  *a0 = vreinterpret_s16_s32(c0.val[0]);
  *a1 = vreinterpret_s16_s32(c1.val[0]);
  *a2 = vreinterpret_s16_s32(c0.val[1]);
  *a3 = vreinterpret_s16_s32(c1.val[1]);
}

static inline void fdct4x4_pass1_neon(int16x4_t *in) {
  int16x4_t out[4];

  const int16x8_t input_01 = vcombine_s16(in[0], in[1]);
  const int16x8_t input_32 = vcombine_s16(in[3], in[2]);

  // in_0 +/- in_3, in_1 +/- in_2
  const int16x8_t s_01 = vaddq_s16(input_01, input_32);
  const int16x8_t s_32 = vsubq_s16(input_01, input_32);

  // step_0 +/- step_1, step_2 +/- step_3
  const int16x4_t s_0 = vget_low_s16(s_01);
  const int16x4_t s_1 = vget_high_s16(s_01);
  const int16x4_t s_2 = vget_high_s16(s_32);
  const int16x4_t s_3 = vget_low_s16(s_32);

  // fdct_round_shift(s_0 +/- s_1) * cospi_16_64
  butterfly_one_coeff_half(s_0, s_1, cospi_16_64, &out[0], &out[2]);

  // s_3 * cospi_8_64 + s_2 * cospi_24_64
  // s_3 * cospi_24_64 - s_2 * cospi_8_64
  butterfly_two_coeff_half(s_3, s_2, cospi_8_64, cospi_24_64, &out[1], &out[3]);

  transpose_s16_4x4d(&out[0], &out[1], &out[2], &out[3]);

  in[0] = out[0];
  in[1] = out[1];
  in[2] = out[2];
  in[3] = out[3];
}

void fdct4x4_neon(const int16_t *input, int16_t *final_output,
                      int stride) {
  // input[M * stride] * 16
  int16x4_t in[4];
  in[0] = vshl_n_s16(vld1_s16(input + 0 * stride), 4);
  in[1] = vshl_n_s16(vld1_s16(input + 1 * stride), 4);
  in[2] = vshl_n_s16(vld1_s16(input + 2 * stride), 4);
  in[3] = vshl_n_s16(vld1_s16(input + 3 * stride), 4);

  // If the very first value != 0, then add 1.
  if (input[0] != 0) {
    const int16x4_t one = vreinterpret_s16_s64(vdup_n_s64(1));
    in[0] = vadd_s16(in[0], one);
  }
  fdct4x4_pass1_neon(in);
  fdct4x4_pass1_neon(in);
  {
    // Not quite a rounding shift. Only add 1 despite shifting by 2.
    const int16x8_t one = vdupq_n_s16(1);
    int16x8_t out_01 = vcombine_s16(in[0], in[1]);
    int16x8_t out_23 = vcombine_s16(in[2], in[3]);
    out_01 = vshrq_n_s16(vaddq_s16(out_01, one), 2);
    out_23 = vshrq_n_s16(vaddq_s16(out_23, one), 2);
    vst1q_s16(final_output + 0 * 8, out_01);
    vst1q_s16(final_output + 1 * 8, out_23);
  }
}

int main() {
    int16_t a[N*N], dct[N*N];

    init_vec(a);
    print_vec(a);
    fdct4x4_neon(a, dct, N);
    print_vec(dct);
}
```

Compile the program:
```bash 
gcc -O3 butterfly1.c -o butterfly1
```
Run it as follows:
```bash
./butterfly1
```

The output should look like:
```output
A[] =
0001 0002 0003 0004
0005 0006 0007 0008
0009 000a 000b 000c
000d 000e 000f 0010
A[] =
0110 ffdc 0000 fffd
ff71 0000 0000 0000
0000 0000 0000 0000
fff6 0000 0000 0000
```

A 4x4 matrix `a` is initialized and a `fDCT` function is called on it. The function carries out 2 passes of the same algorithm on the elements of the array, calls the 2 butterfly functions (for one and two coefficients respectively) and transposes the results in between the calculations. The result is rounded and stored in the output buffer `dct`.

The [assembly output](/learning-paths/cross-platform/simd-on-rust/butterfly1.asm) is available separately due to its size.

Now create a Rust version of this algorithm and save the contents below in a file called `butterfly2.rs`:

```Rust
#[cfg(target_arch = "aarch64")]

use std::arch::aarch64::*;

const N : usize = 4;
const DCT_CONST_BITS : i32 = 14;

const COSPI_8_64  : i16 = 15137;
const COSPI_16_64 : i16 = 11585;
const COSPI_24_64 : i16 = 6270;

fn main() {
    let mut a: [i16; N*N] = [0; N*N];
    let mut dct: [i16; N*N] = [0; N*N];

    init_vec(&mut a);
    print_vec(&a);
    fdct4x4_vec(&a, &mut dct, N);
    print_vec(&dct);
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
            print!("{:04x} ", a[i*N + j]);
        }
        println!();
    }
}

unsafe fn transpose_s16_4x4(va: &mut [int16x4_t; N]) -> () {
    let b0 : int16x4x2_t = vtrn_s16(va[0], va[1]);
    let b1 : int16x4x2_t = vtrn_s16(va[2], va[3]);

    let c0 : int32x2x2_t = vtrn_s32(vreinterpret_s32_s16(b0.0),
                                    vreinterpret_s32_s16(b1.0));
    let c1 : int32x2x2_t = vtrn_s32(vreinterpret_s32_s16(b0.1),
                                    vreinterpret_s32_s16(b1.1));
    va[0] = vreinterpret_s16_s32(c0.0);
    va[1] = vreinterpret_s16_s32(c1.0);
    va[2] = vreinterpret_s16_s32(c0.1);
    va[3] = vreinterpret_s16_s32(c1.1);
}

// fdct_round_shift((a +/- b) * c)
unsafe fn butterfly_one_coeff_half(a: int16x4_t, b : int16x4_t, c: i16) -> (int16x4_t, int16x4_t) {
  let a32  : int32x4_t = vmull_n_s16(a, c);
  let sum  : int32x4_t = vmlal_n_s16(a32, b, c);
  let diff : int32x4_t = vmlsl_n_s16(a32, b, c);
  // Rust functions can return pair of values
  (vqrshrn_n_s32::<DCT_CONST_BITS>(sum), vqrshrn_n_s32::<DCT_CONST_BITS>(diff))
}

// fdct_round_shift(a * c1 +/- b * c2)
unsafe fn butterfly_two_coeff_half(a: int16x4_t, b : int16x4_t, c1: i16, c2: i16) -> (int16x4_t, int16x4_t) {
  let a1   : int32x4_t = vmull_n_s16(a, c1);
  let a2   : int32x4_t = vmull_n_s16(a, c2);
  let sum  : int32x4_t = vmlal_n_s16(a1, b, c2);
  let diff : int32x4_t = vmlsl_n_s16(a2, b, c1);
  // Rust functions can return pair of values
  (vqrshrn_n_s32::<DCT_CONST_BITS>(sum), vqrshrn_n_s32::<DCT_CONST_BITS>(diff))
}

unsafe fn fdct4x4_pass1_asimd(vin: &[int16x4_t; N], vout: &mut [int16x4_t; N]) -> () {
    let input_01 : int16x8_t = vcombine_s16(vin[0], vin[1]);
    let input_32 : int16x8_t = vcombine_s16(vin[3], vin[2]);

    // in_0 +/- in_3, in_1 +/- in_2
    let s_01 : int16x8_t = vaddq_s16(input_01, input_32);
    let s_32 : int16x8_t = vsubq_s16(input_01, input_32);

    // step_0 +/- step_1, step_2 +/- step_3
    let s_0 : int16x4_t = vget_low_s16(s_01);
    let s_1 : int16x4_t = vget_high_s16(s_01);
    let s_2 : int16x4_t = vget_high_s16(s_32);
    let s_3 : int16x4_t = vget_low_s16(s_32);

    // fdct_round_shift(s_0 +/- s_1) * cospi_16_64
    (vout[0], vout[2]) = butterfly_one_coeff_half(s_0, s_1, COSPI_16_64);

    // s_3 * cospi_8_64 + s_2 * cospi_24_64
    // s_3 * cospi_24_64 - s_2 * cospi_8_64
    (vout[1], vout[3]) = butterfly_two_coeff_half(s_3, s_2, COSPI_8_64, COSPI_24_64);

    transpose_s16_4x4(vout);
}

#[inline(never)]
fn fdct4x4_vec(input: &[i16], output: &mut [i16], stride: usize) -> () {
    #[cfg(target_arch = "aarch64")]
    {
        use std::arch::is_aarch64_feature_detected;
        if is_aarch64_feature_detected!("neon") {
            return unsafe { fdct4x4_vec_asimd(input, output, stride) };
        }
    }
    // Scalar implementation should be included here as fallback
}

unsafe fn fdct4x4_vec_asimd(input: &[i16], output: &mut [i16], stride: usize) -> () {

    // initialize array of vectors immediately
    let mut vin: [int16x4_t; N] = [ vld1_s16(&input[0 * stride]),
                                    vld1_s16(&input[1 * stride]),
                                    vld1_s16(&input[2 * stride]),
                                    vld1_s16(&input[3 * stride]) ];
    vin[0] = vshl_n_s16::<4>(vin[0]);
    vin[1] = vshl_n_s16::<4>(vin[1]);
    vin[2] = vshl_n_s16::<4>(vin[2]);
    vin[3] = vshl_n_s16::<4>(vin[3]);

    // If the very first value != 0, then add 1.
    if input[0] != 0 {
      let one: int16x4_t = vreinterpret_s16_s64(vdup_n_s64(1));
      vin[0] = vadd_s16(vin[0], one);
    }
    let mut vout : [int16x4_t; N] = [ vdup_n_s16(0); N ];
    fdct4x4_pass1_asimd(&vin, &mut vout);
    fdct4x4_pass1_asimd(&vout, &mut vin);

    // Not quite a rounding shift. Only add 1 despite shifting by 2.
    let one : int16x8_t = vdupq_n_s16(1);
    let mut out_01 : int16x8_t = vcombine_s16(vin[0], vin[1]);
    let mut out_23 : int16x8_t = vcombine_s16(vin[2], vin[3]);
    out_01 = vshrq_n_s16::<2>(vaddq_s16(out_01, one));
    out_23 = vshrq_n_s16::<2>(vaddq_s16(out_23, one));
    vst1q_s16(&mut output[ 0 * 8], out_01);
    vst1q_s16(&mut output[ 1 * 8], out_23);
}
```

Compile the program as follows:

```bash 
rustc -O butterfly2.rs
```
Run the program:
```bash
./butterfly2
```
The output should look like the following:
```output
A[] =
0001 0002 0003 0004
0005 0006 0007 0008
0009 000a 000b 000c
000d 000e 000f 0010
A[] =
0110 ffdc 0000 fffd
ff71 0000 0000 0000
0000 0000 0000 0000
fff6 0000 0000 0000
```

The [disassembly output](/learning-paths/cross-platform/simd-on-rust/butterfly2.asm) is available separately for size reasons. You will see that it is very similar to the C version, apart from the cpu feature check at the start.

### Comments

There are some things to highlight here:

* The config declaration `#[cfg(target_arch = "aarch64")]` and the `use std::arch::aarch64::*;` are used at the top of the file as there are many functions that need to use SIMD intrinsics and it is simpler than having to add it to every function.
* Rust functions can return pairs of values so there is no need for the pointer values of `add`, `sub` to be passed as arguments to the butterfly functions, as done in C.
This leads to more readable code as shown below (a similar thing can also be achieved with C++'s `std::pair`).
```Rust
  // Rust functions can return pair of values
  (vqrshrn_n_s32::<DCT_CONST_BITS>(sum), vqrshrn_n_s32::<DCT_CONST_BITS>(diff))
```
* You have probably noticed the different syntax for the intrinsics `vshl_n_s16`, `vqrshrn_n_s32` and `vshrq_n_s16`. The shift immediate is not passed as an argument but as a Rust *generics* parameter, which is similar to the C++ template system. In C you would just write the following:

```C
vin[0] = vshl_n_s16(vin[0], 4);
```
In Rust, while that syntax is still allowed, it is encouraged to use the new generics syntax:

```Rust
vin[0] = vshl_n_s16::<4>(vin[0]);
```

### An alternative way with std::simd

Although you could create this example with `std::simd`, it is not included in the learning path and is left as an exercise for you to experiment with.

