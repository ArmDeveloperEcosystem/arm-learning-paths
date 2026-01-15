---
title: Benchmark Django application performance on Arm
weight: 7

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
## Verify installation

This command confirms ApacheBench is correctly installed and available system-wide:

```console
ab -V
```

The output displays the ApacheBench version, confirming successful installation.

## Install and configure Gunicorn

Before benchmarking your Django application, you need to install Gunicorn, a production-grade WSGI HTTP server. Gunicorn provides better performance characteristics than Django's development server and more accurately represents real-world deployment scenarios.

Install both Django and Gunicorn using pip:

```console
python3 -m pip install django gunicorn
```

This command installs two essential packages. Django is the Python web framework you're benchmarking, while Gunicorn serves as a high-performance WSGI HTTP server that handles multiple concurrent requests efficiently. Unlike Django's built-in development server, Gunicorn is designed for production workloads and provides the multi-worker architecture needed for accurate performance testing.


## Run Django with Gunicorn

Start your Django application using Gunicorn:

```console
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 --workers 4 &
```

This command starts Gunicorn with four worker processes to handle concurrent requests. Replace `myproject` with your Django project's actual name. The `--bind 0.0.0.0:8000` flag makes the server accessible on port 8000 from any network interface, while the `&` runs the process in the background so you can continue using your terminal.

{{% notice Note %}}
Ensure your VM's firewall allows inbound traffic on port 8000. See the firewall setup section if you haven't already configured this.
{{% /notice %}}

## Run the benchmark
Use ApacheBench to test your Django server with simulated traffic:

```console
ab -n 1000 -c 10 http://127.0.0.1:8000/
```

This sends 1000 requests using 10 concurrent connections to your local server's root URL. The `-n` flag sets the total number of requests, while `-c` controls how many run simultaneously.

The output is similar to:

```output
This is ApacheBench, Version 2.3
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
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

Server Software:        gunicorn
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /
Document Length:        41 bytes

Concurrency Level:      10
Time taken for tests:   0.104 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      280000 bytes
HTML transferred:       41000 bytes
Requests per second:    9651.21 [#/sec] (mean)
Time per request:       1.036 [ms] (mean)
Time per request:       0.104 [ms] (mean, across all concurrent requests)
Transfer rate:          2639.00 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:     0    1   0.3      1       4
Waiting:        0    1   0.3      1       3
Total:          0    1   0.4      1       5

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      2
  98%      2
  99%      3
 100%      5 (longest request)
```
## Stop the Gunicorn server

After reviewing the benchmark results, stop the Gunicorn server running in the background:

```bash
fg
```

This brings the background Gunicorn process to the foreground. Then press `Ctrl+C` to stop it.

## Interpret your benchmark results

The ApacheBench output provides key performance metrics that help you evaluate your Django application's capabilities on Arm. Here's what each metric tells you:
### Request handling metrics
- Concurrency Level: number of simultaneous requests the benchmark sent (10 in this example)
- Complete Requests: total successful requests processed (1000 in this test)
- Failed Requests: number of errors or timeouts (0 indicates stable performance)

### Performance metrics
- Requests per Second: how many requests your server handles per second - higher values indicate better throughput
- Time per Request (mean): average time to complete a single request - lower values mean faster responses
- Time per Request (across concurrent): average latency when factoring in concurrent processing, this shows how well your app handles parallel requests

### Data transfer metrics
- Total Transferred: all data sent and received, including HTTP headers
- HTML Transferred: actual response content size
- Transfer Rate: network throughput in KB/sec—indicates data handling efficiency
### Timing breakdown
- Time Taken for Tests: total benchmark duration
- Connection Times: shows minimum, mean, median, and maximum times for connecting, processing, and waiting

These metrics provide a performance baseline for your Django application on Arm. You can use them to compare different configurations, identify bottlenecks, or validate optimizations.

## Benchmark summary

The table below summarizes the key performance indicators from the benchmark test. These results demonstrate the capabilities of your Django application running on a Google Cloud C4A Arm-based VM with Gunicorn.

Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

| **Parameter** | **Description** | **Value** |
|----------------|------------------|-----------|
| **Server Software** | Web server used for serving Django | gunicorn |
| **Server Hostname** | Host address tested | 127.0.0.1 |
| **Server Port** | Port number for benchmark | 8000 |
| **Document Path** | Endpoint used for testing | / |
| **Document Length** | Size of each response | 41 bytes |
| **Concurrency Level** | Number of concurrent requests | 10 |
| **Time Taken for Tests** | Total time to complete all requests | 0.104 seconds |
| **Complete Requests** | Total number of successful requests | 1000 |
| **Failed Requests** | Number of failed requests | 0 |
| **Total Transferred** | Total bytes transferred (including headers) | 280000 bytes |
| **HTML Transferred** | Total HTML body bytes transferred | 41000 bytes |
| **Requests per Second (mean)** | Throughput — higher is better | **9651.21 req/sec** |
| **Time per Request (mean)** | Average time for each request | **1.036 ms** |
| **Time per Request (across all concurrent requests)** | Average latency considering concurrency | **0.104 ms** |
| **Transfer Rate** | Network throughput rate | **2639.00 KB/sec** |

## Key performance insights

The benchmark results reveal several important characteristics of running Django on Arm-based infrastructure:

- Exceptional Throughput: the Arm64 VM efficiently handled nearly 10K requests per second, showcasing excellent concurrency handling.
- Low Latency: average response time stayed around 1 ms, indicating rapid request processing even under load.
- High Efficiency: zero failed requests demonstrate stable and reliable performance under benchmark conditions.
- Optimized Networking: strong data transfer rate highlights Arm64's efficient network I/O capabilities.
- Ideal for Scalable Apps: the consistent and predictable response times make Arm64 VMs well-suited for high-performance web workloads.
