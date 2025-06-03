---
title: How to run the benchmarks
weight: 50

### FIXED, DO NOT MODIFY
layout: learningpathall
---

With setup complete, you can now run and analyze the benchmarks. 

## Overview of the benchmarking process


`sweet` runs the benchmarks, and `benchstat` is used to analyze and compare two or more results against each other.  For example, if you are interested in seeing performance differences between an Arm and an x86 VM, you would run the benchmarks on each VM to get a benchmark for each instance, and then use `benchstat` to analyze and compare the results of the two.

Benchstat output formats include text (default) or CSV.  When using text format, you get a tabular view of the results. Alternatively, CSV provides you with a format you can use with any tool of your choice that supports it.

To get started, you'll run a benchmark by hand to get a feel for how sweet and benchstat work together.

### Choosing a benchmark to run

Sweet comes ready to run with the following benchmarks:  

| Benchmark       | Description                                                                                                                               | Command                                                      |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| **biogo-igor**    | Processes pairwise alignment data using the biogo library, grouping repeat feature families and outputting results in JSON format.         | `sweet run -count 10 -run="biogo-igor" config.toml`           |
| **biogo-krishna** | Pure-Go implementation of the PALS algorithm for pairwise sequence alignment, measuring alignment runtime performance.                    | `sweet run -count 10 -run="biogo-krishna" config.toml`        |
| **bleve-index**   | Indexes a subset of Wikipedia articles into a Bleve full-text search index to assess indexing throughput and resource usage.            | `sweet run -count 10 -run="bleve-index" config.toml`          |
| **cockroachdb**   | Executes CockroachDB KV workloads with varying read percentages (0%, 50%, 95%) and node counts (1 & 3) to evaluate database performance. | `sweet run -count 10 -run="cockroachdb" config.toml`          |
| **esbuild**       | Bundles and minifies JavaScript/TypeScript code using esbuild on a representative codebase to measure build speed and efficiency.        | `sweet run -count 10 -run="esbuild" config.toml`              |
| **etcd**          | Uses the official etcd benchmarking tool to stress-test an etcd cluster, measuring request latency and throughput for key-value operations. | `sweet run -count 10 -run="etcd" config.toml`                 |
| **go-build**      | Compiles a representative Go module (or the Go toolchain) to measure compilation time and memory (RSS) usage on supported platforms.     | `sweet run -count 10 -run="go-build" config.toml`             |
| **gopher-lua**    | Executes Lua scripts using the GopherLua VM to benchmark the performance of a pure-Go Lua interpreter.                                   | `sweet run -count 10 -run="gopher-lua" config.toml`           |
| **gvisor**        | Benchmarks gVisor by measuring raw syscall overhead and HTTP server performance within the sandboxed container.                          | `sweet run -count 10 -run="gvisor" config.toml`               |
| **markdown**      | Parses and renders Markdown documents to HTML using a Go-based markdown library to evaluate parsing and rendering throughput.            | `sweet run -count 10 -run="markdown" config.toml`             |
| **tile38**        | Stress-tests a Tile38 geospatial database with WITHIN, INTERSECTS, and NEARBY queries to measure spatial query performance.              | `sweet run -count 10 -run="tile38" config.toml`               |


When testing, its suggested to run each benchmark at least 10-times (specified via the `count` parameter) to handle outlier/errant runs.
