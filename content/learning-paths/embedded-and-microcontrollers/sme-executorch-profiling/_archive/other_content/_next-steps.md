---
weight: 99
title: "Next Steps"
layout: "learningpathall"
---

## What you've learned

You can now:
- Profile ExecuTorch models with operator-level precision
- Compare SME2 on/off to quantify acceleration and find new bottlenecks
- Interpret ETDump traces (nested events, category breakdowns, kernel hints)
- Identify when data movement dominates (~40% after SME2 accelerates compute)
- Map profiling insights back to model architecture changes

**This workflow generalizes:** Use it on any PyTorch model that targets Arm devices.

## Immediate next steps

### 1. Profile your production model
Apply pages 04 + 08 to your real workload. Look for:
- Non-delegated ops (export issues)
- Layout churn (architecture issues)
- Surprising bottlenecks (batch norms? reshapes? specific conv layers?)

### 2. Try on real Armv9 hardware (Android)
See page 07 for Android pipeline setup. Real SME2 devices reveal:
- Actual speedups (not Mac simulations)
- Device-specific bottlenecks (thermal throttling, memory bandwidth)
- Production-representative behavior

### 3. Automate with agentic kits (page 09)
If you're integrating this into CI or want AI assistants to run/validate/troubleshoot:
- `agentic-kits/setup-agent.md` for automated setup validation
- `agentic-kits/pipeline-agent.md` for config-driven runs
- `agentic-kits/validation-agent.md` for schema-level result checking

## Advanced topics (beyond this learning path)

### Quantization + SME2
- INT8 benefits from SME2 but less than FP16 (~1.8× vs ~3.9×)
- Profile both: sometimes FP16+SME2 beats INT8+NEON
- Resources: [ExecuTorch quantization guide](https://pytorch.org/executorch/main/quantization-overview.html)

### Multi-threading
- Current configs use 1 thread (isolates SME2 effect)
- Production: try 2–4 threads on big cores
- Watch for: synchronization overhead, cache thrashing

### Custom delegates
- If XNNPACK doesn't cover your ops, write a custom delegate
- Resources: [ExecuTorch backend guide](https://pytorch.org/executorch/main/backend-delegate-tutorial.html)

### Model architecture optimization
Based on profiling findings:
- **High data movement?** Reduce layout changes, fuse ops, use consistent memory formats
- **Non-delegated ops?** Replace with XNNPACK-friendly alternatives
- **Specific conv slow?** Adjust padding/strides to match kernel expectations

## Community and support

- **ExecuTorch forums:** https://discuss.pytorch.org/c/executorch
- **Arm developer forums:** https://community.arm.com/
- **Kleidi kernels:** https://gitlab.arm.com/kleidi (for kernel-level optimization insights)

## Share your findings

If you discover interesting SME2 acceleration patterns or optimization techniques, consider:
- Writing a blog post or technical report
- Contributing examples back to ExecuTorch
- Sharing operator-level insights with the Arm community

**Remember to include ExecuTorch SHA** (from `manifest.json`) when publishing results for reproducibility.
