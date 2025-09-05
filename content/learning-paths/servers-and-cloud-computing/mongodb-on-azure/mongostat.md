---
title: Monitor MongoDB with mongostat
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Monitoring MongoDB Performance using mongostat
This guide demonstrates real-time MongoDB monitoring using **mongostat** on Arm64 Azure virtual machines. It **shows low-latency, stable insert, query, update, and delete operations**, with consistent memory usage and network throughput, providing a quick health-and-performance overview during benchmarking.

## Monitor with mongostat — Terminal 3

```console
mongostat 2
```
**mongostat** gives a one-line summary every 2 seconds of inserts, queries, updates, deletes, memory use and network I/O. It’s your quick health-and-throughput dashboard during the test.

You should see an output similar to:
```output
insert query update delete getmore command dirty used flushes vsize  res qrw arw net_in net_out conn                time
    *0    *0     *0     *0       0     4|0  0.0% 0.0%       0 3.53G 140M 0|0 0|0   664b   52.7k    6 Sep  4 04:57:16.761
    50    *0     *0     *0       0     7|0  0.0% 0.0%       0 3.53G 141M 0|0 0|0  10.9k   57.8k   10 Sep  4 04:57:18.761
   404    13      4      4      71     8|0  0.0% 0.0%       0 3.53G 143M 0|0 0|0  96.3k    114k   10 Sep  4 04:57:20.761
     7    14      7      7     108     2|0  0.0% 0.0%       0 3.53G 143M 0|0 0|0  21.8k    118k   10 Sep  4 04:57:22.760
     6    12      6      6     112     0|0  0.0% 0.0%       0 3.53G 143M 0|0 0|0  21.9k    120k   10 Sep  4 04:57:24.760
     8    16      8      8     136     1|0  0.0% 0.0%       0 3.53G 144M 0|0 0|0  27.1k    137k   10 Sep  4 04:57:26.762
     5    10      5      5      93     2|0  0.0% 0.0%       0 3.54G 144M 0|0 0|0  18.2k    111k   11 Sep  4 04:57:28.760
     7    15      7      7     135     0|0  0.0% 0.0%       0 3.54G 144M 0|0 0|0  26.5k    139k   11 Sep  4 04:57:30.761
     5    11      5      5     102     1|0  0.0% 0.0%       0 3.54G 144M 0|0 0|0  19.7k    118k   11 Sep  4 04:57:32.761
     7    16     10      7     138     2|0  0.0% 0.0%       0 3.54G 145M 0|0 0|0  27.0k    143k   11 Sep  4 04:57:34.761
insert query update delete getmore command dirty used flushes vsize  res qrw arw net_in net_out conn                time
     5    10      5      5     104     1|0  0.0% 0.0%       0 3.54G 145M 0|0 0|0  20.1k    121k   11 Sep  4 04:57:36.761
     8    16      8      8     142     2|0  0.0% 0.0%       0 3.54G 145M 0|0 0|0  27.6k    144k   11 Sep  4 04:57:38.761
     5    11      5      5     114     1|0  0.0% 0.0%       0 3.54G 145M 0|0 0|0  21.3k    125k   11 Sep  4 04:57:40.760
     7    15      7      7     134     1|0  0.0% 0.0%       0 3.54G 145M 0|0 0|0  25.9k    141k   11 Sep  4 04:57:42.760
     5    11      5      5     126     1|0  0.0% 0.0%       0 3.54G 145M 0|0 0|0  23.6k    133k   11 Sep  4 04:57:44.761
     6    12      6      6     128     1|0  0.0% 0.0%       0 3.54G 145M 0|0 0|0  24.4k    136k   11 Sep  4 04:57:46.761
     6    13      6      6     140     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  26.5k    144k   11 Sep  4 04:57:48.762
     6    12      6      6     114     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  21.7k    128k   11 Sep  4 04:57:50.762
     7    15      7      7     164     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  30.4k    157k   11 Sep  4 04:57:52.761
     5    10      5      5     100     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  18.9k    118k   11 Sep  4 04:57:54.761
insert query update delete getmore command dirty used flushes vsize  res qrw arw net_in net_out conn                time
     8    16      8      8     182     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  34.0k    172k   11 Sep  4 04:57:56.761
     4     8      4      4      98     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  18.3k    116k   11 Sep  4 04:57:58.762
     9    18      9      9     198     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  36.4k    179k   11 Sep  4 04:58:00.760
     4     9      4      4      99     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  18.3k    117k   11 Sep  4 04:58:02.760
     8    17      8      8     202     1|0  0.0% 0.0%       0 3.54G 146M 0|0 0|0  37.0k    183k   11 Sep  4 04:58:04.762
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

## Explanation of mongostat Metrics

- **insert** - Number of document insert operations per second.
- **query** - Number of query operations (reads) per second.
- **update** - Number of document update operations per second.
- **delete** - Number of delete operations per second.
- **getmore** - Number of getMore operations per second (used when fetching more results from a cursor).
- **command** - Number of database commands executed per second (e.g., createIndex, count, aggregate).
  - command = number of regular commands | number of getLastError (GLE) commands
- **dirty/used** - Percentage of the WiredTiger cache that is dirty (not yet written to disk) and the percentage actively used.
- **flushes** - How many times data has been flushed to disk (per second).
- **vsize** - Virtual memory size of the mongod process.
- **res** - Resident memory size (actual RAM in use).
- **qrw arw** - Queued and active readers/writers:
  - `qrw` = queued read | queued write.
  - `arw` = active read | active write.
- **net_in/net_out** - Amount of network traffic coming into (net_in) and going out of (net_out) the database per second.
- **conn** - Number of active client connections.
- **time** - Timestamp of the sample.

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

## Benchmark summary on x86_64:
Here is a summary of the benchmark results collected on x86_64 **D4s_v6 Ubuntu Pro 24.04 LTS virtual machine**.

| insert | query | update | delete | getmore | command | dirty | used | flushes | vsize | res  | qrw  | arw  | net_in | net_out | conn | time                 |
|--------|-------|--------|--------|---------|---------|-------|------|---------|-------|------|------|------|--------|---------|------|----------------------|
| 249    | 2     | 0      | 0      | 0       | 11/0    | 0.0%  | 0.0% | 0       | 3.54G | 186M | 0/1  | 0/0  | 52.5k  | 66.9k   | 10   | Sep  4 05:52:36.629 |
| 208    | 18    | 8      | 8      | 120     | 5/0     | 0.0%  | 0.0% | 0       | 3.54G | 190M | 0/0  | 0/0  | 64.8k  | 134k    | 10   | Sep  4 05:52:38.629 |
| 5      | 10    | 5      | 5      | 95      | 1/0     | 0.0%  | 0.0% | 0       | 3.54G | 190M | 0/0  | 0/0  | 18.6k  | 110k    | 10   | Sep  4 05:52:40.629 |
| 8      | 17    | 8      | 8      | 152     | 1/0     | 0.0%  | 0.0% | 0       | 3.54G | 190M | 0/0  | 0/0  | 30.0k  | 144k    | 10   | Sep  4 05:52:42.630 |
| 9      | 18    | 9      | 9      | 153     | 2/0     | 0.0%  | 0.0% | 0       | 3.54G | 190M | 0/0  | 0/0  | 30.2k  | 150k    | 11   | Sep  4 05:52:46.629 |
| 8      | 17    | 8      | 8      | 161     | 1/0     | 0.0%  | 0.0% | 0       | 3.54G | 190M | 0/0  | 0/0  | 31.3k  | 158k    | 11   | Sep  4 05:52:52.629 |
| 7      | 15    | 7      | 7      | 150     | 2/0     | 0.0%  | 0.0% | 0       | 3.54G | 190M | 0/0  | 0/0  | 28.4k  | 148k    | 11   | Sep  4 05:52:56.628 |
| 8      | 17    | 8      | 8      | 170     | 1/0     | 0.0%  | 0.0% | 0       | 3.54G | 190M | 0/0  | 0/0  | 32.6k  | 164k    | 11   | Sep  4 05:52:58.629 |
| 8      | 17    | 8      | 8      | 179     | 1/0     | 0.0%  | 0.0% | 0       | 3.54G | 190M | 0/0  | 0/0  | 33.8k  | 168k    | 11   | Sep  4 05:53:02.631 |
| 9      | 18    | 9      | 9      | 193     | 1/0     | 0.0%  | 0.0% | 0       | 3.54G | 190M | 0/0  | 0/0  | 35.8k  | 177k    | 11   | Sep  4 05:53:12.628 |

### Highlights from Azure Ubuntu Pro 24.04 LTS Arm64 Benchmarking

When comparing the results on Arm64 vs x86_64 virtual machines:

- **Insert, Query, Update, Delete Rates:** Throughput remains consistent, with inserts and queries ranging from **5–50 ops/sec**, while updates and deletes generally track queries. A workload burst is observed with an **insert spike of 404**, highlighting MongoDB’s ability to handle sudden surges.
- **Memory Usage:** Resident memory remains stable at **141–145 MB**, with virtual memory steady at **3.53–3.54 GB**, confirming efficient memory allocation and stability.
- **Network Activity:** Network traffic scales proportionally with workload, with **net_in ranging ~18k–96k** and **net_out ~111k–143k**, showing balanced data flow.
- **Connections:** Active connections hold steady at **10–11**, indicating reliable support for concurrent client sessions without instability.
- **Command Execution & System Load:** Command executions (0–8) stay minimal, with dirty/used at **0.0%** and no flushes recorded, reflecting efficient internal resource handling.
- **Overall System Behavior:** MongoDB demonstrates stable throughput, predictable memory usage, and balanced network performance, while also showcasing resilience under workload bursts on Arm64.

  
You have now benchmarked MongoDB on an Azure Cobalt 100 Arm64 virtual machine and compared results with x86_64.
