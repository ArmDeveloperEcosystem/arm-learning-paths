#!/usr/bin/env python3
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Plot LiteRT-LM inference performance.")
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    data = pd.read_csv(args.run_dir / "llm-perf.csv")
    columns = [
        "prefillTokens",
        "ttftSeconds",
        "prefillTokensPerSecond",
        "decodeTokensPerSecond",
    ]
    missing = [column for column in columns if column not in data]
    if missing:
        raise ValueError(f"llm-perf.csv is missing columns: {', '.join(missing)}")
    data[columns] = data[columns].apply(pd.to_numeric, errors="coerce")
    data = data.dropna(subset=columns)
    if data.empty:
        raise ValueError("llm-perf.csv contains no complete inference measurements")

    metrics = [
        ("ttftSeconds", "Time to first token", "Time (s)"),
        ("prefillTokensPerSecond", "Prefill speed", "Tokens/s"),
        ("decodeTokensPerSecond", "Decode speed", "Tokens/s"),
    ]
    figure, axes = plt.subplots(1, 3, figsize=(16, 5))
    for axis, (column, title, ylabel) in zip(axes, metrics):
        prompt_tokens = data["prefillTokens"]
        axis.scatter(prompt_tokens, data[column], alpha=0.75)
        if prompt_tokens.nunique() > 1:
            slope, intercept = np.polyfit(prompt_tokens, data[column], 1)
            fit_x = np.array([prompt_tokens.min(), prompt_tokens.max()])
            axis.plot(fit_x, slope * fit_x + intercept, linestyle="--")
        axis.set(title=title, xlabel="Prompt length (tokens)", ylabel=ylabel)
        axis.xaxis.set_major_locator(MaxNLocator(integer=True))
        axis.grid(alpha=0.25)

    figure.suptitle("PhotoTalk inference performance")
    figure.tight_layout()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    figure.savefig(args.output_dir / "gameplay-inference.png", dpi=160)
    plt.close(figure)


if __name__ == "__main__":
    main()
