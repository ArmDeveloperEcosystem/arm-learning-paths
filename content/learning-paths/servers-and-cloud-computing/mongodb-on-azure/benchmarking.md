---
title: Generate a MongoDB workload
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install MongoDB Database Tools

The tools package provides `mongotop` and `mongostat`. Download and install the Ubuntu 24.04 Arm64 package:

```console
wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu2404-arm64-100.13.0.deb
sudo apt install -y ./mongodb-database-tools-ubuntu2404-arm64-100.13.0.deb
mongotop --version
mongostat --version
```

The `.deb` installs the tools into the system PATH; no shell profile changes are needed.

## Create a bounded workload

In terminal 1 on your VM, create `long_system_load.js` with this content. The script uses only a tutorial collection, seeds 1,000 documents, and runs insert, read, update, and delete operations for 60 seconds:

```javascript
const workloadDB = db.getSiblingDB("benchmarkDB");
const collection = workloadDB.testCollection;
for (let i = 0; i < 1000; i++) {
  collection.updateOne({ _id: i }, { $set: { value: i } }, { upsert: true });
}
const deadline = Date.now() + 60000;
let cycles = 0;
while (Date.now() < deadline) {
  const id = cycles % 1000;
  const inserted = collection.insertOne({ value: cycles, temporary: true });
  assert(inserted.acknowledged);
  assert(collection.findOne({ _id: id }) !== null);
  assert(collection.updateOne({ _id: id }, { $inc: { value: 1 } }).matchedCount === 1);
  assert(collection.deleteOne({ _id: inserted.insertedId }).deletedCount === 1);
  cycles++;
}
print("Completed workload cycles:", cycles);
```

Run the script from your VM terminal:

```console
mongosh --quiet mongodb://127.0.0.1:27017 long_system_load.js
```

The script stops after its 60-second loop and reports the number of completed cycles. Keep it running while you sample the monitoring tools in terminals 2 and 3. Connect each terminal to the same VM using SSH. Re-run the script if it finishes before you start monitoring.

This is a single-client synthetic workload for learning the monitoring tools. A cycle contains four operations; cycle count is not a MongoDB capacity measurement. The script generates activity in `benchmarkDB.testCollection`, not internal replication or transaction-system collections.
