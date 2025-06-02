<_ZN10butterfly211fdct4x4_vec17h46a2223e96f0f894E>:
	1e2703e0 	fmov	s0, wzr
	6d400801 	ldp	d1, d2, [x0]
	d00001a8 	adrp	x8, <__init_cpu_features_constructor.isra.0+0x4a0>
	6d411404 	ldp	d4, d5, [x0, #16]
	fd41f103 	ldr	d3, [x8, #992]
	5285a828 	mov	w8, #0x2d41                	// #11585
	52830fc9 	mov	w9, #0x187e                	// #6270
	2e608c20 	cmeq	v0.4h, v1.4h, v0.4h
	0f145421 	shl	v1.4h, v1.4h, #4
	0f145442 	shl	v2.4h, v2.4h, #4
	0f145484 	shl	v4.4h, v4.4h, #4
	0e020400 	dup	v0.4h, v0.h[0]
	0ea31c23 	orr	v3.8b, v1.8b, v3.8b
	0e628486 	add	v6.4h, v4.4h, v2.4h
	2e648442 	sub	v2.4h, v2.4h, v4.4h
	2e631c20 	bsl	v0.8b, v1.8b, v3.8b
	0f1454a1 	shl	v1.4h, v5.4h, #4
	0e020d03 	dup	v3.4h, w8
	0e020d25 	dup	v5.4h, w9
	52876428 	mov	w8, #0x3b21                	// #15137
	0e608424 	add	v4.4h, v1.4h, v0.4h
	2e618400 	sub	v0.4h, v0.4h, v1.4h
	0e020d01 	dup	v1.4h, w8
	0e63c0c7 	smull	v7.4s, v6.4h, v3.4h
	0e65c050 	smull	v16.4s, v2.4h, v5.4h
	0e63c091 	smull	v17.4s, v4.4h, v3.4h
	0e65c012 	smull	v18.4s, v0.4h, v5.4h
	0e638087 	smlal	v7.4s, v4.4h, v3.4h
	0e618010 	smlal	v16.4s, v0.4h, v1.4h
	0e63a0d1 	smlsl	v17.4s, v6.4h, v3.4h
	0e61a052 	smlsl	v18.4s, v2.4h, v1.4h
	0f129ce0 	sqrshrn	v0.4h, v7.4s, #14
	0f129e02 	sqrshrn	v2.4h, v16.4s, #14
	0f129e24 	sqrshrn	v4.4h, v17.4s, #14
	0f129e46 	sqrshrn	v6.4h, v18.4s, #14
	0e422807 	trn1	v7.4h, v0.4h, v2.4h
	0e426800 	trn2	v0.4h, v0.4h, v2.4h
	0e462882 	trn1	v2.4h, v4.4h, v6.4h
	0e466884 	trn2	v4.4h, v4.4h, v6.4h
	0e843806 	zip1	v6.2s, v0.2s, v4.2s
	0e8278f0 	zip2	v16.2s, v7.2s, v2.2s
	0e8238e2 	zip1	v2.2s, v7.2s, v2.2s
	0e847800 	zip2	v0.2s, v0.2s, v4.2s
	0e668604 	add	v4.4h, v16.4h, v6.4h
	2e7084c6 	sub	v6.4h, v6.4h, v16.4h
	0e628407 	add	v7.4h, v0.4h, v2.4h
	2e608440 	sub	v0.4h, v2.4h, v0.4h
	0e63c082 	smull	v2.4s, v4.4h, v3.4h
	0e65c0d0 	smull	v16.4s, v6.4h, v5.4h
	0e63c0f1 	smull	v17.4s, v7.4h, v3.4h
	0e65c005 	smull	v5.4s, v0.4h, v5.4h
	0e6380e2 	smlal	v2.4s, v7.4h, v3.4h
	0e618010 	smlal	v16.4s, v0.4h, v1.4h
	0e63a091 	smlsl	v17.4s, v4.4h, v3.4h
	0e61a0c5 	smlsl	v5.4s, v6.4h, v1.4h
	0f129c40 	sqrshrn	v0.4h, v2.4s, #14
	0f129e01 	sqrshrn	v1.4h, v16.4s, #14
	0f129e22 	sqrshrn	v2.4h, v17.4s, #14
	0f129ca3 	sqrshrn	v3.4h, v5.4s, #14
	0e412804 	trn1	v4.4h, v0.4h, v1.4h
	0e416800 	trn2	v0.4h, v0.4h, v1.4h
	0e432841 	trn1	v1.4h, v2.4h, v3.4h
	0e436842 	trn2	v2.4h, v2.4h, v3.4h
	0e813883 	zip1	v3.2s, v4.2s, v1.2s
	0e823805 	zip1	v5.2s, v0.2s, v2.2s
	0e817881 	zip2	v1.2s, v4.2s, v1.2s
	0e827800 	zip2	v0.2s, v0.2s, v2.2s
	4f008422 	movi	v2.8h, #0x1
	6e1804a3 	mov	v3.d[1], v5.d[0]
	6e180401 	mov	v1.d[1], v0.d[0]
	4e628460 	add	v0.8h, v3.8h, v2.8h
	4e628421 	add	v1.8h, v1.8h, v2.8h
	4f1e0400 	sshr	v0.8h, v0.8h, #2
	4f1e0421 	sshr	v1.8h, v1.8h, #2
	ad000420 	stp	q0, q1, [x1]
	d65f03c0 	ret
