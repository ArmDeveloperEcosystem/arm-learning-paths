---
title: Validate live parallel inference
description: Verify the startup image, live camera UI, NPU interrupts, and rolling parallel timing values.
weight: 6
layout: "learningpathall"
---

The application validates the inference path before it consumes camera frames. This separates model or NPU failures from camera and ISP failures.

## Check the startup test

After reset, the display shows the bundled image of a man and a baby. The U55 model draws two green face boxes. The person and face indicators are green.

The U4 log includes model preparation and isolated preflight messages similar to:

```output
dual-et: starting parallel worker threads
dual-et: YOLO faces=2 candidates=13
dual-et: isolated U55 done irqs=1/0
dual-et: isolated U85 done irqs=1/1
dual-et: startup self-test passed; switching to camera in 5 seconds
```

The exact inference times and memory addresses vary between builds.

## Check the live camera UI

After five seconds, the application clears the test image and starts the MT9M114 stream. Confirm these results:

- The 352 x 352 live preview appears near the center of the MW405 display.
- The preview is in color and updates when you move the camera.
- Green boxes track faces in the live frame.
- `P` changes with the Visual Wake Words person result.
- `F` changes with the YOLO face result.
- The lower status area shows rolling U55, U85, span, and overlap values.

The log confirms the transition:

```output
dual-et: live dual-NPU pipeline started
```

## Confirm both NPUs execute for each frame

The coordinator wakes both Zephyr worker threads before waiting for their completion. Every tenth frame, the application prints the current and average timing values:

```output
dual-et: PAR PERSON frame=10 sample=10 U55=... U85=... span=... overlap=... us avg U55/U85/span/overlap=.../.../.../... us
```

Use the fields as follows:

| Field | Meaning |
| --- | --- |
| `U55` | YOLO execution time on Ethos-U55 |
| `U85` | Visual Wake Words execution time on Ethos-U85 |
| `span` | Time from the first worker starting to the last worker finishing |
| `overlap` | Time during which both model executions overlap |

The two NPU interrupt counters also increase during live operation:

```output
dual-et: live frame=30 IRQs=.../...
```

Changing the scene changes the preview, tensor checksums, and detection results. If the image and results remain fixed, the application is still using the startup test input instead of live frames.

You have now built, flashed, and validated a Zephyr application that drives
two Ethos-U NPUs with separate persistent worker threads on one Cortex-M55.
This design runs both ML workloads without adding a second MCU and its
associated system power overhead.
