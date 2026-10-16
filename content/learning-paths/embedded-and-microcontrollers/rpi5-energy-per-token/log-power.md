---
title: Log rail power to a CSV file
description: Write a small Python sampler that reads the Raspberry Pi 5 PMIC in a loop, time stamps every sample, and saves the power of each rail to a CSV file.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create the sampler

To compute energy you need power samples with a time stamp on each one, so that you can later select only the samples that fall inside a measurement window.

Create a working directory:

```bash
mkdir -p $HOME/pi-energy
cd $HOME/pi-energy
```

Use a text editor to save the following code as `pmic_sampler.py` in that directory:

```python
#!/usr/bin/env python3
"""Log Raspberry Pi 5 PMIC rail power to a CSV file until stopped.

Every sample runs `vcgencmd pmic_read_adc`, pairs each rail's current (_A)
with its voltage (_V), and writes one CSV row: time, total watts, then watts
per rail. With --rail NAME only that rail is read (two short reads per
sample), which is several times faster.
"""
import argparse
import re
import signal
import subprocess
import sys
import time

LINE = re.compile(r"^\s*(\S+)_([AV]) (?:current|volt)\(\d+\)=([-0-9.]+)[AV]\s*$")


def read_adc(channel=None):
    cmd = ["vcgencmd", "pmic_read_adc"]
    if channel:
        cmd.append(channel)
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    amps, volts = {}, {}
    for line in out.splitlines():
        m = LINE.match(line)
        if m:
            name, kind, value = m.group(1), m.group(2), float(m.group(3))
            (amps if kind == "A" else volts)[name] = value
    return amps, volts


def rail_power(rail=None):
    if rail:
        amps, _ = read_adc(rail + "_A")
        _, volts = read_adc(rail + "_V")
    else:
        amps, volts = read_adc()
    return {n: amps[n] * volts[n] for n in sorted(amps) if n in volts}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("csv", help="output CSV file")
    ap.add_argument("--rail", help="read only this rail, for example VDD_CORE")
    ap.add_argument("--duration", type=float, default=0,
                    help="stop after this many seconds (default: run until stopped)")
    args = ap.parse_args()

    stop = []
    signal.signal(signal.SIGTERM, lambda *_: stop.append(1))
    signal.signal(signal.SIGINT, lambda *_: stop.append(1))

    rails = sorted(rail_power(args.rail))
    if not rails:
        sys.exit("no rail has both a current and a voltage reading")
    t_end = time.time() + args.duration if args.duration else None
    n = 0
    with open(args.csv, "w", buffering=1) as f:
        f.write("time_s,total_W," + ",".join(r + "_W" for r in rails) + "\n")
        while not stop and (t_end is None or time.time() < t_end):
            t0 = time.time()
            p = rail_power(args.rail)
            t1 = time.time()
            # time stamp the middle of the read
            f.write("%.4f,%.4f,%s\n" % ((t0 + t1) / 2, sum(p.values()),
                                        ",".join("%.4f" % p.get(r, 0.0) for r in rails)))
            n += 1
    print("wrote %d samples to %s" % (n, args.csv), file=sys.stderr)


if __name__ == "__main__":
    main()
```

The script calls `vcgencmd pmic_read_adc`, matches each rail's current line with its voltage line, and writes one row per sample:

- `time_s` is the wall-clock time, in seconds, at the middle of the read.
- `total_W` is the sum of the power of all rails that report both a current and a voltage.
- One column per rail follows, in watts.

The script stops cleanly when it receives `Ctrl+C` or a `kill` signal, or after `--duration` seconds.

## Log an idle board

Make sure nothing else is running, then log ten seconds of idle power:

```bash
python3 pmic_sampler.py idle.csv --duration 10
head -3 idle.csv | cut -c1-120
```

The output is similar to:

```output
wrote 404 samples to idle.csv
time_s,total_W,0V8_AON_W,0V8_SW_W,1V1_SYS_W,1V8_SYS_W,3V3_ADC_W,3V3_DAC_W,3V3_SYS_W,3V7_WL_SW_W,DDR_VDD2_W,DDR_VDDQ_W,HD
1791953741.3029,1.8872,0.0024,0.2130,0.1940,0.2904,0.0012,0.0000,0.3165,0.3327,0.0000,0.0000,0.1275,0.4094
1791953741.3292,1.7417,0.0023,0.2150,0.1941,0.2891,0.0024,0.0000,0.1841,0.3256,0.0000,0.0000,0.1287,0.4003
```

Count the samples and compute the mean power with a one-line Python command:

```bash
python3 -c "import csv,statistics as s; r=list(csv.DictReader(open('idle.csv'))); print(len(r), 'samples', round(s.fmean(float(x['total_W']) for x in r), 3), 'W')"
```

The output is similar to:

```output
404 samples 1.752 W
```

## Sample one rail faster

If you only need one rail, pass `--rail`. The sampler then reads only that rail's current and voltage channels:

```bash
python3 pmic_sampler.py core.csv --rail VDD_CORE --duration 10
python3 -c "import csv; r=list(csv.DictReader(open('core.csv'))); print(len(r), 'samples')"
```

The output is similar to:

```output
wrote 1386 samples to core.csv
1386 samples
```

{{% notice Note %}}
The sampler runs on the same four Cortex-A76 cores as the workload you measure, and each sample starts a `vcgencmd` process. Logging at a higher rate costs more CPU time. The last section of this Learning Path measures how much this slows down llama.cpp, so that you can decide whether the overhead matters for your measurement.
{{% /notice %}}

You can now log power with time stamps. In the next section, you line these samples up with llama.cpp token generation and compute joules per token.
