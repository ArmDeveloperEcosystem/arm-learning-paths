---
title: Inspect the generated CMSIS Pack selection
weight: 5
description: Trace the mixed ExecuTorch graph to versioned runtime, backend, operator, and CMSIS-NN source components.

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand what the CMSIS Pack provides

The [ExecuTorch CMSIS Pack](https://www.keil.arm.com/packs/executorch-pytorch/overview/) is a *source Pack*, not a prebuilt runtime library. It supplies the ExecuTorch runtime, registration code, backends, and
operators as selectable CMSIS components.

A `.pack` file is a ZIP-compatible archive. Its Pack Description file, or
PDSC, records component names, source files, dependencies, versions, and
conditions.

CMSIS-Toolbox uses that metadata to add only the chosen components to the
application build. A CMSIS project can select only the components required by its lowered graph
instead of maintaining one large source list. Arm Compiler then compiles those sources for the Cortex-M55
target with the rest of the project. 

## See which Packs were resolved

CMSIS-Toolbox has already acquired the software Packs needed by the project.
Inspect the generated Pack lock:

{{< tabpane code=true >}}
  {{< tab header="Linux and macOS" language="bash">}}
cat cmsis-executorch-u55.cbuild-pack.yml
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
Get-Content .\cmsis-executorch-u55.cbuild-pack.yml
  {{< /tab >}}
{{< /tabpane >}}

Among the resolved entries, you can see the two Packs responsible for the
mixed model:

```output
- resolved-pack: ARM::CMSIS-NN@8.0.0
- resolved-pack: PyTorch::ExecuTorch@1.5.1
```

They have different responsibilities:

- `PyTorch::ExecuTorch@1.5.1` supplies the ExecuTorch runtime, Ethos-U backend,
  Cortex-M operator wrappers, registration code, and portable operators.
- `ARM::CMSIS-NN@8.0.0` supplies the optimized neural-network kernels called by
  the Cortex-M convolution wrapper.

The Pack lock records exact resolved versions so later builds don't silently
move to newer installed Packs.

## Trace the graph into the AI layer

The AI layer is a generated CMSIS software layer that embeds the model and declares the runtime, backends, operators, and libraries needed to execute it.

Open the AI layer generated from the `.pte` operator list:

{{< tabpane code=true >}}
  {{< tab header="Linux and macOS" language="bash">}}
cat ai_layer/ai_layer.clayer.yml
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
Get-Content .\ai_layer\ai_layer.clayer.yml
  {{< /tab >}}
{{< /tabpane >}}

Its component list includes:

```yaml
components:
  - component: Machine Learning:ExecuTorch:Runtime
  - component: Machine Learning:ExecuTorch:Kernel Utils
  - component: Machine Learning:ExecuTorch:Kernel Registration
  - component: Machine Learning:ExecuTorch:Backend EthosU
  - component: Machine Learning:ExecuTorch Operators:Cortex-M dequantize_per_tensor
  - component: Machine Learning:ExecuTorch Operators:Cortex-M quantize_per_tensor
  - component: Machine Learning:ExecuTorch Operators:Cortex-M quantized_conv2d
  - component: Machine Learning:ExecuTorch Operators:Cortex-M transpose
  - component: Machine Learning:ExecuTorch Operators:Portable topk
  - component: ARM::CMSIS:NN Lib
```

This file is the handover between model export and firmware build:

| Export result | Selected component |
| --- | --- |
| Ethos-U delegate | `Backend EthosU` |
| Cortex-M convolution | `Cortex-M quantized_conv2d` and `ARM::CMSIS:NN Lib` |
| Quantized boundaries and layout changes | Matching Cortex-M components |
| Portable `topk` | `Portable topk` |

The runtime, kernel utilities, and registration components provide the common
machinery needed to load the `.pte` and dispatch its operators.

You will also see `ARM_NN_ENABLE_F32` and `ARM_NN_ENABLE_F16` definitions in
the generated layer. CMSIS-NN 8.0.0 needs them because its Pack component
compiles optional floating-point source files. The fallback convolution in
this model remains INT8; these definitions don't change its data type.

## What you've learned and what's next

You have followed graph targets into two versioned source Packs and a concrete
component list. Pack acquisition, dependency resolution, and component
selection are now one connected workflow rather than separate downloads.

Next, you will see how the reusable CMSIS project combines this generated AI
layer with the Corstone-300 board and application layers.
