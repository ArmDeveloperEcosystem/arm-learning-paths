---
title: "Build runners (SME2 on/off)"
weight: 5
layout: "learningpathall"
---

<p>
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/step03_build.svg"
    alt="Outcome: two runner binaries built"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Outcome: two runner binaries built for SME2 on/off comparison.
  </span>
</p>

## Goal of this step

Build two variants of `executor_runner` so you can run the same `.pte` program with SME2 enabled and disabled. The rest of this learning path uses this on/off pair to interpret performance changes.

**Time:** ~15–25 minutes (CMake configure + build + Kleidi download)

## Build both variants

```bash
bash scripts/build_runners.sh
```

This creates:
- `runners/mac_sme2_on/executor_runner`
- `runners/mac_sme2_off/executor_runner`

**What happens under the hood:**
1. CMake configures ExecuTorch with XNNPACK backend
2. Downloads Arm Kleidi (optimized kernels for Armv8/Armv9)
3. Compiles two build configs (SME2 enabled vs disabled)
4. If `ANDROID_NDK` is set, also builds `android_sme2_on` and `android_sme2_off`

## Validate

```bash
ls -lh runners/mac_sme2_on/executor_runner
ls -lh runners/mac_sme2_off/executor_runner
```

Expected: Two binaries, each ~2–10 MB.

**Quick sanity check:**
```bash
runners/mac_sme2_on/executor_runner --help
```

Should print usage (confirms binary is valid).

<details>
  <summary><strong>If builds fail</strong> (common causes)</summary>

  <ul>
    <li><strong>Missing Ninja/CMake</strong>: rerun <code>bash scripts/check_prereqs.sh</code></li>
    <li><strong>Interrupted Kleidi download</strong>: remove the stale directory (<code>rm -rf build/_deps/kleidiai-*</code>) and rerun</li>
    <li><strong>Xcode CLI tools missing</strong>: <code>xcode-select --install</code></li>
  </ul>

  <p>If you want to shorten first iteration time, you can build <code>mac_sme2_on</code> only first, confirm export/run works, then build the off variant.</p>
</details>

## Optional: Android runners

```bash
export ANDROID_NDK=~/android-sdk/android-ndk-r26d  # See page 07 for NDK setup
bash scripts/build_runners.sh
```

Adds: `runners/android_sme2_on/` and `runners/android_sme2_off/`.

---

**Next:** Export a reference model (`.pte` + `.etrecord`).
