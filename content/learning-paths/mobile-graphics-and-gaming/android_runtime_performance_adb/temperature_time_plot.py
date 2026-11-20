#!/usr/bin/env python3
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Plot device temperature over time.")
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    data = pd.read_csv(args.run_dir / "thermal-hal.csv")
    columns = ["elapsedSeconds", "type", "temperatureCelsius"]
    missing = [column for column in columns if column not in data]
    if missing:
        raise ValueError(f"thermal-hal.csv is missing columns: {', '.join(missing)}")
    data[columns] = data[columns].apply(pd.to_numeric, errors="coerce")
    data = data.dropna(subset=["elapsedSeconds", "temperatureCelsius"])
    cpu = data[data["type"].eq(0)]
    if not cpu.empty:
        data = cpu
    if data.empty:
        raise ValueError("thermal-hal.csv contains no temperature measurements")

    data = data.groupby("elapsedSeconds", as_index=False)["temperatureCelsius"].mean()

    figure, axis = plt.subplots(figsize=(10, 5))
    axis.plot(data["elapsedSeconds"], data["temperatureCelsius"], linewidth=2)
    axis.set(title="Device temperature over time", xlabel="Time (s)", ylabel="Temperature (°C)")
    axis.grid(alpha=0.25)
    figure.tight_layout()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    figure.savefig(args.output_dir / "gameplay-temperature.png", dpi=160)
    plt.close(figure)


if __name__ == "__main__":
    main()
