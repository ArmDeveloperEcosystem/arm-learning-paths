---
title: "Overview and prerequisites"
weight: 2
layout: "learningpathall"
---

## Overview: build a repeatable SME2 profiling lab

Run ExecuTorch with and without SME2, capture ETDump traces, and see exactly where SME2 kernels land. This overview keeps the rest of the steps anchored in the big picture.

<p style="max-width: 980px; margin: 1.25rem auto;">
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/SME2_stack_01062026.png"
    alt="Runtime stack: PyTorch → ExecuTorch → XNNPACK → Arm Kleidi → SME2"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Runtime stack: PyTorch → ExecuTorch → XNNPACK → Arm Kleidi kernels → SME2 instructions.
  </span>
</p>

<p style="max-width: 980px; margin: 1.25rem auto;">
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/step_flow_overview.svg"
    alt="Workflow overview: setup → build → export → run → analyze → automate"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Workflow: setup → build → export → run → analyze (and optionally automate).
  </span>
</p>

### What you will deliver

- A **reproducible run directory** (`runs/mac/manifest.json`, `runs/mac/metrics.json`, `.etdump` traces per experiment).
- An **operator-level breakdown** (`runs/mac/analysis_summary.json` with category totals, operator details, and kernel hints).
- A **validated workflow** (scripts + configs that check prerequisites, run the pipelines, and compare against a known-good fixture).

### What you will learn (decision signals)

1. **SME2 is either used or it isn’t.** Confirm SME2 kernels in your traces (for example kernel names containing `__neonsme2`).
2. **SME2 shifts what is slow.** Faster compute makes data movement, layout conversions, or non-delegated ops show up clearly.
3. **Operator profiling gives next steps.** See which operators dominate and tie that back to export, delegation, and layout choices.

### Example outputs

<p style="max-width: 960px; margin: 1.25rem auto;">
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/squeeze_sam_latency_comparison.png"
    alt="End-to-end latency comparison (SME2 on vs off)"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    End-to-end latency changes when SME2 is enabled.
  </span>
</p>

<p style="max-width: 960px; margin: 1.25rem auto;">
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/combined_operator_breakdown_stacked.png"
    alt="Operator category breakdown (SME2 shifts bottlenecks)"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Operator-category breakdown: compute shrinks; other costs become visible.
  </span>
</p>

### Choose your route

{{% notice Note %}}
Two supported ways to follow this path:
- **Hands-on (human):** start here and proceed through page 08.
- **Automation-first (AI / CI):** jump to Automation workflows (page 09) and use the step pages as reference.
{{% /notice %}}

<p>
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/step01_prereqs.svg"
    alt="Outcome: prerequisites verified"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Outcome: prerequisites verified and you can proceed to setup/build.
  </span>
</p>

## Goal of this step

Confirm your machine has the build and runtime tools needed for this learning path. This avoids getting stuck mid-build with an opaque toolchain error.

**Time:** ~5 minutes

## Run the automated checker (recommended)

```bash
# After sparse checkout (see next page), run:
bash scripts/check_prereqs.sh
```

This checks: Python 3.9+, CMake 3.29+, Git, Ninja, Clang, and reports your CPU architecture.

{{% notice Note %}}
**Hardware note:** SME2 performance deltas require Armv9-class hardware (for example an Armv9 Android device with SME2, or Apple M4). The profiling workflow and ETDump analysis still work on earlier Apple Silicon.
{{% /notice %}}

## Manual checks (if you prefer)

```bash
python3 --version  # 3.9+ required
cmake --version    # 3.29+ required
git --version
uname -m           # Should show arm64 on Mac
df -h .            # Need ~15 GB free
```

## Optional: Android device validation

If you plan to profile on a real Armv9 Android device:

```bash
adb devices
adb shell getprop ro.product.cpu.abi  # Expect arm64-v8a
adb shell "cat /proc/cpuinfo | grep -i sme"  # Confirms SME2 capability
```

Android is the most common way to run on real Armv9 + SME2 hardware.

---

**Next:** Set up the workspace and install dependencies.
