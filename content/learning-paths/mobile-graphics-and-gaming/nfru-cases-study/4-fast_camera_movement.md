---
title: Fast Camera Movement
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Fast camera movement

Check the screen corners and outer edges while the camera moves quickly. The artifact usually appears on the interpolated frame as a brief color mismatch near the edge. The edge might look smeared, noisy, or flickery, or it might look as if it is using color from a nearby part of the image. This issue is most visible on the side of the screen that the camera moves toward, because that edge has the least reliable image information to reuse.

![Sample fast camera movement#center](./images/fast_camera_movement/sample_fast_camera_move.gif "Sample fast camera movement")

NFRU generates `InterpolatedRT` from two consecutive rendered frames: the previous interpolation source and the current interpolation source. Compare these frames together to understand how much camera movement and newly exposed scene area NFRU must account for.

![Side-by-side fast camera movement comparison showing InterpolatedRT, previous, and current frames in a corridor scene with large camera motion#center](./images/fast_camera_movement/full_comparison.png "Fast camera movement comparison across interpolated, previous, and current frames")

The interpolated frame shows the generated scene produced between the two source frames. Use the comparison to confirm whether artifacts are visible during normal gameplay motion.

![Interpolated NFRU frame from a fast camera movement scene, showing a corridor with visible edge artifacts near the screen boundaries#center](./images/fast_camera_movement/InterpolatedRT.png "Interpolated frame during fast camera movement")

The first callout highlights a corner region where color separation and smearing appear along the outer edge of the frame. These artifacts can occur when newly exposed screen-space regions don't have enough reliable information from the previous frame.

![Close-up of the upper-left screen corner in the interpolated frame, with an arrow highlighting color separation and edge smearing#center](./images/fast_camera_movement/InterpolatedRT_corner_artifact_1.png "Corner artifact during fast camera movement")

The second callout highlights artifacts along the lower edge of the interpolated frame. Watch for this type of artifact when the camera pans or turns quickly across high-contrast geometry.

![Close-up of the lower screen edge in the interpolated frame, with an arrow highlighting smearing and color mismatch near high-contrast geometry#center](./images/fast_camera_movement/InterpolatedRT_corner_artifact_2.png "Lower-edge artifact during fast camera movement")

Use RenderDoc to inspect the `r_mv_holes_tm1` and `r_mv_holes_tp1` buffers. Here, `tm1` means time minus one (`t-1`), and `tp1` means time plus one (`t+1`). These buffers show where motion-vector reprojection has holes or invalid regions in the previous (`t-1`) and next (`t+1`) temporal sources. The hole masks reveal areas where motion history is unreliable, particularly around object silhouettes and screen edges. When the interpolation pass samples from these unreliable areas, it picks up mismatched foreground and background pixels, creating noticeable edge-line artifacts in the final image.

| ![Motion-vector holes in previous frame#center](./images/fast_camera_movement/r_mv_holes_tm1.png "Motion-vector holes in previous frame (r_mv_holes_tm1)") | ![Motion-vector holes in next temporal source#center](./images/fast_camera_movement/r_mv_holes_tp1.png "Motion-vector holes in next temporal source (r_mv_holes_tp1)") |
| --- | --- |


## What you've learned and what's next

In this section, you inspected how fast camera movement can affect NFRU-generated frames. You learned that edge artifacts often appear near newly exposed screen regions, especially when rapid motion leaves limited reliable image information for interpolation.

Next, continue evaluating NFRU output in additional gameplay scenarios so you can compare how different types of motion and scene content affect visual quality.
