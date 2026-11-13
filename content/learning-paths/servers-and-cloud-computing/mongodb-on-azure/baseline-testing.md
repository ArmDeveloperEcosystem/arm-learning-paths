---
title: MongoDB baseline testing
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Validate MongoDB on Cobalt 200

Check your MongoDB setup on a **Standard_D4ps_v7** Cobalt 200 VM running **Ubuntu 24.04 LTS (Arm64)**. You will check server health, run a small storage test with `fio`, and validate CRUD, queries, indexes, and concurrent inserts with `mongosh`.

{{% notice Note %}}
This local test deployment has authorization disabled. Keep `mongod` bound to `127.0.0.1`. Use only the tutorial collections for these tests.
{{% /notice %}}

## Verify server health

From your VM terminal, check the process, listening address, and connectivity:

```console
pgrep -a mongod
ss -ltn | grep 27017
mongosh --quiet --host 127.0.0.1 --port 27017 --eval 'printjson(db.adminCommand({ping: 1}))'
```

Confirm that the listener is `127.0.0.1:27017` and the ping returns:

```output
{ ok: 1 }
```

Review the log if the ping fails:

```console
tail -n 20 /var/log/mongodb/mongod.log
```

## Run a storage baseline with fio

Create a dedicated test directory, then read random 4 KiB blocks from a 100 MiB file for 30 seconds. `--direct=1` bypasses the operating system page cache for this test. The file is created in your home directory; this does not test MongoDB operations or database capacity.

```console
mkdir -p ~/mongodb-storage-baseline
cd ~/mongodb-storage-baseline
fio --name=baseline --filename=baseline.dat --rw=randread --bs=4k --size=100M --numjobs=1 --direct=1 --time_based --runtime=30 --group_reporting
```

The output is similar to:

```output
baseline: (groupid=0, jobs=1): err= 0: pid=32755: Tue Nov 10 18:57:42 2026
  read: IOPS=7458, BW=29.1MiB/s (30.5MB/s)(874MiB/30001msec)
    clat (usec): min=63, max=14576, avg=133.80, stdev=76.43
     lat (usec): min=63, max=14576, avg=133.84, stdev=76.44
```

Check `err=0` for a successful run. Read bandwidth and IOPS depend on the VM disk, cache settings, queue depth, and other activity. This small test does not isolate CPU performance.

## Validate CRUD operations

Connect to MongoDB:

```console
mongosh mongodb://127.0.0.1:27017
```

Inside the shell, insert, retrieve, update, and delete a test document. The assertions report unexpected results:

```javascript
use baselineDB
const inserted = db.testCollection.insertOne({ name: "baseline-check", value: 1 });
assert(inserted.acknowledged);
assert(db.testCollection.findOne({ _id: inserted.insertedId }).value === 1);
assert(db.testCollection.updateOne({ _id: inserted.insertedId }, { $set: { value: 2 } }).modifiedCount === 1);
assert(db.testCollection.deleteOne({ _id: inserted.insertedId }).deletedCount === 1);
print("CRUD checks passed");
exit()
```

The output includes:

```output
CRUD checks passed
```

## Check query performance

From your VM terminal, insert 1,000 documents into a tutorial collection and time a filtered count. Re-running this command adds another 1,000 documents:

```console
mongosh --quiet --eval '
db = db.getSiblingDB("baselineDB");
for (let i = 0; i < 1000; i++) { db.perf.insertOne({ index: i, value: Math.random() }); }
const start = Date.now();
const matched = db.perf.countDocuments({ value: { $gt: 0.5 } });
print("Matched documents:", matched);
print("Query Time (ms):", Date.now() - start);
'
```

The output is similar to:

```output
Matched documents: 505
Query Time (ms): 2
```

Counts vary because values are random and each run adds 1,000 documents to the existing collection. If you repeat the test after the indexing step, the `value` index is also present. The sample above is from the first run against an empty `perf` collection. Run the complete `mongosh --eval` command from your VM terminal; entering the statements individually at the `baselineDB>` prompt includes the time between commands in the elapsed measurement. Treat the timing as a smoke test, not a latency benchmark.

## Measure index creation time

Create an index on `value`:

```console
mongosh --quiet --eval '
db = db.getSiblingDB("baselineDB");
const start = Date.now();
print("Index name:", db.perf.createIndex({ value: 1 }));
print("Index Creation Time (ms):", Date.now() - start);
'
```

The output is similar to:

```output
Index name: value_1
Index Creation Time (ms): 41
```

On a subsequent run, the index already exists, so the timing will not represent a new index build.

## Test concurrent inserts

Start five parallel shell sessions. Each uses JavaScript database selection and inserts 1,000 documents. The shell loop checks every client’s exit status:

```console
pids=()
for i in {1..5}; do
  mongosh --quiet --eval 'db = db.getSiblingDB("baselineDB"); const result = db.concurrent.insertMany(Array.from({length: 1000}, (_, k) => ({test: k, ts: new Date()}))); assert(result.acknowledged);' &
  pids+=("$!")
done
for pid in "${pids[@]}"; do
  wait "$pid" || { echo "A concurrent client failed"; exit 1; }
done
mongosh --quiet --eval 'print("Concurrent documents:", db.getSiblingDB("baselineDB").concurrent.countDocuments({}))'
```

On the first run against an empty `concurrent` collection, the output ends with:

```output
Concurrent documents: 5000
```

Re-running the test adds another 5,000 documents. Continue to the next section to generate a workload and observe it with `mongotop` and `mongostat`.
