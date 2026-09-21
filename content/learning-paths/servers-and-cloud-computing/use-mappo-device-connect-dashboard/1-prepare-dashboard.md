---
title: Prepare the Device Connect dashboard
description: Install the dashboard dependencies and verify that the exported MAPPO actor matches the deployment interface.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the deployment workflow

The training Learning Path produces an actor-only `.npz` file. The dashboard treats that file as a model that can move through a Device Connect deployment:

```text
Exported MAPPO actor
        ↓
Local model server
        ↓
Device Connect model download
        ↓
Simulated device policy package
```

You will run every service on the Arm cloud instance. The dashboard uses a simulated device, so this workflow doesn't connect to or move a physical robot.

## Locate the exported actor

Set `ACTOR_OUTPUT` to the artifact printed by `export_mappo_actor.py` in the training Learning Path. Replace the example filename with the frame count and source-checksum suffix from your export:

```bash
export ACTOR_OUTPUT="$HOME/mappo_actor_exports/mappo_actor_3agent_1910000_a1b2c3d4e5f6.npz"
test -f "$ACTOR_OUTPUT" && echo "Actor found: $ACTOR_OUTPUT"
```

The command prints the complete actor path. If it prints nothing, correct `ACTOR_OUTPUT` before continuing.

## Clone the MAPPO demo

Clone the repository that contains the Device Connect dashboard:

```bash
export MAPPO_DEMO="$HOME/mappo-arm-cloud-physical-ai"
git clone --filter=blob:none --no-checkout --depth 1 \
    https://github.com/armwaheed/mappo-arm-cloud-physical-ai.git \
    "$MAPPO_DEMO"
git -C "$MAPPO_DEMO" fetch --depth 1 origin \
    40d9be795da4e06725a1fc515ed5d3a6a9e7e5c1
git -C "$MAPPO_DEMO" checkout --detach \
    40d9be795da4e06725a1fc515ed5d3a6a9e7e5c1
```

The commit is pinned so that the commands and dashboard interface remain consistent with this Learning Path.

## Install the dashboard dependencies

Create a separate Python environment for the dashboard. Device Connect needs Python 3.11 or later; the Arm cloud environment from the training Learning Path provides Python 3.12:

```bash
python3.12 -m venv "$HOME/venvs/mappo-dashboard"
source "$HOME/venvs/mappo-dashboard/bin/activate"
python -m pip install --upgrade pip
python -m pip install \
    "device-connect-edge==0.2.5" \
    "device-connect-agent-tools==0.2.5" \
    "aiohttp==3.14.3" \
    "numpy==2.4.6" \
    "Pillow==12.3.0"
```

Verify the architecture, Python version, and Device Connect package versions:

```bash
python - <<'PY'
import platform
import sys
from importlib.metadata import version

print("Architecture:", platform.machine())
print("Python:", sys.version.split()[0])
print("Device Connect edge:", version("device-connect-edge"))
print("Device Connect agent tools:", version("device-connect-agent-tools"))
PY
```

The output is similar to:

```output
Architecture: aarch64
Python: 3.12.x
Device Connect edge: 0.2.5
Device Connect agent tools: 0.2.5
```

## Check the actor interface

The dashboard accepts the actor only if it contains the expected arrays and metadata. Run the same inspection that the dashboard applies after a model download:

```bash
cd "$MAPPO_DEMO/dashboard"
python - <<'PY'
import json
import os

from model_store import inspect_model

report = inspect_model(os.environ["ACTOR_OUTPUT"])
print(json.dumps(report.as_dict(), indent=2))
raise SystemExit(0 if report.loadable else 1)
PY
```

A compatible actor reports values similar to:

```output
{
  "name": "mappo_actor_3agent_1910000_a1b2c3d4e5f6.npz",
  "loadable": true,
  "problems": [],
  "trained_lidar_range_vmas": 0.35,
  "rays": 12,
  "training_frames": 1910000,
  "training_n_agents": 3
}
```

The command exits with a nonzero status if the actor can't be loaded. Don't continue if `problems` contains an unexpected array shape or LiDAR feature count.

## Create a disposable policy package

Arming a model changes `config.json` in the policy package. Copy the package to a temporary directory so the repository remains unchanged:

```bash
DASHBOARD_PACKAGE="$(mktemp -d -t mappo-dashboard-policy.XXXXXX)"
export DASHBOARD_PACKAGE
cp -a "$MAPPO_DEMO/policy/." "$DASHBOARD_PACKAGE/"
echo "Dashboard package: $DASHBOARD_PACKAGE"
```

## What you've accomplished

You have installed the dashboard dependencies, verified the exported actor contract, and created a disposable policy package. Next, you will start the Device Connect services and open the dashboard.
