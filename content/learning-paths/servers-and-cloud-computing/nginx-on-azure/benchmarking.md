---
title: NGINX Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## NGINX Benchmarking by ApacheBench

To understand how your NGINX deployment performs under load, you can benchmark it using ApacheBench (ab). ApacheBench is a lightweight command-line tool for benchmarking HTTP servers. It measures performance metrics like requests per second, response time, and throughput under concurrent load.


1. Install ApacheBench

On **Ubuntu Pro 24.04 LTS**, ApacheBench is available as part of the `apache2-utils` package:
```console
sudo apt update
sudo apt install apache2-utils -y
```

2. Verify Installation

```console
ab -V
```
You should see output similar to:

```output
This is ApacheBench, Version 2.3 <$Revision: 1923142 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/
```

3. Basic Benchmark Syntax

The general syntax for running an ApacheBench test is:

```console
ab -n <total_requests> -c <concurrent_clients> <http://host:port/path>
```

Now run an example:

```console
ab -n 1000 -c 50 http://localhost/
```
This sends **1000 total requests** with **50 concurrent connections** to `http://localhost/`.

You should see a output similar to:
```output
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
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


Server Software:        nginx/1.24.0
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        890 bytes

Concurrency Level:      50
Time taken for tests:   0.032 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      1132000 bytes
HTML transferred:       890000 bytes
Requests per second:    31523.86 [#/sec] (mean)
Time per request:       1.586 [ms] (mean)
Time per request:       0.032 [ms] (mean, across all concurrent requests)
Transfer rate:          34848.65 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   0.1      1       1
Processing:     0    1   0.1      1       1
Waiting:        0    1   0.2      1       1
Total:          1    2   0.1      2       2

Percentage of the requests served within a certain time (ms)
  50%      2
  66%      2
  75%      2
  80%      2
  90%      2
  95%      2
  98%      2
  99%      2
 100%      2 (longest request)
```

### Interpret Benchmark Results:

ApacheBench outputs several metrics. Key ones to focus on include:

  - Requests per second: Average throughput.
  - Time per request: Latency per request.
  - Failed request: Should ideally be zero.
  - Transfer rate: Bandwidth used by the responses.

### Benchmark summary on Arm64:
Here is a summary of benchmark results collected on an Arm64 **D4ps_v6 Ubuntu Pro 24.04 LTS virtual machine**.

| **Category**              | **Metric**                                      | **Value**   |
|---------------------------|-------------------------------------------------|-------------------------------|
| **General Info**          | Server Software                                  | nginx/1.24.0                  |
|                           | Server Hostname                                  | localhost                     |
|                           | Server Port                                      | 80                            |
|                           | Document Path                                    | /                             |
|                           | Document Length                                  | 890 bytes                     |
| **Test Setup**            | Concurrency Level                                | 50                            |
|                           | Time Taken for Tests                             | 0.032 sec                     |
|                           | Complete Requests                                | 1000                          |
|                           | Failed Requests                                  | 0                             |
| **Transfer Stats**        | Total Transferred                                | 1,132,000 bytes               |
|                           | HTML Transferred                                 | 890,000 bytes                 |
|                           | Requests per Second                              | 31,523.86 [#/sec]             |
|                           | Time per Request (mean)                          | 1.586 ms                      |
|                           | Time per Request (across all)                    | 0.032 ms                      |
|                           | Transfer Rate                                    | 34,848.65 KB/sec              |
| **Connection Times (ms)** | Connect (min / mean / stdev / median / max)      | 0 / 1 / 0.1 / 1 / 1          |
|                           | Processing (min / mean / stdev / median / max)   | 0 / 1 / 0.1 / 1 / 1          |
|                           | Waiting (min / mean / stdev / median / max)      | 0 / 1 / 0.2 / 1 / 1          |
|                           | Total (min / mean / stdev / median / max)        | 1 / 2 / 0.1 / 2 / 2          |

### Analysis of results from NGINX benchmarking on Arm-based Azure Cobalt-100  

These benchmark results highlight the strong performance characteristics of NGINX running on Arm64-based Azure VMs (such as the D4ps_v6 instance type):

- High Requests Per second(31,523.86 requests/sec), demonstrating high throughput under concurrent load.
- Response time per request averaged **1.586 ms**, indicating efficient handling of requests with minimal delay.
- **Zero failed requests**, confirming stability and reliability during testing.
- Consistently low **connection and processing times** (mean ≈ 1 ms), ensuring smooth performance.

Overall, these results illustrate that NGINX on Arm64 machines provides a highly performant solution for web workloads on Azure. You can also use the same benchmarking framework to compare results on equivalent x86-based Azure instances, which provides useful insight into relative performance and cost efficiency across architectures.
