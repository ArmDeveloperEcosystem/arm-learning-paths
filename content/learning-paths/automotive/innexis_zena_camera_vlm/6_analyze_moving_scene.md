---
title: (Optional) Analyze a moving automotive scene with a larger VLM
description: Capture changing frames from the Zena CSS virtual camera and compare local scene descriptions from two vision models.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare camera frames that show motion

You validated one camera frame and one local vision-model response. You can extend the workflow by using a clip with vehicle movement. You'll check that changing images reach the Zena CSS guest. Then, you'll run the existing 500M model and a 2.2B model on the same selected frame. 

The source is [Video Codec Test rush hour 1080p25.y4m.webm](https://commons.wikimedia.org/wiki/File:Video_Codec_Test_rush_hour_1080p25.y4m.webm) by Taurus Media Technik. Wikimedia Commons describes it as a fixed-camera view of moving traffic in Munich and marks it CC0 1.0, with a recorded license review. 

### Download and convert the moving video

On your local machine, download the original WebM video from Wikimedia Commons and verify its SHA-256:

```bash
MEDIA_DIR="$HOME/zena-camera-media" ; SOURCE_VIDEO="$MEDIA_DIR/rush-hour-source.webm" ; mkdir -p "$MEDIA_DIR" ; curl -fL --retry 2 --retry-delay 3 -o "$SOURCE_VIDEO.part" 'https://upload.wikimedia.org/wikipedia/commons/a/a3/Video_Codec_Test_rush_hour_1080p25.y4m.webm' && printf 'bb587147edb58630b0025b1e86cc2bdfe85fc7caf1f2c8f179e4226749963e76  %s\n' "$SOURCE_VIDEO.part" | shasum -a 256 -c - && mv "$SOURCE_VIDEO.part" "$SOURCE_VIDEO" ; printf 'Source download status: %s\n' "$?"
```

The file is saved as `rush-hour-source.webm` in `$HOME/zena-camera-media`.

If Wikimedia Commons rate-limits the command, open the [source file page](https://commons.wikimedia.org/wiki/File:Video_Codec_Test_rush_hour_1080p25.y4m.webm). Select **Original file**, and save it as `rush-hour-source.webm` in the same local directory. 

Check the hash of the file before continuing:

```bash
MEDIA_DIR="$HOME/zena-camera-media" ; SOURCE_VIDEO="$MEDIA_DIR/rush-hour-source.webm" ; printf 'bb587147edb58630b0025b1e86cc2bdfe85fc7caf1f2c8f179e4226749963e76  %s\n' "$SOURCE_VIDEO" | shasum -a 256 -c -
```

Convert the WebM to the format that's used for virtual camera input.

```bash
MEDIA_DIR="$HOME/zena-camera-media" ; SOURCE_VIDEO="$MEDIA_DIR/rush-hour-source.webm" ; CAMERA_VIDEO="$MEDIA_DIR/automotive-moving-traffic-640x480.mp4" ; ffmpeg -hide_banner -loglevel error -i "$SOURCE_VIDEO" -vf 'fps=30,scale=640:360,pad=640:480:0:60:color=black,format=yuv420p' -c:v libx264 -crf 21 -preset veryfast -an -movflags +faststart -y "$CAMERA_VIDEO" && ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate -of default=noprint_wrappers=1 "$CAMERA_VIDEO" && shasum -a 256 "$CAMERA_VIDEO" ; printf 'Conversion status: %s\n' "$?"
```

The output is similar to:  

```output
codec_name=h264
width=640
height=480
r_frame_rate=30/1
9d9098519fb4de998cd74c8fcfae4755e849d33954f43ef79822fa3e8eb57482  /Users/kiehej01/zena-camera-media/automotive-moving-traffic-640x480.mp4
Conversion status: 0
```
The hash might differ depending on the `ffmpeg` version that you used.

### Send the moving clip through ANA

Reuse the camera path that you configured earlier. Upload the verified MP4 to the root of your Architecture Native Acceleration (ANA) virtual platform workspace.

In **Lab Manager → Device Connections → Audio/Video Inputs**, check that `vsock-camera-0` is set to **None**. If not, stop the virtual platform, modify the settings, and start the virtual platform. 

Start `virtualcam-bridge@1.service` in the guest:

```bash
systemctl start virtualcam-bridge@1.service ; printf 'Bridge start status: %s\n' "$?" ; systemctl is-active virtualcam-bridge@1.service ; CMD_PORT=$(printf 'vsock-camera-0:cmd\n' | socat -T5 - VSOCK-CONNECT:2:5000) ; LOOKUP_STATUS=$? ; printf 'Command port: <%s>\nLookup status: %s\n' "$CMD_PORT" "$LOOKUP_STATUS"
```

The output is similar to: 

```output
Bridge start status: 0
active
Command port: <6001>
Lookup status: 0
```
Ensure that the output indicates `active`. The command port might differ.

Run the following command:

```bash
if [ -n "$CMD_PORT" ]; then INPUT_REPLY=$(printf '%s\n' 'INPUT=${project_loc}/automotive-moving-traffic-640x480.mp4' | socat -T5 - "VSOCK-CONNECT:2:$CMD_PORT") ; SET_STATUS=$? ; printf 'Set input response: <%s>\nSet input status: %s\n' "$INPUT_REPLY" "$SET_STATUS" ; printf 'INPUT\n' | socat -T5 - "VSOCK-CONNECT:2:$CMD_PORT" ; printf 'Readback status: %s\n' "$?" ; printf 'CAPS\n' | socat -T5 - "VSOCK-CONNECT:2:$CMD_PORT" ; printf 'CAPS status: %s\n' "$?" ; else printf 'No camera command port was discovered.\n' ; fi
```

The output is similar to:

```ouptput
Set input response: <OK>
Set input status: 0
${project_loc}/automotive-moving-traffic-640x480.mp4
Readback status: 0
video/x-raw,format=I420,width=640,height=480,framerate=30/1
CAPS status: 0
```

### Capture frames that show motion

Capture frames from `/dev/video0` at several recorded points while the clip plays. The following guest command saves three JPEGs approximately six seconds apart. It records capture time, exit status, file size, and SHA-256 for each image:

```bash
WORK_DIR=/root/zena-camera-vlm ; mkdir -p "$WORK_DIR/frames" "$WORK_DIR/results" ; for n in 1 2 3; do FRAME_FILE="$WORK_DIR/frames/moving-traffic-$n.jpg" ; rm -f "$FRAME_FILE" ; printf 'Frame %s capture time: ' "$n" ; date -u '+%Y-%m-%d %H:%M:%S UTC' ; timeout 15s gst-launch-1.0 -e v4l2src device=/dev/video0 num-buffers=1 ! videoconvert ! jpegenc ! filesink location="$FRAME_FILE" > "$WORK_DIR/results/moving-capture-$n.log" 2>&1 ; CAPTURE_STATUS=$? ; printf 'Frame %s capture status: %s\n' "$n" "$CAPTURE_STATUS" ; if [ "$CAPTURE_STATUS" -ne 0 ] || [ ! -s "$FRAME_FILE" ]; then tail -n 20 "$WORK_DIR/results/moving-capture-$n.log" ; break ; fi ; ls -lh "$FRAME_FILE" ; sha256sum "$FRAME_FILE" ; if [ "$n" -lt 3 ]; then sleep 6 ; fi ; done
```

In the example `test3` run, captures at 10:47:07, 10:47:14 and 10:47:20 UTC all returned `0` and created nonempty 640 × 480 JPEGs. 

Transfer the three images through your authorized chamber route and inspect them side by side. Ensure that the transferred hashes match the guest output. Confirm that visual inspection shows vehicles in changing positions against the fixed road view. Different SHA-256 values alone don't establish motion.

![Three Zena guest camera frames showing road traffic at successive capture times; foreground vehicles change position while the right-side red car remains a reference#center](ana_moving_traffic_frames.jpg "Guest frames captured about six seconds apart from the CC0 rush-hour source by Taurus Media Technik")

## Prepare and run the larger model

Compare the 500M and 2.2B models on the same captured JPEG. Use the same prompt and inference settings for both runs, then save each response, log, exit status, and elapsed time. This checks what the two models report for the same frame.

### Check the frame and rerun the 500M model

Select a captured frame that shows the moving traffic scene. The example run used `moving-traffic-2.jpg`, which passed its SHA-256 check. Run the 500M model from on this frame:

```bash
WORK_DIR=/root/zena-camera-vlm ; FRAME_FILE="$WORK_DIR/frames/moving-traffic-2.jpg" ; MODEL_FILE="$WORK_DIR/models/SmolVLM2-500M-Video-Instruct-Q8_0.gguf" ; MMPROJ_FILE="$WORK_DIR/models/mmproj-SmolVLM2-500M-Video-Instruct-Q8_0.gguf" ; LLAMA_CLI=/root/zena-llamacpp/llama.cpp/build/bin/llama-cli ; mkdir -p "$WORK_DIR/results" ; START_TIME=$(date +%s) ; timeout 180s "$LLAMA_CLI" -m "$MODEL_FILE" --mmproj "$MMPROJ_FILE" --no-mmproj-offload --image "$FRAME_FILE" -ngl 0 -t 4 -tb 4 -c 4096 -n 96 --temp 0 --seed 42 --single-turn --simple-io -p 'Describe what you can see in this image in one short sentence.' > "$WORK_DIR/results/moving-500m.log" 2>&1 ; RUN_STATUS=$? ; END_TIME=$(date +%s) ; printf '%s\n' "$RUN_STATUS" > "$WORK_DIR/results/moving-500m.exit" ; printf '500M run status: %s\nElapsed wall seconds: %s\n' "$RUN_STATUS" "$((END_TIME - START_TIME))" ; tail -n 40 "$WORK_DIR/results/moving-500m.log"
```

The reported 500M run exited `0` after nine seconds and described a traffic jam with cars and trucks. The model received one JPEG. Its use of “in motion” doesn't establish video understanding.

### Download and verify the 2.2B model

Check the free disk space of the guest, available memory, and remaining virtual platform run time before downloading. In the example Zena run, the guest had 23 GB free on `/`, `MemAvailable: 7836192 kB`, and an executable `llama-cli` from commit `b86d2f075`. Your values might differ.

Use the pinned [SmolVLM2-2.2B-Instruct-GGUF revision](https://huggingface.co/ggml-org/SmolVLM2-2.2B-Instruct-GGUF/tree/1bc3c9f74ceafd4c8d4411cc9cf188bba3798f91) to download the following files:

- [Q4_K_M model](https://huggingface.co/ggml-org/SmolVLM2-2.2B-Instruct-GGUF/blob/1bc3c9f74ceafd4c8d4411cc9cf188bba3798f91/SmolVLM2-2.2B-Instruct-Q4_K_M.gguf)
- [Q8_0 multimodal projector](https://huggingface.co/ggml-org/SmolVLM2-2.2B-Instruct-GGUF/blob/1bc3c9f74ceafd4c8d4411cc9cf188bba3798f91/mmproj-SmolVLM2-2.2B-Instruct-Q8_0.gguf)

Together, the files are about 1.7 GB. 

Each download command checks its SHA-256 before moving the file to its final path:

```bash
WORK_DIR=/root/zena-camera-vlm ; MODEL_REV=1bc3c9f74ceafd4c8d4411cc9cf188bba3798f91 ; MODEL_FILE="$WORK_DIR/models/SmolVLM2-2.2B-Instruct-Q4_K_M.gguf" ; wget -nv -c -O "$MODEL_FILE.part" "https://huggingface.co/ggml-org/SmolVLM2-2.2B-Instruct-GGUF/resolve/$MODEL_REV/SmolVLM2-2.2B-Instruct-Q4_K_M.gguf" && printf '0cf76814555b8665149075b74ab6b5c1d428ea1d3d01c1918c12012e8d7c9f58  %s\n' "$MODEL_FILE.part" | sha256sum -c - && mv "$MODEL_FILE.part" "$MODEL_FILE" && ls -lh "$MODEL_FILE" ; printf 'Model download status: %s\n' "$?"
```

In the example guest run, the downloaded `Q4_K_M` file passed SHA-256, and the final status was `0`. `ls -lh` showed 1.1G.

```bash
WORK_DIR=/root/zena-camera-vlm ; MODEL_REV=1bc3c9f74ceafd4c8d4411cc9cf188bba3798f91 ; MMPROJ_FILE="$WORK_DIR/models/mmproj-SmolVLM2-2.2B-Instruct-Q8_0.gguf" ; wget -nv -c -O "$MMPROJ_FILE.part" "https://huggingface.co/ggml-org/SmolVLM2-2.2B-Instruct-GGUF/resolve/$MODEL_REV/mmproj-SmolVLM2-2.2B-Instruct-Q8_0.gguf" && printf 'ae07ea1facd07dd3230c4483b63e8cda96c6944ad2481f33d531f79e892dd024  %s\n' "$MMPROJ_FILE.part" | sha256sum -c - && mv "$MMPROJ_FILE.part" "$MMPROJ_FILE" && ls -lh "$MMPROJ_FILE" ; printf 'Projector download status: %s\n' "$?"
```

In the example guest run, both files passed their SHA-256 checks with status `0`. The model was 1.1G and the projector was 566M. Save the hash results with the inference log.

### Run the 2.2B model on the same frame

Use the JPEG and prompt from the 500M run. The inference settings are the same. The larger model has a longer timeout to allow it to finish:

```bash
WORK_DIR=/root/zena-camera-vlm ; FRAME_FILE="$WORK_DIR/frames/moving-traffic-2.jpg" ; MODEL_FILE="$WORK_DIR/models/SmolVLM2-2.2B-Instruct-Q4_K_M.gguf" ; MMPROJ_FILE="$WORK_DIR/models/mmproj-SmolVLM2-2.2B-Instruct-Q8_0.gguf" ; LLAMA_CLI=/root/zena-llamacpp/llama.cpp/build/bin/llama-cli ; START_TIME=$(date +%s) ; timeout 300s "$LLAMA_CLI" -m "$MODEL_FILE" --mmproj "$MMPROJ_FILE" --no-mmproj-offload --image "$FRAME_FILE" -ngl 0 -t 4 -tb 4 -c 4096 -n 96 --temp 0 --seed 42 --single-turn --simple-io -p 'Describe what you can see in this image in one short sentence.' > "$WORK_DIR/results/moving-2b.log" 2>&1 ; RUN_STATUS=$? ; END_TIME=$(date +%s) ; printf '%s\n' "$RUN_STATUS" > "$WORK_DIR/results/moving-2b.exit" ; printf '2.2B run status: %s\nElapsed wall seconds: %s\n' "$RUN_STATUS" "$((END_TIME - START_TIME))" ; tail -n 45 "$WORK_DIR/results/moving-2b.log"
```

## Compare the model responses

Confirm that both runs completed with exit status `0`, then compare their descriptions of the same captured frame.

The 500M model described traffic, cars and trucks. The 2.2B model reported: “A traffic jam on a busy city street with cars and a fountain in the background.”

Inspect the captured image and check which details support each description. Note any objects that the models omitted or described incorrectly. 

{{% notice Note %}}
The results validate functional inference on the virtual platform. They don't establish model accuracy, measure physical-silicon performance, or demonstrate continuous video inference.
{{% /notice %}}

## What you've accomplished

You've used a recorded moving scene to check that the virtual camera supplies changing images. You've also inspected how two local vision models describe the same captured input.
