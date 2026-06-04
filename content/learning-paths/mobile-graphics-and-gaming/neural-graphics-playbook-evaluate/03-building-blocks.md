---
title: The building blocks
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Up to this point, we’ve focused on the results of what we’ve built. The next step is understanding what’s actually involved in using these techniques. Starting with the core building blocks, the aim with this section is to make the technology easier to reason about in the context of your own game.

Arm provides the foundation: the Unreal Engine plugins, the SDK, prebuilt models, and tooling to run and evaluate them with today’s runtime path centered on Vulkan on Arm platforms. You also get reference implementations and sample content to help you get started quickly, all packaged in the Neural Graphics Development Kit mentioned in the introduction.

What you own is everything that makes this work in your game. That includes integrating the technology into your rendering pipeline, ensuring that required inputs such as motion vectors are correct, and evaluating whether the output meets your quality bar. You are also responsible for making tradeoffs between performance, quality, and latency, and for handling edge cases that arise from your specific content.

In some cases, you may also choose to customize or retrain models. More on that later.

The important takeaway is that neural graphics is not a feature you simply enable. It is a system you integrate, evaluate, and tune. Understanding that upfront will make the rest of the playbook (and your evaluation process) much more effective.

## Technical overview

## NFRU

NFRU — Neural Frame Rate Upscaling — is the part of the system that makes motion feel smooth. The way it works is by looking at two consecutive frames and estimating how every pixel moves between them. This is done using optical flow, which operates in image space and captures not just object motion, but also changes in lighting, shading, and other effects that show up in the final image.

Once you have that motion, both frames are warped toward the intermediate timestep. That gives you two different guesses for what the in-between frame should look like — one coming forward from the previous frame, and one coming backward from the next.

![Animation showing two consecutive frames being warped toward an intermediate timestep using optical flow, then combined by the NFRU neural network into a single coherent in-between frame#center](assets/nfru.gif "NFRU warping two frames toward an intermediate timestep")

Those guesses don’t line up perfectly. Some areas are missing, some disagree, and some are just wrong due to motion estimation errors. The neural network’s role is to resolve that. It looks at the warped inputs and the motion field, and learns how to combine them into a single, coherent frame. That includes deciding which input to trust, reconstructing newly visible regions, and smoothing out artifacts so the result is stable over time.

So rather than interpolating, NFRU is really doing a reconstruction of motion. It also deliberately sits at the very end of the pipeline. By that point, the image has already been denoised and upscaled, so the model is working with relatively clean inputs, which makes the problem much easier to solve.

## NSSD

NSSD — Neural Super Sampling and Denoising — is where most of the image quality is actually recovered. It takes a low-resolution, noisy render and turns it into something that looks like a clean, high-resolution frame.

The important thing to understand is that the input here is intentionally very rough. We’re rendering at 540p, and we’re only taking a few lighting samples per pixel. With stochastic rendering techniques like ReSTIR and MegaLights, that means the image is dominated by noise.

The pipeline is often described as a “compute, neural, compute” sandwich, which is actually a useful way to think about it. It starts with a preprocessing pass that gathers all the information the network needs. This includes not just the noisy radiance buffer, but also depth, normals, motion vectors, and material properties like albedo and specular.

That context allows the network to understand where surfaces begin and end, how they’re oriented, and how they move over time — which is exactly what you need to separate noise from real signal.

The neural network itself then processes this data. But instead of directly outputting a final image, it produces a set of intermediate signals that guide the rest of the pipeline.

From there, a series of compute passes reconstruct the image. One of the key ideas is the use of a multi-resolution pyramid. The image is represented at several levels of detail, from high-frequency (sharp but noisy) to low-frequency (smooth but blurred). The network predicts how to combine these levels for each pixel.

In practice, that means flat regions can be aggressively smoothed by pulling from lower-resolution representations, while edges and fine details stay sharp by relying more on high-resolution data. Instead of applying a fixed denoising filter, the system is adapting its behavior across the image.

On top of that, there’s a temporal component. Previous frames are reprojected using motion vectors and combined with the current frame, and a feedback tensor is fed back into the network on the next frame. That feedback loop gives the model a kind of memory. It allows it to learn when to trust historical data and when to rely on the current frame, which is what keeps the result stable instead of flickering.

By the end of the pipeline, you have a frame that is denoised, temporally consistent, and upscaled — for example from 540p to 1080p — even though it was never rendered that way directly.


## Putting them together

Once you put NSSD and NFRU together, the pipeline starts to look very different from a traditional renderer. If you look at the full system, you end up rendering on the order of one eighth of the total pixels across space and time.

That’s really the key takeaway. The renderer is no longer responsible for producing the final image. Its job is to produce just enough signal for the neural system to reconstruct everything else.

![Diagram of the full neural graphics rendering pipeline showing how NSSD denoises and upscales low-resolution frames while NFRU generates intermediate frames, resulting in roughly one eighth of pixels rendered directly#center](assets/pipeline.png "Full neural graphics rendering pipeline combining NSSD and NFRU")