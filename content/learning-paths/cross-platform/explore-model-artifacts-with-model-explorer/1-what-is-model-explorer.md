---
title: "What is Model Explorer and what will you learn?"

weight: 2

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Model Explorer and Arm Adapters

[Model Explorer](https://ai.google.dev/edge/model-explorer) is an open-source, web-based graph visualizer and debugger from Google AI Edge. It provides a hierarchical view of model graphs, lets you expand and collapse layers, search for nodes, inspect metadata, highlight inputs and outputs, compare models, and add overlays to graph nodes. The default version, [contained in this repository](https://github.com/google-ai-edge/model-explorer/) supports TFLite, TF, TFJS, MLIR, and PyTorch (Exported Program) formats.

Model Explorer uses adapters and data providers to load formats beyond the built-in model types. The Arm adapters used in this Learning Path transform `.pte`, `.tosa`, `.vgf`, and `.etrecord` files into graph data that Model Explorer can display. In the final section, you also add `.etdp` runtime trace data as an overlay on top of the exported graph.

## What you will do

This learning path is about model artifacts, not model training or export. You start from small pre-generated files and use each to gain an understanding of when you would use Model Explorer, and the insights you can gain.

The artifacts covered in this learning path are:

| Artifact | Model Explorer support | Workflow layer | Use it to inspect |
| --- | --- | --- | --- |
| `.pte` | `pte-adapter-model-explorer` | ExecuTorch program | Delegate regions, backend partitioning, CPU fallback, and the deployed ExecuTorch graph |
| `.tosa` | `tosa-adapter-model-explorer` | Compiler/backend intermediate representation | Lowered operators, tensor shapes, quantized types, graph splits, and missed optimization opportunities |
| `.vgf` | `vgf-adapter-model-explorer` | Vulkan ML graph artifact | Inputs, outputs, constants, tensor metadata, graph connectivity, and SPIR-V graph modules |
| `.etrecord` | ExecuTorch ETRecord adapter | Export-time profiling context | Graph structure, debug handles, operator names, and delegate metadata used to map runtime events back to graph nodes |
| `.etdp` | ExecuTorch ETDump data provider | Runtime trace overlay | Timing data from a specific execution |

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

ETRecord and ETDump sit alongside these artifact views rather than replacing them. ETRecord is generated at export time and preserves the graph context needed for profiling attribution. ETDump is generated at runtime and records what actually happened when a `.pte` ran. Together, they let Model Explorer move from static inspection to runtime overlays: you can connect the graph structures you saw in the `.pte`, `.tosa`, and `.vgf` sections to operator and delegate events measured during execution.

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
| ETRecord | An ExecuTorch export-time debug artifact that preserves graph and delegate metadata for profiling attribution. |
| ETDump | An ExecuTorch runtime trace artifact that can record operator, delegate, backend, timing, and cycle-count events from execution. The first Model Explorer overlay used in this Learning Path focuses on timing data. |

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
├── vgf/
│   ├── small_upscaler_ptq.vgf
│   ├── small_upscaler_qat.vgf
│   └── add_sigmoid.vgf
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

You have learned how Model Explorer uses adapters and data providers to load artifact formats beyond its built-in model types. You have also seen how `.pte`, `.tosa`, `.vgf`, `.etrecord`, and `.etdp` files fit into Cortex-A, Cortex-M, Ethos-U, Vulkan ML, and ExecuTorch profiling workflows.

Next, you will install Model Explorer, launch it with the Arm adapters, and open the first `.pte` artifact.
