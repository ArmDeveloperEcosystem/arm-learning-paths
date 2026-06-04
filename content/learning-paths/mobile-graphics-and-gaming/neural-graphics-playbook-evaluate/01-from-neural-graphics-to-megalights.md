---
title: "From Neural Graphics to MegaLights, and beyond: could it be for me?"
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The opportunity: why neural graphics, why now

When we first started talking about neural graphics at Arm, the idea was pretty simple: if some parts of rendering can be done more efficiently with machine learning, that frees up budget for everything else. At SIGGRAPH 2025, we announced that [Arm GPUs will have dedicated neural accelerators (NX) in 2026](https://newsroom.arm.com/news/arm-announces-arm-neural-technology). Since then, we’ve worked hard to build the tools that developers will need to seamlessly evaluate and integrate neural graphics use cases.

On mobile, every rendering decision is a tradeoff. Resolution, lighting, effects, frame rate, thermals, battery life—they all compete for the same limited resources. And ultimately, those technical tradeoffs affect something even more important: the player experience. Visual quality matters, but so does responsiveness, stable performance, and how long a player can stay immersed in the game without the device heating up or throttling.

[Neural Super Sampling (NSS)](https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/how-to-access-arm-neural-super-sampling) was our first attempt at shifting that balance. Upscaling itself isn’t new. Shader-based upscalers are already widely used across game engines and mobile games because rendering at lower resolution is one of the most effective ways to save performance. What interested us was whether machine learning could push that idea further.

In practice, NSS allowed us to work with more aggressive upscale ratios, like rendering at 540p and reconstructing to 1080p, while maintaining image quality that would be difficult to achieve with more traditional approaches. It also opened up better NX utilization in Arm GPUs, while reducing pressure on bandwidth and energy consumption, which are often just as important to mobile developers as raw frame rate.

On mobile, bandwidth is expensive. Moving less data around the system can have a major impact on power efficiency and sustained performance. In many cases, that becomes just as valuable as the rendering speedup itself.

NSS was really a first step in exploring a bigger question: what happens if machine learning becomes a normal part of the rendering pipeline?

## From a single technique to something you can actually build on

This has resulted in the Neural Graphics Development Kit - a set of Vulkan based tools to support early experimentation of different neural graphics use cases that are production ready and efficient for mobile.

| Resource |
|----------|
| [Neural Graphics landing page](https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics) |
| [Enable Neural Super Sampling in Unreal Engine with ML Extensions](/learning-paths/mobile-graphics-and-gaming/nss-unreal/) |
| [ML SDK for Vulkan](https://github.com/arm/ai-ml-sdk-for-vulkan) |
| [Neural Super Sampling (NSS) model](https://huggingface.co/Arm/neural-super-sampling) |
| [ML Emulation Layer for Vulkan](https://github.com/arm/ai-ml-emulation-layer-for-vulkan) |
| [Neural Graphics Model Gym](https://github.com/arm/neural-graphics-model-gym) |

The development kit, the Unreal plugin, the sample content—those are provided so you can get started with minimal effort and validate how it behaves with your own content. And that’s really the point. It’s one thing to show a clean before-and-after in a controlled scene, and something else entirely when you’re dealing with dynamic lighting, fast camera movement, complex materials, and all the edge cases that come with real production conditions. That’s where things either hold up or start to break, and where you actually learn if a technique is useful.

Since then, we’ve been expanding neural graphics use cases beyond NSS into applications of frame generation and ray denoising, while also making sure it can be integrated in real projects. This playbook will focus on the techniques we’ve worked on since then, but NSS remains relevant as the most straightforward way to start evaluating neural graphics in a real project.

## Why this matters now

As engines like Unreal adopt more advanced techniques like ray tracing, new neural graphics use cases start to make sense in a practical way. Features like MegaLights make it possible to work with far more dynamic lights than before, without the cost scaling directly with the number of lights. The challenge is that these approaches rely on very low sample counts, which quickly introduce noise—especially on mobile.

Traditional denoisers and shader-based upscalers already help solve part of that problem. But as rendering pushes toward lower resolutions, fewer samples, and more dynamic lighting, reconstruction quality becomes harder to maintain. We’ve found that neural reconstruction allows us to push more aggressive upscale ratios, work with noisier inputs, and still produce stable, high-quality output. It also helps reduce bandwidth and energy pressure, which matters just as much as raw frame rate on mobile devices. More importantly, it starts making some of these newer rendering approaches practical on mobile in the first place.

## Enter Neural Dawn

Neural Dawn is how we validate the use cases are production ready.

It’s a mobile game created with Unreal Engine using Megalights, combined with the neural graphics work we’ve been developing. The goal was to build a real game and see what actually happens when you try to use this end to end. Where the integration feels natural, where it doesn’t, what kind of gains you get, and what trade-offs show up along the way.

## Why we’re sharing this playbook

This playbook is a reflection of that process. We wanted to share a record of the journey behind Neural Dawn—what worked, what didn’t, what surprised us, and what we’d approach differently next time.

There’s still a gap between seeing a technique and knowing whether it fits your game. That’s the gap we’re trying to close.

Some projects will benefit a lot from this kind of approach, others might not, and that’s fine. It depends on what you’re building, what constraints you’re working under, and artistic direction and features you care about in your game. The goal is to give you enough context and real-world experience to answer a more useful question: is this something worth exploring for your game?