---
title: Example 1 - code generation
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This example specifies two versions of `sumPosEltsScaledByIndex` using the `target_clones` attribute. The order in which they are listed does not matter. 

At certain optimization levels, compilers can decide to perform loop vectorization depending on the target's vector capabilities. 

The intention is to enable the compiler to use SVE instructions in the specialized case, while restricting it to use only Armv8 instructions in the default case.

Use a text editor to create a file named `loop.c` with the code below:

```c
__attribute__((target_clones("sve", "default")))
int sumPosEltsScaledByIndex(int *v, unsigned n) {
  int s = 0;
  for (unsigned i = 0; i < n; ++i)
    if (v[i] > 0)
      s += v[i] * i;
  return s;
}
```

You can use either Clang or GCC to compile the code example.

To compile with Clang, run:

```console
clang --target=aarch64-linux-gnu -march=armv8-a -O3 --rtlib=compiler-rt -S -o - loop.c
```

To compile with GCC, use:

```console
gcc -march=armv8-a -O3 -S -o - loop.c
```

{{% notice Note %}}
When using the `clang` compiler, specify the option `--rtlib=compiler-rt` on the command line. This allows the compiler to generate runtime checks for detecting the presence of hardware features.
{{% /notice %}}

Here is the generated compiler output for the SVE version of `sumPosEltsScaledByIndex` (using `clang`):

```output
	.text
	.globl	sumPosEltsScaledByIndex._Msve
	.p2align	2
	.type	sumPosEltsScaledByIndex._Msve,@function
sumPosEltsScaledByIndex._Msve:
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

This is the default version of `sumPosEltsScaledByIndex`:

```output
	.section	.rodata.cst16,"aM",@progbits,16
	.p2align	4, 0x0
.LCPI2_0:
	.word	0
	.word	1
	.word	2
	.word	3
	.text
	.globl	sumPosEltsScaledByIndex.default
	.p2align	2
	.type	sumPosEltsScaledByIndex.default,@function
sumPosEltsScaledByIndex.default:
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

Any calls to `sumPosEltsScaledByIndex` are routed through `sumPosEltsScaledByIndex.resolver`. This is the function which contains the runtime checks for feature detection. 

```output
	.section	.text.sumPosEltsScaledByIndex.resolver,"axG",@progbits,sumPosEltsScaledByIndex.resolver,comdat
	.weak	sumPosEltsScaledByIndex.resolver
	.p2align	2
	.type	sumPosEltsScaledByIndex.resolver,@function
sumPosEltsScaledByIndex.resolver:
	str	x30, [sp, #-16]!
	bl	__init_cpu_features_resolver
	adrp	x8, __aarch64_cpu_features+3
	adrp	x9, sumPosEltsScaledByIndex._Msve
	add	x9, x9, :lo12:sumPosEltsScaledByIndex._Msve
	ldrb	w8, [x8, :lo12:__aarch64_cpu_features+3]
	tst	w8, #0x40
	adrp	x8, sumPosEltsScaledByIndex.default
	add	x8, x8, :lo12:sumPosEltsScaledByIndex.default
	csel	x0, x8, x9, eq
	ldr	x30, [sp], #16
	ret
```

The called symbol `sumPosEltsScaledByIndex` is an indirect function (ifunc) which points to the resolver.

```output
.weak	sumPosEltsScaledByIndex
.type	sumPosEltsScaledByIndex,@gnu_indirect_function
.set sumPosEltsScaledByIndex, sumPosEltsScaledByIndex.resolver
```

The names `sumPosEltsScaledByIndex._Msve` and `sumPosEltsScaledByIndex.default` correspond to the function versions of `sumPosEltsScaledByIndex`. 

See the [Arm C Language Extensions](https://arm-software.github.io/acle/main/acle.html#name-mangling) for further information on the name mangling rules.
