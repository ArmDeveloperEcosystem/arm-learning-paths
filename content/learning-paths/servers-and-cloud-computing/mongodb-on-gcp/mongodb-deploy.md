---
title: Install MongoDB
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This section shows how to install MongoDB and the MongoDB Shell (`mongosh`) on an Arm-based Google Axion C4A instance running Red Hat Enterprise Linux. You will download the Arm64 binaries, update your environment, and verify that the database server runs correctly.

## Install system dependencies

Install the required system packages:

```console
sudo dnf update -y
sudo dnf install -y libcurl openssl tar wget curl


Download and extract MongoDB

Fetch and unpack the MongoDB Arm64 (aarch64) binaries for RHEL 9.3:

```console
wget https://fastdl.mongodb.org/linux/mongodb-linux-aarch64-rhel93-8.0.12.tgz
tar -xzf mongodb-linux-aarch64-rhel93-8.0.12.tgz
ls mongodb-linux-aarch64-rhel93-8.0.12/bin
```

Add the binaries to your `PATH` so they are available in every shell session:

```console
echo 'export PATH=~/mongodb-linux-aarch64-rhel93-8.0.12/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

## Start the MongoDB server



Create a data directory for MongoDB files:

```console
mkdir -p ~/mongodb-data/db
```
Start mongod in the foreground to verify that it launches and to view logs directly:

```console
mongod --dbpath ~/mongodb-data/db
```

Starting the server in the foreground allows you to see real-time logs and is useful for debugging or verifying that MongoDB starts correctly. However, this will occupy your terminal and stop the server if you close the terminal or interrupt it.

Stop the server (for example, with **Ctrl+C**), then confirm that data files were created:

```console
ls ~/mongodb-data/db/
```

Example output:

```output
collection-0-7680310461694759627.wt  index-3-7680310461694759627.wt  mongod.lock      WiredTiger.lock
```

Once you’ve confirmed it’s working, you can start MongoDB in the background using the `--fork` option and redirecting logs to a file. This allows MongoDB to run continuously without tying up your terminal session. 

Start mongod in the background with logging enabled so it continues to run after you close the terminal:

```console
mongod --dbpath ~/mongodb-data/db --logpath ~/mongodb-data/mongod.log --fork
```

## Install MongoDB Shell (mongosh)

`mongosh` is the MongoDB shell used to interact with your database. Download and install mongosh for Arm64:

```console
wget https://github.com/mongodb-js/mongosh/releases/download/v2.5.6/mongodb-mongosh-2.5.6.aarch64.rpm
sudo dnf install -y ./mongodb-mongosh-2.5.6.aarch64.rpm
```

Verify the installation:
```console
mongosh --version
```

## Connect to MongoDB with mongosh

Connect to the local server:

```console
mongosh mongodb://127.0.0.1:27017
```

Sample output:

```output
Connecting to: mongodb://127.0.0.1:27017/?directConnection=true&...
Using MongoDB: 8.0.12
Using Mongosh: 2.5.6
...
test>
```

With MongoDB and `mongosh` successfully installed and running, you’re now ready to proceed with baseline testing.
