---
title: About Neural Dawn
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## A game designed around neural graphics

Neural Dawn is a mobile game we built together with Sumo Digital. They focused on the game itself - design, gameplay, art - while we focused on the rendering pipeline and neural graphics systems underneath it.

The goal was to answer a simple question: _What can a game look like if you design it around neural graphics from the start?_

We had three things we wanted to hit at the same time.

First, it had to look good, like _really_ good. The lighting fidelity and scene complexity you would expect from a PC or console game, but on mobile.

Second, it had to run efficiently. We targeted 60 FPS to meet modern expectations for smooth, responsive mobile gameplay.

And third, it had to show what becomes possible when neural graphics and Arm NX are used together with approaches such as MegaLights, on mobile.

Instead of optimizing a traditional graphics pipeline, we built one that depends on neural reconstruction. Neural Dawn is built around MegaLights. We render at low resolution tracing a low amount of rays per pixel, then rely on:

- Neural Super Sampling Denoising (NSSD) to denoise and upscale the image
- Neural Frame Rate Upscaling (NFRU) to generate intermediate frames

So, the final result looks like a clean, high-resolution, smooth experience, even though we rendered only about one-eighth of the pixels directly.

Ultimately, Neural Dawn shows that neural graphics on mobile are production ready.

TODO: trailer link

## Enabled by neural technology

NFRU and NSSD both help you reach the same end goal. The difference is in what you get out of that.

### NFRU

NFRU gives you extra frames without having to render them. By taking two real frames and generating the one in between, NFRU allows you to go from something like 30 FPS to 60 FPS. You still need to hit your base frame rate target consistently, and there is additional cost associated with NFRU itself, but it can significantly reduce the amount of rendering work needed to reach higher output frame rates.

Some teams will use that added budget to hit a higher frame rate. Others will keep the same target and spend elsewhere: more effects, better lighting, higher quality settings. The important part is that it doesn’t force you to change how your content is built. You’re still rendering the same frames, just fewer of them.

It also stacks well with other techniques. Overall, NFRU is a fairly predictable trade. If you’re looking for something you can try quickly and get value from, this is it.

{{< youtube-nocookie id="YQK1QATQHtI" title="NFRU splitscreen" >}}

### NSSD

NSSD is about making noisy, low-cost rendering usable. If you’ve worked with ray tracing, you’ve seen the issue. At real-time budgets, you can only afford a few rays per pixel. That gives you a very noisy image. Traditional shader- based denoisers help, but can struggle in challenging scenarios (for example, translucent particles such as fire or mist).

Unlike shader-based approaches, which often process diffuse, specular, shadows, and other signals separately, NSSD uses a neural network to reconstruct the final lighting result directly. Doing so allows NSSD to perform denoising and upscaling together in a single pass, reducing the need for multiple specialized denoising stages.

In practical terms, with NSSD, you can achieve high-quality rendering with Raytracing. We validated NSSD with Project Dawn with the following setup:

Rendering at 540p and upscaling to 1080p, tracing 1 ray per pixel with MegaLights.

Normally, lighting cost scales with scene complexity. More lights = more cost. With stochastic techniques, you can keep the cost roughly constant, but the image gets noisy. NSSD cleans up that noise after the fact and makes the content usable.

That’s what enables things such as:

- lots of dynamic lights in a scene
- soft shadows from all lights
- more complex lighting setups without baking

NSSD lets you build scenes that you wouldn’t normally even try to render in real-time (on any platform – not just mobile).

{{< youtube-nocookie id="CzBwmQNBGAA" title="NFRU and NSSD splitscreen" >}}

So, what is the bottom line?

NFRU and NSSD don’t compete—they sit at different levels:

- NFRU helps you stretch your existing budget
- NSSD lets you spend that budget in different ways

You can use NFRU without touching your content.

You can’t really use NSSD that way — it depends on how your game looks and how much you’re willing to invest in getting good results.

That’s why most teams will start with NSS and NFRU, and treat NSSD as something to explore when they’re ready to go deeper. In the next section, you'll learn what is really behind these technologies, and how we enable them through tooling.
