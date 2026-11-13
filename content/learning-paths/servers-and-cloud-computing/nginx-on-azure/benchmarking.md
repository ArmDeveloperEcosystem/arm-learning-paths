---
title: NGINX Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark NGINX with ApacheBench on Arm

Use ApacheBench (**ab**) to measure NGINX performance on your Arm64 Azure VM. This section shows you how to install the tool, run a basic benchmark, interpret key metrics, and review a sample result from an Azure **D4ps_v7** instance.

## Install ApacheBench

On **Ubuntu 24.04 LTS**, ApacheBench is provided by the **apache2-utils** package:

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
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/
```

## Run a basic benchmark

The general syntax for running an ApacheBench test is:

```console
ab -n <total_requests> -c <concurrent_clients> <http://host:port/path>
```

Example (1,000 requests, 50 concurrent, to your static website on localhost):

```console
ab -n 1000 -c 50 http://localhost/
```

This command sends 1,000 total requests with 50 concurrent connections to `http://localhost/`.

Sample output:

```output
Server Software:        nginx/1.24.0
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        880 bytes

Concurrency Level:      50
Time taken for tests:   0.025 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      1122000 bytes
HTML transferred:       880000 bytes
Requests per second:    40196.16 [#/sec] (mean)
Time per request:       1.244 [ms] (mean)
Time per request:       0.025 [ms] (mean, across all concurrent requests)
Transfer rate:          44043.06 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:     0    1   0.2      1       2
Waiting:        0    1   0.2      1       1
Total:          1    1   0.1      1       2

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      2
  99%      2
 100%      2 (longest request)
```

## Interpret benchmark results

ApacheBench produces a variety of metrics, but the most useful ones highlight how well your server handles load. The requests per second value shows the average throughput, while the first time per request value is calculated as concurrency multiplied by test duration divided by completed requests. The second time per request value divides test duration by completed requests. Use the connection timings and percentiles to examine request latency. Ideally, the failed requests metric should remain at zero to confirm reliability. Finally, the transfer rate measures the effective bandwidth used by the responses, giving you insight into overall data flow efficiency.

## Benchmark summary on Arm64

The following results were collected on an Azure Cobalt 200 **Standard_D4ps_v7** VM (4 vCPUs) in **West US 2**, running **Ubuntu 24.04 LTS** with **NGINX 1.24.0**. ApacheBench ran on the same VM against the 880-byte static page created in the previous section.

| Metric | Value |
|--------|-------|
| Concurrency | 50 |
| Complete requests | 1,000 |
| Failed requests | 0 |
| Time taken | 0.025 seconds |
| Requests per second | 40,196.16 |
| Time per request (mean) | 1.244 ms |
| Time per request (mean, across concurrent requests) | 0.025 ms |
| Total transferred | 1,122,000 bytes |
| HTML transferred | 880,000 bytes |
| Transfer rate | 44,043.06 Kbytes/sec |

## Summary

Your NGINX deployment on Azure Cobalt 200 successfully handled all 1,000 requests with 50 concurrent connections and no failures. You now have a working static website and an initial performance baseline to guide further testing.

ApacheBench ran on the same VM as NGINX, so these results reflect local request handling. To evaluate production capacity, run longer, repeated tests from a separate load generator using representative content and traffic patterns. Keep the test conditions consistent when comparing configurations or VM types.
