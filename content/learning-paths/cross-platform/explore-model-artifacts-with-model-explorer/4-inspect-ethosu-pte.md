---
title: "Inspect Ethos-U PTE delegation"

weight: 5

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Inspect NPU delegation

Ethos-U is Arm's microNPU family for embedded and edge AI acceleration. In ExecuTorch Arm Ethos-U flows, suitable quantized subgraphs are lowered for the Ethos-U backend and compiled through the Arm toolchain.

Model Explorer is useful because the final `.pte` shows whether the ExecuTorch program contains a clean NPU delegate region, fragmented delegate regions, or CPU fallback.

Ethos-U execution is heterogeneous: supported subgraphs are delegated to the NPU, while unsupported operators fall back to the CPU. The PyTorch blog [Efficient Edge AI on Arm CPUs and NPUs](https://pytorch.org/blog/efficient-edge-ai-on-arm-cpus-and-npus/) describes this flow as quantizing the model, lowering supported regions to TOSA, running Vela to produce an optimized Ethos-U command stream, and packaging the result into the final `.pte`. In this section, you inspect three MobileNetV2 artifacts in order: FP32 with no NPU delegation, INT8 with clean delegation, and INT8 with fragmented delegation.

To run through how the artifacts used in this section are obtained, used the [ExecuTorch on Arm Practical Labs](https://github.com/arm-education/executorch_on_arm_labs).

## Open the FP32 Ethos-U artifact

First we will use a MobileNetV2 model, in FP32 form.

Open:

```output
ml-model-artifacts/pte/mv2_fp32_ethos_u85.pte
```

Inspect the graph and answer:

- Is there an Ethos-U delegate region?
- Are the operators still regular `aten::` operators?
- What are the input and output shapes?
- What does this tell you about targeting Ethos-U without quantization?

![Screenshot of examining an FP32 Ethos-U PTE in Model Explorer.#center](ethos_fp32.png "Inspecting FP32 Ethos-U PTE with Model Explorer")

Ethos-U execution expects quantized integer workloads. This artifact was generated from an FP32 MobileNetV2 model, so the graph is not in the form Ethos-U needs for NPU execution. As a result, the work falls back on to the CPU instead of being packaged as an Ethos-U delegate region.

- The graph is much larger at the top level, with many visible `aten::convolution`, `aten::_native_batch_norm_legit_no_training`, and `aten::hardtanh` nodes.
- You should not see an `EthosUBackend` delegate node.
- The input and output shapes still match the image classification model: `[1, 3, 224, 224]` to `[1, 1000]`.

This shows why quantization matters for Ethos-U. A model can be structurally valid and still fall back to CPU execution if it is not in a supported quantized form.

## Open a delegated INT8 Ethos-U artifact

Now we will use the same MobileNetV2 model, but quantized with the `EthosUQuantizer` into INT8.

Open:

```output
ml-model-artifacts/pte/mv2_int8_ethos_u85.pte
```

Inspect the graph and answer:

- Is there an Ethos-U delegate region?
- Is the NPU region one large block or several smaller blocks?
- Which inputs and outputs cross the delegate boundary?
- Does any visible work remain outside the delegated region?

![Screenshot of examining an INT8 Ethos-U PTE in Model Explorer.#center](ethosu-int8-clean.png "Inspecting INT8 Ethos-U PTE with Model Explorer")

A clean delegated example should have most supported quantized work inside the Ethos-U region. In this example, the compute-heavy quantized CNN operators are suitable for Ethos-U and should appear as one large delegated region.

In Model Explorer, this artifact should look very compact at the top level:

- The graph has one input with shape `[1, 3, 224, 224]` and one output with shape `[1, 1000]`.
- You should see a `quantized_decomposed::quantize_per_tensor` node near the start.
- You should see a single `EthosUBackend` delegate node for the main accelerated region.
- You should see a `quantized_decomposed::dequantize_per_tensor` node near the end.

Most of the quantized MobileNetV2 compute is hidden behind one Ethos-U delegate call, so the top-level `.pte` graph mostly shows data entering the delegate, leaving the delegate, and returning to ExecuTorch.

## Open a fragmented Ethos-U artifact

To create this example, the original MobileNetV2 graph was modified by inserting an LRN (Local Response Normalization) layer. This is a useful example because the rest of the model still looks like the clean INT8 MobileNetV2 case, but the inserted LRN operation introduces work that the Ethos-U flow cannot keep inside one contiguous delegated region.

Open:

```output
ml-model-artifacts/pte/mv2_lrn_int8_ethos_u85.pte
```

Look for:

- Multiple delegate regions
- Operators between delegate regions
- Unsupported operations that force CPU fallback
- Extra tensor movement around backend boundaries

![Screenshot of examining a fragmented INT8 Ethos-U PTE in Model Explorer.#center](ethos-u-int8-fragmented.png "Inspecting fragmented INT8 Ethos-U PTE with Model Explorer")

Fragmentation often means that the model was only partly suitable for the target backend. Common causes include unsupported operators, unsupported tensor shapes, quantization issues, or target-specific compiler constraints.

LRN is not natively supported by the Ethos-U flow used here, so it is decomposed into lower-level operations during lowering. Not all of those operations can be delegated to the NPU. Model Explorer should therefore show supported regions delegated to Ethos-U and unsupported work left on the CPU path. In summary: a single unsupported operation can break an otherwise clean NPU region into multiple segments, increasing transitions between CPU and NPU.

In Model Explorer, compare it with the clean delegated artifact:

- The graph still has one input with shape `[1, 3, 224, 224]` and one output with shape `[1, 1000]`.
- You should see two `EthosUBackend` delegate nodes instead of one.
- You should see quantize and dequantize nodes around the delegated regions.
- You should see an `aten::avg_pool3d` node between the delegate regions. This is the visible CPU-side work that breaks the otherwise contiguous NPU path.

This is what fragmentation looks like in a `.pte`: the NPU still accelerates supported regions, but unsupported work splits the graph and creates extra boundaries between CPU execution and Ethos-U execution. These extra boundaries can cause extra overhead that leads to reduced performance.

## Compare targets only with target-specific artifacts

Remember, an artifact generated for one Ethos-U target does not fully explain another target.

For example, an Ethos-U85 artifact does not provide full insight into Ethos-U55 behavior. Generate and inspect separate `.pte` files when comparing targets because operator support constraints, Vela behavior, memory configuration, MAC configuration, and fragmentation can differ.

## Optional extension: TFLite and PT2

<details>
<summary>Click to reveal</summary>

The artifacts repository also includes MobileNetV2 `.pt2` and `.tflite` files. Model Explorer supports PyTorch exported programs and TensorFlow Lite files directly, so visualizing these files does not require an adapter.

```output
ml-model-artifacts/pt2/mv2_fp32.pt2
ml-model-artifacts/tflite/mv2_fp32.tflite
ml-model-artifacts/tflite/mv2_int8.tflite
ml-model-artifacts/tflite/mv2_lrn_int8.tflite
```

Try them out, and compare differences in the model graphs between TensorFlow Lite and ExecuTorch, and also the `.pte` stage and the `.pt2` stage.

</details>

## What you have learned

You have inspected three Ethos-U `.pte` artifacts and seen how quantization and operator support affect NPU delegation. The FP32 MobileNetV2 artifact stays on the CPU path because Ethos-U expects supported quantized integer workloads. The INT8 MobileNetV2 artifact shows the clean delegated pattern: quantize, run a compact `EthosUBackend` region, then dequantize. The LRN example shows fragmentation, where unsupported work splits one clean NPU region into multiple delegate regions with CPU work between them.

Next, you will inspect TOSA artifacts directly to see the intermediate representation that sits between model lowering and backend compilation.
