---
title: Wrapping up
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you've accomplished

You completed a case study workflow for Neural Frame Rate Upsampling (NFRU) with Project Moku. You learned how NFRU generates intermediate frames to improve presented smoothness, and how to evaluate both the visual quality and performance behavior of those generated frames.

In this Learning Path, you:

- Used Project Moku for NFRU performance and visual quality analysis.
- Enabled the Arm Neural Graphics Plugin in an Unreal Engine project.
- Validated NFRU with Streamline and RenderDoc.
- Compared real frame inputs, generated frame output, motion data, and debug views.
- Investigated visual artifacts caused by fast camera movement, fast object movement, occlusion changes, and particle effects.
- Reviewed how display refresh rate, VSync, platform frame pacing, Android Swappy, NFRU overhead, and the NFRU pace adjuster can affect the final FPS uplift.

## Key takeaways

NFRU can improve perceived smoothness by presenting generated frames between real rendered frames. In representative Moku gameplay, the overall visual quality remains good and the FPS uplift is noticeable, especially when the generated frames are presented with stable pacing.

NFRU is not perfect in every scenario. Artifacts are most likely in areas where the correct intermediate image is hard to infer. Fast camera movement can expose screen-edge regions with limited history. Fast-moving objects can create ambiguous motion. Occlusion-in and occlusion-out cases can mix foreground and background information. Alpha-blended particle effects can lack stable depth or motion data.

These issues are usually localized to difficult content rather than affecting the whole frame. Use Streamline, RenderDoc, and the NFRU debug views to understand whether an artifact comes from motion vectors, optical flow, depth, disocclusion masks, or content that is difficult for interpolation.

Performance analysis requires observing render FPS and present FPS separately. A higher present FPS is only useful when frame pacing remains stable and the generated frames fit within the available GPU and neural processing budget.

## Next steps

Apply the same workflow to your own Unreal Engine content. Start with a repeatable test scene, capture runs with NFRU disabled and enabled, inspect generated frames when artifacts appear, and use Streamline to check whether NFRU cost or pacing behavior limits the expected uplift.

For deeper investigation, continue with the related NFRU Unreal Engine setup, RenderDoc, and Arm Performance Studio guidance:

- [Set up the Unreal project](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/3-set_up_the_unreal_project/)
- [RenderDoc integration guide](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/7-renderdoc/)
- [Streamline](/learning-paths/mobile-graphics-and-gaming/ams/streamline/)
- [Neural Graphics Playbook - Evaluate](/learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/)
- [Fine-tune neural graphics models using Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym/)
- [Generate neural graphics datasets with Neural Graphics Data Capture in Unreal Engine](/learning-paths/mobile-graphics-and-gaming/neural-graphics-data-capture-unreal/)