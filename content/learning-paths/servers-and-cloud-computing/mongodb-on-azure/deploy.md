---
title: Install MongoDB and Mongosh
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Get started

Install MongoDB and **mongosh** on Ubuntu 24.04 LTS (Arm64). You will download the binaries, add them to your `PATH`, create data and log directories, and start the server locally to verify the setup.

{{% notice Note %}}
For this exercise, `mongod` runs locally and **access control is disabled** by default. Keep the server bound to `127.0.0.1` until you configure users and authentication. To accept remote connections later, set `--bind_ip` (or `bindIp` in the config) and enable authorization.
{{% /notice %}}

## Install system dependencies

Install the required system packages to support MongoDB:

```console
sudo apt update
sudo apt install -y curl wget tar fio openssl libcurl4
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
sudo chown "$USER:$USER" /var/lib/mongo /var/log/mongodb
```

## Start the MongoDB server (local)

Start `mongod` in the background, explicitly bound to loopback, and write logs to `/var/log/mongodb/mongod.log`. The 1 GiB WiredTiger cache limit leaves memory for other services on this shared test VM; it is not a production tuning recommendation:

```console
mongod --bind_ip 127.0.0.1 --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --wiredTigerCacheSizeGB 1 --fork
```

Sample output:

```output
about to fork child process, waiting until server is ready for connections.
forked process: 32400
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

A `test>` prompt confirms that you connected. The shell can display startup notices about the filesystem, access control, or host settings. This is a local test deployment with authorization disabled; review MongoDB’s [production notes](https://www.mongodb.com/docs/manual/administration/production-notes/) before using it for production.

Run the following inside `mongosh`:

```javascript
db.adminCommand({ ping: 1 })
exit()
```

The ping response should contain `ok: 1`. With this verification complete, proceed to baseline testing on your Cobalt 200 VM.

{{% notice Note %}}
This tarball installation runs `mongod` as your current user. It does not install a systemd service or restart the server automatically after a VM reboot. Re-run the start command after rebooting.
{{% /notice %}}
