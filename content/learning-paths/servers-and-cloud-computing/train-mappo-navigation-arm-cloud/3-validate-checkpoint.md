---
title: Evaluate and validate the training checkpoint
description: Measure the MAPPO evaluation returns and validate the checkpoint and configuration needed for actor export.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Measure the evaluation returns

BenchMARL writes evaluation episodes to a JSON file because the training command sets `experiment.create_json=true`. Locate the file created in `RUN_DIR`:

```bash
EVAL_JSON="$(
python - <<'PY'
import os
from pathlib import Path

files = list(Path(os.environ["RUN_DIR"]).rglob("*.json"))
if len(files) != 1:
    raise SystemExit(f"Expected one evaluation JSON file, found {len(files)}: {files}")
print(files[0])
PY
)"
export EVAL_JSON
echo "Evaluation data: $EVAL_JSON"
```

Summarize the first, final, and best mean return across evaluation episodes:

```bash
python - <<'PY'
import json
import math
import os
import statistics

with open(os.environ["EVAL_JSON"], encoding="utf-8") as file:
    report = json.load(file)

steps = []

def collect_steps(value):
    if not isinstance(value, dict):
        return
    for key, nested in value.items():
        if (
            key.startswith("step_")
            and isinstance(nested, dict)
            and "step_count" in nested
            and "return" in nested
        ):
            returns = [float(item) for item in nested["return"]]
            if not returns or not all(math.isfinite(item) for item in returns):
                raise SystemExit(f"Non-finite or empty returns in {key}")
            steps.append((int(nested["step_count"]), statistics.fmean(returns)))
        collect_steps(nested)

collect_steps(report)
if not steps:
    raise SystemExit("No evaluation returns found")

steps.sort()
first_frames, first_return = steps[0]
final_frames, final_return = steps[-1]
best_frames, best_return = max(steps, key=lambda item: item[1])

print(f"First mean return: {first_return:.4f} at {first_frames} frames")
print(f"Final mean return: {final_return:.4f} at {final_frames} frames")
print(f"Best mean return:  {best_return:.4f} at {best_frames} frames")
print(f"Best improvement:  {best_return - first_return:+.4f}")
PY
```

The output reports measured values from your run. A best return greater than the first return is evidence that training improved the evaluated policy. A single run is not a performance benchmark; repeat several seeds before drawing broader conclusions. If the best return doesn't improve, inspect the CSV logs and retry with more frames or different hyperparameters before deploying the policy.

## Locate the checkpoint

The training command requests one checkpoint at the end of the run. Resolve that checkpoint without relying on filename sorting or whitespace-sensitive shell pipelines:

```bash
CHECKPOINT="$(
python - <<'PY'
import os
from pathlib import Path

files = list(Path(os.environ["RUN_DIR"]).glob("*/checkpoints/checkpoint_*.pt"))
if len(files) != 1:
    raise SystemExit(f"Expected one final checkpoint, found {len(files)}: {files}")
print(files[0])
PY
)"
export CHECKPOINT
test -f "$CHECKPOINT" && echo "Checkpoint found: $CHECKPOINT"
```

Determine the BenchMARL experiment directory and verify its two required artifacts:

```bash
SOURCE_EXPERIMENT_DIR="$(dirname "$(dirname "$CHECKPOINT")")"
export SOURCE_EXPERIMENT_DIR
ls -lh "$CHECKPOINT" "$SOURCE_EXPERIMENT_DIR/config.pkl"
```

Keep this layout intact when you archive the complete training experiment:

```text
<experiment-directory>/
├── config.pkl
└── checkpoints/
    └── checkpoint_<frames>.pt
```

## Validate the stored task configuration

{{% notice Security %}}
Only load `config.pkl` from a training run you trust. Python pickle files can execute code when loaded.
{{% /notice %}}

Read the task settings through the exported environment variable instead of interpolating a path into Python source:

```bash
CHECKPOINT_AGENTS="$(
python - <<'PY'
import os
import pickle
from pathlib import Path

config_file = Path(os.environ["SOURCE_EXPERIMENT_DIR"]) / "config.pkl"
with config_file.open("rb") as file:
    _task = pickle.load(file)
    config = pickle.load(file)

print(config["n_agents"])
PY
)"
export CHECKPOINT_AGENTS
echo "Checkpoint agents=$CHECKPOINT_AGENTS"
```

Inspect the deployment-critical navigation settings:

```bash
python - <<'PY'
import os
import pickle
from pathlib import Path

config_file = Path(os.environ["SOURCE_EXPERIMENT_DIR"]) / "config.pkl"
with config_file.open("rb") as file:
    task = pickle.load(file)
    config = pickle.load(file)

print("Task:", task)
for key in ("n_agents", "collisions", "observe_all_goals", "lidar_range", "agent_radius", "max_steps"):
    print(f"{key}: {config[key]}")
PY
```

The values must match the navigation configuration used for training. The exporter stops if a deployment-critical value is absent or incompatible.

## What you've accomplished

You have measured the policy's evaluation returns and validated the final checkpoint with its trusted task configuration. Next, you will export the actor into a smaller inference artifact.
