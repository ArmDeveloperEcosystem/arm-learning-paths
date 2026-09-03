---
title: Configure and train MAPPO
description: Size the VMAS workload, configure MAPPO training and evaluation, and start the navigation experiment.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose the agent count and devices

MAPPO uses the centralized critic to learn from joint training information while each agent acts from its own observation. With `share_policy_params=true`, the three agents use the same actor parameters but receive different observations.

Move to the BenchMARL repository:

```bash
source $HOME/venvs/mappo/bin/activate
cd $HOME/BenchMARL
```

Use three agents for the reference experiment:

```bash
export AGENTS=3
```

Use CPU sampling and CPU training:

```bash
export SAMPLING_DEVICE=cpu
export TRAIN_DEVICE=cpu
```

BenchMARL configures sampling and training devices independently. You can also test `sampling=cpu, train=cuda` or `sampling=cuda, train=cuda` on a compatible system.

## Size the CPU sampling workload

Recreate the CPU sizing variables so that the configuration works after a new SSH login:

```bash
export CORE_COUNT=$(nproc)
export RESERVED_CPUS=1
export WORKLOAD_CPUS=$((CORE_COUNT - RESERVED_CPUS))
test "$WORKLOAD_CPUS" -ge 1 || { echo "This sizing policy needs at least 2 CPUs" >&2; exit 1; }
export N_ENVS=$WORKLOAD_CPUS
```

Collect 100 frames from each environment before every MAPPO update:

```bash
export FRAMES_PER_ENV_PER_BATCH=100
export FRAMES_PER_BATCH=$((N_ENVS * FRAMES_PER_ENV_PER_BATCH))
```

Evaluate every 20 batches using ten evaluation episodes:

```bash
export EVAL_EVERY_BATCHES=20
export EVAL_INTERVAL=$((FRAMES_PER_BATCH * EVAL_EVERY_BATCHES))
export EVAL_EPISODES=10
```

Choose one of the following budgeting options. Keeping 100 training batches reproduces the tested configuration. Keeping approximately 1,910,000 total frames keeps the total number of collected frames approximately constant when the CPU-sized environment count changes.

### Keep 100 training batches

Use this option to reproduce the reference experiment. The number of environments scales with the workload CPUs. Each environment contributes 100 frames per batch, and the run always performs 100 training batches:

```bash
export FRAME_BUDGET_MODE=fixed_batches
unset TARGET_MAX_FRAMES
export TRAINING_BATCHES=100
export MAX_FRAMES=$((FRAMES_PER_BATCH * TRAINING_BATCHES))
```

The primary configuration gives:

| Total CPUs | Environments | Frames per batch | Training batches | Total frames | Evaluation interval |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 64 | 63 | 6,300 | 100 | 630,000 | 126,000 |
| 192 | 191 | 19,100 | 100 | 1,910,000 | 382,000 |

The 64-vCPU example processes fewer total frames because it keeps both 100 frames per environment and 100 training batches. This is intentional for the original CPU-scaled benchmark configuration.

### Keep approximately 1,910,000 total frames

Use this alternative when you want different CPU-sized runs to collect approximately the same number of frames. Calculate enough complete batches to meet or exceed the target:

```bash
export FRAME_BUDGET_MODE=fixed_total_frames
export TARGET_MAX_FRAMES=1910000
export TRAINING_BATCHES=$(((TARGET_MAX_FRAMES + FRAMES_PER_BATCH - 1) / FRAMES_PER_BATCH))
export MAX_FRAMES=$((FRAMES_PER_BATCH * TRAINING_BATCHES))
```

The fixed-total-frame alternative gives:

| Total CPUs | Environments | Frames per batch | Training batches | Target frames | Actual frames | Evaluation interval |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 64 | 63 | 6,300 | 304 | 1,910,000 | 1,915,200 | 126,000 |
| 192 | 191 | 19,100 | 100 | 1,910,000 | 1,910,000 | 382,000 |

BenchMARL collects complete batches, so the actual frame count can exceed the target by less than one batch. This option also changes the number of MAPPO update and evaluation cycles on smaller instances. It preserves the approximate sample budget rather than an identical optimization trajectory.

{{% notice Note %}}
When VMAS sampling runs on CUDA, tune `N_ENVS` for the GPU instead of deriving it from the CPU count.
{{% /notice %}}

## Configure the output directory

Create a directory for the experiment:

```bash
export OUTPUT_ROOT=$HOME/mappo_navigation_runs
mkdir -p "$OUTPUT_ROOT"
```

Name the run so that the agent count, environment count, devices, and budgeting option are visible:

```bash
export RUN_NAME="agents_${AGENTS}__envs_${N_ENVS}__sampling_${SAMPLING_DEVICE}__train_${TRAIN_DEVICE}__budget_${FRAME_BUDGET_MODE}"
export RUN_DIR="$OUTPUT_ROOT/$RUN_NAME"
mkdir -p "$RUN_DIR"
ln -sfn "$RUN_DIR" "$OUTPUT_ROOT/latest"
```

The `latest` symbolic link gives later sections a stable way to recover the run directory after a new SSH login.

## Limit CPU thread parallelism

Cap the main CPU thread pools at the number of workload CPUs:

```bash
export OMP_NUM_THREADS=$WORKLOAD_CPUS
export MKL_NUM_THREADS=$WORKLOAD_CPUS
export OPENBLAS_NUM_THREADS=$WORKLOAD_CPUS
export NUMEXPR_MAX_THREADS=$WORKLOAD_CPUS
```

Capping the thread pools avoids library thread pools using more CPU threads than the workload allocation.

Record the software revision, installed packages, and shell configuration with the run:

```bash
export BENCHMARL_REVISION=$(git rev-parse HEAD)
python -m pip freeze > "$RUN_DIR/software-versions.txt"
declare -px \
  AGENTS SAMPLING_DEVICE TRAIN_DEVICE \
  CORE_COUNT RESERVED_CPUS WORKLOAD_CPUS N_ENVS \
  FRAMES_PER_ENV_PER_BATCH FRAMES_PER_BATCH FRAME_BUDGET_MODE \
  TRAINING_BATCHES MAX_FRAMES EVAL_EVERY_BATCHES EVAL_INTERVAL EVAL_EPISODES \
  OUTPUT_ROOT RUN_NAME RUN_DIR \
  OMP_NUM_THREADS MKL_NUM_THREADS OPENBLAS_NUM_THREADS NUMEXPR_MAX_THREADS \
  BENCHMARL_REVISION > "$RUN_DIR/run.env"
if [ -n "${TARGET_MAX_FRAMES:-}" ]; then
  declare -px TARGET_MAX_FRAMES >> "$RUN_DIR/run.env"
fi
```

`run.env` contains only the variables listed in the command. It doesn't copy credentials or the rest of your shell environment.

## Validate the configuration

Print the complete configuration before training:

```bash
echo "BudgetMode=$FRAME_BUDGET_MODE Agents=$AGENTS TotalCPUs=$CORE_COUNT ReservedCPUs=$RESERVED_CPUS WorkloadCPUs=$WORKLOAD_CPUS Environments=$N_ENVS FramesPerBatch=$FRAMES_PER_BATCH TrainingBatches=$TRAINING_BATCHES MaxFrames=$MAX_FRAMES EvalInterval=$EVAL_INTERVAL EvalEpisodes=$EVAL_EPISODES Sampling=$SAMPLING_DEVICE Training=$TRAIN_DEVICE"
```

For a 192-CPU system using the primary configuration, the reference values are:

```output
BudgetMode=fixed_batches Agents=3 TotalCPUs=192 ReservedCPUs=1 WorkloadCPUs=191 Environments=191 FramesPerBatch=19100 TrainingBatches=100 MaxFrames=1910000 EvalInterval=382000 EvalEpisodes=10 Sampling=cpu Training=cpu
```

Don't start training if a required field is blank.

## Train the policy

Start MAPPO training:

```bash
python benchmarl/run.py \
  algorithm=mappo \
  task=vmas/navigation \
  task.n_agents="$AGENTS" \
  experiment.sampling_device="$SAMPLING_DEVICE" \
  experiment.train_device="$TRAIN_DEVICE" \
  experiment.on_policy_n_envs_per_worker="$N_ENVS" \
  experiment.on_policy_collected_frames_per_batch="$FRAMES_PER_BATCH" \
  'experiment.loggers=[csv]' \
  experiment.render=false \
  experiment.evaluation=true \
  experiment.max_n_frames="$MAX_FRAMES" \
  experiment.checkpoint_at_end=true \
  experiment.prefer_continuous_actions=true \
  experiment.evaluation_interval="$EVAL_INTERVAL" \
  experiment.evaluation_episodes="$EVAL_EPISODES" \
  experiment.save_folder="$RUN_DIR"
```

This is the argument set used for the reference experiment. The tested BenchMARL and VMAS defaults define the 18-value observation and `256, 256` actor architecture checked by the exporter. BenchMARL saves a checkpoint when training completes.

{{% notice Important %}}
Training takes several hours on the reference system. Run the command in a persistent terminal session, such as `tmux`, so that an SSH disconnection doesn't terminate the process. The tested command saves its checkpoint at the end of training.
{{% /notice %}}

## What you've accomplished and what's next

You've configured a CPU-sized VMAS batch using either the tested fixed-batch budget or the alternative fixed-total-frame budget. BenchMARL now evaluates the policy periodically and saves the final checkpoint with the package versions, BenchMARL revision, budgeting mode, and workload variables recorded alongside the run.

Next, you'll locate and validate the training checkpoint.