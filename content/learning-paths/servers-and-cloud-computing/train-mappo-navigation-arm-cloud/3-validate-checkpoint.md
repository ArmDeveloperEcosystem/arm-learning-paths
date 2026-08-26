---
title: Locate and validate the training checkpoint
description: Find the trained MAPPO checkpoint and keep the BenchMARL configuration required to reload it.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Find the checkpoint

BenchMARL creates an experiment directory below `RUN_DIR` with a structure similar to:

```text
$RUN_DIR/
└── mappo_navigation_mlp__<experiment-id>/
    ├── config.pkl
    ├── checkpoints/
    │   └── checkpoint_<frames>.pt
    └── ...
```

List the checkpoints created by the run:

```bash
find "$RUN_DIR" -type f -path '*/checkpoints/checkpoint_*.pt' -print
```

Select the most recently written checkpoint from this run:

```bash
export CHECKPOINT=$(find "$RUN_DIR" -type f -path '*/checkpoints/checkpoint_*.pt' -printf '%T@ %p\n' | sort -nr | head -1 | cut -d' ' -f2-)
```

Display and verify the path:

```bash
echo "$CHECKPOINT"
test -f "$CHECKPOINT" && echo "Checkpoint found: $CHECKPOINT"
```

## Keep `config.pkl` with the checkpoint

Determine the BenchMARL experiment directory:

```bash
export SOURCE_EXPERIMENT_DIR=$(dirname "$(dirname "$CHECKPOINT")")
```

Verify both artifacts:

```bash
ls -lh "$CHECKPOINT" "$SOURCE_EXPERIMENT_DIR/config.pkl"
```

BenchMARL uses the following relative layout when it reconstructs an experiment:

```text
<experiment-directory>/
├── config.pkl
└── checkpoints/
    └── checkpoint_<frames>.pt
```

Do not copy only `checkpoint_<frames>.pt` when you need to reload the complete BenchMARL experiment.

## Read deployment metadata from the experiment

Read the actual number of agents stored in the task configuration:

```bash
export CHECKPOINT_AGENTS=$(python -c "import pickle; f=open('$SOURCE_EXPERIMENT_DIR/config.pkl','rb'); pickle.load(f); cfg=pickle.load(f); print(cfg['n_agents'])")
```

Verify it:

```bash
echo "Checkpoint agents=$CHECKPOINT_AGENTS"
```

Inspect the full VMAS task configuration:

```bash
python -c "import pickle; f=open('$SOURCE_EXPERIMENT_DIR/config.pkl','rb'); task=pickle.load(f); cfg=pickle.load(f); print('Task:', task); print('Task configuration:', cfg)"
```

This value comes from the trained experiment and prevents a checkpoint from being registered with a stale shell value for the agent count.

{{% notice Security %}}
Only load `config.pkl` from a training run you trust. Python pickle files can execute code when loaded.
{{% /notice %}}
