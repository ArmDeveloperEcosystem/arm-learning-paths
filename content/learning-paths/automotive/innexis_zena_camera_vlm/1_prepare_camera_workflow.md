---
title: Prepare the camera-to-VLM workflow
description: Check the Zena CSS guest and prepare to collect one virtual camera frame and a vision-model response.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Validate the virtual platform for the camera-to-VLM workflow

This Learning Path extends [Run local LLM inference with llama.cpp on Arm Zena CSS](/learning-paths/automotive/innexis_zena_llamacpp/) by adding a vision model and projector. Continue in the same guest OS where you built and ran llama.cpp. You'll give Siemens Innexis Architecture Native Acceleration (ANA) a video file. You'll read one frame through the Zena CSS Linux guest OS virtual camera. Then, you'll run a vision-language model (VLM) on that saved frame inside the guest.

The workflow has four parts: 

```text
ANA file input → virtual camera bridge → guest OS `/dev/video0` → vision-capable model running with the existing `llama.cpp` binary
```

The model runs on the frame captured in the guest, so you don't need a separate download of the source photograph. It checks functional integration using one frame. It doesn't measure real-time video performance or physical hardware.

{{% notice Note %}}
The 90-minute Learning Path completion time is an estimate. It hasn't been measured from start to finish in a fresh chamber.
{{% /notice %}}

Run the following commands in the Zena Edge Workloads for Automotive Linux (EWAOL) guest OS:

```bash
cat /etc/os-release
uname -m
uname -r
grep -E '^(MemTotal|MemAvailable):' /proc/meminfo
df -h /
for tool in systemctl gst-launch-1.0 gst-inspect-1.0 sha256sum; do
    command -v "$tool" || printf 'Missing: %s\n' "$tool"
done
```

The guest that was used to test the Learning Path reported the following values: 

```output
ID=ewaol
VERSION="v2.1.0 (styhead)"
aarch64
6.6.54-yocto-standard
MemTotal:        8120232 kB
MemAvailable:    7854188 kB
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        28G  1.3G   25G   5% /
/usr/bin/systemctl
/usr/bin/gst-launch-1.0
/usr/bin/gst-inspect-1.0
/usr/bin/sha256sum
```
All four tools were found under `/usr/bin`. Your available memory and disk space will depend on the current virtual platform session.

Confirm that the `llama-cli` binary from the preceding Learning Path is available in this same guest OS:

```bash
LLAMA_CLI=/root/zena-llamacpp/llama.cpp/build/bin/llama-cli ; test -x "$LLAMA_CLI" && "$LLAMA_CLI" --version ; printf 'llama-cli prerequisite status: %s\n' "$?"
```

The output is similar to:

```output
version: 0.6.0-dev (build 11482, commit b86d2f075)
built with GNU 14.2.0 for Linux aarch64
llama-cli prerequisite status: 0
```

## Create directories for input and output

Create one directory for the camera image and VLM results:

```bash
WORK_DIR=/root/zena-camera-vlm ; mkdir -p "$WORK_DIR/frames" "$WORK_DIR/results" "$WORK_DIR/models" ; df -h "$WORK_DIR"
```

The ANA Auto Shutdown setting is configurable. Check the remaining session time in Lab Manager before starting a long model download. Save your files before the virtual platform stops.

## What you've accomplished and what's next

You've identified the guest OS and prepared a place to preserve the camera input and inference result. 

Next, you'll configure the virtual camera source.
