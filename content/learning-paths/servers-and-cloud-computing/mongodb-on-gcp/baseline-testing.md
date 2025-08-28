---
title: Baseline Testing
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


Since MongoDB is installed successfully on your GCP C4A Arm virtual machine, follow these steps to validate that the server is running and accepting local connections.

## MongoDB Baseline Testing (Using **mongosh**) 

1. Connect to MongoDB

Open a shell session to the local MongoDB instance:
```console
mongosh mongodb://127.0.0.1:27017
```

2. Create a Test Database and Collection:

```console
use baselineDB
db.createCollection("test")
```
This creates a new database **baselineDB** and an empty collection named test.

You should see an output similar to:

```output
test> use baselineDB
... db.createCollection("test")
...
switched to db baselineDB
```
3. Insert 10,000 Test Documents:

```javascript
for (let i = 0; i < 10000; i++) {
  db.test.insertOne({
    record: i,
    status: "new",
    timestamp: new Date()
  })
}
```
This simulates basic write operations with timestamped records. 
10,000 documents will be cretaed and inserted into the test collection of the currently selected database.
The record field would increment from 0 to 9999. The status is always "new". 
The timestamp would capture the insertion time for each document using ***new Date()***.

You should see an output similar to:

```output
{
  acknowledged: true,
  insertedId: ObjectId('6892dacfbd44e23df4750aa9')
}
```

4. Read (Query) a Subset of Documents:

Fetch a few documents to verify read functionality.
```javascript
db.test.find({ status: "new" }).limit(5)
```
This command is a simple read operation to verify that your data is inserted correctly. It queries the test collection in the current database, and only returns documents where the status is "new". ***limit(5)*** returns only the first 5 matching documents.

You should see an output similar to:

```output
[
 {
    _id: ObjectId('6892dacbbd44e23df474e39a'),
    record: 0,
    status: 'new',
    timestamp: ISODate('2025-08-06T04:32:11.090Z')
  },
  {
    _id: ObjectId('6892dacbbd44e23df474e39b'),
    record: 1,
    status: 'new',
    timestamp: ISODate('2025-08-06T04:32:11.101Z')
  },
  {
    _id: ObjectId('6892dacbbd44e23df474e39c'),
    record: 2,
    status: 'new',
    timestamp: ISODate('2025-08-06T04:32:11.103Z')
  },
  {
    _id: ObjectId('6892dacbbd44e23df474e39d'),
    record: 3,
    status: 'new',
    timestamp: ISODate('2025-08-06T04:32:11.104Z')
  },
  {
    _id: ObjectId('6892dacbbd44e23df474e39e'),
    record: 4,
    status: 'new',
    timestamp: ISODate('2025-08-06T04:32:11.106Z')
  }
]
```
5. Update a Document:

Update a specific document's field to validate update capability.
```javascript
db.test.updateOne({ record: 100 }, { $set: { status: "processed" } })
```
Above command will find the first document where record is exactly 100, and updates that document by setting its status field to "processed".

You should see an output similar to:

```output
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```
6. View the Updated Document Before Deletion

```console
db.test.findOne({ record: 100 })
```
This retrieves the document where record is 100, allowing you to verify that its status has been updated to "processed".

You should see output similar to:

```output
{
  _id: ObjectId('689490ddb7235c65ca74e3fe'),
  record: 100,
  status: 'processed',
  timestamp: ISODate('2025-08-07T11:41:17.508Z')
}
```

7. Delete a Document:

```javascript
db.test.deleteOne({ record: 100 })
```
This tells MongoDB to delete one document from the test collection, where record is exactly 100.

You should see an output similar to:

```output
{ acknowledged: true, deletedCount: 1 }
```
Now, confirm the deletion:

```console
db.test.findOne({ record: 100 })
```
The above command confirms that the document was successfully deleted.

You should see an output similar to:
```output
null
```

8. Measure Execution Time (Optional):

The below snippet measures how long it takes to insert documents for performance insight.
```javascript
var start = new Date()
for (let i = 0; i < 10000; i++) {
  db.test.insertOne({ sample: i })
}
print("Insert duration (ms):", new Date() - start)
```
You should see an output similar to:

```output
Insert duration (ms): 4427
```
9. Count Total Documents:

Count total entries to confirm expected data volume.
```javascript
db.test.countDocuments()
```
You should see an output similar to:

```output
19999
```
The count **19999** reflects the total documents after inserting 10,000 initial records, adding 10,000 more (in point 8), and deleting one (record: 100).

10. Clean Up (Optional):

Deletes the **baselineDB** database and all its contents.
```javascript
db.dropDatabase()
```
You should see an output similar to:

```output
{ ok: 1, dropped: 'baselineDB' }
```

The above is a destructive command that completely deletes the current database you are connected to in mongosh.

The above operations confirm that MongoDB is installed successfully and is functioning as expected on the GCP Arm64 environment.

Using **mongosh**, you validated key database operations such as **insert**, **read**, **update**, **delete**, and **count**.
Now, your MongoDB instance is ready for further benchmarking and production use.
