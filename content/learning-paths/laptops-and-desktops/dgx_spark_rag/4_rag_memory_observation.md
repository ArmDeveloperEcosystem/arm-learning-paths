---
title: Observe unified memory performance
weight: 6
layout: "learningpathall"
---

## Observe unified memory performance

In this section, you will learn how to monitor unified memory performance and GPU utilization on Grace–Blackwell systems during Retrieval-Augmented Generation (RAG) AI workloads. By observing real-time system memory and GPU activity, you will verify zero-copy data sharing and efficient hybrid AI inference enabled by the Grace–Blackwell unified memory architecture.


You will start from an idle system state, then progressively launch the RAG model server and run a query, while monitoring both system memory and GPU activity from separate terminals. This hands-on experiment demonstrates how unified memory enables both the Grace CPU and Blackwell GPU to access the same memory space without data movement, optimizing AI inference performance.

You will start from an idle system state, then progressively launch the model server and run a query, while monitoring both system memory and GPU activity from separate terminals.

Through these real-time observations, you will verify that the Grace–Blackwell unified memory architecture enables zero-copy data sharing, allowing both processors to access the same memory space without moving data.

Open two terminals on your GB10 system and use them as listed in the table below:

| **Terminal**         | **Observation Target** | **Purpose**                                        |
|----------------------|------------------------|----------------------------------------------------|
| Monitor Terminal 1 | System memory usage    | Observe memory allocation changes as processes run |
| Monitor Terminal 2 | GPU activity           | Track GPU utilization, power draw, and temperature |

You should also have your original terminals open that you used to run the `llama-server` and the RAG queries in the previous section. You will run these again and use the two new terminals for observation.


### Prepare for Unified Memory Observation Experiments

Ensure the RAG pipeline is stopped before starting the observation.

#### Terminal 1 - system memory observation

Run the Bash commands below in terminal 1 to print the free memory of the system:

```bash
while true; do
  echo -n "$(date '+[%Y-%m-%d %H:%M:%S]') "
  free -h | grep Mem: | awk '{printf "used=%s free=%s available=%s\n", $3, $4, $7}'
  sleep 1
done
```

The output is similar to the following:

```output
[2025-11-07 22:34:24] used=3.5Gi free=106Gi available=116Gi
[2025-11-07 22:34:25] used=3.5Gi free=106Gi available=116Gi
[2025-11-07 22:34:26] used=3.5Gi free=106Gi available=116Gi
[2025-11-07 22:34:27] used=3.5Gi free=106Gi available=116Gi
```

The printed fields are:

- `used` — Total memory currently utilized by all active processes.  
- `free` — Memory not currently allocated or reserved by the system.  
- `available` — Memory immediately available for new processes, accounting for reclaimable cache and buffers.

#### Terminal 2 – GPU status observation

Run the Bash commands below in terminal 2 to print the GPU statistics:

```bash
stdbuf -oL nvidia-smi --loop-ms=1000 \
  --query-gpu=timestamp,utilization.gpu,utilization.memory,power.draw,temperature.gpu,memory.used \
  --format=csv,noheader,nounits
```

The output is similar to the following:

```output
2025/11/07 22:38:05.114, 0, 0, 4.43, 36, [N/A]
2025/11/07 22:38:06.123, 0, 0, 4.46, 36, [N/A]
2025/11/07 22:38:07.124, 0, 0, 4.51, 36, [N/A]
2025/11/07 22:38:08.124, 0, 0, 4.51, 36, [N/A]
```

The format is not easy to read, but following the date and time, there are three key stats being reported: utilization, power, and temperature. The memory-related stats are not used on the GB10 system.

Here is an explanation of the fields:

| **Field**            | **Description**           | **Interpretation**                                                          |
|----------------------|---------------------------|-----------------------------------------------------------------------------|
| `timestamp`          | Time of data sampling     | Used to align GPU metrics with memory log timestamps                        |
| `utilization.gpu`    | GPU compute activity      | Peaks during token generation                                               |
| `utilization.memory` | GPU DRAM controller usage | Stays at 0% — Unified Memory bypasses the GDDR controller                   |
| `power.draw`         | GPU power consumption     | Rises during inference, falls after completion                              |
| `temperature.gpu`    | GPU temperature (°C)      | Slightly increases during workload, confirming GPU activity                 |
| `memory.used`        | GPU VRAM usage            | GB10 does not include separate VRAM; all data resides within Unified Memory |


### Run the llama-server

With the idle condition understood, start the `llama.cpp` REST server again in your original terminal, not the two new terminals being used for observation.

Here is the command:

```bash
cd ~/llama.cpp/build-gpu/
./bin/llama-server \
  -m ~/models/Llama-3.1-8B-gguf/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf \
  -ngl 40 --ctx-size 8192 \
  --port 8000 --host 0.0.0.0
```

Observe both monitoring terminals:

The output in monitor terminal 1 is similar to:

```output
[2025-11-07 22:50:27] used=3.5Gi free=106Gi available=116Gi
[2025-11-07 22:50:28] used=3.9Gi free=106Gi available=115Gi
[2025-11-07 22:50:29] used=11Gi free=98Gi available=108Gi
[2025-11-07 22:50:30] used=11Gi free=98Gi available=108Gi
[2025-11-07 22:50:31] used=11Gi free=98Gi available=108Gi
[2025-11-07 22:50:32] used=12Gi free=97Gi available=106Gi
[2025-11-07 22:50:33] used=12Gi free=97Gi available=106Gi
```

The output in monitor terminal 2 is similar to:

```output
2025/11/07 22:50:27.836, 0, 0, 4.39, 35, [N/A]
2025/11/07 22:50:28.836, 0, 0, 6.75, 36, [N/A]
2025/11/07 22:50:29.837, 6, 0, 11.47, 36, [N/A]
2025/11/07 22:50:30.837, 7, 0, 11.51, 36, [N/A]
2025/11/07 22:50:31.838, 6, 0, 11.50, 36, [N/A]
2025/11/07 22:50:32.839, 0, 0, 11.90, 36, [N/A]
2025/11/07 22:50:33.840, 0, 0, 10.85, 36, [N/A]
```

| **Terminal**       | **Observation**                                      | **Behavior**                                    |
|--------------------|------------------------------------------------------|-------------------------------------------------|
| Monitor Terminal 1 | used increases by about 8 GiB                             | Model weights loaded into shared Unified Memory |
| Monitor Terminal 2 | GPU utilization momentarily spikes and power rises | GPU initialization and model mapping            |


This confirms the model is resident in unified memory, which is visible by the increased system RAM usage.


## Execute the RAG Query

With the observation code and the `llama-server` still running, run the RAG query in another terminal: 

```bash
python3 ~/rag/rag_query_rest.py
```

The output in monitor terminal 1 is similar to:

```output
[2025-11-07 22:53:56] used=12Gi free=97Gi available=106Gi
[2025-11-07 22:53:57] used=12Gi free=97Gi available=106Gi
[2025-11-07 22:53:58] used=12Gi free=97Gi available=106Gi
[2025-11-07 22:53:59] used=13Gi free=96Gi available=106Gi
[2025-11-07 22:54:00] used=13Gi free=96Gi available=106Gi
[2025-11-07 22:54:01] used=13Gi free=96Gi available=106Gi
[2025-11-07 22:54:02] used=13Gi free=96Gi available=106Gi
[2025-11-07 22:54:03] used=13Gi free=96Gi available=106Gi
[2025-11-07 22:54:04] used=13Gi free=96Gi available=106Gi
[2025-11-07 22:54:05] used=13Gi free=96Gi available=106Gi
[2025-11-07 22:54:06] used=13Gi free=96Gi available=106Gi
[2025-11-07 22:54:07] used=13Gi free=96Gi available=106Gi
[2025-11-07 22:54:08] used=13Gi free=96Gi available=106Gi
[2025-11-07 22:54:09] used=13Gi free=96Gi available=106Gi
[2025-11-07 22:54:10] used=12Gi free=97Gi available=106Gi
[2025-11-07 22:54:11] used=12Gi free=97Gi available=106Gi
```

The output in monitor terminal 2 is similar to:

```output
2025/11/07 22:53:56.010, 0, 0, 11.24, 41, [N/A]
2025/11/07 22:53:57.010, 0, 0, 11.22, 41, [N/A]
2025/11/07 22:53:58.011, 0, 0, 11.20, 41, [N/A]
2025/11/07 22:53:59.012, 0, 0, 11.19, 41, [N/A]
2025/11/07 22:54:00.012, 0, 0, 11.33, 41, [N/A]
2025/11/07 22:54:01.013, 0, 0, 11.89, 41, [N/A]
2025/11/07 22:54:02.014, 96, 0, 31.53, 44, [N/A]
2025/11/07 22:54:03.014, 96, 0, 31.93, 45, [N/A]
2025/11/07 22:54:04.015, 96, 0, 31.98, 45, [N/A]
2025/11/07 22:54:05.015, 96, 0, 32.11, 46, [N/A]
2025/11/07 22:54:06.016, 96, 0, 32.01, 46, [N/A]
2025/11/07 22:54:07.016, 96, 0, 32.03, 46, [N/A]
2025/11/07 22:54:08.017, 96, 0, 32.14, 47, [N/A]
2025/11/07 22:54:09.017, 95, 0, 32.17, 47, [N/A]
2025/11/07 22:54:10.018, 0, 0, 28.87, 45, [N/A]
2025/11/07 22:54:11.019, 0, 0, 11.83, 44, [N/A]
```

| **Timestamp** | **GPU Utilization** | **GPU Power** | **System Memory (used)** | **Interpretation**                                    |
|---------------|---------------------|---------------|--------------------------|-------------------------------------------------------|
| 22:53:58      | 0%                  | 11 W          | 12 Gi                    | System idle                                           |
| 22:54:02      | 96%                 | 32 W          | 13 Gi                    | GPU performing generation while CPU handles retrieval |
| 22:54:09      | 96%                 | 32 W          | 13 Gi                    | Unified Memory data sharing in progress               |
| 22:54:10      | 0%                  | 12 W          | 12 Gi                    | Query completed, temporary buffers released           |


The GPU executes compute kernels with GPU utilization at 96%, without reading from GDDR or PCIe.

The `utilization.memory=0` and `memory.used=[N/A]` metrics are clear signs that data sharing, not data copying, is happening.

### Observe and interpret unified memory behavior

This experiment confirms the Grace–Blackwell Unified Memory architecture in action:
- The CPU and GPU share the same address space.
- No data transfers occur via PCIe.
- Memory activity remains stable while GPU utilization spikes.

Data does not move — computation moves to the data.

The Grace CPU orchestrates retrieval, and the Blackwell GPU performs generation, both operating within the same Unified Memory pool.

### Summary of unified memory behavior

| **Observation**                                    | **Unified Memory Explanation**                           |
|----------------------------------------------------|----------------------------------------------------------|
| Memory increases once (during model loading)       | Model weights are stored in shared Unified Memory        |
| Slight memory increase during query execution      | CPU temporarily stores context; GPU accesses it directly |
| GPU power increases during computation             | GPU cores are actively performing inference              |
| No duplicated allocation or data transfer observed | Data is successfully shared between the CPU and GPU      |


Through this experiment, you confirmed that:
- The Grace CPU efficiently handles retrieval, embedding, and orchestration tasks.
- The Blackwell GPU accelerates generation using data directly from Unified Memory.
- The system memory and GPU activity clearly demonstrate zero-copy data sharing.

This exercise highlights how the Grace–Blackwell architecture simplifies hybrid AI development by reducing complexity and improving efficiency for next-generation Arm-based AI systems.
