---
title: Pack the QD8 activation without requantizing
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Preserve the QD8 quantization

The selected KAI LHS format is `qai8dxp`: asymmetric int8 with dynamic per-row parameters. This matches the XNNPACK qd8 input.

This step corresponds to [patch 3: Pack QD8 LHS for KAI SME2](../0003-pack-qd8-lhs-for-kai-sme2.patch).

## Convert the XNNPACK LHS to the KAI LHS

Before packing, XNNPACK provides two related inputs:

```text
input[M, K]                    signed int8 activation values
quantization_params[M]         one { zero_point, inv_scale } pair per row
```

`input` is row-major. Row `m` starts at `input + m * input_stride`. Its quantization parameters are stored separately at `quantization_params[m]`.

The KAI SME2 microkernel cannot consume these two arrays directly. It expects one packed `qai8dxp` LHS buffer. For each group of `mr` rows, that buffer contains:

```text
| KAI-interleaved int8 values for mr rows |
| int32 negative zero point for each row  |
| float scale for each row                |
```

The conversion changes the memory layout, but not the quantization meaning:

```text
XNNPACK input[M, K] + quantization_params[M]
  -> KAI qai8dxp packed LHS
```

The int8 values are copied and interleaved for the KAI inner loop. The separate XNNPACK metadata is appended after the values as KAI metadata. The following sections show the exact mapping.

For each XNNPACK row:

```text
real_value = (q - zero_point) * inv_scale
```

The KAI packed row stores:

```text
interleaved int8 values
int32 negative_zero_point
float scale
```

The correct mapping is therefore:

```text
KAI int8 values       = XNNPACK qd8 values
KAI negative zero pt  = -XNNPACK zero_point
KAI scale             = XNNPACK inv_scale
```

No floating-point dequantization is required. No new int8 quantization is required.

## Interleave values for the microkernel

The selected KAI microkernel uses:

```text
kr = 4
sr = 1
```

For a packed group of `mr` rows, values are interleaved in groups of four K values:

```text
K[0..3] for row 0
K[0..3] for row 1
...
K[0..3] for row mr-1
K[4..7] for row 0
...
```

The `mr` value is vector-length dependent, so obtain it from the KAI kernel query function. For a tail M tile, duplicate the last valid row in the packed buffer. The microkernel writes only the requested M rows.

## Pad K with the quantized zero

KAI rounds K up to a multiple of 32. For a qd8 row, the quantized representation of real zero is its row's zero point:

```text
q_zero = zero_point
```

Use it for padding:

```c
packed_value = k_index < k ? input[k_index] : quantization.zero_point;
```

This guarantees that padded elements contribute zero to the dot product:

```text
(q_zero - zero_point) * inv_scale = 0
```


## How the packing loop works

The packing helper processes the activation matrix in groups of `mr` rows. Each group has three adjacent regions in the destination buffer:

```text
| interleaved int8 values | int32 negative zero points | float scales |
```

For every group, the helper performs the following work:

1. Select up to `mr` source rows starting at `m_start`.
2. If the final group has fewer than `mr` rows, reuse the last valid source row for the unused packed slots.
3. Copy values in K blocks of `kr`, interleaving the same K block from every row.
4. Pad any K values beyond the original K dimension with that row's quantized zero.
5. Store `-zero_point` and `inv_scale` for every packed row.

The implementation obtains `kr` from the selected KAI microkernel instead of relying on a hard-coded value. The current SME2 kernel reports `kr = 4`, but querying it keeps the pack layout coupled to the actual kernel contract:

```c
const size_t kr = kai_get_kr_matmul_clamp_f16_qai8dxp...();
const size_t sr = kai_get_sr_matmul_clamp_f16_qai8dxp...();
assert(sr == 1);
```

For example, if `mr = 4`, the values are stored in this order:

```text
K[0..kr-1] for row 0, row 1, row 2, row 3
K[kr..2*kr-1] for row 0, row 1, row 2, row 3
...
```

For an M tail, suppose the final group contains only two valid rows. The packer uses the following source rows:

```text
packed slots:  0  1  2  3
source rows:   8  9  9  9
```

The matmul call still receives `m = 2`, so it writes results only for rows 8 and 9. Duplicating row 9 only gives the kernel safe data for the complete packed group.

Next, wire the adapter into XNNPACK runtime dispatch.
