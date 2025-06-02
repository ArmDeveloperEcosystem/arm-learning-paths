---
# User change
title: "Alternative performance testing of MongoDB"
weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
To measure the performance of MongoDB, use the [MongoDB performance test tool](https://github.com/idealo/mongodb-performance-test).

This is an open source Java application that tests the MongoDB performance, such as latency and throughput, by running one or more threads executing either all the same or different database operations, such as Inserts, Updates, Deletes, Counts or Finds until a defined number of operations is executed or a defined maximum runtime is reached.

## Install OpenJDK packages

Install the appropriate run-time environment to be able to use the performance test tool.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" >}}
sudo apt install default-jre default-jdk -y
{{< /tab >}}
{{< tab header="RHEL/Amazon Linux" >}}
sudo yum install java-17-openjdk
{{< /tab >}}
{{< /tabpane >}}

For more information see the [OpenJDK](https://openjdk.org/install/) website.

## Setup the MongoDB performance test tool

On your instance running MongoDB (you may need to start a new terminal), clone the `MongoDB performance test tool` project:

```bash { pre_cmd="sudo apt-get install -y openjdk-8-jre git" }
git clone https://github.com/idealo/mongodb-performance-test.git
```

Now change into the project folder and execute the JAR file to see its usage instructions:

```bash { ret_code="1" }
cd mongodb-performance-test
java -jar ./latest-version/mongodb-performance-test.jar
```
This will print a description of how to use the Java application.


## Run Insert test

Run a test that inserts documents on `localhost:27017` (default).

First, set an environment variable for the JAR file path for convenience:
```bash { cwd="./mongodb-performance-test" }
export jarfile=./latest-version/mongodb-performance-test.jar
```

Use the following options:
  * `-m` defines the test mode (e.g., `insert`, `update_one`).
  * `-o` defines the number of operations (iterations).
    * Alternatively, use `-d` to specify a duration limit (in seconds).
  * `-t` defines the number of threads.
  * `-db` defines the database to use.
  * `-c` defines the collection to use.

  For example, run an insert test for 1 million operations using 10 threads:
```bash { cwd="./mongodb-performance-test" }
java -jar $jarfile -m insert -o 1000000 -t 10 -db test -c perf
```
As the test runs, the progress count will be printed periodically. It will increase until it reaches 1 million, and then the test will end.

## Run Update-one test

Similarly, to run an update test (updating one document per query) using 10, 20, and finally 30 threads for 1 hour each (3 hours total), run the following command:

```console
java -jar $jarfile -m update_one -d 3600 -t 10 20 30 -db test -c perf
```

For instructions on running any other tests or more details on the metrics reported, refer to the [github project for the performance tool](https://github.com/idealo/mongodb-performance-test#readme).

## View the results

During each test, statistics over the last second are printed to the console every second. After the test completes, final summary statistics are displayed. The following is example output from the end of the Insert test run:

``` output
-- Timers ----------------------------------------------------------------------
stats-per-run-INSERT
2022-07-05 19:14:45,894 [main] INFO  d.i.mongodb.perf.MongoDbAccessor - <<< closeConnections localhost:27017
             count = 1000000
         mean rate = 5001.61 calls/second
     1-minute rate = 5042.28 calls/second
     5-minute rate = 3699.92 calls/second
    15-minute rate = 2963.07 calls/second
               min = 0.36 milliseconds
               max = 15.59 milliseconds
              mean = 1.93 milliseconds
            stddev = 0.66 milliseconds
            median = 1.87 milliseconds
              75% <= 1.99 milliseconds
              95% <= 2.22 milliseconds
              98% <= 2.64 milliseconds
              99% <= 3.85 milliseconds
            99.9% <= 15.59 milliseconds
```

Detailed per-second metrics are also output to a CSV file named `stats-per-second-[mode].csv` (e.g., `stats-per-second-INSERT.csv`), located in the same folder as the JAR file. `[mode]` corresponds to the executed mode(s), such as `INSERT`, `UPDATE_ONE`, `DELETE_ONE`, etc.
