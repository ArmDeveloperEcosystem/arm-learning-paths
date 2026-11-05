---
title: Visualise performance data
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Inspect the benchmark summary
Inside `$WORK/data/` you should have a directory labelled with the timestamp you ran the benchmark, for example: `runtime-perf-TIMESTAMP/`. Open this directory and inspect the file called `summary.txt`.

This text file contains useful information about the benchmark such as:
- Duration
- Number of inference calls
- Number of measurement samples
- Device information

Check these fields in the job summary:
- `device_serial=` matches your target device. If not, repeat the device setup steps.
- `package_name=` is `com.google.aiedge.examples.phototalk`. If not, check the application setup.
- `inference_count=` is greater than zero. If not, confirm that you pushed the model to the correct location.
- `power_source=` is not `unavailable`. If it is, your device might not expose a supported power-monitoring source.

## Download the plotting scripts
Download the four plotting scripts into `$WORK/plots/`:
```bash
mkdir -p "$WORK/plots"
cd "$WORK/plots"

curl -fL -O "$BASE_URL/inference_plot.py"
curl -fL -O "$BASE_URL/temperature_time_plot.py"
curl -fL -O "$BASE_URL/memory_time_plot.py"
curl -fL -O "$BASE_URL/power_time_plot.py"
```

## Visualise the latest benchmark
The plotting scripts use pandas to load the CSV files and Matplotlib to create the figures.

Create a new Jupyter Notebook section titled **Visualise performance data** and install both packages from a new notebook cell if they are not already available:
```python
%pip install pandas matplotlib
```

Create another cell and add this Python code:
```python
from IPython.display import Image, display
from pathlib import Path
import subprocess
import sys

ROOT = Path.cwd().resolve()
DATA_DIR = ROOT / "data"
PLOTS_DIR = ROOT / "plots"

run_dirs = sorted(DATA_DIR.glob("runtime-perf-*"))
if not run_dirs:
    raise FileNotFoundError(f"No benchmark runs found in {DATA_DIR}")

run_dir = run_dirs[-1]
FIGURES_DIR = run_dir / "figures"

plot_scripts = [
    "inference_plot.py",
    "temperature_time_plot.py",
    "memory_time_plot.py",
    "power_time_plot.py",
]

for script_name in plot_scripts:
    result = subprocess.run(
        [
            sys.executable,
            str(PLOTS_DIR / script_name),
            "--run-dir",
            str(run_dir),
            "--output-dir",
            str(FIGURES_DIR),
        ],
        check=False,
    )
    if result.returncode:
        print(f"Warning: {script_name} failed with exit code {result.returncode}")

for figure_path in sorted(FIGURES_DIR.glob("*.png")):
    display(Image(filename=str(figure_path)))
```

This cell selects the newest timestamped benchmark directory and creates data plots under the `$WORK/data/runtime-perf-TIMESTAMP/figures/` directory. Run the cell and inspect the figures to visualise the following performance measurements:
- TTFT, prefill, and decode speed by prompt length
- Device temperature over time
- Application resident memory over time
- Device power usage over time

## What you've accomplished and what's next
You have converted the measurements from your benchmark into figures that show inference performance and device behaviour over time. You should move on to the next section where you will learn to interpret the results you have gathered.
