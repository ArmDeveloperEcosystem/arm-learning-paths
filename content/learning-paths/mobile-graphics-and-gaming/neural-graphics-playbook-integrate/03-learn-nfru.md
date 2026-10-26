---
title: Learn how NFRU works
description: Understand the NFRU algorithm, its engine inputs, and the decisions your integration must own.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Watch the NFRU technical deep dive

Watch the technical explanation of Neural Frame Rate Upscaling (NFRU) and its place in a mobile rendering pipeline:

{{< youtube-nocookie id="J-kcCPSOWXY" title="Neural Frame Rate Upscaling technical deep dive" >}}

## Follow a frame through NFRU

NFRU generates an intermediate frame between neighboring rendered frames. It uses three major stages:

1. Estimate motion: Optical flow estimates dense pixel-level movement between rendered frames. Engine motion vectors provide additional information about projected scene movement.
2. Generate the frame: NFRU aligns candidates from neighboring frames. A neural network combines them and resolves missing or conflicting information.
3. Pace presentation: Rendered and generated frames must reach the display at an even cadence. You can use the SDK component or own frame pacing in your engine.

Your engine supplies color, depth, and motion vectors. It also supplies camera data and metadata. The [SDK API workflow](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#api-interface) provides the exact dispatch sequence.

## Understand where the headroom comes from

NFRU still needs a stable base cadence and adds processing and latency. It creates value when interpolation costs less than rendering another full frame. Choose one goal before testing: a higher presentation rate or more headroom for sustained performance and visual features.

## Own the integration boundaries

Your game owns the following behavior:

- Input correctness
- Temporal resets
- Presentation
- Content testing
- Fallback behavior

Use the [NFRU integration checklist](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#neural-frame-rate-upscaling-integration-checklist) as the implementation reference.

## What you've learned

You've learned how NFRU combines motion estimation, neural composition, and frame pacing. 

Next, you'll test the complete path against your content.
