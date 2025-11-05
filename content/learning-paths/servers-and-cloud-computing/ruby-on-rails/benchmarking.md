---
title: Ruby on Rails Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Ruby on Rails Benchmarking 
In this section you will benchmark Ruby on Rails using Ruby’s built-in `Benchmark` library to measure execution time for database inserts, queries, and CPU computations on GCP SUSE VMs, providing insights into performance metrics and bottlenecks.

### Go into your Rails app folder
Navigate into the folder of your Rails application. This is where Rails expects your application code, models, and database configurations to be located. All commands related to your app should be run from this folder.

```console
cd ~/db_test_rubyapp
````

### Create the benchmark
Now create a new Ruby file named `benchmark.rb` where you will write code to measure performance.

```console
vi benchmark.rb
```

### Benchmark code for measuring Rails app performance
Below mentioned code (`benchmark.rb` file) measures database inserts, queries, and CPU computations in your Rails application using Ruby’s Benchmark library.

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
- `require 'benchmark'` → Loads Ruby’s built-in benchmarking library.
- `n = 1000` → Sets the number of iterations for each task. You can increase or decrease this number to simulate heavier or lighter workloads.
- `Benchmark.bm` → Starts a block to measure performance of different tasks.
- **DB Insert** → Creates 1,000 new `Task` records in the database. Measures how long it takes to insert data.
- **DB Query** → Retrieves the 1,000 `Task` records from the database. Measures how long it takes to query data.
- **Computation** → Performs a simple calculation 1,000 times. Measures pure CPU performance (without database interactions).

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

### Benchmark Metrics Explained

- **user** → Time spent executing your Ruby code (**CPU time in user mode**).  
- **system** → Time spent in **system calls** (I/O, database, kernel interactions).  
- **total** → `user + system` (sum of CPU processing time).  
- **real** → The **wall-clock time** (actual elapsed time, includes waiting for DB, I/O, etc).  

### Benchmark summary on Arm64
Results summarized from the your run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):


| Task         | user (sec) | system (sec) | total (sec) | real (sec) |
|--------------|----------|----------|----------|----------|
| DB Insert    | 2.271645 | 0.050236 | 2.321881 | 2.721631 |
| DB Query     | 3.379849 | 0.009345 | 3.389194 | 3.389613 |
| Computation  | 0.410907 | 0.000000 | 0.410907 | 0.410919 |


### Analysis of Results

When you look the benchmarking results, you will notice that on the Google Axion C4A Arm-based instances:

- **Database operations are the main bottleneck:** DB Insert and DB Query take the most time.  
- **DB Query has the highest latency:** It is the slowest operation at 3.39 seconds.  
- **Core computation is fast:** Pure Ruby/Rails calculations complete quickly at 0.41 seconds.
