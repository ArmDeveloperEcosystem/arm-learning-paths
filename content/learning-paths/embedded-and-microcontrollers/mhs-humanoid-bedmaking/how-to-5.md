---
title: The whole-body bed-reach policy in Isaac Lab
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why a whole-body reinforcement-learning policy

When a free-standing humanoid bends over a bed, a walking-balance controller topples because the reach throws the centre of mass past the feet. The demo solves this with **one whole-body RL policy** that owns all 29 body joints (legs, waist, and arms) at 50 Hz and holds **balance and reach at once**.

The policy is trained in Isaac Lab on the same locomotion RL rails Unitree uses, with:

- a **station-keeping reward** — reach by leaning, but stay planted;
- a **bed-obstacle constraint** so the robot bends around the bed, not through it; and
- a **grip-slip force load** so the learned reach is robust to the sheet pulling back.

It is **ambidextrous**: each robot reaches with the hand on the target's side, so the two flanking robots both draw the sheet headward as a natural same-side motion.

You do **not** need to train it to run this Learning Path — the trained policy ships with the demo. You will play the shipped checkpoint, then optionally run a short training loop to see how it is produced.

## Play the shipped policy

The deployable policy is committed at `rl/policy/policy.pt` (with an ONNX copy at `rl/policy/policy.onnx`). Play it and render a video:

```bash
cd "$WORK/IsaacLab"
export LD_PRELOAD="${LD_PRELOAD:+$LD_PRELOAD:}/lib/aarch64-linux-gnu/libgomp.so.1"
./isaaclab.sh -p "$WORK/robots/examples/isaac_bed_making/rl/play.py" \
    --headless --enable_cameras --video --num_envs 4 --video_length 350 \
    --checkpoint "$WORK/robots/examples/isaac_bed_making/rl/policy/policy.pt"
```

This spawns four robots in parallel and records an MP4 of them reaching over the bedside while balancing — the skill the full demo hands off to after the approach walk.

## Optional: run a short training loop

To see how the policy is trained, run a **short** loop. This is for learning the training workflow, not for producing a converged policy — the shipped policy was trained for around 1500 iterations, which takes considerably longer.

```bash
cd "$WORK/IsaacLab"
./isaaclab.sh -p "$WORK/robots/examples/isaac_bed_making/rl/train.py" \
    --headless --num_envs 2048 --max_iterations 50 --run_name teaching_run
```

Training logs and checkpoints are written under `rl/logs/bed_reach_g1/<run>/`. You can play any checkpoint from your run by pointing `--checkpoint` at its `model_*.pt`:

```bash
./isaaclab.sh -p "$WORK/robots/examples/isaac_bed_making/rl/play.py" \
    --headless --enable_cameras --video --num_envs 4 --video_length 350 \
    --checkpoint "$WORK/robots/examples/isaac_bed_making/rl/logs/bed_reach_g1/<run>/model_49.pt"
```

{{% notice Note %}}
**Why ship the checkpoint instead of training in the Learning Path.** Training a whole-body RL policy to convergence is many hours of GPU time and is non-deterministic run to run. Shipping the trained policy keeps the Learning Path reproducible: everyone plays the same policy and gets the same behavior, and the short training loop above is there only to make the workflow concrete.
{{% /notice %}}

## Where to go deeper

The full method — the reward and force terms, the four training iterations that reached the two-robot benchmark, the training configuration, and the sim-to-real design (no kinematic cheats, sensor-calibrated observations) — is documented in the demo's `RL_WHOLE_BODY_REACH.md`. The sensor calibration that shapes the observations comes from Arm's [robotics-connect](https://github.com/armwaheed/robotics-connect) G1 control stack.

You have now run the demo, seen how the robots coordinate over MHS, and played the policy that keeps them balanced. See the summary and next steps to continue.
