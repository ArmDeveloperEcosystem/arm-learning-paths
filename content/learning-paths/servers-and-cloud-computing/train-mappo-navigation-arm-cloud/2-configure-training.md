---
title: Configure and train MAPPO
description: Size the VMAS workload, configure MAPPO training and evaluation, and start the navigation experiment.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose the agent count and devices

Move to the BenchMARL repository:

```bash
source "$HOME/venvs/mappo/bin/activate"
export BENCHMARL_ROOT="$HOME/BenchMARL"
cd "$BENCHMARL_ROOT"
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

BenchMARL configures sampling and training devices independently. This Learning Path keeps both workloads on the Arm CPU so the reference configuration is reproducible.

## Size the CPU sampling workload

Recreate the CPU sizing variables so the configuration works after a new SSH login:

```bash
CORE_COUNT="$(nproc)"
export CORE_COUNT
export RESERVED_CPUS=1
export WORKLOAD_CPUS=$((CORE_COUNT > RESERVED_CPUS ? CORE_COUNT - RESERVED_CPUS : 1))
export N_ENVS="$WORKLOAD_CPUS"
```

Collect 100 frames from each environment before every MAPPO update:

```bash
export FRAMES_PER_ENV_PER_BATCH=100
export FRAMES_PER_BATCH=$((N_ENVS * FRAMES_PER_ENV_PER_BATCH))
```

Run 100 training batches:

```bash
export TRAINING_BATCHES=100
export MAX_FRAMES=$((FRAMES_PER_BATCH * TRAINING_BATCHES))
```

Evaluate every 20 batches using ten evaluation episodes:

```bash
export EVAL_EVERY_BATCHES=20
export EVAL_INTERVAL=$((FRAMES_PER_BATCH * EVAL_EVERY_BATCHES))
export EVAL_EPISODES=10
```

The reference sizing gives:

| Total CPUs | Workload CPUs / environments | Frames per batch | Total frames | Evaluation interval |
| ---: | ---: | ---: | ---: | ---: |
| 64 | 63 | 6,300 | 630,000 | 126,000 |
| 192 | 191 | 19,100 | 1,910,000 | 382,000 |

{{% notice Note %}}
When VMAS sampling runs on CUDA, tune `N_ENVS` for the GPU instead of deriving it from the CPU count.
{{% /notice %}}

## Configure the output directory

Create a directory for the experiment:

```bash
export OUTPUT_ROOT=$HOME/mappo_navigation_runs
mkdir -p "$OUTPUT_ROOT"
```

Name the run so that the agent count, environment count, sampling device, and training device are visible:

```bash
export RUN_NAME="agents_${AGENTS}__envs_${N_ENVS}__sampling_${SAMPLING_DEVICE}__train_${TRAIN_DEVICE}"
export RUN_DIR="$OUTPUT_ROOT/$RUN_NAME"
mkdir -p "$RUN_DIR"
```

## Limit CPU thread parallelism

Give PyTorch access to the workload CPUs and keep secondary numerical libraries single-threaded:

```bash
export OMP_NUM_THREADS="$WORKLOAD_CPUS"
export MKL_NUM_THREADS="$WORKLOAD_CPUS"
export OPENBLAS_NUM_THREADS=1
export NUMEXPR_MAX_THREADS=1
```

This avoids nested OpenBLAS or NumExpr pools competing with PyTorch for every CPU. Monitor memory use and frames per second during the first batches. If the instance swaps or throughput drops, stop the run and retry with a smaller `N_ENVS`.

## Validate the configuration

Print the complete configuration before training:

```bash
echo "Agents=$AGENTS TotalCPUs=$CORE_COUNT ReservedCPUs=$RESERVED_CPUS WorkloadCPUs=$WORKLOAD_CPUS Environments=$N_ENVS FramesPerBatch=$FRAMES_PER_BATCH MaxFrames=$MAX_FRAMES EvalInterval=$EVAL_INTERVAL EvalEpisodes=$EVAL_EPISODES Sampling=$SAMPLING_DEVICE Training=$TRAIN_DEVICE"
```

For a 192-CPU system, the reference values are:

```output
Agents=3 TotalCPUs=192 ReservedCPUs=1 WorkloadCPUs=191 Environments=191 FramesPerBatch=19100 MaxFrames=1910000 EvalInterval=382000 EvalEpisodes=10 Sampling=cpu Training=cpu
```

Do not start training if a required field is blank.

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
    experiment.create_json=true \
    experiment.render=false \
    experiment.evaluation=true \
    experiment.max_n_frames="$MAX_FRAMES" \
    experiment.checkpoint_at_end=true \
    experiment.prefer_continuous_actions=true \
    experiment.evaluation_interval="$EVAL_INTERVAL" \
    experiment.evaluation_episodes="$EVAL_EPISODES" \
    experiment.save_folder="$RUN_DIR"
```

BenchMARL performs training and periodic evaluation and saves a checkpoint when the run completes.

## What you've accomplished

You have configured a CPU-only MAPPO run with bounded thread pools, periodic evaluation, and machine-readable evaluation output. Next, you will inspect the returns and validate the saved checkpoint.
