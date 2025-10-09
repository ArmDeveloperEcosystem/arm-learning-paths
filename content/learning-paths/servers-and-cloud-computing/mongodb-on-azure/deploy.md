---
title: Install MongoDB and Mongosh
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Get started

Install MongoDB and **mongosh** on Ubuntu Pro 24.04 LTS (Arm64). You will download the binaries, add them to your `PATH`, create data and log directories, and start the server locally to verify the setup.

{{% notice Note %}}
For this exercise, `mongod` runs locally and **access control is disabled** by default. Keep the server bound to `127.0.0.1` until you configure users and authentication. To accept remote connections later, set `--bind_ip` (or `bindIp` in the config) and enable authorization.
{{% /notice %}}

## Install system dependencies

Install the required system packages to support MongoDB:

```console
sudo apt update
sudo apt install -y curl wget tar fio openssl libcurl4 net-tools
```

## Download and extract MongoDB

Fetch and unpack the MongoDB binaries for Arm64:

```console
wget https://fastdl.mongodb.org/linux/mongodb-linux-aarch64-ubuntu2404-8.0.12.tgz
tar -xvzf mongodb-linux-aarch64-ubuntu2404-8.0.12.tgz
sudo mv mongodb-linux-aarch64-ubuntu2404-8.0.12 /usr/local/mongodb
```

## Add MongoDB to the system PATH

Enable running MongoDB from any terminal session:

```console
echo 'export PATH=/usr/local/mongodb/bin:$PATH' | sudo tee /etc/profile.d/mongodb.sh
source /etc/profile.d/mongodb.sh
```

## Create data and log directories

Create the database data and log directories and assign ownership to your user:

```console
sudo mkdir -p /var/lib/mongo
sudo mkdir -p /var/log/mongodb
sudo chown -R $USER:$USER /var/lib/mongo /var/log/mongodb
```

## Start the MongoDB server (local)

Start `mongod` in the background and write logs to `/var/log/mongodb/mongod.log`:

```console
mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --fork
```

Sample output:

```output
about to fork child process, waiting until server is ready for connections.
forked process: 3356
child process started successfully, parent exiting
```

## Install mongosh (MongoDB shell)

**mongosh** is the MongoDB shell for running queries and database operations.

Download and install the MongoDB shell for Arm64:

```console
wget https://downloads.mongodb.com/compass/mongosh-2.3.8-linux-arm64.tgz
tar -xvzf mongosh-2.3.8-linux-arm64.tgz
sudo mv mongosh-2.3.8-linux-arm64 /usr/local/mongosh
```

Add `mongosh` to the system `PATH`:

```console
echo 'export PATH=/usr/local/mongosh/bin:$PATH' | sudo tee /etc/profile.d/mongosh.sh
source /etc/profile.d/mongosh.sh
```

## Verify MongoDB and mongosh installation

Confirm that MongoDB and `mongosh` are installed and available:

```console
mongod --version
mongosh --version
```

You should see output similar to:

```output
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
2.3.8
```

## Connect to MongoDB using mongosh

Connect to the local instance and verify an interactive prompt:

```console
mongosh mongodb://127.0.0.1:27017
```

You should see output similar to:

```output
Current Mongosh Log ID: 68b573411523231d81a00aa0
Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.8
Using MongoDB:          8.0.12
Using Mongosh:          2.3.8
mongosh 2.5.7 is available for download: https://www.mongodb.com/try/download/shell

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

------
   The server generated these startup warnings when booting
   2025-09-01T09:45:32.382+00:00: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
   2025-09-01T09:45:33.012+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2025-09-01T09:45:33.012+00:00: This server is bound to localhost. Remote systems will be unable to connect to this server. Start the server with --bind_ip <address> to specify which IP addresses it should serve responses from, or with --bind_ip_all to bind to all interfaces. If this behavior is desired, start the server with --bind_ip 127.0.0.1 to disable this warning
   2025-09-01T09:45:33.012+00:00: Soft rlimits for open file descriptors too low
   2025-09-01T09:45:33.012+00:00: For customers running the current memory allocator, we suggest changing the contents of the following sysfsFile
   2025-09-01T09:45:33.012+00:00: For customers running the current memory allocator, we suggest changing the contents of the following sysfsFile
   2025-09-01T09:45:33.012+00:00: We suggest setting the contents of sysfsFile to 0.
   2025-09-01T09:45:33.012+00:00: Your system has glibc support for rseq built in, which is not yet supported by tcmalloc-google and has critical performance implications. Please set the environment variable GLIBC_TUNABLES=glibc.pthread.rseq=0
------
test>
```

With this verification complete, proceed to MongoDB baseline testing on your Azure Cobalt 100 VM.
