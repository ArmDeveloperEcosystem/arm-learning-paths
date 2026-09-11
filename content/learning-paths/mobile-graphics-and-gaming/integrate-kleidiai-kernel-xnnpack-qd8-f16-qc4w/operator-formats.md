---
title: Understand the XNNPACK operator qd8_f16_qc4w formats
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Start with the math

The fully connected operator computes:

```text
C[M,N] = A[M,K] x B[N,K]^T + bias[N]
```

Where:

- `M` is the number of input rows/tokens.
- `K` is the number of input feature dimension/reduction dimension.
- `N` is the number of output feature dimension.
- `A` is the activation matrix.
- `B` is the weight matrix.
- `C` is the FP16 output matrix.

Although the logical RHS matrix is written as `B[N,K]`, the multiplication uses its transpose. Each output has one row of weights with `K` values.

## Left-hand side: QD8 activation data

XNNPACK stores the activation matrix as signed 8-bit values. Each row has separate dynamic quantization parameters:

```c
struct xnn_qd8_quantization_params {
  int32_t zero_point;
  float inv_scale;
};
```

The real value represented by one element is:

```text
A_real[m,k] = (A_q[m,k] - zero_point[m]) * inv_scale[m]
```

This is **asymmetric, per-row quantization**:

- The int8 values are stored row-major with the input stride.
- Each row can have a different zero point.
- Each row can have a different scale.

The important point is that this qd8 representation already contains the quantized activation values. A framework integration should preserve these values whenever possible.

## Right-hand side: QC4W weights

The XNNPACK QC4W input consists of:

- Packed 4-bit weights.
- One FP32 scale for each output channel.
- A kernel zero point of `0` or `8`.
- Optional FP32 bias values.

Two 4-bit weights occupy one byte:

```text
bits [3:0] = K element 0
bits [7:4] = K element 1
```

For the normal weight layout, the raw tensor is `N x K`: each output channel has a contiguous packed row.

XNNPACK also supports `XNN_FLAG_TRANSPOSE_WEIGHTS`. In that case, the source tensor is `K x N`, so the integration must convert it to the `N x K` form expected by the selected KleidiAI RHS packer.

## Padding K safely

The selected KleidiAI SME2 microkernel rounds its internal K dimension up to a multiple of 32. The original model does not need to have a K dimension that is divisible by 32.

The integration creates a padded representation:

```text
K_padded = round_up(K, 32)
```

Padding must represent real value zero:

- For the QD8 LHS, pad each row with its own `zero_point`.
- For signed int4 weights, pad with zero.
- For unsigned int4 weights with zero point 8, the RHS packer converts padding to signed zero.

Padding with any other value changes the dot product and produces incorrect output.

## Where this data enters XNNPACK

The public operator entry points are:

```c
xnn_create_fully_connected_nc_qd8_f16_qc4w(...)
xnn_reshape_fully_connected_nc_qd8_f16_qc4w(...)
xnn_setup_fully_connected_nc_qd8_f16_qc4w(...)
```

The create step receives the static weights, scales, and bias, and packs the persistent RHS representation. The reshape step receives the runtime batch size and plans the GEMM tiles, parallel work, and any required workspace. The setup step receives the qd8 activation values, the FP16 output buffer, and the per-row `xnn_qd8_quantization_params` array.

Next, use these facts to choose a compatible KleidiAI microkernel.
