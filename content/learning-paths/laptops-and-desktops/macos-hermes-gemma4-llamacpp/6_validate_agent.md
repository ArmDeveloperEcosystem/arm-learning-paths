---
title: Validate autonomous tool-calling workflows
description: Test Nous Research Hermes Agent on macOS with a local Python bug-fixing task powered by Gemma 4 E4B and measure completion time and unified memory usage.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a local test workspace

Create a small test directory containing a Python script with two deliberate bugs so you can evaluate Hermes Agent's end-to-end tool-calling loop in a repeatable way:

```bash
mkdir -p ~/hermes-test-workspace
cd ~/hermes-test-workspace
```

Create `metrics_parser.py` with an intentional off-by-one divisor bug and a mismatched dictionary key name:

```bash
cat <<'EOF' > ~/hermes-test-workspace/metrics_parser.py
def average_latency(records):
    if not records:
        return 0.0
    total = sum(r["latency"] for r in records)
    return total / (len(records) - 1)

if __name__ == "__main__":
    sample = [
        {"endpoint": "/v1/models", "latency_ms": 12.0},
        {"endpoint": "/v1/chat/completions", "latency_ms": 48.0},
    ]
    print(f"Average latency: {average_latency(sample):.2f} ms")
EOF
```

Running it directly reveals the `KeyError: 'latency'` failure, alongside the division by `len(records) - 1` that skews averages and fails on single-item lists:

```bash
python3 metrics_parser.py
```

The output is similar to:

```output
Traceback (most recent call last):
  File "/Users/user/hermes-test-workspace/metrics_parser.py", line 12, in <module>
    print(f"Average latency: {average_latency(sample):.2f} ms")
                              ~~~~~~~~~~~~~~~^^^^^^^^
  File "/Users/user/hermes-test-workspace/metrics_parser.py", line 4, in average_latency
    total = sum(r["latency"] for r in records)
  File "/Users/user/hermes-test-workspace/metrics_parser.py", line 4, in <genexpr>
    total = sum(r["latency"] for r in records)
                ~^^^^^^^^^^^
KeyError: 'latency'
```

## Run the multi-step agent prompt

Run Hermes Agent inside `~/hermes-test-workspace` with Gemma 4 E4B active on `llama-server` (you can run interactively with `hermes` or pass the prompt directly with `hermes chat --cli`):

```bash
hermes chat --cli -q "Inspect the current directory, read metrics_parser.py, diagnose any bugs, fix metrics_parser.py, and run python3 metrics_parser.py to verify the output." --oneshot
```

{{% notice Note %}}
On the first turn of a new session, Hermes Agent sends an ~11K-token system prompt and tool schemas. With Metal GPU offloading active on Apple M4 Pro, cold prefill finishes in only a few seconds, and subsequent tool calls reuse the `llama-server` KV cache.
{{% /notice %}}

Observe how the agent runs the full tool loop:

1. Lists the workspace files and reads `metrics_parser.py`
2. Diagnoses both the `r["latency"]` key mismatch and the `len(records) - 1` divisor bug
3. Patches both lines in `metrics_parser.py`
4. Runs `python3 metrics_parser.py` and confirms `Average latency: 30.00 ms`

The output is similar to:

```output
Query: Inspect the current directory, read metrics_parser.py, diagnose any bugs,
fix metrics_parser.py, and run python3 metrics_parser.py to verify the output.
...
💻 $ ls -F  0.4s
📖 Read metrics_parser.py
...
🔧 Patch metrics_parser.py
│ metrics_parser.py
│ @@ -1,7 +1,7 @@
│  def average_latency(records):
│      if not records:
│          return 0.0
│ -    total = sum(r["latency"] for r in records)
│ +    total = sum(r["latency_ms"] for r in records)
│      return total / (len(records) - 1)
│
│  if __name__ == "__main__":
🔧 Patch metrics_parser.py
│ metrics_parser.py
│ @@ -2,7 +2,7 @@
│      if not records:
│          return 0.0
│      total = sum(r["latency_ms"] for r in records)
│ -    return total / (len(records) - 1)
│ +    return total / len(records)
│
│  if __name__ == "__main__":
│      sample = [
💻 $ python3 metrics_parser.py  0.8s
────────────────────────────────────────
☤ Hermes
The code was diagnosed with a KeyError (using "latency" instead of "latency_ms") and a potential ZeroDivisionError/logical error (dividing by N-1 instead of N). Fixes implemented:
1. Changed r["latency"] to r["latency_ms"] in average_latency.
2. Changed the denominator in average_latency from len(records) - 1 to len(records) to ensure the correct simple average is calculated and prevent division by zero for single-record inputs.
Execution of python3 metrics_parser.py verified the fix, producing the output: Average latency: 30.00 ms
────────────────────────────────────────

Session:        local-9c2f2bdee7306a37eeb5f3a92a7e2bdb92715a28f5c150922c632d689897d3b8
Duration:       47s
Messages:       12 (1 user, 10 tool calls)
```

## Monitor system resources while running

In a separate terminal while `llama-server` is running, inspect its resident set size (RSS), physical memory footprint, and overall system memory pressure on macOS:

```bash
ps -o pid=,rss=,comm= -p $(pgrep -n llama-server) | awk '{printf "PID=%s RSS=%.2f GiB CMD=%s\n", $1, $2/1048576, $3}'
top -l 1 -s 0 | grep PhysMem
footprint -p $(pgrep -n llama-server) | grep -E "Footprint:|mapped file|TOTAL"
```

The output is similar to:

```output
PID=65968 RSS=3.62 GiB CMD=./build/bin/llama-server
PhysMem: 23G used (9489M wired, 5828M compressor), 279M unused.
llama-server [65968]: 64-bit    Footprint: 955 MB (16384 bytes per page)
    0 B    2878 MB          0 B         22    mapped file
 955 MB    2884 MB      6608 KB       3991    TOTAL
```

With Gemma 4 E4B, the 64K context window, and `q8_0` KV cache active, `llama-server` uses about 955 MB of dirty physical footprint plus ~2.8–4.3 GB of clean memory-mapped weights. This fits comfortably on Apple silicon Macs with 16 GB or more of unified memory.

## Summary of observed agentic performance

The following table summarizes the observed run for Gemma 4 E4B on an Apple M4 Pro (24 GB unified memory, Metal GPU offload):

| Metric | Gemma 4 E4B (`Q4_0`, Metal) |
|---|---|
| Tool-call format reliability | Clean tool calls (`terminal`, `read_file`, `patch`) |
| Diagnosis and fix accuracy | Identified and patched both bugs before verification |
| Total wall-clock completion time | 47s (cold ~11K-token prefill + 10 tool calls across 12 messages) |
| `llama-server` memory (RSS and dirty footprint) | ~3.62 GiB RSS (`955 MB` dirty footprint + `2.8 GB` mapped file) |

## What you've accomplished and what's next

You compiled llama.cpp from source with Metal GPU offloading, Apple Accelerate, and Arm KleidiAI, downloaded Gemma 4 E4B from Hugging Face, served it with a 64K context window and `q8_0` KV cache, and connected Nous Research Hermes Agent to verify end-to-end autonomous bug diagnosis, patching, and verification.

From here, you can extend this setup by:

- Running `llama-server` as a `launchd` service: Create a user LaunchAgent plist in `~/Library/LaunchAgents/` so your local Metal inference server starts automatically at login.
- Connecting local MCP servers to Hermes Agent: Extend Hermes Agent's capabilities by attaching Model Context Protocol (MCP) servers for local Git repositories, databases, or documentation search.
- Experimenting with larger models or speculative decoding: Test larger quantized models on 24 GB–64 GB Macs, or evaluate llama.cpp speculative decoding with draft models to push decode speed even higher.
