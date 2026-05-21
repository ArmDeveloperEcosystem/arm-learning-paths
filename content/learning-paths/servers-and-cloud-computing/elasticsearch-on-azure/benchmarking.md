---
title: Benchmark Elasticsearch using ESRally on the Cobalt 100 virtual machine instance

weight: 5

layout: "learningpathall"
---

## Use ESRally to measure Elasticsearch performance

ESRally is designed to benchmark Elasticsearch instances. It uses a race model where a selected track exercises specific indexing and query patterns. In this section, you'll run the geonames track to benchmark your Elasticsearch deployment.

### The geonames track in ESRally

The geonames track is a general-purpose Elasticsearch workload based on the GeoNames dataset. ESRally indexes millions of location records and runs representative search operations so you can measure indexing throughput and query latency under mixed ingest and search conditions.

### Run the benchmark

Run the benchmark command from the virtual machine. Replace `9.4.0` with the Elasticsearch version you confirmed in the previous section:

```bash
esrally race --distribution-version=9.4.0 --track=geonames --kill-running-processes
```

By default, ESRally downloads and manages its own Elasticsearch process for the duration of the benchmark. It does not use the Elasticsearch instance you started with `systemctl`. The `--distribution-version` flag tells ESRally which Elasticsearch version to download and run. The `--kill-running-processes` flag stops any existing Elasticsearch processes before starting, including the one started by `systemctl`, so there is no port conflict on 9200.

{{% notice Note %}}
This benchmarking test takes approximately 85-90 minutes to complete on an E4pds_v6 instance. To avoid skewing the results, don't interrupt or pause the benchmark.
{{% /notice %}}

## Interpret the benchmark results

The following sample output shows a baseline geonames run on an Azure Cobalt 100 E4pds_v6 virtual machine. Your results will be similar but might vary slightly depending on VM load, Elasticsearch version, and available memory. 

Indexing sustained a mean of about 61,054 docs/s with 0% errors. Common read-path workloads such as default search, term search, phrase search, and cached aggregation stayed in an excellent 3-4 ms p50 range.

The system completed the run without any old-generation garbage collections, suggesting healthy JVM behavior under this benchmark. The main latency costs appeared in heavier workloads such as uncached aggregation, scroll, expression queries, and script-based scoring. This is consistent with Elasticsearch performance expectations for compute-intensive query patterns.

### Example performance summary

![Screenshot of ESRally geonames summary output with throughput and latency metrics for a Cobalt 100 Arm VM. Use this table to confirm your run completed and produced baseline results.#center](images/performance-1.png "Performance summary for the E4pds_v6 Arm64 Cobalt 100 VM")

### Example detailed metrics

![Screenshot of detailed ESRally geonames metrics including query types, p50 latency, and GC data. Review these values to identify the heaviest operations in your workload.#center](images/performance-2.png "Performance details on the E4pds_v6 Arm64 Cobalt 100 VM")

### Key findings

- Indexing throughput averaged 61,054 docs/s (min 58,586 docs/s, max 64,191 docs/s) and completed with 0% errors.
- Common search workloads were consistently fast, with default, term, and phrase queries all clustered around 3-4 ms p50 latency.
- Caching made a major difference for aggregation: Cached country aggregation was about 36.5x faster than uncached at p50 latency (2.88 ms vs 105.1 ms).
- Scripted scoring remained expensive: `field_value_script_score` was about 1.39x slower than `field_value_function_score` at p50 latency (197.8 ms vs 142.1 ms). `painless_static` was the slowest task in the run at 410.9 ms p50, slightly ahead of `painless_dynamic` at 384.9 ms p50.
- Scroll and uncached aggregation were the most notable non-script latency costs at about 222 ms and 105 ms p50 latency, respectively.
- JVM behavior looked stable: 983 young-generation collections consumed 6.40 seconds total, and there were no old-generation collections.
- Merge work totaled 3.34 minutes with 1.25 minutes of throttle time, indicating some ingest-side background pressure but not a throughput collapse.
- The final store footprint matched the dataset size at 2.67 GB, suggesting low additional storage overhead in this run.

### Conclusions

This benchmark result supports the view that Azure Cobalt 100 E4pds_v6 is capable of delivering strong Elasticsearch baseline performance for the geonames track, especially for ordinary search, sort, and cached aggregation paths. Indexing sustained over 61,000 docs/s on average with zero errors, and the JVM remained stable throughout with no old-generation collections. 

The main practical limitation is query complexity. Scripting, score computation, scroll, and uncached aggregation create a clear latency step-up relative to fast-path queries. These workloads should be isolated, cached, or minimized when low latency matters.

## What you've accomplished

You've now deployed Elasticsearch on an Arm-based Azure Cobalt 100 virtual machine, installed ESRally, and run a baseline geonames benchmark. You've interpreted the main throughput and latency indicators to assess initial performance on Arm.

You can now use this baseline to continue tuning or evaluating Arm-based deployments.
