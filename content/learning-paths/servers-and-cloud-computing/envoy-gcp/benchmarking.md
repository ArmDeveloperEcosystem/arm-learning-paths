---
title: Envoy performance benchmarks on Arm64 and x86_64 in Google Cloud
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How to run Envoy benchmarks with Siege on Arm64 in GCP

**Siege** is a lightweight HTTP load testing and benchmarking tool that simulates concurrent users making requests to a target service. It is useful for **Envoy benchmarking** because it measures availability, throughput, response time, and failure rates under load—helping evaluate Envoy’s performance as a proxy under real-world traffic conditions.

Follow the steps outlined to run Envoy benchmarks using the Siege.
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
These commands prepare Siege for your system, build (compile) it, and then install it so you can run it from anywhere.

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

1. Ensure Envoy is Running

To make sure your Envoy proxy is up with your config file (listening on port 10000 for example):

```console
envoy -c envoy_config.yaml --base-id 1
```
This runs the Envoy proxy with your configuration file (envoy_config.yaml) so it can start listening for requests.

2. Verify with curl from the another terminal:

```
curl -v http://127.0.0.1:10000/get
```
Running from another terminal returns a **200 OK** status, confirming that Envoy is running and successfully proxying requests.

3. Run a Time-based Load Test

Benchmark for a fixed time instead of request count:

```console
siege -c30 -t10S http://127.0.0.1:10000/get
```
This runs a load test where 30 users hit Envoy continuously for 10 seconds. After this, Siege will show performance results.

The output should look similar to:

```output
** SIEGE 4.1.6
** Preparing 30 concurrent users for battle.
The server is now under siege...
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.09 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.09 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.07 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.16 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.17 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.09 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.25 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.32 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.32 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.21 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.34 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.34 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.35 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.36 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.19 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.39 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.32 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.32 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.39 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.36 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.45 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.42 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.02 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.32 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.55 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.30 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.68 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.33 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.27 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.54 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.56 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.47 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.40 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.46 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.14 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.86 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.92 secs:     383 bytes ==> GET  /get
HTTP/1.1 502     0.07 secs:     122 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.29 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.77 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.79 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.24 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.18 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.80 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.99 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.46 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.74 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.16 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.38 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.62 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.44 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.43 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.32 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.21 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.68 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.34 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.95 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.91 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.17 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.19 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.38 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.87 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.26 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.09 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.09 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.48 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.61 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.40 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.42 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.52 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.52 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.37 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.20 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.61 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.96 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.57 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.48 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.07 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.47 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.39 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.83 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.28 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.65 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.88 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.59 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.20 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.66 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.23 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.62 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.41 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     2.21 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.48 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.55 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.25 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.14 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.90 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.70 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.98 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.64 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.07 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.30 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.07 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.22 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.62 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.43 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.70 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.42 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.79 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.15 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.67 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.54 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.81 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.59 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.34 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.69 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.86 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.55 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.53 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.43 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.28 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.15 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.28 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     2.55 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.58 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.63 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.27 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.25 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.36 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.45 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.67 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.43 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     2.27 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.15 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.28 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.16 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.12 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.63 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.58 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.07 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.65 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.98 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.23 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.63 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.34 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.21 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.54 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.00 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.11 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.23 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.49 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.31 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.25 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.11 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.38 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.41 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.60 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.81 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.14 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.31 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.36 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.62 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.46 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.18 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.46 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.09 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.09 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.82 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.89 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.38 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.51 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.80 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.44 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.16 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.07 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.63 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.62 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.23 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.02 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.37 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.61 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.57 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.83 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.49 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.66 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.34 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.22 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.19 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.52 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.63 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.19 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.19 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.81 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.80 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.48 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.66 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.68 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.33 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.16 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.80 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.83 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.57 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.29 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.49 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.23 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.07 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.58 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.18 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.34 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.19 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.28 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.31 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.43 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.45 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.48 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.16 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.14 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.15 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.29 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.58 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.75 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.60 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.18 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.68 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.11 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.07 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.78 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.96 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.41 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.29 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.47 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.42 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.75 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.84 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.14 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.60 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.02 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.95 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.16 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.23 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.59 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.23 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.12 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.20 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.54 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.81 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.25 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.36 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.76 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.39 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.15 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.84 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.50 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.14 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.11 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.76 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.56 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.69 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.09 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.18 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.68 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.56 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.58 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.64 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 502     0.36 secs:     122 bytes ==> GET  /get
HTTP/1.1 200     0.54 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.57 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.66 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.31 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.12 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.39 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.69 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.49 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.79 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     2.81 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.25 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.62 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.39 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.78 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.14 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.69 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.72 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.40 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.66 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.62 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.93 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.59 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.17 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.18 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.43 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.51 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.39 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.54 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.11 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.23 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.16 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.29 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.75 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.32 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.64 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.15 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.84 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.28 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.58 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.54 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.59 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.93 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.09 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.07 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.93 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.51 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.96 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.44 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.14 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.57 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.33 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.46 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.89 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.60 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.31 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.44 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.36 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.46 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.31 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.16 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.36 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.35 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.33 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.74 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.24 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.42 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.09 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.33 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.14 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.12 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.23 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.33 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.53 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.21 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.56 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.92 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.14 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.68 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.18 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.16 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.34 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.27 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.65 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.18 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.66 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.20 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.36 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.25 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.02 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.66 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.36 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.47 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.59 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.39 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.40 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.22 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.57 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.17 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.48 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.74 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.32 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.39 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.06 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.24 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.14 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.69 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     2.35 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.83 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.67 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.55 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.60 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.73 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.07 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.28 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.28 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.56 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.73 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.07 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.39 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.53 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.33 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.12 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.78 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.57 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.61 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.49 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.90 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.13 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.02 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.26 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.45 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.20 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.98 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.53 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     2.10 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.27 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     2.45 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.74 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.46 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.31 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.39 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.48 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.99 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.26 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.53 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.12 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.02 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.80 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.67 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.37 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.07 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.26 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.21 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.38 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.53 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.20 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.64 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     2.89 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.20 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.04 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     1.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.08 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.64 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.46 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.81 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.51 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.61 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.35 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.91 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.35 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.91 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.05 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.53 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.51 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.03 secs:     383 bytes ==> GET  /get
HTTP/1.1 200     0.37 secs:     383 bytes ==> GET  /get
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
The following benchmark results were collected by running the same benchmark on a c3-standard-4 (4 vCPU, 2 core, 16 GB Memory) x86_64 virtual machine in GCP, running RHEL 9.

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
When you compare the benchmarking results you will notice that on the Google Axion C4A Arm-based instances:

- Achieved **1019 successful transactions** with only **2 failures**, ensuring **99.80%** availability.
- Delivered a strong **transaction rate of 98.17 trans/sec** and throughput of **0.04 MB/sec**.
- Maintained low **response times (0.29 secs average)**, with a shortest transaction of **0.02 secs**.
- Demonstrated **stable concurrency handling (28.07)** and controlled latency, with the longest transaction completing in **2.89 secs.**
