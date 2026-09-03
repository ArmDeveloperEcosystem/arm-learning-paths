---
title: Configure and dispatch the SME2 kernel
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Select the KAI SME2 backend

Keep the existing XNNPACK microkernels as the fallback. Select the KAI path only when XNNPACK detects SME2:

```c
if (hardware_config->arch_flags & xnn_arch_arm_sme2) {
  // Configure KAI RHS packing, LHS packing, and the DQGEMM adapter.
} else {
  // Continue with the existing native XNNPACK configuration.
}
```

The selected backend has two different packing lifetimes:

```text
RHS: pack static weights once during operator creation
LHS: pack dynamic qd8 activation tiles at runtime
```

Both sides must use the layouts expected by the same KAI SME2 matmul microkernel.

## Configure the KAI RHS packer

XNNPACK already has an adapter around the KAI `qsi4cxp` RHS packer:

```c
xnn_pack_kai_qs4_weights_and_biases_sme
xnn_packed_stride_kai_qs4_weights_and_biases_sme
```

When SME2 is selected, set these functions in the GEMM configuration:

```c
qd8_f16_qc4w_gemm_config.pack_weights_and_biases =
    xnn_pack_kai_qs4_weights_and_biases_sme;
qd8_f16_qc4w_gemm_config.packed_stride_weights_and_biases =
    xnn_packed_stride_kai_qs4_weights_and_biases_sme;
```

XNNPACK uses this configuration during operator creation. It passes the original QC4W weights, scales, and bias to the KAI RHS packer. The resulting packed RHS, including `weight_sum[n]`, is stored in operator memory or the XNNPACK weights cache.


## Configure the KAI LHS packer

There is no persistent LHS buffer at operator creation because qd8 activations and their quantization parameters change for every invocation.

Instead, the XNNPACK DQGEMM adapter packs each activation tile immediately before calling KAI:

```text
raw qd8 int8 values + qd8 parameters
  -> KAI qai8dxp packed LHS
  -> KAI SME2 MOPA matmul
```

The adapter uses the private `pack_lhs` helper in the SME2 wrapper file. It performs the following mapping for each activation row:

```text
KAI int8 values       = XNNPACK qd8 values
KAI negative zero pt  = -XNNPACK zero_point
KAI scale             = XNNPACK inv_scale
```

It also queries KAI `kr` and `sr`, checks that `sr == 1`, interleaves the values in `kr`-sized blocks, and pads the K tail with the row zero point. See [Pack the QD8 activation without requantizing](../pack-lhs/) for the packed-LHS layout.

## Register the DQGEMM adapter

Query the KAI tile sizes and register the adapter for both the single-row and full-MR cases:

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

Set the KAI packing parameters:

```text
kr = 4
sr = 1
```

The adapter calls:

```text
kai_run_matmul_clamp_f16_qai8dxp1vlx8_qsi4cxp4vlx8_1vlx4vl_sme2_mopa
```

Pass the output row stride, an FP16 column stride of two bytes, and XNNPACK's FP16 clamp range.

This step corresponds to [patch 4: Dispatch QD8 F16 QC4W through KAI SME2](../0004-dispatch-qd8-f16-qc4w-through-kai-sme2.patch).

The patch also changes the generated SME2 source lists. Run the generator after adding or renaming a file that ends in `-neonsme2.c`:

```bash
python3 tools/update-microkernels.py
```

Before this dispatch is registered, the new wrapper is listed as a non-production SME2 source. After `gemm-config.c` registers the wrapper, the generator finds it in the configuration and moves it to the production SME2 source list. Do not edit the generated list files by hand.

## Understand the adapter

The adapter has the standard XNNPACK DQGEMM ABI. XNNPACK calls it with an int8 activation tile, a pointer to packed weights, the FP16 output tile, clamp parameters, and the qd8 parameters for the activation rows.

The adapter performs three operations:

```text
raw QD8 tile + per-row parameters
  -> pack_lhs() into KAI qai8dxp layout
  -> kai_run_matmul_clamp_f16_qai8dxp...sme2_mopa()
  -> FP16 output tile
```

The wrapper filename uses the XNNPACK-style label `16x64c4__neonsme2`. It is not a fixed runtime tile size. The actual M and N tile sizes are queried from KleidiAI because they depend on the SME streaming vector length.

The adapter currently allocates a temporary packed-LHS buffer for each DQGEMM call. This keeps the first integration simple and correct. The next optimization is to allocate and reuse a workspace buffer so the same LHS is not repacked for every N tile.
