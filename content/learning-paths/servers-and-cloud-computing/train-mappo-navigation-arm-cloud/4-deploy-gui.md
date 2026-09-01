---
title: Deploy the checkpoint to the cloud GUI
description: Package the full BenchMARL experiment for the MARL GUI and validate the registered model.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the GUI dependency

The MARL GUI used in this stage is a separate application from BenchMARL and VMAS. It is not created automatically by the training workflow.

The GUI source and helper scripts are not included in the Arm Learning Paths repository. Treat this stage as optional unless you have the companion checkout described in the prerequisites. Checkpoint validation and actor export do not depend on the GUI.

If you already have the companion GUI code, use that checkout and continue with the steps below.

If you do not have the GUI code, you can either skip this stage and continue to the actor-export section, or create an equivalent visualization application. A compatible GUI should be able to:

- accept a BenchMARL `checkpoint_<frames>.pt` file and its associated `config.pkl`;
- reload the trained experiment with BenchMARL;
- run a single VMAS environment for interactive evaluation;
- render agent positions, goals, and episode state;
- register and select trained checkpoints;
- preserve the BenchMARL directory layout required by `Experiment.reload_from_file()`.

The required portable model structure is:

```text
<model-directory>/
├── config.pkl
└── checkpoints/
    └── checkpoint_<frames>.pt
```

The companion GUI used in this Learning Path also provides these utilities:

```text
tools/deploy_checkpoint.py
tools/inspect_checkpoint.py
```

`deploy_checkpoint.py` copies the trained checkpoint and its configuration into the GUI model store and registers the model. `inspect_checkpoint.py` verifies that BenchMARL can reload the checkpoint successfully.

The remaining commands assume that the companion GUI is available locally. If you create your own GUI, replace the paths and helper-script names below with the corresponding paths in your implementation.

## Prepare the GUI environment

The GUI reloads the full BenchMARL experiment, so use the same Python environment that you used for training:

```bash
source $HOME/venvs/mappo/bin/activate
export RUN_DIR=$HOME/mappo_navigation_runs/latest
source "$RUN_DIR/run.env"
```

Sourcing `run.env` restores `CHECKPOINT`, `SOURCE_EXPERIMENT_DIR`, the agent count, and the device labels saved in the previous section.

Set the GUI root to your local checkout:

```bash
export GUI_ROOT=$HOME/rl_marl_vmassmapponav_demo/app/marl_live_demo_gui
```

Verify that the deployment and inspection tools are available:

```bash
test -f "$GUI_ROOT/tools/deploy_checkpoint.py" && echo "Deployment tool found"
```

```bash
test -f "$GUI_ROOT/tools/inspect_checkpoint.py" && echo "Inspection tool found"
```

Install the GUI requirements into the active MAPPO environment:

```bash
python -m pip install -r "$GUI_ROOT/requirements.txt"
```

## Move training artifacts when the GUI is on another system

The GUI import requires both of these training artifacts:

```text
$SOURCE_EXPERIMENT_DIR/config.pkl
$SOURCE_EXPERIMENT_DIR/checkpoints/checkpoint_<frames>.pt
```

If training and the GUI run on different systems, copy the complete experiment directory to the GUI system and preserve this layout. After the copy, update `CHECKPOINT` and `SOURCE_EXPERIMENT_DIR` to the paths on the GUI system.

If the GUI runs on the same system as training, keep the existing paths.

## Validate the source checkpoint

Move to the GUI directory:

```bash
cd "$GUI_ROOT"
```

Inspect the source checkpoint:

```bash
python tools/inspect_checkpoint.py "$CHECKPOINT" --device cpu
```

Find this result in the output:

```output
"reload": "success"
```

If the tool reports `config.pkl file not found in experiment folder`, restore the BenchMARL directory layout before continuing.

## Register the checkpoint

The GUI deployment tool is part of the GUI checkout. Run it from its existing path:

```bash
python "$GUI_ROOT/tools/deploy_checkpoint.py" --checkpoint "$CHECKPOINT" --gui-root "$GUI_ROOT" --instance-label "$(hostname)" --sampling-device "$SAMPLING_DEVICE" --train-device "$TRAIN_DEVICE"
```

The deployment tool performs these tasks:

1. Locates `config.pkl` relative to the source checkpoint.
2. Reads `n_agents` from the trained task configuration.
3. Copies the checkpoint and configuration to the GUI model store.
4. Preserves the `checkpoints/checkpoint_<frames>.pt` layout required by BenchMARL.
5. Creates model metadata.
6. Adds the training instance, agent count, run configuration, and checkpoint to `configs/models.yaml`.

The deployed model has this structure:

```text
$GUI_ROOT/model_assets/models/<model-id>/
├── config.pkl
├── checkpoints/
│   └── checkpoint_<frames>.pt
├── model_metadata.json
└── source_path.txt
```

The `instance` metadata is required because the GUI first filters models by training instance and then builds the available agent-count selections.

## Verify the GUI model

Extract the checkpoint step:

```bash
export CHECKPOINT_STEP=$(basename "$CHECKPOINT" | sed 's/checkpoint_//;s/.pt//')
```

Construct the model ID generated by the deployment tool:

```bash
export MODEL_ID="$(hostname)_agents$(printf '%03d' "$CHECKPOINT_AGENTS")_sampling_${SAMPLING_DEVICE}_train_${TRAIN_DEVICE}_ckpt${CHECKPOINT_STEP}"
```

Set the deployed model paths:

```bash
export GUI_MODEL_DIR="$GUI_ROOT/model_assets/models/$MODEL_ID"
```

```bash
export GUI_CHECKPOINT="$GUI_MODEL_DIR/checkpoints/$(basename "$CHECKPOINT")"
```

Verify the artifacts:

```bash
ls -lh "$GUI_MODEL_DIR/config.pkl" "$GUI_CHECKPOINT" "$GUI_MODEL_DIR/model_metadata.json"
```

Verify the registry metadata:

```bash
python -c "import yaml; d=yaml.safe_load(open('$GUI_ROOT/configs/models.yaml')); m=next(x for x in d['models'] if x['id']=='$MODEL_ID'); print('kind=',m.get('kind')); print('instance=',m['metadata'].get('instance')); print('agents=',m['metadata'].get('agent_count')); print('run=',m['metadata'].get('run_name')); print('asset=',m['checkpoint'].get('asset_path'))"
```

A valid entry is similar to:

```output
kind= benchmarl_checkpoint
instance= <hostname>
agents= 3
run= sampling_cpu_train_cpu
asset= model_assets/models/<model-id>/checkpoints/checkpoint_<frames>.pt
```

Validate the deployed checkpoint:

```bash
python tools/inspect_checkpoint.py "$GUI_CHECKPOINT" --device cpu
```

Confirm that the output again contains:

```output
"reload": "success"
```

## Start the GUI

Start the application on the cloud instance. Bind it to the loopback interface so it is not exposed directly through the instance network:

```bash
cd "$GUI_ROOT"
```

```bash
./run_demo.sh --host 127.0.0.1 --port 8045
```

From your local workstation, open an SSH tunnel to the instance:

```bash
ssh -L 8045:127.0.0.1:8045 ubuntu@INSTANCE_PUBLIC_IP
```

Keep the SSH connection open and visit `http://127.0.0.1:8045` in your local browser. Replace `ubuntu` and `INSTANCE_PUBLIC_IP` with the SSH user and address for your instance.

{{% notice Security %}}
The SSH tunnel avoids opening TCP port 8045 to the internet. If you intentionally bind the GUI to `0.0.0.0`, restrict the cloud firewall or security-group rule to a trusted source address and confirm that the GUI's authentication is suitable for your environment.
{{% /notice %}}

Refresh the browser after registration. Select the model in this order:

```text
Training instance
    ↓
Agent count
    ↓
Run configuration
    ↓
Checkpoint
```

Select **Start** to run interactive VMAS playback with the trained MAPPO policy.

{{% notice Note %}}
The GUI uses a single VMAS environment for interactive playback. This is independent of the number of vectorized environments used during training.
{{% /notice %}}

## Know which artifacts the GUI uses

| Artifact | Location | Purpose |
| --- | --- | --- |
| Training checkpoint | `$CHECKPOINT` | Complete BenchMARL training state |
| Training configuration | `$SOURCE_EXPERIMENT_DIR/config.pkl` | Reconstructs the experiment |
| GUI checkpoint | `$GUI_MODEL_DIR/checkpoints/checkpoint_<frames>.pt` | Portable checkpoint used by the GUI |
| GUI configuration | `$GUI_MODEL_DIR/config.pkl` | Required for BenchMARL reload |
| GUI metadata | `$GUI_MODEL_DIR/model_metadata.json` | Describes the imported model |
| GUI registry | `$GUI_ROOT/configs/models.yaml` | Drives model selection |

The full BenchMARL checkpoint is the correct artifact for the GUI. For a downstream inference runtime, you can export only the actor parameters, as shown in the next section.

## What you've accomplished

You have preserved the BenchMARL directory layout, registered the checkpoint with the companion GUI, reloaded the deployed model, and accessed interactive playback through a secure tunnel. Next, you will extract the shared actor for a runtime that does not include BenchMARL.
