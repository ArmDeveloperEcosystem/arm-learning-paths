---
title: Benchmark Apache Spark on Azure Cobalt 100 Arm64 and x86_64
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark Apache Spark on Azure Cobalt 100 Arm64 and x86_64

Apache Spark includes internal micro-benchmarks to evaluate the performance of core components such as SQL execution, aggregation, joins, and data source reads. These benchmarks are useful for comparing performance on Arm64 and x86_64 platforms in Azure.

This section shows you how to run Spark’s built-in SQL benchmarks using the SBT-based framework.

## Steps to run Spark benchmarks

1. Clone the Apache Spark source code  

   ```console
   git clone https://github.com/apache/spark.git
   ```
   This downloads the full Spark source code, including test suites and benchmarking tools  

2. Checkout the desired Spark version  

   ```console
   cd spark/ && git checkout v4.0.0
   ```
   Switch to the stable Spark 4.0.0 release, which supports the latest benchmarking APIs  

3. Build Spark with the benchmarking profile  

   ```console
   ./build/sbt -Pbenchmarks clean package
   ```
   This compiles Spark and its dependencies, enabling the benchmarking build profile  

4. Run a built-in benchmark suite  

   ```console
   ./build/sbt -Pbenchmarks "sql/test:runMain org.apache.spark.sql.execution.benchmark.JoinBenchmark"
   ```
   This runs the `JoinBenchmark`, which measures the performance of SQL join operations such as `SortMergeJoin` and `BroadcastHashJoin`. It evaluates how Spark SQL optimizes join strategies, especially with and without WholeStageCodegen  

## Example Apache Spark benchmark output

You should see output similar to the following:

```output
[info] Running benchmark: Join w long
[info]   Running case: Join w long wholestage off
[info]   Stopped after 2 iterations, 5297 ms
[info]   Running case: Join w long wholestage on
[info]   Stopped after 5 iterations, 4238 ms
[info] OpenJDK 64-Bit Server VM 17.0.15+6-LTS on Linux 6.6.92.2-2.azl3
[info] 06:05:52.695 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] Join w long:                              Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] Join w long wholestage off                         2345           2649         429          8.9         111.8       1.0X
[info] Join w long wholestage on                           842            848           5         24.9          40.2       2.8X
[info] Running benchmark: Join w long duplicated
[info]   Running case: Join w long duplicated wholestage off
[info]   Stopped after 2 iterations, 3931 ms
[info]   Running case: Join w long duplicated wholestage on
[info]   Stopped after 5 iterations, 4350 ms
[info] OpenJDK 64-Bit Server VM 17.0.15+6-LTS on Linux 6.6.92.2-2.azl3
[info] 06:06:05.954 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] Join w long duplicated:                   Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] Join w long duplicated wholestage off              1965           1966           1         10.7          93.7       1.0X
[info] Join w long duplicated wholestage on                865            870           4         24.2          41.3       2.3X
[info] Running benchmark: Join w 2 ints
[info]   Running case: Join w 2 ints wholestage off
[info]   Stopped after 2 iterations, 216362 ms
[info]   Running case: Join w 2 ints wholestage on
[info]   Stopped after 5 iterations, 538414 ms
[info] OpenJDK 64-Bit Server VM 17.0.15+6-LTS on Linux 6.6.92.2-2.azl3
[info] 06:22:16.697 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] Join w 2 ints:                            Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] Join w 2 ints wholestage off                     108110         108181         101          0.2        5155.1       1.0X
[info] Join w 2 ints wholestage on                      107521         107683         109          0.2        5127.0       1.0X
[info] Running benchmark: Join w 2 longs
[info]   Running case: Join w 2 longs wholestage off
[info]   Stopped after 2 iterations, 7806 ms
[info]   Running case: Join w 2 longs wholestage on
[info]   Stopped after 5 iterations, 10771 ms
[info] OpenJDK 64-Bit Server VM 17.0.15+6-LTS on Linux 6.6.92.2-2.azl3
[info] 06:22:41.568 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] Join w 2 longs:                           Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] Join w 2 longs wholestage off                      3867           3903          51          5.4         184.4       1.0X
[info] Join w 2 longs wholestage on                       2061           2154         113         10.2          98.3       1.9X
[info] Running benchmark: Join w 2 longs duplicated
[info]   Running case: Join w 2 longs duplicated wholestage off
[info]   Stopped after 2 iterations, 17850 ms
[info]   Running case: Join w 2 longs duplicated wholestage on
[info]   Stopped after 5 iterations, 26145 ms
[info] OpenJDK 64-Bit Server VM 17.0.15+6-LTS on Linux 6.6.92.2-2.azl3
[info] 06:23:40.009 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] Join w 2 longs duplicated:                Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] Join w 2 longs duplicated wholestage off           8923           8925           4          2.4         425.5       1.0X
[info] Join w 2 longs duplicated wholestage on            5224           5229           8          4.0         249.1       1.7X
[info] Running benchmark: outer join w long
[info]   Running case: outer join w long wholestage off
[info]   Stopped after 2 iterations, 3070 ms
[info]   Running case: outer join w long wholestage on
[info]   Stopped after 5 iterations, 4178 ms
[info] OpenJDK 64-Bit Server VM 17.0.15+6-LTS on Linux 6.6.92.2-2.azl3
[info] 06:23:52.993 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] outer join w long:                        Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] outer join w long wholestage off                   1531           1535           6         13.7          73.0       1.0X
[info] outer join w long wholestage on                     833            836           3         25.2          39.7       1.8X
[info] Running benchmark: semi join w long
[info]   Running case: semi join w long wholestage off
[info]   Stopped after 2 iterations, 2152 ms
[info]   Running case: semi join w long wholestage on
[info]   Stopped after 5 iterations, 2569 ms
[info] OpenJDK 64-Bit Server VM 17.0.15+6-LTS on Linux 6.6.92.2-2.azl3
[info] 06:24:02.077 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] semi join w long:                         Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] semi join w long wholestage off                    1069           1076          10         19.6          51.0       1.0X
[info] semi join w long wholestage on                      512            514           2         40.9          24.4       2.1X
[info] Running benchmark: sort merge join
[info]   Running case: sort merge join wholestage off
[info]   Stopped after 2 iterations, 1106 ms
[info]   Running case: sort merge join wholestage on
[info]   Stopped after 5 iterations, 2406 ms
[info] OpenJDK 64-Bit Server VM 17.0.15+6-LTS on Linux 6.6.92.2-2.azl3
[info] 06:24:10.485 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] sort merge join:                          Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] sort merge join wholestage off                      551            553           3          3.8         262.7       1.0X
[info] sort merge join wholestage on                       478            481           3          4.4         227.8       1.2X
[info] Running benchmark: sort merge join with duplicates
[info]   Running case: sort merge join with duplicates wholestage off
[info]   Stopped after 2 iterations, 2426 ms
[info]   Running case: sort merge join with duplicates wholestage on
[info]   Stopped after 5 iterations, 5285 ms
[info] OpenJDK 64-Bit Server VM 17.0.15+6-LTS on Linux 6.6.92.2-2.azl3
[info] 06:24:23.172 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] sort merge join with duplicates:                Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------------
[info] sort merge join with duplicates wholestage off           1207           1213           9          1.7         575.4       1.0X
[info] sort merge join with duplicates wholestage on            1029           1057          18          2.0         490.5       1.2X
[info] Running benchmark: shuffle hash join
[info]   Running case: shuffle hash join wholestage off
[info]   Stopped after 2 iterations, 1170 ms
[info]   Running case: shuffle hash join wholestage on
[info]   Stopped after 5 iterations, 2037 ms
[info] OpenJDK 64-Bit Server VM 17.0.15+6-LTS on Linux 6.6.92.2-2.azl3
[info] 06:24:31.312 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] shuffle hash join:                        Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] ------------------------------------------------------------------------------------------------------------------------
[info] shuffle hash join wholestage off                    578            585           9          7.3         137.9       1.0X
[info] shuffle hash join wholestage on                     385            408          13         10.9          91.8       1.5X
[info] Running benchmark: broadcast nested loop join
[info]   Running case: broadcast nested loop join wholestage off
[info]   Stopped after 2 iterations, 53739 ms
[info]   Running case: broadcast nested loop join wholestage on
[info]   Stopped after 5 iterations, 94642 ms
[info] OpenJDK 64-Bit Server VM 17.0.15+6-LTS on Linux 6.6.92.2-2.azl3
[info] 06:27:45.952 ERROR org.apache.spark.util.Utils: Process List(/usr/bin/grep, -m, 1, model name, /proc/cpuinfo) exited with code 1:
[info] Unknown processor
[info] broadcast nested loop join:                Best Time(ms)   Avg Time(ms)   Stdev(ms)    Rate(M/s)   Per Row(ns)   Relative
[info] -------------------------------------------------------------------------------------------------------------------------
[info] broadcast nested loop join wholestage off          26847          26870          32          0.8        1280.2       1.0X
[info] broadcast nested loop join wholestage on           18857          18928          84          1.1         899.2       1.4X
[success] Total time: 1644 s (27:24), completed Jul 25, 2025, 6:27:46 AM
```
### Benchmark Results Table Explained:

- **Best Time (ms):** Fastest execution time observed (in milliseconds).
- **Avg Time (ms):** Average time across all iterations.
- **Stdev (ms):** Standard deviation of execution times (lower is more stable).
- **Rate (M/s):** Rows processed per second in millions.
- **Per Row (ns):** Average time taken per row (in nanoseconds).
- **Relative Speed comparison:** baseline (1.0X) is the slower version.

{{% notice Note %}}
Benchmarks were performed in both an Azure Linux 3.0 Docker container and an Azure Linux 3.0 virtual machine. Results were found to be comparable.
{{% /notice %}}


### Benchmark summary on Arm64:
For easier comparison, shown here is a summary of benchmark results collected on an Arm64 `D4ps_v6` Azure virtual machine created from a custom Azure Linux 3.0 image using the AArch64 ISO.
| Benchmark                              | Wholestage | Best Time (ms) | Avg Time (ms) | Stdev (ms) | Rate (M/s) | Per Row (ns) | Relative |
|----------------------------------------|------------|----------------|----------------|------------|-------------|----------------|----------|
| Join w long                             | Off        | 2345           | 2649           | 429        | 8.9         | 111.8          | 1.0X     |
|                                        | On         | 842            | 848            | 5          | 24.9        | 40.2           | 2.8X     |
| Join w long duplicated                  | Off        | 1965           | 1966           | 1          | 10.7        | 93.7           | 1.0X     |
|                                        | On         | 865            | 870            | 4          | 24.2        | 41.3           | 2.3X     |
| Join w 2 ints                           | Off        | 108110         | 108181         | 101        | 0.2         | 5155.1         | 1.0X     |
|                                        | On         | 107521         | 107683         | 109        | 0.2         | 5127.0         | 1.0X     |
| Join w 2 longs                          | Off        | 3867           | 3903           | 51         | 5.4         | 184.4          | 1.0X     |
|                                        | On         | 2061           | 2154           | 113        | 10.2        | 98.3           | 1.9X     |
| Join w 2 longs duplicated               | Off        | 8923           | 8925           | 4          | 2.4         | 425.5          | 1.0X     |
|                                        | On         | 5224           | 5229           | 8          | 4.0         | 249.1          | 1.7X     |
| Outer join w long                       | Off        | 1531           | 1535           | 6          | 13.7        | 73.0           | 1.0X     |
|                                        | On         | 833            | 836            | 3          | 25.2        | 39.7           | 1.8X     |
| Semi join w long                        | Off        | 1069           | 1076           | 10         | 19.6        | 51.0           | 1.0X     |
|                                        | On         | 512            | 514            | 2          | 40.9        | 24.4           | 2.1X     |
| Sort merge join                         | Off        | 551            | 553            | 3          | 3.8         | 262.7          | 1.0X     |
|                                        | On         | 478            | 481            | 3          | 4.4         | 227.8          | 1.2X     |
| Sort merge join with duplicates         | Off        | 1207           | 1213           | 9          | 1.7         | 575.4          | 1.0X     |
|                                        | On         | 1029           | 1057           | 18         | 2.0         | 490.5          | 1.2X     |
| Shuffle hash join                       | Off        | 578            | 585            | 9          | 7.3         | 137.9          | 1.0X     |
|                                        | On         | 385            | 408            | 13         | 10.9        | 91.8           | 1.5X     |
| Broadcast nested loop join             | Off        | 26847          | 26870          | 32         | 0.8         | 1280.2         | 1.0X     |
|                                        | On         | 18857          | 18928          | 84         | 1.1         | 899.2          | 1.4X     |

### Benchmark summary on x86_64:
Shown here is a summary of the benchmark results collected on an `x86_64` `D4s_v4` Azure virtual machine using the Azure Linux 3.0 image published by Ntegral Inc.
| Benchmark                                | Wholestage | Best Time (ms) | Avg Time (ms) | Stdev (ms) | Rate (M/s) | Per Row (ns) | Relative |
|------------------------------------------|------------|----------------|----------------|------------|-------------|----------------|----------|
| Join w long                               | Off        | 3168           | 3185           | 24         | 6.6         | 151.1          | 1.0X     |
|                                           | On         | 1509           | 1562           | 61         | 13.9        | 72.0           | 2.1X     |
| Join w long duplicated                    | Off        | 2490           | 2504           | 20         | 8.4         | 118.7          | 1.0X     |
|                                           | On         | 1151           | 1181           | 27         | 18.2        | 54.9           | 2.2X     |
| Join w 2 ints                             | Off        | 217074         | 219364         | 3239       | 0.1         | 10350.9        | 1.0X     |
|                                           | On         | 119692         | 119756         | 74         | 0.2         | 5707.4         | 1.8X     |
| Join w 2 longs                            | Off        | 4367           | 4401           | 49         | 4.8         | 208.2          | 1.0X     |
|                                           | On         | 2952           | 3003           | 35         | 7.1         | 140.8          | 1.5X     |
| Join w 2 longs duplicated                 | Off        | 10255          | 10286          | 45         | 2.0         | 489.0          | 1.0X     |
|                                           | On         | 7243           | 7300           | 36         | 2.9         | 345.4          | 1.4X     |
| Outer join w long                         | Off        | 2401           | 2422           | 30         | 8.7         | 114.5          | 1.0X     |
|                                           | On         | 1544           | 1564           | 17         | 13.6        | 73.6           | 1.6X     |
| Semi join w long                          | Off        | 1344           | 1350           | 8          | 15.6        | 64.1           | 1.0X     |
|                                           | On         | 673            | 685            | 12         | 31.2        | 32.1           | 2.0X     |
| Sort merge join                           | Off        | 1144           | 1145           | 1          | 1.8         | 545.6          | 1.0X     |
|                                           | On         | 1177           | 1228           | 46         | 1.8         | 561.4          | 1.0X     |
| Sort merge join w/ duplicates             | Off        | 2075           | 2113           | 55         | 1.0         | 989.4          | 1.0X     |
|                                           | On         | 1704           | 1720           | 14         | 1.2         | 812.3          | 1.2X     |
| Shuffle hash join                         | Off        | 672            | 674            | 2          | 6.2         | 160.3          | 1.0X     |
|                                           | On         | 524            | 525            | 1          | 8.0         | 124.9          | 1.3X     |
| Broadcast nested loop join               | Off        | 36060          | 36103          | 62         | 0.6         | 1719.5         | 1.0X     |
|                                           | On         | 31254          | 31346          | 78         | 0.7         | 1490.3         | 1.2X     |


### Benchmark comparison insights

When comparing the results on Arm64 vs x86_64 virtual machines:

- Whole-stage codegen improves performance by up to 2.8× on complex joins  
- Simple joins, such as integer joins, show negligible performance differences  
- Broadcast and shuffle-based joins achieve 1.4× to 1.5× improvements  
- Enabling whole-stage codegen consistently improves performance across most join types  

You have now benchmarked Apache Spark on an Azure Cobalt 100 Arm64 virtual machine and compared results with x86_64.
