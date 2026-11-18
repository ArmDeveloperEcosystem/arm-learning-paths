---
title: Understand the SmolVLA-ExecuTorch workflow
description: Understand how SmolVLA is split and lowered through ExecuTorch and XNNPACK before converting the model for Arm CPU inference.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Review the SmolVLA architecture
The [SmolVLA research paper](https://arxiv.org/pdf/2506.01844) describes a lightweight vision-language-action model with around 450 million parameters. The model takes camera images, a language instruction, and the robot state as inputs. It then outputs a sequence of robot actions.

![SmolVLA uses a vision-language model to combine camera images, a task instruction, and robot state. An action expert then denoises an action sequence for the robot to execute.#center](smolvla_architecture.png "SmolVLA architecture from the research paper")

{{% notice Note %}}
The embedded vision-language model processes and concatenates the inputs into a multimodal sequence of context tokens known as the prefix. It then passes the prefix to the action expert.
{{% /notice %}}

LeRobot's provided SmolVLA checkpoint is configured with the following:

- Three camera image inputs
- 48-token instruction padding
- Ten iterations of flow matching in the action expert

After denoising, the action expert outputs a robot action chunk with shape `[1, 50, 32]`. The checkpoint uses six action dimensions. Removing the padding leaves a `[1, 50, 6]` tensor that represents a 50-step trajectory for each action dimension.

## Model stages in the ExecuTorch conversion pipeline

ExecuTorch provides a common platform for edge AI inference deployment.

You'll first export your PyTorch model to a hardware-independent ExecuTorch intermediate representation (IR). Next, you'll use a suitable backend to lower the model into an optimized form for your target hardware. You'll use the [XNNPACK backend](https://github.com/google/XNNPACK), which enables optimized inference on Arm CPUs.

The ExecuTorch conversion pipeline has the following stages:

```output
PyTorch model (SmolVLA)
      │
      │  torch.export.export(...)
      v
ExportedProgram
      │
      │  to_edge(...)
      v
ExecuTorch Edge IR
      │
      │  partition with XnnpackPartitioner
      │  lower supported subgraphs to XNNPACK
      v
Edge program with XNNPACK delegate calls
      │
      │  to_executorch()
      v
Serialized ExecuTorch program (.pte)
      │
      │  loaded by native ExecuTorch runtime
      v
ExecuTorch runtime
      │
      ├─ XNNPACK delegate kernels
      │
      └─ portable CPU fallback ops
      v
Arm CPU
```

### How the model is partitioned and lowered

After `torch.export`, the model is represented as a graph of ATen operations.

The XNNPACK partitioner inspects this graph and groups the operations that
XNNPACK can execute. These supported regions are replaced with delegate calls
that the XNNPACK backend will handle at runtime.

During backend lowering, XNNPACK-supported subgraphs are converted into delegate data and replaced in the Edge graph with XNNPACK delegate calls. Operations that XNNPACK can't execute remain in the Edge graph when the ExecuTorch runtime has suitable fallback kernels for them.

Where possible, higher-level operations can also be decomposed into simpler
ATen operations that can be delegated to the backend. If neither the backend nor the runtime supports an operation, you can implement a decomposition into supported operations.

Finally, `to_executorch()` applies runtime-specific transformations, including memory planning, and produces the ExecuTorch program that's serialized as a `.pte` file.

### How the model is split into components

You'll export and lower three separate components: the vision encoder, prefix forward pass, and denoising step.

This split has several benefits compared with exporting the whole model:

- The pinned ExecuTorch version unrolls the whole denoising loop by copying the single-step graph ten times. Exporting one iteration and running it ten times reduces lowering time and memory overhead.
- You can use different numbers of CPU cores to optimize the `vision`, `prefix`, and `denoise` latencies independently.
- The latency added by connecting the three components is negligible compared with the benefit of the split.
- This [LeRobot SmolVLA](https://huggingface.co/lerobot/smolvla_base) development split gives you direct access to denoising without rerunning the more expensive vision and prefix stages.

## What you've learned and what's next

You now understand the SmolVLA architecture and how the model progresses through the ExecuTorch pipeline.

Next, you'll set up your environment and the resources for your own conversion.
