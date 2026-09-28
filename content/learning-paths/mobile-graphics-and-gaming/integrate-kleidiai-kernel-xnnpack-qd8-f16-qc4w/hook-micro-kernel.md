---
title: Inspect SME2 kernel configuration and dispatch
description: Inspect XNNPACK runtime dispatch and packing configuration for the KleidiAI SME2 adapter and its native fallback.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Select the KleidiAI SME2 backend

Selection of the KleidiAI SME2 backend corresponds to the fourth patch [`0004-dispatch-qd8-f16-qc4w-through-kai-sme2.patch`](../0004-dispatch-qd8-f16-qc4w-through-kai-sme2.patch), which you applied during preparation. Its configuration and registration changes are in `init_qd8_f16_qc4w_gemm_config` in `src/configs/gemm-config.c`.

The configuration keeps the existing XNNPACK microkernels as the fallback and selects the KleidiAI path only when XNNPACK detects SME2:

```c
if (hardware_config->arch_flags & xnn_arch_arm_sme2) {
  // Configure KleidiAI RHS packing, LHS packing, and the DQGEMM adapter.
} else {
  // Continue with the existing native XNNPACK configuration.
}
```

The selected backend has two different packing lifetimes:

```text
RHS: pack static weights once during operator creation
LHS: pack dynamic qd8 activation tiles at runtime
```

Both sides must use the layouts expected by the same KleidiAI SME2 matmul microkernel.

## Configure the KleidiAI RHS packer

XNNPACK already has an adapter around the KleidiAI `qsi4cxp` right-hand side (RHS) packer:

```c
xnn_pack_kai_qs4_weights_and_biases_sme
xnn_packed_stride_kai_qs4_weights_and_biases_sme
```

When SME2 is selected, the patch sets the following functions in the GEMM configuration:

```c
qd8_f16_qc4w_gemm_config.pack_weights_and_biases =
    xnn_pack_kai_qs4_weights_and_biases_sme;
qd8_f16_qc4w_gemm_config.packed_stride_weights_and_biases =
    xnn_packed_stride_kai_qs4_weights_and_biases_sme;
```

XNNPACK uses this configuration during operator creation. It passes the original QC4W weights, scales, and bias to the KleidiAI RHS packer. The resulting packed RHS, including `weight_sum[n]`, is stored in operator memory or the XNNPACK weights cache.


## Configure the KleidiAI LHS packer

There's no persistent left-hand side (LHS) buffer at operator creation because QD8 activations and their quantization parameters change for every invocation.

Instead, the XNNPACK dynamically quantized general matrix multiplication (DQGEMM) adapter packs each activation tile immediately before calling KleidiAI:

```text
raw qd8 int8 values + qd8 parameters
  -> KleidiAI qai8dxp packed LHS
  -> KleidiAI SME2 MOPA matmul
```

The adapter uses the private `pack_lhs` helper in the SME2 wrapper file. It performs the following mapping for each activation row:

```text
KleidiAI int8 values       = XNNPACK qd8 values
KleidiAI negative zero pt  = -XNNPACK zero_point
KleidiAI scale             = XNNPACK inv_scale
```

It also queries KleidiAI `kr` and `sr`, checks that `sr == 1`, interleaves the values in `kr`-sized blocks, and pads the K tail with the row zero point. For the packed-LHS layout, see [Pack the QD8 activation without requantizing](../pack-lhs/).

## Register the DQGEMM adapter

The configuration queries the KleidiAI tile sizes and registers the adapter for both the single-row and full-MR cases:

```c
const size_t mr =
    xnn_qd8_f16_qc4w_gemm_minmax_ukernel_16x64c4__neonsme2_get_mr();
const size_t nr =
    xnn_qd8_f16_qc4w_gemm_minmax_ukernel_16x64c4__neonsme2_get_nr();

qd8_f16_qc4w_gemm_config.minmax.dqgemm[XNN_MR_TO_INDEX(1)] =
    XNN_INIT_HMP_DQGEMM_UKERNEL(
        xnn_qd8_f16_qc4w_gemm_minmax_ukernel_16x64c4__neonsme2);
qd8_f16_qc4w_gemm_config.minmax.dqgemm[XNN_MR_TO_INDEX(mr)] =
    XNN_INIT_HMP_DQGEMM_UKERNEL(
        xnn_qd8_f16_qc4w_gemm_minmax_ukernel_16x64c4__neonsme2);
```

The integration uses the following KleidiAI packing parameters:

```text
kr = 4
sr = 1
```

The adapter in `src/qd8-f16-qc4w-gemm/qd8-f16-qc4w-gemm-minmax-16x64c4-neonsme2.c` calls:

```text
kai_run_matmul_clamp_f16_qai8dxp1vlx8_qsi4cxp4vlx8_1vlx4vl_sme2_mopa
```

It passes the output row stride, an FP16 column stride of two bytes, and XNNPACK's FP16 clamp range as inputs.

This step corresponds to the fourth patch [`0004-dispatch-qd8-f16-qc4w-through-kai-sme2.patch`](../0004-dispatch-qd8-f16-qc4w-through-kai-sme2.patch).

The patch also changes the generated SME2 source lists. Run the generator after adding or renaming a file that ends in `-neonsme2.c`:

```bash
python3 tools/update-microkernels.py
```

Depending on your Python version, the generator might report `DeprecationWarning: codecs.open() is deprecated. Use open() instead.` This warning alone doesn't indicate a failure. Check that the script completes successfully.

Before this dispatch is registered, the new wrapper is listed as a non-production SME2 source. After `gemm-config.c` registers the wrapper, the generator finds it in the configuration and moves it to the production SME2 source list. Don't edit the generated list files manually.

## Understand the adapter

The adapter has the standard XNNPACK DQGEMM application binary interface (ABI). XNNPACK calls it with the following:

- An int8 activation tile
- A pointer to packed weights
- The FP16 output tile
- Clamp parameters
- The QD8 parameters for the activation rows

The adapter performs three operations:

```text
raw QD8 tile + per-row parameters
  -> pack_lhs() into KleidiAI qai8dxp layout
  -> kai_run_matmul_clamp_f16_qai8dxp...sme2_mopa()
  -> FP16 output tile
```

The wrapper filename uses the XNNPACK-style label `16x64c4__neonsme2`. It's not a fixed runtime tile size. The actual M and N tile sizes are queried from KleidiAI because they depend on the SME streaming vector length.

The adapter currently allocates a temporary packed-LHS buffer for each DQGEMM call. This keeps the first integration simple and correct. The next optimization is to allocate and reuse a workspace buffer so that the same LHS isn't repacked for every N tile.

## What you've learned and what's next

You've followed the applied configuration from SME2 detection through packing and adapter registration to the KleidiAI call.

Next, you'll build the patched checkout and run the correctness and fallback-build checks.
