---
title: Install MongoDB on Google Axion C4A virtual machine
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Install MongoDB and mongosh on Google Axion C4A virtual machine

Install MongoDB and mongosh on GCP RHEL 9 Arm64 by downloading the binaries, setting up environment paths, configuring data and log directories, and starting the server for local access and verification.

1. Install System Dependencies

Install required system packages to support MongoDB:
```console
sudo dnf install -y libcurl openssl tar wget curl
```

2. Download annd Extract MongoDB

Fetch and unpack the MongoDB binaries for Arm64:
```console
wget https://fastdl.mongodb.org/linux/mongodb-linux-aarch64-rhel93-8.0.12.tgz
tar -xzf mongodb-linux-aarch64-rhel93-8.0.12.tgz
ls mongodb-linux-aarch64-rhel93-8.0.12/bin
```

3. Add MongoDB to System PATH

Enable running mongod from any terminal session:
```console
echo 'export PATH=~/mongodb-linux-aarch64-rhel93-8.0.12/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

4. Create a data Directory

Set up the database data directory:
```console
mkdir -p ~/mongodb-data/db
```

5. Start MongoDB Server 

Start MongoDB in the **foreground** (without --fork) to view real-time output and ensure it starts correctly:
```console
~/mongodb-linux-aarch64-rhel93-8.0.12/bin/mongod --dbpath ~/mongodb-data/db
```
Once confirmed it's working, you can start MongoDB in the **background** with logging:
```console
./mongodb-linux-aarch64-rhel93-8.0.12/bin/mongod --dbpath ~/mongodb-data/db --logpath ~/mongodb-data/mongod.log --fork
```
{{% notice Note %}}Make sure the **~/mongodb-data/db** directory exists before starting.{{% /notice %}}

6. Install mongosh

**mongosh** is the MongoDB Shell used to interact with your MongoDB server. It provides a modern, user-friendly CLI for running queries and database operations.

Download and install MongoDB’s command-line shell for Arm:
```console
wget https://github.com/mongodb-js/mongosh/releases/download/v2.5.6/mongodb-mongosh-2.5.6.aarch64.rpm
sudo dnf install -y ./mongodb-mongosh-2.5.6.aarch64.rpm
```
### Verify Mongodb and mongosh Installation

Check if MongoDb and mongosh is properly installed:
```console
mongod --version
mongosh --version
```
You should see an output similar to: 
```output
db version v8.0.12
Build Info: {
    "version": "8.0.12",
    "gitVersion": "b60fc6875b5fb4b63cc0dbbd8dda0d6d6277921a",
    "openSSLVersion": "OpenSSL 3.2.2 4 Jun 2024",
    "modules": [],
    "allocator": "tcmalloc-google",
    "environment": {
        "distmod": "rhel93",
        "distarch": "aarch64",
        "target_arch": "aarch64"
    }
}
$ mongosh --version
2.5.6
```

### Connect to MongoDB via mongosh

Start interacting with MongoDB through its shell interface:
```console
mongosh mongodb://127.0.0.1:27017
```
You should see an output similar to: 
```output
Current Mongosh Log ID: 6891ebb158db5b705d74e399
Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.6
Using MongoDB:          8.0.12
Using Mongosh:          2.5.6

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

------
   The server generated these startup warnings when booting
   2025-08-05T07:17:45.864+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2025-08-05T07:17:45.864+00:00: Soft rlimits for open file descriptors too low
   2025-08-05T07:17:45.864+00:00: For customers running the current memory allocator, we suggest changing the contents of the following sysfsFile
   2025-08-05T07:17:45.864+00:00: We suggest setting the contents of sysfsFile to 0.
   2025-08-05T07:17:45.864+00:00: Your system has glibc support for rseq built in, which is not yet supported by tcmalloc-google and has critical performance implications. Please set the environment variable GLIBC_TUNABLES=glibc.pthread.rseq=0
------

test>
```

MongoDB installation is complete. You can now proceed with the baseline testing.
