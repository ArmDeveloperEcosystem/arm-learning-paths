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

ApacheBench (`ab`) is a command-line tool that simulates multiple HTTP requests to measure web server performance. Install it using the following:

```console
sudo zypper install -y apache2-utils
```

### Verify installation
This command confirms ApacheBench is correctly installed and available system-wide:

```console
ab -V
```

The output displays the ApacheBench version, confirming successful installation.

### Install and configure Gunicorn

Before benchmarking your Django application, you need to install Gunicorn, a production-grade WSGI HTTP server. Gunicorn provides better performance characteristics than Django's development server and more accurately represents real-world deployment scenarios.

### Install both Django and Gunicorn using pip:

```console
python3 -m pip install django gunicorn
```
This command installs two essential packages. Django is the Python web framework you're benchmarking, while Gunicorn serves as a high-performance WSGI HTTP server that handles multiple concurrent requests efficiently. Unlike Django's built-in development server, Gunicorn is designed for production workloads and provides the multi-worker architecture needed for accurate performance testing.

### Run Django with Gunicorn
Start your Django application using Gunicorn (already running inside GKE):

Gunicorn is deployed inside your Kubernetes Pods and exposed via a Kubernetes Service and LoadBalancer.
The benchmark is executed against the **external IP of the GKE service**.

{{% notice Note %}}
Ensure your VM's firewall allows inbound traffic on port 8000. See the firewall setup section if you haven't already configured this.
{{% /notice %}}

### Run the benchmark

Use ApacheBench to test your Django server with simulated traffic:

```console
ab -n 5000 -c 100 http://<external_IP_of_the_GKE_service>/healthz/
```
This sends 5000 requests using 100 concurrent connections to your Django REST endpoint exposed through the GKE LoadBalancer.

```output
This is ApacheBench, Version 2.3
Benchmarking 34.132.110.81 (be patient)

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

## Stop the Gunicorn server

After reviewing the benchmark results, stop the Gunicorn server running in the background:

```bash
fg
```
This brings the background Gunicorn process to the foreground. Then press `Ctrl+C` to stop it.

## Interpret your benchmark results

The ApacheBench output provides key performance metrics that help you evaluate your Django application's capabilities on Google Axion (Arm64) GKE. Here's what each metric tells you:
### Request handling metrics
- Concurrency Level: number of simultaneous requests the benchmark sent (100 in this test)
- Complete Requests: total successful requests processed (5000 in this test)
- Failed Requests: number of errors or timeouts (0, indicating stable production-grade performance)

### Performance metrics
- Requests per Second: how many requests your server handles per second — higher values indicate better throughput (14,001.88 req/sec)
- Time per Request (mean): average time to complete a single request (7.142 ms)
- Time per Request (across concurrent): average latency when factoring in concurrent processing (0.071 ms), showing excellent parallel execution on Axion Arm cores

### Data transfer metrics
- Total Transferred: all data sent and received, including HTTP headers (1,650,000 bytes)
- HTML Transferred: actual response payload size (75,000 bytes)
- Transfer Rate: network throughput in KB/sec (4512.32 KB/sec), indicating efficient networking through GKE LoadBalancer

### Timing breakdown
- Time Taken for Tests: total benchmark duration (0.357 seconds)
- Connection Times: shows minimum, mean, median, and maximum times for connecting, processing, and waiting

These metrics establish a real production-grade performance baseline for your Django REST API running on GKE Axion (Arm64) with Gunicorn, Cloud SQL, and Redis.

## Benchmark summary

The table below summarizes the key performance indicators from your real benchmark run on the Axion Arm64 GKE cluster.

Results from the run on the `Axion (C4A) Arm64 GKE nodes`:

| **Parameter** | **Description** | **Value** |
|--------------|------------------|-----------|
| **Server Software** | Web server used for serving Django | gunicorn |
| **Server Hostname** | External LoadBalancer IP | 34.132.110.81 |
| **Server Port** | Port number for benchmark | 80 |
| **Document Path** | Endpoint used for testing | /healthz/ |
| **Document Length** | Size of each response | 15 bytes |
| **Concurrency Level** | Number of concurrent requests | 100 |
| **Time Taken for Tests** | Total time to complete all requests | 0.357 seconds |
| **Complete Requests** | Total number of successful requests | 5000 |
| **Failed Requests** | Number of failed requests | 0 |
| **Total Transferred** | Total bytes transferred (including headers) | 1,650,000 bytes |
| **HTML Transferred** | Total response body bytes | 75,000 bytes |
| **Requests per Second (mean)** | Throughput — higher is better | **14,001.88 req/sec** |
| **Time per Request (mean)** | Average time for each request | **7.142 ms** |
| **Time per Request (across all concurrent requests)** | Average latency considering concurrency | **0.071 ms** |
| **Transfer Rate** | Network throughput rate | **4512.32 KB/sec** |
| **p50 (Median Latency)** | 50% of requests completed within | **6 ms** |
| **p90 Latency** | 90% of requests completed within | **11 ms** |
| **p95 Latency** | 95% of requests completed within | **11 ms** |
| **p99 Latency** | 99% of requests completed within | **28 ms** |
| **Max Latency** | Longest request observed | **34 ms** |

## Key performance insights

The benchmark results demonstrate the strength of running Django on Google Axion (Arm64) GKE:

- Extreme Throughput: The cluster sustained 14,000+ requests per second through a public LoadBalancer → GKE → Gunicorn → Django → Cloud SQL → Redis stack.
- Ultra-Low p95 Latency: Even at 100 concurrent users, 95% of all requests completed within 11 ms, proving excellent tail-latency control.
- Production Stability: Zero failed requests confirms the platform is resilient under heavy parallel load.
- Efficient Networking: Over 4.4 MB/sec of data transfer through the GKE LoadBalancer shows Arm-based networking is highly optimized.
- Cloud-native Scalability: These results validate that Axion Arm64 nodes are well-suited for high-performance, horizontally scalable REST APIs in production.
