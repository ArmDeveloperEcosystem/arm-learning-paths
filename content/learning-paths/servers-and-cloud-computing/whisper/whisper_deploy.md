---
title: Run the Whisper Model
weight: 4

layout: learningpathall
---

## Run Whisper File
After installing the dependencies and enabling the Arm specific flags in the previous step, now lets run the Whisper model and analyze it.

Run the `whisper-application.py` file:

```python
python3 whisper-application.py
```

## Output

You should see output similar to the image below with the log since we enabled verbose, transcript of the audio and the audio transcription time:
![frontend](whisper_output.png)

## Analyze

The output in the above image has the log containing `attr-fpmath:bf16`, which confirms that fast math BF16 kernels are used in the compute process to improve the performance.

It also generated the text transcript of the audio and the `Inference elapsed time`.

By enabling the Arm specific flags as described in the learning path you can see the performance upliftment with the Whisper using Hugging Face Transformers framework on Arm.