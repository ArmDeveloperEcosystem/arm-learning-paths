---
title: Apply this to your own model (where the real insights live)
weight: 9
layout: "learningpathall"
---

## Why onboarding your model matters

MobileNet taught you the **workflow**. Your model will teach you the **surprises**:
- Maybe your conv layers are already fast, but batch norms dominate (unexpected!)
- Maybe you have non-delegated ops causing fallback (export issue to fix)
- Maybe layout churn (NCHW ↔ NHWC) is costing 30% of runtime (model architecture insight)
- Maybe FP16 is now **faster** than INT8 because conv benefits more from SME2 than quantized ops

This is where profiling results translate into concrete, model-specific actions.

## Export your model

```bash
# If your model is in torchvision/timm/transformers:
python scripts/export_model.py --model-name your_model --dtype fp16 --out models/my_model.pte

# If it's custom, add it to scripts/export_model.py's registry:
# 1. Define input shapes
# 2. Add preprocessing if needed
# 3. Ensure it exports cleanly (torch.export.export with strict=False)
```

**Pro tips:**
- Start with FP16 (larger SME2 deltas, easier to see patterns)
- Use small input sizes first (224×224 for vision) to iterate fast
- Keep the `.etrecord` — without it, you get timings but no operator names

## Run the SME2 on/off comparison

```bash
# Copy template and edit model path
cp configs/examples/mac_mobilenet_fp16.json configs/my_model_mac.json
# Edit: "model": "models/my_model.pte"

# Run pipeline
python scripts/mac_pipeline.py --config configs/my_model_mac.json

# Analyze
python scripts/analyze_results.py --run-dir runs/mac --quiet
```

## What to look for (and what it means)

### Surprising finding #1: Your convs are FAST, but batch norms dominate
**What it means:** Norms aren't delegated to XNNPACK; they run as individual ops with layout churn.  
**Action:** Consider layer norm (better for delegation) or fuse norms into conv at export.

### Surprising finding #2: Many tiny transposes add up (e.g., 30× 0.5 ms = 15 ms)
**What it means:** Layout disagreements between operators (channels-first vs channels-last).  
**Action:** Force consistent layout in export, or use `memory_format=channels_last` in PyTorch.

### Surprising finding #3: A specific conv layer is 10× slower than others
**What it means:** Kernel didn't delegate (wrong shapes? unsupported padding? depthwise conv edge case?).  
**Action:** Check `kernel_hint` in `operator_details` — if no `__neonsme2`, it fell back. Debug export.

### Surprising finding #4: FP16 is now faster than INT8
**What it means:** Your model's bottleneck shifted from compute (helped by quantization) to memory/layout (not helped by quantization).  
**Action:** FP16 becomes viable! Skip quantization complexity.

## Compare to the reference (MobileNet)

```bash
# Put MobileNet and your model side-by-side
cat runs/mac/analysis_summary.json | jq '.category_totals_ms'
cat runs/my_model/analysis_summary.json | jq '.category_totals_ms'
```

**Questions to ask:**
- Is your Data Movement % higher? (layout churn issue)
- Is your "Other" % higher? (non-delegated ops issue)
- Is your Convolution % lower? (good! SME2 is working)

## Iterate

This is now a **measurement loop**:
1. Profile → identify slow operators
2. Hypothesize why (export? delegation? layout?)
3. Change model/export
4. Re-profile → measure delta

**The magic:** You're no longer guessing. Operator-level data tells you **exactly where time goes**.

---

**You've completed the core learning path.** Next steps (page 09) cover automation kits for CI/agents, and advanced topics like Android profiling.
