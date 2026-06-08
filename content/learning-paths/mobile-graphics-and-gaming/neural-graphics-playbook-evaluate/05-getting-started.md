---
title: Getting started with NFRU and NSSD
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

At this point, you should have a good sense of whether neural graphics is something worth exploring for your game. You can start with NSS and explore the Neural Graphics Development Kit today, but this section is about taking that first step into the latest developments.

## NFRU

NFRU is a good entry point to start evaluating neural graphics. The setup is designed to feel familiar. You integrate the plugin, enable it in your project, and evaluate it the way you would any other rendering feature.

The NFRU plugin will be available publicly in the coming weeks. In the meantime, if you want early access, you can sign up for the Early Access Program to start experimenting. 

[Sign up to the NFRU Early Access Program](https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics/early-access-program)

Try it in a representative scene, look at how it behaves with your content, and get a feel for the tradeoffs — especially around motion, UI, and responsiveness.

## NSSD

Getting started with NSSD is a different kind of effort. There isn’t a plug-and-play path here today. The work we’ve done with NSSD — especially in combination with MegaLights — required deeper integration into the rendering pipeline, including modifications to Unreal Engine itself.

If you’re curious about what that looks like in practice, we’re sharing more detail in the following blog, which describes how we approached lighting at scale and how NSSD fits into that setup:

[Lighting at Scale: Bringing Hundreds of Dynamic Lights to Mobile with Unreal MegaLights](https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/lighting-at-scale-bringing-hundreds-of-dynamic-lights-to-mobile-with-unreal-megalights)

The blog should give you a clearer picture of what’s involved, and whether it’s something you want to explore further.

At this stage, it's best to approach NSSD as an experiment rather than a feature. It’s something you evaluate if you’re interested in pushing beyond what’s currently possible with traditional techniques — particularly around dynamic lighting — but it comes with a higher barrier to entry.

You’ll need to be comfortable working closer to the rendering pipeline, and expect some iteration to get stable results for your content.

In the final chapter, we’ll shift focus slightly and look at what it means to bring models into your workflow. That’s where things become more open-ended. If you decide to go down that path, expect to learn as you go — this is still new territory for most game teams, and part of the process is building that knowledge over time.
