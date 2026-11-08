---
title: Capture and inspect one frame
description: Save a JPEG frame from the virtual camera and check the file before model inference.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Capture and inspect one frame

First check whether the guest has the GStreamer elements needed for a JPEG capture:

```bash
for element in v4l2src videoconvert jpegenc filesink waylandsink; do
    if gst-inspect-1.0 "$element" >/dev/null 2>&1; then
        printf 'Available: %s\n' "$element"
    else
        printf 'Missing: %s\n' "$element"
    fi
done
```

In the reported Zena guest, all five elements were available:

```output
Available: v4l2src
Available: videoconvert
Available: jpegenc
Available: filesink
Available: waylandsink
```

If an element is missing in your guest, stop here and record the output. A replacement capture command must be tested with that guest image before it is added to the published path.

Capture a single frame in the **guest shell**. Keep the commands together so the pipeline result, file size, and hash appear in one terminal output. The `timeout` command prevents the capture from waiting indefinitely if no frame arrives:

<!-- VERIFY: This exact command passed after the file was selected through the camera control interface. The current filename reflects the experimental run; choose a reader-facing filename and rerun before publication. -->
```bash
WORK_DIR=/root/zena-camera-vlm ; FRAME_FILE="$WORK_DIR/frames/file-after-control.jpg" ; command -v timeout ; timeout 15s gst-launch-1.0 -e v4l2src device=/dev/video0 num-buffers=1 ! videoconvert ! jpegenc ! filesink location="$FRAME_FILE" ; CAPTURE_STATUS=$? ; printf 'Capture status: %s\n' "$CAPTURE_STATUS" ; if [ -s "$FRAME_FILE" ]; then ls -lh "$FRAME_FILE" ; sha256sum "$FRAME_FILE" ; else printf 'No nonempty frame captured\n' ; fi
```

The reported Zena run reached EOS, returned status `0`, and wrote a nonempty JPEG with this SHA-256:

```output
Got EOS from element "pipeline0".
EOS received - stopping pipeline...
Capture status: 0
-rw-r--r-- 1 root root 70K Nov  5 21:49 /root/zena-camera-vlm/frames/file-after-control.jpg
632e0ade2f7827eb33d9d099a615069a94f8254104f7770694a48b1dace3798a  /root/zena-camera-vlm/frames/file-after-control.jpg
```

After transfer to the local machine, the SHA-256 matched and file inspection showed a 640 × 480 JPEG. Visual inspection showed the row of parked vehicles from the selected source video. This validates one complete file-to-virtual-camera-to-guest-JPEG run.

![JPEG captured from the Zena CSS virtual camera showing parked cars#center](ana_automotive_camera_frame.jpg "A captured virtual camera frame")

The source photograph and its license are identified on the preceding page. The original photograph does not need to be downloaded into the guest: this tutorial tests the frame delivered through ANA's virtual camera.

Transfer the **captured camera frame** using your chamber's authorized file-transfer route, then open it on your local computer. If you use SSH, obtain this VP's current SSH external port from ANA **Port Mapping**; do not copy a port number from another chamber. Check that the frame shows the parked-car scene and is not blank, stale, or corrupted. The captured frame will not have the same hash as the source photograph because ANA and the JPEG capture re-encode it. Record the captured image dimensions and SHA-256 in the run notes. Use the captured frame as the VLM input on the next pages.

## What you have learned

You have a saved frame and can verify which camera image the model will receive. The next page prepares a model that accepts images.
