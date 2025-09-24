---
title: MongoDB Baseline Testing 
weight: 5 

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Baseline testing of MongoDB
In this section you will perform baseline testing by verifying MongoDB is running, logging into the shell, executing a few test queries, and monitoring live performance. This ensures the database is functioning correctly before starting any benchmarks.

## Verify MongoDB installation and service health (Azure Cobalt 100 Arm64)

```console
ps -ef | grep mongod
mongod --version
netstat -tulnp | grep 27017
```
What each command does:
- **ps -ef | grep mongod** checks if the MongoDB server process is running
- **mongod --version** shows the installed MongoDB version
- **netstat -tulnp | grep 27017** confirms MongoDB is listening on the default port 27017

You should see output similar to:

```output
mongod --version
netstat -tulnp | grep 27017
ubuntu      4288       1  0 10:40 ?        00:00:01 mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --fork
ubuntu      4545    1764  0 10:43 pts/0    00:00:00 grep --color=auto mongod
db version v8.0.12
Build Info: {
    "version": "8.0.12",
    "gitVersion": "b60fc6875b5fb4b63cc0dbbd8dda0d6d6277921a",
    "openSSLVersion": "OpenSSL 3.0.13 30 Jan 2024",
    "modules": [],
    "allocator": "tcmalloc-google",
    "environment": {
        "distmod": "ubuntu2404",
        "distarch": "aarch64",
        "target_arch": "aarch64"
    }
}
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp        0      0 127.0.0.1:27017         0.0.0.0:*               LISTEN      4288/mongod
```

## Run storage baseline with fio (random read IOPS on Ubuntu 24.04):

This reads random 4 KB blocks from a 100 MB file for 30 seconds with one job and prints a summary

```console
fio --name=baseline --rw=randread --bs=4k --size=100M --numjobs=1 --time_based --runtime=30 --group_reporting
```
You should see output similar to:

```output
baseline: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=psync, iodepth=1
fio-3.36
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=14.8MiB/s][r=3799 IOPS][eta 00m:00s]
baseline: (groupid=0, jobs=1): err= 0: pid=3753: Mon Sep  1 10:25:07 2025
  read: IOPS=4255, BW=16.6MiB/s (17.4MB/s)(499MiB/30001msec)
    clat (usec): min=88, max=46246, avg=234.23, stdev=209.81
     lat (usec): min=88, max=46246, avg=234.28, stdev=209.81
    clat percentiles (usec):
     |  1.00th=[   99],  5.00th=[  111], 10.00th=[  126], 20.00th=[  167],
     | 30.00th=[  190], 40.00th=[  229], 50.00th=[  243], 60.00th=[  253],
     | 70.00th=[  269], 80.00th=[  289], 90.00th=[  318], 95.00th=[  330],
     | 99.00th=[  416], 99.50th=[  490], 99.90th=[  799], 99.95th=[ 1106],
     | 99.99th=[  3884]
   bw (  KiB/s): min=14536, max=19512, per=100.00%, avg=17046.10, stdev=1359.69, samples=59
   iops        : min= 3634, max= 4878, avg=4261.53, stdev=339.92, samples=59
  lat (usec)   : 100=1.27%, 250=56.61%, 500=41.65%, 750=0.34%, 1000=0.06%
  lat (msec)   : 2=0.04%, 4=0.01%, 10=0.01%, 20=0.01%, 50=0.01%
  cpu          : usr=0.33%, sys=2.93%, ctx=127668, majf=0, minf=8
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=127661,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=16.6MiB/s (17.4MB/s), 16.6MiB/s-16.6MiB/s (17.4MB/s-17.4MB/s), io=499MiB (523MB), run=30001-30001msec

Disk stats (read/write):
  sda: ios=127195/29, sectors=1017560/552, merge=0/15, ticks=29133/8, in_queue=29151, util=96.37%
```
The output shows how fast it read data (**16.6 MB/s**) and how many reads it did per second (**~4255 IOPS**), which tells you how responsive your storage is for random reads.

## Connectivity and CRUD Sanity Check

To verify that the MongoDB server is reachable you will perform a connectivity check. You will run a sanity test of core database functionality and permissions, refered to as CRUD:

C - Create: Insert a new record/document into the database.
R - Read: Query the database to retrieve data.
U - Update: Modify an existing record.
D - Delete: Remove a record.

```console
mongosh --host localhost --port 27017
```

Inside the shell:

```javascript
use baselineDB
db.testCollection.insertOne({ name: "baseline-check", value: 1 })
db.testCollection.find()
db.testCollection.updateOne({ name: "baseline-check" }, { $set: { value: 2 } })
db.testCollection.deleteOne({ name: "baseline-check" })
exit
```
What these commands do:
- Create a test document
- Read it
- Update its value
- Delete it

You should see output similar to:

```output
test> use baselineDB
switched to db baselineDB
baselineDB> db.testCollection.insertOne({ name: "baseline-check", value: 1 })
{
  acknowledged: true,
  insertedId: ObjectId('689acdae6a86b49bca74e39a')
}
baselineDB> db.testCollection.find()
[
  {
    _id: ObjectId('689acdae6a86b49bca74e39a'),
    name: 'baseline-check',
    value: 1
  }
]
baselineDB> db.testCollection.updateOne({ name: "baseline-check" }, { $set: { value: 2 } })
...
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
baselineDB> db.testCollection.deleteOne({ name: "baseline-check" })
...
{ acknowledged: true, deletedCount: 1 }
```

## Basic query performance test (count filter)

Run a lightweight query performance check:

```console
mongosh --eval '
db = db.getSiblingDB("baselineDB");
for (let i=0; i<1000; i++) { db.perf.insertOne({index:i, value:Math.random()}) };
var start = new Date();
db.perf.find({ value: { $gt: 0.5 } }).count();
print("Query Time (ms):", new Date() - start);
'
```
This connects to MongoDB, selects the `baselineDB` database, inserts 1,000 documents into the `perf` collection, and measures the time to count documents where `value > 0.5`

You should see output similar to:

```output
Query Time (ms): 2
```

## Index creation speed test in MongoDB

Measure how long MongoDB takes to create an index on a collection:

```console
mongosh --eval '
db = db.getSiblingDB("baselineDB");
var start = new Date();
db.perf.createIndex({ value: 1 });
print("Index Creation Time (ms):", new Date() - start);
'
```
This creates an index on the `value` field in the `perf` collection and prints the time taken

You should see output similar to:

```output
Index Creation Time (ms): 22
```

## Concurrency smoke test with parallel mongosh sessions

Verify that MongoDB can handle concurrent client connections and inserts

```console
for i in {1..5}; do
  mongosh --eval 'use baselineDB; db.concurrent.insertMany([...Array(1000).keys()].map(k => ({ test: k, ts: new Date() })))' &
done
wait
```
This runs five parallel MongoDB shell sessions, each inserting 1,000 documents into the `baselineDB.concurrent` collection.

You should see output similar to

```output
[1] 3818
[2] 3819
[3] 3820
[4] 3821
[5] 3822
switched to db baselineDB;
[1]   Done                    mongosh --eval 'use baselineDB; db.concurrent.insertMany([...Array(1000).keys()].map(k => ({ test: k, ts: new Date() })))'
switched to db baselineDB;
switched to db baselineDB;
switched to db baselineDB;
[2]   Done                    mongosh --eval 'use baselineDB; db.concurrent.insertMany([...Array(1000).keys()].map(k => ({ test: k, ts: new Date() })))'
[4]-  Done                    mongosh --eval 'use baselineDB; db.concurrent.insertMany([...Array(1000).keys()].map(k => ({ test: k, ts: new Date() })))'
[3]-  Done                    mongosh --eval 'use baselineDB; db.concurrent.insertMany([...Array(1000).keys()].map(k => ({ test: k, ts: new Date() })))'
switched to db baselineDB;
[5]+  Done                    mongosh --eval 'use baselineDB; db.concurrent.insertMany([...Array(1000).keys()].map(k => ({ test: k, ts: new Date() })))'
```

Five parallel MongoDB shell sessions were executed, each inserting 1,000 test documents into the baselineDB.concurrent collection. All sessions completed successfully, confirming that concurrent data insertion works as expected.

With these tests you have confirmed that MongoDB is installed successfully and is functioning as expected on the Azure Cobalt 100 (Arm64) environment.

You are now ready to perform further benchmarking for MongoDB.
