---
title: Look beyond NFRU to NSSD
description: Understand what NSSD could unlock for advanced mobile rendering and decide whether to explore the technology with Arm.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## See the larger opportunity with NSSD

Neural Super Sampling and Denoising (NSSD) reconstructs a clean, high-resolution frame from a low-resolution, noisy render. This can make low sample counts useful for advanced lighting and ray tracing. To learn more about the algorithm and Neural Dawn implementation, see the Arm [NSSD presentation](https://community.arm.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-20-66/2026_2D00_mmg_2D00_liam_2D00_nssd.pdf).

<!-- TODO: Add the NSSD recorded presentation embed when the public URL is available. -->

## Decide whether NSSD changes the game

NSSD matters when it changes the content you can build, not only the frame time. Arm and Sumo Digital used NSSD with dynamic lighting and reduced dependence on baked lighting to build [Neural Dawn](/learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/02-neural-dawn/).

NSSD also reaches deeper into the renderer and model workflow than NFRU. Use the [NSSD guidance in Arm Neural Technology Playbook - Evaluate](/learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/04-evaluating-fit-for-your-game/) for the content tradeoffs. Consider an investigation when the following conditions are true:

- Advanced dynamic lighting is central to the visual identity of the game.
- Graphics, art, and ML specialists can change the renderer together.
- You can capture representative data and define a high-quality reference.
- You can fund a research phase and maintain a fallback rendering path.

## Approach NSSD as an exploration with Arm

NSSD isn't a public product or plugin. To explore NSSD, [apply to the Arm Neural Technology Early Access Program](https://developer.arm.com/mobile-graphics-and-gaming/neural-technology/early-access-program) with your visual goal, target content, renderer, and team. Include available evidence from your evaluation, such as representative captures, measured results, or documented gaps.

## What you've learned and what's next

NSSD is the most demanding route in this playbook and potentially the most transformative. You've learned what circumstances make NSSD useful, and how you can explore it.

Next, you'll decide how to approach model work without committing too early.
