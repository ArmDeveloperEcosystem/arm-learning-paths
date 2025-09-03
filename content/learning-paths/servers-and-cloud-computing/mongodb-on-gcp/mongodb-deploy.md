---
title: Install MongoDB
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you’ll install MongoDB and the MongoDB Shell (`mongosh`) by downloading the necessary binaries, configuring your environment, and verifying that the database server is running correctly.

### 1. Install System Dependencies

Start by installing required system packages to support MongoDB:

```console
sudo dnf update
sudo dnf install -y libcurl openssl tar wget curl
```

### 2. Download and Extract MongoDB

Next, fetch and unpack the MongoDB binaries for Arm:

```console
wget https://fastdl.mongodb.org/linux/mongodb-linux-aarch64-rhel93-8.0.12.tgz
tar -xzf mongodb-linux-aarch64-rhel93-8.0.12.tgz
ls mongodb-linux-aarch64-rhel93-8.0.12/bin
```

To make MongoDB binaries accessible from any terminal session, add them to your PATH:

```console
echo 'export PATH=~/mongodb-linux-aarch64-rhel93-8.0.12/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### 3. Start the MongoDB server



Set up a directory to store MongoDB's data files:

```console
mkdir -p ~/mongodb-data/db
```
Run MongoDB in the **foreground** to verify it starts correctly:

```console
mongod --dbpath ~/mongodb-data/db
```

Starting the server in the **foreground** allows you to see real-time logs and is useful for debugging or verifying that MongoDB starts correctly. However, this will occupy your terminal and stop the server if you close the terminal or interrupt it.

After stopping the server (e.g., with `Ctrl+C`), confirm that files have been created in the database directory:

```console
ls ~/mongodb-data/db/
```

Example output:

```output
collection-0-7680310461694759627.wt  index-3-7680310461694759627.wt  mongod.lock      WiredTiger.lock
```

Once you’ve confirmed it’s working, you can start MongoDB in the **background** using the `--fork` option and redirecting logs to a file. This allows MongoDB to run continuously without tying up your terminal session. To start MongoDB in the **background** with logging enabled:

```console
mongod --dbpath ~/mongodb-data/db --logpath ~/mongodb-data/mongod.log --fork
```


### 4. Install mongosh

`mongosh` is the MongoDB shell used to interact with your database. Download and install it for Arm:

```console
wget https://github.com/mongodb-js/mongosh/releases/download/v2.5.6/mongodb-mongosh-2.5.6.aarch64.rpm
sudo dnf install -y ./mongodb-mongosh-2.5.6.aarch64.rpm
```

Confirm that`mongosh` was installed correctly by checking that the version is printed:

```console
mongosh --version
```

### 5. Connect to MongoDB via mongosh

Finally, connect to your MongoDB server using the shell:

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
