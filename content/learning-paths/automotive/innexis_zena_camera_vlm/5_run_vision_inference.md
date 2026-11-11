---
title: Run and record image inference
description: Submit the captured camera frame to a vision model and keep the exact input and response.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Run inference on the captured frame

Run llama.cpp inside the Zena guest on the JPEG captured from `/dev/video0` using the models that you downloaded earlier. This connects the virtual camera input to a local vision-language model (VLM) response.

Copy and run the entire block in the guest shell:

```bash
WORK_DIR=/root/zena-camera-vlm ; FRAME_FILE="$WORK_DIR/frames/file-after-control.jpg" ; MODEL_FILE="$WORK_DIR/models/SmolVLM2-500M-Video-Instruct-Q8_0.gguf" ; MMPROJ_FILE="$WORK_DIR/models/mmproj-SmolVLM2-500M-Video-Instruct-Q8_0.gguf" ; LLAMA_CLI=/root/zena-llamacpp/llama.cpp/build/bin/llama-cli
mkdir -p "$WORK_DIR/results" ; if test -s "$FRAME_FILE" && test -s "$MODEL_FILE" && test -s "$MMPROJ_FILE" && test -x "$LLAMA_CLI"; then
    timeout 180s "$LLAMA_CLI" -m "$MODEL_FILE" --mmproj "$MMPROJ_FILE" --no-mmproj-offload --image "$FRAME_FILE" -ngl 0 -t 4 -tb 4 -c 4096 -n 96 --temp 0 --seed 42 --single-turn --simple-io -p 'Describe what you can see in this image in one short sentence.' > "$WORK_DIR/results/vision-run.log" 2>&1 ; RUN_STATUS=$?
    printf '%s\n' "$RUN_STATUS" > "$WORK_DIR/results/vision-run.exit" ; printf 'Vision run status: %s\n' "$RUN_STATUS" ; tail -n 70 "$WORK_DIR/results/vision-run.log"
else
    printf 'A required camera frame, model, projector, or binary is missing.\n'
fi
```
The commands save the raw log and exit status under `/root/zena-camera-vlm/results/`.

## Check the result

Check the results for the following details:

- `vision-run.exit` contains `0`
- The log names `file-after-control.jpg` after `Loaded media from`
- The response describes the saved JPEG.

When testing the workflow, all three checks passed. 

The model responded:

```output
> Describe what you can see in this image in one short sentence.
 A row of cars are parked in a parking lot, with a building in the background.
```

The response matched the parked-car frame. Your model might use different words. Compare the answer with your saved image instead of expecting this exact sentence.

## Save the evidence and stop the virtual platform

Transfer the files through the authorized route for your chamber. Then, stop the virtual platform and confirm its state in **Lab Manager**. Check the current **Auto Shutdown** setting before any longer run.

This result confirms that a camera frame reached a local VLM in the guest. Note that the result isn't indicative of detection accuracy, continuous video rate, accelerator use, or physical-silicon performance.

## What you've accomplished

You've used a captured a virtual camera frame as input for a local VLM, and used the VLM to perform inference. 

You can extend the Learning Path to analyze other images or [optionally complete steps to analyze a moving scene](/learning-paths/automotive/innexis_zena_llamacpp/5_iterate_and_collect/). 

If you choose to perform optional inference on a moving scene, begin with the virtual platform stopped. With the virtual platform stopped, you can check its camera input before starting it again.


