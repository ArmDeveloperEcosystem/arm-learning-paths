---
title: Cassendra Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cassendra Benchmarking by Cassendra-Stress
Cassandra benchmarking can be performed using the built-in `cassandra-stress` tool, which helps measure database performance under different workloads such as write, read, and mixed operations.

### Steps for Cassendra Benchmarking with Cassendra-Stress
**Verify cassandra-stress Installation:**

Cassandra comes with a built-in tool called **cassandra-stress** that is used for testing performance. It is usually located in the `tools/bin/` folder of your Cassandra installation. 

```console
ls ~/cassandra/tools/bin | grep cassandra-stress
```
If you see cassandra-stress in the list, it means the tool is installed and ready to use.

**Run the version check:**

To make sure the tool works correctly, check its help options.

```console
~/cassandra/tools/bin/cassandra-stress help
```
You should see output similar to the following:

```output
Usage:      cassandra-stress <command> [options]
Help usage: cassandra-stress help <command>

---Commands---
read                 : Multiple concurrent reads - the cluster must first be populated by a write test
write                : Multiple concurrent writes against the cluster
mixed                : Interleaving of any basic commands, with configurable ratio and distribution - the cluster must first be populated by a write test
counter_write        : Multiple concurrent updates of counters.
counter_read         : Multiple concurrent reads of counters. The cluster must first be populated by a counterwrite test.
user                 : Interleaving of user provided queries, with configurable ratio and distribution
help                 : Print help for a command or option
print                : Inspect the output of a distribution definition
version              : Print the version of cassandra stress
```
If the tool is working, you will see a list of commands and options that you can use to run benchmarks.
This confirms that your setup is correct and you’re ready to start testing Cassandra’s performance.

### Basic Write Test
Insert 10,000 rows with 50 concurrent threads using `cassandra-stress`:

```console
~/cassandra/tools/bin/cassandra-stress write n=10000 -rate threads=50
```
- **write** → Performs only write operations on the Cassandra cluster.  
- **n=10000** → Specifies the number of rows to insert during the benchmark test.  
- **-rate threads=50** → Sets the number of concurrent worker threads simulating multiple clients writing to the cluster. 

You should see output similar to the following:

```output
******************** Stress Settings ********************
Command:
  Type: write
  Count: 10,000
  No Warmup: false
  Consistency Level: LOCAL_ONE
  Target Uncertainty: not applicable
  Key Size (bytes): 10
  Counter Increment Distibution: add=fixed(1)
Rate:
  Auto: false
  Thread Count: 50
  OpsPer Sec: 0
Population:
  Sequence: 1..10000
  Order: ARBITRARY
  Wrap: true
Insert:
  Revisits: Uniform:  min=1,max=1000000
  Visits: Fixed:  key=1
  Row Population Ratio: Ratio: divisor=1.000000;delegate=Fixed:  key=1
  Batch Type: not batching
Columns:
  Max Columns Per Key: 5
  Column Names: [C0, C1, C2, C3, C4]
  Comparator: AsciiType
  Timestamp: null
  Variable Column Count: false
  Slice: false
  Size Distribution: Fixed:  key=34
  Count Distribution: Fixed:  key=5
Errors:
  Ignore: false
  Tries: 10
Log:
  No Summary: false
  No Settings: false
  File: null
  Interval Millis: 1000
  Level: NORMAL
Mode:
  API: JAVA_DRIVER_NATIVE
  Connection Style: CQL_PREPARED
  Protocol Version: V5
  Username: null
  Password: null
  Auth Provide Class: null
  Max Pending Per Connection: 128
  Connections Per Host: 8
  Compression: NONE
Node:
  Nodes: [localhost]
  Is White List: false
  Datacenter: null
Schema:
  Keyspace: keyspace1
  Replication Strategy: org.apache.cassandra.locator.SimpleStrategy
  Replication Strategy Options: {replication_factor=1}
  Table Compression: null
  Table Compaction Strategy: null
  Table Compaction Strategy Options: {}
Transport:
  Truststore: null
  Truststore Password: null
  Keystore: null
  Keystore Password: null
  SSL Protocol: TLS
  SSL Algorithm: null
  SSL Ciphers: TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_256_CBC_SHA
Port:
  Native Port: 9042
  JMX Port: 7199
JMX:
  Username: null
  Password: *not set*
Graph:
  File: null
  Revision: unknown
  Title: null
  Operation: WRITE
TokenRange:
  Wrap: false
  Split Factor: 1
Credentials file:
  File: *not set*
  CQL username: *not set*
  CQL password: *not set*
  JMX username: *not set*
  JMX password: *not set*
  Transport truststore password: *not set*
  Transport keystore password: *not set*
Reporting:
  Output frequency: 1s
  Header frequency: *not set*

Connected to cluster: Test Cluster, max pending requests per connection 128, max connections per host 8
Datacenter: datacenter1; Host: localhost/127.0.0.1:9042; Rack: rack1
Created keyspaces. Sleeping 1s for propagation.
Sleeping 2s...
Warming up WRITE with 2500 iterations...
Running WRITE with 50 threads for 10000 iteration
type                                               total ops,    op/s,    pk/s,   row/s,    mean,     med,     .95,     .99,    .999,     max,   time,   stderr, errors,  gc: #,  max ms,  sum ms,  sdv ms,      mb
total,                                                 10000,   10690,   10690,   10690,     3.7,     2.8,     9.5,    16.7,    28.9,    38.4,    0.9,  0.00000,      0,      0,       0,       0,       0,       0


Results:
Op rate                   :   10,690 op/s  [WRITE: 10,690 op/s]
Partition rate            :   10,690 pk/s  [WRITE: 10,690 pk/s]
Row rate                  :   10,690 row/s [WRITE: 10,690 row/s]
Latency mean              :    3.7 ms [WRITE: 3.7 ms]
Latency median            :    2.8 ms [WRITE: 2.8 ms]
Latency 95th percentile   :    9.5 ms [WRITE: 9.5 ms]
Latency 99th percentile   :   16.7 ms [WRITE: 16.7 ms]
Latency 99.9th percentile :   28.9 ms [WRITE: 28.9 ms]
Latency max               :   38.4 ms [WRITE: 38.4 ms]
Total partitions          :     10,000 [WRITE: 10,000]
Total errors              :          0 [WRITE: 0]
Total GC count            : 0
Total GC memory           : 0 B
Total GC time             :    0.0 seconds
Avg GC time               :    NaN ms
StdDev GC time            :    0.0 ms
Total operation time      : 00:00:00

END
```

### Read Test
The following command runs a **read benchmark** on your Cassandra database using `cassandra-stress`. It simulates multiple clients reading from the cluster at the same time and records performance metrics such as **throughput** and **latency**.

```console
~/cassandra/tools/bin/cassandra-stress read n=10000 -rate threads=50
```
You should see output similar to the following:
```output
******************** Stress Settings ********************
Command:
  Type: read
  Count: 10,000
  No Warmup: false
  Consistency Level: LOCAL_ONE
  Target Uncertainty: not applicable
  Key Size (bytes): 10
  Counter Increment Distibution: add=fixed(1)
Rate:
  Auto: false
  Thread Count: 50
  OpsPer Sec: 0
Population:
  Distribution: Gaussian:  min=1,max=10000,mean=5000.500000,stdev=1666.500000
  Order: ARBITRARY
  Wrap: false
Insert:
  Revisits: Uniform:  min=1,max=1000000
  Visits: Fixed:  key=1
  Row Population Ratio: Ratio: divisor=1.000000;delegate=Fixed:  key=1
  Batch Type: not batching
Columns:
  Max Columns Per Key: 5
  Column Names: [C0, C1, C2, C3, C4]
  Comparator: AsciiType
  Timestamp: null
  Variable Column Count: false
  Slice: false
  Size Distribution: Fixed:  key=34
  Count Distribution: Fixed:  key=5
Errors:
  Ignore: false
  Tries: 10
Log:
  No Summary: false
  No Settings: false
  File: null
  Interval Millis: 1000
  Level: NORMAL
Mode:
  API: JAVA_DRIVER_NATIVE
  Connection Style: CQL_PREPARED
  Protocol Version: V5
  Username: null
  Password: null
  Auth Provide Class: null
  Max Pending Per Connection: 128
  Connections Per Host: 8
  Compression: NONE
Node:
  Nodes: [localhost]
  Is White List: false
  Datacenter: null
Schema:
  Keyspace: keyspace1
  Replication Strategy: org.apache.cassandra.locator.SimpleStrategy
  Replication Strategy Options: {replication_factor=1}
  Table Compression: null
  Table Compaction Strategy: null
  Table Compaction Strategy Options: {}
Transport:
  Truststore: null
  Truststore Password: null
  Keystore: null
  Keystore Password: null
  SSL Protocol: TLS
  SSL Algorithm: null
  SSL Ciphers: TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_256_CBC_SHA
Port:
  Native Port: 9042
  JMX Port: 7199
JMX:
  Username: null
  Password: *not set*
Graph:
  File: null
  Revision: unknown
  Title: null
  Operation: READ
TokenRange:
  Wrap: false
  Split Factor: 1
Credentials file:
  File: *not set*
  CQL username: *not set*
  CQL password: *not set*
  JMX username: *not set*
  JMX password: *not set*
  Transport truststore password: *not set*
  Transport keystore password: *not set*
Reporting:
  Output frequency: 1s
  Header frequency: *not set*

Sleeping 2s...
Warming up READ with 2500 iterations...
Connected to cluster: Test Cluster, max pending requests per connection 128, max connections per host 8
Datacenter: datacenter1; Host: localhost/127.0.0.1:9042; Rack: rack1
Running READ with 50 threads for 10000 iteration
type                                               total ops,    op/s,    pk/s,   row/s,    mean,     med,     .95,     .99,    .999,     max,   time,   stderr, errors,  gc: #,  max ms,  sum ms,  sdv ms,      mb
total,                                                  1540,    1540,    1540,    1540,     8.1,     6.2,    19.2,    38.4,    73.3,    80.9,    1.0,  0.00000,      0,      0,       0,       0,       0,       0
total,                                                  9935,    8395,    8395,    8395,     5.9,     4.2,    16.7,    33.1,    57.3,    86.0,    2.0,  0.48892,      0,      0,       0,       0,       0,       0
total,                                                 10000,    4217,    4217,    4217,     8.5,     4.2,    27.1,    27.4,    27.4,    27.4,    2.0,  1.89747,      0,      0,       0,       0,       0,       0


Results:
Op rate                   :    4,962 op/s  [READ: 4,962 op/s]
Partition rate            :    4,962 pk/s  [READ: 4,962 pk/s]
Row rate                  :    4,962 row/s [READ: 4,962 row/s]
Latency mean              :    6.3 ms [READ: 6.3 ms]
Latency median            :    4.5 ms [READ: 4.5 ms]
Latency 95th percentile   :   17.4 ms [READ: 17.4 ms]
Latency 99th percentile   :   33.4 ms [READ: 33.4 ms]
Latency 99.9th percentile :   59.6 ms [READ: 59.6 ms]
Latency max               :   86.0 ms [READ: 86.0 ms]
Total partitions          :     10,000 [READ: 10,000]
Total errors              :          0 [READ: 0]
Total GC count            : 0
Total GC memory           : 0 B
Total GC time             :    0.0 seconds
Avg GC time               :    NaN ms
StdDev GC time            :    0.0 ms
Total operation time      : 00:00:02

END
```

## Benchmark Results Table Explained:

- **Op rate (operations per second):** The number of read operations Cassandra successfully executed per second.  
- **Partition rate:** Number of partitions read per second. Since this is a read test, the partition rate equals the op rate.  
- **Row rate:** Number of rows read per second. Again, for this test it equals the op rate.  
- **Latency mean:** The average time taken for each read request to complete.  
- **Latency median:** The 50th percentile latency — half of the operations completed faster than this time.  
- **Latency max:** The slowest single read request during the test.  
- **Total partitions:** The total number of partitions read during the test.  
- **Total errors:** Number of failed read operations.  
- **GC metrics (Garbage Collection):** Shows whether JVM garbage collection paused Cassandra during the test.  
- **Total operation time:** The total wall-clock time taken to run the benchmark.  

### Benchmark summary on Arm64
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SuSE shown, Ubuntu results were very similar):

| Metric                     | Write Test             | Read Test              |
|----------------------------|----------------------|----------------------|
| Operation Rate (op/s)       | 10,690               | 4,962                |
| Partition Rate (pk/s)       | 10,690               | 4,962                |
| Row Rate (row/s)            | 10,690               | 4,962                |
| Latency Mean                | 3.7 ms               | 6.3 ms               |
| Latency Median              | 2.8 ms               | 4.5 ms               |
| Latency 95th Percentile     | 9.5 ms               | 17.4 ms              |
| Latency 99th Percentile     | 16.7 ms              | 33.4 ms              |
| Latency 99.9th Percentile   | 28.9 ms              | 59.6 ms              |
| Latency Max                 | 38.4 ms              | 86.0 ms              |
| Total Partitions            | 10,000               | 10,000               |
| Total Errors                | 0                    | 0                    |
| Total GC Count              | 0                    | 0                    |
| Total GC Memory             | 0 B                  | 0 B                  |
| Total GC Time               | 0.0 s                | 0.0 s                |
| Total Operation Time        | 0:00:00              | 0:00:02              |

### Cassendra performance benchmarking notes
When examining the benchmark results, you will notice that on the Google Axion C4A Arm-based instances:

- The write operations achieved a high throughput of **10,690 op/s**, while read operations reached **4,962 op/s** on the `c4a-standard-4` Arm64 VM.  
- Latency for writes was very low (mean: **3.7 ms**) compared to reads (mean: **6.3 ms**), indicating fast write processing on this Arm64 VM.  
- The 95th and 99th percentile latencies show consistent performance, with writes significantly faster than reads.  
- There were no errors or GC overhead, confirming stable and reliable benchmarking results.  

Overall, the Arm64 VM provides efficient and predictable performance, making it suitable for high-throughput Cassandra workloads.
