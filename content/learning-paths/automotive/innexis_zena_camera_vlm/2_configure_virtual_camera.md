---
title: Configure and check the virtual camera
description: Select a repeatable video source in ANA and confirm that the Zena CSS guest can access it.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure and check the virtual camera

Create a three-second H.264 MP4 from a public photograph of parked cars. The source is [Car parking (25737623545).jpg by StockyPics](https://commons.wikimedia.org/wiki/File:Car_parking_(25737623545).jpg), identified as CC0 1.0 on Wikimedia Commons. The short clip gives you a recognizable scene for this single-frame exercise. You will download the source photograph yourself; this Learning Path does not distribute the MP4.

### Download the source and create the camera video

On your local machine, create a media directory:

{{% notice Note %}}
This Learning Path was tested with an Apple Silicon Mac as the local machine. Commands, file paths, and interface details may differ on other operating systems.
{{% /notice %}}

```bash
MEDIA_DIR="$HOME/zena-camera-media" ; mkdir -p "$MEDIA_DIR"
```

Open the [source photograph on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Car_parking_(25737623545).jpg), select **Original file**, and save it in that directory as `parked-cars-original.jpg`. Verify that you received the same source used for this tutorial:

<!-- VERIFY: Repeat the browser download and the reader-formatted hash check on a clean local computer before publication. -->
```bash
MEDIA_DIR="$HOME/zena-camera-media" ; SOURCE_IMAGE="$MEDIA_DIR/parked-cars-original.jpg" ; printf 'b37d713f4fb70409e18e678dac73743b9b64ad358e3023ffce06e5d72b897c3  %s\n' "$SOURCE_IMAGE" | shasum -a 256 -c -
```

On your local machine, crop the photograph and create a three-second camera video. Run the following commands together:

<!-- VERIFY: Run these reader-formatted commands verbatim on the Mac. The same conversion settings reproduced the reported MP4 hash from the saved source image. -->
```bash
MEDIA_DIR="$HOME/zena-camera-media" ; SOURCE_IMAGE="$MEDIA_DIR/parked-cars-original.jpg" ;
PREVIEW_IMAGE="$MEDIA_DIR/parked-cars-preview.jpg" ;
CAMERA_VIDEO="$MEDIA_DIR/automotive-parked-cars-640x480.mp4" ;
ffmpeg -hide_banner -loglevel error -i "$SOURCE_IMAGE" \
    -vf 'scale=640:480:force_original_aspect_ratio=increase,crop=640:480' \
    -frames:v 1 -y "$PREVIEW_IMAGE" &&
ffmpeg -hide_banner -loglevel error -loop 1 -framerate 30 -i "$PREVIEW_IMAGE" \
    -t 3 -vf 'scale=in_range=pc:out_range=tv,format=yuv420p' \
    -c:v libx264 -pix_fmt yuv420p -color_range tv -crf 18 \
    -preset veryfast -an -movflags +faststart -y "$CAMERA_VIDEO" &&
ffprobe -v error -select_streams v:0 \
    -show_entries stream=codec_name,width,height,r_frame_rate \
    -of default=noprint_wrappers=1 "$CAMERA_VIDEO" &&
shasum -a 256 "$CAMERA_VIDEO" ;
printf 'Video preparation status: %s\n' "$?"
```

Check that the command reports H.264 at 640 × 480 and 30 fps. Open the MP4 and confirm that it shows parked cars. Record its SHA-256; a different `ffmpeg` version can produce different bytes.

In ANA Web IDE, open **Explorer** and drag `automotive-parked-cars-640x480.mp4` into the root of your VP folder under **Virtual Platforms**. Confirm that it appears beside `README` and `vsoc.json`. ANA then makes it available as `${project_loc}/automotive-parked-cars-640x480.mp4`.

### Select the ANA camera input

Stop the VP before changing its camera settings. In **Lab Manager → Device Connections → Audio/Video Inputs**, find `vsock-camera-0` under **Camera Inputs**. Select **None**, click **Save**, and start the VP. You will choose the uploaded file from the guest after startup, as documented in the Siemens ANA Zena CSS guide.

![ANA Lab Manager Audio/Video Inputs page showing vsock-camera-0 with None selected#center](ana_camera_inputs_none.png "Find vsock-camera-0 and select None")

The screenshot shows where to select **None**. It was captured while the VP was running, so the controls are greyed out. Perform this step with the VP stopped.

### Start the guest bridge and choose the file

In the **Zena guest shell**, start the virtual camera bridge:

```bash
systemctl start virtualcam-bridge@1.service ; printf 'Bridge start status: %s\n' "$?" ; systemctl is-active virtualcam-bridge@1.service
```

Continue when the command returns status `0` and `active`. The frame capture on the next page checks whether the intended image arrives.

Discover this VP's camera command port. Its value can change after a restart:

<!-- VERIFY: Rerun this reader-formatted command as written. The individual lookup and INPUT query passed in the reported run. -->
```bash
CMD_PORT=$(printf 'vsock-camera-0:cmd\n' | socat -T5 - VSOCK-CONNECT:2:5000) ; LOOKUP_STATUS=$? ; printf 'Command port: <%s>\nLookup status: %s\n' "$CMD_PORT" "$LOOKUP_STATUS" ; if [ "$LOOKUP_STATUS" -eq 0 ] && [ -n "$CMD_PORT" ]; then printf 'INPUT\n' | socat -T5 - "VSOCK-CONNECT:2:$CMD_PORT" ; printf 'Input query status: %s\n' "$?" ; fi
```

In the reported run, the lookup returned port `6001` and initial input `NONE`. Continue only if your lookup succeeds and returns a number. Set the file using that port. Keep `${project_loc}` literal so ANA resolves the VP workspace path:

<!-- VERIFY: Rerun the dynamic-port form as written. The reported run used the discovered port 6001 directly and received OK. -->
```bash
printf '%s\n' 'INPUT=${project_loc}/automotive-parked-cars-640x480.mp4' | socat -T5 - "VSOCK-CONNECT:2:$CMD_PORT" ; printf 'Set input status: %s\n' "$?" ; printf 'INPUT\n' | socat -T5 - "VSOCK-CONNECT:2:$CMD_PORT" ; printf 'Readback status: %s\n' "$?"
```

The set command returned `OK`, and `INPUT` read back the selected file path. The next page checks the actual guest image.

### Inspect stream details if needed

If the next page cannot capture a frame, check the declared format and playback status:

<!-- VERIFY: Rerun the dynamic-port form as written. The reported run queried port 6001 directly. -->
```bash
printf 'Camera capabilities:\n' ; printf 'CAPS\n' | socat -T5 - "VSOCK-CONNECT:2:$CMD_PORT" ; printf 'CAPS status: %s\n' "$?" ; printf 'File playback status:\n' ; printf 'STATUS\n' | socat -T5 - "VSOCK-CONNECT:2:$CMD_PORT" ; printf 'STATUS query status: %s\n' "$?"
```

For the tested VP, `CAPS` returned `video/x-raw,format=I420,width=640,height=480,framerate=30/1`, and `STATUS` initially displayed the video path. These values describe the control interface; a captured frame is the check that image content reached the guest.

If the bridge restarts repeatedly, inspect `journalctl -u virtualcam-bridge@1.service -n 30 --no-pager -o cat`. An empty control response is not proof of success even when `socat` exits `0`. Check the captured frame before treating the camera setup as complete.

## What you have learned

You have selected a repeatable camera input. Next, capture and inspect a frame from `/dev/video0`.
