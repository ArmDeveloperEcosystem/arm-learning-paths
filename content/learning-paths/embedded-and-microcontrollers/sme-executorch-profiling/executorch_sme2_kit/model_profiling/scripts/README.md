# Profiling kit scripts (SME2 + ExecuTorch)

These scripts are a **self-contained profiling kit** that lives alongside the learning path.

## Expected directory layout

Run everything from the learning path directory:

```bash
cd content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling
```

The scripts will create (or reuse):
- `.venv/` Python virtual environment
- `executorch/` ExecuTorch checkout (tracks `main`)
- `executorch/cmake-out/` built `executor_runner` binaries (runners stay with their ExecuTorch version for traceability)
- `models/` exported `.pte` and `.etrecord`
- `configs/` JSON pipeline configs
- `runs/` results, logs, traces, and manifests

## Time budget (clean machine)

- Setup: ~20–30 min  
- Build: ~15–25 min  
- Export + pipeline + analyze: ~10 min  
- **Total first success: ~60–75 min**

## Fast smoke test (recommended for first-time users)

After setup + build, validate the end-to-end flow with a tiny model:

```bash
python scripts/run_quick_test.py
```

This runs the full workflow (validate → build → export toy model → pipeline → validate results) in **~10–15 minutes** and confirms your setup works.

## Quick flow (manual, step-by-step)

```bash
chmod +x scripts/setup_repo.sh
./scripts/setup_repo.sh

chmod +x scripts/build_runners.sh
bash scripts/build_runners.sh

python scripts/export_model.py --model-name mobilenet_v3_small --dtype fp16 --out models/mobilenet_v3_small_fp16.pte

cp configs/templates/mac_template.json configs/mac.json
# edit configs/mac.json: set "model" to "models/mobilenet_v3_small_fp16.pte"
python scripts/mac_pipeline.py --config configs/mac.json

python scripts/analyze_results.py --run-dir runs/mac --quiet

# Validate results
python scripts/validate_results.py --results runs/mac
python scripts/compare_run_to_known_good.py --run-dir runs/mac --fixture-dir test-cases/fixtures/known_good_mac/runs/mac
```

## Notes
- On **macOS Apple Silicon**, you can learn the workflow and get operator-level breakdowns. SME2 acceleration requires Armv9 hardware: Apple M4 Macs and Armv9 Android devices will show SME2 deltas; earlier Apple Silicon will not.
- To observe SME2 deltas and `__neonsme2` kernel paths, use an **SME2-capable Armv9 device** (Android or Apple M4):

```bash
export ANDROID_NDK=/path/to/android-ndk
bash scripts/build_runners.sh

cp configs/templates/android_template.json configs/android.json
# edit configs/android.json: set "model" to your .pte
python scripts/android_pipeline.py --config configs/android.json

python scripts/analyze_results.py --run-dir runs/android
```

- Fast sanity: `python scripts/run_quick_test.py` builds, exports a toy model, runs the Mac pipeline, and validates outputs end-to-end.

