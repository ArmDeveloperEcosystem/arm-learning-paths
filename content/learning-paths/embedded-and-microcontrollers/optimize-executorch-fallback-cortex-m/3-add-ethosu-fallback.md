---
title: Add Ethos-U delegation and CPU fallback
weight: 4
description: Partition TinyCNN for Ethos-U, lower the remaining convolution to Cortex-M, and generate the model-specific AI layer on the U55 demonstration target.

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Partition the same model for Ethos-U

The mixed export changes the order of decisions. It first gives
`EthosUPartitioner` the opportunity to claim supported graph regions. It then
applies Cortex-M lowering only to the operations left outside the delegate:

![Flow diagram showing that the graph is quantized, supported work is partitioned for Ethos-U, the supported remainder is lowered to Cortex-M operators, and the final remainder stays portable. This order preserves eligible NPU work before CPU lowering.#center](images/executorch-export-flow.svg "ExecuTorch partitioning and lowering order")

Ordering matters. If Cortex-M lowering ran first, it could rewrite a
convolution that should have been offered to the NPU.

This run uses the `ethos-u55-128` target to create the predictable fallback
described earlier. The partition-then-lower order also applies to
other Ethos-U targets; the operations left outside their delegates can differ.

Run the diagnostic exporter in mixed mode:

{{< tabpane code=true >}}
  {{< tab header="Linux" language="bash">}}
python export_cortex_m_fallback.py \
  --mode ethos-u-fallback \
  --target ethos-u55-128 \
  --model-file model/model.py \
  --output-dir artifacts
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
python .\export_cortex_m_fallback.py `
  --mode ethos-u-fallback `
  --target ethos-u55-128 `
  --model-file model/model.py `
  --output-dir artifacts
  {{< /tab >}}
{{< /tabpane >}}

Vela prints a summary for the region it compiles:

```output
Relevant targets before Cortex-M lowering:
aten.convolution.default: 1
aten.topk.default: 1
executorch_call_delegate: 1

Relevant targets after Cortex-M lowering:
aten.topk.default: 1
cortex_m.dequantize_per_tensor.default: 2
cortex_m.quantize_per_tensor.default: 2
cortex_m.quantized_conv2d_nhwc.default: 1
cortex_m.transpose.default: 2
executorch_call_delegate: 1
```

The above summary is interpreted as follows:

| Model work | Final Graph target | Execution engine |
| --- | --- | --- |
| Stride-one convolution and supported surrounding work | `executorch_call_delegate` | Ethos-U55 |
| Stride-four convolution | `cortex_m.quantized_conv2d_nhwc` | Cortex-M55 using CMSIS-NN |
| Output selection | `aten.topk` | Cortex-M55 using the portable ExecuTorch kernel |

One of the two convolution nodes has disappeared into the delegate. The other
becomes a Cortex-M operator. `topk` remains portable.

{{% notice Note %}}
Vela can report `CPU operators = 0` for the region submitted to it. That line
doesn't describe the complete ExecuTorch graph. The graph summary shows the
Cortex-M convolution and portable `topk` that remain outside the delegate.
{{% /notice %}}

## Connect fallback to the CMSIS project

The CMSIS-Executorch project uses `create_ai_layer.py` to export the model again, generate the final PTE, and select the source components required to execute it. 

However, some patches have to be made. The project generator within that project currently handles Ethos-U delegation, but it does not lower the remaining convolution to Cortex-M or select CMSIS-NN. The focused
integration patch makes four related changes:

- It adds `ARM::CMSIS-NN@8.0.0` to the solution's Pack list.
- It applies Cortex-M lowering after Ethos-U partitioning.
- It maps explicit-layout names such as `quantized_conv2d_nhwc` to their Pack
  component names.
- It selects the CMSIS-NN library when the exported program contains a
  CMSIS-NN-backed Cortex-M operator.

Check and apply the patch, then inspect its small project diff:

```console
git apply --check enable_cortex_m_fallback.patch
git apply enable_cortex_m_fallback.patch
git --no-pager diff -- cmsis-executorch-u55.csolution.yml create_ai_layer.py
```

No board, runner, or linker changes are needed.

## Generate the target description

Resolve the declared Packs and active target:

```console
cbuild setup cmsis-executorch-u55.csolution.yml --active SSE-300-U55 --packs
```

This one command installs missing packs through the public Pack index and
writes three useful descriptions:

- `cmsis-executorch-u55.cbuild-pack.yml` locks the resolved Pack versions.
- `cmsis-executorch-u55.cbuild-mlops.yml` describes the Cortex-M55, Ethos-U55,
  Vela settings, and destination AI layer.
- `cmsis-executorch-u55.cbuild-idx.yml` indexes the resolved build context.

## Generate the AI layer

Use the MLOps description to export the model and write its CMSIS AI layer:

{{< tabpane code=true >}}
  {{< tab header="Linux" language="bash">}}
python create_ai_layer.py cmsis-executorch-u55.cbuild-mlops.yml
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
python .\create_ai_layer.py .\cmsis-executorch-u55.cbuild-mlops.yml
  {{< /tab >}}
{{< /tabpane >}}

The relevant final output is similar to:

```output
[ai_layer] 7608 byte program, operators: ['Cortex-M dequantize_per_tensor', 'Cortex-M quantize_per_tensor', 'Cortex-M quantized_conv2d', 'Cortex-M transpose', 'Portable topk']
[ai_layer] wrote .../ai_layer/ai_layer.clayer.yml
```

The generator writes the final `model.pte`, converts it to C data for the
firmware, and records the runtime and operator components needed to execute it.

## What you've accomplished and what's next

You have produced a model-specific AI layer with one Ethos-U55 delegate, one
CMSIS-NN-backed fallback convolution, and one portable operation. The split is
decided ahead of time and stored in the ExecuTorch program.

Next, you will inspect how the two published source Packs supply the code behind
those graph targets.
