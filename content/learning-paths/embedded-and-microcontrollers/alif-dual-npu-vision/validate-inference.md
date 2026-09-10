---
title: Validate live parallel inference
description: Verify the startup image, live camera UI, NPU interrupts, and rolling parallel timing values.
weight: 6
layout: "learningpathall"
---

## Check the startup test

The application validates the inference path before it consumes camera frames. This separates model or neural processing unit (NPU) failures from camera and image signal processor (ISP) failures.

After reset, the display shows the bundled Grace Hopper image. The U55 model draws one green face box. The U85 result identifies an ImageNet class such as `ACADEMIC GOWN`.

The U4 log includes model preparation and isolated preflight messages similar to:

```output
dual-et: starting parallel worker threads
dual-et: SSD persons=1 candidates=...
dual-et: frame=0 CLASS=400 ACADEMIC GOWN confidence=...%
dual-et: isolated U55 done irqs=1/0
dual-et: isolated U85 done irqs=1/1
dual-et: startup self-test passed; switching to camera in 5 seconds
```

The exact inference times and memory addresses vary between builds.

## Check the live camera UI

After 5 seconds, the application clears the test image and starts the MT9M114 stream. Confirm the following results:

- The MW405 display shows a 480 x 352 live preview.
- The preview is in color and updates when you move the camera.
- Green boxes track faces in the live frame.
- The classification label and confidence change with the scene.
- Face boxes appear when SSD-Slim detects a face.
- The lower status area shows rolling U55, U85, span, and overlap values.

The log confirms the transition:

```output
dual-et: live dual-NPU pipeline started
```

{{% notice Note %}}
If the preview is grainy or monochrome, the application is displaying packed sensor data as RGB565. Confirm that the build includes both ISP overlays and that the selected video endpoint is `isp@49046000`. The native pipeline requests planar RGB888 output from the ISP before it creates the display preview and model inputs.
{{% /notice %}}

## Confirm both NPUs execute for each frame

The coordinator wakes both Zephyr worker threads before waiting for their completion. Every tenth frame, the application prints the current and average timing values:

```output
dual-et: PAR class=... frame=10 sample=10 U55=... U85=... span=... overlap=... us avg U55/U85/span/overlap=.../.../.../... us
```

Use the fields as follows:

| Field | Meaning |
| --- | --- |
| `U55` | SSD-Slim `Method::execute()` wall time on Ethos-U55 |
| `U85` | MobileNetV2 `Method::execute()` wall time on Ethos-U85 |
| `span` | Time from the first worker starting to the last worker finishing |
| `overlap` | Time during which both model executions overlap |

These are Cortex-M cycle-counter wall-time measurements around delegated `Method::execute()` rather than NPU PMU active-cycle counts. Input preparation and result decoding are outside these intervals. The two NPU interrupt counters also increase during live operation:

```output
dual-et: live frame=30 IRQs=.../...
```

Changing the scene changes the preview, tensor checksums, and detection results. If the image and results remain fixed, the application is still using the startup test input instead of live frames.

{{% notice Note %}}
If the startup test completes but the live result doesn't change, confirm that `dual-et: live dual-NPU pipeline started` appears and that the live-frame messages and NPU interrupt counters continue to increase.

If capture errors repeat, power-cycle the board, flash the package again, and recheck the camera connector and overlay order.
{{% /notice %}}

## What you've accomplished

You've now built, flashed, and validated a Zephyr application that drives
two Ethos-U NPUs with separate persistent worker threads on one Cortex-M55.
This design runs both ML workloads without adding a second microcontroller unit and its
associated system power overhead.

You can now use the workflow to run ExecuTorch models for your own use cases concurrently on separate Ethos-U NPUs under Zephyr.