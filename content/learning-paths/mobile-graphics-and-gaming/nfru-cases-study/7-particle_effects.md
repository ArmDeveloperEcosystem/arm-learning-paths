---
title: Particle effects
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Particle effects

In NFRU-generated intermediate frames, particle effects can show visible artifacts because many translucent or alpha-blended particles may not provide stable depth or motion-vector information after composition.

Compare the previous frame, current frame, and `InterpolatedRT` to find whether the generated frame preserves the particle shape and position.

![Side-by-side comparison showing the previous frame, current frame, and InterpolatedRT frame for a particle effect#center](./images/particles/full_comparison.png "Particle comparison across previous, current, and interpolated frames")

Common artifacts:

- **Blur or smear**: the particle color is warped using an estimated motion that does not match the actual particle movement, especially for smoke, sparks, fire, or trails.
- **Disappear or flicker**: particles that fade in/out, spawn, die, or change opacity between real frames may not have a stable match, so the generated frame may reduce or drop them.
- **Distortion**: optical flow may interpret changing shape, additive brightness, or overlapping particles as motion, producing stretched, bent, or duplicated particle regions.

The highlighted blur area shows a particle ring that loses definition in the generated frame. Look for soft edges, smeared color, or a shape that no longer matches either source frame.

![Marked particle blur area in the generated frame, with a zoomed inset showing the alpha-blended ring losing edge definition#center](./images/particles/blur_area_highlight.png "Blur artifact in alpha-blended particles")

The distortion callout shows particles that bend or stretch after interpolation. This usually means the generated frame is using an unreliable motion estimate for small, bright, fast-changing particle elements.

![Marked particle distortion area in the generated frame, with a zoomed inset showing stretched bright particles near the floor#center](./images/particles/distortion_zoom_in_marked_issue_generated.png "Distortion artifact in particles")

## Identify natural-looking generated particles

Some particle effects, such as fire, sparks, and smoke, already have random shapes from frame to frame. In those cases, the generated frame can look natural even if it doesn't match a physically exact intermediate shape. The result is usually acceptable when the particle keeps the expected color, brightness, and approximate location during playback.

The highlighted thruster fire shows a generated particle result that still reads naturally because the effect is noisy, soft-edged, and expected to change shape quickly.

![Marked thruster fire particle area in the generated frame, with a zoomed inset showing a natural-looking random fire shape near the drone exhaust#center](./images/particles/natural_result_area_highlight.png "Natural-looking generated fire particles")

## What you've learned and what's next

In this section, you inspected how particle effects can affect NFRU-generated frames. You learned that alpha blending, fast opacity changes, noisy shapes, and missing or unreliable motion data can lead to blur, distortion, flicker, or dropped particle detail in the interpolated frame.

Next, continue with NFRU performance analysis to understand how frame generation affects render FPS, present FPS, and frame pacing during gameplay.
