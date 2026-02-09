---
title: Fine-tune segmentation parameters
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

After applying the previous steps—model upgrade, VAD, smart turn detection, and multi-threaded audio collection—you now have a high-quality, CPU-based local speech-to-text system.

At this stage, the core pipeline is complete. What remains is fine-tuning: adapting the system to your environment, microphone setup, and speaking style. This flexibility is one of the key advantages of a fully local STT pipeline.

By adjusting a small set of parameters, you can significantly improve transcription stability and user experience.

No two environments are the same. A quiet office, a noisy lab, and a home setup with background music all require different segmentation behavior. Similarly, users speak at different speeds and with different pause patterns.

Fine-tuning allows you to:
- Avoid cutting long sentences too early
- Reduce false triggers from background noise
- Balance responsiveness and transcription accuracy

## Tunable parameters

The following parameters control how speech is segmented and when transcription is triggered:

### faster-whisper model selection

Model choice directly impacts accuracy and performance:
- small.en: Fast, suitable for lightweight or low-latency use
- medium.en: Higher accuracy, recommended for most CPU-based deployments
- Larger models: Better accuracy but may not be practical on CPU

Choosing the right model ensures an optimal balance between speed and transcription quality.

### VAD mode

webrtcvad provides multiple aggressiveness levels (0-3):
- Lower modes (0-1): More permissive, better for quiet environments
- Higher modes (2-3): More aggressive filtering, better for noisy environments

Adjust this setting based on background noise and microphone quality.

### Tuning `MIN_SPEECH_SEC` and `SILENCE_LIMIT_SEC`

- `MIN_SPEECH_SEC`: This parameter defines the minimum duration of detected speech required before a segment is considered valid. Use this to filter out very short utterances such as false starts or background chatter.
	- Lower values: More responsive, but may capture incomplete phrases or noise
	- Higher values: More stable sentences, but slower response

- `SILENCE_LIMIT_SEC`: This parameter defines how long the system waits after speech stops before finalizing a segment.
	- Lower values: Faster turn completion, but higher risk of sentence truncation
	- Higher values: Better sentence continuity, but increased latency

## Recommended presets

Based on practical experiments, the following presets provide a good starting point:

| Usage Scenario | `MIN_SPEECH_SEC` | `SILENCE_LIMIT_SEC` | Description |
|----------------------|----------------------|-------------------------|-------------------|
| Short command phrases | 0.8 | 0.6 | Optimized for quick voice commands such as "yes", "next", or "stop". Prioritizes responsiveness over sentence completeness. |
| Natural conversational speech | 1.0 | 1.0 | Balanced settings for everyday dialogue with natural pauses between phrases. |
| Long-form explanations (for example, tutorials) | 2.0 | 2.0 | Designed for longer sentences and structured explanations, reducing the risk of premature segmentation. |

## Apply these settings

To modify these parameters in your `transcribe.py` file, adjust the values at the top of the script:

```python
# --- Parameters ---
SAMPLE_RATE = 16000
FRAME_DURATION_MS = 30
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION_MS / 1000)
VAD_MODE = 3                    # Adjust: 0-3 (higher = more aggressive)
SILENCE_LIMIT_SEC = 1.0         # Adjust based on use case
MIN_SPEECH_SEC = 2.0            # Adjust based on use case
```

For conversational use, start with `SILENCE_LIMIT_SEC = 1.0` and `MIN_SPEECH_SEC = 1.0`. If you experience premature sentence breaks, increase both values. If the system feels sluggish, decrease them.

You can also experiment with different faster-whisper models by changing:

```python
model = WhisperModel("medium.en", device=device, compute_type=compute_type)
```

Replace `"medium.en"` with `"small.en"` for faster performance or `"large-v2"` for higher accuracy.

## What you've accomplished and what's next

You now understand how to fine-tune your STT system for different environments and use cases. These adjustments allow you to optimize the balance between responsiveness and transcription quality based on your specific needs.

In the next section, you'll integrate this STT system with vLLM to add natural language understanding and response generation, completing your offline voice assistant.
