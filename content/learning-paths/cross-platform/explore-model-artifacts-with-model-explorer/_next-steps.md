---
# ================================================================================
#       FIXED, DO NOT MODIFY THIS FILE
# ================================================================================
weight: 21
title: "Next Steps"
layout: "learningpathall"
---

## PTE next steps

Run the inspected models with ExecuTorch to connect graph structure to runtime behavior.

Use the XNNPACK delegate documentation to generate your own XNNPACK `.pte` from a model you care about. Then inspect both the portable and XNNPACK artifacts in Model Explorer.

For CPU runtime profiling on modern Arm systems, continue with [Profile ExecuTorch models with SME2 on Arm](/learning-paths/cross-platform/sme-executorch-profiling/).

## Ethos-U next steps

Generate Ethos-U `.pte` files from your own quantized models and inspect delegation coverage.

If you are comparing Ethos-U55 and Ethos-U85, generate target-specific artifacts for each target. Do not infer one target's graph behavior from the other target's artifact.

For a board-focused ExecuTorch workflow, continue with [Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration](/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/).

## TOSA next steps

Generate TOSA from your own model export or compiler flow and inspect it before backend compilation.

Use TOSA inspection when debugging custom frontend, ONNX-to-TOSA, or framework-dialect-to-TOSA conversion flows. Continue to Vela or another backend compiler after the TOSA graph looks correct.

## VGF next steps

Use the VGF adapter to validate tensor contracts before integrating a graph with a Vulkan ML or neural graphics application.

Continue with the related neural graphics Learning Paths:

- [Train neural graphics models with Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym/)
- [Quantize neural upscaling models](/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/)
- [Prepare models for neural technology](/learning-paths/mobile-graphics-and-gaming/preparing-models-for-nt/)

## Runtime profiling next steps

Use ExecuTorch Inspector APIs with ETDump and ETRecord to connect runtime events to graph structure.

When Model Explorer runtime overlays are available, use ETRecord and ETDump together to move from "what did I compile?" to "what actually cost time?"

