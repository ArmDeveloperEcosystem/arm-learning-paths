---
title: First implementation
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## First implementation
Given what we said in the previous chapters, the exponential function can be implemented with SVE intrinsics in the following way:

```C
svfloat32_t lane_consts = svld1rq(pg, constants); // Load ln2_lo, c0, c2, c4 in register

/* Compute k as round(x/ln2) using shift = 1.5*2^23 + 127 */
svfloat32_t z = svmad_x(pg, svdup_f32(inv_ln2), x, shift);
svfloat32_t k = svsub_x(pg, z, shift);

/* Compute r as x - k*ln2 with Cody and Waite */
svfloat32_t r = svmsb_x(pg, svdup_f32(ln2_hi), k, x);
            r = svmls_lane(r, k, lane_consts, 0);

/* Compute the scaling factor 2^k */
svfloat32_t scale = svreinterpret_f32_u32(svlsl_n_u32_m(pg, svreinterpret_u32_f32(z), 23));

/* Compute poly(r) = exp(r) - 1 */
svfloat32_t p12  = svmla_lane(svdup_f32(c1), r, lane_consts, 2); // c1 + c2 * r
svfloat32_t p34  = svmla_lane(svdup_f32(c3), r, lane_consts, 3); // c3 + c4 * r
svfloat32_t r2   = svmul_x(pg, r, r);
svfloat32_t p14  = svmla_x(pg, p12, p34, r2); // c1 + c2 * r + c3 * r^2 + c4 * r^3
svfloat32_t p0   = svmul_lane(r, lane_consts, 1); // c0 * r
svfloat32_t poly = svmla_x(pg, p0, r2, p14); // c0 * r + c1 * r^2 + c2 * r^3 + c3 * r^4 + c4 * r^5

/* exp(x) = scale * exp(r) = scale * (1 + poly(r)) */
svfloat32_t result = svmla_f32_x(pg, scale, poly, scale);
```
