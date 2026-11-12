---
title: Configure and check the virtual camera
description: Select a repeatable video source in ANA and confirm that the Zena CSS guest can access it.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare a camera input

After preparing directories for input and output, you can prepare camera input.

You'll create a three-second H.264 MP4 clip from a public photograph of parked cars available under CC0 1.0 on Wikimedia Commons. The short clip gives you a recognizable scene for the Learning Path. You'll use the video as input for the virtual camera.

You'll then capture one frame through the guest camera device and pass it to the vision-language model (VLM). Repeating the same photograph makes the expected camera image easy to verify.

### Download the source and create the camera video

{{% notice Note %}}
This Learning Path was tested with an Apple® silicon Mac as the local machine. Commands, file paths, and interface details might differ on other operating systems.

Ensure that your local machine has `ffmpeg`. For example, on Mac, you can install it using the `brew` package manager with the following command:

```sh
brew install ffmpeg
```
{{% /notice %}}

On your local machine, create a media directory:

```bash
MEDIA_DIR="$HOME/zena-camera-media" ; mkdir -p "$MEDIA_DIR"
```

Open the [source photograph on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Car_parking_(25737623545).jpg). Select **Original file** under the download button, and save the file in the media directory as `parked-cars-original.jpg`.

Set `MEDIA_DIR` and `SOURCE_IMAGE` to the directory and filename you used:

```bash
MEDIA_DIR="$HOME/zena-camera-media" ; SOURCE_IMAGE="$MEDIA_DIR/parked-cars-original.jpg"
```

On your local machine, crop the photograph and create a three-second camera video:

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

The output is similar to:

```output
codec_name=h264
width=640
height=480
r_frame_rate=30/1
7a053923146ab81ae6c8bd991cf3620411a3ca664e40196ba2c9d1963bc4767e  /Users/kiehej01/zena-camera-media/automotive-parked-cars-640x480.mp4
Video preparation status: 0
```

Confirm that the command reports `h264` at 640 × 480 and 30 fps. You can open the MP4 and confirm that it shows parked cars.

In the ANA Web IDE, open **Explorer** and drag `automotive-parked-cars-640x480.mp4` into the root of your virtual platform folder under **Virtual Platforms**. Confirm that it appears beside `README` and `vsoc.json`. Architecture Native Acceleration (ANA) then makes it available as `${project_loc}/automotive-parked-cars-640x480.mp4`.

## Select the ANA camera input

In **Lab Manager → Device Connections → Audio/Video Inputs**, find `vsock-camera-0` under **Camera Inputs**. Confirm that **None** is currently selected. The following screenshot was captured while the virtual platform was running, so the controls are greyed out:

![ANA Lab Manager Audio/Video Inputs page showing vsock-camera-0 with None selected#center](ana_camera_inputs_none.png "Find vsock-camera-0 and select None")

If **None** isn't selected, stop the virtual platform. Select **None**, then select **Save** and restart the virtual platform.

{{% notice Note%}}

If you restart the virtual platform, you might need to reestablish SSH tunnelling as described in the [Arm Zena CSS setup Learning Path](/learning-paths/automotive/innexis_ana_zena/).

{{% /notice %}}

## Start the guest bridge and choose the file

In the Zena guest shell, start the virtual camera bridge:

```bash
systemctl start virtualcam-bridge@1.service ; printf 'Bridge start status: %s\n' "$?" ; systemctl is-active virtualcam-bridge@1.service
```

Continue when the command returns status `0` and `active`. The frame capture later checks whether the intended image arrives.

Discover the camera command port of the virtual platform:

```bash
CMD_PORT=$(printf 'vsock-camera-0:cmd\n' | socat -T5 - VSOCK-CONNECT:2:5000) ; LOOKUP_STATUS=$? ; printf 'Command port: <%s>\nLookup status: %s\n' "$CMD_PORT" "$LOOKUP_STATUS" ; if [ "$LOOKUP_STATUS" -eq 0 ] && [ -n "$CMD_PORT" ]; then printf 'INPUT\n' | socat -T5 - "VSOCK-CONNECT:2:$CMD_PORT" ; printf 'Input query status: %s\n' "$?" ; fi
```

The port value can change after a restart.

In the example run, the lookup returned port `6001` and initial input `NONE`. Continue only if your lookup succeeds and returns a number. 

Set the file using that port. Keep `${project_loc}` literal so that ANA resolves the virtual platform workspace path:

```bash
printf '%s\n' 'INPUT=${project_loc}/automotive-parked-cars-640x480.mp4' | socat -T5 - "VSOCK-CONNECT:2:$CMD_PORT" ; printf 'Set input status: %s\n' "$?" ; printf 'INPUT\n' | socat -T5 - "VSOCK-CONNECT:2:$CMD_PORT" ; printf 'Readback status: %s\n' "$?"
```

The set command returns `OK`, and `INPUT` reads back the selected file path. 

## What you've accomplished and what's next

You've prepared and selected a repeatable camera input.

Next, you'll capture and inspect a frame from `/dev/video0`.
