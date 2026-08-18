---
title: Reproduce natural motion with Adversarial Motion Priors
description: Train humanoid walking, running, and dance policies with Adversarial Motion Priors in Isaac Lab on DGX Spark.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduce natural and humanlike motion with AMP

Adversarial Motion Priors (AMP) is a workflow that helps reinforcement learning policies produce motion that looks more natural and humanlike.

Traditional reinforcement learning can teach a robot to walk, run, or satisfy control objectives, but the resulting motion is often effective rather than natural. For robots that coexist with people, interact in human environments, or demonstrate expressive behavior, that's usually not enough. Isaac Lab therefore supports AMP, which uses reference motion-capture data to guide policy learning toward smoother and more realistic movement.

AMP comes from the SIGGRAPH 2021 paper by researchers at UC Berkeley and collaborators: [Adversarial Motion Priors for Stylized Physics-Based Character Control](https://arxiv.org/abs/2104.02180). At a high level, AMP works like a generative adversarial setup. A policy generates simulated motion, while a discriminator compares that motion against an unlabeled set of natural movement clips, often from motion capture. The policy then learns not only to complete the task reward, but also to produce trajectories that look statistically closer to the reference motion.

You'll use the `skrl` library with the `--algorithm AMP` flag to run humanoid walking, running, and dancing tasks.


## Train a humanoid robot to walk with a humanlike gait

You'll use human walking reference data to train a humanoid robot to produce stable and natural walking behavior.

### Run the training command

From `~/IsaacLab`, launch `skrl` training with `--algorithm AMP`:

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
  --task=Isaac-Humanoid-AMP-Walk-Direct-v0 \
  --headless \
  --algorithm AMP \
  --max_iterations=1000
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh train \
  --rl_library skrl \
  --task=Isaac-Humanoid-AMP-Walk-Direct-v0 \
  --viz none \
  --algorithm AMP \
  --max_iterations=1000
{{< /tab >}}
{{< /tabpane >}}

These commands use 1,000 iterations for a short baseline. The upstream task configuration defaults to 5,000 iterations.

### Verify the results of training

After training, look for the following behaviors:

- The humanoid moves forward stably instead of losing balance frequently.
- The gait shows smoother center-of-mass transfer instead of stiff hopping-like motion.
- The left and right leg timing resembles a more natural walking pattern.

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/skrl/play.py \
  --task=Isaac-Humanoid-AMP-Walk-Direct-v0 \
  --algorithm=AMP \
  --num_envs=16 \
  --checkpoint=logs/skrl/humanoid_amp_walk/<run_timestamp>/checkpoints/best_agent.pt \
  --real-time
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh play \
  --rl_library skrl \
  --task=Isaac-Humanoid-AMP-Walk-Direct-v0 \
  --algorithm=AMP \
  --num_envs=16 \
  --checkpoint=logs/skrl/humanoid_amp_walk/<run_timestamp>/checkpoints/best_agent.pt \
  --real-time
{{< /tab >}}
{{< /tabpane >}}

![Humanoid AMP walk training comparison. The left panel at iteration 3200 shows less stable gait timing and more rigid motion. The right panel at iteration 11600 shows smoother center-of-mass transfer, better leg coordination, and more natural walking behavior.#center](./walking_humanoid.gif "Humanoid AMP walk progression. Left: iteration 3200. Right: iteration 11600.")


## Train a humanoid robot to run with speed and coordination

If walking is mainly about stability and rhythm, running introduces a higher level of dynamic coordination. The robot must generate propulsion in a shorter contact window, keep the body balanced, and avoid losing control as motion amplitude increases.

You'll use human running reference data to train a humanoid robot to maintain a natural and controllable running pattern at higher speed.

### Run the training command

From `~/IsaacLab`, launch `skrl` training with `--algorithm AMP`:

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task=Isaac-Humanoid-AMP-Run-Direct-v0 \
    --headless \
    --algorithm AMP \
    --max_iterations=1000 
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh train \
    --rl_library skrl \
    --task=Isaac-Humanoid-AMP-Run-Direct-v0 \
    --viz none \
    --algorithm AMP \
    --max_iterations=1000
{{< /tab >}}
{{< /tabpane >}}

### Verify the effects of training

After training, confirm the following:

- As forward speed increases, the robot remains stable rather than falling immediately.
- Arm swing, leg lift, and landing timing become more coordinated.
- The motion looks like a recognizable running pattern rather than uncontrolled forward movement.

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/skrl/play.py \
  --task=Isaac-Humanoid-AMP-Run-Direct-v0 \
  --algorithm=AMP \
  --num_envs=16 \
  --checkpoint=logs/skrl/humanoid_amp_run/<run_timestamp>/checkpoints/best_agent.pt \
  --real-time
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh play \
  --rl_library skrl \
  --task=Isaac-Humanoid-AMP-Run-Direct-v0 \
  --algorithm=AMP \
  --num_envs=16 \
  --checkpoint=logs/skrl/humanoid_amp_run/<run_timestamp>/checkpoints/best_agent.pt \
  --real-time
{{< /tab >}}
{{< /tabpane >}}

![Humanoid AMP running comparison. At 3,000 iterations, the humanoid stumbles immediately. At 26,000 iterations, it uses a skipping gait while attempting to match the target running velocity.#center](./amp_running.gif "Humanoid AMP running at 3,000 and 26,000 iterations")


To continue training from a checkpoint, run:

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task=Isaac-Humanoid-AMP-Run-Direct-v0 \
    --headless \
    --algorithm AMP \
    --max_iterations=<number of additional iterations (Epochs)> \
    --checkpoint=<path_to_checkpoint>
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh train \
    --rl_library skrl \
    --task=Isaac-Humanoid-AMP-Run-Direct-v0 \
    --viz none \
    --algorithm AMP \
    --max_iterations=<number of additional iterations (Epochs)> \
    --checkpoint=<path_to_checkpoint>
{{< /tab >}}
{{< /tabpane >}}


Try training the model further to see if the skipping-like motion evolves into a run.

## (Optional) Train a humanoid robot to dance

To optionally test style-heavy motion generation, run the following AMP dance task:

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task=Isaac-Humanoid-AMP-Dance-Direct-v0 \
    --headless \
    --algorithm AMP
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh train \
    --rl_library skrl \
    --task=Isaac-Humanoid-AMP-Dance-Direct-v0 \
    --viz none \
    --algorithm AMP
{{< /tab >}}
{{< /tabpane >}}

{{% notice Note %}}

As of May 2026, training this model with the default number of iterations typically takes several hours on a DGX Spark. A pre-trained checkpoint for the dance task isn't available at this time, so you'll need to train the model from scratch.

{{% /notice %}}


## What you've accomplished and what's next

You've now used AMP to compare task completion with motion quality across humanoid behaviors.

Next, you'll compare the main reinforcement learning libraries supported by Isaac Lab.
