---
title: Monitor MongoDB with mongostat
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Observe server activity

Keep the workload running in terminal 1. In terminal 3, SSH into the same Cobalt 200 VM and collect three samples at two-second intervals:

```console
mongostat --host 127.0.0.1 --port 27017 --rowcount=3 2
```

The command stops after three samples. To monitor continuously, omit `--rowcount=3` and press **Ctrl+C** to stop.

The output is similar to:

```output
insert query update delete getmore command dirty used flushes vsize  res qrw arw net_in net_out conn                time
  1894  1894   1894   1894       0     1|0  0.5% 0.6%       0 3.55G 157M 0|0 0|0  1.31m    607k   10 Nov 10 18:58:39.089
  1867  1867   1867   1867       0     0|0  0.6% 0.7%       0 3.55G 157M 0|0 0|0  1.29m    599k   10 Nov 10 18:58:41.089
  1831  1831   1831   1831       0     1|0  0.7% 0.9%       0 3.55G 159M 0|0 0|0  1.27m    589k   11 Nov 10 18:58:43.090
```

These samples were collected on a **Standard_D4ps_v7** Cobalt 200 VM (4 vCPUs, 16 GiB) running **Ubuntu 24.04 LTS**, **MongoDB 8.0.12**, and **Database Tools 100.13.0** with the provided single-client workload. Your results will vary.

## Interpret the metrics

- **insert, query, update, delete** report operation rates. Some modern read operations are reported as commands rather than legacy query operations.
- **getmore** reports operations that fetch additional cursor results.
- **command** reports database command activity, including commands issued by the monitoring tools.
- **dirty/used** describe dirty and used portions of the WiredTiger cache.
- **vsize/res** report virtual and resident process memory.
- **qrw/arw** describe queued and active readers and writers.
- **net_in/net_out** show incoming and outgoing network traffic rates.
- **conn** reports active connections.
- **time** identifies each sample.

For field definitions, see the [mongostat documentation](https://www.mongodb.com/docs/database-tools/mongostat/).

## Evaluate the baseline

The workload performs inserts, reads, updates, and deletes, so you should see activity while it runs. Compare several samples and use `mongotop` to identify the active collection. If activity is absent, check whether the 60-second workload has already finished and re-run it if needed.

These short samples demonstrate monitoring of a functional local MongoDB deployment on Cobalt 200. They do not establish sustained throughput, request latency, production capacity, or a performance or cost comparison with other VM types. Use representative data and a separate load generator for capacity testing.
