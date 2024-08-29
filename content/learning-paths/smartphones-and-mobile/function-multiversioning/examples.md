---
title: Examples
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Examples

#### Code Generation example

In this example we have specified two versions of `foo` using the `target_clones` attribute (the order in which they are listed does not matter). At certain optimization levels compilers can decide to perform loop vectorization depending on the target's vector capabilities. Our intention is to enable the compiler to use SVE instructions in the specialized case, whilst restricting it to use only Armv8 instructions in the default one.

loop.c
```c
__attribute__((target_clones("sve", "default")))
int foo(int *v, unsigned n) {
  int s = 0;
  for (unsigned i = 0; i < n; ++i)
    if (v[i] > 0)
      s += v[i] * i;
  return s;
}
```

Below are the commands for compiling this example using either `clang` or `gcc`.
```
$ clang --target=aarch64-linux-gnu -march=armv8-a -O3 --rtlib=compiler-rt -S -o - loop.c
```
or
```
$ gcc -march=armv8-a -O3 -S -o - loop.c
```
Note that when using the `clang` compiler, the option `--rtlib=compiler-rt` should be specified on the command line. This allows the compiler to generate runtime checks for detecting the presence of hardware features on your host target.

Here is the generated compiler output for the SVE version of `foo` (using `clang`):
```
	.text
	.globl	foo._Msve
	.p2align	2
	.type	foo._Msve,@function
foo._Msve:
	cbz	w1, .LBB0_3
	mov	w9, w1
	cnth	x8
	cmp	x8, x9
	b.ls	.LBB0_4
	mov	x10, xzr
	mov	w8, wzr
	b	.LBB0_7
.LBB0_3:
	mov	w8, wzr
	mov	w0, w8
	ret
.LBB0_4:
	ptrue	p0.s
	mov	z0.s, #0
	index	z2.s, #0, #1
	cntw	x10
	sub	x12, x8, #1
	rdvl	x13, #1
	mov	z1.s, w10
	and	x12, x9, x12
	mov	x11, xzr
	mov	z3.d, z0.d
	sub	x10, x9, x12
	add	x13, x0, x13
.LBB0_5:
	ld1w	{ z4.s }, p0/z, [x0, x11, lsl #2]
	ld1w	{ z5.s }, p0/z, [x13, x11, lsl #2]
	add	z6.s, z2.s, z1.s
	add	x11, x11, x8
	cmpgt	p1.s, p0/z, z4.s, #0
	cmpgt	p2.s, p0/z, z5.s, #0
	cmp	x10, x11
	mla	z0.s, p1/m, z4.s, z2.s
	mla	z3.s, p2/m, z5.s, z6.s
	add	z2.s, z6.s, z1.s
	b.ne	.LBB0_5
	add	z0.s, z3.s, z0.s
	uaddv	d0, p0, z0.s
	fmov	x8, d0
	cbz	x12, .LBB0_8
.LBB0_7:
	ldr	w11, [x0, x10, lsl #2]
	mul	w12, w11, w10
	cmp	w11, #0
	add	x10, x10, #1
	csel	w11, w12, wzr, gt
	cmp	x9, x10
	add	w8, w11, w8
	b.ne	.LBB0_7
.LBB0_8:
	mov	w0, w8
	ret
```

This is the default version of `foo`:
```
	.section	.rodata.cst16,"aM",@progbits,16
	.p2align	4, 0x0
.LCPI2_0:
	.word	0
	.word	1
	.word	2
	.word	3
	.text
	.globl	foo.default
	.p2align	2
	.type	foo.default,@function
foo.default:
	cbz	w1, .LBB2_3
	cmp	w1, #8
	mov	w9, w1
	b.hs	.LBB2_4
	mov	x10, xzr
	mov	w8, wzr
	b	.LBB2_7
.LBB2_3:
	mov	w0, wzr
	ret
.LBB2_4:
	movi	v0.2d, #0000000000000000
	movi	v1.4s, #4
	adrp	x8, .LCPI2_0
	movi	v2.4s, #8
	movi	v3.2d, #0000000000000000
	and	x10, x9, #0xfffffff8
	ldr	q4, [x8, :lo12:.LCPI2_0]
	add	x8, x0, #16
	mov	x11, x10
.LBB2_5:
	add	v5.4s, v4.4s, v1.4s
	ldp	q6, q7, [x8, #-16]
	subs	x11, x11, #8
	add	x8, x8, #32
	mul	v16.4s, v6.4s, v4.4s
	cmgt	v6.4s, v6.4s, #0
	add	v4.4s, v4.4s, v2.4s
	mul	v5.4s, v7.4s, v5.4s
	cmgt	v7.4s, v7.4s, #0
	and	v6.16b, v16.16b, v6.16b
	and	v5.16b, v5.16b, v7.16b
	add	v0.4s, v6.4s, v0.4s
	add	v3.4s, v5.4s, v3.4s
	b.ne	.LBB2_5
	add	v0.4s, v3.4s, v0.4s
	cmp	x10, x9
	addv	s0, v0.4s
	fmov	w8, s0
	b.eq	.LBB2_8
.LBB2_7:
	ldr	w11, [x0, x10, lsl #2]
	mul	w12, w11, w10
	cmp	w11, #0
	add	x10, x10, #1
	csel	w11, w12, wzr, gt
	cmp	x9, x10
	add	w8, w11, w8
	b.ne	.LBB2_7
.LBB2_8:
	mov	w0, w8
	ret
```

Any calls to `foo` are routed through `foo.resolver`. This is the function which contains the runtime checks for feature detection. More on this later.
```
	.section	.text.foo.resolver,"axG",@progbits,foo.resolver,comdat
	.weak	foo.resolver
	.p2align	2
	.type	foo.resolver,@function
foo.resolver:
	str	x30, [sp, #-16]!
	bl	__init_cpu_features_resolver
	adrp	x8, __aarch64_cpu_features+3
	adrp	x9, foo._Msve
	add	x9, x9, :lo12:foo._Msve
	ldrb	w8, [x8, :lo12:__aarch64_cpu_features+3]
	tst	w8, #0x40
	adrp	x8, foo.default
	add	x8, x8, :lo12:foo.default
	csel	x0, x8, x9, eq
	ldr	x30, [sp], #16
	ret
```

The called symbol `foo` is an indirect function (IFUNC) which points to the resolver.
```
.weak	foo
.type	foo,@gnu_indirect_function
.set foo, foo.resolver
```

The names `foo._Msve` and `foo.default` correspond to the function versions of `foo`. See the [Arm C Language Extensions](https://arm-software.github.io/acle/main/acle.html#name-mangling) document for more details on the name mangling rules.

#### Runtime example with use of ACLE intrinsics

In this example we are computing the dot product of two vectors using ACLE intrinsics. Our intention is to enable the compiler to use SVE instructions in the specialized case, whilst restricting it to use only Armv8 instructions in the default one.

More details on the default implementation can be found here: [Implement dot product of two vectors](/learning-paths/smartphones-and-mobile/android_neon/dot_product_neon)

dotprod.c
```c
#include <stdio.h>
#include <stdlib.h>
#include <arm_neon.h>
#include <arm_sve.h>

__attribute__((target_version("sve")))
int dotProduct(short *vec1, short* vec2, short len) {
  printf("Running the sve version of dotProduct\n");

  int i = 0;
  svbool_t pg = svwhilelt_b32(i, len);
  svbool_t pt = svptrue_b32();
  svint32_t res = svdup_s32(0);
  while (svptest_any(pt, pg)) {
    svint32_t sv1 = svld1sh_s32(pg, vec1 + i);
    svint32_t sv2 = svld1sh_s32(pg, vec2 + i);
    res = svmla_m(pg, res, sv1, sv2);
    i += svcntw();
    pg = svwhilelt_b32(i, len);
  }
  return (int) svaddv(pt, res);
}

__attribute__((target_version("default")))
int dotProduct(short* vec1, short* vec2, short len) {
  printf("Running the default version of dotProduct\n");

  const short transferSize = 4;
  short segments = len / transferSize;

  // 4-element vector of zeros
  int32x4_t partialSumsNeon = vdupq_n_s32(0);
  int32x4_t sum1 = vdupq_n_s32(0);
  int32x4_t sum2 = vdupq_n_s32(0);
  int32x4_t sum3 = vdupq_n_s32(0);
  int32x4_t sum4 = vdupq_n_s32(0);

  // Main loop (note that loop index goes through segments). Unroll with 4
  int i = 0;
  for(; i+3 < segments; i+=4) {
    // Load vector elements to registers
    int16x8_t v11 = vld1q_s16(vec1);
    int16x4_t v11_low = vget_low_s16(v11);
    int16x4_t v11_high = vget_high_s16(v11);

    int16x8_t v12 = vld1q_s16(vec2);
    int16x4_t v12_low = vget_low_s16(v12);
    int16x4_t v12_high = vget_high_s16(v12);

    int16x8_t v21 = vld1q_s16(vec1+8);
    int16x4_t v21_low = vget_low_s16(v21);
    int16x4_t v21_high = vget_high_s16(v21);

    int16x8_t v22 = vld1q_s16(vec2+8);
    int16x4_t v22_low = vget_low_s16(v22);
    int16x4_t v22_high = vget_high_s16(v22);

    // Multiply and accumulate: partialSumsNeon += vec1Neon * vec2Neon
    sum1 = vmlal_s16(sum1, v11_low, v12_low);
    sum2 = vmlal_s16(sum2, v11_high, v12_high);
    sum3 = vmlal_s16(sum3, v21_low, v22_low);
    sum4 = vmlal_s16(sum4, v21_high, v22_high);

    vec1 += 16;
    vec2 += 16;
  }
  partialSumsNeon = sum1 + sum2 + sum3 + sum4;

  // Sum up remain parts
  int remain = len % transferSize;
  for(i = 0; i < remain; i++) {
    int16x4_t vec1Neon = vld1_s16(vec1);
    int16x4_t vec2Neon = vld1_s16(vec2);
    partialSumsNeon = vmlal_s16(partialSumsNeon, vec1Neon, vec2Neon);
    vec1 += 4;
    vec2 += 4;
  }

  // Store partial sums
  int partialSums[transferSize];
  vst1q_s32(partialSums, partialSumsNeon);

  // Sum up partial sums
  int result = 0;
  for(i = 0; i < transferSize; i++)
    result += partialSums[i];

  return result;
}

int scanVector(short *vec, short len) {
  short *p = vec;
  for (int i = 0; i < len; i++, p++)
    if (scanf("%hd", p) != 1)
      return 0;
  return 1;
}

int main(int argc, char **argv) {
  if (argc == 2) {
    int n = atoi(argv[1]);
    if (n < 16 || n > 1024)
      return -1;
    short v1[1024];
    short v2[1024];
    if (!scanVector(v1, n) || !scanVector(v2, n))
      return -1;
    int result = dotProduct(v1, v2, n);
    printf("dotProduct = %d\n", result);
  }
  return 0;
}
```

We are compiling and running the above example on hardware that has both SVE and Armv8 instructions:
```
$ clang --target=aarch64-linux-gnu -march=armv8-a -O3 dotprod.c --rtlib=compiler-rt
```
or
```
$ g++ -march=armv8-a -O3 dotprod.c
```
Note that gcc-14 does not yet support `target_version` when using the c-frontend, therefore it is recommended to use g++-14 instead.

```
$ echo 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 | ./a.out 16
$ Running the sve version of dotProduct
$ dotProduct = 32
```
The SVE version is being selected because it has higher priority than the default, as indicated by the table [here](https://arm-software.github.io/acle/main/acle.html#mapping).

#### Runtime example with use of inline assembly

In this example we are manipulating strings with the use of SVE2 instructions via inline assembly. Moreover we rely on the compiler in generating an optimized version of memcpy using FEAT_MOPS.

More details on the SkipWord implementation can be found here: [SVE Programming Examples](https://developer.arm.com/documentation/dai0548/latest)

skip-word.c
```c
#include <stdio.h>
#include <string.h>

__attribute__((target_clones("default", "mops")))
char *CopyWord(char *dst, const char *src) {
  size_t n = strlen(src);
  memcpy(dst, src, n + 1);
  return dst + n;
}

__attribute__((target_version("sve2")))
const char *SkipWord(const char *p, const char *end) {
  printf("Running the sve2 SkipWord\n");
  __asm volatile (
    "mov w2, #0xd090000\n\t"
    "add w2, w2, #0xa20\n\t"
    "mov z1.s, w2\n\t"
    "whilelt p0.b, %0, %1\n"
    "1:\n\t"
    "ld1b z0.b, p0/z, [%0]\n\t"
    "match p1.b, p0/z, z0.b, z1.b\n\t"
    "b.any 2f\n\t"
    "incb %0\n\t"
    "whilelt p0.b, %0, %1\n\t"
    "b.first 1b\n\t"
    "mov %0, %1\n\t"
    "b 3f\n"
    "2:\n\t"
    "brkb p2.b, p0/z, p1.b\n\t"
    "incp %0, p2.b\n"
    "3:\n\t"
    : "+r" (p)
    : "r" (end)
    : "w2", "p0", "p1", "p2", "z0", "z1");
    return p;
}

__attribute__((target_version("default")))
const char *SkipWord(const char *p, const char *end) {
  printf("Running the default SkipWord\n");
  while (p != end && *p != ' ' && *p != '\n' && *p != '\r' && *p != '\t')
    p++;
  return p;
}

int main(int argc, char **argv) {
  if (argc != 3)
    return -1;
  char buffer[256];
  char *end = CopyWord(buffer, argv[1]);
  end = CopyWord(end, argv[2]);
  printf("%s\n", buffer);
  printf("%s\n", SkipWord(buffer, buffer + strlen(buffer)));
  return 0;
}
```

We are compiling and running the above example on hardware that has both SVE2 and Armv8 instructions:
```
$ clang --target=aarch64-linux-gnu -march=armv8-a -O3 skip-word.c --rtlib=compiler-rt
```
or
```
$ g++ -march=armv8-a -O3 skip-word.c
```
Note that gcc++-14 does not support "mops" as a Function Multiversioning feature, so to compile this example with gcc remove the `target_clones` from CopyWord.

```
$ ./a.out "foo 2" " bar"
$ foo 2 bar
$ Running the sve2 SkipWord
$  2 bar
```
The SVE2 version is being selected because it has higher priority than the default, as indicated by the table [here](https://arm-software.github.io/acle/main/acle.html#mapping).
