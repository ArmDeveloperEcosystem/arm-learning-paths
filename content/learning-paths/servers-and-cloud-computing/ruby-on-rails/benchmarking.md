---
title: Ruby on Rails Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Overview
In this section you will benchmark Ruby on Rails using Ruby’s built-in `Benchmark` library to measure execution time for database inserts, queries, and CPU computations on GCP SUSE VMs, providing insights into performance metrics and bottlenecks.

## Locate the Rails app folder
Navigate into the folder of your Rails application. This is where Rails expects your application code, models, and database configurations to be located. All commands related to your app should be run from this folder.

```console
cd ~/db_test_rubyapp
````

## Create the benchmark file

Create a new Ruby file called `benchmark.rb` to measure your Rails application's performance:

```console
vi benchmark.rb
```

This file will contain the benchmarking code that tests different aspects of your application's performance.
Copy the following code into `benchmark.rb`. This code measures three different aspects of your Rails application's performance:


```ruby
require 'benchmark'

n = 1000

Benchmark.bm do |x|
  x.report("DB Insert:") do
    n.times do
      Task.create(title: "Benchmark Task", due_date: Date.today)
    end
  end

  x.report("DB Query:") do
    n.times do
      Task.where(title: "Benchmark Task").to_a
    end
  end

  x.report("Computation:") do
    n.times do
      (1..10_000).reduce(:+)
    end
  end
end
```
This benchmarking script tests three key areas of your Rails application's performance:

- The `require 'benchmark'` statement loads Ruby's built-in benchmarking library, which provides precise timing measurements for code execution. 
- The variable `n = 1000` sets how many times each test runs - you can adjust this number to simulate lighter or heavier workloads depending on your testing needs.
- The `Benchmark.bm` method creates a benchmarking block that measures and reports the performance of different tasks. Within this block, three different tests run to evaluate your application:

  - The DB Insert test creates 1,000 new `Task` records in your PostgreSQL database. This measures how efficiently your application can write data, which is crucial for understanding performance during high-volume data entry operations.

  - The DB Query test retrieves those same `Task` records from the database. This measurement shows how quickly your application can read data, helping you understand performance during data-heavy read operations like report generation or search functionality.

  - The Computation test performs a mathematical calculation (summing numbers 1 through 10,000) repeatedly without any database interaction. This gives you a baseline for pure CPU performance, showing how your application handles processing-intensive tasks that don't involve external resources.

This code gives you a basic understanding of how your Rails app performs under different types of workloads.

### Run the benchmark inside Rails
Now that your benchmark file is ready, run it within the Rails environment using the following command:

```console
rails runner benchmark.rb
```
`rails runner` runs any Ruby script in the context of your Rails application.  

It automatically loads your Rails environment, including:
  - All models (like `Task`)
  - Database connections
  - Configuration and dependencies  

This ensures that your benchmark can interact with the PostgreSQL database through ActiveRecord, rather than running as a plain Ruby script.

You should see output similar to:

```output
                  user     system      total        real
DB Insert:    2.271645   0.050236   2.321881 (  2.721631)
DB Query:     3.379849   0.009345   3.389194 (  3.389613)
Computation:  0.410907   0.000000   0.410907 (  0.410919)
```
## Interpet your benchmark results

The output shows four different timing measurements that help you understand where your application spends its time.

- The user time measures how long your Ruby code actually ran on the CPU. This represents the pure processing time for your application logic, calculations, and Ruby operations.

- The system time tracks how long your application spent waiting for system-level operations like database queries, file I/O, and network requests. Higher system time usually indicates bottlenecks in external resources.

- The total time simply adds user and system time together, giving you the complete CPU processing time your application consumed.

- The real time shows the actual wall-clock time that passed from start to finish. This includes everything: CPU processing, waiting for the database to respond, network delays, and any other factors that made your application pause. Real time is often higher than total time because your application might wait for resources that are busy with other tasks.

When real time significantly exceeds total time, it typically indicates that your application is spending considerable time waiting for external resources rather than actively processing data.

## Benchmark summary on Arm64

Here are the performance results from running the benchmark on a `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP with SUSE:

| Task | User Time | System Time | Total Time | Real Time |
|------|-----------|-------------|------------|-----------|
| DB Insert | 2.27 sec | 0.05 sec | 2.32 sec | 2.72 sec |
| DB Query | 3.38 sec | 0.01 sec | 3.39 sec | 3.39 sec |
| Computation | 0.41 sec | 0.00 sec | 0.41 sec | 0.41 sec |

### What these results tell you

- Database operations (insert and query) take significantly longer than pure computation, with queries being the slowest operation.
- System time is minimal across all tasks, indicating efficient system resource usage on Arm64.
- Real time closely matches total time for most operations, showing minimal waiting for external resources.
- Computation tasks run very efficiently, demonstrating strong CPU performance on Axion processors.

## Key takeaways

When you analyze the benchmarking results, you'll notice several important patterns on Google Cloud Axion C4A Arm-based instances:

- Consistent performance - Ruby and PostgreSQL are both natively optimized for Arm, which provides stable and predictable latency across different workloads.
- Database optimization opportunities - the results show that database I/O remains the primary bottleneck. You can improve database-heavy performance using techniques such as:
- Query caching
- Connection pooling  
- Asynchronous queries
- Strong compute performance - Axion's Arm cores combined with Ruby's YJIT compiler demonstrate excellent CPU utilization for compute-intensive tasks that don't rely heavily on I/O operations.

Ruby on Rails runs efficiently on Google Cloud's Axion-based C4A Arm64 instances, making them a solid choice for Rails applications.

## What you've accomplished

You’ve benchmarked your Ruby on Rails application on a Google Cloud C4A Arm-based VM using Ruby’s built-in Benchmark library. You measured database insert and query speeds, as well as CPU computation performance, and interpreted the results to identify optimization opportunities. With these insights, you’re equipped to further tune your Rails workloads for Arm and confidently deploy performance-sensitive applications on Arm-based cloud infrastructure.