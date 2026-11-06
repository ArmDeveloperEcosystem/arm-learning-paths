---
title: Export the streaming VAD model
description: Quantize Silero VAD for Ethos-U85 and generate the recorded-audio reference used to check the E8 output.
weight: 4
layout: learningpathall
---

## Download the model and calibration audio

Use the model and recording from one pinned Silero VAD revision. Keep the upstream project's license with any redistributed model or audio. The application archive contains neither file.

Download both inputs into your output directory:

```bash
cd "$EXECUTORCH_ROOT"
curl --fail --location \
  --output "$SILERO_OUTPUT/silero_vad.jit" \
  https://raw.githubusercontent.com/snakers4/silero-vad/dbacf536adadf42210f37ae50fbaf75f6235b3cf/src/silero_vad/data/silero_vad.jit
curl --fail --location \
  --output "$SILERO_OUTPUT/test.wav" \
  https://raw.githubusercontent.com/snakers4/silero-vad/dbacf536adadf42210f37ae50fbaf75f6235b3cf/tests/data/test.wav
shasum -a 256 "$SILERO_OUTPUT/silero_vad.jit" "$SILERO_OUTPUT/test.wav"
```

The expected hashes are:

| File | SHA256 |
| --- | --- |
| `silero_vad.jit` | `e1122837f4154c511485fe0b9c64455f7b929c96fbb8d79fbdb336383ebd3720` |
| `test.wav` | `89f17d9c94c4b31eb320f424628bcbc920abaddbee6e2760fd868bfb1d9a2e47` |

Trim the first 2.5 seconds for a short firmware validation workload:

```bash
python examples/arm/silero_vad_example_ethos_u/model_export/generate_smoke_audio.py \
  --source-wav "$SILERO_OUTPUT/test.wav" \
  --output "$SILERO_OUTPUT/validation.wav"
```

This produces 40,000 samples. The file remains mono 16-bit PCM at 16 kHz. Using a real speech recording exercises speech and silence probabilities; the helper's optional synthetic tone is a different workload.

## Export the quantized program and reference

The exporter calibrates int8 activations and weights, estimates the hidden/cell state quantization parameters, and serializes initialized recurrent state. It lowers supported computation to Ethos-U85-256 while retaining CPU operators needed for state updates and tensor conversion.

Use `test.wav` as the calibration source and the trimmed clip for validation. The exporter caps calibration at 256 windows by default and processes all 79 validation windows. Enable pipeline failure propagation so an export error remains visible even when saving the log:

```bash
set -o pipefail
python examples/arm/silero_vad_example_ethos_u/model_export/export_silero_vad_ethos_u.py \
  --jit-model "$SILERO_OUTPUT/silero_vad.jit" \
  --calibration-audio "$SILERO_OUTPUT/test.wav" \
  --validation-audio "$SILERO_OUTPUT/validation.wav" \
  --output-path "$SILERO_OUTPUT/silero_vad_ethos_u.pte" \
  --expected-output-path "$SILERO_OUTPUT/expected_probs.bin" \
  2>&1 | tee "$SILERO_OUTPUT/export.log"
```

The compile specification in this pinned example selects `ethos-u85-256`, `Shared_Sram`, and the default `Ethos_U85_SYS_DRAM_Mid` system configuration. The latter is a compiler performance model, not a claim that the E8 has the FVP memory system. The application copies the PTE into aligned SRAM and supplies SRAM for delegated scratch. Keep the exported memory mode and firmware placement together when changing either.

The export generates two artifacts that must stay paired:

| Artifact | Purpose |
| --- | --- |
| `silero_vad_ethos_u.pte` | Quantized program, delegated command streams, weights, and initial recurrent state |
| `expected_probs.bin` | Host quantized-graph probabilities for the 79 windows in `validation.wav` |

The host reference checks agreement with the quantized model. It is not the floating-point model's accuracy against labeled speech. Calibration and validation overlap in this example; use separate labeled recordings for an accuracy study.

The pinned source and released environment were checked together: export produced a 363,392-byte PTE and 316-byte reference. Both matched the retained FVP-tested release artifacts byte for byte. This checks host export reproducibility; it does not establish physical E8 execution.

## Inspect the exported operators

Require both nonempty artifacts, then generate the CPU operator selection that the firmware build will use:

```bash
test -s "$SILERO_OUTPUT/silero_vad_ethos_u.pte"
test -s "$SILERO_OUTPUT/expected_probs.bin"
python codegen/tools/gen_oplist.py \
  --model_file_path "$SILERO_OUTPUT/silero_vad_ethos_u.pte" \
  --output_path "$SILERO_OUTPUT/selected_operators.yaml"
cat "$SILERO_OUTPUT/selected_operators.yaml"
```

CPU operators are expected. A Vela subgraph's zero CPU-operator count describes that compiled subgraph, not the entire ExecuTorch program. Do not apply a fully delegated MobileSAM check to this stateful model.

Record hashes so you can identify the exact firmware inputs later:

```bash
shasum -a 256 \
  "$SILERO_OUTPUT/silero_vad_ethos_u.pte" \
  "$SILERO_OUTPUT/expected_probs.bin" \
  "$SILERO_OUTPUT/validation.wav" \
  > "$SILERO_OUTPUT/model-inputs.sha256"
```

## What you've accomplished

You have exported the U85 program, preserved its initialized recurrent state, and generated a 79-window host reference from the same audio. Next, embed the program and recording in E8 firmware with the required CPU and NPU components.
