---
title: MongoDB Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark MongoDB with **mongotop** and **mongostat**

This guide will help the user measure MongoDB’s performance in real time.
The user will install the official MongoDB database tools, start MongoDB, run a script to simulate heavy load, and watch the database’s live performance using **mongotop** and **mongostat**.

1. Install MongoDB Database Tools

```console
wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu2404-arm64-100.13.0.deb
sudo apt update
sudo apt install -y ./mongodb-database-tools-ubuntu2404-arm64-100.13.0.deb
echo 'export PATH=$PATH:~/mongodb-database-tools-ubuntu2404-arm64-100.13.0/bin' >> ~/.bashrc
source ~/.bashrc
```
These commands download and unpack MongoDB’s official monitoring tools (**mongotop** & **mongostat**), then add them to your PATH so you can run them from any terminal.

2. Verify the Installation

```console
mongotop --version
mongostat --version
```
This checks that both tools were installed correctly and are ready to use.

You should see an output similar to:
```output
mongostat --version
mongotop version: 100.13.0
git version: 23008ff975be028544710a5da6ae749dc7e90ab7
Go version: go1.23.11
   os: linux
   arch: arm64
   compiler: gc
mongostat version: 100.13.0
git version: 23008ff975be028544710a5da6ae749dc7e90ab7
Go version: go1.23.11
   os: linux
   arch: arm64
   compiler: gc
```

3. Make sure that the MongoDB Server that you started in the previous section is still running. If not, start it again, using the command as shown:

```console
mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --fork
```
These commands create a folder for MongoDB’s data, then start the database server in the background, allowing connections from any IP, and save logs for troubleshooting.

4. Create a Long-Running Load Script for Benchmarking

Save this script file as **long_system_load.js**:

```javascript
function randomString(len) {
    return Math.random().toString(36).substring(2, 2 + len);
}

var systemCollections = [
    { db: "admin", coll: "atlascli" },
    { db: "config", coll: "system_sessions_bench" },
    { db: "config", coll: "transactions_bench" },
    { db: "local", coll: "system_replset_bench" },
    { db: "benchmarkDB", coll: "testCollection" },
    { db: "benchmarkDB", coll: "cursorTest" },
    { db: "test", coll: "atlascli" },
    { db: "test", coll: "system_sessions_bench" },
    { db: "test", coll: "admin_system_version_test" }
];

systemCollections.forEach(function(ns) {
    let col = db.getSiblingDB(ns.db).getCollection(ns.coll);
    col.drop();
    for (let i = 0; i < 100; i++) {
        col.insertOne({ rnd: randomString(10), ts: new Date(), idx: i });
    }
    col.findOne();
});

var totalCycles = 50;   
var pauseMs = 1000;      

for (let cycle = 0; cycle < totalCycles; cycle++) {
    systemCollections.forEach(function(ns) {
        let col = db.getSiblingDB(ns.db).getCollection(ns.coll);

        col.insertOne({ cycle, action: "insert", value: randomString(8), ts: new Date() });
        col.find({ cycle: { $lte: cycle } }).limit(10).toArray();
        col.updateMany({}, { $set: { updatedAt: new Date() } });
        col.deleteMany({ idx: { $gt: 80 } });

        let cursor = col.find().batchSize(5);
        while (cursor.hasNext()) {
            cursor.next();
        }
    });

    print(`Cycle ${cycle + 1} / ${totalCycles} completed`);
    sleep(pauseMs);
}

print("=== Long load generation completed ===");
```

This is the load generator script, it creates several collections and repeatedly **inserts, queries, updates** and **deletes** data. Running it simulates real application traffic so the monitors have something to measure.

{{% notice Note %}}
Before proceeding, the load script and the monitoring tools must be run in separate terminals simultaneously.

- The load script continuously generates activity in MongoDB, keeping the database busy with multiple operations.
- The mongotop and mongostat tools monitor and report this activity in real time as it happens.

If all commands are run in the same terminal, the monitoring tools will only start after the script finishes, preventing real-time observation of MongoDB’s performance.
{{% /notice %}}

### Run the load script (start the workload) — Terminal 1

```console
mongosh < long_system_load.js
```

This command tells the MongoDB shell to execute the entire script. The script will run through its cycles and print the progress while generating the read/write activity on the server.

You should see an output similar to:
```output
test> // long_system_load.js

test> // Run with: mongosh < long_system_load.js

test>

test> function randomString(len) {
...     return Math.random().toString(36).substring(2, 2 + len);
... }
[Function: randomString]
test>

test> // ---------- 1. Safe shadow "system-like" namespaces ----------

test> var systemCollections = [
...     { db: "admin", coll: "atlascli" },
...     { db: "config", coll: "system_sessions_bench" },
...     { db: "config", coll: "transactions_bench" },
...     { db: "local", coll: "system_replset_bench" },
...     { db: "benchmarkDB", coll: "testCollection" },
...     { db: "benchmarkDB", coll: "cursorTest" },
...     { db: "test", coll: "atlascli" },
...     { db: "test", coll: "system_sessions_bench" },
...     { db: "test", coll: "admin_system_version_test" }
... ];

test>

test> // Create and warm up

test> systemCollections.forEach(function(ns) {
...     let col = db.getSiblingDB(ns.db).getCollection(ns.coll);
...     col.drop();
...     for (let i = 0; i < 100; i++) {
...         col.insertOne({ rnd: randomString(10), ts: new Date(), idx: i });
...     }
...     col.findOne();
... });

test>

test> // ---------- 2. Generate load loop ----------

test> var totalCycles = 50;   // increase this for longer runs

test> var pauseMs = 1000;      // 1 second pause between cycles

test>

test> for (let cycle = 0; cycle < totalCycles; cycle++) {
...     systemCollections.forEach(function(ns) {
...         let col = db.getSiblingDB(ns.db).getCollection(ns.coll);
...
...         col.insertOne({ cycle, action: "insert", value: randomString(8), ts: new Date() });
...         col.find({ cycle: { $lte: cycle } }).limit(10).toArray();
...         col.updateMany({}, { $set: { updatedAt: new Date() } });
...         col.deleteMany({ idx: { $gt: 80 } });
...
...         let cursor = col.find().batchSize(5);
...         while (cursor.hasNext()) {
...             cursor.next();
...         }
...     });
...
...     print(`Cycle ${cycle + 1} / ${totalCycles} completed`);
...     sleep(pauseMs);
... }
Cycle 1 / 50 completed
Cycle 2 / 50 completed
Cycle 3 / 50 completed
Cycle 4 / 50 completed
Cycle 5 / 50 completed
Cycle 6 / 50 completed
Cycle 7 / 50 completed
Cycle 8 / 50 completed
Cycle 9 / 50 completed
Cycle 10 / 50 completed
Cycle 11 / 50 completed
Cycle 12 / 50 completed
Cycle 13 / 50 completed
Cycle 14 / 50 completed
Cycle 15 / 50 completed
Cycle 16 / 50 completed
Cycle 17 / 50 completed
Cycle 18 / 50 completed
Cycle 19 / 50 completed
Cycle 20 / 50 completed
Cycle 21 / 50 completed
Cycle 22 / 50 completed
Cycle 23 / 50 completed
Cycle 24 / 50 completed
Cycle 25 / 50 completed
Cycle 26 / 50 completed
Cycle 27 / 50 completed
Cycle 28 / 50 completed
Cycle 29 / 50 completed
Cycle 30 / 50 completed
Cycle 31 / 50 completed
Cycle 32 / 50 completed
Cycle 33 / 50 completed
Cycle 34 / 50 completed
Cycle 35 / 50 completed
Cycle 36 / 50 completed
Cycle 37 / 50 completed
Cycle 38 / 50 completed
Cycle 39 / 50 completed
Cycle 40 / 50 completed
Cycle 41 / 50 completed
Cycle 42 / 50 completed
Cycle 43 / 50 completed
Cycle 44 / 50 completed
Cycle 45 / 50 completed
Cycle 46 / 50 completed
Cycle 47 / 50 completed
Cycle 48 / 50 completed
Cycle 49 / 50 completed
Cycle 50 / 50 completed

test>

test> print("=== Long load generation completed ===");
=== Long load generation completed ===

```

The load has been generated successfully. Now, you can proceed with the monitoring:

- **mongotop** to observe activity per collection.
- **mongostat** to monitor overall operations per second, memory usage, and network activity.
