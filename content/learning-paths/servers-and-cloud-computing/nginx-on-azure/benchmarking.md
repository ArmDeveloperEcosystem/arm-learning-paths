---
title: NGINX Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark NGINX with ApacheBench (ab) on Ubuntu Pro 24.04 LTS

Use ApacheBench (**ab**) to measure NGINX performance on your Arm64 Azure VM. This section shows you how to install the tool, run a basic benchmark, interpret key metrics, and review a sample result from an Azure **D4ps_v6** instance.

## Install ApacheBench

On **Ubuntu Pro 24.04 LTS**, ApacheBench is provided by the **apache2-utils** package:

```console
sudo apt update
sudo apt install -y apache2-utils
```

Verify the installation:

```console
ab -V
```

Expected output:

```output
This is ApacheBench, Version 2.3 <$Revision: 1923142 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/
```

## Run a basic benchmark

The general syntax for running an ApacheBench test is:

```console
ab -n <total_requests> -c <concurrent_clients> <http://host:port/path>
```

Example (1,000 requests, 50 concurrent, to the NGINX default page on localhost):

```console
ab -n 1000 -c 50 http://localhost/
```

This command sends 1,000 total requests with 50 concurrent connections to `http://localhost/`.

Sample output:

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

## Interpret benchmark results

ApacheBench produces a variety of metrics, but the most useful ones highlight how well your server handles load. The requests per second value shows the average throughput, while the time per request (mean) indicates the latency experienced by each request. Ideally, the failed requests metric should remain at zero to confirm reliability. Finally, the transfer rate measures the effective bandwidth used by the responses, giving you insight into overall data flow efficiency.

## Benchmark summary on Arm64

The following results were collected on an Arm64 **D4ps_v6** VM running **Ubuntu Pro 24.04 LTS**:

| Category              | Metric                                       | Value                  |
|---------------------------|--------------------------------------------------|----------------------------|
| General info          | Server Software                                  | nginx/1.24.0               |
|                           | Server Hostname                                  | localhost                  |
|                           | Server Port                                      | 80                         |
|                           | Document Path                                    | /                          |
|                           | Document Length                                  | 890 bytes                  |
| Test setup            | Concurrency Level                                | 50                         |
|                           | Time Taken for Tests                             | 0.032 sec                  |
|                           | Complete Requests                                | 1,000                      |
|                           | Failed Requests                                  | 0                          |
| Transfer stats        | Total Transferred                                | 1,132,000 bytes            |
|                           | HTML Transferred                                 | 890,000 bytes              |
|                           | Requests per Second                              | 31,523.86 #/sec            |
|                           | Time per Request (mean)                          | 1.586 ms                   |
|                           | Time per Request (across all)                    | 0.032 ms                   |
|                           | Transfer Rate                                    | 34,848.65 KB/sec           |
| Connection times (ms) | Connect (min / mean / stdev / median / max)      | 0 / 1 / 0.1 / 1 / 1        |
|                           | Processing (min / mean / stdev / median / max)   | 0 / 1 / 0.1 / 1 / 1        |
|                           | Waiting (min / mean / stdev / median / max)      | 0 / 1 / 0.2 / 1 / 1        |
|                           | Total (min / mean / stdev / median / max)        | 1 / 2 / 0.1 / 2 / 2        |

## Analysis of results from NGINX benchmarking on Arm-based Azure Cobalt-100  

These results highlight the performance characteristics of NGINX on Arm64-based Azure VMs (such as **D4ps_v6**):

- High Requests per second (31,523.86 requests/sec), demonstrating high throughput under concurrent load.
- Response time per request averaged 1.586 ms, indicating efficient handling of requests with minimal delay.
- Zero failed requests, confirming stability and reliability during testing.
- Consistently low connection and processing times (mean ≈ 1 ms), ensuring smooth performance.

Overall, NGINX on Arm64 provides a performant, cost‑efficient platform for web workloads on Azure. You can use the same benchmark to compare with equivalent x86-based instances to evaluate relative performance and cost efficiency across architectures.
