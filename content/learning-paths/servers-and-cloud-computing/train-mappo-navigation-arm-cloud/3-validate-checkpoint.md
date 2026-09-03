---
title: Locate and validate the training checkpoint
description: Find the trained MAPPO checkpoint and keep the BenchMARL configuration required to reload it.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Restore the run configuration

Activate the training environment and recover the saved variables. The `latest` link was created when you configured the run:

```bash
source $HOME/venvs/mappo/bin/activate
export RUN_DIR=$HOME/mappo_navigation_runs/latest
source "$RUN_DIR/run.env"
cd $HOME/BenchMARL
```

If you want to validate an older run, set `RUN_DIR` to that run directory before you source `run.env`.

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
test -n "$CHECKPOINT" && test -f "$CHECKPOINT" || { echo "No checkpoint found under $RUN_DIR" >&2; exit 1; }
echo "Checkpoint found: $CHECKPOINT"
```

The command stops the shell if no checkpoint exists, which prevents later commands from deriving paths from an empty value.

## Keep config.pkl with the checkpoint

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

Don't copy only `checkpoint_<frames>.pt` when you need to reload the complete BenchMARL experiment.

## Read deployment metadata from the experiment

Read the actual number of agents stored in the task configuration:

```bash
export CHECKPOINT_AGENTS=$(python -c "import pickle; f=open('$SOURCE_EXPERIMENT_DIR/config.pkl','rb'); pickle.load(f); cfg=pickle.load(f); print(cfg['n_agents'])")
```

Verify the read:

```bash
echo "Checkpoint agents=$CHECKPOINT_AGENTS"
```

Inspect the full VMAS task configuration:

```bash
python -c "import pickle; f=open('$SOURCE_EXPERIMENT_DIR/config.pkl','rb'); task=pickle.load(f); cfg=pickle.load(f); print('Task:', task); print('Task configuration:', cfg)"
```

This value comes from the trained experiment and prevents a checkpoint from being registered with a stale shell value for the agent count.

Save the checkpoint variables so you can restore them after a new SSH login:

```bash
declare -px CHECKPOINT SOURCE_EXPERIMENT_DIR CHECKPOINT_AGENTS >> "$RUN_DIR/run.env"
```

## Evaluate the reloaded policy

Run BenchMARL's evaluation entry point against the selected checkpoint:

```bash
python benchmarl/evaluate.py "$CHECKPOINT"
```

This command reconstructs the experiment from `config.pkl`, loads the trained state, and runs the saved evaluation configuration. A successful run proves that BenchMARL can execute the policy, while the earlier file checks prove only that the artifacts exist.

List the CSV logs produced by the experiment:

```bash
find "$SOURCE_EXPERIMENT_DIR" -type f -name '*.csv' -print
```

Compare the first and final evaluation returns in these logs. Returns vary with the random seed and package versions, so this Learning Path doesn't use an unverified numeric threshold. A flat or falling return means that checkpoint creation succeeded but the policy didn't demonstrate learning.

{{% notice Important %}}
Load `config.pkl` only from a training run that you trust. Python pickle files can execute code when loaded.
{{% /notice %}}

## What you've accomplished and what's next

You've selected a valid checkpoint, confirmed that its matching configuration is present, recovered deployment metadata, and reloaded the policy for evaluation. The checkpoint and `config.pkl` now form the portable BenchMARL experiment.

Next, you can [optionally deploy the experiment to a GUI](/learning-paths/servers-and-cloud-computing/train-mappo-navigation-arm-cloud/4-deploy-gui/). If you don't have companion GUI code, skip to [export the MAPPO actor for inference](/learning-paths/servers-and-cloud-computing/train-mappo-navigation-arm-cloud/5-export-actor/).
