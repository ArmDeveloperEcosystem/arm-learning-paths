---
# User change
title: "Benchmark MongoDB with YCSB"
weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

YCSB (Yahoo! Cloud Serving Benchmark) is a widely adopted open-source benchmarking tool designed to evaluate the performance of cloud-based or distributed data-serving systems. It was developed by Yahoo! and is now maintained by the open-source community.

The primary goal of YCSB is to simulate different types of workloads commonly encountered in real-world cloud applications, such as read-heavy or write-heavy workloads. It provides a standardized framework for testing and comparing the performance of various data-serving systems, including databases, key-value stores, and distributed storage systems.

YCSB supports a variety of popular data-serving systems, including Apache Cassandra, MongoDB, Redis, HBase, Amazon DynamoDB, and more. It provides a set of workload scenarios that can be customized to simulate specific application patterns and data access patterns.

Using YCSB, you can measure key performance metrics like throughput, latency, and scalability of the target data-serving system under different workloads. This helps in evaluating the system's suitability for specific use cases, comparing different systems, and identifying performance bottlenecks or areas for optimization.

YCSB is a command-line tool that provides a simple and extensible framework for benchmarking. It allows users to define their own workloads, extend it for new systems, and customize parameters such as the data distribution, request rate, and operation mix.

Overall, YCSB has become a standard benchmarking tool in the cloud and distributed systems community, facilitating performance evaluations and enabling fair comparisons between various data-serving solutions.

You are now ready to benchmark MongoDB with YCSB on your Arm server!

## YCSB Setup
Setup the YCSB on a benchmark machine with __JAVA__:
```console
cd ~
wget -c https://github.com/brianfrankcooper/YCSB/releases/download/0.17.0/ycsb-0.17.0.tar.gz
tar xfvz ycsb-0.17.0.tar.gz
```

Create a workload file with the following content:  
```
vi ~/ycsb-0.17.0/workloads/iworkload

recordcount=1000  
operationcount=1000  
workload=site.ycsb.workloads.CoreWorkload  
readallfields=true  
readproportion=0.2  
updateproportion=0.3  
scanproportion=0.3  
insertproportion=0  
readmodifywriteproportion=0.2  
requestdistribution=zipfian  

```

## YCSB Run
 1. To run YCSB, you need following the `load` command first: 
    ```console
    ~/ycsb-0.17.0/bin/ycsb.sh load mongodb -s -P ~/ycsb-0.17.0/workloads/iworkload -p recordcount=10000000 -threads 256 -p mongodb.url="mongodb://${mongo_ip}:${mongo_port}/mymongodb"
    ```
    You can see the result after the `load` command finishes:
    ```out
    /usr/bin/java  -classpath /root/workload/tools/ycsb-0.17.0/conf:/root/workload/tools/ycsb-0.17.0/lib/core-0.17.0.jar:/root/workload/tools/ycsb-0.17.0/lib/HdrHistogram-2.1.4.jar:/root/workload/tools/ycsb-0.17.0/lib/htrace-core4-4.1.0-incubating.jar:/root/workload/tools/ycsb-0.17.0/lib/jackson-core-asl-1.9.4.jar:/root/workload/tools/ycsb-0.17.0/lib/jackson-mapper-asl-1.9.4.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/logback-classic-1.1.2.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/logback-core-1.1.2.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/mongodb-async-driver-2.0.1.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/mongodb-binding-0.17.0.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/mongo-java-driver-3.8.0.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/slf4j-api-1.7.25.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/snappy-java-1.1.7.1.jar site.ycsb.Client -load -db site.ycsb.db.MongoDbClient -s -P /root/workload/tools/ycsb-0.17.0/workloads/iworkloadf -p recordcount=10000000 -threads 256 -p mongodb.url=mongodb://172.26.202.189:27017/mymongodb
    mongo client connection created with mongodb://172.26.202.189:27017/mymongodb
    [OVERALL], RunTime(ms), 241978
    [OVERALL], Throughput(ops/sec), 41326.07096512906
    [TOTAL_GCS_G1_Young_Generation], Count, 334
    [TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 723
    [TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.2987874930778831
    [TOTAL_GCS_G1_Old_Generation], Count, 0
    [TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
    [TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
    [TOTAL_GCs], Count, 334
    [TOTAL_GC_TIME], Time(ms), 723
    [TOTAL_GC_TIME_%], Time(%), 0.2987874930778831
    [CLEANUP], Operations, 256
    [CLEANUP], AverageLatency(us), 14.421875
    [CLEANUP], MinLatency(us), 0
    [CLEANUP], MaxLatency(us), 3581
    [CLEANUP], 95thPercentileLatency(us), 2
    [CLEANUP], 99thPercentileLatency(us), 2
    [INSERT], Operations, 10000000
    [INSERT], AverageLatency(us), 6153.2624904
    [INSERT], MinLatency(us), 183
    [INSERT], MaxLatency(us), 969215
    [INSERT], 95thPercentileLatency(us), 7563
    [INSERT], 99thPercentileLatency(us), 14991
    [INSERT], Return=OK, 10000000
    ```

 2. Then you can benchmark the performance of MongoDB following the `run` command:
    ```
    ~/ycsb-0.17.0/bin/ycsb.sh run mongodb -s -P ~/ycsb-0.17.0/workloads/iworkload -p operationcount=5000000 -threads 256 -p mongodb.url="mongodb://${mongo_ip}:${mongo_port}/mymongodb"
    ```

    You can see the performance data after the `run` command execution is finished.
    ```output
    /usr/bin/java  -classpath /root/workload/tools/ycsb-0.17.0/conf:/root/workload/tools/ycsb-0.17.0/lib/core-0.17.0.jar:/root/workload/tools/ycsb-0.17.0/lib/HdrHistogram-2.1.4.jar:/root/workload/tools/ycsb-0.17.0/lib/htrace-core4-4.1.0-incubating.jar:/root/workload/tools/ycsb-0.17.0/lib/jackson-core-asl-1.9.4.jar:/root/workload/tools/ycsb-0.17.0/lib/jackson-mapper-asl-1.9.4.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/logback-classic-1.1.2.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/logback-core-1.1.2.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/mongodb-async-driver-2.0.1.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/mongodb-binding-0.17.0.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/mongo-java-driver-3.8.0.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/slf4j-api-1.7.25.jar:/root/workload/tools/ycsb-0.17.0/mongodb-binding/lib/snappy-java-1.1.7.1.jar site.ycsb.Client -t -db site.ycsb.db.MongoDbClient -s -P /root/workload/tools/ycsb-0.17.0/workloads/iworkloadf -p operationcount=5000000 -threads 256 -p mongodb.url=mongodb://172.26.202.189:27017/mymongodb
    mongo client connection created with mongodb://172.26.202.189:27017/mymongodb
    [OVERALL], RunTime(ms), 774685
    [OVERALL], Throughput(ops/sec), 6454.236237954781
    [TOTAL_GCS_G1_Young_Generation], Count, 2889
    [TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 27004
    [TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 3.4858039073946183
    [TOTAL_GCS_G1_Old_Generation], Count, 0
    [TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
    [TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
    [TOTAL_GCs], Count, 2889
    [TOTAL_GC_TIME], Time(ms), 27004
    [TOTAL_GC_TIME_%], Time(%), 3.4858039073946183
    [READ], Operations, 2000633
    [READ], AverageLatency(us), 23745.636704982873
    [READ], MinLatency(us), 257
    [READ], MaxLatency(us), 242047
    [READ], 95thPercentileLatency(us), 43423
    [READ], 99thPercentileLatency(us), 63551
    [READ], Return=OK, 2000633
    [READ-MODIFY-WRITE], Operations, 1000524
    [READ-MODIFY-WRITE], AverageLatency(us), 47604.22748279901
    [READ-MODIFY-WRITE], MinLatency(us), 496
    [READ-MODIFY-WRITE], MaxLatency(us), 389631
    [READ-MODIFY-WRITE], 95thPercentileLatency(us), 75647
    [READ-MODIFY-WRITE], 99thPercentileLatency(us), 97343
    [CLEANUP], Operations, 256
    [CLEANUP], AverageLatency(us), 17.16015625
    [CLEANUP], MinLatency(us), 0
    [CLEANUP], MaxLatency(us), 4035
    [CLEANUP], 95thPercentileLatency(us), 2
    [CLEANUP], 99thPercentileLatency(us), 3
    [UPDATE], Operations, 2500512
    [UPDATE], AverageLatency(us), 23774.697541143574
    [UPDATE], MinLatency(us), 219
    [UPDATE], MaxLatency(us), 254847
    [UPDATE], 95thPercentileLatency(us), 43551
    [UPDATE], 99thPercentileLatency(us), 63775
    [UPDATE], Return=OK, 2500512
    [SCAN], Operations, 1499379
    [SCAN], AverageLatency(us), 60546.94498655777
    [SCAN], MinLatency(us), 455
    [SCAN], MaxLatency(us), 547327
    [SCAN], 95thPercentileLatency(us), 101183
    [SCAN], 99thPercentileLatency(us), 125375
    [SCAN], Return=OK, 1499379

    ```

