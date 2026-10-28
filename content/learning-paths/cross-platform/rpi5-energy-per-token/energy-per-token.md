---
title: Measure joules per token for llama.cpp
description: Build llama-bench and run a Python script that aligns PMIC power samples with the llama.cpp token-generation phase to compute joules per token with and without idle power.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build llama-bench and download a model

If you already have `llama-bench` built in `$HOME/llama.cpp`, skip to [Measure only the token-generation phase](/learning-paths/cross-platform/rpi5-energy-per-token/#measure-only-the-token-generation-phase). Otherwise, install the build tools and build only the `llama-bench` target with one compile job, which keeps memory use low on a 2 GB board:

```bash
sudo apt update
sudo apt install -y git cmake build-essential
cd $HOME
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --target llama-bench -j 1
```

Your token rates and energy results might differ from the example outputs because llama.cpp changes frequently.

Download the Qwen2.5 0.5B Instruct model in the Q4_0 format:

```bash
mkdir -p $HOME/models
cd $HOME/models
wget https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/9217f5db79a29953eb74d5343926648285ec7e67/qwen2.5-0.5b-instruct-q4_0.gguf
```
The size of the file is about 429 MB.

## Measure only the token-generation phase

A `llama-bench` process first loads the model, then runs a warmup. Only then does the process run the timed repetitions. Loading reads the whole file from storage and draws a different amount of power than token generation. If you average power over the whole process, the result mixes the two and depends on how long loading took.

To exclude loading, the `energy_per_token.py` script runs `llama-bench` with `--progress`. With this option, `llama-bench` prints a line such as `generation run 1/3` immediately before each timed repetition starts. The script records a timestamp for each line as it arrives. The length of each repetition comes from `llama-bench` itself, in the `samples_ns` field of its JSON output. Every repetition therefore has a known start and end time. The script averages only the power samples inside that window.

The script also records an idle window before `llama-bench` starts. It saves the output of `vcgencmd get_throttled` and the temperature before and after the run.

The script starts `pmic_sampler.py` from its own directory, so both files need to be in the same directory. 

Change to the working directory that you created earlier:

```bash
cd $HOME/pi-energy
```

Use a text editor to save the following code as `energy_per_token.py` in `$HOME/pi-energy`:

```python
#!/usr/bin/env python3
"""Measure joules per generated token for llama.cpp on a Raspberry Pi 5.

1. Start pmic_sampler.py in the background.
2. Record an idle window with nothing else running.
3. Run llama-bench (generation only) with --progress and time stamp each
   "generation run" line, so every repetition has a known start time. Its
   length comes from llama-bench's own samples_ns.
4. Average the PMIC power inside each decode window only (model load and
   warmup are excluded) and convert to joules per token, with and without
   the idle power subtracted.
"""
import argparse
import csv
import json
import os
import statistics
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))


def vc(*args):
    return subprocess.run(["vcgencmd", *args], capture_output=True, text=True).stdout.strip()


def mean_power(rows, t0, t1, col):
    vals = [float(r[col]) for r in rows if t0 <= float(r["time_s"]) <= t1]
    return (statistics.fmean(vals) if vals else float("nan")), len(vals)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-m", "--model", required=True, help="GGUF model file")
    ap.add_argument("-t", "--threads", type=int, default=4)
    ap.add_argument("-n", "--n-gen", type=int, default=128, help="tokens per repetition")
    ap.add_argument("-r", "--reps", type=int, default=3, help="llama-bench repetitions")
    ap.add_argument("--idle", type=float, default=10.0, help="idle window in seconds")
    ap.add_argument("--rail", help="pass to the sampler to read one rail only")
    ap.add_argument("--llama-bench", default=os.path.expanduser("~/llama.cpp/build/bin/llama-bench"))
    ap.add_argument("--out", default="energy_run", help="output directory")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    power_csv = os.path.join(args.out, "power.csv")
    before = {"throttled": vc("get_throttled"), "temp": vc("measure_temp"),
              "arm_clock_hz": vc("measure_clock", "arm")}

    cmd = [sys.executable, os.path.join(HERE, "pmic_sampler.py"), power_csv]
    if args.rail:
        cmd += ["--rail", args.rail]
    sampler = subprocess.Popen(cmd)
    time.sleep(1.0)                      # let the sampler write its header

    idle_start = time.time()
    time.sleep(args.idle)
    idle_end = time.time()

    bench = [args.llama_bench, "-m", args.model, "-p", "0", "-n", str(args.n_gen),
             "-r", str(args.reps), "-t", str(args.threads), "--progress", "-o", "json"]
    proc = subprocess.Popen(bench, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    starts = []
    with open(os.path.join(args.out, "llama-bench.stderr"), "w") as err:
        for line in proc.stderr:
            now = time.time()
            err.write("%.4f %s" % (now, line))
            if ": generation run " in line:
                starts.append(now)
    result = json.loads(proc.stdout.read())[0]
    proc.wait()
    time.sleep(0.5)
    sampler.terminate()
    sampler.wait()
    after = {"throttled": vc("get_throttled"), "temp": vc("measure_temp")}

    with open(power_csv) as f:
        rows = list(csv.DictReader(f))
    col = "total_W" if not args.rail else args.rail + "_W"
    idle_w, idle_n = mean_power(rows, idle_start, idle_end, col)

    reps = []
    for start, ns in zip(starts, result["samples_ns"]):
        dur = ns / 1e9
        load_w, n = mean_power(rows, start, start + dur, col)
        reps.append({"start": start, "seconds": dur, "samples": n,
                     "tokens_per_s": args.n_gen / dur, "power_W": load_w,
                     "J_per_token": load_w * dur / args.n_gen,
                     "net_J_per_token": (load_w - idle_w) * dur / args.n_gen})

    summary = {"model": os.path.basename(args.model), "threads": args.threads,
               "n_gen": args.n_gen, "rail": col, "idle_W": idle_w, "idle_samples": idle_n,
               "before": before, "after": after, "build_commit": result.get("build_commit"),
               "reps": reps}
    with open(os.path.join(args.out, "summary.json"), "w") as f:
        json.dump(summary, f, indent=1)

    print("idle %s: %.3f W (%d samples)" % (col, idle_w, idle_n))
    print("rep  tok/s   power_W  J/token  net_J/token  samples")
    for i, r in enumerate(reps, 1):
        print("%3d  %6.2f  %7.3f  %7.4f  %11.4f  %7d" % (
            i, r["tokens_per_s"], r["power_W"], r["J_per_token"], r["net_J_per_token"], r["samples"]))
    print("throttled before %s after %s; %s -> %s" % (
        before["throttled"], after["throttled"], before["temp"], after["temp"]))
    if after["throttled"] != "throttled=0x0" or before["throttled"] != "throttled=0x0":
        print("WARNING: the board reported throttling; do not trust this run", file=sys.stderr)


if __name__ == "__main__":
    main()
```

For each repetition, the script computes the following values:

- `power_W`: the mean power of the rail sum inside the token-generation window.
- `J/token`: `power_W` multiplied by the window length, divided by the number of tokens. This is the energy the measured rails used per token, including the power the board draws when idle.
- `net_J/token`: the same calculation with the idle power subtracted first. This is the extra energy that token generation adds to an idle board.

The value that you need depends on the question that you want to answer. If the board is dedicated to the model and would otherwise be off, use `J/token`. If the board stays on anyway and you want the cost of the extra work, use `net_J/token`.

## Run the measurement

Check that the board is idle and not throttling, then run four threads and 128 generated tokens per repetition:

```bash
cd $HOME/pi-energy
uptime
vcgencmd get_throttled
python3 energy_per_token.py -m $HOME/models/qwen2.5-0.5b-instruct-q4_0.gguf -t 4 --out run_t4
```

The output is similar to:

```output
 05:56:03 up 28 days,  4:33,  2 users,  load average: 0.76, 1.64, 1.84
throttled=0x0
wrote 1085 samples to run_t4/power.csv
idle total_W: 1.720 W (420 samples)
rep  tok/s   power_W  J/token  net_J/token  samples
  1   24.31    5.256   0.2162       0.1455      188
  2   24.32    5.340   0.2196       0.1489      191
  3   24.20    5.329   0.2202       0.1491      188
throttled before throttled=0x0 after throttled=0x0; temp=47.2'C -> temp=49.9'C
```

The `samples` column shows how many power samples fall inside each window. Aim for at least 50, because a short window gives a noisy mean. To lengthen the window, increase the number of tokens generated in each repetition with the `-n` option of `energy_per_token.py`. The default is 128, so `-n 256` roughly doubles the window length and the number of samples.

The `throttled` values before and after the run have to both be `throttled=0x0`. If they aren't, the clock was reduced during the run and the result isn't valid.

The run directory contains `power.csv` with every sample. It also contains `llama-bench.stderr` with the timestamped progress lines, and `summary.json` with the per-repetition results. You can check every number later.

## Check the window alignment

Print the power around the generation windows to confirm that each window starts where power rises. The following command prints the mean power for each second, starting at the idle window. It marks with `G` each second whose midpoint falls inside a generation window:

```bash
python3 - <<'PY'
import csv, json
s = json.load(open("run_t4/summary.json"))
rows = list(csv.DictReader(open("run_t4/power.csv")))
t0 = float(rows[0]["time_s"])
gen = [(r["start"], r["start"] + r["seconds"]) for r in s["reps"]]
for sec in range(int(float(rows[-1]["time_s"]) - t0)):
    w = [float(x["total_W"]) for x in rows if t0 + sec <= float(x["time_s"]) < t0 + sec + 1]
    mid = t0 + sec + 0.5
    tag = "G" if any(a <= mid <= b for a, b in gen) else ""
    print("%3d s %5.2f W %s" % (sec, sum(w) / len(w), tag))
PY
```

The output is similar to:

```output
  0 s  1.75 W
  1 s  1.76 W
  2 s  1.77 W
  3 s  1.75 W
  4 s  1.75 W
  5 s  1.66 W
  6 s  1.60 W
  7 s  1.79 W
  8 s  1.67 W
  9 s  1.61 W
 10 s  1.92 W
 11 s  3.62 W
 12 s  5.27 W G
 13 s  5.33 W G
 14 s  5.12 W G
 15 s  5.22 W G
 16 s  5.36 W G
 17 s  5.36 W G
 18 s  5.28 W G
 19 s  5.36 W G
 20 s  5.33 W G
 21 s  5.36 W G
 22 s  5.36 W G
 23 s  5.29 W G
 24 s  5.36 W G
 25 s  5.34 W G
 26 s  5.31 W G
 27 s  3.91 W G
```

Seconds 0 to 9 are the idle window, at about 1.7 W. Power starts to rise at second 10, while `llama-bench` loads the model and runs its warmup, and the first `G` second follows. Within the generation windows, the rail sum stays between 5.1 W and 5.4 W. The last second is lower because it only partly overlaps the end of the run. 

If the `G` marks start before the power rises, or long after it, the timestamps and the power samples aren't aligned. The result in that case isn't valid.

## What you've accomplished and what's next

You've now measured joules per token for one setting. 

Next, you'll repeat the measurement across clock frequencies and thread counts to find the most efficient setting on your board.
