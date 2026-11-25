---
title: Validate autonomous tool-calling workflows
description: Test Nous Research Hermes Agent on NVIDIA DGX Spark with a local Python bug-fixing task powered by Gemma 4 E4B and measure completion time and GB10 memory usage.
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
  File "/home/user/hermes-test-workspace/metrics_parser.py", line 12, in <module>
    print(f"Average latency: {average_latency(sample):.2f} ms")
                              ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/hermes-test-workspace/metrics_parser.py", line 4, in average_latency
    total = sum(r["latency"] for r in records)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/hermes-test-workspace/metrics_parser.py", line 4, in <genexpr>
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
On the first turn of a new session, Hermes Agent sends an ~11K-token system prompt and tool schemas. With Blackwell GB10 GPU offloading active (`~7,460 tok/s` prefill with `q8_0` KV cache), cold prefill finishes in ~2–3 seconds, and subsequent tool calls reuse the `llama-server` KV cache.
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
💻 $ ls -R  0.2s
📖 Read metrics_parser.py
...
🔧 Patch metrics_parser.py
│ metrics_parser.py
│ @@ -1,8 +1,8 @@
│  def average_latency(records):
│      if not records:
│          return 0.0
│ -    total = sum(r["latency"] for r in records)
│ -    return total / (len(records) - 1)
│ +    total = sum(r["latency_ms"] for r in records)
│ +    return total / len(records)
│
│  if __name__ == "__main__":
│      sample = [
💻 $ python3 metrics_parser.py

────────────────────────────────────────
☤ Hermes
The directory inspection showed only metrics_parser.py. Analysis of the file identified two bugs:
1. KeyError: The function accessed r["latency"], but the sample data provided r["latency_ms"].
2. Incorrect average calculation: The function divided by len(records) - 1 instead of len(records).
The function was updated to use the correct key and calculate the mean correctly.
Execution of python3 metrics_parser.py returned: Average latency: 30.00 ms
────────────────────────────────────────

Session:        local-648f77d8b520533c510593b1ed77bdcfcbace6d9928a63ce0364b817b58e55f9
Duration:       38s
Messages:       10 (1 user, 8 tool calls)
```

## Monitor system resources while running

In a separate terminal while `llama-server` is running, inspect its resident set size (RSS), GB10 GPU memory allocation, and overall unified memory usage:

```bash
ps -o pid=,rss=,comm= -p $(pgrep -n llama-server) | awk '{printf "PID=%s RSS=%.2f GiB CMD=%s\n", $1, $2/1048576, $3}'
nvidia-smi --query-compute-apps=pid,process_name,used_memory --format=csv
free -h
```

The output is similar to:

```output
PID=1223023 RSS=3.03 GiB CMD=llama-server
pid, process_name, used_gpu_memory [MiB]
1223023, ./build/bin/llama-server, 4088 MiB
```

With Gemma 4 E4B, the 64K context window, and `q8_0` KV cache active, `llama-server` uses ~4,088 MiB (~4.0 GiB) of GB10 unified GPU memory (`3.03 GiB` process RSS), leaving over 115 GB available on a dedicated 128 GB NVIDIA DGX Spark.

## Summary of observed agentic performance

The following table summarizes the observed run for Gemma 4 E4B on NVIDIA DGX Spark (Grace Blackwell GB10, 128 GB unified memory, CUDA `sm_121a` offload):

| Metric | Gemma 4 E4B (`Q4_0`, GB10 CUDA) |
|---|---|
| Tool-call format reliability | Clean tool calls (`terminal`, `read_file`, `patch`) |
| Diagnosis and fix accuracy | Identified and patched both bugs cleanly before verification |
| Total wall-clock completion time | 38s (cold ~11K-token prefill + 8 tool calls across 10 messages) |
| `llama-server` memory usage | ~3.03 GiB RSS / `4,088 MiB` GPU memory in `nvidia-smi` |

## What you've accomplished and what's next

You compiled llama.cpp from source with CUDA 13 Blackwell (`sm_121a`), Armv9.2 Grace CPU flags, and Arm KleidiAI, downloaded Gemma 4 E4B, 26B-A4B MoE, and 31B from Hugging Face, served Gemma 4 E4B with full GB10 GPU offload and a 64K `q8_0` KV cache context window, and connected Nous Research Hermes Agent to verify end-to-end autonomous bug diagnosis, patching, and verification.

From here, you can extend this setup by:

- Switching Hermes Agent to Gemma 4 26B-A4B (MoE): Restart `llama-server` with `-m ./models/gemma-4-26B-A4B-it-Q4_0.gguf` and run `hermes config set model.default ./models/gemma-4-26B-A4B-it-Q4_0.gguf` to gain higher reasoning capacity at 61.72 tok/s GPU decode speed.
- Running `llama-server` as a `systemd` service: Create a user or system `systemd` unit so your local inference server starts automatically on boot and restarts cleanly if needed.
- Connecting local MCP servers to Hermes Agent: Extend Hermes Agent's capabilities by attaching Model Context Protocol (MCP) servers for local Git repositories, databases, or documentation search.
