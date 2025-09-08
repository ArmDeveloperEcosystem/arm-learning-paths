---
title: Envoy performance benchmarks on Arm64 and x86_64 in Google Cloud
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How to run Envoy benchmarks with Siege on Arm64 in GCP

**Siege** is a lightweight HTTP load testing and benchmarking tool that simulates concurrent users making requests to a target service. It is useful for Envoy benchmarking because it measures availability, throughput, response time, and failure rates under load, thus helping evaluate Envoy’s performance as a proxy under real-world traffic conditions.

Follow the steps outlined to run Envoy benchmarks using Siege.

### Install Siege(Build from Source)

1. Install required build tools

```console
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y wget make gcc
```
2. Download, extract and build Siege source

```console
wget http://download.joedog.org/siege/siege-4.1.6.tar.gz
tar -xvzf siege-4.1.6.tar.gz
cd siege-4.1.6
./configure
make
sudo make install
```
You have now successfully built and installed Seige on your Arm-based machine.

3. Verify installation

```console
siege --version
```
This checks if Siege is installed properly and shows the version number.
```output
SIEGE 4.1.6

Copyright (C) 2023 by Jeffrey Fulmer, et al.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.
```
### Envoy Benchmarking

1. To start, make sure Envoy is up and running with your config file (listening on port 10000):


```console
envoy -c envoy_config.yaml --base-id 1
```
This runs the Envoy proxy with your configuration file (envoy_config.yaml) so it can start listening for requests.

2. On another terminal, verify that envoy is running as expected with curl:

```
curl -v http://127.0.0.1:10000/get
```
Running from another terminal returns a **200 OK** status, confirming that Envoy is running and successfully proxying requests.

3. Run a Time-based Load Test

There are different ways you can setup your benchmark tests. Here you will run a Benchmark for a fixed time instead of using request count:

```console
siege -c30 -t10S http://127.0.0.1:10000/get
```
This runs a load test where 30 users hit Envoy continuously for 10 seconds. After this, Siege will show performance results.

The output should show a list of HTTP requests and responses followed by a summary as shown:

```output
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.02 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.42 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.17 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.81 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.14 secs:     383 bytes ==> GET  /get

Lifting the server siege...
Transactions:                   1019 hits
Availability:                  99.80 %
Elapsed time:                  10.38 secs
Data transferred:               0.37 MB
Response time:                  0.29 secs
Transaction rate:              98.17 trans/sec
Throughput:                     0.04 MB/sec
Concurrency:                   28.07
Successful transactions:        1019
Failed transactions:               2
Longest transaction:            2.89
Shortest transaction:           0.02
```

### Understanding Envoy benchmark metrics and results with Siege

- **Transactions**: Total number of completed requests during the benchmark.
- **Availability**: Percentage of requests that returned a successful response.
- **Elapsed Time**: Total time taken to run the benchmark test.
- **Data Transferred**: Total amount of data exchanged during the test.
- **Response Time**: Average time taken for the server to respond to each request.
- **Transaction Rate**: Number of requests processed per second.
- **Throughput**: Volume of data transferred per second.
- **Concurrency**: Average number of simultaneous connections maintained.
- **Successful Transactions**: Total number of requests completed successfully.
- **Failed Transactions**: Total number of requests that failed.
- **Longest Transaction**: Maximum response time observed for a single request.
- **Shortest Transaction**: Minimum response time observed for a single request.

### Benchmark summary on x86_64:
To compare the benchmark results, the following results were collected by running the same benchmark on a `c3-standard-4` (4 vCPU, 2 core, 16 GB Memory) x86_64 virtual machine in GCP, running RHEL 9.

| Metric                 | Value        | Metric                   | Value           |
|-------------------------|--------------|---------------------------|-----------------|
| Transactions            | 720 hits     | Availability              | 98.90 %         |
| Elapsed time            | 10.98 secs   | Data transferred          | 0.26 MB         |
| Response time           | 0.44 secs    | Transaction rate          | 65.57 trans/sec |
| Throughput              | 0.02 MB/sec  | Concurrency               | 28.66           |
| Successful transactions | 720          | Failed transactions       | 8               |
| Longest transaction     | 4.63 secs    | Shortest transaction      | 0.02 secs       |

### Benchmark summary on Arm64:
Results from the earlier run on the c4a-standard-4 (4 vCPU, 16 GB memory) Arm64 VM in GCP (RHEL 9):

| Metric                 | Value         | Metric                   | Value           |
|-------------------------|---------------|---------------------------|-----------------|
| Transactions            | 1019 hits     | Availability              | 99.80 %         |
| Elapsed time            | 10.38 secs    | Data transferred          | 0.37 MB         |
| Response time           | 0.29 secs     | Transaction rate          | 98.17 trans/sec |
| Throughput              | 0.04 MB/sec   | Concurrency               | 28.07           |
| Successful transactions | 1019          | Failed transactions       | 2               |
| Longest transaction     | 2.89 secs     | Shortest transaction      | 0.02 secs       |

### Envoy performance benchmarking comparison on Arm64 and x86_64
When you compare the benchmarking performance results between the two instance types with the same vCPUs, you will notice that on the Google Axion C4A Arm-based instances:

- You have more successful transactions, fewer failures.
- Lower response times, higher transaction rate, better throughput.

You have successfully learned how to use Siege to benchmark Envoy on your Arm-based Axion Google cloud instance, validating both performance and reliability against similar x86 instances.
