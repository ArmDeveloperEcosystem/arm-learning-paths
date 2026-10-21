---
title: Catch up on what changed
description: See how NFRU moved from Early Access to a public integration route and how this playbook builds on the Arm Neural Technology Playbook - Evaluate.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The story so far

[Arm Neural Technology](https://developer.arm.com/mobile-graphics-and-gaming/neural-technology) uses machine learning to reconstruct pixels, generate frames, and make advanced rendering workloads practical within mobile power and thermal limits. You already know the cast: Neural Super Sampling (NSS), Neural Frame Rate Upscaling (NFRU), and Neural Super Sampling and Denoising (NSSD).

The [Arm Neural Technology Playbook - Evaluate](/learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/) asks whether these techniques fit your game. It explains what Arm and Sumo Digital learned from Neural Dawn and compares the opportunities and tradeoffs of NFRU and NSSD. Return to that playbook if you need to revisit the technology or the fit questions.

This playbook starts at the next decision: *you see a potential fit, so how do you make the first move?*

You don't need to have read the earlier playbook. The only context you need is that neural graphics is not one feature with one integration path. Your route depends on the problem you want to solve, the engine you use, and how deeply you want to change your rendering and model-development workflows.

Your actionable starting points are the public NFRU and NSS integration routes. Treat NSSD separately as experimental exploration with Arm through the Early Access Program, rather than as a public integration route.

## Your journey through Integrate

Think of the playbook as a series of decisions. Each episode narrows the next move:

| Episode | Story beat | Decision |
| --- | --- | --- |
| Choose your play | Start with your goal and engine | Which route fits your game? |
| Learn NFRU | See what happens between two rendered frames | What must your engine own? |
| Test the result | Try NFRU with Project Moku, then with your game | Does NFRU meet the bar? |
| Look beyond | See what NSSD could make possible for lighting | Is deeper exploration worth it? |
| Prepare model work | Know how to change the model to fit your content | Does your model need to change? |
| Use the model toolkit | Connect MLIA estimates to Streamline device measurements | What evidence supports your model choice? |
| Look ahead | Get ready to put your work on NX devices | What needs to be ready for deployment? |

## Start with the public NFRU and NSS routes

NFRU and NSS both have public integration routes. When Arm first shared NFRU, developers were directed to the Early Access Program. NFRU is now available through the public Arm Neural Graphics SDK for Game Engines and the Arm Neural Graphics plugin for Unreal Engine.

Use the plugin for the shortest Unreal Engine route. Use the open, engine-agnostic SDK when you need direct control in another engine. The release also includes NFRU support in [Neural Graphics Model Gym](https://github.com/arm/neural-graphics-model-gym) and additional debugging controls. See the [SDK v1.1 release notes](https://github.com/arm/neural-graphics-sdk-for-game-engines/releases/tag/v1.1.0) and [Arm Neural Graphics SDK Developer Guide](https://github.com/arm/neural-graphics-sdk-for-game-engines/blob/main/docs/user_guide.md) for details.

The [Introducing Neural Frame Rate Upscaling in Arm Neural Graphics SDK for Game Engines and UE plugins](https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/introducing-neural-frame-rate-upscaling-in-arm-neural-graphics-sdk-for-game-engines-and-ue-plugins) blog connects the release to the wider story: why NFRU complements NSS, how the SDK and Unreal Engine routes differ, and where to start.

## Connect model assessment to runtime profiling

The model toolkit supports decisions before and after you have an NX device. [ML Inference Advisor (MLIA)](/learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/) checks supported models for Neural Technology compatibility and estimates NX performance on your development host. These estimates help you compare candidates; they aren't measurements of your game's frame time or image quality.

Arm Streamline 9.9 adds profiling for neural graphics workloads that use the ML extensions for Vulkan. The Mali Timeline places Data Graph work beside the rest of the system and separates Mali NX execution from shader execution.

Dispatch Graph Workloads then shows which graph operations consumed the time, fell back to shaders, or behaved as outliers. Follow [Profile Arm Neural Technology workloads with Streamline](/learning-paths/mobile-graphics-and-gaming/streamline-nx/) for device setup, capture, and analysis. Later, [use the model toolkit](/learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-integrate/07-model-toolkit/) to decide which evidence you need at each stage.

## What remains experimental

NSSD represents a more advanced and demanding use of neural graphics. Arm has built and demonstrated the technology, but this playbook doesn't present it as a product you can enable. Treat it as experimental Early Access exploration with Arm. Later, you'll learn what it could unlock and when that exploration makes sense.

## What you've learned

You can act now through public NFRU and NSS integration routes, while NSSD remains an experimental Early Access exploration with Arm. Next, choose the route that matches your goal, engine, and appetite for engineering change.
