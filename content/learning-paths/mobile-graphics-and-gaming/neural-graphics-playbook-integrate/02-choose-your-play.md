---
title: Choose your integration route
description: Match your visual goal, engine, and engineering appetite to the right Arm Neural Technology integration route.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Start with the problem

Name the player-facing outcome, then choose the technology and integration surface. Choose between Neural Frame Rate Upscaling (NFRU), Neural Super Sampling (NSS), and Neural Super Sampling and Denoising (NSSD). If the fit is still unclear, return to the [evaluation guidance in Arm Neural Technology Playbook - Evaluate](/learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/04-evaluating-fit-for-your-game/).

Compare the routes before you choose where to start. NFRU, NSS, and NSSD target Arm GPUs with dedicated neural accelerators (NX). The ML Emulation Layer supports desktop development and testing, but its performance isn't representative of production hardware.

| Technology or route | Use case | Availability | Prerequisites | Key constraints | Next step |
| --- | --- | --- | --- | --- | --- |
| NFRU | Present smoother motion without rendering every displayed frame | Public plugins for Unreal Engine 5.4 and 5.6, and the open SDK | Stable base rate of at least 30 FPS for a 60 FPS target; correct depth and motion-vector inputs; measurable quality and pacing targets | Adds processing and latency and needs frame pacing and fallback behavior | Use the [NFRU plugin](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/) or [integrate the SDK](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#integrate-the-sdk). |
| NSS | Lower spatial rendering cost through neural upscaling | Public plugins for Unreal Engine 4.27, 5.4, and 5.6, and the open SDK | Arm Neural Graphics plugin in a supported Unreal Engine project, or SDK integration in another engine | The plugin includes the model integration, and desktop emulation is for development and testing only | Use the [NSS plugin](/learning-paths/mobile-graphics-and-gaming/nss-unreal/) or [NSS SDK checklist](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#neural-super-sampling-integration-checklist). |
| NSSD | Reconstruct advanced lighting from low-resolution, noisy rendering | Early Access exploration with Arm, not a public product or plugin | A ray-traced lighting use case and a team prepared to explore the technology with Arm | Operates in screen space on scene color after ray-traced lighting; it isn't a general denoiser for arbitrary noisy inputs | [Apply to the Arm Neural Technology Early Access Program](https://developer.arm.com/mobile-graphics-and-gaming/neural-technology/early-access-program). |
| Custom model work | Address a quality or performance gap that the published model doesn't meet | Model Gym supports NSS and NFRU model workflows | A reproducible gap, fixed training and evaluation data, and capacity for model work | Start with the published model and customize only for a measured reason | Start with [Neural Graphics Model Gym](https://github.com/arm/neural-graphics-model-gym). |

Unreal Engine 4.27 provides only NSS and uses Neural Graphics SDK v1.0.1. Unreal Engine 5.4 and 5.6 provide NSS and NFRU through public release v1.1.0. The Unreal Engine 5.5 plugin is deprecated and isn't included in the current release. Follow the version-specific setup instructions for [Unreal Engine 4.27](https://github.com/arm/neural-graphics-for-unreal/blob/main/UE4.27/README.md), [Unreal Engine 5.4](https://github.com/arm/neural-graphics-for-unreal/blob/main/UE5.4/README.md), or [Unreal Engine 5.6](https://github.com/arm/neural-graphics-for-unreal/blob/main/UE5.6/README.md).

## Lead with NFRU

NFRU is the primary choice because Arm publishes [routes for Unreal Engine and custom engines](https://developer.arm.com/mobile-graphics-and-gaming/neural-technology). You can start with a prebuilt model and defer model work.

NFRU is a credible candidate when your game has the following characteristics:

- A stable base frame rate of at least 30 FPS before frame generation when targeting 60 FPS presentation
- Correct depth and motion-vector inputs
- A quality target you can test in motion
- Enough latency tolerance and a fallback for unsupported devices

Use the [Project Moku frame-pacing analysis](/learning-paths/mobile-graphics-and-gaming/nfru-cases-study/7-nfru_performance/) to examine the timing conditions.

## Integrate the SDK into a custom or other engine

The [MIT-licensed Neural Graphics SDK](https://github.com/arm/neural-graphics-sdk-for-game-engines#license) supports NFRU and NSS in engines that expose the necessary Vulkan resources and presentation control. This sequence uses NFRU, but the guide also provides an [NSS checklist](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#neural-super-sampling-integration-checklist).

Integrate the SDK in five steps:

1. Check the target: Confirm [platform support](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#platform-support). For desktop development and testing, configure the [ML Emulation Layer](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#ml-emulation-layer-for-vulkan).
2. Run the sample: [Build the SDK](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#build-the-sdk) and verify the [NFRU sample](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#neural-frame-rate-upscaling-sample).
3. Add the SDK: Use it as a CMake subproject or link the prebuilt libraries by following the [SDK integration instructions](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#integrate-the-sdk).
4. Connect NFRU: Enable the [Vulkan extensions](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#enable-extensions), create the context, provide resources, and use the [shared API](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#api-interface).
5. Validate the data contract: Check formats, coordinate systems, resets, latency, and pacing against the [NFRU checklist](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md#neural-frame-rate-upscaling-integration-checklist).

The ML Emulation Layer is for development and testing only. Don't use it in production or treat its performance as representative of production hardware.

Use the linked Arm Neural Graphics SDK Developer Guide sections for commands and API details as you complete the steps.

## What you've learned and what's next

You now have a starting route based on your needs. 

Next, you'll learn the NFRU mechanics that affect integration and evaluation.
