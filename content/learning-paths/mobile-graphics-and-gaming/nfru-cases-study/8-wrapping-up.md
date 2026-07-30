---
title: Wrapping up
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you've accomplished

You completed a case study workflow for Neural Frame Rate Upscaling (NFRU) with Project Moku. You learned how NFRU generates intermediate frames to improve presented smoothness, and how to evaluate both the visual quality and performance behavior of those generated frames.

## Key takeaways

NFRU provides a practical way to stretch an existing rendering budget. Its prebuilt neural model and Unreal Engine integration let you evaluate frame generation without introducing a new content-authoring workflow or building custom machine learning infrastructure.

In representative Moku gameplay, NFRU delivers a noticeable improvement in presented smoothness while maintaining good overall visual quality. The most demanding cases—visibility changes, alpha-blended particles, and dramatic lighting transitions—can produce localized differences where the correct intermediate image is difficult to infer.

The visible differences remain localized, making these scenarios useful evaluation targets. Streamline, RenderDoc, and the NFRU debug views make it possible to trace a difference to motion vectors, optical flow, depth, disocclusion masks, or content that is difficult for interpolation.

Performance analysis requires observing render FPS and present FPS separately. When generated frames fit within the available GPU and neural processing budget, the NFRU pace adjuster helps select a stable presentation target so the additional frames translate into consistently smoother motion.

## Next steps

Apply the same workflow to your own Unreal Engine content. Start with a repeatable test scene, capture runs with NFRU disabled and enabled, measure the smoothness and performance benefit, and then inspect any localized differences that affect your quality target. Use Streamline to select a sustainable presentation rate for the workload.

For deeper investigation, continue with the related NFRU Unreal Engine setup, RenderDoc, and Arm Performance Studio guidance:

- [Set up the Unreal project](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/3-set_up_the_unreal_project/)
- [RenderDoc integration guide](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/7-renderdoc/)
- [Streamline](/learning-paths/mobile-graphics-and-gaming/ams/streamline/)
- [Neural Graphics Playbook - Evaluate](/learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/)
- [Fine-tune neural graphics models using Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym/)
- [Generate neural graphics datasets with Neural Graphics Data Capture in Unreal Engine](/learning-paths/mobile-graphics-and-gaming/neural-graphics-data-capture-unreal/)

NFRU is one of the most approachable entry points into neural graphics: the model and engine integration are provided, no new content-authoring pipeline is required, and you can evaluate the benefit quickly in representative gameplay. Project Moku shows how you can use neural-accelerated hardware to present smoother motion while retaining the measurement, debugging, and pacing controls needed to meet your quality bar. Use this case study as a baseline, then bring that opportunity to your own game.
