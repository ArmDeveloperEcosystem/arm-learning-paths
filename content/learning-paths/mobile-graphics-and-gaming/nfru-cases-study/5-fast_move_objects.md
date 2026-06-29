---
title: Fast Object Movement
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Fast object movement
Fast-moving or teleported objects can exhibit trailing artifacts or duplicated shapes during frame interpolation.

![Previous Current to Interpolated RT Issue#center](./images/fast_move_object/previous_current_to_interpolated_rt_issue.gif "Previous Current to Interpolated RT Issue")

NFRU attempts to synthesize intermediate frames between two rendered frames using motion vectors, optical flow, depth, and disocclusion masks. However, when a fast-moving object changes position significantly between frames, these signals can become ambiguous or incomplete. The algorithm may struggle to accurately determine where pixels should originate when motion is too large or when objects become newly visible or hidden.

![Fast Move Object Issue#center](./images/fast_move_object/fast_move_object_issue_1.png "Fast Move Object Issue")

Visually, this can appear as a distorted object, trailing artifact, duplicated shape, missing object parts, or incorrect blending
with the background. It is most common around fast-moving objects, thin geometry, sharp edges, particles, or objects
crossing in front of other surfaces.

For debugging, enable the NFRU debug view and inspect motion-vector-warped `tm1`/`tp1` color, optical-flow-warped `tm1`/`tp1` color, and disocclusion masks. Here, `tm1` means time minus one (`t-1`), and `tp1` means time plus one (`t+1`). These views should show whether the failure comes from engine motion vectors, optical flow, or mask/hole filling.

Use the console command:
```
r.NFRU.ShowDebugView 1
```

![NFRU Debug View#center](./images/fast_move_object/show_debug_view.png "NFRU Debug View")

## What you've learned and what's next

In this section, you inspected how fast-moving objects can affect NFRU-generated frames. You learned that large object motion can make motion vectors, optical flow, depth, and disocclusion masks harder to interpret, which can lead to trailing artifacts, duplicated shapes, or distorted object edges in the interpolated frame.

Next, continue evaluating NFRU output in additional gameplay scenarios so you can compare how occlusion, transparency, and other scene content affect visual quality.
