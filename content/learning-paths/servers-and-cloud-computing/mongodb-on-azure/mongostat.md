---
title: Monitor MongoDB with mongostat
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section you will use mongostat to monitor MongoDB in real time on an Azure Cobalt 100 Arm64 VM running Ubuntu 24.04 LTS. It provides a one‑line snapshot of operations per second, cache pressure, memory, and network throughput - perfect as a quick health and throughput dashboard while your workload runs.

## Monitor with mongostat - terminal 3

With the workload running, start `mongostat` in another terminal:

```console
mongostat 2
```
This prints a line every two seconds with key metrics. Press **Ctrl+C** to stop.

**Connect explicitly if needed.** If your instance is on a non‑default host or port, provide them:
```console
mongostat --host 127.0.0.1 --port 27017 2
```

## Example output

```output
insert query update delete getmore command dirty used flushes vsize  res qrw arw net_in net_out conn                time
     8    16      8      8     182     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  34.0k    172k   11 Sep  4 04:57:56.761
     4     8      4      4      98     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  18.3k    116k   11 Sep  4 04:57:58.762
     9    18      9      9     198     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  36.4k    179k   11 Sep  4 04:58:00.760
     4     9      4      4      99     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  18.3k    117k   11 Sep  4 04:58:02.760
     8    17      8      8     202     1|0  0.0% 0.0%       0 3.54G 146M 0|0  0|0  37.0k    183k   11 Sep  4 04:58:04.762
     4     9      4      4     103     2|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  19.0k    119k   11 Sep  4 04:58:06.760
     8    15      7      7     183     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  33.5k    171k   11 Sep  4 04:58:08.761
     5    11      5      5     126     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  23.1k    135k   11 Sep  4 04:58:10.760
     6    12      6      6     133     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  24.5k    138k   11 Sep  4 04:58:12.760
     7    14      7      7     190     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  34.1k    174k   11 Sep  4 04:58:14.761
insert query update delete getmore command dirty used flushes vsize  res qrw arw net_in net_out conn                time
     4     9      4      4     108     2|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  19.6k    123k   11 Sep  4 04:58:16.760
     9    18      9      9     220     2|0  0.0% 0.0%       0 3.54G 147M 0|0 0|0  39.7k    195k   11 Sep  4 04:58:18.760
     4     8      4      4     112     0|0  0.0% 0.0%       0 3.54G 147M 0|0 0|0  20.1k    125k   11 Sep  4 04:58:20.762
     7    15      7      7     179     1|0  0.0% 0.0%       0 3.54G 147M 0|0 0|0  32.4k    169k   11 Sep  4 04:58:22.760
     5    11      5      5     158     1|0  0.0% 0.0%       0 3.54G 147M 0|0 0|0  28.1k    155k   11 Sep  4 04:58:24.761
     5     9      4      4     117     2|0  0.0% 0.0%       0 3.54G 147M 0|0 0|0  21.1k    128k   11 Sep  4 04:58:26.761
     4     8      4      4     117     1|0  0.0% 0.0%       0 3.54G 147M 0|0 0|0  20.7k    127k    6 Sep  4 04:58:28.761
    *0    *0     *0     *0       0     0|0  0.0% 0.0%       0 3.54G 147M 0|0 0|0    98b   53.3k    6 Sep  4 04:58:30.762
    *0    *0     *0     *0       0     1|0  0.0% 0.0%       0 3.54G 147M 0|0 0|0    87b   51.0k    3 Sep  4 04:58:32.761
```

## Explanation of mongostat metrics

- **insert** - number of document insert operations per second
- **query** - number of query operations (reads) per second
- **update** - number of document update operations per second
- **delete** - number of delete operations per second
- **getmore** - number of getMore operations per second (used when fetching more results from a cursor)
- **command** - number of database commands executed per second (for example, createIndex, count, aggregate)
  - command = number of regular commands | number of getLastError (GLE) commands
- **dirty/used** - percentage of the WiredTiger cache that is dirty (not yet written to disk) and the percentage actively used
- **flushes** - how many times data has been flushed to disk (per second)
- **vsize** - virtual memory size of the mongod process
- **res** - resident memory size (actual RAM in use)
- **qrw arw** - queued and active readers/writers
  - `qrw` = queued read | queued write
  - `arw` = active read | active write
- **net_in/net_out** - amount of network traffic coming into (net_in) and going out of (net_out) the database per second
- **conn** - number of active client connections
- **time** - timestamp of the sample

## Benchmark summary on Arm64
Here is a summary of benchmark results collected on an Arm64 **D4ps_v6 Ubuntu Pro 24.04 LTS virtual machine**.

| insert | query | update | delete | getmore | command | dirty | used | flushes | vsize | res  | qrw  | arw  | net_in | net_out | conn | time                 |
|--------|-------|--------|--------|---------|---------|-------|------|---------|-------|------|------|------|--------|---------|------|----------------------|
| 50     | 0     | 0      | 0      | 0       | 7/0     | 0.0%  | 0.0% | 0       | 3.53G | 141M | 0/0  | 0/0  | 10.9k  | 57.8k   | 10   | Sep  4 04:57:18.761 |
| 404    | 13    | 4      | 4      | 71      | 8/0     | 0.0%  | 0.0% | 0       | 3.53G | 143M | 0/0  | 0/0  | 96.3k  | 114k    | 10   | Sep  4 04:57:20.761 |
| 7      | 14    | 7      | 7      | 108     | 2/0     | 0.0%  | 0.0% | 0       | 3.53G | 143M | 0/0  | 0/0  | 21.8k  | 118k    | 10   | Sep  4 04:57:22.760 |
| 6      | 12    | 6      | 6      | 112     | 0/0     | 0.0%  | 0.0% | 0       | 3.53G | 143M | 0/0  | 0/0  | 21.9k  | 120k    | 10   | Sep  4 04:57:24.760 |
| 8      | 16    | 8      | 8      | 136     | 1/0     | 0.0%  | 0.0% | 0       | 3.53G | 144M | 0/0  | 0/0  | 27.1k  | 137k    | 10   | Sep  4 04:57:26.762 |
| 5      | 10    | 5      | 5      | 93      | 2/0     | 0.0%  | 0.0% | 0       | 3.54G | 144M | 0/0  | 0/0  | 18.2k  | 111k    | 11   | Sep  4 04:57:28.760 |
| 7      | 15    | 7      | 7      | 135     | 0/0     | 0.0%  | 0.0% | 0       | 3.54G | 144M | 0/0  | 0/0  | 26.5k  | 139k    | 11   | Sep  4 04:57:30.761 |
| 5      | 11    | 5      | 5      | 102     | 1/0     | 0.0%  | 0.0% | 0       | 3.54G | 144M | 0/0  | 0/0  | 19.7k  | 118k    | 11   | Sep  4 04:57:32.761 |
| 7      | 16    | 10     | 7      | 138     | 2/0     | 0.0%  | 0.0% | 0       | 3.54G | 145M | 0/0  | 0/0  | 27.0k  | 143k    | 11   | Sep  4 04:57:34.761 |
| 5      | 10    | 5      | 5      | 104     | 1/0     | 0.0%  | 0.0% | 0       | 3.54G | 145M | 0/0  | 0/0  | 20.1k  | 121k    | 11   | Sep  4 04:57:36.761 |


### Highlights from Azure Ubuntu Pro 24.04 LTS Arm64 benchmarking

- **insert, query, update, delete rates:** throughput remains consistent, with inserts and queries ranging from **5–50 ops/sec**, while updates and deletes generally track queries; a workload burst is observed with an **insert spike of 404**, highlighting MongoDB’s ability to handle sudden surges
- **memory usage:** resident memory remains stable at **141–145 MB**, with virtual memory steady at **3.53–3.54 GB**, confirming efficient memory allocation and stability
- **network activity:** network traffic scales proportionally with workload, with **net_in ranging ~18k–96k** and **net_out ~111k–143k**, showing balanced data flow
- **connections:** active connections hold steady at **10–11**, indicating reliable support for concurrent client sessions without instability
- **command execution & system load:** command executions (0–8) stay minimal, with dirty/used at **0.0%** and no flushes recorded, reflecting efficient internal resource handling
- **overall system behavior:** MongoDB demonstrates stable throughput, predictable memory usage, and balanced network performance, while also showcasing resilience under workload bursts on Arm64

You have now successfully benchmarked MongoDB on an Azure Cobalt 100 Arm64 virtual machine.
