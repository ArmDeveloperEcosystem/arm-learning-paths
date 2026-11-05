---
title: Measure response time and throughput
description: Time individual HTTP requests and run load tests with wrk to measure the component's throughput and latency under two load profiles.
weight: 5
layout: learningpathall
---

## Choose the metrics

Keep `wash dev` running in the first terminal. Stop any other load tests and builds. Then, run the following tests from the
second SSH terminal on the same server to collect the following measurements:

| Test | Metric | What it tells you |
|---|---|---|
| One request to a ready host | Total request time | How long this client takes to receive the response |
| Repeated requests on one connection | Latency and requests per second | Warm behavior with one outstanding request at a time |
| Concurrent requests | Latency and requests per second | Behavior when multiple requests overlap |

The fixed greeting measures a small HTTP path. Results include the client,
loopback networking, wasmCloud routing, and component execution. They don't
represent a database application or the internet latency of an external user.

Record the runtime version and system state before testing:

```bash
result_dir="$HOME/wasmcloud-learning-path/results/$(date -u +%Y%m%dT%H%M%SZ)"
mkdir -p "$result_dir"
date -u > "$result_dir/environment.txt"
wash --version >> "$result_dir/environment.txt"
uname -a >> "$result_dir/environment.txt"
lscpu >> "$result_dir/environment.txt"
free -h >> "$result_dir/environment.txt"
uptime >> "$result_dir/environment.txt"
```

The tests use the normal scheduler without CPU affinity. Both the load generator
and host share the CPU of your server. 

This is a local performance overview. It's not a measurement of the maximum capacity available to a remote client.

## Time individual requests

Make one request to confirm that the application is ready:

```bash
curl --noproxy '*' --fail --show-error http://127.0.0.1:8000/
printf '\n'
```

Measure five more requests, saving the HTTP status and elapsed time:

```bash
for attempt in 1 2 3 4 5; do
  curl --noproxy '*' --fail --silent --show-error \
    --output /dev/null \
    --write-out 'status=%{http_code} total_seconds=%{time_total}\n' \
    http://127.0.0.1:8000/ || break
done | tee "$result_dir/curl-times.txt"
```

The output is similar to:

```output
status=200 total_seconds=0.000659
status=200 total_seconds=0.000480
status=200 total_seconds=0.000468
status=200 total_seconds=0.000469
status=200 total_seconds=0.000481
```

Each line should contain `status=200` and a time in seconds. For example,
multiply a measured value in seconds by 1,000 to express it in milliseconds.
These calls create a new curl process and connection each time. The reported
`time_total` covers the curl transfer, rather than shell process startup.

The host is already running, so these are warm-host requests. They don't
measure loading the component, compiling it, or starting an EC2 instance.

## Measure one connection

Use `wrk` to issue repeated requests for 15 seconds with one client thread and
one open connection:

```bash
set -o pipefail
wrk -t1 -c1 -d15s --latency http://127.0.0.1:8000/ \
  | tee "$result_dir/wrk-one-connection.txt"
```

The output is similar to:

```output
Running 15s test @ http://127.0.0.1:8000/
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   182.09us   10.28us 429.00us   72.13%
    Req/Sec     5.48k    47.55     5.55k    72.85%
  Latency Distribution
     50%  182.00us
     75%  188.00us
     90%  196.00us
     99%  209.00us
  82382 requests in 15.10s, 8.96MB read
Requests/sec:   5455.72
Transfer/sec:    607.37KB
```

Read the following fields in the output:

- `Latency` reports average latency and its variation.
- `Latency Distribution` gives request-latency percentiles.
- `Requests/sec` gives the completed request rate during the test.
- Socket errors, timeouts, and non-success responses indicate an unhealthy run.

With one connection and no HTTP pipelining, the client waits for each response
before issuing the next request. A fast response therefore also allows a higher
request rate. `wrk` reuses connections, so its timings are different from the
individual `curl` transfers.

## Measure concurrent requests

Repeat with four client threads and 32 total connections:

```bash
wrk -t4 -c32 -d15s --latency http://127.0.0.1:8000/ \
  | tee "$result_dir/wrk-32-connections.txt"
```

The output is similar to:

```output
Running 15s test @ http://127.0.0.1:8000/
  4 threads and 32 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.93ms  333.35us   5.38ms   69.44%
    Req/Sec     8.64k   122.72     9.00k    70.03%
  Latency Distribution
     50%    0.93ms
     75%    1.15ms
     90%    1.35ms
     99%    1.65ms
  518889 requests in 15.10s, 56.41MB read
Requests/sec:  34363.59
Transfer/sec:      3.74MB
```

`-c32` distributes 32 connections across the four load-generator threads. It
doesn't create 32 applications or configure a pool of 32 guest instances.
This test changes the offered concurrency and the client thread count together.
It compares two useful load profiles, rather than isolating one runtime setting.

Compare the request rate and latency with the one-connection test. Throughput
can increase when requests overlap, while latency can also rise as work queues.
A higher request rate is useful only if errors and latency remain acceptable
for your application.

Treat runs with socket errors, timeouts, or non-2xx/3xx responses as failures to
investigate. The `wrk` exit status alone doesn't certify that every request
succeeded. Check the response body with `curl` as well because `wrk` doesn't validate it.

Run the two `wrk` commands again if you want to check consistency, choosing new
output filenames. Keep the application, server, and test duration the same.
Avoid interpreting small differences from a single short run as an improvement.

## Save the results

Print the location of the run results:

```bash
printf '%s\n' "$result_dir"
ls -1 "$result_dir"
```

Keep the environment record with the test output. If you close this shell,
`result_dir` will no longer be defined. Use the printed absolute path to find
the files later.

## Clean up

Stop `wash dev` by navigating to the terminal and entering **Ctrl+C** in its terminal. Stop any SSH tunnel that you opened.
Keep the application source and results if you want to repeat the tests.

When finished with your AWS instance, stop or terminate it to avoid continued charges.

## What you've accomplished and what's next

You've measured individual warm-host requests and collected latency and
throughput under two load profiles. 

Next, you'll connect those observations to the application model and the choices that wasmCloud gives you.
