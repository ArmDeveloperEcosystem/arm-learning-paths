---
title: Export and validate the MAPPO actor
description: Extract the shared MAPPO actor from the BenchMARL checkpoint and validate a lightweight inference artifact.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the actor artifact

The full BenchMARL checkpoint contains the actor, critic, optimizer, collector state, and training counters. A deployment runtime needs only the actor policy and the metadata that defines its input and output contract.

The shared actor trained in this Learning Path has the following structure:

```text
18 observation values
        ↓
Linear 18 → 256 and Tanh
        ↓
Linear 256 → 256 and Tanh
        ↓
Linear 256 → 4
        ↓
2-D deterministic action
```

The observation contains two position values, two velocity values, two agent-minus-goal values, and 12 LiDAR proximity values. The four raw outputs define the location and scale of a two-dimensional `TanhNormal` action distribution. Deterministic inference applies `tanh()` to the two location values.

The exporter is deliberately specific to this interface. It stops if the checkpoint, configuration, actor shapes, or action semantics don't match.

## Download the exporter

The reviewed [`export_mappo_actor.py` script](export_mappo_actor.py) is stored with this Learning Path. Download the same version from the Learning Paths repository:

```bash
source "$HOME/venvs/mappo/bin/activate"
cd "$HOME/BenchMARL"
curl -fL \
    https://learn.arm.com/learning-paths/servers-and-cloud-computing/train-mappo-navigation-arm-cloud/export_mappo_actor.py \
    -o export_mappo_actor.py
chmod +x export_mappo_actor.py
```

{{% notice Security %}}
`config.pkl` uses Python pickle serialization. Run the exporter only on configuration and checkpoint files produced by a training run you trust.
{{% /notice %}}

## Export the actor

Create an output name that includes the checkpoint frame count and a short source checksum. This prevents two different training runs from silently sharing a filename:

```bash
export ACTOR_EXPORT_DIR="$HOME/mappo_actor_exports"
mkdir -p "$ACTOR_EXPORT_DIR"

CHECKPOINT_STEP="${CHECKPOINT##*checkpoint_}"
CHECKPOINT_STEP="${CHECKPOINT_STEP%.pt}"
CHECKPOINT_SHA="$(sha256sum "$CHECKPOINT" | cut -d' ' -f1)"
export ACTOR_OUTPUT="$ACTOR_EXPORT_DIR/mappo_actor_${CHECKPOINT_AGENTS}agent_${CHECKPOINT_STEP}_${CHECKPOINT_SHA:0:12}.npz"
```

Run the exporter with the explicit output path:

```bash
python export_mappo_actor.py \
    --checkpoint "$CHECKPOINT" \
    --output "$ACTOR_OUTPUT"
```

The exporter refuses to replace an existing file. Use a different output name for another run, or add `--force` only when you intend to atomically replace the artifact.

A successful export ends with output similar to:

```output
Actor export:              /home/ubuntu/mappo_actor_exports/mappo_actor_3agent_1910000_a1b2c3d4e5f6.npz
Source SHA-256:            a1b2c3d4e5f6...
Agents:                    3
Frames:                    1910000
Input:                     18
Hidden:                    256, 256
Raw output:                4
NumPy raw parity max err:  <small value>
Action parity max err:     <small value>
Validation:                PASS
```

The exporter validates the following contract:

- The navigation configuration includes every deployment-critical setting
- The policy shares actor parameters and uses `TanhNormal`
- The actor has two 256-unit `Tanh` layers and no normalization layer
- The actor input implies exactly 12 LiDAR values
- The serialized NumPy tensors reproduce the extracted PyTorch tensor computation
- The deterministic two-value action matches the TorchRL distribution semantics

It writes to a temporary file, validates that file, and then moves it atomically to `ACTOR_OUTPUT`. The artifact metadata stores source names and a SHA-256 checksum, but it doesn't expose absolute paths from the training host.

## Inspect the exported artifact

Inspect the arrays and metadata without allowing pickled NumPy objects:

```bash
python - <<'PY'
import json
import os

import numpy as np

with np.load(os.environ["ACTOR_OUTPUT"], allow_pickle=False) as actor:
    for name in actor.files:
        print(name, actor[name].shape, actor[name].dtype)
    metadata = json.loads(str(actor["metadata_json"]))

print(json.dumps(metadata, indent=2))
PY
```

Confirm that the archive contains these arrays:

```output
W1 (256, 18)
b1 (256,)
W2 (256, 256)
b2 (256,)
W3 (4, 256)
b3 (4,)
metadata_json ()
```

## Run a standalone inference check

Run one inference step with an all-zero observation:

```bash
python - <<'PY'
import os

import numpy as np

with np.load(os.environ["ACTOR_OUTPUT"], allow_pickle=False) as actor:
    observation = np.zeros(18, dtype=np.float32)
    hidden1 = np.tanh(actor["W1"] @ observation + actor["b1"])
    hidden2 = np.tanh(actor["W2"] @ hidden1 + actor["b2"])
    raw = actor["W3"] @ hidden2 + actor["b3"]
    action = np.tanh(raw[:2])

print("Action:", action)
print("Shape:", action.shape)
print("Finite:", np.all(np.isfinite(action)))
print("Within [-1, 1]:", np.all(np.abs(action) <= 1.0))
PY
```

The expected validation fields are:

```output
Shape: (2,)
Finite: True
Within [-1, 1]: True
```

## What you've accomplished

You have trained and evaluated a MAPPO navigation policy, exported its shared actor without the training-only state, and validated the deployment interface. Continue with [the Device Connect dashboard Learning Path](/learning-paths/servers-and-cloud-computing/use-mappo-device-connect-dashboard/) to distribute and arm the actor through a simulated device.
