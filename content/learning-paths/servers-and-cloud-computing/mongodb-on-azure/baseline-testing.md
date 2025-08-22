---
title: MongoDB Baseline Testing 
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


### Baseline testing of MongoDB
Perform baseline testing by verifying MongoDB is running, logging into the shell, executing a few test queries, and monitoring live performance. This ensures the database is functioning correctly before starting any benchmarks.

1. Verify Installation & Service Health

```console
ps -ef | grep mongod
mongod --version
netstat -tulnp | grep 27017
```
- **ps -ef | grep mongod** – Checks if the MongoDB server process is running.
- **mongod --version** – Shows the version of MongoDB installed.
- **netstat -tulnp | grep 27017** – Checks if MongoDB is listening for connections on its default port 27017.

You should see an output similar to:

```output
azureus+     976     797  0 05:00 pts/0    00:00:00 grep --color=auto mongod
db version v8.0.12
Build Info: {
    "version": "8.0.12",
    "gitVersion": "b60fc6875b5fb4b63cc0dbbd8dda0d6d6277921a",
    "openSSLVersion": "OpenSSL 3.3.3 11 Feb 2025",
    "modules": [],
    "allocator": "tcmalloc-google",
    "environment": {
        "distmod": "rhel93",
        "distarch": "aarch64",
        "target_arch": "aarch64"
    }
}
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp        0      0 127.0.0.1:27017         0.0.0.0:*               LISTEN      1113/./mongodb-linu
```

2. Storage and Health Check

```console
ls -lh ~/mongodb-data/db
```
Make sure MongoDB’s data files exist and test your disk’s read speed. You want steady, consistent performance.

You should see an output similar to:

```output
total 6.5M
-rw-------. 1 azureuser azureuser   50 Aug  8 10:54 WiredTiger
-rw-------. 1 azureuser azureuser   21 Aug  8 10:54 WiredTiger.lock
-rw-------. 1 azureuser azureuser 1.5K Aug 11 13:05 WiredTiger.turtle
-rw-------. 1 azureuser azureuser 100K Aug 11 13:05 WiredTiger.wt
-rw-------. 1 azureuser azureuser 4.0K Aug 11 13:05 WiredTigerHS.wt
-rw-------. 1 azureuser azureuser  36K Aug 11 13:05 _mdb_catalog.wt
-rw-------. 1 azureuser azureuser 3.1M Aug 11 13:05 collection-0-18324942683865842057.wt
-rw-------. 1 azureuser azureuser  20K Aug 11 13:05 collection-0-2816474184925722673.wt
-rw-------. 1 azureuser azureuser  36K Aug 11 13:05 collection-2-2816474184925722673.wt
-rw-------. 1 azureuser azureuser  12K Aug 11 13:05 collection-4-2816474184925722673.wt
-rw-------. 1 azureuser azureuser 1.3M Aug 11 13:05 collection-62-18324942683865842057.wt
-rw-------. 1 azureuser azureuser 4.0K Aug  8 12:41 collection-7-2816474184925722673.wt
-rw-------. 1 azureuser azureuser  12K Aug 11 13:05 collection-82-18324942683865842057.wt
drwx------. 2 azureuser azureuser 4.0K Aug 11 13:05 diagnostic.data
-rw-------. 1 azureuser azureuser 1.4M Aug 11 13:05 index-1-18324942683865842057.wt
-rw-------. 1 azureuser azureuser  20K Aug 11 13:05 index-1-2816474184925722673.wt
-rw-------. 1 azureuser azureuser  36K Aug 11 13:05 index-3-2816474184925722673.wt
-rw-------. 1 azureuser azureuser  12K Aug 11 13:05 index-5-2816474184925722673.wt
-rw-------. 1 azureuser azureuser  36K Aug 11 13:05 index-6-2816474184925722673.wt
-rw-------. 1 azureuser azureuser 504K Aug 11 13:05 index-71-18324942683865842057.wt
-rw-------. 1 azureuser azureuser 4.0K Aug  8 12:41 index-8-2816474184925722673.wt
-rw-------. 1 azureuser azureuser  12K Aug 11 13:05 index-83-18324942683865842057.wt
-rw-------. 1 azureuser azureuser 4.0K Aug  8 12:41 index-9-2816474184925722673.wt
drwx------. 2 azureuser azureuser 4.0K Aug 11 04:10 journal
-rw-------. 1 azureuser azureuser    0 Aug 11 13:05 mongod.lock
-rw-------. 1 azureuser azureuser  36K Aug 11 13:05 sizeStorer.wt
-rw-------. 1 azureuser azureuser  114 Aug  8 10:54 storage.bson
```

Run the command below to check how fast your storage can **randomly read small 4KB chunks** from a 100 MB file for 30 seconds, using one job, and then show a summary report:

```console
fio --name=baseline --rw=randread --bs=4k --size=100M --numjobs=1 --time_based --runtime=30 --group_reporting
```
You should see an output similar to:

```output
baseline: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=psync, iodepth=1
fio-3.37
Starting 1 process
baseline: Laying out IO file (1 file / 100MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=19.8MiB/s][r=5058 IOPS][eta 00m:00s]
baseline: (groupid=0, jobs=1): err= 0: pid=1065: Tue Aug 12 05:04:48 2025
  read: IOPS=5201, BW=20.3MiB/s (21.3MB/s)(610MiB/30001msec)
    clat (usec): min=83, max=21382, avg=191.64, stdev=106.48
     lat (usec): min=83, max=21382, avg=191.68, stdev=106.48
    clat percentiles (usec):
     |  1.00th=[   91],  5.00th=[   95], 10.00th=[  100], 20.00th=[  139],
     | 30.00th=[  155], 40.00th=[  169], 50.00th=[  225], 60.00th=[  229],
     | 70.00th=[  233], 80.00th=[  235], 90.00th=[  247], 95.00th=[  269],
     | 99.00th=[  314], 99.50th=[  330], 99.90th=[  412], 99.95th=[  465],
     | 99.99th=[  635]
   bw (  KiB/s): min=17888, max=22896, per=100.00%, avg=20815.73, stdev=1085.63, samples=59
   iops        : min= 4472, max= 5724, avg=5203.93, stdev=271.41, samples=59
  lat (usec)   : 100=10.12%, 250=81.30%, 500=8.55%, 750=0.02%, 1000=0.01%
  lat (msec)   : 2=0.01%, 10=0.01%, 20=0.01%, 50=0.01%
  cpu          : usr=0.27%, sys=3.38%, ctx=156062, majf=0, minf=7
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=156056,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1
Run status group 0 (all jobs):
   READ: bw=20.3MiB/s (21.3MB/s), 20.3MiB/s-20.3MiB/s (21.3MB/s-21.3MB/s), io=610MiB (639MB), run=30001-30001msec
Disk stats (read/write):
  sda: ios=155988/70, sectors=1247904/1016, merge=0/31, ticks=29060/28, in_queue=29096, util=95.44%
```
The output shows how fast it read data (**20.3 MB/s**) and how many reads it did per second (**~5200 IOPS**), which tells you how responsive your storage is for random reads.

3. Connectivity and CRUD Sanity Check

```console
mongosh --host localhost --port 27017
```

Inside shell:

```javascript
use baselineDB
db.testCollection.insertOne({ name: "baseline-check", value: 1 })
db.testCollection.find()
db.testCollection.updateOne({ name: "baseline-check" }, { $set: { value: 2 } })
db.testCollection.deleteOne({ name: "baseline-check" })
exit
```
These commands create a test record, read it, update its value, and then delete it a simple way to check if MongoDB’s basic **add, read, update, and delete** operations are working.

You should see an output similar to:

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

4. Basic Query Performance Test

```console
mongosh --eval '
db = db.getSiblingDB("baselineDB");
for (let i=0; i<1000; i++) { db.perf.insertOne({index:i, value:Math.random()}) };
var start = new Date();
db.perf.find({ value: { $gt: 0.5 } }).count();
print("Query Time (ms):", new Date() - start);
'
```
The command connected to MongoDB, switched to the **baselineDB** database, inserted **1,000 documents** into the perf collection, and then measured the execution time for counting documents where **value > 0.5**. The final output displayed the **query execution time** in milliseconds.

You should see an output similar to:

```output
Query Time (ms): 2
```

5. Index Creation Speed Test

```console
mongosh --eval '
db = db.getSiblingDB("baselineDB");
var start = new Date();
db.perf.createIndex({ value: 1 });
print("Index Creation Time (ms):", new Date() - start);
'
```
The test connected to MongoDB, switched to the **baselineDB** database, and created an index on the **value** field in the **perf** collection. The index creation process completed in **38 milliseconds**, indicating relatively fast index building for the dataset size.

You should see an output similar to:

```output
Index Creation Time (ms): 38
```

6. Concurrency Smoke Test

```console
for i in {1..5}; do
  /usr/bin/mongosh --eval 'use baselineDB; db.concurrent.insertMany([...Array(1000).keys()].map(k => ({ test: k, ts: new Date() })))' &
done
wait
```
This command runs **five MongoDB insert jobs at the same time**, each adding **1,000 new records** to the **baselineDB.concurrent** collection.
It’s a quick way to test how MongoDB handles **multiple users writing data at once**.

You should see an output similar to:

```output
[1] 1281
[2] 1282
[3] 1283
[4] 1284
[5] 1285
switched to db baselineDB;
switched to db baselineDB;
[1]   Done                    /usr/bin/mongosh --eval 'use baselineDB; db.concurrent.insertMany([...Array(1000).keys()].map(k => ({ test: k, ts: new Date() })))'
switched to db baselineDB;
[2]   Done                    /usr/bin/mongosh --eval 'use baselineDB; db.concurrent.insertMany([...Array(1000).keys()].map(k => ({ test: k, ts: new Date() })))'
[3]   Done                    /usr/bin/mongosh --eval 'use baselineDB; db.concurrent.insertMany([...Array(1000).keys()].map(k => ({ test: k, ts: new Date() })))'
switched to db baselineDB;
switched to db baselineDB;
[4]-  Done                    /usr/bin/mongosh --eval 'use baselineDB; db.concurrent.insertMany([...Array(1000).keys()].map(k => ({ test: k, ts: new Date() })))'
[5]+  Done                    /usr/bin/mongosh --eval 'use baselineDB; db.concurrent.insertMany([...Array(1000).keys()].map(k => ({ test: k, ts: new Date() })))'
```

**Five parallel MongoDB shell sessions** were executed, each inserting **1,000** test documents into the baselineDB.concurrent collection. All sessions completed successfully, confirming that concurrent data insertion works as expected.

The above operations confirm that MongoDB is installed successfully and is functioning as expected on the Azure Cobalt 100 (Arm64) environment.

Now, your MongoDB instance is ready for further benchmarking and production use.
