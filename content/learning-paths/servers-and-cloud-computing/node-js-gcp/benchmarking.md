---
title: Node.js Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Node.js Benchmarking by Autocannon

After validating that Node.js is installed and your HTTP server is running, you can benchmark it using **Autocannon**.

### Install Autocannon
**Autocannon** is a fast HTTP/1.1 benchmarking tool for Node.js, used to measure server throughput, latency, and request handling under concurrent load.

```console
npm install -g autocannon
```

### Start Your Node.js HTTP Server

If your sample HTTP server is not already running from the last section, you can start it by typing:
```console
export MY_NODE=`which node`
sudo ${MY_NODE} app.js &
```

Server should be listening on port 80 in the background:

```output
Server running at http://0.0.0.0:80/
```

### Run a Basic Benchmark (Local)

```console
autocannon -c 100 -d 10 http://localhost:80
```
- `-c 100` → 100 concurrent connections
- `-d 10` → duration 10 seconds
- URL → endpoint to test

You should see an output similar to:
```output
Running 10s test @ http://localhost:80
100 connections


┌─────────┬──────┬──────┬───────┬──────┬─────────┬─────────┬───────┐
│ Stat    │ 2.5% │ 50%  │ 97.5% │ 99%  │ Avg     │ Stdev   │ Max   │
├─────────┼──────┼──────┼───────┼──────┼─────────┼─────────┼───────┤
│ Latency │ 1 ms │ 1 ms │ 2 ms  │ 2 ms │ 1.06 ms │ 0.41 ms │ 28 ms │
└─────────┴──────┴──────┴───────┴──────┴─────────┴─────────┴───────┘
┌───────────┬─────────┬─────────┬─────────┬────────┬───────────┬──────────┬─────────┐
│ Stat      │ 1%      │ 2.5%    │ 50%     │ 97.5%  │ Avg       │ Stdev    │ Min     │
├───────────┼─────────┼─────────┼─────────┼────────┼───────────┼──────────┼─────────┤
│ Req/Sec   │ 66,175  │ 66,175  │ 70,847  │ 72,191 │ 70,713.61 │ 1,616.86 │ 66,134  │
├───────────┼─────────┼─────────┼─────────┼────────┼───────────┼──────────┼─────────┤
│ Bytes/Sec │ 12.8 MB │ 12.8 MB │ 13.7 MB │ 14 MB  │ 13.7 MB   │ 313 kB   │ 12.8 MB │
└───────────┴─────────┴─────────┴─────────┴────────┴───────────┴──────────┴─────────┘

Req/Bytes counts sampled once per second.
# of samples: 10

707k requests in 10.02s, 137 MB read
```

### Understanding Node.js benchmark metrics and results with Autocannon

- **Avg (Average Latency)** → The mean time it took for requests to get a response.
- **Stdev (Standard Deviation)** → How much individual request times vary around the average. Smaller numbers mean more consistent response times.
- **Min (Minimum Latency)** → The fastest request observed during the test.

### Benchmark summary on x86_64
To compare the benchmark results, the following results were collected by running the same benchmark on a `x86 - c4-standard-4` (4 vCPUs, 15 GB Memory) x86_64 VM in GCP, running SUSE:

Latency (ms):

| Metric   | 2.5% | 50% (Median) | 97.5% | 99% | Avg    | Stdev  | Max   |
|----------|------|--------------|-------|-----|--------|--------|-------|
| Latency  | 0    | 1            | 2     | 2   | 0.73   | 0.87   | 104   |

Throughput:

| Metric     | 1%     | 2.5%   | 50%     | 97.5%   | Avg      | Stdev     | Min     |
|------------|--------|--------|---------|---------|----------|-----------|---------|
| Req/Sec    | 70,143 | 70,143 | 84,479  | 93,887  | 84,128   | 7,547.18  | 70,095 |
| Bytes/Sec  | 13.6 MB| 13.6 MB| 16.4 MB | 18.2 MB | 16.3 MB  | 1.47 MB   | 13.6 MB|

### Benchmark summary on Arm64
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

Latency (ms):

| Metric   | 2.5% | 50% (Median) | 97.5% | 99% | Avg  | Stdev | Max  |
|----------|------|--------------|-------|-----|------|-------|------|
| Latency  | 1    | 1            | 3     | 3   | 1.2  | 0.62  | 24   |

Throughput:

| Metric     | 1%     | 2.5%   | 50%     | 97.5%   | Avg      | Stdev    | Min     |
|------------|--------|--------|---------|---------|----------|----------|---------|
| Req/Sec    | 45,279 | 45,279 | 54,719  | 55,199  | 53,798.4 | 2,863.96 | 45,257 |
| Bytes/Sec  | 8.78 MB| 8.78 MB| 10.6 MB | 10.7 MB | 10.4 MB  | 557 kB   | 8.78 MB |

### Node.js performance benchmarking comparison on Arm64 and x86_64
When you compare the benchmarking results, you will notice that on the Google Axion C4A Arm-based instances:

- Average latency is very low (~1.2 ms) with consistent response times.  
- Maximum latency spikes are rare, reaching up to 24 ms.  
- The server handles high throughput, averaging ~53,798 requests/sec.  
- Data transfer rate averages 10.4 MB/sec, demonstrating efficient performance under load.
