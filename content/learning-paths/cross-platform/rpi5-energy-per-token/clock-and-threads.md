---
title: Compare energy per token across clock caps and thread counts
description: Cap the Raspberry Pi 5 CPU clock with cpufreq and measure llama.cpp joules per token at one, two, and four threads to find the most energy-efficient setting and the overhead of the power sampler.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cap the CPU clock

The Linux `cpufreq` interface sets the highest frequency that the CPU governor can choose. On the Raspberry Pi 5, all four cores share one frequency policy, `policy0`. Check the governor, the available frequencies, and the current maximum frequency:

```bash
cat /sys/devices/system/cpu/cpufreq/policy0/scaling_governor
cat /sys/devices/system/cpu/cpufreq/policy0/scaling_available_frequencies
cat /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq
```

The output is similar to:

```output
ondemand
1500000 1600000 1700000 1800000 1900000 2000000 2100000 2200000 2300000 2400000
2400000
```

The values are in kHz. The `ondemand` governor is the Raspberry Pi OS default. With `ondemand`, the CPU runs at the lowest frequency when idle and moves to `scaling_max_freq` under load. 

Writing a lower value to `scaling_max_freq` caps the clock:

```bash
echo 2000000 | sudo tee /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq
```

Confirm that the cap holds while llama.cpp generates tokens. To confirm, read the current frequency during a run:

```bash
$HOME/llama.cpp/build/bin/llama-bench -m $HOME/models/qwen2.5-0.5b-instruct-q4_0.gguf -p 0 -n 256 -r 1 -t 1 > /dev/null 2>&1 &
sleep 5; cat /sys/devices/system/cpu/cpufreq/policy0/scaling_cur_freq; wait
```

The expected output is:

```output
2000000
```

{{% notice Note %}}
If your governor isn't `ondemand`, for example `userspace` or `powersave`, the CPU doesn't move to `scaling_max_freq` under load. Set the governor with `echo ondemand | sudo tee /sys/devices/system/cpu/cpufreq/policy0/scaling_governor` before you run the sweep. Then, record the governor with your results.
{{% /notice %}}

## Run the sweep

The following loop measures three clock caps and three thread counts. Each run takes about 30 seconds, so the loop takes about five minutes:

```bash
cd $HOME/pi-energy
MODEL=$HOME/models/qwen2.5-0.5b-instruct-q4_0.gguf
for cap in 1500000 2000000 2400000; do
  echo $cap | sudo tee /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq > /dev/null
  for t in 1 2 4; do
    python3 energy_per_token.py -m $MODEL -t $t --out sweep_${cap}_t$t > sweep_${cap}_t$t.txt
  done
done
echo 2400000 | sudo tee /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq > /dev/null
```

The last line restores the default maximum frequency of 2.4 GHz.

Summarize the runs in one table:

```bash
python3 - <<'PY'
import glob, json, statistics as st
print("cap_GHz threads tok/s  power_W idle_W J/token net_J/token")
for f in sorted(glob.glob("sweep_*_t*/summary.json")):
    s = json.load(open(f))
    cap = int(f.split("_")[1]) / 1e6
    m = lambda k: st.fmean(r[k] for r in s["reps"])
    print("%7.1f %7d %6.2f %7.3f %6.3f %7.4f %11.4f" % (cap, s["threads"],
          m("tokens_per_s"), m("power_W"), s["idle_W"], m("J_per_token"), m("net_J_per_token")))
PY
```

The output is similar to:

```output
cap_GHz threads tok/s  power_W idle_W J/token net_J/token
    1.5       1  21.68   2.937  1.755  0.1355      0.0545
    1.5       2  26.12   4.044  1.629  0.1548      0.0924
    1.5       4  22.36   4.038  1.523  0.1805      0.1125
    2.0       1  26.87   3.414  1.589  0.1271      0.0679
    2.0       2  28.47   4.068  1.445  0.1429      0.0921
    2.0       4  23.27   4.227  1.558  0.1816      0.1146
    2.4       1  31.96   4.170  1.497  0.1305      0.0836
    2.4       2  31.49   4.833  1.564  0.1535      0.1038
    2.4       4  23.96   5.177  1.595  0.2162      0.1496
```

## Read the results

Your numbers will differ from these, but look for the following patterns: 

- How tokens per second changes with the thread count
- Whether a lower clock reduces the total J per token or only the net J per token

Also compare the `idle_W` column across runs. On the example board, the idle power moved between about 1.45 W and 1.76 W from run to run. Almost all of this change was on the Wi-Fi rail `3V7_WL_SW`. This is because the board was controlled over SSH through Wi-Fi. A change of this size can reorder settings that are close, so a single sweep isn't enough to rank them.

## Repeat the sweep before making a decision

The idle power and the temperature drift between runs. Repeat the sweep at least five times, alternating the order of the settings, before you trust a difference of a few percent. For the example board, five passes in alternating order gave the following means:

| Clock cap | Threads | Tokens per second | Rail sum during generation (W) | J per token | Net J per token |
|---|---|---|---|---|---|
| 1.5 GHz | 1 | 21.69 | 2.83 | 0.1305 | 0.0570 |
| 1.5 GHz | 2 | 26.09 | 4.11 | 0.1576 | 0.0945 |
| 1.5 GHz | 4 | 21.98 | 4.04 | 0.1839 | 0.1084 |
| 2.0 GHz | 1 | 26.93 | 3.46 | 0.1285 | 0.0684 |
| 2.0 GHz | 2 | 28.43 | 4.03 | 0.1418 | 0.0857 |
| 2.0 GHz | 4 | 23.38 | 4.29 | 0.1833 | 0.1148 |
| 2.4 GHz | 1 | 31.94 | 4.23 | 0.1323 | 0.0817 |
| 2.4 GHz | 2 | 31.51 | 4.82 | 0.1529 | 0.1020 |
| 2.4 GHz | 4 | 24.02 | 5.12 | 0.2131 | 0.1451 |

Across the five passes, the tokens per second of each setting varied by 1.2% or less (coefficient of variation). The J per token varied by 3.8% or less, and the net J per token by 6.7% or less. `get_throttled` returned `throttled=0x0` before and after every run, and the system-on-chip (SoC) temperature stayed between 45°C and 51°C.

Four threads is the worst setting at every clock cap. At 2.4 GHz, it costs 61% more energy per token than one thread while running 25% slower. This is despite four being the thread count that `llama-bench` uses by default on the board. Token generation for this model is limited by memory bandwidth. Extra threads therefore add power on `VDD_CORE` without adding tokens.

With one thread, the three clock caps are within 3% of each other in total J per token. That's inside the run-to-run variation, so this data doesn't rank them. A lower clock reduces the power, but each token takes longer. As a result, the board draws its idle power for longer too.

The net J per token does depend on the clock. One thread at 1.5 GHz uses 30% less net energy per token than one thread at 2.4 GHz. However, it generates 32% fewer tokens per second.

Most of the extra power during generation is on `VDD_CORE`. With one thread at 2.4 GHz, `VDD_CORE` rises from 0.42 W at idle to 2.62 W. This is about 85% of the rise of the rail sum.

Which setting is best depends on what you pay for. If the board runs only this model, the total energy per token is the decider. One thread at any clock cap is close to the best. If the board stays on for other work, the net energy per token is the decider. A lower clock saves energy at the cost of speed.

## Measure the cost of the sampler

The sampler competes with llama.cpp for the four cores. To see how much it costs, compare `llama-bench` alone with the same run under the full-rail sampler and the single-rail sampler, at 2.4 GHz:

```bash
cd $HOME/pi-energy
MODEL=$HOME/models/qwen2.5-0.5b-instruct-q4_0.gguf
for t in 1 4; do
  $HOME/llama.cpp/build/bin/llama-bench -m $MODEL -p 0 -n 128 -r 3 -t $t -o csv 2>/dev/null | tail -1 | awk -F, -v t=$t '{gsub(/"/, ""); printf "threads %d none %.2f tok/s\n", t, $(NF-1)}'
  python3 energy_per_token.py -m $MODEL -t $t --out over_full_t$t | awk -v t=$t '/^ +[0-9]+ / {s+=$2; n++} END {printf "threads %d full %.2f tok/s\n", t, s/n}'
  python3 energy_per_token.py -m $MODEL -t $t --rail VDD_CORE --out over_core_t$t | awk -v t=$t '/^ +[0-9]+ / {s+=$2; n++} END {printf "threads %d core %.2f tok/s\n", t, s/n}'
done
```

The output is similar to:

```output
threads 1 none 32.42 tok/s
wrote 1002 samples to over_full_t1/power.csv
threads 1 full 31.91 tok/s
wrote 3479 samples to over_core_t1/power.csv
threads 1 core 29.94 tok/s
threads 4 none 25.23 tok/s
wrote 1098 samples to over_full_t4/power.csv
threads 4 full 24.25 tok/s
wrote 3027 samples to over_core_t4/power.csv
threads 4 core 21.74 tok/s
```

The full-rail sampler reads about 40 samples per second. It slows token generation by about 2% with one thread and 4% with four threads. The single-rail sampler reads more often, about 100 to 140 samples per second. It costs more: about 8% with one thread and 14% with four threads. Over five alternating passes on the example board, the full-rail sampler slowed generation by 1.8% with one thread and 4.5% with four threads. The single-rail sampler slowed generation by 8.0% and 14.0%, respectively. Both samplers reported the same `VDD_CORE` power during generation, within 0.5%.

The full-rail sampler already gives more than 150 samples in each 128-token window. A faster sampler therefore adds overhead without making the average more precise. Use the single-rail mode only when you need to see short changes in power. Report the slowdown with your results.

## What you've accomplished

You've now compared joules per token across clock caps and thread counts. 

You can extend the Learning Path for any workload that prints a marker when its measured phase starts. For other models, replace the GGUF file and repeat the sweep.
