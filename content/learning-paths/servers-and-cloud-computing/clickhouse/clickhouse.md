---
layout: learningpathall
title: Run ClickHouse and measure performance
weight: 2
---

[ClickHouse](https://clickhouse.com/docs/en/home) is a column-oriented database management system (DBMS) for online analytical processing of queries (OLAP).

You can use ClickBench to measure the processing time (query latency) of ClickHouse on Arm servers.

ClickBench is open-source software used to evaluate the performance of various database management systems for web analytics.

## Before you begin

You will need an Arm server or an [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider running a recent version of Ubuntu for Arm. 

You will also need sufficient storage on the instance for the web-analytics dataset used for measuring ClickHouse performance, 500 GB is recommended.


## Install ClickHouse

Install ClickHouse and start the server. For detailed installation instructions refer to the [installation guide](https://clickhouse.com/docs/en/install).

1. Install ClickHouse:

```bash
curl https://clickhouse.com/ | sh
sudo DEBIAN_FRONTEND=noninteractive ./clickhouse install
```

2. Set the compression method for `clickhouse-server` to use `zstd` by running the commands: 

```bash
echo "
compression:
    case:
        method: zstd
" | sudo tee /etc/clickhouse-server/config.d/compression.yaml
```

3. Start the ClickHouse server:

```bash
sudo clickhouse start
```

## Run ClickBench 

1. Clone the ClickBench repository:

```bash
sudo apt install -y git wget curl
git clone https://github.com/ClickHouse/ClickBench.git
```

2. Navigate to the repository and create a table:

```bash
cd ClickBench/clickhouse
clickhouse-client < create.sql
```

3. Load the benchmark data 

The data file is very large and takes more than 10 minutes to download and uncompress. 

```console
wget --continue 'https://datasets.clickhouse.com/hits_compatible/hits.tsv.gz'
gzip -d hits.tsv.gz
```

4. Import the data using `clickhouse-client`:

Importing the data takes more than 5 minutes. 

```console
clickhouse-client --time --query "INSERT INTO hits FORMAT TSV" < hits.tsv
```

The data is the [Anonymized Web Analytics dataset](https://clickhouse.com/docs/en/getting-started/example-datasets/metrica/).

5. Execute the benchmark 

The script loops through each query three times. A total of 43 queries are run.

```bash
./run.sh
```

### ClickBench results

When you execute the `run.sh` script, the query processing time for each individual query is displayed on the console. 

The three comma separated values represent the query latency time for each of the three times the query is run.

```output
[0.002, 0.001, 0.001],
[0.028, 0.023, 0.022],
[0.066, 0.052, 0.052],
```

The summarized results are also saved to the `results.csv` file in the current directory. The `results.csv` file has 129 lines (43 queries each run 3 times).

You can try different types of hardware and compare results. For example, if you use AWS try c6g.2xlarge and compare to c7g.2xlarge to see the difference between AWS Graviton2 and Graviton3 processors. 


