---
title: Lower a model to the Cortex-M backend
weight: 3
description: Export a Cortex-M model and identify CMSIS-NN accelerated convolutions

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## First use only Cortex-M

Before we demonstrate fallback from an Ethos-U, we will briefly look at running a model exclusively on Cortex-M. Not every microcontroller has an onboard NPU, so some use-cases will involve running TinyML directly on the CPU. In this case, any optimizations can be the vital difference between functional performance, and an impractical application.

## See how the export script lowers the graph

The exporter first prepares and converts the model with `CortexMQuantizer`:

```python
quantizer = CortexMQuantizer()

prepared = prepare_pt2e(exported_program.module(), quantizer)
prepared(*example_inputs)
quantized_model = convert_pt2e(prepared)
quantized_exported_program = torch.export.export(quantized_model, example_inputs)
```

The prepared model is run once with the example input to calibrate activation
ranges. `convert_pt2e()` uses those ranges to choose quantization parameters and
insert the operations that move values between FP32 and INT8.

The exporter converts the quantized program to the ExecuTorch Edge dialect and
applies the Cortex-M pass manager:

```python
edge_program_manager = to_edge(
    quantized_exported_program,
    compile_config=EdgeCompileConfig(_check_ir_validity=False)
)

edge_program_manager._edge_programs["forward"] = CortexMPassManager(
    edge_program_manager.exported_program()
).transform()
```

This step rewrites supported patterns as `cortex_m.*` operators. Unsupported
operations, including `aten.topk`, remain in the portable graph.

The Cortex-M backend is broader than CMSIS-NN. In this model, the quantized
convolutions use CMSIS-NN, while quantize and dequantize use Cortex-M operators
with Arm Helium vector implementations. A `cortex_m.*` target therefore means
that the Cortex-M backend owns the operator, not necessarily that CMSIS-NN
implements it.

{{% notice Important %}}
The Cortex-M backend is not a delegate. Delegation replaces a graph region with
a call to a separately compiled backend. Cortex-M lowering instead rewrites
supported patterns as registered `cortex_m.*` operators that the ExecuTorch
runtime dispatches normally. You will not see an `executorch_call_delegate`
node until the Ethos-U partitioner is added on the next page.
{{% /notice %}}

## Export the model for Cortex-M

Use the provided script to lower the model to Cortex-M only, by specifying `-mode cortex-m`:

{{< tabpane code=true >}}
  {{< tab header="Linux and macOS" language="bash">}}
python export_cortex_m_fallback.py \
  --mode cortex-m \
  --model-file model/model.py \
  --output-dir artifacts
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
python .\export_cortex_m_fallback.py `
  --mode cortex-m `
  --model-file model/model.py `
  --output-dir artifacts
  {{< /tab >}}
{{< /tabpane >}}

The relevant output is:

```output
Relevant targets before Cortex-M lowering:
aten.convolution.default: 2
aten.topk.default: 1

Relevant targets after Cortex-M lowering:
aten.topk.default: 1
cortex_m.dequantize_per_tensor.default: 2
cortex_m.quantize_per_tensor.default: 2
cortex_m.quantized_conv2d_nhwc.default: 2
cortex_m.transpose.default: 1
```

Before lowering, the graph contained two general convolution operations (Stride-1 and Stride-4). The `aten` prefix identifies PyTorch’s ATen operator namespace. These operators describe the computation, but not the hardware or kernel that will perform it. Lowering replaces both with `cortex_m.quantized_conv2d_nhwc`, an INT8 convolution using NHWC layout.

`aten.topk` is unchanged, so it will use the portable CPU kernel. The `cortex_m.quantize_*`
and `cortex_m.dequantize_*` operators mark boundaries between floating-point (FP32) and INT8
regions. 

## What you've accomplished and what's next

You have seen how Cortex-M lowering replaces supported patterns with optimized
Cortex-M operators. The convolutions use CMSIS-NN, quantize and dequantize use
Helium vector implementations, and `topk` remains an ExecuTorch portable
kernel.

Next, you will see how CMSIS-NN provides optimized CPU fallback when deploying a
model to an Ethos-U NPU. The resulting graph combines Ethos-U delegation,
CMSIS-NN-backed Cortex-M operators, and a portable CPU kernel.
