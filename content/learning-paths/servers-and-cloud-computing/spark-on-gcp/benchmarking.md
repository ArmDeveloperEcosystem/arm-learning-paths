---
title: Spark Internal Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Apache Spark Internal Benchmarking
Apache Spark includes internal micro-benchmarks to evaluate the performance of core components like SQL execution, aggregation, joins, and data source reads. These benchmarks are helpful for comparing platforms such as x86_64 vs Arm64.
Below are the steps to run Spark’s built-in SQL benchmarks using the SBT-based framework.

1. Clone the Apache Spark source code
```console
git clone https://github.com/apache/spark.git
```
This downloads the full Spark source including internal test suites and the benchmarking tools.

2. Checkout the desired Spark version
```console
cd spark/ && git checkout v4.0.0
```
Switch to the stable Spark 4.0.0 release, which supports the latest internal benchmarking APIs.

3. Build Spark with benchmarking profile enabled
```console
./build/sbt -Pbenchmarks clean package
```
This compiles Spark and its dependencies, enabling the benchmarks build profile for performance testing.

4. Run a built-in benchmark suite
```console
./build/sbt -Pbenchmarks "sql/test:runMain org.apache.spark.sql.execution.benchmark.AggregateBenchmark"
```  
This executes the AggregateBenchmark, which compares performance of SQL aggregation operations (e.g., SUM, STDDEV) with and without WholeStageCodegen. WholeStageCodegen is an optimization technique used by Spark SQL to improve the performance of query execution by generating Java bytecode for entire query stages (aka whole stages) instead of interpreting them step-by-step.

You should see an output similar to:
```output
[info] Running benchmark: agg w/o group
[info]   Running case: agg w/o group wholestage off
[info]   Stopped after 2 iterations, 66883 ms
[info]   Running case: agg w/o group wholestage on
[info]   Stopped after 5 iterations, 4283 ms
[info] OpenJDK 64-Bit Server VM 17.0.16+8-LTS on Linux 5.14.0-570.28.1.el9_6.aarch64
[info] 05:36:00.495 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] agg w/o group:                            Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] agg w/o group wholestage off                      32967          33442         672         63.6          15.7       1.0X
[info] agg w/o group wholestage on                         856            857           1       2451.2           0.4      38.5X
[info] Running benchmark: stddev
[info]   Running case: stddev wholestage off
[info]   Stopped after 2 iterations, 7538 ms
[info]   Running case: stddev wholestage on
[info]   Stopped after 5 iterations, 4357 ms
[info] OpenJDK 64-Bit Server VM 17.0.16+8-LTS on Linux 5.14.0-570.28.1.el9_6.aarch64
[info] 05:36:18.982 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] stddev:                                   Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] stddev wholestage off                              3765           3769           5         27.8          35.9       1.0X
[info] stddev wholestage on                                870            872           2        120.6           8.3       4.3X
[info] Running benchmark: kurtosis
[info]   Running case: kurtosis wholestage off
[info]   Stopped after 2 iterations, 38309 ms
[info]   Running case: kurtosis wholestage on
[info]   Stopped after 5 iterations, 4729 ms
[info] OpenJDK 64-Bit Server VM 17.0.16+8-LTS on Linux 5.14.0-570.28.1.el9_6.aarch64
[info] 05:37:24.198 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] kurtosis:                                 Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] kurtosis wholestage off                           19114          19155          58          5.5         182.3       1.0X
[info] kurtosis wholestage on                              943            946           3        111.2           9.0      20.3X
[info] Running benchmark: Aggregate w keys
[info]   Running case: codegen = F
[info]   Stopped after 2 iterations, 11018 ms
[info]   Running case: codegen = T, hashmap = F
[info]   Stopped after 3 iterations, 9331 ms
[info]   Running case: codegen = T, row-based hashmap = T
[info]   Stopped after 5 iterations, 5086 ms
[info]   Running case: codegen = T, vectorized hashmap = T
[info]   Stopped after 5 iterations, 3553 ms
[info] OpenJDK 64-Bit Server VM 17.0.16+8-LTS on Linux 5.14.0-570.28.1.el9_6.aarch64
[info] 05:38:06.612 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] Aggregate w keys:                         Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] -----------------------------------------------------------------------------------------------------------------------            -
[info] codegen = F                                        5401           5509         154         15.5          64.4       1.0X
[info] codegen = T, hashmap = F                           3103           3110           7         27.0          37.0       1.7X
[info] codegen = T, row-based hashmap = T                 1004           1017          11         83.5          12.0       5.4X
[info] codegen = T, vectorized hashmap = T                 707            711           3        118.7           8.4       7.6X
[info] Running benchmark: Aggregate w keys
[info]   Running case: codegen = F
[info]   Stopped after 2 iterations, 10796 ms
[info]   Running case: codegen = T, hashmap = F
[info]   Stopped after 3 iterations, 8988 ms
[info]   Running case: codegen = T, row-based hashmap = T
[info]   Stopped after 5 iterations, 6483 ms
[info]   Running case: codegen = T, vectorized hashmap = T
[info]   Stopped after 5 iterations, 4909 ms
[info] OpenJDK 64-Bit Server VM 17.0.16+8-LTS on Linux 5.14.0-570.28.1.el9_6.aarch64
[info] 05:38:51.375 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] Aggregate w keys:                         Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] codegen = F                                        5374           5398          34         15.6          64.1       1.0X
[info] codegen = T, hashmap = F                           2918           2996          68         28.7          34.8       1.8X
[info] codegen = T, row-based hashmap = T                 1289           1297           8         65.1          15.4       4.2X
[info] codegen = T, vectorized hashmap = T                 978            982           4         85.8          11.7       5.5X
[info] Running benchmark: Aggregate w string key
[info]   Running case: codegen = F
[info]   Stopped after 2 iterations, 3882 ms
[info]   Running case: codegen = T, hashmap = F
[info]   Stopped after 3 iterations, 3624 ms
[info]   Running case: codegen = T, row-based hashmap = T
[info]   Stopped after 5 iterations, 4145 ms
[info]   Running case: codegen = T, vectorized hashmap = T
[info]   Stopped after 5 iterations, 3779 ms
[info] OpenJDK 64-Bit Server VM 17.0.16+8-LTS on Linux 5.14.0-570.28.1.el9_6.aarch64
[info] 05:39:18.280 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] Aggregate w string key:                   Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] -----------------------------------------------------------------------------------------------------------------------            -
[info] codegen = F                                        1938           1941           4         10.8          92.4       1.0X
[info] codegen = T, hashmap = F                           1208           1208           0         17.4          57.6       1.6X
[info] codegen = T, row-based hashmap = T                  820            829           5         25.6          39.1       2.4X
[info] codegen = T, vectorized hashmap = T                 756            756           0         27.8          36.0       2.6X
[info] Running benchmark: Aggregate w decimal key
[info]   Running case: codegen = F
[info]   Stopped after 2 iterations, 3771 ms
[info]   Running case: codegen = T, hashmap = F
[info]   Stopped after 2 iterations, 2231 ms
[info]   Running case: codegen = T, row-based hashmap = T
[info]   Stopped after 5 iterations, 2114 ms
[info]   Running case: codegen = T, vectorized hashmap = T
[info]   Stopped after 8 iterations, 2238 ms
[info] OpenJDK 64-Bit Server VM 17.0.16+8-LTS on Linux 5.14.0-570.28.1.el9_6.aarch64
[info] 05:39:39.289 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] Aggregate w decimal key:                  Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] codegen = F                                        1878           1886          11         11.2          89.6       1.0X
[info] codegen = T, hashmap = F                           1116           1116           0         18.8          53.2       1.7X
[info] codegen = T, row-based hashmap = T                  411            423          11         51.0          19.6       4.6X
[info] codegen = T, vectorized hashmap = T                 278            280           2         75.4          13.3       6.8X
[info] Running benchmark: Aggregate w multiple keys
[info]   Running case: codegen = F
[info]   Stopped after 2 iterations, 6554 ms
[info]   Running case: codegen = T, hashmap = F
[info]   Stopped after 2 iterations, 3608 ms
[info]   Running case: codegen = T, row-based hashmap = T
[info]   Stopped after 2 iterations, 2936 ms
[info]   Running case: codegen = T, vectorized hashmap = T
[info]   Stopped after 2 iterations, 2569 ms
[info] OpenJDK 64-Bit Server VM 17.0.16+8-LTS on Linux 5.14.0-570.28.1.el9_6.aarch64
[info] 05:40:06.514 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] Aggregate w multiple keys:                Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] codegen = F                                        3272           3277           8          6.4         156.0       1.0X
[info] codegen = T, hashmap = F                           1802           1804           3         11.6          85.9       1.8X
[info] codegen = T, row-based hashmap = T                 1461           1468          10         14.4          69.7       2.2X
[info] codegen = T, vectorized hashmap = T                1283           1285           3         16.4          61.2       2.6X
[info] Running benchmark: max function bytecode size
[info]   Running case: codegen = F
[info]   Stopped after 8 iterations, 2146 ms
[info]   Running case: codegen = T, hugeMethodLimit = 10000
[info]   Stopped after 14 iterations, 2072 ms
[info]   Running case: codegen = T, hugeMethodLimit = 1500
[info]   Stopped after 16 iterations, 2112 ms
[info] OpenJDK 64-Bit Server VM 17.0.16+8-LTS on Linux 5.14.0-570.28.1.el9_6.aarch64
[info] 05:40:19.258 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] max function bytecode size:               Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] codegen = F                                         263            268           4          2.5         401.6       1.0X
[info] codegen = T, hugeMethodLimit = 10000                143            148           8          4.6         217.4       1.8X
[info] codegen = T, hugeMethodLimit = 1500                 129            132           3          5.1         196.6       2.0X
[info] Running benchmark: cube
[info]   Running case: cube wholestage off
[info]   Stopped after 2 iterations, 3164 ms
[info]   Running case: cube wholestage on
[info]   Stopped after 5 iterations, 4215 ms
[info] OpenJDK 64-Bit Server VM 17.0.16+8-LTS on Linux 5.14.0-570.28.1.el9_6.aarch64
[info] 05:40:32.879 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] cube:                                     Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] cube wholestage off                                1572           1582          14          3.3         299.9       1.0X
[info] cube wholestage on                                  841            843           2          6.2         160.4       1.9X
[info] Running benchmark: BytesToBytesMap
[info]   Running case: UnsafeRowhash
[info]   Stopped after 15 iterations, 2052 ms
[info]   Running case: murmur3 hash
[info]   Stopped after 42 iterations, 2003 ms
[info]   Running case: fast hash
[info]   Stopped after 48 iterations, 2016 ms
[info]   Running case: arrayEqual
[info]   Stopped after 29 iterations, 2064 ms
[info]   Running case: Java HashMap (Long)
[info]   Stopped after 8 iterations, 2209 ms
[info]   Running case: Java HashMap (two ints)
[info]   Stopped after 8 iterations, 2217 ms
[info]   Running case: Java HashMap (UnsafeRow)
[info]   Stopped after 4 iterations, 2039 ms
[info]   Running case: LongToUnsafeRowMap (opt=false)
[info]   Stopped after 9 iterations, 2144 ms
[info]   Running case: LongToUnsafeRowMap (opt=true)
[info]   Stopped after 26 iterations, 2005 ms
[info]   Running case: BytesToBytesMap (off Heap)
[info]   Stopped after 5 iterations, 2368 ms
[info]   Running case: BytesToBytesMap (on Heap)
[info]   Stopped after 4 iterations, 2023 ms
[info]   Running case: Aggregate HashMap
[info]   Stopped after 87 iterations, 2011 ms
[info] OpenJDK 64-Bit Server VM 17.0.16+8-LTS on Linux 5.14.0-570.28.1.el9_6.aarch64
[info] 05:41:23.750 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] BytesToBytesMap:                          Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] UnsafeRowhash                                       137            137           0        153.6           6.5       1.0X
[info] murmur3 hash                                         48             48           0        440.6           2.3       2.9X
[info] fast hash                                            42             42           0        499.2           2.0       3.3X
[info] arrayEqual                                           71             71           0        296.8           3.4       1.9X
[info] Java HashMap (Long)                                 269            276           6         78.0          12.8       0.5X
[info] Java HashMap (two ints)                             273            277           2         76.7          13.0       0.5X
[info] Java HashMap (UnsafeRow)                            507            510           3         41.4          24.2       0.3X
[info] LongToUnsafeRowMap (opt=false)                      237            238           0         88.3          11.3       0.6X
[info] LongToUnsafeRowMap (opt=true)                        76             77           1        277.1           3.6       1.8X
[info] BytesToBytesMap (off Heap)                          472            474           2         44.4          22.5       0.3X
[info] BytesToBytesMap (on Heap)                           505            506           1         41.6          24.1       0.3X
[info] Aggregate HashMap                                    23             23           0        913.0           1.1       5.9X
[success] Total time: 669 s (11:09), completed Jul 24, 2025, 5:41:24 AM

```
### Benchmark Results Table Explained:

- **Best Time (ms):** Fastest execution time observed (in milliseconds).
- **Avg Time (ms):** Average time across all iterations.
- **Stdev (ms):** Standard deviation of execution times (lower is more stable).
- **Rate (M/s):** Rows processed per second in millions.
- **Per Row (ns):** Average time taken per row (in nanoseconds).
- **Relative Speed comparison:** baseline (1.0X) is the slower version.

### Benchmark summary on x86_64:
The following  benchmark results are collected on a c3-standard-4 (4 vCPU, 2 core, 16 GB Memory) x86_64 environment, running RHEL 9.

| **Benchmark Case**         | **Sub-Case / Config**                | **Best Time (ms)** | **Avg Time (ms)** | **Stdev (ms)** | **Rate (M/s)** | **Per Row (ns)** | **Relative** |
|---------------------------|--------------------------------------|--------------------|-------------------|----------------|----------------|------------------|--------------|
| agg w/o group             | wholestage off                       | 30044              | 32090             | 2892           | 69.8           | 14.3             | 1.0X         |
| agg w/o group             | wholestage on                        | 2728               | 2739              | 7              | 768.7          | 1.3              | 11.0X        |
| stddev                    | wholestage off                       | 4097               | 4112              | 21             | 25.6           | 39.1             | 1.0X         |
| stddev                    | wholestage on                        | 948                | 954               | 4              | 110.6          | 9.0              | 4.3X         |
| kurtosis                  | wholestage off                       | 21658              | 21664             | 9              | 4.8            | 206.5            | 1.0X         |
| kurtosis                  | wholestage on                        | 1327               | 1335              | 7              | 79.0           | 12.7             | 16.3X        |
| Aggregate w keys          | codegen = F                          | 7233               | 7234              | 1              | 11.6           | 86.2             | 1.0X         |
| Aggregate w keys          | codegen = T, hashmap = F             | 4556               | 4570              | 21             | 18.4           | 54.3             | 1.6X         |
| Aggregate w keys          | codegen = T, row-based hashmap = T   | 1201               | 1205              | 6              | 69.8           | 14.3             | 6.0X         |
| Aggregate w keys          | codegen = T, vectorized hashmap = T  | 702                | 715               | 10             | 119.6          | 8.4              | 10.3X        |
| Aggregate w keys          | codegen = F                          | 6439               | 6524              | 119            | 13.0           | 76.8             | 1.0X         |
| Aggregate w keys          | codegen = T, hashmap = F             | 4156               | 4170              | 12             | 20.2           | 49.5             | 1.5X         |
| Aggregate w keys          | codegen = T, row-based hashmap = T   | 2113               | 2126              | 19             | 39.7           | 25.2             | 3.0X         |
| Aggregate w keys          | codegen = T, vectorized hashmap = T  | 1310               | 1322              | 8              | 64.0           | 15.6             | 4.9X         |
| Aggregate w string key    | codegen = F                          | 2265               | 2268              | 4              | 9.3            | 108.0            | 1.0X         |
| Aggregate w string key    | codegen = T, hashmap = F             | 1926               | 1941              | 20             | 10.9           | 91.8             | 1.2X         |
| Aggregate w string key    | codegen = T, row-based hashmap = T   | 1280               | 1285              | 8              | 16.4           | 61.0             | 1.8X         |
| Aggregate w string key    | codegen = T, vectorized hashmap = T  | 1118               | 1123              | 7              | 18.8           | 53.3             | 2.0X         |
| Aggregate w decimal key   | codegen = F                          | 2139               | 2167              | 40             | 9.8            | 102.0            | 1.0X         |
| Aggregate w decimal key   | codegen = T, hashmap = F             | 1475               | 1488              | 18             | 14.2           | 70.3             | 1.5X         |
| Aggregate w decimal key   | codegen = T, row-based hashmap = T   | 447                | 451               | 6              | 46.9           | 21.3             | 4.8X         |
| Aggregate w decimal key   | codegen = T, vectorized hashmap = T  | 270                | 275               | 5              | 77.6           | 12.9             | 7.9X         |
| Aggregate w multiple keys | codegen = F                          | 3788               | 3834              | 65             | 5.5            | 180.6            | 1.0X         |
| Aggregate w multiple keys | codegen = T, hashmap = F             | 2412               | 2423              | 16             | 8.7            | 115.0            | 1.6X         |
| Aggregate w multiple keys | codegen = T, row-based hashmap = T   | 1890               | 1895              | 6              | 11.1           | 90.1             | 2.0X         |
| Aggregate w multiple keys | codegen = T, vectorized hashmap = T  | 1739               | 1766              | 38             | 12.1           | 82.9             | 2.2X         |
| max func bytecode size    | codegen = F                          | 315                | 338               | 24             | 2.1            | 480.7            | 1.0X         |
| max func bytecode size    | codegen = T, hugeMethodLimit = 10000 | 178                | 200               | 13             | 3.7            | 272.3            | 1.8X         |
| max func bytecode size    | codegen = T, hugeMethodLimit = 1500  | 174                | 188               | 22             | 3.8            | 264.8            | 1.8X         |
| cube                      | wholestage off                       | 1864               | 1867              | 5              | 2.8            | 355.5            | 1.0X         |
| cube                      | wholestage on                        | 1060               | 1075              | 16             | 4.9            | 202.2            | 1.8X         |
| BytesToBytesMap           | UnsafeRowhash                        | 204                | 204               | 0              | 103.0          | 9.7              | 1.0X         |
| BytesToBytesMap           | murmur3 hash                         | 69                 | 69                | 0              | 304.1          | 3.3              | 3.0X         |
| BytesToBytesMap           | fast hash                            | 41                 | 42                | 1              | 517.4          | 1.9              | 5.0X         |
| BytesToBytesMap           | arrayEqual                           | 142                | 142               | 0              | 148.0          | 6.8              | 1.4X         |
| BytesToBytesMap           | Java HashMap (Long)                  | 65                 | 72                | 5              | 323.6          | 3.1              | 3.1X         |
| BytesToBytesMap           | Java HashMap (two ints)              | 89                 | 93                | 2              | 235.4          | 4.2              | 2.3X         |
| BytesToBytesMap           | Java HashMap (UnsafeRow)             | 544                | 546               | 2              | 38.5           | 26.0             | 0.4X         |
| BytesToBytesMap           | LongToUnsafeRowMap (opt=false)       | 352                | 355               | 1              | 59.5           | 16.8             | 0.6X         |
| BytesToBytesMap           | LongToUnsafeRowMap (opt=true)        | 74                 | 75                | 1              | 284.6          | 3.5              | 2.8X         |
| BytesToBytesMap           | BytesToBytesMap (off Heap)           | 623                | 628               | 7              | 33.7           | 29.7             | 0.3X         |
| BytesToBytesMap           | BytesToBytesMap (on Heap)            | 624                | 627               | 3              | 33.6           | 29.8             | 0.3X         |
| BytesToBytesMap           | Aggregate HashMap                    | 31                 | 31                | 0              | 680.7          | 1.5              | 6.6X         |


### Benchmark summary on Arm64:
The following  benchmark results are collected on a c4a-standard-4 (4 vCPU, 16 GB Memory) Arm64 environment, running RHEL 9.

| Benchmark Case             | Sub-Case / Config        | Best Time (ms) | Avg Time (ms) | Stdev (ms) | Rate (M/s) | Per Row (ns) | Relative |
|----------------------------|--------------------------|----------------|----------------|------------|-------------|----------------|-----------|
| agg w/o group              | wholestage off           | 32967          | 33442          | 672        | 63.6        | 15.7           | 1.0X      |
| agg w/o group              | wholestage on            | 856            | 857            | 1          | 2451.2      | 0.4            | 38.5X     |
| stddev                     | wholestage off           | 3765           | 3769           | 5          | 27.8        | 35.9           | 1.0X       |
| stddev                     | wholestage on            | 870            | 872            | 2          | 120.6       | 8.3            | 4.3X       |
| kurtosis                   | wholestage off           | 19114          | 19155          | 58         | 5.5         | 182.3          | 1.0X       |
| kurtosis                   | wholestage on            | 943            | 946            | 3          | 111.2       | 9.0            | 20.3X      |
| Aggregate w/ keys          | codegen = F              | 5401           | 5509           | 154        | 15.5        | 64.4           | 1.0X     |
| Aggregate w/ keys          | codegen = T, hashmap = F | 3103           | 3110           | 7          | 27.0        | 37.0           | 1.7X      |
| Aggregate w/ keys          | row-based hashmap = T    | 1004           | 1017           | 11         | 83.5        | 12.0           | 5.4X       |
| Aggregate w/ keys          | vectorized hashmap = T   | 707            | 711            | 3          | 118.7       | 8.4            | 7.6X      |
| Aggregate w/ string key    | codegen = F              | 1938           | 1941           | 4          | 10.8        | 92.4           | 1.0X      |
| Aggregate w/ string key    | codegen = T, hashmap = F | 1208           | 1208           | 0          | 17.4        | 57.6           | 1.6X      |
| Aggregate w/ string key    | row-based hashmap = T    | 820            | 829            | 5          | 25.6        | 39.1           | 2.4X      |
| Aggregate w/ string key    | vectorized hashmap = T   | 756            | 756            | 0          | 27.8        | 36.0           | 2.6X       |
| Aggregate w/ decimal key   | codegen = F              | 1878           | 1886           | 11         | 11.2        | 89.6           | 1.0X       |
| Aggregate w/ decimal key   | codegen = T, hashmap = F | 1116           | 1116           | 0          | 18.8        | 53.2           | 1.7X       |
| Aggregate w/ decimal key   | row-based hashmap = T    | 411            | 423            | 11         | 51.0        | 19.6           | 4.6X      |
| Aggregate w/ decimal key   | vectorized hashmap = T   | 278            | 280            | 2          | 75.4        | 13.3           | 6.8X      |
| Aggregate w/ multiple keys | codegen = F              | 3272           | 3277           | 8          | 6.4         | 156.0          | 1.0X      |
| Aggregate w/ multiple keys | codegen = T, hashmap = F | 1802           | 1804           | 3          | 11.6        | 85.9           | 1.8X      |
| Aggregate w/ multiple keys | row-based hashmap = T    | 1461           | 1468           | 10         | 14.4        | 69.7           | 2.2X      |
| Aggregate w/ multiple keys | vectorized hashmap = T   | 1283           | 1285           | 3          | 16.4        | 61.2           | 2.6X      |
| Max function bytecode size | codegen = F              | 263            | 268            | 4          | 2.5         | 401.6          | 1.0X      |
| Max function bytecode size | hugeMethodLimit = 10000  | 143            | 148            | 8          | 4.6         | 217.4          | 1.8X      |
| Max function bytecode size | hugeMethodLimit = 1500   | 129            | 132            | 3          | 5.1         | 196.6          | 2.0X      |
| Cube                       | wholestage off           | 1572           | 1582           | 14         | 3.3         | 299.9          | 1.0X      |
| Cube                       | wholestage on            | 841            | 843            | 2          | 6.2         | 160.4          | 1.9X      |
| BytesToBytesMap            | UnsafeRowhash            | 137            | 137            | 0          | 153.6       | 6.5            | 1.0X      |
| BytesToBytesMap            | murmur3 hash             | 48             | 48             | 0          | 440.6       | 2.3            | 2.9X      |
| BytesToBytesMap            | fast hash                | 42             | 42             | 0          | 499.2       | 2.0            | 3.3X      |
| BytesToBytesMap    |Aggregate HashMap                 | 23             | 23             | 0          | 913.0       | 1.1            | 5.9X      |

### **Highlights from GCP C4A Arm virtual machine**

- **Whole-stage code generation significantly boosts performance**, improving execution by up to **38×** (e.g., `agg w/o group` from 33.4s to 0.86s).
- **Vectorized and row-based hash maps** consistently outperform non-codegen and traditional hashmap approaches, especially for aggregation with keys and complex data types (e.g., decimal keys: **6.8× faste**r with vectorized hashmap).
- **Arm-based Spark shows strong hash performance**, with `fast hash` and `murmur3` achieving up to **3.3× better throughput** than UnsafeRowhash.
 
