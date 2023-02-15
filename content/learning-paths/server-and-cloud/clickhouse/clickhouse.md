---
layout: learningpathall
title: Run Clickhouse and measure its performance
weight: 2
---

[Clickhouse](https://clickhouse.com/docs/en/home) is a column-oriented database management system (DBMS) for online analytical processing of queries (OLAP).
We will measure the processing time (query latency) of Clickhouse on Arm based servers.

## Prerequisites

You will need a local Arm platform or an [Arm based instance](/learning-paths/server-and-cloud/csp/) from your cloud service providers, running an appropriate operating system (at time of writing, `Ubuntu 16.04 LTS` or later). You will also need sufficient storage on the instance for the web-analytics dataset used for measuring Clickhouser performance. We used 50GB in our instances.

You can either install both the clickhouse server and client standalone on your Arm instances, or skip this step as it is installed as part of the benchmark script we will run next.

## Standalone Installation of clickouse-server and clickhouse-client
You can install clickhouse-server and clickhouse-client on your Arm server instance, using the package manager on your Linux Distribution. The installation instructions are outlined [here](https://clickhouse.com/docs/en/install)

## Run benchmark 

To measure the query latency time of Clickhouse, we run ClickBench. ClickBench is open-sourced and can be used to evaluate the performance of various Database management systems to use for a web analytics system. 

Start by cloning the ClickBench repository

```bash
sudo apt install -y git wget curl
git clone https://github.com/ClickHouse/ClickBench.git
```
Then navigate into the `clickhouse` directory and run the steps outlined in `benchmark.sh`. We will break each of these commands out

First, install clickhouse if you haven't already done so through the standalone instructions

```bash
curl https://clickhouse.com/ | sh
sudo DEBIAN_FRONTEND=noninteractive ./clickhouse install
```
Then, set the compression method for clickhouse-server to use `zstd` and then start the server

```bash
echo "
compression:
    case:
        method: zstd
" | sudo tee /etc/clickhouse-server/config.d/compression.yaml

sudo clickhouse start
```
Now, create a table:

```bash
cd ClickBench/clickhouse
clickhouse-client < create.sql
```

Let's load the data. It uses the [Anonymized Web Analytics dataset](https://clickhouse.com/docs/en/getting-started/example-datasets/metrica/).

```console
wget --continue 'https://datasets.clickhouse.com/hits_compatible/hits.tsv.gz'
gzip -d hits.tsv.gz

clickhouse-client --time --query "INSERT INTO hits FORMAT TSV" < hits.tsv
```

Finally, execute the run script. This script loops through each query three times. A total of 43 queries are run.

```bash
cd ClickBench/clickhouse
./run.sh
```

## View Results

On the execution of the `run.sh` script. the query processing time for each individual query is displayed on the console. It looks like the output shown below. The three comma separated values represent the query latency time for each of the three times the query is run.

```console
[0.002, 0.001, 0.001],
[0.028, 0.023, 0.022],
[0.066, 0.052, 0.052],
```

The summarized results are also output to the `results.csv` file in your working directory. 