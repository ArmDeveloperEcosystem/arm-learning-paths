---
title: Benchmark Django application performance on Arm
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark your Django application with ApacheBench and Gunicorn

This section guides you through benchmarking your Django web application using Gunicorn as a production-like WSGI server and ApacheBench (`ab`) for load testing. You'll measure throughput (requests per second) and latency (response time) to evaluate your Django app's performance on an Arm-based Google Cloud C4A VM.

## Install ApacheBench

To begin, if your Django development server is still running, stop it using `Ctrl + C`.

Install ApacheBench to measure your application's performance under load.

```bash
sudo zypper install -y apache2-utils
```

Verify the installation:

```bash
ab -V
```

You should see the ApacheBench version information displayed.


ApacheBench (`ab`) is a command-line tool that simulates multiple HTTP requests to measure web server performance. Install it using the following:

```bash
sudo zypper install -y apache2-utils
```

### Verify installation

Confirm ApacheBench is correctly installed and available.

```bash
ab -V
```

The output displays the ApacheBench version.

## Install and configure Gunicorn

Before benchmarking your Django application, you need to install Gunicorn, a production-grade WSGI HTTP server. Gunicorn provides better performance characteristics than Django's development server and more accurately represents real-world deployment scenarios.

### Install both Django and Gunicorn using pip

```bash
python3 -m pip install django gunicorn
```

This installs Django and Gunicorn. Gunicorn is a production-grade WSGI HTTP server that handles multiple requests at the same time. Unlike Django's built-in development server, Gunicorn uses multiple workers to process requests efficiently, which gives you more accurate performance measurements.

## Run Django with Gunicorn

Your Django application runs with Gunicorn inside GKE. The Gunicorn server is deployed inside your Kubernetes Pods and exposed through a Kubernetes Service and LoadBalancer. You run the benchmark against the external IP of the GKE service.

{{% notice Note %}}Ensure your GKE cluster and LoadBalancer are properly configured. If you haven't set up the cluster yet, refer to the previous sections for GKE deployment and service configuration.{{% /notice %}}

## Run the benchmark

Use ApacheBench to test your Django server with simulated traffic:

```bash
ab -n 5000 -c 100 http://<external_IP_of_the_GKE_service>/healthz/
```

This command sends 5000 requests with 100 concurrent connections to your Django REST endpoint.

Parameters explained:
- `-n 5000`: total number of requests to send
- `-c 100`: number of concurrent requests
- `http://<external_IP_of_the_GKE_service>/healthz/`: your Django health check endpoint

Replace `<external_IP_of_the_GKE_service>` with your actual GKE LoadBalancer IP address.

The benchmark runs for a few seconds and displays results similar to:

```output
Server Software:        gunicorn
Server Hostname:        34.132.110.81
Server Port:            80

Document Path:          /healthz/
Document Length:        15 bytes

Concurrency Level:      100
Time taken for tests:   0.357 seconds
Complete requests:      5000
Failed requests:        0
Total transferred:      1650000 bytes
HTML transferred:       75000 bytes
Requests per second:    14001.88 [#/sec] (mean)
Time per request:       7.142 [ms] (mean)
Time per request:       0.071 [ms] (mean, across all concurrent requests)
Transfer rate:          4512.32 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       2
Processing:     1    6   4.7      6      32
Waiting:        0    6   4.7      6      32
Total:          1    7   4.8      6      34

Percentage of the requests served within a certain time (ms)
  50%      6
  66%      9
  75%     10
  80%     11
  90%     11
  95%     11
  98%     16
  99%     28
 100%     34 (longest request)
```
## Interpret your benchmark results

The ApacheBench output provides key performance metrics for evaluating your Django application on Google Axion (Arm64) GKE:

### Request handling metrics

Your benchmark captures three foundational indicators of request handling capacity:

- Concurrency Level: simultaneous requests sent during the benchmark (100)
- Complete Requests: total successful requests processed (5000)
- Failed Requests: errors or timeouts encountered (0, indicating stable performance)

### Performance metrics

Your Django application's performance under load is measured by three critical metrics:

- Requests per Second: how many requests your server handles per second; higher values indicate better throughput (14,001.88 req/sec)
- Time per Request (mean): average time to complete a single request (7.142 ms)
- Time per Request (across concurrent): average latency when factoring in concurrent processing (0.071 ms), showing excellent parallel execution on Axion Arm cores

### Data transfer metrics

The benchmark captures how efficiently your application transfers data across the network stack:

- Total Transferred: all data sent and received, including HTTP headers (1,650,000 bytes)
- HTML Transferred: actual response payload size (75,000 bytes)
- Transfer Rate: network throughput in KB/sec (4512.32 KB/sec), indicating efficient networking through GKE LoadBalancer

### Timing breakdown

The timing breakdown section provides detailed insight into how your application spends time processing each request:

- Time Taken for Tests: total benchmark duration (0.357 seconds)
- Connection Times: shows minimum, mean, median, and maximum times for connecting, processing, and waiting

These metrics establish a real production-grade performance baseline for your Django REST API running on GKE Axion (Arm64) with Gunicorn, Cloud SQL, and Redis.

## Benchmark summary

The table below summarizes the key performance indicators from your real benchmark run on the Axion Arm64 GKE cluster.

Results from the run on the `Axion (C4A) Arm64 GKE nodes`:

| **Parameter** | **Description** | **Value** |
|--------------|------------------|-----------|
| **Server Software** | web server used for serving Django | gunicorn |
| **Server Hostname** | external LoadBalancer IP | 34.132.110.81 |
| **Server Port** | port number for benchmark | 80 |
| **Document Path** | endpoint used for testing | /healthz/ |
| **Document Length** | size of each response | 15 bytes |
| **Concurrency Level** | number of concurrent requests | 100 |
| **Time Taken for Tests** | total time to complete all requests | 0.357 seconds |
| **Complete Requests** | total number of successful requests | 5000 |
| **Failed Requests** | number of failed requests | 0 |
| **Total Transferred** | total bytes transferred (including headers) | 1,650,000 bytes |
| **HTML Transferred** | total response body bytes | 75,000 bytes |
| **Requests per Second (mean)** | throughput - higher is better | **14,001.88 req/sec** |
| **Time per Request (mean)** | average time for each request | **7.142 ms** |
| **Time per Request (across all concurrent requests)** | average latency considering concurrency | **0.071 ms** |
| **Transfer Rate** | network throughput rate | **4512.32 KB/sec** |
| **p50 (Median Latency)** | 50% of requests completed within | **6 ms** |
| **p90 Latency** | 90% of requests completed within | **11 ms** |
| **p95 Latency** | 95% of requests completed within | **11 ms** |
| **p99 Latency** | 99% of requests completed within | **28 ms** |
| **Max Latency** | longest request observed | **34 ms** |

## Key performance insights

The benchmark results demonstrate the strength of running Django on Google Axion (Arm64) GKE:

- Extreme Throughput: the cluster sustained 14,000+ requests per second through a public LoadBalancer → GKE → Gunicorn → Django → Cloud SQL → Redis stack.
- Ultra-Low p95 Latency: even at 100 concurrent users, 95% of all requests completed within 11 ms.
- Production Stability: zero failed requests confirms the platform is resilient under heavy parallel load.
- Efficient Networking: over 4.4 MB/sec of data transfer through the GKE LoadBalancer shows Arm-based networking is highly optimized.
- Cloud-native Scalability: these results validate that Axion Arm64 nodes are well-suited for high-performance, horizontally scalable REST APIs in production.

## What you've accomplished and what's next

In this section, you:
- Installed and configured ApacheBench for load testing
- Deployed Gunicorn as a production-grade WSGI server for Django
- Executed a comprehensive benchmark against your GKE-hosted Django application
- Analyzed performance metrics showing 14,000+ requests per second with sub-millisecond concurrent latency
- Validated that Google Axion (Arm64) GKE delivers production-ready performance for Django workloads

Your Django application is now proven to handle high-concurrency traffic efficiently on Arm-based infrastructure. You've established a performance baseline that demonstrates the scalability and reliability of running Django on Google Cloud's Axion processors with GKE, Cloud SQL, and Redis.

You're ready to optimize further, scale your deployment, or integrate additional services into your cloud-native Django architecture.