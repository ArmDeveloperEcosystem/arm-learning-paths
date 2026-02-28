---
title: Overview and setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

KleidiAI includes highly optimized matrix multiplication (matmul) microkernels that accelerate quantized operators on Arm CPUs. On SME2-capable systems, these microkernels use SME2 INT8 MOPA (outer product accumulate) instructions to increase throughput for the compute-heavy parts of inference.

This Learning Path focuses on one concrete microkernel and walks through:
- How the microkernel expects its inputs (quantization + packing)
- Where SME2 instructions show up in the inner loop
- How this maps back to "normal" FP32 matmul semantics

### Where llama.cpp appears in this Learning Path

This Learning Path mentions llama.cpp as a concrete reference point in two ways:
- It uses GGML Q4_0 as a real-world weight format that needs repacking before it can feed the SME2 microkernel.
- It uses llama.cpp call stacks to show where RHS repacking and LHS quantization/packing happen in a real inference pipeline.

It does not ask you to build or run llama.cpp end-to-end. If you want to build and profile llama.cpp with KleidiAI on-device, use [the llama.cpp performance Learning Path](/learning-paths/mobile-graphics-and-gaming/performance_llama_cpp_sme2/).

## What you’ll do (hands-on)

You’ll do a few lightweight, practical checks as you go:
- Confirm whether your target device exposes SME2 (optional)
- Locate the exact microkernel source file in KleidiAI
- Search for key SME2 instructions (for example `smopa`, `luti4`, and `zero {za}`)
- Connect those instructions back to the diagrams and pseudocode in this Learning Path

If you already have llama.cpp built with KleidiAI (for example from [the llama.cpp performance Learning Path](/learning-paths/mobile-graphics-and-gaming/performance_llama_cpp_sme2/)), you can also use that build to validate call stacks and confirm where the kernel runs.

## Hands-on: get the kernel source

If you want to follow the microkernel implementation directly, start by cloning KleidiAI and locating the SME2 matmul microkernel assembly file.

```bash
git clone https://github.com/ARM-software/kleidiai.git
cd kleidiai

KERNEL_FILE="kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qai4c32p/kai_matmul_clamp_f32_qsi8d32p1vlx4_qai4c32p4vlx4_1vlx4vl_sme2_mopa_asm.S"

ls -la "$KERNEL_FILE"
grep -n "smopa" "$KERNEL_FILE" | head
grep -n "luti" "$KERNEL_FILE" | head
grep -n "zero {za}" "$KERNEL_FILE" | head
```

The output is similar to:

```output
90:    KAI_ASM_INST(0xa0840100)        // smopa za0.s, p0/m, p0/m, z8.b, z4.b
(...)
88:    KAI_ASM_INST(0xc08a4044)        // luti4 {z4.b - z5.b}, zt0, z2[0]
(...)
81:    KAI_ASM_INST(0xc00800ff)        // zero {za}
```

If you don’t see matches, your local checkout might be on a different revision. In that case, search for the function name used in this Learning Path:

```bash
grep -R "kai_matmul_clamp_f32_qsi8d32p1vlx4" -n kai | head
```

## Hands-on: verify SME2 is available (optional)

You can complete the "source inspection" parts of this Learning Path without SME2 hardware. To run SME2 code on-device, your CPU and OS need to expose SME2.

{{< tabpane code=true >}}
	{{< tab header="Linux on Arm" language="bash" >}}
uname -m
grep -m1 -E '^Features' /proc/cpuinfo | tr ' ' '\n' | grep -E '^sme$|^sme2$' || true
	{{< /tab >}}
	{{< tab header="macOS" language="bash" >}}
uname -m
sysctl -a | rg -i 'sme2|sme'
	{{< /tab >}}
{{< /tabpane >}}

If neither `sme` nor `sme2` appears, you can still follow the explanation, but you should treat any "run" steps as not applicable on your device.