---
title: Install TypeScript
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install TypeScript on GCP VM
This page guides you through installing **TypeScript** and its prerequisites on a **GCP SUSE Arm64 VM**. We will install Node.js, npm, TypeScript, and ts-node, and verify that everything works correctly.

### Update SUSE System
Before installing new packages, refresh the repositories and update existing packages:

```console
sudo zypper refresh
sudo zypper update -y
```
This ensures that your VM has the latest package information and security updates.

### Install Node.js and npm
Node.js is required to run TypeScript scripts, and npm is the Node.js package manager:

```console
sudo zypper install -y nodejs npm
```
The above command installs Node.js runtime and npm on your GCP SUSE VM.

### Install TypeScript globally
TypeScript (`tsc`) compiles `.ts` files to JavaScript, and ts-node allows you to run TypeScript directly without compiling:

```console
sudo npm install -g typescript ts-node
```
- Installing globally (`-g`) makes `tsc` and `ts-node` available in any directory on your VM.

### Verify installations
Check that Node.js, npm, TypeScript, and ts-node are installed correctly:

```console
node -v
npm -v
tsc -v
ts-node -v
```

**Output:**

```output
>node -v
v18.20.5
>npm -v
10.8.2
>tsc -v
Version 5.9.3
> ts-node -v
v10.9.2
```

These version outputs confirm that the Node.js and TypeScript are installed correctly and are ready for development or benchmarking.
