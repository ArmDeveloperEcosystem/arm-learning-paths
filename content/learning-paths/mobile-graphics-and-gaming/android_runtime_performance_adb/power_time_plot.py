#!/usr/bin/env python3
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Plot device power usage over time.")
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    data = pd.read_csv(args.run_dir / "power.csv")
    columns = ["elapsedSeconds", "powerWatts"]
    missing = [column for column in columns if column not in data]
    if missing:
        raise ValueError(f"power.csv is missing columns: {', '.join(missing)}")
    data[columns] = data[columns].apply(pd.to_numeric, errors="coerce")
    data = data.dropna(subset=columns)
    if data.empty:
        raise ValueError("power.csv contains no power measurements")

    data["powerWatts"] = data["powerWatts"].abs()

    figure, axis = plt.subplots(figsize=(10, 5))
    axis.plot(data["elapsedSeconds"], data["powerWatts"], linewidth=2)
    axis.set(title="Device power usage over time", xlabel="Time (s)", ylabel="Power (W)")
    axis.grid(alpha=0.25)
    figure.tight_layout()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    figure.savefig(args.output_dir / "gameplay-power.png", dpi=160)
    plt.close(figure)


if __name__ == "__main__":
    main()
