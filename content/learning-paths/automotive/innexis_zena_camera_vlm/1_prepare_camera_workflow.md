---
title: Prepare the camera-to-VLM workflow
description: Check the Zena CSS guest and prepare to collect one virtual camera frame and a vision-model response.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the camera-to-VLM workflow

This Learning Path extends [Run Local LLM Inference with llama.cpp on Arm Zena CSS](../innexis_zena_llamacpp/). Continue in the same guest OS where you built and ran `llama.cpp`. You will give Siemens Innexis ANA a video file, read one frame through the Zena CSS Linux guest OS virtual camera, and run a vision-language model (VLM) on that saved frame **inside the guest**. Keep the image and response together so another developer can inspect the result.

The path has four parts: ANA file input → virtual camera bridge → guest OS `/dev/video0` → vision-capable model running with the existing `llama.cpp` binary. The video source and its license are identified on the next page. The model runs on the frame captured in the guest; a separate download of the source photograph is not required. This tutorial adds a vision model and projector to the previous [Run Local LLM Inference with llama.cpp on Arm Zena CSS](../innexis_zena_llamacpp/) environment. It checks functional integration using one frame; it does not measure real-time video performance or physical hardware.

The 90-minute completion time is an estimate. It has not been measured from start to finish in a fresh chamber.

Run in the **Zena EWAOL Linux guest OS**:

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

the tested guest reported EWAOL v2.1.0 (`styhead`), `aarch64`, Linux `6.6.54-yocto-standard`, 8,120,232 kB total memory, and 25 GB available on `/`. All four tools were found under `/usr/bin`. Your available memory and disk space will depend on the current VP session.

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

Confirm that the `llama-cli` binary from the preceding Learning Path is available in this **same guest OS**:

```bash
LLAMA_CLI=/root/zena-llamacpp/llama.cpp/build/bin/llama-cli ; test -x "$LLAMA_CLI" && "$LLAMA_CLI" --version ; printf 'llama-cli prerequisite status: %s\n' "$?"
```

In the current guest OS, the binary reported:

```output
version: 0.6.0-dev (build 11482, commit b86d2f075)
built with GNU 14.2.0 for Linux aarch64
llama-cli prerequisite status: 0
```

If the binary is absent, complete the preceding [Learning Path](../innexis_zena_llamacpp/) in this guest OS before continuing. This Learning Path does not repeat its source and build steps.

Create one directory for the camera image and VLM results:

<!-- VERIFY: Check that this path is writable and persists for the duration of the VP session. -->
```bash
WORK_DIR=/root/zena-camera-vlm ; mkdir -p "$WORK_DIR/frames" "$WORK_DIR/results" "$WORK_DIR/models" ; df -h "$WORK_DIR"
```

ANA's Auto Shutdown setting is configurable. Check the selected duration in Lab Manager before starting a long model download, and save your files before the VP stops.

## What you have learned

You have identified the guest OS and prepared a place to preserve the camera input and inference result. The next page configures the virtual camera source.
