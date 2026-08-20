---
title: Fine-tune SmolVLA
description: Fine-tune SmolVLA with the recorded SO-101 dataset, monitor training, and validate the saved model.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Fine-tune SmolVLA with your dataset

You will fine-tune the SmolVLA model with the SO-101 demonstrations you recorded. Fine-tuning adapts the model to your two camera views, robot joint layout, and pick-and-place task. Training runs locally on the DGX Spark GPU and produces a model checkpoint for physical evaluation.

Use the same LeRobot environment as the previous pages. Keep the values of `DATASET_REPO_ID` and `LOCAL_DATASET_ROOT` from the recording step.

## Run fine-tuning

Choose unused paths for `LOCAL_TRAIN_OUTPUT_DIR` and `LOCAL_TRAIN_LOG`. The output directory stores checkpoints and training metadata, while the log file stores the terminal output. The command stops instead of overwriting either path if it already exists.

Replace the placeholders, then run:

```bash
set -o pipefail
test ! -e $LOCAL_TRAIN_OUTPUT_DIR && \
test ! -e $LOCAL_TRAIN_LOG && \
PYTHONUNBUFFERED=1 lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --policy.device=cuda \
  --policy.push_to_hub=false \
  --policy.empty_cameras=1 \
  --rename_map='{"observation.images.gripper_cam":"observation.images.camera1","observation.images.workspace_cam":"observation.images.camera2"}' \
  --dataset.repo_id="$DATASET_REPO_ID" \
  --dataset.root="$LOCAL_DATASET_ROOT" \
  --output_dir="$LOCAL_TRAIN_OUTPUT_DIR" \
  --job_name=smolvla-so101-pick-place \
  --batch_size=64 \
  --steps=20000 \
  --save_checkpoint=true \
  --save_freq=20000 \
  --log_freq=200 \
  --wandb.enable=false \
  2>&1 | tee -a $LOCAL_TRAIN_LOG
```

The command loads the local dataset, fine-tunes the model, and saves the final checkpoint.

The key options are:

- `--policy.path=lerobot/smolvla_base` selects the pretrained SmolVLA model to fine-tune. In robotics, a policy is a model that converts observations, such as camera images and joint positions, into actions that control the robot.
- `--rename_map` maps the camera feature names in the dataset to the names expected by SmolVLA. The model expects camera inputs named `camera1`, `camera2`, and `camera3`, while this dataset contains `gripper_cam` and `workspace_cam`. The command maps:
  - `gripper_cam` to `camera1`
  - `workspace_cam` to `camera2`
- `--policy.empty_cameras=1` allows one expected camera input to be absent. The model's third camera input, `camera3`, is left empty.
- `--steps=20000` sets a fine-tuning baseline of 20,000 optimization steps. The SmolVLA documentation uses this value as a starting point.
- `--batch_size=64` follows the documented starting configuration and fits within the memory available on the DGX Spark used for this Learning Path.
- `--save_checkpoint=true` enables checkpoint saving, while `--save_freq=20000` saves a checkpoint after 20,000 steps. Because the training run is also 20,000 steps long, this configuration saves the final checkpoint without creating intermediate checkpoints.
- `--policy.push_to_hub=false` prevents the trained model from being uploaded automatically to the Hugging Face Hub.
- `PYTHONUNBUFFERED=1` makes Python write log messages immediately instead of buffering them. This allows `tee` to display and save the training output in real time.
- `2>&1 | tee -a $LOCAL_TRAIN_LOG` displays both standard output and error messages in the terminal and appends them to the specified log file.

## Monitor training

Open another terminal and run:

```bash
nvidia-smi
tail -f $LOCAL_TRAIN_LOG
```

`nvidia-smi` confirms that the training process is using the CUDA-enabled GPU. The log shows the current step, loss, learning rate, and timing information. Press `Ctrl+C` to stop following the log; this doesn't stop training in the original terminal.

After training finishes, set `MODEL_CHECKPOINT` to the saved model directory:

```bash
export MODEL_CHECKPOINT=$LOCAL_TRAIN_OUTPUT_DIR/checkpoints/last/pretrained_model
```

Verify that the required model, configuration, and processor files exist and aren't empty:

```bash
for file in config.json model.safetensors train_config.json \
            policy_preprocessor.json policy_postprocessor.json; do
    test -s "$MODEL_CHECKPOINT/$file" || {
        echo "Missing or empty: $file" >&2
        exit 1
    }
done
echo "Checkpoint files verified."
```

The expected output is:

```output
Checkpoint files verified.
```

## Understand how SmolVLA works

[SmolVLA](https://huggingface.co/docs/lerobot/smolvla) is a compact vision-language-action (VLA) model designed for fine-tuning on robot demonstrations. It combines a pretrained SmolVLM2 vision-language backbone with an action expert:

1. Camera images, the task instruction, and the current joint state provide context.
2. The vision-language backbone encodes the images and text, while a projection encodes the robot state.
3. A flow-matching action expert generates a chunk of continuous future joint commands.
4. During evaluation, LeRobot executes commands from the chunk and requests updated chunks as new observations arrive.

An *action chunk* is a short sequence of commands rather than one command.

- During training, flow matching adds noise to demonstrated action chunks and learns how to recover the demonstrated actions.
- During evaluation, the model starts from noise and iteratively produces a chunk conditioned on the live observations and instruction.

The [SmolVLA research paper](https://arxiv.org/abs/2506.01844) describes the model and its asynchronous inference design.

Fine-tuning adapts the model to the SO-101 geometry, camera viewpoints, and demonstrated behavior. With this configuration, the vision encoder remains frozen while the action expert and projection layers learn from the dataset.

## Review results from the example experiment

The following results come from the experiment performed while creating this Learning Path. They show what happened with this dataset on the DGX Spark; they aren't expected values for every training run.

The example run completed 20,000 steps in about 30 hours. Mean loss decreased across successive 4,000-step windows:

| Steps | Mean training loss |
|---|---:|
| 200–4,000 | 0.1031 |
| 4,200–8,000 | 0.0472 |
| 8,200–12,000 | 0.0287 |
| 12,200–16,000 | 0.0204 |
| 16,200–20,000 | 0.0175 |

The final logged loss was 0.017, and the last 2,000 steps stayed between 0.017 and 0.018. These values show stable optimization for this example. These values don’t measure physical task success.

## What you've accomplished

You fine-tuned SmolVLA with the recorded SO-101 dataset. Next, connect the follower and cameras to run controlled physical evaluations.
