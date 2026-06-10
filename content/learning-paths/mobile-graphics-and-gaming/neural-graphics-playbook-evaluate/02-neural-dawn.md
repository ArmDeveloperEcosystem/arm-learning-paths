---
title: About Neural Dawn
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## A game designed around Arm Neural Technology

Neural Dawn is a mobile game built in collaboration with Sumo Digital. Sumo Digital focused on the game design, gameplay, and art, while Arm focused on the rendering pipeline and neural graphics systems.

The goal was to answer a question: _What can a game look like when designed around neural graphics from the start?_

The project had three objectives:

First, deliver high-fidelity visuals. The lighting quality and scene complexity you'd expect from PC or console games, running on mobile.

Second, run efficiently. The target was 60 FPS to meet modern expectations for smooth, responsive mobile gameplay.

Third, demonstrate what becomes possible when neural graphics and Arm NX are used with approaches such as MegaLights on mobile.

Instead of optimizing a traditional graphics pipeline, Neural Dawn uses one that depends on neural reconstruction. The game is built around MegaLights. It renders at low resolution, tracing a small number of rays per pixel, then relies on:

- Neural Super Sampling Denoising (NSSD) to denoise and upscale the image
- Neural Frame Rate Upscaling (NFRU) to generate intermediate frames

The final result is a clean, high-resolution, smooth experience, even though only about one-eighth of the pixels are rendered directly.

Neural Dawn demonstrates that Arm Neural Technology techniques on mobile are production ready.

Watch the Neural Dawn trailer to see Arm Neural Technology in action:

{{< youtube-nocookie id="e4cnNm805YI" title="Neural Dawn trailer" >}}

## How NFRU and NSSD work

NFRU and NSSD help you reach the same end goal but differ in what they deliver.

### NFRU

NFRU gives you extra frames without rendering them. By taking two consecutive frames and generating the one in between, NFRU lets you go from 30 FPS to 60 FPS. You still need to hit your base frame rate target consistently, and NFRU itself has a cost, but it significantly reduces the rendering work needed to reach higher output frame rates.

Some teams use that budget to hit a higher frame rate. Others maintain the same target and invest elsewhere: more effects, better lighting, or higher quality settings. The key advantage is that it doesn't force you to change how your content is built. You're still rendering the same frames, just fewer of them.

NFRU stacks well with other techniques and offers a predictable tradeoff. If you're looking for something you can try quickly and get value from, NFRU is a good starting point.

{{< youtube-nocookie id="YQK1QATQHtI" title="NFRU splitscreen" >}}

### NSSD

NSSD makes noisy, low-cost rendering usable. If you've worked with ray tracing, you know the challenge. At real-time budgets, you can only afford a few rays per pixel, resulting in a very noisy image. Traditional shader-based denoisers help but can struggle in challenging scenarios, such as translucent particles like fire or mist.

Unlike shader-based approaches, which often process diffuse, specular, shadows, and other signals separately, NSSD uses a neural network to reconstruct the final lighting result directly. This allows NSSD to perform denoising and upscaling together in a single pass, reducing the need for multiple specialized denoising stages.

NSSD enables high-quality rendering with ray tracing. Neural Dawn validated NSSD with this setup:

Rendering at 540p and upscaling to 1080p, tracing one ray per pixel with MegaLights.

Normally, lighting cost scales with scene complexity: more lights means more cost. With stochastic techniques, you can keep the cost roughly constant, but the image becomes noisy. NSSD cleans up that noise and makes the content usable.

This enables:

- Many dynamic lights in a scene
- Soft shadows from all lights
- Complex lighting setups without baking

NSSD lets you build scenes you wouldn't normally attempt to render in real time on any platform, not just mobile.

{{< youtube-nocookie id="CzBwmQNBGAA" title="NFRU and NSSD splitscreen" >}}

## Choosing between NFRU and NSSD

NFRU and NSSD don't compete. They work at different levels:

- NFRU helps you stretch your existing rendering budget
- NSSD lets you spend that budget in different ways

You can use NFRU without touching your content.

You can't use NSSD that way. It depends on how your game looks and how much you're willing to invest in achieving good results.

Most teams start with NSS and NFRU, then treat NSSD as something to explore when ready to go deeper. The next section explains what's behind these technologies and how tooling enables them.
