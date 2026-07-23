---
title: Understand Model Explorer and the artifacts you will inspect
description: Understand how Model Explorer and Arm extensions visualize PTE, TOSA, VGF, ETRecord, and ETDump artifacts across model deployment workflows.

weight: 2

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Model Explorer and Arm extensions

[Model Explorer](https://ai.google.dev/edge/model-explorer) is an open-source, web-based graph visualizer and debugger from Google AI Edge. The visualizer provides a hierarchical view of model graphs. You can expand and collapse layers, search for nodes, inspect metadata, highlight inputs and outputs, compare models, and add overlays to graph nodes. The default version, [contained in the Model Explorer GitHub repository](https://github.com/google-ai-edge/model-explorer/) supports TFLite, TF, TFJS, MLIR, and PyTorch (Exported Program) formats.

Model Explorer uses adapters and data providers to load formats beyond the built-in model types. The [ExecuTorch extension for Model Explorer](https://github.com/arm/executorch-extension-model-explorer) combines support for `.pte`, `.etrecord`, and `.etdp` files. Standalone `.tosa` and `.vgf` files use separate Tensor Operator Set Architecture (TOSA) and VGF adapters. You'll install all three packages together in the next section.

## What you will do

This Learning Path is about model artifacts, not model training or export. You'll start from small pre-generated files and use each to gain an understanding of when you'd use Model Explorer, and what insights you can gain.

You'll use the following artifacts:

| Artifact | Model Explorer support | Workflow layer | Use it to inspect |
| --- | --- | --- | --- |
| `.pte` | PTE adapter in the ExecuTorch extension | ExecuTorch program | Delegate regions, backend partitioning, work outside delegates, and the deployed ExecuTorch graph |
| `.tosa` | Separate TOSA adapter | Compiler or backend intermediate representation | Lowered operators, tensor shapes, quantized types, graph splits, and missed optimization opportunities |
| `.vgf` | Separate VGF adapter | Graph artifact for the ML extensions for Vulkan | Inputs, outputs, constants, tensor metadata, graph connectivity, and SPIR-V graph modules |
| `.etrecord` | ETRecord adapter in the ExecuTorch extension | Export-time profiling context | Graph structure, debug handles, operator names, and delegate metadata used to map runtime events back to graph nodes |
| `.etdp` | ETDump data provider in the ExecuTorch extension | Runtime trace overlay | Timing data from a specific execution |

You'll focuses on Arm adapters and extensions for Model Explorer, but the artifacts repository also includes `.tflite` and `.pt2` files. You can optionally try these files because Model Explorer supports them without an additional adapter.

{{% notice Note %}}
Model Explorer visualizes the specific artifact you generated or received. Small differences in the target the model has been delegated to can result in a very different model graph. For example, delegating the same model to an Ethos-U55, might produce a very different model graph from delegating to an Ethos-U85.
{{% /notice %}}

## Understand the model artifact flow

Not every graph in this Learning Path needs to start with PyTorch and ExecuTorch. 

PTE is ExecuTorch-specific. A `.pte` file is the serialized ExecuTorch program loaded by the ExecuTorch runtime. Baseline portable-kernel, XNNPACK, Cortex-M, Ethos-U, and VGF-backend examples are all ExecuTorch deployment artifacts.

The portable-kernel and XNNPACK routes are Cortex-A CPU routes. Cortex-M uses a separate ExecuTorch flow that applies CMSIS-NN-oriented passes for supported quantized operators.

For Ethos-U, the ExecuTorch backend uses the Ethos-U Vela compiler to compile TOSA flatbuffers into an Ethos-U command stream that's packaged into the final `.pte`.

TOSA is not inherently ExecuTorch-specific. TOSA is an intermediate representation (IR) that can sit between a model frontend and an Arm backend compiler or converter. ExecuTorch can lower supported graph partitions to TOSA, but another framework can also provide its own TOSA exporter and generate `.tosa` files.

```output
      PyTorch model
        |
        v
      ExecuTorch export
        |
        +-- Cortex-A portable kernels -> baseline .pte
        |
        +-- Cortex-A XNNPACK delegate -> XNNPACK .pte
        |
        +-- Cortex-M CMSIS-NN passes -> Cortex-M .pte
        |
        +-- Lower to TOSA -------------+
                                       |
                                       |
                                       |
      Alternative (non PT/ET)          v
      frontend with TOSA export ---> TOSA (.tosa)
                                      |
                                      |
                                      +-- Ethos-U Vela
                                      |     -> command stream
                                      |     -> Ethos-U .pte
                                      |
                                      +-- ML SDK Model Converter
                                            -> VGF payload
                                            -> VGF-backend .pte
                                            -> standalone .vgf
                                               for workflows using the ML extensions for Vulkan
```

For VGF, the ExecuTorch Arm VGF backend uses the [Arm ML SDK Model Converter](https://github.com/arm/ai-ml-sdk-model-converter) to produce a VGF backend payload from TOSA. But the Arm ML SDK Model Converter can be used to convert `.tosa` files generated from a different flow, so VGF is also not specific to just ExecuTorch.

When ExecuTorch is used for VGF, a `.pte` is emitted as well. Use that VGF-backend `.pte` when you want to run through ExecuTorch. Use the standalone `.vgf` when you want to inspect or integrate the VGF artifact used with the ML extensions for Vulkan, such as in a neural graphics workflow.

If you've used the [Arm Neural Graphics Model Gym](https://github.com/arm/neural-graphics-model-gym), then you've been using ExecuTorch to export your neural graphics model to VGF. To learn more, see the [Fine-tune neural graphics using Model Gym](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/model-training-gym/#:~:text=Upon%20completion%20of%20this%20Learning,and%20train%20neural%20graphics%20models) Learning Path, which briefly introduces Model Explorer.

ETRecord and ETDump are additional ExecuTorch-specific artifacts. ETRecord is generated at export time and preserves the graph context needed for profiling attribution. ETDump is generated at runtime and records what happened when a `.pte` ran. Together, they let Model Explorer move from static inspection to runtime overlays. 

You can connect the graph structures you saw in the `.pte`, `.tosa`, and `.vgf` sections to operator and delegate events measured during execution.

## Terminology

The following is a glossary of different terms used in this Learning Path:

| Term | Meaning in this Learning Path |
| --- | --- |
| Model | The neural network you want to deploy, before or after transformation by export and compiler tools. |
| Framework | The software used to define or train the model, such as PyTorch. |
| Export | The step that turns a framework model into a deployable or compiler-friendly representation. |
| Artifact | A file produced by export, lowering, compilation, or conversion, such as `.pte`, `.tosa`, or `.vgf`. |
| Runtime | The software on the target system that loads and executes a deployable artifact. ExecuTorch is the runtime for `.pte` files. |
| Compiler | A tool that transforms an intermediate representation into a lower-level target representation, such as Vela compiling TOSA for Ethos-U. |
| Lower | To transform a model or graph from a higher-level representation into a lower-level representation closer to a target backend. |
| Convert | To change one artifact format into another, such as TOSA to VGF. |
| Intermediate representation | A representation between the original model and the final target artifact. TOSA is the main intermediate representation in this learning path. |
| Delegate | A backend-specific execution path that handles supported parts of a graph. Unsupported parts can remain outside the delegate, and can run on a CPU path only when the deployed runtime includes compatible kernels. |
| Kernel | The code that executes a model operator for a specific runtime or backend, such as a portable ExecuTorch kernel or a CMSIS-NN kernel. |
| Flatbuffer | A compact binary serialization format. TOSA flatbuffers store TOSA graphs; `.pte` files use a FlatBuffer-based ExecuTorch program format. |
| SPIR-V | Standard Portable Intermediate Representation - Vulkan. SPIR-V modules inside VGF files describe the data graph used by the ML extensions for Vulkan. |
| ETRecord | An ExecuTorch export-time debug artifact that preserves graph and delegate metadata for profiling attribution. |
| ETDump | An ExecuTorch runtime trace artifact that can record operator, delegate, backend, timing, and cycle-count events from execution. The first Model Explorer overlay used in this Learning Path focuses on timing data. |

## What models you will use

The hands-on sections will use a variety of pre-provided model artifacts. These are provided purely for educational purposes.

```output
ml-model-artifacts/
├── pte/
│   ├── mv2_cortex_m.pte
│   ├── opt125m_cortex_a_portable.pte
│   ├── opt125m_cortex_a_xnnpack.pte
│   ├── mv2_fp32_ethos_u85.pte
│   ├── mv2_int8_ethos_u85.pte
│   ├── mv2_lrn_int8_ethos_u85.pte
│   └── small_upscaler_ptq_vgf.pte
├── tosa/
│   ├── mv2_fp32.tosa
│   ├── mv2_int8.tosa
│   ├── mv2_lrn_int8_1.tosa
│   ├── mv2_lrn_int8_2.tosa
│   ├── small_upscaler_ptq.tosa
│   └── small_upscaler_qat.tosa
├── vgf/
│   └── small_upscaler_ptq.vgf
├── etrecord/
│   ├── opt125m_portable.etrecord
│   ├── opt125m_xnnpack.etrecord
│   ├── mobilenetv2_fp32_ethosu.etrecord
│   ├── mobilenetv2_int8_ethosu.etrecord
│   └── mobilenetv2_lrn_int8_ethosu.etrecord
└── etdump/
    ├── opt125m_portable.etdp
    ├── opt125m_xnnpack.etdp
    ├── mobilenetv2_fp32_ethosu.etdp
    ├── mobilenetv2_int8_ethosu.etdp
    └── mobilenetv2_lrn_int8_ethosu.etdp
```

## What you have learned

You've now learned how the combined ExecuTorch extension and the separate TOSA and VGF adapters add artifact formats to Model Explorer. You've also seen how `.pte`, `.tosa`, `.vgf`, `.etrecord`, and `.etdp` files support Cortex-A, Cortex-M, Ethos-U, the ML extensions for Vulkan, and ExecuTorch profiling workflows.

Next, you'll install Model Explorer and the Arm extensions, then open the first `.pte` artifact.
