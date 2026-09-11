---
title: Select a compatible KleidiAI microkernel
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Match quantization contracts first

Do not select a microkernel only because it produces FP16 output and uses int8 and int4 inputs. Its quantization contract must also match the framework operator.

An initially tempting KleidiAI kernel is:

```text
matmul_clamp_f16_qsi8d32p_qai4c32p
```

It is not a correct match for XNNPACK `qd8_f16_qc4w`:

- `qsi8d32p` requires symmetric int8 quantization for each block of 32 K values.
- XNNPACK QD8 uses asymmetric int8 quantization for each row.

Using that kernel requires dequantizing and then requantizing the LHS per 32-value block. This adds quantization error and can violate the numerical contract of the existing XNNPACK operator.

## Select `qai8dxp/qsi4cxp`

Use this KleidiAI SME2 MOPA microkernel instead:

```text
kai_matmul_clamp_f16_qai8dxp1vlx8_qsi4cxp4vlx8_1vlx4vl_sme2_mopa
```

Its formats match the operator:

| Operand | XNNPACK format | KAI format | Result |
|---|---|---|---|
| LHS | QD8, asymmetric per row | `qai8dxp`, asymmetric per row | Direct metadata adaptation |
| RHS | QC4W, int4 per output channel | `qsi4cxp`, signed int4 per channel | Pack once during create |
| Output | FP16 with min/max clamp | FP16 with min/max clamp | Direct match |

`qai8dxp` means quantized asymmetric int8 with dynamic, per-row parameters. It is the key reason this kernel is suitable: the original qd8 activation values do not need to be requantized.

## Why SME2 MOPA

The `sme2_mopa` suffix means the microkernel uses SME2 matrix outer product accumulate instructions. SME2 provides a matrix accumulator, called ZA, that is designed for matrix workloads.

The kernel tile dimensions are expressed in vector lengths:

```text
1VL x 4VL
```

The actual `mr` and `nr` values depend on the device's streaming vector length. Do not hard-code them. Query the kernel:

```c
size_t mr = kai_get_mr_matmul_clamp_f16_qai8dxp1vlx8_qsi4cxp4vlx8_1vlx4vl_sme2_mopa();
size_t nr = kai_get_nr_matmul_clamp_f16_qai8dxp1vlx8_qsi4cxp4vlx8_1vlx4vl_sme2_mopa();
```

The same kernel reports `kr = 4` and `sr = 1`. These values define the K interleave used by the packed LHS and RHS buffers.

## Prepare the XNNPACK SME2 wrapper

The first implementation step is [patch 1: Prepare QD8 F16 QC4W SME2 kernel](../0001-prepare-qd8-f16-qc4w-sme2-kernel.patch).

It adds an XNNPACK wrapper at:

```text
src/qd8-f16-qc4w-gemm/
  qd8-f16-qc4w-gemm-minmax-16x64c4-neonsme2.c
```

The `16x64c4` part follows the existing XNNPACK SME2 wrapper naming convention. It is a name used by XNNPACK tooling, not a claim that the KAI kernel always uses a fixed 16 by 64 tile. The actual tile dimensions come from the KAI `get_mr` and `get_nr` functions at runtime.


{{% notice Tip %}}
The most reusable lesson is simple: select a kernel from its complete operand contract. Compare quantization granularity, signedness, zero-point behavior, output type, clamp behavior, and packing requirements before implementing any adapter.
{{% /notice %}}

Next, pack the static RHS weights.
