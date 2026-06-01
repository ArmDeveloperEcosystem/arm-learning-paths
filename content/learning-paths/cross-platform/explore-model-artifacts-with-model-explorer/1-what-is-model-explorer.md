---
title: "What is Model Explorer and what will you learn?"

weight: 2

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Model Explorer and Arm Adapters

[Model Explorer](https://ai.google.dev/edge/model-explorer) is an open-source, web-based graph visualizer and debugger from Google AI Edge. It provides a hierarchical view of model graphs, lets you expand and collapse layers, search for nodes, inspect metadata, highlight inputs and outputs, compare models, and add overlays to graph nodes. The default version, [contained in this repository](https://github.com/google-ai-edge/model-explorer/) supports TFLite, TF, TFJS, MLIR, and PyTorch (Exported Program) formats.

Model Explorer uses adapters to load formats beyond the built-in model types. The Arm adapters used in this Learning Path transform `.pte`, `.tosa`, and `.vgf` files into graph data that Model Explorer can display.

## What you will do

This learning path is about model artifacts, not model training or export. You start from small pre-generated files and use each to gain an understanding of when you would use Model Explorer, and the insights you can gain.

The three adapters covered in this learning path are:

| Artifact | Adapter | Workflow layer | Use it to inspect |
| --- | --- | --- | --- |
| `.pte` | `pte-adapter-model-explorer` | ExecuTorch program | Delegate regions, backend partitioning, CPU fallback, and the deployed ExecuTorch graph |
| `.tosa` | `tosa-adapter-model-explorer` | Compiler/backend intermediate representation | Lowered operators, tensor shapes, quantized types, graph splits, and missed optimization opportunities |
| `.vgf` | `vgf-adapter-model-explorer` | Vulkan ML graph artifact | Inputs, outputs, constants, tensor metadata, graph connectivity, and SPIR-V graph modules |

{{% notice Note %}}
Model Explorer visualizes the specific artifact you generated or received. Small differences in the target the model has been delegated to, could result in a very different model graph. For example, delegating the same model to an Ethos-U55, may produce a very different model graph from delegating to an Ethos-U85.
{{% /notice %}}

## Understand the model artifact flow

Not every graph in this learning path needs to start with PyTorch and ExecuTorch. Let's run through what is specific to the ExecuTorch flow, and what is applicable more broadly.

PTE is ExecuTorch-specific. A `.pte` file is the serialized ExecuTorch program loaded by the ExecuTorch runtime. Baseline portable-kernel, XNNPACK, Cortex-M, Ethos-U, and VGF-backend examples are all ExecuTorch deployment artifacts.

The portable-kernel and XNNPACK routes are Cortex-A CPU routes. Cortex-M uses a separate ExecuTorch flow that applies CMSIS-NN-oriented passes for supported quantized operators.

For Ethos-U, the ExecuTorch backend uses the Ethos-U Vela compiler to compile TOSA flatbuffers into an Ethos-U command stream that is packaged into the final `.pte`.

TOSA is not inherently ExecuTorch-specific. TOSA is an intermediate representation (IR) that can sit between a model frontend and an Arm backend compiler or converter. ExecuTorch can lower supported graph partitions to TOSA, but another framework could also provide its own TOSA exporter and generate `.tosa` files.

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
                                               for Vulkan ML workflows
```

For VGF, the ExecuTorch Arm VGF backend uses the [Arm ML SDK Model Converter](https://github.com/arm/ai-ml-sdk-model-converter) to produce a VGF backend payload from TOSA. But the Arm ML SDK Model Converter could be used to convert `.tosa` files generated from a different flow, so VGF is also not specific to just ExecuTorch.

When ExecuTorch is used for VGF, a `.pte` is emitted as well. Use that VGF-backend `.pte` when you want to run through ExecuTorch. Use the standalone `.vgf` when you want to inspect or integrate the Vulkan ML artifact directly, such as in a neural graphics workflow. 

If you have used the [Arm Neural Graphics Model Gym](https://github.com/arm/neural-graphics-model-gym), then under the hood you have been using ExecuTorch to export your neural graphics model to VGF. If you are interested in learning more, try out the [Fine-tune neural graphics using Model Gym](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/model-training-gym/#:~:text=Upon%20completion%20of%20this%20Learning,and%20train%20neural%20graphics%20models) learning path, which briefly introduces Model Explorer.

## Terminology

A helpful glossary of different terms is provided below:

| Term | Meaning in this learning path |
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
| Delegate | A backend-specific execution path that handles supported parts of a graph. Unsupported parts can remain on a fallback path. |
| Kernel | The code that executes a model operator for a specific runtime or backend, such as a portable ExecuTorch kernel or a CMSIS-NN kernel. |
| Flatbuffer | A compact binary serialization format. TOSA flatbuffers store TOSA graphs; `.pte` files use a FlatBuffer-based ExecuTorch program format. |
| SPIR-V | Standard Portable Intermediate Representation - Vulkan. SPIR-V modules inside VGF files describe the Vulkan ML data graph used by the runtime. |

## What models will I use?

The hands-on sections will use a variety of pre-provided models.

```output
model-explorer-artifacts/
├── README.md
├── LICENSE.md
├── pte/
│   ├── mv2_cortex_m.pte
│   ├── opt125m_cortex_a_portable.pte
│   ├── opt125m_cortex_a_xnnpack.pte
│   ├── mv2_fp32_ethos_u85.pte
│   ├── mv2_int8_ethos_u85.pte
│   ├── mv2_lrn_int8_ethos_u85.pte
│   ├── small_upscaler_ptq_vgf.pte
│   ├── small_upscaler_qat_vgf.pte
│   └── add_sigmoid_vgf.pte
├── tosa/
│   ├── mv2_fp32.tosa
│   ├── mv2_int8.tosa
│   ├── mv2_lrn_int8_1.tosa
│   ├── mv2_lrn_int8_2.tosa
│   ├── small_upscaler_ptq.tosa
│   └── small_upscaler_qat.tosa
└── vgf/
    ├── small_upscaler_ptq.vgf
    ├── small_upscaler_qat.vgf
    └── add_sigmoid.vgf
```

## What you have learned

You have learned how Model Explorer uses adapters to load artifact formats beyond its built-in model types. You have also seen how `.pte`, `.tosa`, and `.vgf` files fit into Cortex-A, Cortex-M, Ethos-U, and Vulkan ML workflows.

Next, you will install Model Explorer, launch it with the Arm adapters, and open the first `.pte` artifact.
