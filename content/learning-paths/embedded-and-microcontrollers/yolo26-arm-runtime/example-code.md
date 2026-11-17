---
title: Understand the runtime and example code
description: Understand the specialized YOLO26n runtime, its build and Python API, and the video-processing steps around inference.

weight: 3
layout: "learningpathall"
---

## Understand the runtime

Arm Runtime for YOLO26 on Raspberry Pi 5 runs YOLO26n on the CPU of the Pi. The runtime uses a modified version of XNNPACK, with operations and kernels tailored to this model and device. It can plan the order of operations and reuse memory for intermediate results because it already knows the network structure.

When you create a detector, the runtime loads the weights and configuration of the converted model. It then prepares the XNNPACK operations to run.

This setup happens once. The detector then reuses those operations to process each frame.

This specialization lets the implementation reduce work in several ways:

| Choice | What it changes |
| --- | --- |
| Fixed schedule and memory plan | Reuses working memory according to when YOLO26n tensors are needed |
| Fused operations | Combines work such as convolution and SiLU activation, reducing separate operations and intermediate data movement |
| Pi-specific kernels | Uses Arm Neon FP16 operations suited to the Cortex-A76 CPU of the Pi|

General-purpose runtimes such as NCNN, ExecuTorch, and LiteRT support many network structures and operators. They can also fuse operations, reuse memory, and select optimized Arm kernels. The difference is that the specialized Arm Runtime is bespoke for this model and device. It can tailor its run schedule, memory layout, and kernels to squeeze out extra performance.

The tradeoff is flexibility. You can use compatible fine-tuned YOLO26n weights and the supported input resolutions with this runtime. You can't load an unrelated network or a different YOLO model size and expect it to run without implementation changes.

## How the runtime is built

The `make runtime` command that you ran during setup invokes CMake. CMake fetches pinned build dependencies and applies project patches. It compiles and checks the runtime, and installs the library under `dist/runtime/`.

The converter reads the pinned `yolo26n.pt` checkpoint and prepares the model for the fixed topology of the runtime.

The example uses a Python package, a compiled shared library, and a converted model. They have separate roles:

| Artifact | Purpose |
| --- | --- |
| `arm_yolo26n` | Python package, installed in `examples/.venv`; provides the detector API |
| `dist/runtime/lib/libarm-yolo26n.so.0` | Compiled CPU inference library built from `make runtime` |
| `dist/models/yolo26n-640/model.bin` | Converted model weights and metadata |
| `dist/models/yolo26n-640/manifest.json` | Model shapes, labels, and integrity information checked by Python |

## Understand the runtime API

Open `examples/video/detect.py`. Its main function imports the detector and passes the runtime and model paths explicitly:

```python
from arm_yolo26n import Yolo26Detector

with Yolo26Detector(runtime=args.runtime, model=args.model) as detector:
    video = _preload(args.video, args.frame_count, detector.input_shape[3])
    records, summary = _run_model(detector, video)
```

`make example-video` supplies these paths as command-line arguments. `Yolo26Detector` creates a `Yolo26nTensorSession`, which checks the model manifest and binary, then loads the shared library using Python's `ctypes.CDLL`.

The wrapper calls the library's C API. `y26_native_create` copies the model bytes and allocates working memory. It creates a four-worker thread pool, and builds 19 fixed XNNPACK subgraphs. This setup happens once. The detector is reused across frames, and leaving the `with` block calls `y26_native_destroy` to release its runtime resources.

For each prepared frame, the application calls:

```python
result = detector.detect(frame, pixel_format="BGR")
```

`Yolo26Detector` provides the image-level API, including preprocessing and postprocessing. Its `Yolo26nTensorSession` calls `y26_native_execute` for inference. Applications that already prepare their own tensors can use the tensor session directly. The tensor interface accepts FP32 input arrays and returns FP32 predictions. Most intermediate runtime tensors use FP16.

## Follow the object-detection pipeline

The remaining code handles the usual steps around model inference. OpenCV reads the video as BGR images. `_preload` decodes and resizes the requested frames before detection is timed. `_run_model` performs one warm-up call, then processes the measured frames.

Within each `detect` call, preprocessing pads the image and converts BGR to RGB. It normalizes pixel values and arranges them into the model's input tensor. After runtime inference, postprocessing filters predictions and applies non-maximum suppression to remove overlapping detections. Postprocessing returns class labels, confidence scores, and bounding boxes.

The example records detections and separate preprocessing, inference, and postprocessing timings in JSON. Boxes use resized inference-frame coordinates. The separate `examples/video/render.py` command maps them back to the original video dimensions, draws labels and boxes, and encodes the MP4. These video-processing steps are application work outside the inference runtime.

## What you've learned and what's next

You've learned that the runtime specializes running operations for YOLO26n on the Pi, and `make runtime` builds it from your source checkout. The Python API connects the application to that compiled library. The surrounding video and detection code prepares inputs and presents results.

Next, you'll compare the runtime with a general purpose runtime, using the same checkpoint and validation images.
