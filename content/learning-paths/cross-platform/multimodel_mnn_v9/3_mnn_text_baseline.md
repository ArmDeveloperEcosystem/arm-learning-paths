---
title: Run a text baseline with an Omni model on MNN
weight: 4
layout: learningpathall
---

## Steps

Create a simple text prompt file:

```bash
cat > ~/mnn_lp/text_baseline_prompt.txt <<'EOF'
You are an on-device assistant. In one short sentence, describe the goal of this tutorial.
EOF
```

Run `llm_demo`:

```bash
cd ~/mnn_lp/MNN/build
./llm_demo ~/mnn_lp/Qwen2.5-Omni-7B-MNN/config.json ~/mnn_lp/text_baseline_prompt.txt
```

You should see a short textual response describing the tutorial’s goal.

## Checkpoint

You have completed this module when:

- `llm_demo` successfully loads the config and model
- At least one text prompt returns a stable, sensible response
- No crashes or runtime errors occur
