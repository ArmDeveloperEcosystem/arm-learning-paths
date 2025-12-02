---
title: Django Benchmarking
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Django Benchmarking using ApacheBench
This section describes how to benchmark a Django web application deployed with **Gunicorn** using **ApacheBench (ab)** — a lightweight HTTP benchmarking tool.  
You will measure **throughput (requests per second)** and **latency (response time)** to evaluate the performance of your Django app on an Arm-based GCP SUSE VM.

### Stop the server
Press `Ctrl + C` to stop the Django server if running.

### Ensure ApacheBench is installed
**ApacheBench (ab)** is a command-line tool used to benchmark web servers by simulating multiple HTTP requests.

Install it using following command:

```console
sudo zypper install -y apache2-utils
```
**Verify installation:**

This confirms ApacheBench is correctly installed and available system-wide.

```console
ab -V
```

**Ensure Django and Gunicorn are installed:**

```console
python3 -m pip install django gunicorn
```
- **Django** is the Python web framework you’re benchmarking.
- **Gunicorn** is a high-performance WSGI HTTP server for deploying Django apps in production-like environments.

### Run Django with Gunicorn
Use Gunicorn to serve your Django application for benchmarking (run in the background):

```console
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 --workers 4 &
```

- `--workers 4`: number of worker processes
- `--bind 0.0.0.0:8000`: binds to all interfaces on port 8000
- `myproject.wsgi:application` your Django project name ("myproject" used in this example).

{{% notice Note %}}
Keep this terminal running during the benchmark. If you’re testing remotely, ensure port 8000 is open in your VM firewall settings.
{{% /notice %}}

### Benchmark with ApacheBench (ab)
Run ApacheBench to simulate multiple clients hitting your Django server.

```console
ab -n 1000 -c 10 http://127.0.0.1:8000/
```
- `-n 1000`: total number of requests
- `-c 10`: concurrency (simultaneous requests)

You should see an output similar to:

```output
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
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

### Cleanup

With the following output (above) seen, you can type "fg" followed by "ctrl-c" to exit the gunicorn server that is running. 

### Benchmark Metrics Explanation

- **Concurrency Level:** Number of requests executed simultaneously during the test.  
- **Time Taken for Tests:** Total time required to complete all HTTP requests.  
- **Complete Requests:** Total number of successful requests processed.  
- **Failed Requests:** Number of requests that failed or returned errors.  
- **Total Transferred:** Total amount of data (including headers) sent and received.  
- **HTML Transferred:** Amount of actual response content transferred.  
- **Requests per Second:** Average number of requests handled by the server per second.  
- **Time per Request (mean):** Average time taken to process a single request.  
- **Time per Request (across concurrent):** Mean time per request across all concurrent clients.  
- **Transfer Rate:** Average network data throughput during the benchmark.

### Benchmark summary
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

- **Exceptional Throughput:** The Arm64 VM efficiently handled nearly 10K requests per second, showcasing excellent concurrency handling.  
- **Low Latency:** Average response time stayed around 1 ms, indicating rapid request processing even under load.  
- **High Efficiency:** Zero failed requests demonstrate stable and reliable performance under benchmark conditions.  
- **Optimized Networking:** Strong data transfer rate highlights Arm64’s efficient network I/O capabilities.  
- **Ideal for Scalable Apps:** The consistent and predictable response times make Arm64 VMs well-suited for high-performance web workloads.  
