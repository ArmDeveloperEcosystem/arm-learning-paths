---
title: Get started with NFRU and NSSD
weight: 6
description: Begin evaluating NFRU through the Unreal Engine plugin and explore NSSD integration with MegaLights for deeper rendering pipeline customization.

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview 

If you've determined Arm Neural Technology is worth exploring for your game, start by evaluating NFRU in Unreal Engine. You can then use the lower-level Vulkan and model-development resources when you need more control.

## NFRU

Start with [Enable Neural Frame Rate Upscaling in Unreal Engine](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/). This Learning Path guides you through building the Neural Graphics SDK, enabling the ML emulation layers for Vulkan, adding the Unreal Engine plugin, and validating frame generation. It also shows you how to tune NFRU with console variables, inspect intermediate buffers, and analyze a packaged application with RenderDoc for Arm GPUs.

Test it in a representative scene, observe how it behaves with your content, and understand the tradeoffs—especially around motion, UI, and responsiveness.

Next, use [Analyze Neural Frame Rate Upscaling using Project Moku](/learning-paths/mobile-graphics-and-gaming/nfru-cases-study/) to study a complete NFRU case study. It shows how to evaluate occlusion, particle effects, lighting changes, frame pacing, and performance with repeatable scenes, Streamline, and RenderDoc for Arm GPUs.

Arm publishes the [Neural Frame Rate Upscaling model on Hugging Face](https://huggingface.co/Arm/neural-frame-rate-upscaling). To understand the Vulkan execution path behind the plugin, continue with [Get started with neural graphics using ML extensions for Vulkan](/learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/). If you need to fine-tune, evaluate, quantize, or export the model, use [Train and evaluate Neural Frame Rate Upscaling models using Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym-nfru/).

## NSSD

Getting started with NSSD requires a different kind of effort. There isn't a plug-and-play path today. NSSD—especially in combination with MegaLights—requires deeper integration into the rendering pipeline, including modifications to Unreal Engine itself.

For more detail on what this looks like in practice, see the following blog, which describes the approach to lighting at scale and how NSSD fits into that setup:

[Lighting at Scale: Bringing Hundreds of Dynamic Lights to Mobile with Unreal MegaLights](https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/lighting-at-scale-bringing-hundreds-of-dynamic-lights-to-mobile-with-unreal-megalights)

This gives you a clearer picture of what's involved and whether it's something worth exploring further.

Approach NSSD as an experiment rather than a feature. Evaluate it if you're interested in pushing beyond what's currently possible with traditional techniques—particularly around dynamic lighting—but expect a higher barrier to entry.

You'll need to be comfortable working closer to the rendering pipeline and expect iteration to get stable results for your content.

The final section looks at what it means to bring models into your workflow. This is where things become more open-ended. If you decide to go down that path, expect to learn as you go—this is still new territory for most game teams, and part of the process is building that knowledge over time.
