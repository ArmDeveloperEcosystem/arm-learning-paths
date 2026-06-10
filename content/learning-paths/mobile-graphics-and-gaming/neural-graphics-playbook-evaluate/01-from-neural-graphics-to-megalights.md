---
title: Evaluate Arm Neural Technology for your mobile game
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The opportunity: why Neural Technology, why now

Neural Technology addresses a straightforward problem: if you can handle some rendering tasks more efficiently with machine learning, you free up budget for everything else. At SIGGRAPH 2025, Arm announced that [Arm GPUs will have dedicated neural accelerators (NX) in 2026](https://newsroom.arm.com/news/arm-announces-arm-neural-technology). Arm Neural Technology provides the tools you need to evaluate and integrate these techniques into your projects.

On mobile, every rendering decision is a tradeoff. Resolution, lighting, effects, frame rate, thermals, battery life all compete for the same limited resources. Ultimately, those technical tradeoffs affect something even more important: the player experience. Visual quality matters, but so does responsiveness, stable performance, and how long a player can stay immersed in the game without their device heating up or throttling.

[Neural Super Sampling (NSS)](https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/how-to-access-arm-neural-super-sampling) was the first step in shifting that balance. Upscaling isn't new. Shader-based upscalers are already widely used across game engines and mobile games because rendering at lower resolution is one of the most effective ways to save performance. The question was whether machine learning could push that idea further.

NSS enables more aggressive upscale ratios, such as rendering at 540p and reconstructing to 1080p, while maintaining image quality that's difficult to achieve with traditional approaches. It improves NX utilization in Arm GPUs while reducing pressure on bandwidth and energy consumption — often just as important to mobile developers as raw frame rate.

On mobile, bandwidth is expensive. Moving less data around the system can have a major impact on power efficiency and sustained performance. This often becomes just as valuable as the rendering speedup itself.

NSS opened a bigger question: what happens when machine learning becomes a normal part of the rendering pipeline?

## From a single technique to something you can build on

Arm Neural Technology answers that question. It's a set of Vulkan-based tools you can use to experiment with different neural graphics techniques that are production ready and efficient for mobile.

| Resource |
|----------|
| [Neural Graphics landing page](https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics) |
| [Enable Neural Super Sampling in Unreal Engine with ML Extensions](/learning-paths/mobile-graphics-and-gaming/nss-unreal/) |
| [ML SDK for Vulkan](https://github.com/arm/ai-ml-sdk-for-vulkan) |
| [Neural Super Sampling (NSS) model](https://huggingface.co/Arm/neural-super-sampling) |
| [ML Emulation Layer for Vulkan](https://github.com/arm/ai-ml-emulation-layer-for-vulkan) |
| [Neural Graphics Model Gym](https://github.com/arm/neural-graphics-model-gym) |

The development kit, Unreal plugin, and sample content let you get started with minimal effort and validate how these techniques behave with your own content. Seeing a clean before-and-after in a controlled scene is one thing. Testing with dynamic lighting, fast camera movement, complex materials, and all the edge cases that come with real production conditions is another. That's where you learn whether a technique is actually useful.

Neural graphics use cases now extend beyond NSS into frame generation and ray denoising. This playbook focuses on those newer techniques, but NSS remains the most straightforward entry point for evaluating neural graphics in your project.

## Why this matters now

As engines such as Unreal adopt more advanced techniques such as ray tracing, new neural graphics use cases start to make sense in a practical way. Features such as MegaLights make it possible to work with far more dynamic lights than before, without the cost scaling directly with the number of lights. The challenge is that these approaches rely on very low sample counts, which quickly introduce noise, especially on mobile.

Traditional denoisers and shader-based upscalers already help solve part of that problem. But as rendering pushes toward lower resolutions, fewer samples, and more dynamic lighting, reconstruction quality becomes harder to maintain. Neural reconstruction lets you push more aggressive upscale ratios, work with noisier inputs, and still produce stable, high-quality output. It reduces bandwidth and energy pressure, which matters just as much as raw frame rate on mobile devices. More importantly, it makes these newer rendering approaches practical on mobile in the first place.

## Enter Neural Dawn

Neural Dawn validates that neural graphics techniques are production ready for real games.

Built as a mobile game with Unreal Engine and MegaLights, Neural Dawn tests these techniques in a complete, real-world project. Building an actual game reveals what works in practice — where neural graphics integrates naturally, where it creates friction, what performance gains emerge, and what tradeoffs you face. This hands-on approach provides credible insights that isolated demos can't.

## Why this playbook exists

This playbook reflects that process. It shares the journey behind Neural Dawn — what worked, what didn't, what was surprising, and what would be approached differently next time.

A gap exists between seeing a technique and knowing whether it fits your game. This playbook aims to close that gap.

Some projects will benefit from this approach, others won't. Success depends on what you're building, what constraints you're working under, and what artistic direction and features you care about. This playbook gives you enough context and real-world experience to answer the key question: is this worth exploring for your game?