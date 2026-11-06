---
title: Run and record image inference
description: Submit the captured camera frame to a vision model and keep the exact input and response.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run and record image inference

Run llama.cpp **inside the Zena guest** on the JPEG captured from `/dev/video0`. Use the model and projector verified on page 4. This connects the ANA camera input to a local vision-model response.

### Run inference on the captured frame

Copy the entire block into the guest shell. It saves the raw log and exit status under `/root/zena-camera-vlm/results/`.

<!-- VERIFY: Rerun this reader-formatted command exactly as written before publication. Its arguments and output files match the successful reported run. -->

```bash
WORK_DIR=/root/zena-camera-vlm ; FRAME_FILE="$WORK_DIR/frames/file-after-control.jpg" ; MODEL_FILE="$WORK_DIR/models/SmolVLM2-500M-Video-Instruct-Q8_0.gguf" ; MMPROJ_FILE="$WORK_DIR/models/mmproj-SmolVLM2-500M-Video-Instruct-Q8_0.gguf" ; LLAMA_CLI=/root/zena-llamacpp/llama.cpp/build/bin/llama-cli
mkdir -p "$WORK_DIR/results" ; if test -s "$FRAME_FILE" && test -s "$MODEL_FILE" && test -s "$MMPROJ_FILE" && test -x "$LLAMA_CLI"; then
    timeout 180s "$LLAMA_CLI" -m "$MODEL_FILE" --mmproj "$MMPROJ_FILE" --no-mmproj-offload --image "$FRAME_FILE" -ngl 0 -t 4 -tb 4 -c 4096 -n 96 --temp 0 --seed 42 --single-turn --simple-io -p 'Describe what you can see in this image in one short sentence.' > "$WORK_DIR/results/vision-run.log" 2>&1 ; RUN_STATUS=$?
    printf '%s\n' "$RUN_STATUS" > "$WORK_DIR/results/vision-run.exit" ; printf 'Vision run status: %s\n' "$RUN_STATUS" ; tail -n 70 "$WORK_DIR/results/vision-run.log"
else
    printf 'A required camera frame, model, projector, or binary is missing.\n'
fi
```

### Check the result

Check that `vision-run.exit` contains `0`, the log names `file-after-control.jpg` after `Loaded media from`, and the response describes the saved JPEG. In the reported run, all three checks passed. The model responded:

```output
> Describe what you can see in this image in one short sentence.
 A row of cars are parked in a parking lot, with a building in the background.
```

The reported response matches the parked-car frame. Your model might use different words; compare the answer with your saved image instead of expecting this exact sentence.

### Save the evidence and stop the VP

Keep the captured JPEG, `vision-run.log`, `vision-run.exit`, and their file hashes together. Record any mismatch between the image and answer without changing the raw log.

Transfer the files through your chamber's authorized route. Then stop the VP and confirm its state in Lab Manager. If you continue to the optional moving-scene exercise, begin with the VP stopped so you can check its camera input before starting it again. Check the current Auto Shutdown setting before any longer run.

This result confirms a camera frame reached a local VLM in the guest. It does not measure detection accuracy, continuous video rate, accelerator use, or physical-silicon performance.

## What you have learned

You have captured a virtual camera frame, run an image prompt in the guest, and saved the image and response for review.
