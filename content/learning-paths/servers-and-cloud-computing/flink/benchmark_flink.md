---
# User change
title: "Benchmark Flink with nexmark-flink on Arm"
weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

You are now ready to benchmark Flink with Nexmark on your Arm server


## Flink Start
Start the Flink Cluster by running `flink/bin/start-cluster.sh` on the master node:
```console
bash ~/flink-benchmark/flink-1.17.2/bin/start-cluster.sh
```

## Benchmark Setup
Setup the benchmark cluster by running `nexmark/bin/setup_cluster.sh` on the master node:
```console
bash ~/flink-benchmark/nexmark-flink/bin/setup_cluster.sh
```

## Nexmark run
To run nexmark, type the following command:

```console
bash ~/flink-benchmark/nexmark-flink/bin/run_query.sh
```
You can also run the benchmark with additional queries:

```console
bash ~/flink-benchmark/nexmark-flink/bin/run_query.sh q1,q2
```


#### View the results

The sample output from running the benchmark is shown below:

```output
Benchmark Queries: [q0]
==================================================================
Start to run query q0 with workload [tps=10 M, eventsNum=100 M, percentage=bid:46,auction:3,person:1,kafkaServers:null]
Start the warmup for at most 120000ms and 100000000 events.
Stop the warmup, cost 120100ms.
Monitor metrics after 10 seconds.
Start to monitor metrics until job is finished.
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Current Cores=0 (0 TMs)
Summary Average: EventsNum=100,000,000, Cores=0, Time=106.258 s
Stop job query q0
-------------------------------- Nexmark Results --------------------------------

+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Nexmark Query     | Events Num        | Cores             | Time(s)           | Cores * Time(s)   | Throughput/Cores  |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|q0                 |100,000,000        |0                  |106.258            |0.000              |9.22 E/s           |
|Total              |100,000,000        |0.000              |106.258            |0.000              |9.22 E/s           |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+

```

