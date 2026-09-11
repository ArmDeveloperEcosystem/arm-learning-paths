---
title: Pack QC4W weights for the KAI SME2 kernel
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why pack the RHS once

The right-hand side (RHS) is the fully connected weight matrix. Its int4 values, per-channel scales, and bias values are static after the operator is created. Pack this data once during `xnn_create_fully_connected_nc_qd8_f16_qc4w`, rather than during every inference run.

```text
Original QC4W model weights
  -> XNNPACK create
  -> KAI packed RHS
  -> XNNPACK operator memory or weights cache
  -> repeated inference runs
```

This is different from the qd8 left-hand side (LHS), which changes for every inference run and must be packed at runtime.

This step corresponds to [patch 2: Support transposed KAI QC4W weights](../0002-support-transposed-kai-qc4w-weights.patch).

## Raw XNNPACK QC4W source layout

The logical RHS matrix is:

```text
B[N, K]
```

Each row represents one output channel. The source data contains:

```text
packed int4 weights[N, K]
float kernel_scale[N]
float bias[N]
uint8 kernel_zero_point
```

Two consecutive K values occupy one byte:

```text
bits [3:0] = weight[n][k]
bits [7:4] = weight[n][k + 1]
```

For example, eight int4 values for one output channel are stored as four bytes:

```text
logical values:
K0 K1 K2 K3 K4 K5 K6 K7

packed bytes:
[K1|K0] [K3|K2] [K5|K4] [K7|K6]
```

The scale and bias are separate arrays. They are not embedded in the raw packed-int4 bytes.

## Signedness and kernel zero point

XNNPACK accepts two QC4W encodings:

```text
kernel_zero_point = 0
  each nibble is a signed int4 value in [-8, 7]

kernel_zero_point = 8
  each nibble is an unsigned value in [0, 15]
  its signed weight value is nibble - 8
```

The selected KAI microkernel uses signed int4 weight semantics. The KAI RHS packer handles the required zero-point conversion and also pads the K dimension with signed zero.

## Why raw QC4W cannot feed the KAI kernel directly

Raw XNNPACK QC4W data is organized as one K-contiguous row per output channel, with scales and bias stored separately. This is convenient for a model format, but it is not the layout consumed by the SME2 MOPA inner loop.

The KAI microkernel computes several output channels together. It needs K blocks from an N tile arranged for sequential vector and matrix loads, followed by metadata at KAI-defined offsets.

```text
Raw XNNPACK QC4W
  channel-major int4 rows
  separate scale and bias arrays

KAI packed qsi4cxp RHS
  K blocks interleaved for an N tile
  weight sums, scales, and bias embedded with the tile
```

The formats represent the same mathematical weights, but their byte layouts are different.

## KAI qsi4cxp packed RHS layout

Use the KAI packer:

```text
kai_run_rhs_pack_nxk_qsi4cxps1s0_qsu4cxs1s0_neon
```

It produces the `qsi4cxp` packed RHS format used by:

```text
kai_matmul_clamp_f16_qai8dxp1vlx8_qsi4cxp4vlx8_1vlx4vl_sme2_mopa
```

The packer receives the logical `N x K` source, bias, scale, `nr`, `kr`, and `sr`. For the selected SME2 microkernel:

```text
kr = 4
sr = 1
K_padded = round_up(K, 32)
nr = queried from the KAI microkernel at runtime
```

Conceptually, one packed N tile contains:

```text
| packed int4 data for K block 0 across nr channels |
| packed int4 data for K block 1 across nr channels |
| ...                                                |
| int32 weight sums[nr]                              |
| float scales[nr]                                   |
| float bias[nr]                                     |
```

The exact byte interleave is owned by the KAI packer. Framework code should call the packer rather than reproduce this microkernel-specific layout by hand.

The weight sums are used to compensate for the asymmetric qd8 LHS zero point during matrix multiplication.

## Why the packed RHS stores weight sums

The qd8 activation is asymmetric. For one activation row, its real values are:

```text
a_real[k] = (a_q[k] - a_zero_point) * a_scale
```

For one output channel, let `w_q[n,k]` be the signed int4 weight values. Ignoring the final scale and bias for a moment, the integer part of the dot product is:

```text
sum_k ((a_q[k] - a_zero_point) * w_q[n,k])
```

Expanding this expression gives:

```text
sum_k (a_q[k] * w_q[n,k])
  - a_zero_point * sum_k(w_q[n,k])
```

The first term is the normal integer dot product. The second term is the asymmetric activation correction. The RHS packer calculates and stores this per-output-channel value:

```text
weight_sum[n] = sum_k(w_q[n,k])
```

At runtime, the KAI packed LHS stores:

```text
negative_zero_point = -a_zero_point
```

The KAI microkernel can then compute:

```text
dot(a_q, w_q) + negative_zero_point * weight_sum[n]
```

This is equivalent to subtracting `a_zero_point * weight_sum[n]`, which restores the original asymmetric qd8 equation.

`weight_sum[n]` depends only on static weights and K padding, so the RHS packer calculates it once. The dynamic qd8 zero point can change for every activation row and inference run, but it is supplied through the packed LHS metadata. It does not require the RHS to be packed again.

## Worked packing example

Assume one N tile contains four output channels, `K = 8`, and `kr = 4`.

The raw `N x K` source is conceptually:

```text
channel 0: K0 K1 K2 K3 | K4 K5 K6 K7
channel 1: K0 K1 K2 K3 | K4 K5 K6 K7
channel 2: K0 K1 K2 K3 | K4 K5 K6 K7
channel 3: K0 K1 K2 K3 | K4 K5 K6 K7
```

The KAI packed tile is conceptually ordered as:

```text
K0..K3 for channels 0..3
K4..K7 for channels 0..3
weight_sum[0..3]
scale[0..3]
bias[0..3]
```

This diagram explains the data grouping, not every byte position. The KAI packer defines the exact byte layout required by the SME2 microkernel.

## Handle XNN_FLAG_TRANSPOSE_WEIGHTS

Normally, XNNPACK receives packed nibbles in `N x K` order. With `XNN_FLAG_TRANSPOSE_WEIGHTS`, the source is instead `K x N`.

The KAI RHS packer accepts only `N x K`, so the XNNPACK adapter first creates a temporary `N x K` packed-nibble buffer:

```text
XNNPACK source:   K x N packed int4
temporary source:  N x K packed int4
KAI RHS packer:   N x K -> qsi4cxp packed RHS
```

The conversion must move individual nibbles, rather than whole bytes, because the source and destination pack along different matrix dimensions:

```cpp
const uint8_t source = rhs[k * source_stride + n / 2];
const uint8_t value = (source >> ((n & 1) * 4)) & 0x0F;
transposed_rhs[n * destination_stride + k / 2] |= value << ((k & 1) * 4);
```

`n / 2` and `k / 2` select the packed byte. The low or high nibble is selected with `& 1`. The temporary buffer starts as zeroed bytes, so the `|=` operation safely writes one nibble at a time.

Use the original model QC4W tensor as the input to the packer selected for the active backend:

```text
Original QC4W model weights
  -> XNNPACK native packer -> XNNPACK native microkernel

Original QC4W model weights
  -> KAI RHS packer -> KleidiAI SME2 microkernel
```

The following path is incorrect:

```text
Original QC4W model weights
  -> XNNPACK native packer
  -> KleidiAI SME2 microkernel
```

The KAI microkernel would interpret the XNNPACK-native packed bytes using the wrong interleave and metadata offsets. Keep each packed representation private to the microkernel family that created it.

## Summary

When packing the RHS:

1. Start from the original QC4W model weights, scales, and bias.
2. Convert a transposed `K x N` source to `N x K` when required.
3. Let the KAI packer create the `qsi4cxp` layout.
4. Pack once during operator creation and reuse the result through the weights cache.

Next, adapt the dynamic qd8 LHS without requantizing it.
