---
title: Occlusion Objects
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Occlusion objects

When an object moves in front of another surface, NFRU has to generate an intermediate frame where part of the background is being covered (occlusion-in) or revealed (occlusion-out). These pixels are difficult to reconstruct because the correct intermediate content may not exist clearly in either rendered frame.

In an occlusion-in case, foreground and background pixels compete for the same intermediate area. If depth, motion vectors, or optical flow do not agree, the generated frame may blend background color into the foreground edge or produce a soft or doubled contour.

The occlusion-in generation sequence shows how the previous and current interpolation sources combine into `InterpolatedRT` as the foreground object covers the background.

<figure>
  <img src="./images/occlusion_in/interpolated_rt_generation_steps_no_text.gif" alt="NFRU occlusion-in interpolation sequence showing the previous and current source frames generating an intermediate frame as a foreground object covers background pixels">
  <figcaption>Occlusion-in interpolation sequence</figcaption>
</figure>

The marked close-up highlights the generated artifact at the occlusion edge, where background pixels bleed into the foreground area.

<figure>
  <img src="./images/occlusion_in/zoom_in_marked_issue_generated.png" alt="Close-up of the occlusion-in artifact with the problem area marked, showing blended pixels along the foreground edge in the generated frame">
  <figcaption>Marked occlusion-in artifact</figcaption>
</figure>

In an occlusion-out case, newly revealed background may be missing from the previous frame. NFRU must infer or fill that area from nearby pixels and warped samples. If the revealed area is large, thin, or moving quickly, the fill can use the wrong source, causing smearing, holes, flicker, or incorrect texture.

The occlusion-out generation sequence shows how the interpolated frame handles background pixels that become visible as the foreground object moves away.

<figure>
  <img src="./images/occlusion_out/interpolated_rt_generation_steps_no_text.gif" alt="NFRU occlusion-out interpolation sequence showing the previous and current source frames generating an intermediate frame as background pixels are revealed">
  <figcaption>Occlusion-out interpolation sequence</figcaption>
</figure>

The marked close-up shows the revealed area where NFRU uses an incorrect source or fill, creating a visible artifact in the generated frame.

<figure>
  <img src="./images/occlusion_out/zoom_in_marked_issue_generated.png" alt="Close-up of the occlusion-out artifact with the problem area marked, showing incorrect generated pixels where background is revealed">
  <figcaption>Marked occlusion-out artifact</figcaption>
</figure>

## What you've learned and what's next

In this section, you inspected how occlusion changes can affect NFRU-generated frames. You learned that occlusion-in and occlusion-out regions are challenging because foreground, background, depth, motion vectors, and optical flow can disagree about which pixels should appear in the interpolated frame.

Next, continue evaluating NFRU output in transparency-heavy content, where alpha blending and particle effects can introduce a different set of frame-generation artifacts.
