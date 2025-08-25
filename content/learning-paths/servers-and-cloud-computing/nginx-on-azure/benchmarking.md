---
title: Nginx Benchmarking
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Nginx Benchmarking by ApacheBench

**ApacheBench (ab)** is a lightweight command-line tool for benchmarking HTTP servers. It measures performance metrics like requests per second, response time, and throughput under concurrent load.

1. Install ApacheBench

```console
sudo dnf install httpd-tools
```

2. Verify Installation

```console
ab -V
```
You should see an output similar to:

```output
This is ApacheBench, Version 2.3 <$Revision: 1923142 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/
```

3. Basic Benchmark Command Syntax

```console
ab -n <total_requests> -c <concurrent_clients> <http://host:port/path>
```
Example:

```console
ab -n 1000 -c 50 http://localhost/
```
This sends **1000 total requests** with **50 concurrent connections** to `http://localhost/`.

You should see an output similar to:
```output
This is ApacheBench, Version 2.3 <$Revision: 1923142 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        nginx/1.25.4
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        615 bytes

Concurrency Level:      50
Time taken for tests:   0.049 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      848000 bytes
HTML transferred:       615000 bytes
Requests per second:    20352.51 [#/sec] (mean)
Time per request:       2.457 [ms] (mean)
Time per request:       0.049 [ms] (mean, across all concurrent requests)
Transfer rate:          16854.42 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   0.2      1       2
Processing:     0    1   0.2      1       2
Waiting:        0    1   0.3      1       2
Total:          1    2   0.1      2       3

Percentage of the requests served within a certain time (ms)
  50%      2
  66%      2
  75%      2
  80%      2
  90%      2
  95%      3
  98%      3
  99%      3
 100%      3 (longest request)
```

### Benchmark Results Table Explained:

- **Requests per second** – How many requests were served per second.
- **Time per request** – Average latency per request.
- **Transfer rate** – Data throughput.
- **Connection times** – Breakdown of min/mean/max connect, processing, and total times.
- **Percentage served** – Percentile distribution of response times.

### Benchmark summary on x86_64:

The following benchmark results are collected on two different x86_64 environments: a **Docker container running Azure Linux 3.0 hosted on a D4s_v6 Ubuntu-based Azure virtual machine**, and a **D4s_v4 Azure virtual machine created from the Azure Linux 3.0 image published by Ntegral Inc**.

| **Category**              | **Metric**                                     | **Value on Virtual Machine**     | **Value on Docker** |
| ------------------------- | ---------------------------------------------- | ------------------- | ------------------- |
| **General Info**          | Server Software                                | nginx/1.25.4        | nginx/1.25.4        |
|                           | Server Hostname                                | localhost           | localhost           |
|                           | Server Port                                    | 80                  | 80                  |
|                           | Document Path                                  | /                   | /                   |
|                           | Document Length                                | 615 bytes           | 615 bytes           |
| **Test Setup**            | Concurrency Level                              | 50                  | 50                  |
|                           | Time Taken for Tests                           | 0.049 sec           | 0.027 sec           |
|                           | Complete Requests                              | 1000                | 1000                |
|                           | Failed Requests                                | 0                   | 0                   |
| **Transfer Stats**        | Total Transferred                              | 848000 bytes        | 848000 bytes        |
|                           | HTML Transferred                               | 615000 bytes        | 615000 bytes        |
|                           | Requests per Second                            | 20,352.51 [#/sec]   | 37,510.78 [#/sec]   |
|                           | Time per Request (mean)                        | 2.457 ms            | 1.333 ms            |
|                           | Time per Request (across all)                  | 0.049 ms            | 0.027 ms            |
|                           | Transfer Rate                                  | 16,854.42 KB/sec    | 31,063.62 KB/sec    |
| **Connection Times (ms)** | Connect (min / mean / stdev / median / max)    | 0 / 1 / 0.2 / 1 / 2 | 0 / 0 / 0.1 / 0 / 1 |
|                           | Processing (min / mean / stdev / median / max) | 0 / 1 / 0.2 / 1 / 2 | 0 / 1 / 0.2 / 1 / 1 |
|                           | Waiting (min / mean / stdev / median / max)    | 0 / 1 / 0.3 / 1 / 2 | 0 / 1 / 0.2 / 1 / 1 |
|                           | Total (min / mean / stdev / median / max)      | 1 / 2 / 0.1 / 2 / 3 | 1 / 1 / 0.1 / 1 / 2 |


### Benchmark summary on Arm64:

The following benchmark results are collected on two different Arm64 environments: a **Docker container running Azure Linux 3.0 hosted on a D4ps_v6 Ubuntu-based Azure virtual machine**, and a **D4ps_v6 Azure virtual machine created from the Azure Linux 3.0 custom image using the AArch64 ISO**.

| **Category**              | **Metric**                                      | **Value on Virtual Machine**   | **Value on Docker**      |
|---------------------------|--------------------------------------------------|--------------------------|---------------------------|
| **General Info**          | Server Software                                  | nginx/1.25.4             | nginx/1.25.4              |
|                           | Server Hostname                                  | localhost                | localhost                 |
|                           | Server Port                                      | 80                       | 80                        |
|                           | Document Path                                    | /                        | /                         |
|                           | Document Length                                  | 615 bytes                | 615 bytes                 |
| **Test Setup**            | Concurrency Level                                | 50                       | 50                        |
|                           | Time Taken for Tests                             | 0.032 sec                | 0.025 sec                 |
|                           | Complete Requests                                | 1000                     | 1000                      |
|                           | Failed Requests                                  | 0                        | 0                         |
| **Transfer Stats**        | Total Transferred                                | 848000 bytes             | 848000 bytes              |
|                           | HTML Transferred                                 | 615000 bytes             | 615000 bytes              |
|                           | Requests per Second                              | 30,876.59 [#/sec]        | 40,698.38 [#/sec]         |
|                           | Time per Request (mean)                          | 1.619 ms                 | 1.229 ms                  |
|                           | Time per Request (across all)                    | 0.032 ms                 | 0.025 ms                  |
|                           | Transfer Rate                                    | 25,569.67 KB/sec         | 33,703.35 KB/sec          |
| **Connection Times (ms)** | Connect (min / mean / stdev / median / max)     | 0 / 1 / 0.1 / 1 / 1      | 0 / 0 / 0.1 / 0 / 1       |
|                           | Processing (min / mean / stdev / median / max)  | 0 / 1 / 0.1 / 1 / 2      | 0 / 1 / 0.1 / 1 / 1       |
|                           | Waiting (min / mean / stdev / median / max)     | 0 / 1 / 0.2 / 1 / 1      | 0 / 1 / 0.1 / 1 / 1       |
|                           | Total (min / mean / stdev / median / max)       | 1 / 2 / 0.1 / 2 / 2      | 1 / 1 / 0.1 / 1 / 1       |


### Highlights from Azure Linux Arm64 Benchmarking

- Achieved **30,876.59 requests/sec**, significantly outperforming x86_64 (20,352.51 requests/sec).
- Response time per request averaged **1.619 ms**, indicating high efficiency under 50 concurrent connections.
- **Zero failed requests**, ensuring full stability during the stress test.
- Consistently low **connection and processing times** (mean ≈ 1 ms).
