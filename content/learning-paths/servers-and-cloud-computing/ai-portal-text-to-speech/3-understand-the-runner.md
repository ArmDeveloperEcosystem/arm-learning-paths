---
title: Understand the web application and server runner
description: Review how the web application prepares browser input, runs the Qwen3-TTS cascade, and returns WAV audio.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand how the web application works

The `tts_web.py` script is the default entry point. The script adds a FastAPI web interface to `onnx_tts_runner.py` and receives text and reference audio from the browser. It prepares the recording, invokes the runner, and returns the generated WAV file.

The class is named `Qwen3OnnxAdapter` in the code, but it's a wrapper for this specific package rather than a general ONNX text-to-speech loader.

### How the script validates the required files

Before starting the service, `validate()` checks for the runner and its supporting text-path files. 

`validate()` also confirms that FFmpeg is available and that the thread count is valid:

```python
    def validate(self) -> None:
        required = [
            self.runner_path,
            self.model_dir / "onnx_cascade_driver.py",
            self.model_dir / "text_path_config.json",
            self.model_dir / "text_path_weights.npz",
        ]
        missing = [path.name for path in required if not path.is_file()]
        if missing:
            raise FileNotFoundError(
                "The model directory is missing: " + ", ".join(missing)
            )
        if self.ffmpeg is None:
            raise FileNotFoundError(
                "ffmpeg was not found. Install it with: sudo apt install ffmpeg"
            )
        if self.threads < 1:
            raise ValueError("--threads must be at least 1")
```

### How the script prepares the reference recording

Browser recordings and uploaded files can use different audio formats. `normalize_reference()` uses FFmpeg to convert the input to the 24 kHz mono WAV format expected by the runner:

```python
    def normalize_reference(self, source: Path, destination: Path) -> None:
        result = subprocess.run(
            [
                self.ffmpeg,
                "-nostdin",
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-i",
                str(source),
                "-ac",
                "1",
                "-ar",
                "24000",
                str(destination),
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            detail = (result.stderr or result.stdout or "Unsupported audio file").strip()
            raise ValueError("Reference-audio conversion failed: " + detail[-1200:])
```

The `-ac 1` option selects one audio channel, and `-ar 24000` sets the sample rate to 24 kHz.

### How the script invokes the terminal runner

The `synthesize()` method launches `onnx_tts_runner.py` with the same text, reference-audio, output, and thread arguments that are used in the terminal workflow:

```python
    def synthesize(self, text: str, reference_wav: Path, output_wav: Path) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(self.runner_path),
                "--text",
                text,
                "--ref-audio",
                str(reference_wav),
                "--out",
                str(output_wav),
                "--intra-op-threads",
                str(self.threads),
            ],
            cwd=self.model_dir,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            detail = (result.stderr or result.stdout or "Unknown runner error").strip()
            raise RuntimeError("Speech generation failed: " + detail[-3000:])
        if not output_wav.is_file():
            raise RuntimeError("The runner completed without creating the output WAV file.")
```

At startup, the script creates and validates the wrapper before passing it to the FastAPI application:

```python
    adapter = Qwen3OnnxAdapter(args.model_dir, args.threads)
    adapter.validate()
    uvicorn.run(create_app(adapter), host=args.host, port=args.port)
```

The `POST /generate` route validates the request and saves the uploaded recording temporarily. The route prepares the recording, runs synthesis, and returns the output as a WAV file. A lock prevents two model runs from executing at the same time.

## Understand how the terminal runner works

The `onnx_tts_runner.py` script is the terminal entry point for the server package. The script tokenizes the entered text and loads the reference recording at 24 kHz. It resolves the ten ONNX units and constructs `OnnxCascadeDriver` with the shared text-path weights.

The driver generates a waveform, and the script writes it as a 24 kHz WAV file:

```python
    wav = driver.generate(input_ids, ref, SPEAKER_SR, do_sample=False, seed=args.seed)
    wav = np.asarray(wav, dtype=np.float32)

    # 5. Save the 24 kHz waveform + a small JSON summary.
    sf.write(args.out, wav, SPEAKER_SR)
```

The script also writes `prediction.json` with the following:

- Input text 
- Reference filename
- Output filename
- Duration
- Sample rate
- Decode-step count

## What you've learned 

You now understand how the FastAPI application accepts browser input, normalizes the reference recording, and invokes the terminal runner. You've also learned how the application executes the ONNX cascade and returns generated speech as a WAV file.

You can extend the application and the runner to your own use cases.
