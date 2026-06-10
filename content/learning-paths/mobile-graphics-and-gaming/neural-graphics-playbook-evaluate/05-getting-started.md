---
title: Get started with NFRU and NSSD
description: Begin evaluating NFRU through the Unreal Engine plugin and explore NSSD integration with MegaLights for deeper rendering pipeline customization.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview 

If you've determined Arm Neural Technology is worth exploring for your game, you can start with NSSD and the Neural Graphics Development Kit today. This section covers the first steps into the latest developments.

## NFRU

NFRU is a good entry point for evaluating Arm Neural Technology. The setup is designed to feel familiar. You integrate the plugin, enable it in your project, and evaluate it the way you would any other rendering feature.

The NFRU plugin will be available publicly in the coming weeks. For early access, sign up for the Early Access Program to start experimenting.

[Sign up to the NFRU Early Access Program](https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics/early-access-program)

Test it in a representative scene, observe how it behaves with your content, and understand the tradeoffs—especially around motion, UI, and responsiveness.

## NSSD

Getting started with NSSD requires a different kind of effort. There isn't a plug-and-play path today. NSSD—especially in combination with MegaLights—requires deeper integration into the rendering pipeline, including modifications to Unreal Engine itself.

For more detail on what this looks like in practice, see the following blog, which describes the approach to lighting at scale and how NSSD fits into that setup:

[Lighting at Scale: Bringing Hundreds of Dynamic Lights to Mobile with Unreal MegaLights](https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/lighting-at-scale-bringing-hundreds-of-dynamic-lights-to-mobile-with-unreal-megalights)

This gives you a clearer picture of what's involved and whether it's something worth exploring further.

Approach NSSD as an experiment rather than a feature. Evaluate it if you're interested in pushing beyond what's currently possible with traditional techniques—particularly around dynamic lighting—but expect a higher barrier to entry.

You'll need to be comfortable working closer to the rendering pipeline and expect iteration to get stable results for your content.

The final section looks at what it means to bring models into your workflow. This is where things become more open-ended. If you decide to go down that path, expect to learn as you go—this is still new territory for most game teams, and part of the process is building that knowledge over time.
