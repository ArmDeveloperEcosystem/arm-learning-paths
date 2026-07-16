---
title: "Inspect TOSA artifacts"

weight: 6

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Inspect the TOSA intermediate representation

TOSA is the Tensor Operator Set Architecture. It is a stable operator-level intermediate representation (IR) used between model export and backend-specific compilation or conversion.

You have already seen Ethos-U `.pte` files. Those `.pte` files show the final ExecuTorch program after supported regions have been delegated or left outside the NPU delegate. TOSA lets you inspect an earlier stage: the graph representation that backend tools such as Vela or the Arm ML SDK Model Converter can consume.

This is why this section does not include separate TOSA artifacts for the Cortex-A portable, Cortex-A XNNPACK, or Cortex-M examples. In the flow introduced at the start of this learning path, those routes do not need a TOSA intermediate representation: portable kernels stay in the ExecuTorch operator path, XNNPACK uses an ExecuTorch delegate for Cortex-A CPU acceleration, and Cortex-M uses its own Cortex-M/CMSIS-NN-oriented lowering path. TOSA becomes relevant for the backend routes that consume TOSA, such as Ethos-U and VGF.

TOSA inspection is useful when you want to answer questions such as:

- Did lowering produce the operators you expected?
- Are tensors in the expected shapes and data types?
- Did quantization change the graph structure?
- Did an unsupported operation split the graph into separate artifacts?
- Is this TOSA artifact ready to feed into the next backend tool?

Unlike the `.pte` views you inspected earlier, these graphs are not showing ExecuTorch runtime instructions or delegate calls. They show TOSA operators such as `CONV2D`, `DEPTHWISE_CONV2D`, `RESCALE`, `CLAMP`, and `RESHAPE`.

## Inspect Ethos-U TOSA artifacts

Start with the same MobileNetV2 cases you inspected as `.pte` files.

Open the FP32 TOSA artifact:

```output
ml-model-artifacts/tosa/mv2_fp32.tosa
```

Inspect the graph and answer:

- Is the input shape `[1, 3, 224, 224]`?
- Is the output shape `[1, 1000]`?
- Are tensor types FP32?
- Which convolution, add, clamp, and pooling patterns are visible?

![Screenshot of examining an FP32 MobileNetV2 TOSA artifact in Model Explorer.#center](tosa_ethos_fp32.png "Inspecting FP32 TOSA with Model Explorer")

This artifact shows that the FP32 model can be represented in TOSA. In Model Explorer, you should see a large graph with about 800 nodes. Most of the graph is made from constants and arithmetic around the MobileNetV2 operator structure: `CONV2D`, `DEPTHWISE_CONV2D`, `MUL`, `ADD`, `SUB`, `CLAMP`, one `AVG_POOL2D`, and a final `RESHAPE`.

That does not mean the graph can run on Ethos-U. Ethos-U expects supported quantized integer workloads, so the FP32 `.pte` you inspected earlier did not contain an `EthosUBackend` delegate region.

Now open the INT8 TOSA artifact:

```output
ml-model-artifacts/tosa/mv2_int8.tosa
```

Compare it with the FP32 TOSA graph:

- The input and output shapes still match MobileNetV2: `[1, 3, 224, 224]` to `[1, 1000]`.
- Tensor types are INT8.
- You should see many `RESCALE` operations, which are common in quantized graphs.
- You should still see the core CNN structure, including `CONV2D`, `DEPTHWISE_CONV2D`, `ADD`, `AVG_POOL2D`, and `RESHAPE`.

![Screenshot of examining an INT8 MobileNetV2 TOSA artifact in Model Explorer.#center](tosa_ethos_int8.png "Inspecting INT8 TOSA with Model Explorer")

The INT8 graph is still a full MobileNetV2 graph, but the operator mix changes. You should see fewer floating-point arithmetic nodes and many `RESCALE` nodes. These are used in quantized graphs to move values between quantization scales after integer operations. The convolution and depthwise convolution operators use INT32 accumulation, which is typical for INT8 convolution workloads.

This is the kind of TOSA graph that can be compiled by the Ethos-U Vela compiler into an Ethos-U command stream, then packaged into a `.pte`.

## Inspect fragmented TOSA artifacts

Next, inspect the TOSA artifacts from the LRN example:

```output
ml-model-artifacts/tosa/mv2_lrn_int8_1.tosa
ml-model-artifacts/tosa/mv2_lrn_int8_2.tosa
```

You saw earlier that the LRN `.pte` contained two `EthosUBackend` delegate nodes with non-delegated work between them. These two TOSA files help explain why.

Inspect both TOSA files and answer:

- Why did this example produce more than one TOSA artifact?
- What are the input and output shapes for each fragment?
- Which fragment contains most of the MobileNetV2 CNN structure?
- Which fragment represents the graph region after the inserted LRN-related work?
- Are the fragment boundaries consistent with the two `EthosUBackend` regions you saw in the `.pte`?

![Screenshot of examining the first fragmented INT8 TOSA artifact in Model Explorer.#center](tosa_ethos_int8_frag_1.png "Inspecting the first fragmented INT8 TOSA artifact")

![Screenshot of examining the second fragmented INT8 TOSA artifact in Model Explorer.#center](tosa_ethos_int8_frag_2.png "Inspecting the second fragmented INT8 TOSA artifact")

The first LRN TOSA file is the smaller fragment. It has two inputs, with shapes `[1, 1280, 7, 7]` and `[1, 1, 1280, 7, 7]`, and one `[1, 1000]` output. It contains the later part of the graph after the inserted LRN-related work, including a small number of `RESCALE`, `TABLE`, `MUL`, `AVG_POOL2D`, and `CONV2D` operations.

The second LRN TOSA file is the larger fragment. It starts from the original image input shape `[1, 3, 224, 224]` and contains most of the quantized MobileNetV2 CNN structure. It has many `RESCALE`, `CONV2D`, and `DEPTHWISE_CONV2D` operations, and produces intermediate outputs with shapes `[1, 1280, 7, 7]` and `[1, 1, 1284, 7, 7]` that cross the break in the graph.

The graph fragmentation has become visible as multiple backend-ready TOSA artifacts. That matches the fragmented `.pte` view, where two `EthosUBackend` delegate regions were separated by non-delegated work.

The two TOSA files show where the backend-supported graph was split. They do not measure the cost of that split or confirm that the non-delegated operators can run in the deployed runtime. Runtime profiling is needed to identify whether boundary-related work or non-delegated operators dominate execution.

## Use TOSA outside ExecuTorch

TOSA is not limited to ExecuTorch. ExecuTorch can lower supported graph partitions to TOSA, but a different framework, internal compiler, or proprietary model frontend could also produce TOSA directly.

That makes the TOSA adapter useful even when there is no `.pte` file in the workflow. For example, you might be:

- Converting from a framework, ONNX graph, or internal model dialect into TOSA.
- Writing a compiler, graph optimizer, or Vela-like backend tool that consumes TOSA.
- Checking whether your frontend produced the TOSA operators, tensor shapes, layouts, and quantized types you expected.
- Looking for missed optimization opportunities, such as long chains of `ADD`, `MUL`, `RESHAPE`, or layout operations that could potentially be fused or lowered differently.
- Comparing two frontend or compiler versions to see whether the generated TOSA graph became simpler, more fragmented, or more backend-friendly.

One valid artifact flow is:

```output
Custom model format or framework
        |
Frontend or compiler conversion
        |
       TOSA
        |
Arm backend compiler or model converter
        |
Target-specific artifact
```

This matters because TOSA provides a contract between the model frontend and the backend tool. If the TOSA graph has the expected operators, shapes, layouts, and quantized types, the backend compiler or converter has a clearer input to work from. If the graph looks noisy, fragmented, or unexpectedly generic, the issue may be in the frontend conversion, an earlier graph optimization pass, or the backend support boundary.

## Inspect TOSA for VGF conversion

TOSA can also feed Vulkan ML workflows. The Arm ML SDK Model Converter takes TOSA as input, applies transforms and optimizations, lowers to SPIR-V graph IR, and packages the result into a VGF file.

The examples in this section use a small neural upscaling model. It takes a low-resolution image-like tensor and produces a higher-resolution output, which makes it a useful compact example for Vulkan ML and neural graphics workflows.

These artifacts were generated in the [Quantize neural upscaling models with ExecuTorch](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/) learning path. Go through that learning path if you want to learn how to generate the `.tosa` and `.vgf` files yourself, and how to apply post-training quantization (PTQ) and quantization-aware training (QAT) before export.

Open the TOSA artifacts used by the VGF examples:

```output
ml-model-artifacts/tosa/small_upscaler_ptq.tosa
ml-model-artifacts/tosa/small_upscaler_qat.tosa
```

These small upscaler graphs are INT8 TOSA artifacts. In Model Explorer, look for:

- Input shape `[1, 16, 16, 3]`
- Output shape `[1, 32, 32, 3]`
- `RESIZE` with bilinear mode
- `CONV2D` operations
- `RESCALE` operations from quantized arithmetic
- Similarities and differences between the PTQ and QAT artifacts

![Screenshot of examining a PTQ small upscaler TOSA artifact in Model Explorer.#center](tosa_ptq.png "Inspecting a PTQ small upscaler TOSA artifact with Model Explorer")

Do not expect a major visual difference between the PTQ and QAT TOSA graphs. They represent the same small upscaler architecture and were lowered to the same visible TOSA structure: 41 nodes, including one bilinear `RESIZE`, three `CONV2D` operations, four `RESCALE` operations, three `CONST_SHAPE` nodes, and constants for weights and quantization parameters.

The important difference is how the quantized model parameters were produced. PTQ applies quantization after training, usually using calibration data to choose quantization parameters. It is simpler and faster to apply, so it is often the first option to try. QAT simulates quantization during training, so the model can adapt to quantization effects. It takes more work, but can recover accuracy when PTQ causes too much quality loss.

In Model Explorer, that difference is not likely to appear as a different graph shape. Look instead at tensor metadata, constants, scales, shifts, zero-points, and any downstream accuracy or runtime behavior.

These files are useful because they connect the TOSA view to the VGF view. TOSA shows the backend-neutral graph representation. The next section shows the VGF artifact produced for Vulkan ML and neural graphics integration.

## What you have learned

You have inspected TOSA as the intermediate representation between model lowering and backend compilation or conversion. For Ethos-U, TOSA helps explain why FP32 does not delegate, why INT8 can produce a compact NPU region, and why an inserted unsupported operation can fragment the graph. You have also seen that TOSA is not ExecuTorch-specific and can be produced by other frontends.

Next, you will inspect VGF artifacts and see what the TOSA-to-VGF conversion produces for Vulkan ML workflows.
