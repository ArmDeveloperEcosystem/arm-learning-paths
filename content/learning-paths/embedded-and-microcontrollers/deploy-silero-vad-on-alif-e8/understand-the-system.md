---
title: Understand streaming Silero VAD on the Alif E8
description: Trace audio frames, recurrent state, and speech probabilities through the E8 CPU and NPU.
weight: 2
layout: learningpathall
---

{{% notice Important %}}
This Learning Path is a local draft. Host export and the E8 firmware cross-build have passed with the pinned dependencies. Physical E8 execution has not been validated. Complete programming and the probability comparison before treating this port as a working board deployment.
{{% /notice %}}

## Detect speech in a recorded audio stream

You'll export Silero voice activity detection (VAD), build a Zephyr application for the Alif Ensemble E8 Development Kit, and compare its speech probabilities with a host reference. VAD estimates whether each audio window contains speech. It does not transcribe speech or identify the speaker.

The application targets the board's Cortex-M55 High-Performance (HP) core and Ethos-U85-256 NPU. It embeds a recorded WAV clip and the exported ExecuTorch program in the firmware. It processes the recording sequentially, using the same state and framing rules that a streaming source would require. Microphone capture is outside this application.

## Follow one audio frame

The source recording must be uncompressed, mono, 16-bit PCM WAV at 16 kHz. The preparation step converts its signed samples to floating-point values by dividing by 32,768. Each model invocation receives **512 new samples plus 64 samples of history**, giving one `[1, 576]` floating-point input tensor.

The runtime follows this sequence:

1. **Build the input window.** Copy the previous 64 samples into the start of the input, then append up to 512 new samples. The first window starts with zero history. Pad the final window with zeros if fewer than 512 new samples remain.
2. **Execute the method.** Reuse the loaded ExecuTorch method for the entire recording. Delegated `EthosUBackend` subgraphs execute on the NPU. CPU operators handle work between delegates, including quantization, tensor copies, and recurrent-state updates.
3. **Retain streaming state.** The exported model stores its hidden and cell state in a persistent int8 buffer. Export initializes that buffer to its quantized representation of zero. Each invocation reads the previous state and writes the next state. Keep it across calls; resetting it for every window changes the model's behavior.
4. **Read the probability.** Each call returns one floating-point speech probability. The application labels a frame `speech` when its probability is strictly greater than `0.5`; otherwise it labels it `silence`. Consecutive speech frames form a reported segment.

The two forms of history have different owners:

| Information retained between calls | Owner | Initialization |
| --- | --- | --- |
| Previous 64 waveform samples | Application input-framing code | Floating-point zeros before the first window |
| Quantized hidden and cell state | Exported model's mutable int8 buffer | Serialized initial values when the method is loaded |

Reloading the method or clearing either history between windows breaks the streaming contract. For a new, independent recording, start with a fresh application run so both histories return to their initial values.

## Set the validation workload

The supplied validation clip contains 40,000 samples: **2.5 seconds at 16 kHz**. The runtime makes `ceil(40000 / 512) = 79` calls. The last call contains 64 new samples and 448 padding samples, in addition to the 64-sample history.

Each call advances by 512 samples, or 32 ms of audio. Log timestamps describe positions in the recording; they do not measure how long the board takes to execute inference. With padding, the final frame boundary is 2.528 seconds even though the original clip lasts 2.5 seconds.

The host export produces `expected_probs.bin` from the quantized graph using the same clip, framing, and initial state. The board's probabilities should agree with that reference within the validation tolerances. This checks deployment behavior. It does not establish speech-detection accuracy on unseen recordings, because the example's calibration and validation audio overlap.

## Keep CPU execution and NPU execution together

This model intentionally retains CPU operators around delegated subgraphs. Build the portable and quantized operators selected from the PTE as well as the Ethos-U backend. Requiring the entire program to be one NPU partition would reject the state updates needed by this application.

The separate Corstone-320 example provides the exporter and streaming logic used by this port. Its simulator results do not establish E8 execution time, memory fit, or completed NPU execution on the physical board. Validate those on the E8 using the firmware and model built in this Learning Path.

## What you've learned and what's next

You now know why each invocation accepts 576 samples, how waveform history differs from recurrent state, and why CPU operators remain in an NPU application. You can also distinguish the 32 ms audio-window step from inference latency.

Next, prepare the matching source and E8 tools, then export the model and host reference before building the Zephyr application.
