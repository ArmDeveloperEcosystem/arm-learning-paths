---
title: Baseline Testing
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that MongoDB is installed on your Google Axion C4A Arm VM, verify that the server is running and accepting local connections.

## Connect to MongoDB

Open a shell session to the local MongoDB instance:

```console
mongosh mongodb://127.0.0.1:27017


## Create a test database and collection

Switch to a new database and create a collection:

```javascript
use baselineDB
db.createCollection("test")
```

This creates a new database named `baselineDB` and an empty collection called `test`.

Expected output:

```output
switched to db baselineDB
{ ok: 1 }
```

## Insert 10,000 test documents

Populate the collection with 10,000 timestamped documents:

```javascript
for (let i = 0; i < 10000; i++) {
  db.test.insertOne({
    record: i,
    status: "new",
    timestamp: new Date()
  })
}
```

Each document contains:
- `record`: a counter from 0 to 9999
- `status`: `"new"`
- `timestamp`: the current date/time of insertion

Sample output:

```output
{ acknowledged: true, insertedId: ObjectId('...') }
```

## Read a subset of documents

Verify read functionality by querying the first few documents:

```javascript
db.test.find({ status: "new" }).limit(5)
```

This returns the first 5 documents where `status` is `"new"`.

## Update a document

Update a specific document by changing its status:

```javascript
db.test.updateOne({ record: 100 }, { $set: { status: "processed" } })
```

This finds the document where `record` is 100 and updates the `status`.

Expected output:

```output
{
  acknowledged: true,
  matchedCount: 1,
  modifiedCount: 1
}
```

## View the updated document

Confirm that the document was updated:

```javascript
db.test.findOne({ record: 100 })
```

Expected output:

```output
{
  _id: ObjectId('...'),
  record: 100,
  status: 'processed',
  timestamp: ISODate('...')
}
```

## Delete a document

The command below tells MongoDB to delete one document from the test collection, where record is exactly 100:

```javascript
db.test.deleteOne({ record: 100 })
```

Verify deletion:

```javascript
db.test.findOne({ record: 100 })
```

Expected output:

```output
null
```

## Measure execution time (optional)

Measure how long it takes to insert 10,000 documents:

```javascript
var start = new Date()
for (let i = 0; i < 10000; i++) {
  db.test.insertOne({ sample: i })
}
print("Insert duration (ms):", new Date() - start)
```

Sample output:

```output
Insert duration (ms): 4427
```

## Count total documents

Check the total number of documents in the collection:

```javascript
db.test.countDocuments()
```

Expected output:

```output
19999
```

The count **19999** reflects the total documents after inserting 10,000 initial records, adding 10,000 more (in point 8), and deleting one (record: 100).


## Clean up (optional)

For the sake of resetting the environment, this following command deletes the current database you are connected to in mongosh. 

Drop the `baselineDB` database to remove all test data:

```javascript
db.dropDatabase()
```

Expected output:

```output
{ ok: 1, dropped: 'baselineDB' }
```

These baseline operations confirm that MongoDB is functioning properly on your GCP Arm64 environment. Using `mongosh`, you validated inserts, queries, updates, deletes, and basic performance timing. Your instance is now ready for benchmarking or application integration.