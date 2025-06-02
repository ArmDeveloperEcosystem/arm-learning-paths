<fdct4x4_neon>:
	937f7c42 	sbfiz	x2, x2, #1, #32
	79c00004 	ldrsh	w4, [x0]
	8b020003 	add	x3, x0, x2
	fc1f0fe8 	str	d8, [sp, #-16]!
	8b020065 	add	x5, x3, x2
	fd400001 	ldr	d1, [x0]
	fc626803 	ldr	d3, [x0, x2]
	fc626862 	ldr	d2, [x3, x2]
	fc6268a0 	ldr	d0, [x5, x2]
	0f145421 	shl	v1.4h, v1.4h, #4
	0f145463 	shl	v3.4h, v3.4h, #4
	0f145442 	shl	v2.4h, v2.4h, #4
	0f145400 	shl	v0.4h, v0.4h, #4
	34000084 	cbz	w4, <fdct4x4_neon+0x44>
	90000000 	adrp	x0, <__abi_tag-0x278>
	fd456804 	ldr	d4, [x0, #2768]
	0e648421 	add	v1.4h, v1.4h, v4.4h
	6e180440 	mov	v0.d[1], v2.d[0]
	5285a820 	mov	w0, #0x2d41                	// #11585
	6e180461 	mov	v1.d[1], v3.d[0]
	0e020c06 	dup	v6.4h, w0
	52876420 	mov	w0, #0x3b21                	// #15137
	4f008424 	movi	v4.8h, #0x1
	0e020c07 	dup	v7.4h, w0
	52830fc0 	mov	w0, #0x187e                	// #6270
	4e608430 	add	v16.8h, v1.8h, v0.8h
	0e020c08 	dup	v8.4h, w0
	6e608421 	sub	v1.8h, v1.8h, v0.8h
	0f46a202 	smull	v2.4s, v16.4h, v6.h[0]
	0f47a025 	smull	v5.4s, v1.4h, v7.h[0]
	0f48a023 	smull	v3.4s, v1.4h, v8.h[0]
	4ea21c40 	mov	v0.16b, v2.16b
	4f466202 	smlsl2	v2.4s, v16.8h, v6.h[0]
	4f482025 	smlal2	v5.4s, v1.8h, v8.h[0]
	4f476023 	smlsl2	v3.4s, v1.8h, v7.h[0]
	4f462200 	smlal2	v0.4s, v16.8h, v6.h[0]
	0f129c41 	sqrshrn	v1.4h, v2.4s, #14
	0f129ca5 	sqrshrn	v5.4h, v5.4s, #14
	0f129c62 	sqrshrn	v2.4h, v3.4s, #14
	0f129c00 	sqrshrn	v0.4h, v0.4s, #14
	0e452803 	trn1	v3.4h, v0.4h, v5.4h
	0e456800 	trn2	v0.4h, v0.4h, v5.4h
	0e422825 	trn1	v5.4h, v1.4h, v2.4h
	0e426821 	trn2	v1.4h, v1.4h, v2.4h
	0e853862 	zip1	v2.2s, v3.2s, v5.2s
	0e857863 	zip2	v3.2s, v3.2s, v5.2s
	0e813805 	zip1	v5.2s, v0.2s, v1.2s
	0e817800 	zip2	v0.2s, v0.2s, v1.2s
	0ea21c41 	mov	v1.8b, v2.8b
	6e180460 	mov	v0.d[1], v3.d[0]
	6e1804a1 	mov	v1.d[1], v5.d[0]
	4e608430 	add	v16.8h, v1.8h, v0.8h
	6e608420 	sub	v0.8h, v1.8h, v0.8h
	0f46a201 	smull	v1.4s, v16.4h, v6.h[0]
	0f47a005 	smull	v5.4s, v0.4h, v7.h[0]
	0f48a003 	smull	v3.4s, v0.4h, v8.h[0]
	4ea11c22 	mov	v2.16b, v1.16b
	4f482005 	smlal2	v5.4s, v0.8h, v8.h[0]
	fc4107e8 	ldr	d8, [sp], #16
	4f476003 	smlsl2	v3.4s, v0.8h, v7.h[0]
	4f466201 	smlsl2	v1.4s, v16.8h, v6.h[0]
	4f462202 	smlal2	v2.4s, v16.8h, v6.h[0]
	0f129ca5 	sqrshrn	v5.4h, v5.4s, #14
	0f129c63 	sqrshrn	v3.4h, v3.4s, #14
	0f129c21 	sqrshrn	v1.4h, v1.4s, #14
	0f129c42 	sqrshrn	v2.4h, v2.4s, #14
	0e452840 	trn1	v0.4h, v2.4h, v5.4h
	0e456842 	trn2	v2.4h, v2.4h, v5.4h
	0e432825 	trn1	v5.4h, v1.4h, v3.4h
	0e436821 	trn2	v1.4h, v1.4h, v3.4h
	0e853803 	zip1	v3.2s, v0.2s, v5.2s
	0e857800 	zip2	v0.2s, v0.2s, v5.2s
	0e813845 	zip1	v5.2s, v2.2s, v1.2s
	0e817842 	zip2	v2.2s, v2.2s, v1.2s
	0ea31c61 	mov	v1.8b, v3.8b
	6e180440 	mov	v0.d[1], v2.d[0]
	6e1804a1 	mov	v1.d[1], v5.d[0]
	4e648400 	add	v0.8h, v0.8h, v4.8h
	4e648421 	add	v1.8h, v1.8h, v4.8h
	4f1e0400 	sshr	v0.8h, v0.8h, #2
	4f1e0421 	sshr	v1.8h, v1.8h, #2
	ad000021 	stp	q1, q0, [x1]
	d65f03c0 	ret
