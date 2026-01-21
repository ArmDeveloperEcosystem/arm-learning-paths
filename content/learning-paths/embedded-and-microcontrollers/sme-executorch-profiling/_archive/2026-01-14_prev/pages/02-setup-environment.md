---
title: "Set up your profiling workspace"
weight: 4
layout: "learningpathall"
---

<p>
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/step02_setup.svg"
    alt="Outcome: workspace prepared"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Outcome: workspace and dependencies installed.
  </span>
</p>

## Goal of this step

Create a working local workspace: Python environment + dependencies + ExecuTorch sources (or editable install). After this step, you should be able to run the quick test and confirm the toolchain works end-to-end.

**Time budget:** ~20–30 minutes (setup). Building runners is covered in the next step.

## Get the kit (sparse checkout — no 5 GB repo download)

```bash
git clone --filter=blob:none --sparse https://github.com/ArmDeveloperEcosystem/arm-learning-paths.git sme2-profiling && \
cd sme2-profiling && \
git sparse-checkout init --cone && \
git sparse-checkout set content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling && \
cd content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling
```

You now have: `scripts/`, `configs/`, `agentic-kits/`, `test-cases/` — everything needed.

## Install dependencies and clone ExecuTorch

```bash
bash scripts/check_prereqs.sh
chmod +x scripts/setup_repo.sh
./scripts/setup_repo.sh        # Clones ExecuTorch main + installs deps (~20–30 min)
```

**What `setup_repo.sh` does:**
1. Creates `.venv` and activates it
2. Clones ExecuTorch `main` (tracks latest, records SHA for reproducibility)
3. Installs PyTorch, ExecuTorch, and profiling tools
4. Runs a preflight pip check to catch TLS/SSL issues early

## Validate setup (quick test)

```bash
python scripts/run_quick_test.py
```

This runs a minimal end-to-end flow (export → run → validate) so you can confirm your environment is working before building larger runners or running longer experiments.

<details>
  <summary><strong>If setup fails</strong> (common blockers)</summary>

  <p><strong>TLS / SSL / certificates</strong>: pip install fails with certificate errors (for example on corporate networks).</p>
  <ul>
    <li>Fix your proxy / certificate configuration, then rerun <code>./scripts/setup_repo.sh</code>.</li>
    <li>Last resort (not recommended): <code>SME2_PIP_INSECURE=1 ./scripts/setup_repo.sh</code></li>
  </ul>

  <p><strong>Build tools missing</strong>: rerun <code>bash scripts/check_prereqs.sh</code> and install the missing tool (CMake/Ninja/clang).</p>
</details>

---

**Local entrypoints after setup:**
- Human workflow: `scripts/README.md` (quick flow)
- AI automation: `agentic-kits/README.md` (playbooks)
