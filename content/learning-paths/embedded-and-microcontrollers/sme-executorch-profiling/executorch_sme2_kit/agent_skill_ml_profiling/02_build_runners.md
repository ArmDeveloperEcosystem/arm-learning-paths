---
name: build_runners
description: Build ExecuTorch runner binaries with SME2-on and SME2-off variants for profiling. Creates timing-only runners (default) and optionally trace-enabled runners for kernel analysis. Use when setting up profiling environment, after ExecuTorch updates, or when building custom runner variants.
---

# Skill: Build Runners

**Purpose**: Build ExecuTorch runner binaries with SME2-on and SME2-off variants

**When to use**: 
- After `setup_workspace` completes successfully
- After ExecuTorch version updates
- When building custom runner variants (trace-enabled, etc.)
- When switching between different ExecuTorch branches/PRs

## Overview

This skill builds the `executor_runner` binaries that execute `.pte` models. You need **two variants** for complete profiling:

1. **Timing-only runners** (default): No trace logging overhead → accurate latency measurements
2. **Trace-enabled runners** (optional): XNNPACK kernel trace logging → kernel-level insights (logging impacts timing)

**Key point**: The runners are built **inside** the `executorch/cmake-out/` directory (CMake build system) and **stay there** for version tracking. This keeps runners with their ExecuTorch version, making it easy to trace which ExecuTorch commit and build config was used. The `executorch/` directory name is fixed (CMake requirement).

**Prerequisites**:
- `executorch/` directory exists (from setup_workspace)
- `.venv/` activated
- CMake 3.29+ and Ninja installed
- For Android: `ANDROID_NDK` environment variable set

## Runner Variants

| Variant | Build Flags | Use For | Timing Impact |
|---------|-------------|---------|---------------|
| **mac_sme2_on** | SME2 enabled, timing-only | Latency measurement (SME2) | Accurate |
| **mac_sme2_off** | SME2 disabled, timing-only | Latency measurement (baseline) | Accurate |
| **android_sme2_on** | Android + SME2 enabled | Real device testing (SME2) | Accurate |
| **android_sme2_off** | Android + SME2 disabled | Real device testing (baseline) | Accurate |
| **trace-enabled** | Kernel logging enabled | Kernel analysis only | Overhead present |

**Decision**: Always build timing-only runners first. Build trace-enabled runners separately if you need kernel insights.

## Steps

### 1. Activate Virtual Environment

```bash
source .venv/bin/activate
```

### 2. Build Runners

```bash
bash model_profiling/scripts/build_runners.sh
```

This builds:
**Android runners** (for real-world edge ML performance on mobile devices):
- `executorch/cmake-out/android-arm64-v9a/executor_runner` (SME2 acceleration enabled)
- `executorch/cmake-out/android-arm64-v9a-sme2-off/executor_runner` (SME2 disabled, baseline)
- Built automatically if `ANDROID_NDK` environment variable is set

**macOS runners** (included for developer accessibility):
- `executorch/cmake-out/mac-arm64/executor_runner` (SME2 acceleration enabled)
- `executorch/cmake-out/mac-arm64-sme2-off/executor_runner` (SME2 disabled, baseline)
- Built automatically on macOS

**Build process** (simplified using CMake presets):
1. Merges SME2 profiling presets into ExecuTorch's `CMakePresets.json` (handles duplicates)
2. Uses `cmake --preset` to configure builds (clean, simple commands)
3. Uses `cmake --build --preset` to build runners
4. Runners stay in `executorch/cmake-out/` for version tracking (enables working with multiple ExecuTorch versions in parallel)

**Key improvement**: The script now uses CMake presets instead of manual CMake configuration, making it much simpler and easier to maintain.

**Verification**:

```bash
# Check runners exist and are executable
# Check Android runners (for mobile device testing)
test -f executorch/cmake-out/android-arm64-v9a/executor_runner && echo "✓ Android SME2-on runner exists"
test -f executorch/cmake-out/android-arm64-v9a-sme2-off/executor_runner && echo "✓ Android SME2-off runner exists"

# Check macOS runners (developer accessibility)
test -f executorch/cmake-out/mac-arm64/executor_runner && echo "✓ macOS SME2-on runner exists"
test -f executorch/cmake-out/mac-arm64-sme2-off/executor_runner && echo "✓ macOS SME2-off runner exists"

# Test runner can print help (verifies binary is valid)
# Test Android runner (for mobile device testing)
executorch/cmake-out/android-arm64-v9a/executor_runner --help | head -5

# Test macOS runner (developer accessibility)
executorch/cmake-out/mac-arm64/executor_runner --help | head -5

# Run comprehensive validation
python model_profiling/scripts/validate_setup.py
```

**Expected outputs**:
**Android runners** (for mobile device testing):
- `executorch/cmake-out/android-arm64-v9a/executor_runner` (executable binary)
- `executorch/cmake-out/android-arm64-v9a-sme2-off/executor_runner` (executable binary)

**macOS runners** (developer accessibility):
- `executorch/cmake-out/mac-arm64/executor_runner` (executable binary)
- `executorch/cmake-out/mac-arm64-sme2-off/executor_runner` (executable binary)

**Platform context**: This learning path demonstrates profiling ExecuTorch models on SME2-enabled devices using Android as the mobile device example. Android runs provide realistic edge ML performance with actual device constraints (memory bandwidth, thermal throttling, device-specific optimizations). macOS is included because most developers have Mac access, making it convenient for learning the workflow and initial testing. For production validation and accurate performance measurements, Android runs on real SME2-enabled devices provide the most representative results.

## Android Runners (for Mobile Device Testing)

To build Android runners:

```bash
export ANDROID_NDK=/path/to/android-ndk
bash model_profiling/scripts/build_runners.sh
```

The script detects `ANDROID_NDK` and builds Android variants automatically.

## Failure Handling

| Issue | Symptom | Fix |
|-------|---------|-----|
| **CMake errors** | Configuration failures | Check CMake version (3.29+), clean build dir: `rm -rf executorch/cmake-out/mac-*` |
| **KleidiAI download failures** | Missing KleidiAI source | Script auto-retries; if persistent, check network, verify submodules initialized |
| **Build timeouts** | Long build times | Increase parallelism or reduce `-j` flag, check system resources |
| **Missing dependencies** | Linker errors | Re-run `01_setup_workspace.md` to ensure ExecuTorch is properly installed |
| **Ninja not found** | `ninja: command not found` | Install ninja: `brew install ninja` (macOS) or `apt install ninja-build` (Linux) |

## Common Issues

### KleidiAI Download Failures

The build script automatically handles KleidiAI downloads. If it fails:
```bash
# Check network connectivity
ping github.com

# Manually verify submodules
cd executorch
git submodule status
```

### Build Directory Corruption

If builds fail mysteriously:
```bash
# Clean build directories
rm -rf executorch/cmake-out/mac-*

# Rebuild
bash model_profiling/scripts/build_runners.sh
```

### Android NDK Issues

```bash
# Verify NDK path
echo $ANDROID_NDK
ls $ANDROID_NDK

# Check NDK version (should be r21+)
$ANDROID_NDK/ndk-build --version
```

## Best Practices

- **Build timing-only runners first** - These are the default, most commonly used
- **Record ExecuTorch SHA** - Note which ExecuTorch version was used for builds
- **Keep runners after ExecuTorch updates** - Rebuild when ExecuTorch version changes
- **Verify runners before use** - Test with `--help` flag to ensure binaries are valid

## Implementation Checklist

- [ ] Virtual environment activated
- [ ] ExecuTorch directory exists (`executorch/`)
- [ ] CMake and Ninja installed
- [ ] Build script executed successfully
- [ ] Runners exist in `executorch/cmake-out/` directory
- [ ] Runners are executable and respond to `--help`
- [ ] Validation script passes

**References**:
- Build script: `model_profiling/scripts/build_runners.sh`
- Preset merge script: `model_profiling/scripts/merge_cmake_presets.py`
- CMake presets asset: `model_profiling/assets/cmake_presets.json`
- Learning path: `03-pipeline-and-analysis.md` (runner variants explanation)

**Assets**:
- `model_profiling/scripts/build_runners.sh` - Runner build orchestration (uses CMake presets)
- `model_profiling/scripts/merge_cmake_presets.py` - Merges SME2 presets into ExecuTorch's CMakePresets.json
- `model_profiling/assets/cmake_presets.json` - SME2 profiling presets (merged into ExecuTorch's defaults)

**Next skill**: `03_export_model.md` or `04_run_profiling.md` (if model already exported)
