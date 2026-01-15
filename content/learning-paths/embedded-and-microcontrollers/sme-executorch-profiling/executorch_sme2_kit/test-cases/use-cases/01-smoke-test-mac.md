---
title: "Use case: macOS smoke test (export → run → validate)"
---

This is the fastest way to prove your environment + runner builds + pipeline wiring are correct.

## Preconditions

- You are in the profiling kit root (after copying `executorch_sme2_kit/` to your workspace):
  - `.../executorch_sme2_kit/`
- Network access is available (for cloning/installing ExecuTorch).

## Run

```bash
# 1) Setup ExecuTorch + venv
bash model_profiling/scripts/setup_repo.sh

# 2) Build SME2-on/off runners
bash model_profiling/scripts/build_runners.sh

# 3) End-to-end smoke test
python model_profiling/scripts/run_quick_test.py
```

## Expected outputs

- `models/toy_fp16.pte`
- `models/toy_fp16.pte.etrecord`
- `runners/mac_sme2_on/executor_runner`
- `runners/mac_sme2_off/executor_runner`
- `runs/mac/manifest.json`
- `runs/mac/metrics.json`
- `runs/mac/**.etdump`

Optional (recommended):

```bash
python model_profiling/scripts/analyze_results.py --run-dir runs/mac --model models/toy_fp16.pte
```

Expected output:

- `runs/mac/analysis_summary.json`

