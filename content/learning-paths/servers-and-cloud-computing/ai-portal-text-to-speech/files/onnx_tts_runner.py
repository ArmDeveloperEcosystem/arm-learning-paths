"""Qwen3-TTS-0.6B INT8 ONNX cascade — minimal voice-clone inference example.
Synthesizes speech for a piece of text in the voice of a reference clip, running
entirely on the per-unit ONNX cascade (zero PyTorch in the synthesis compute
path) via onnxruntime. Optimized for Arm (Graviton / KleidiAI), runs on x86 too.
Unlike a single-tensor CV model, Qwen3-TTS deploys as a CASCADE of ONNX units
(talker backbone/decode, sub-talker backbone/decode/heads, codec_decoder,
speaker_encoder, + embeds). This script wires them together with the
`OnnxCascadeDriver` and synthesizes one utterance.
Requirements (beyond this file + the *.onnx units shipped alongside it):
  - onnxruntime, numpy, soundfile, librosa
  - transformers==4.57.3  (Qwen3-TTS processor — used ONLY to tokenize text and
    is harness, not part of the deployed synthesis engine)
  - onnx_cascade_driver.py from the qwen3_tts runner
    (src/model_optimizers/tts/onnx_cascade_driver.py) importable on PYTHONPATH,
    plus text_path_weights.npz / text_path_config.json (shipped in this dir).
Usage:
    python onnx_tts_runner.py --text "Hello, this is a cloned voice." \
        --ref-audio sample_input.wav --out sample_output.wav
"""

from __future__ import annotations

import argparse
import json
import os

import librosa
import numpy as np
import soundfile as sf
from onnx_cascade_driver import (  # from the qwen3_tts runner
    OnnxCascadeDriver,
    resolve_cascade_component_paths,
)
from transformers import AutoProcessor


HERE = os.path.dirname(os.path.abspath(__file__))
MODEL_ID = "Qwen/Qwen3-TTS-12Hz-0.6B-Base"
SPEAKER_SR = 24000  # speaker_encoder_sample_rate (text_path_config.json)

# v4 accepted precision recipe: FP16 talker, FP32 speaker_encoder /
# sub_talker_backbone, INT8 sub_talker_decode / sub_talker_heads / codec_decoder.
FP16_UNITS = frozenset({"talker_backbone", "talker_decode"})
FP32_UNITS = frozenset({"speaker_encoder", "sub_talker_backbone"})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", default="Hello, this is a cloned voice.")
    parser.add_argument("--ref-audio", default=os.path.join(HERE, "sample_input.wav"))
    parser.add_argument("--out", default=os.path.join(HERE, "sample_output.wav"))
    parser.add_argument("--units-dir", default=HERE, help="dir with the *.onnx units")
    parser.add_argument("--intra-op-threads", type=int, default=os.cpu_count())
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    # 1. Tokenize text (harness; the processor is not part of the ONNX engine).
    #    Qwen3-TTS has no chat_template; it uses a fixed assistant-prompt wrapper
    #    (mirrors qwen_tts ``Qwen3TTSModel._build_assistant_text``).
    processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)
    text = (
        f"<|im_start|>assistant\n{args.text}<|im_end|>\n<|im_start|>assistant\n"
    )
    tokens = processor(text=text, return_tensors="pt", padding=True)
    input_ids = tokens["input_ids"].cpu().numpy().astype(np.int64)
    if input_ids.ndim == 1:
        input_ids = input_ids[None, :]

    # 2. Load reference audio (resampled to the speaker-encoder rate).
    ref, _ = librosa.load(args.ref_audio, sr=SPEAKER_SR, mono=True)
    ref = ref.astype(np.float32)

    # 3. Resolve the optimized cascade units and build the ONNX-only driver.
    with open(os.path.join(args.units_dir, "text_path_config.json")) as fh:
        num_layers = json.load(fh)["num_hidden_layers"]
    paths = resolve_cascade_component_paths(
        args.units_dir, fp16_units=FP16_UNITS, fp32_units=FP32_UNITS
    )
    driver = OnnxCascadeDriver.from_component_paths(
        paths,
        text_weights_npz=os.path.join(args.units_dir, "text_path_weights.npz"),
        text_weights_config=os.path.join(args.units_dir, "text_path_config.json"),
        num_talker_layers=num_layers,
        intra_op_num_threads=args.intra_op_threads,
        graph_optimization_level="all",
    )

    # 4. Synthesize (greedy talker decode = deterministic, matches eval).
    wav = driver.generate(input_ids, ref, SPEAKER_SR, do_sample=False, seed=args.seed)
    wav = np.asarray(wav, dtype=np.float32)

    # 5. Save the 24 kHz waveform + a small JSON summary.
    sf.write(args.out, wav, SPEAKER_SR)
    summary = {
        "text": args.text,
        "ref_audio": os.path.basename(args.ref_audio),
        "output_audio": os.path.basename(args.out),
        "sample_rate": SPEAKER_SR,
        "duration_s": round(len(wav) / SPEAKER_SR, 3),
        "decode_steps": int(getattr(driver, "last_decode_steps", -1)),
    }
    with open(os.path.join(HERE, "prediction.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
