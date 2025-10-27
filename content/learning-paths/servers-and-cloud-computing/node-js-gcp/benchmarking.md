---
title: Benchmark Node.js performance with Autocannon 
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark Node.js with Autocannon

After validating that Node.js is installed and your HTTP server is running, you can benchmark it using Autocannon. You'll use Autocannon to run a series of tests, analyze the results, and identify areas for optimization. Benchmarking on Arm64 provides valuable insights into how Node.js applications scale and perform in cloud environments, helping you make informed decisions about deployment and resource allocation.

## Install Autocannon

Autocannon is a fast HTTP/1.1 benchmarking tool for Node.js, used to measure server throughput, latency, and request handling under concurrent load. To install Autocannon, run this command:

```console
npm install -g autocannon
```

## Start the Node.js HTTP server

If your sample HTTP server isn't running from the last section, start it by using this command:
```console
export MY_NODE=`which node`
sudo ${MY_NODE} app.js &
```

The server should be listening on port 80 in the background:

```output
Server running at http://0.0.0.0:80/
```

## Run a local Node.js benchmark with Autocannon

Now run a local Node.js benchmark with Autocannon:

```console
autocannon -c 100 -d 10 http://localhost:80
```
{{% notice Tip %}}
These options specify how the benchmarking tool runs the test:

- The `-c 100` flag sets the number of concurrent connections to one hundred, simulating multiple users accessing the endpoint at the same time.
- The `-d 10` flag sets the test duration to ten seconds, so the tool sends requests for that period.
- The URL is the endpoint you're measuring, which could be a web service or API running on your Arm server.

This configuration helps you evaluate how your application performs under load on Arm platforms.
{{% /notice %}}

You should see an output similar to:
```output
Running 10s test @ http://localhost:80
100 connections


┌─────────┬──────┬──────┬───────┬──────┬─────────┬─────────┬───────┐
│ Stat    │ 2.5% │ 50%  │ 97.5% │ 99%  │ Avg     │ Stdev   │ Max   │
├─────────┼──────┼──────┼───────┼──────┼─────────┼─────────┼───────┤
│ Latency │ 1 ms │ 1 ms │ 2 ms  │ 2 ms │ 1.06 ms │ 0.41 ms │ 28 ms │
└─────────┴──────┴──────┴───────┴──────┴─────────┴─────────┴───────┘
┌───────────┬─────────┬─────────┬─────────┬────────┬───────────┬──────────┬─────────┐
│ Stat      │ 1%      │ 2.5%    │ 50%     │ 97.5%  │ Avg       │ Stdev    │ Min     │
├───────────┼─────────┼─────────┼─────────┼────────┼───────────┼──────────┼─────────┤
│ Req/Sec   │ 66,175  │ 66,175  │ 70,847  │ 72,191 │ 70,713.61 │ 1,616.86 │ 66,134  │
├───────────┼─────────┼─────────┼─────────┼────────┼───────────┼──────────┼─────────┤
│ Bytes/Sec │ 12.8 MB │ 12.8 MB │ 13.7 MB │ 14 MB  │ 13.7 MB   │ 313 kB   │ 12.8 MB │
└───────────┴─────────┴─────────┴─────────┴────────┴───────────┴──────────┴─────────┘

Req/Bytes counts sampled once per second.
# of samples: 10

707k requests in 10.02s, 137 MB read
```

## Interpret the Autocannon benchmark metrics

Now have a look at the Autocannon benchmark metrics to get a sense of how Node.js performed. Here is an explanation of the metrics and what they mean:

- The average latency (Avg) shows the mean time it takes for each request to receive a response from the server. 
- Standard deviation (Stdev) indicates how much the response times vary around the average; lower values mean the server responds more consistently. 
- The minimum latency (Min) represents the fastest response recorded during the benchmark, highlighting the best-case performance for individual requests.

## Review Node.js benchmark results on Arm64

Here are the results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

### Latency results (ms):

| Metric   | 2.5% | 50% (Median) | 97.5% | 99% | Avg  | Stdev | Max  |
|----------|------|--------------|-------|-----|------|-------|------|
| Latency  | 1    | 1            | 3     | 3   | 1.2  | 0.62  | 24   |

### Throughput results:

| Metric     | 1%     | 2.5%   | 50%     | 97.5%   | Avg      | Stdev    | Min     |
|------------|--------|--------|---------|---------|----------|----------|---------|
| Req/Sec    | 45,279 | 45,279 | 54,719  | 55,199  | 53,798.4 | 2,863.96 | 45,257 |
| Bytes/Sec  | 8.78 MB| 8.78 MB| 10.6 MB | 10.7 MB | 10.4 MB  | 557 kB   | 8.78 MB |

## Evaluate Node.js performance on Arm64

Now that you have the benchmarking results, you can see how Node.js performs on Arm64: 
- The average latency is low, around 1.2 ms, which means your server responds quickly to requests.
- Response times are consistent, with only occasional spikes up to 24 ms.
- The server processes a high volume of traffic, averaging about 53,800 requests per second.
- Data transfer rates are efficient, averaging 10.4 MB per second during the benchmark.
