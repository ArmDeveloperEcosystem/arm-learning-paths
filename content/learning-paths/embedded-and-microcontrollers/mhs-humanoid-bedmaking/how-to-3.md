---
title: Run the two-humanoid bed-making demo
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run it headless and render an MP4

The demo runs headless (no display) and captures frames into an MP4. From the Isaac Lab directory:

```bash
cd "$WORK/IsaacLab"
export LD_PRELOAD="${LD_PRELOAD:+$LD_PRELOAD:}/lib/aarch64-linux-gnu/libgomp.so.1"
PYTHONUNBUFFERED=1 ./isaaclab.sh -p \
    "$WORK/robots/examples/isaac_bed_making/demo.py" --loopback --render
```

{{% notice Note %}}
`--render` encodes the captured frames into an MP4 with **ffmpeg**. If ffmpeg is not installed, the
run still completes and writes the individual frames, but no MP4 is produced. Install it first:

```bash
sudo apt-get update && sudo apt-get install -y ffmpeg
```
{{% /notice %}}

The first launch takes a few minutes while Isaac Sim starts. You will then see the run progress through its stages in the log:

```output
[setup] scene built
[setup] floating base set; hand friction bound to 60 colliders
[setup] locomotion ready (unitree_rl_lab velocity walk-in + stand, GPU/torch)
[setup] bedsheet built (flat head edge + accordion ruffle at the foot; thick visual shell)
```

When the run finishes, the rendered video is written under:

```bash
ls "$WORK/robots/examples/isaac_bed_making/artifacts/isaac_bed_making/"
```

Open the MP4 and you should see both G1s walk in with their arms at their sides, then lean over the bed while balancing on their own two feet and reach for the draped sheet. The two robots adopt *different* postures — one squats deeper, one leans — because each solves the reach within its own balance envelope: learned control, not scripted choreography. Drawing the sheet fully up to the pillows is an open manipulation-quality problem; the walk-in, the balanced whole-body reach, and the MHS coordination are what this run reliably demonstrates.

## What the flags do

The demo takes several flags; the important ones for this Learning Path:

| Flag | Effect |
| --- | --- |
| `--loopback` | Coordinate the two robots over an in-process MHS bus (offline; the default). No broker required. |
| `--broker` | Register both robots on a real NATS fabric instead (needs credentials). |
| `--render` | Capture frames and encode an MP4 into `artifacts/isaac_bed_making/`. |
| `--gui` | Open the Isaac Sim window to watch live, instead of running headless. |
| `--no-walk` | Spawn the robots at the bedside and skip the approach walk. |
| `--walk-only` | Stop after the approach walk, to inspect locomotion on its own. |

{{% notice Note %}}
`--loopback` is the reproducible default for this Learning Path: the two robots coordinate over an **in-process MHS message bus**, so the whole demo runs on the Spark with no external broker and no credentials. In the next step you will look at what that coordination actually is, and how `--broker` puts the same robots on a real fabric.
{{% /notice %}}

## Inspect locomotion on its own (optional)

To watch just the approach walk — useful for confirming the velocity-walk policy runs on the GPU before the full sequence — run:

```bash
cd "$WORK/IsaacLab"
PYTHONUNBUFFERED=1 ./isaaclab.sh -p \
    "$WORK/robots/examples/isaac_bed_making/demo.py" --loopback --render --walk-only
```

With the demo running, continue to the next step to see how the two robots coordinate over MHS.
