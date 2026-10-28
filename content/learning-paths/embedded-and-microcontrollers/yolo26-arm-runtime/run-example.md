---
title: Run your first object detection with YOLO26n
description: Prepare Raspberry Pi 5 and run the YOLO26n video example to produce detections and an annotated MP4.

weight: 2
layout: "learningpathall"
---

## Arm Runtime for YOLO26 on Raspberry Pi 5

Arm Runtime for YOLO26 on Raspberry Pi 5 is optimized to run YOLO26n inference on the CPU of the Pi. It uses a fixed inference schedule, planned memory reuse, and fused operations on the Arm Cortex-A76 cores of the Pi.

You'll run object detection on a supplied video example with the optimized runtime. You can also use your own video or a live feed from a PiCamera.

You'll then understand how the Python example works, and how it uses the optimized runtime. You'll also learn more about why this runtime is so performant.

Finally, you'll export the same YOLO26n checkpoint to NCNN, a general-purpose runtime, on your Pi. You'll use the Ultralytics validation harness to compare inference latency for both runtimes.

## Prepare your Raspberry Pi

Connect to your Raspberry Pi. You can connect directly or over SSH.

Use 64-bit Raspberry Pi OS Trixie, and Python 3.13.

Install the following prerequisites on your Pi:

```bash
sudo apt update
sudo apt install --yes --no-install-recommends \
  build-essential ca-certificates cmake curl git libgl1 libglib2.0-0t64 \
  make patch python3 python3-venv tar gzip
```

Clone the Arm Runtime for YOLO26 on Raspberry Pi 5 repository:

```bash
git clone https://github.com/arm/Optimized-Runtimes.git
cd Optimized-Runtimes/yolo26-raspberry-pi-5
```

Run the remaining commands from this `yolo26-raspberry-pi-5` directory. Build the runtime from the same source checkout:

```bash
make runtime
```

The build downloads its dependencies and installs the library under `dist/runtime/`.

The Python examples use this library automatically.

## Run object detection

Run object detection on the supplied sample:

```bash
make example-video
```

The first example run downloads and checks the YOLO26n checkpoint and sample video. It converts the checkpoint and prepares a Python environment. It then runs detection on 200 frames at a model input size of 640 × 640. Later runs reuse the prepared files.

The output is similar to the following run on an 8GB Raspberry Pi 5 (no heatsink or cooling):

```output
Detection performance:
  throughput: 26.27 FPS
  detection time: 38.07 ms/frame
  frames: 200
  mean timing: preprocess 1.09 ms, inference 36.08 ms, postprocess 0.87 ms
  video decode and resize: 2010.36 ms total
```
Your timings will vary.

The frames per second (FPS) figure measures how quickly the detector processes frames that are already decoded and resized in memory. The figure includes preparing the model input, running inference, and converting predictions into detections. It excludes reading and decoding the video, resizing frames, saving the detection JSON, and drawing and encoding the output video.

The runtime accelerates model inference. It doesn't accelerate video decoding, resizing, drawing boxes, or encoding the output video. This example therefore reports detection FPS separately from those video-processing steps. It lists inference time separately from preprocessing and postprocessing.

## Check your results

The command writes `detections.json` and `rendered.mp4` under `examples/video/output/`. Check the frame count and print the first detected object:

```bash
python3 - <<'PY'
import json
from pathlib import Path

data = json.loads(Path("examples/video/output/detections.json").read_text())
assert len(data["frames"]) == 200
detection = next(
    detection
    for frame in data["frames"]
    for detection in frame["detections"]
)
print("Frames:", len(data["frames"]))
print("First detection:", detection)
PY
```

The output is similar to this example, which reports 200 frames and shows a class name, confidence, and bounding box for the first detection:

```output
Frames: 200
First detection: {'box': [10.625, 275.125, 131.625, 358.875], 'class_id': 64, 'class_name': 'mouse', 'confidence': 0.91943359375}
```

Open `examples/video/output/rendered.mp4` in a video player to inspect the boxes and labels.

If you're connected over SSH, use `scp` to copy the video back to your local machine for viewing.

## (Optional) Bring your own video, or use live feed from PiCamera

To use your own video, provide a file on the Pi with at least 200 frames:

```bash
make example-video VIDEO=/path/to/your-video.mp4
```

For a connected Raspberry Pi Camera, install the camera packages and run live detection without a preview:

```bash
sudo apt install --yes python3-picamera2 rpicam-apps
make example-camera
```

Press **Ctrl+C** to stop. For a live preview, see the [camera example instructions](https://github.com/arm/Optimized-Runtimes/tree/main/yolo26-raspberry-pi-5/examples/picamera2).

## What you've accomplished

You've run YOLO26n on the CPU of the Pi using the Arm Runtime.

Next, you'll understand how the example works, and learn how and why the runtime is optimized for Arm CPUs.
