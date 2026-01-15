---
name: setup_workspace
description: Initialize the ExecuTorch profiling environment with all dependencies (venv, ExecuTorch clone, submodules, editable install). Use when setting up a new profiling workspace, after cleaning environment, or when ExecuTorch version needs updating.
---

# Skill: Setup Workspace

**Purpose**: Initialize the ExecuTorch profiling environment with all dependencies

**When to use**: 
- First-time setup of profiling workspace
- After cleaning workspace (`rm -rf .venv executorch`)
- When ExecuTorch version needs updating
- When submodules are out of sync

## Overview

This skill sets up a complete, isolated profiling environment. It creates a Python virtual environment, clones/updates the ExecuTorch repository, initializes all git submodules (critical for XNNPACK, KleidiAI), and installs ExecuTorch in editable mode so export tools and devtools work.

**Key outputs**: `.venv/` (Python environment) and `executorch/` (source code with submodules). The `executorch/` directory name **cannot be changed** - CMake requires it.

**Prerequisites**:
- macOS (Apple Silicon) or Linux
- Python 3.9+ installed
- CMake 3.29+ installed
- Git installed
- ~15 GB free disk space
- Network access (for cloning ExecuTorch and downloading dependencies)

## Steps

### 1. Verify Prerequisites

```bash
python3 --version  # Should be 3.9+
cmake --version    # Should be 3.29+
git --version
```

### 2. Run Setup Script

```bash
bash model_profiling/scripts/setup_repo.sh
```

This orchestrates:
- Creates `.venv/` Python virtual environment
- Clones `executorch/` repository (if missing) or updates existing checkout
- Fetches latest `origin/main`
- **Initializes git submodules** (`git submodule sync && git submodule update --init --recursive`) - **critical for XNNPACK, KleidiAI**
- Installs ExecuTorch in editable mode (`pip install -e .`)

### 3. Activate Virtual Environment

```bash
source .venv/bin/activate
```

**Verification**:

```bash
# Check venv exists and ExecuTorch is importable
source .venv/bin/activate
python -c "import executorch; print(f'ExecuTorch: {executorch.__file__}')"

# Check executorch/ directory exists (name is fixed, CMake requires it)
ls -d executorch/

# Verify submodules initialized (critical for XNNPACK backend)
ls -d executorch/backends/xnnpack/third-party/XNNPACK

# Run comprehensive validation
python model_profiling/scripts/validate_setup.py
```

**Expected outputs**:
- `.venv/` directory with Python environment
- `executorch/` directory with ExecuTorch source (name cannot be changed)
- ExecuTorch importable in Python
- Submodules initialized (XNNPACK, KleidiAI, etc.)
- Validation script returns exit code 0

## Failure Handling

| Issue | Symptom | Fix |
|-------|---------|-----|
| **Missing tools** | `command not found` | Install via package manager: `brew install cmake ninja` (macOS) |
| **Network/SSL issues** | `OSStatus -26276` or SSL errors | Check proxy settings, Python certificates, corporate firewall |
| **Submodule failures** | XNNPACK/KleidiAI missing | Manually run: `cd executorch && git submodule sync && git submodule update --init --recursive` |
| **Install failures** | `pip install` errors | Check logs, recreate venv: `rm -rf .venv && python3 -m venv .venv` |
| **Python version** | `Python 3.9+ required` | Upgrade Python or use `pyenv` to manage versions |

## Common Issues

### Corporate Proxy/SSL

If you see SSL certificate errors:
```bash
# Check Python certificates
python -c "import ssl; print(ssl.get_default_verify_paths())"

# If needed, set insecure mode (not recommended, use only if necessary)
SME2_PIP_INSECURE=1 bash model_profiling/scripts/setup_repo.sh
```

### Submodule Sync Issues

Submodules are critical - without them, XNNPACK backend won't work:
```bash
cd executorch
git submodule sync
git submodule update --init --recursive
```

### ExecuTorch Directory Name

**Important**: The `executorch/` directory name is **fixed** - CMake build system requires it. Don't rename it.

## Implementation Checklist

- [ ] Prerequisites verified (Python 3.9+, CMake 3.29+, Git)
- [ ] Setup script executed successfully
- [ ] Virtual environment activated
- [ ] ExecuTorch importable: `python -c "import executorch"`
- [ ] Submodules initialized (XNNPACK directory exists)
- [ ] Validation script passes: `python model_profiling/scripts/validate_setup.py`

**References**:
- Setup script: `model_profiling/scripts/setup_repo.sh`
- Validation script: `model_profiling/scripts/validate_setup.py`
- Prerequisites check: `model_profiling/scripts/check_prereqs.sh`
- Learning path: `02-setup-and-model-onboarding.md` (detailed setup instructions)
- ExecuTorch setup reference: `/Users/jaszhu01/Local/Github/sme2_executorch/pr16533_env_setup.md`

**Assets**:
- `model_profiling/scripts/setup_repo.sh` - Main setup orchestration script
- `model_profiling/scripts/check_prereqs.sh` - Prerequisites validation

**Next skill**: `02_build_runners.md`
