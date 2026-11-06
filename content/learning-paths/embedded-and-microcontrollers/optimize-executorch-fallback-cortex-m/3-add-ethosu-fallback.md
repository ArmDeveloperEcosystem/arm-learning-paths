---
title: Add Ethos-U delegation and CPU fallback
weight: 4
description: Partition TinyCNN for Ethos-U, lower the remaining convolution to Cortex-M, and generate the model-specific AI layer on the Ethos-U55 demonstration target.

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploying across Cortex-M and Ethos-U NPU

We can re-use the same script as on the previous page, this time using 'Fallback mode'. This uses `EthosUPartitioner` to
create an Ethos-U55 delegate region, represented by `executorch_call_delegate`.
The exporter then applies `CortexMPassManager` to operations left outside that
delegate, lowering its supported convolution to a registered Cortex-M operator
implemented by CMSIS-NN.

For supported neural-network operations, the expected order is Ethos-U NPU,
then CMSIS-NN on the Cortex-M CPU, then a portable CPU kernel. This keeps as much
work as possible on the NPU and gives unsupported quantized work an optimized
CPU route before using a general implementation.

![Flow diagram showing that the graph is quantized, supported work is partitioned for Ethos-U, the supported remainder is lowered to Cortex-M operators, and the final remainder stays portable. This order preserves eligible NPU work before CPU lowering.#center](images/executorch-export-flow.svg "ExecuTorch partitioning and lowering order")

Ordering matters. If Cortex-M lowering runs first, it could rewrite a
convolution that should be offered to the NPU.

The exporter first creates an Ethos-U55 compile specification and configures
the target-specific quantizer:

```python
compile_spec = EthosUCompileSpec(target=args.target)
quantizer = EthosUQuantizer(compile_spec)
quantizer.set_global(
    get_symmetric_quantization_config(is_per_channel=True)
)
```

After quantization, `EthosUPartitioner` identifies supported regions and lowers
them into an Ethos-U delegate:

```python
edge_program_manager = to_edge_transform_and_lower(
    quantized_exported_program,
    partitioner=[EthosUPartitioner(compile_spec)],
    compile_config=EdgeCompileConfig(_check_ir_validity=False),
)
```

The exporter then applies Cortex-M lowering to the operations that remain
outside the delegate:

```python
edge_program_manager._edge_programs["forward"] = CortexMPassManager(
    edge_program_manager.exported_program(), use_explicit_layout=True
).transform()
```

This run uses the `ethos-u55-128` target to create the predictable fallback
described earlier.

Run the export script in mixed Cortex-M + Ethos-U mode:

{{< tabpane code=true >}}
  {{< tab header="Linux and macOS" language="bash">}}
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

The export script prints a summary of the graph before and after Cortex-M lowering:

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

The final graph contains all three execution paths:
- `executorch_call_delegate` contains the stride-one convolution accepted by
  Ethos-U55.
- `cortex_m.quantized_conv2d_nhwc` is the stride-four convolution rejected by
  Ethos-U55 and lowered to CMSIS-NN.
- `aten.topk` remains a portable FP32 operation.

## Using the CMSIS-ExecuTorch project workflow

The CMSIS-Executorch project workflow uses `create_ai_layer.py` to export a model, generate a `.pte`, and select the source components required to execute it. 

We have instead used a separate script for the previous examples. By using `create_ai_layer.py` instead, we will benefit from the rest of the setup.

The pre-existing `create_ai_layer.py` does not include CMSIS-NN lowering, so we will add this through a targeted patch that makes four key changes:

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
  {{< tab header="Linux and macOS" language="bash">}}
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
