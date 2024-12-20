---
# User change
title: "Benchmark MongoDB 7.0 on Arm with Yahoo Cloud Serving Benchmark (YCSB)"

draft: true 

weight: 20 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
To further measure the performance of MongoDB, you will run the [Yahoo Cloud Serving Benchmark](http://github.com/brianfrankcooper/YCSB).

YCSB is an open sourced project which provides the framework and common set of workloads to evaluate the performance of different "key-value" and "cloud" serving stores. Here are the steps to run YCSB to evaluate the performance of MongoDB running on 64-bit Arm machine.

## Additional software packages

To run YCSB, additional software packages are required, [Apache Maven](https://maven.apache.org/), and [Python](https://www.python.org) 2.7.

Installing Apache Maven:

```bash
   cd ~
   wget https://archive.apache.org/dist/maven/maven-3/3.1.1/binaries/apache-maven-3.1.1-bin.tar.gz
   sudo tar xzf apache-maven-*-bin.tar.gz -C /usr/local
   cd /usr/local
   sudo ln -s apache-maven-* maven
   cd ~/
   export M2_HOME=/usr/local/maven
   export PATH="$M2_HOME/bin:$PATH"
```

Installing Python 2.7:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" >}}
sudo apt-get update
sudo apt install python -y
{{< /tab >}}
{{< tab header="RHE/Amazon" >}}
sudo yum check-update
sudo yum install python2
{{< /tab >}}
{{< /tabpane >}}
{{% notice  Python Note%}}

For Ubuntu 22.04 the `python` package may not be found. You can install Python 2.7 using:
```console
sudo apt install python2 -y
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 1
```

For Red Hat you can configure `python2` to be the default `python` using:
```console
sudo alternatives --set python /usr/bin/python2
```
{{% /notice %}}

## Setup YCSB

Download the latest released YCSB zip file and uncompress it.

```bash { pre_cmd="sudo apt install -y python" }
mkdir ycsb && cd ycsb
curl -O --location https://github.com/brianfrankcooper/YCSB/releases/download/0.17.0/ycsb-0.17.0.tar.gz
tar xfvz ycsb-0.17.0.tar.gz
```
Now `cd` into project folder and run the executable to print a description of how to use the benchmark.

```bash { env="M2_HOME=/usr/local/maven,PATH=/usr/local/maven/bin:$PATH",cwd="./ycsb",ret_code="2" }
cd ycsb-0.17.0
./bin/ycsb
```
## Load/Insert Test on MongoDB

To load and test the performance of loading data(INSERT) into default database `ycsb` at `localhost:27017` where MongoDB is running using the synchronous driver run the following command:

```console
./bin/ycsb load mongodb -s -P workloads/workloada -p mongodb.url=mongodb://localhost:27017/ycsb?w=0 -threads 10
```
The "-P" parameter is used to load property files. In this example, you used it load the workloada parameter file which sets the recordcount to 1000 in addition to other parameters. The "-threads" parameter indicates the number of threads and is set to 1 by default.

## Update/Read/Read Modify Write Test on MongoDB

To test the performance of executing a workload which includes running UPDATE, Read Modify Write(RMW) and/or READ operations on the data using 10 threads for example, use the following command:

```console
./bin/ycsb load mongodb -s -P workloads/workloada -p mongodb.url=mongodb://localhost:27017/ycsb?w=0
```

The workloads/workloada file in this example sets the following values `readproportion=0.5` and  `updateproportion=0.5` which means there is an even split between the number of READ and UPDATE operations performed. You can change the type of operations and the splits by providing your own workload parameter file.

For more detailed information on all the parameters for running a workload refer to [this section](https://github.com/brianfrankcooper/YCSB/wiki/Running-a-Workload).

## View the results

At the end of each test, statistics are printed to the console. Shown below is the output from the end of Load/Insert test

```output
2022-07-06 15:50:18:917 1 sec: 1000 operations; 542.01 current ops/sec; [CLEANUP: Count=10, Max=12951, Min=0, Avg=1295.2, 90=4, 99=12951, 99.9=12951, 99.99=12951] [INSERT: Count=1000, Max=134655, Min=561, Avg=8506.37, 90=10287, 99=39903, 99.9=134015, 99.99=134655]
[OVERALL], RunTime(ms), 1849
[OVERALL], Throughput(ops/sec), 540.8328826392644
[TOTAL_GCS_Copy], Count, 5
[TOTAL_GC_TIME_Copy], Time(ms), 23
[TOTAL_GC_TIME_%_Copy], Time(%), 1.2439156300703083
[TOTAL_GCS_MarkSweepCompact], Count, 0
[TOTAL_GC_TIME_MarkSweepCompact], Time(ms), 0
[TOTAL_GC_TIME_%_MarkSweepCompact], Time(%), 0.0
[TOTAL_GCs], Count, 5
[TOTAL_GC_TIME], Time(ms), 23
[TOTAL_GC_TIME_%], Time(%), 1.2439156300703083
[CLEANUP], Operations, 10
[CLEANUP], AverageLatency(us), 1295.2
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 12951
[CLEANUP], 95thPercentileLatency(us), 12951
[CLEANUP], 99thPercentileLatency(us), 12951
[INSERT], Operations, 1000
[INSERT], AverageLatency(us), 8506.367
[INSERT], MinLatency(us), 561
[INSERT], MaxLatency(us), 134655
[INSERT], 95thPercentileLatency(us), 11871
[INSERT], 99thPercentileLatency(us), 39903
[INSERT], Return=OK, 1000
...
```
## Other tests

For instructions on running any other tests or more details on the metrics reported, refer to the [GitHub project for the YCSB](https://github.com/brianfrankcooper/YCSB/wiki/).

