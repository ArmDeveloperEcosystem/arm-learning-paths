---
title: Test NFRU against your game
description: Use Project Moku and Streamline 9.9 to plan repeatable NFRU quality, performance, and frame-pacing tests.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Define the pass condition

Your evaluation has one question: *Can NFRU meet the game's presentation target within its quality, latency, power, and thermal limits?*

Use the [Project Moku case study](/learning-paths/mobile-graphics-and-gaming/nfru-cases-study/) to rehearse the test, then repeat it with your game. Set the thresholds before looking at the result; the [evaluation guidance in Arm Neural Technology Playbook - Evaluate](/learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/04-evaluating-fit-for-your-game/) explains the wider tradeoffs.

| Area | Record | Define |
| --- | --- | --- |
| Presentation | Render FPS, present FPS, frame-time distribution | Target cadence and pacing variance |
| Cost | GPU and neural time, power, thermals | Maximum cost and sustained duration |
| Quality | Captures from difficult content | Acceptable artifacts in motion |
| Responsiveness and reach | Latency and device coverage | Latency limit and fallback policy |

## Run one controlled pass

1. **Capture a baseline.** Record the same short action with NFRU disabled and enabled under fixed conditions.
2. **Stress the content.** Use the [Project Moku occlusion test](/learning-paths/mobile-graphics-and-gaming/nfru-cases-study/4-occlusion_objects/), [Project Moku particle-effects test](/learning-paths/mobile-graphics-and-gaming/nfru-cases-study/5-particle_effects/), and [Project Moku lighting-change test](/learning-paths/mobile-graphics-and-gaming/nfru-cases-study/6-lighting_change/) to select relevant scenes from your game.
3. **Measure execution.** Follow the [Streamline and RenderDoc workflow](/learning-paths/mobile-graphics-and-gaming/nfru-cases-study/3-validate_nfru_with_streamline_and_renderdoc/) to confirm neural activity and inspect unexpected output.
4. **Check presentation.** Compare render FPS with present FPS and use the [frame-pacing analysis](/learning-paths/mobile-graphics-and-gaming/nfru-cases-study/7-nfru_performance/) to choose a sustainable target.

Keep the model unchanged. First determine whether a failure comes from inputs, content, runtime cost, or pacing.

## Profile graph execution on NX

On a supported NX target, Streamline 9.9 connects a slow frame to the graph operation behind it. Follow [Profile Arm Neural Technology workloads with Streamline](/learning-paths/mobile-graphics-and-gaming/streamline-nx/) to prepare your device and debuggable application, collect a capture through the CLI or GUI, and inspect neural accelerator activity.

Select the interval in the Mali Timeline, then use Dispatch Graph Workloads to find expensive operations, outlier dispatches, and shader fallbacks. Repeat the same capture after each change. The [Streamline neural-graphics profiling overview](https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/profile-neural-graphics-workloads-with-arm-streamline) explains the graph-analysis views and CSV export options.

## Make the call

- **Continue** if the integration meets every threshold
- **Iterate** if the failure is reproducible and has a credible fix
- **Stop** if quality, latency, sustained cost, or fallback misses the product target

## What you've accomplished

You now have a controlled NFRU result and a clear decision. Next, consider whether the more demanding NSSD route belongs in your plan.
