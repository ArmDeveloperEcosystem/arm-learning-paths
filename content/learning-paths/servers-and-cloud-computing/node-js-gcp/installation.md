---
title: Install Node.js
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Node.js 
This guide walks you through installing **Node.js v24.8.0** on a SUSE Arm64 virtual machine using the official tarball package. 

### 1. Download Node.js Binary
First, download the Node.js package (precompiled binaries for Linux Arm64) from the official website.

```console
sudo wget https://nodejs.org/dist/latest/node-v24.8.0-linux-arm64.tar.gz
```

### 2. Extract the Tarball
Unpack the downloaded file so we can access the Node.js binaries.

```console
sudo tar -xvf node-v24.8.0-linux-arm64.tar.gz
```

### 3. Rename Extracted Directory
Rename the extracted folder to something shorter such as node-v24.8.01 for easier reference.

```console
sudo mv node-v24.8.0-linux-arm64 node-v24.8.0
```

### 4. Create a Symlink (Optional)
This step creates a shortcut (`/usr/local/node`) pointing to your Node.js installation directory.

It makes future upgrades easier — you only need to update the symlink instead of changing paths everywhere.

```console
sudo ln -s /usr/local/node-v24.8.0 /usr/local/node
```

### 5. Update PATH Environment Variable

Add Node.js binaries to your PATH so you can run `node` and `npm` commands from anywhere in your terminal.

```console
echo 'export PATH=$HOME/node-v24.8.0/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### 6. Verify Installation
Check that Node.js and npm (Node’s package manager) are installed correctly.

```console
node -v
npm -v
```
You should see an output similar to:
```output
v24.8.0
11.6.0
```

Node.js installation is complete. You can now proceed with the baseline testing.
