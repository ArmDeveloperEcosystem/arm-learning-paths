---
title: "Inspect VGF artifacts"

weight: 7

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Inspect VGF artifacts for the ML extensions for Vulkan

VGF is the artifact used by Arm ML SDK for Vulkan workflows. It is useful in workflows using the ML extensions for Vulkan and in neural graphics applications where you need to inspect the graph consumed by the Vulkan runtime.

In the previous section, you inspected the TOSA artifacts for a small neural upscaling model, obtained from the [Quantize neural upscaling models with ExecuTorch](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/) learning path. In this section, you inspect the VGF and PTE artifacts produced from that flow.

Although that flow uses ExecuTorch, and hence it generates `.pte` files as well, VGF is not ExecuTorch-specific. If you have a `.tosa` file obtained from another flow, it can be converted to `.vgf` using the Arm ML SDK Model Converter.

## Compare PTE and VGF views

There are two related but different Model Explorer views in a VGF workflow:

| View | Open with | Layer inspected | What to look out for |
| --- | --- | --- | --- |
| VGF-backend `.pte` | PTE adapter | ExecuTorch program and deployment container | Where does the VGF backend call appear? Is there surrounding quantize, dequantize, or CPU work? |
| Standalone `.vgf` | VGF adapter | Backend graph for the ML extensions for Vulkan | What operators, tensors, shapes, constants, descriptors, and graph connectivity will the Vulkan runtime consume? |

Use the `.pte` file when you want to understand how ExecuTorch wraps and calls the VGF backend. Use the `.vgf` file when you want to inspect the VGF artifact used with the ML extensions for Vulkan. You can also open the VGF backend in Model Explorer from the `.pte` file and see the same view as opening the `.vgf` file directly.

## Open the VGF-backend PTE

Start with the PTQ small upscaler packaged as an ExecuTorch program:

```output
ml-model-artifacts/pte/small_upscaler_ptq_vgf.pte
```

Inspect the graph and answer:

- Is there a `VgfBackend` delegate node?
- What work happens before and after the backend call?
- Does the top-level graph show the internal upscaler operators?
- What does this view tell you about the ExecuTorch runtime path?

![Screenshot of examining a VGF-backed PTE in Model Explorer.#center](ptq_vgf_pte.png "Inspecting a VGF-backed PTE with Model Explorer")

In Model Explorer, this `.pte` should look compact. You should see a `quantized_decomposed::quantize_per_tensor` node, a single `VgfBackend` delegate node, a `quantized_decomposed::dequantize_per_tensor` node, and graph inputs and outputs.

This is a very similar view to the Ethos delegation, where aside from inputs/outputs and quantize/dequantize operators, the model is completely delegated to the backend.

Click to expand the `VgfBackend` delegate graph:

![Screenshot of examining the VGF backend subgraph inside a PTE in Model Explorer.#center](ptq_vgf_pte_subgraph.png "Inspecting the VGF backend subgraph inside a PTE")

Now open the matched standalone VGF artifact:

```output
ml-model-artifacts/vgf/small_upscaler_ptq.vgf
```

You will see they show the same view.

Inspect the graph and answer:

- What input tensor shape and Vulkan tensor format are shown?
- What output shape does the graph produce?
- Do you see the `Resize` and `Conv2D` structure from the TOSA graph?
- Where do `Rescale` operations appear?
- Which details are visible here that were hidden behind the `VgfBackend` node in the `.pte` view?

The VGF graph shows the backend-level structure consumed by the workflow using the ML extensions for Vulkan. For the PTQ upscaler, you should see a small graph with the same high-level structure you saw in TOSA:

- `Resize`
- `Rescale`
- `Conv2D`
- `Rescale`
- `Conv2D`
- `Rescale`
- `Conv2D`
- `Rescale`

You should also see Vulkan tensor descriptor nodes such as `VK_DESCRIPTOR_TYPE_TENSOR_ARM`. The input descriptor has shape `[1, 16, 16, 3]` and format `VK_FORMAT_R8_SINT`. The graph produces an INT8 output with shape `[1, 32, 32, 3]`.

This is the view to use when you care about integration with the ML extensions for Vulkan: tensor shapes, tensor formats, graph connectivity, quantized operators, and backend-visible layout choices.

## Look at other artifacts

Also provided in the repo are the quantization-aware-training version, and a toy `add_sigmoid` model (`.pte` and `.vgf`) from the [Prepare models for neural graphics](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/preparing-models-for-nt/) learning path.

```output
ml-model-artifacts/pte/small_upscaler_qat_vgf.pte
ml-model-artifacts/vgf/small_upscaler_qat.vgf
ml-model-artifacts/pte/add_sigmoid_vgf.pte
ml-model-artifacts/vgf/add_sigmoid.vgf
```
You can use Model Explorer to inspect these graphs in the same way.

## What you have learned

You have inspected the same VGF workflow from two angles. The `.pte` view shows the ExecuTorch program and where it calls the VGF backend. The standalone `.vgf` view shows the backend graph for the ML extensions for Vulkan: tensor descriptors, graph connectivity, operator structure, quantization-related rescale operations, and the input/output contract used by a neural graphics application.

At this point, you have used Model Explorer to inspect the main static artifacts in this learning path: `.pte` files for the deployed ExecuTorch program, `.tosa` files for backend-ready intermediate graphs, and `.vgf` files for integration with the ML extensions for Vulkan. These views answer what was exported, lowered, converted, and packaged.

The final section adds runtime profiling context. You will load ETRecord and ETDump data to see how exported graph structure connects to measured operator and delegate events during execution.
