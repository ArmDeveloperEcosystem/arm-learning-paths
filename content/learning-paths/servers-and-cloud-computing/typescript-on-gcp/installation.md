---
title: Install TypeScript
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install TypeScript on GCP VM
This section walks you through installing TypeScript and its dependencies on a Google Cloud Platform (GCP) SUSE Arm64 virtual machine. You’ll install Node.js, npm, TypeScript, and ts-node, and verify that everything works correctly.

Running TypeScript on Google Cloud C4A instances, powered by Axion Arm64 processors, provides a high-performance and energy-efficient platform for Node.js-based workloads.

### Update SUSE System
Before installing new packages, refresh the repositories and update existing ones to ensure your environment is current and secure:

```console
sudo zypper refresh
sudo zypper update -y
```
Keeping your system up to date ensures that dependencies, libraries, and compilers required for Node.js and TypeScript work seamlessly on the Arm64 architecture.

### Install Node.js and npm
Node.js provides the JavaScript runtime that powers TypeScript execution, while npm (Node Package Manager) manages project dependencies and global tools.

Install both packages using SUSE’s repositories:

```console
sudo zypper install -y nodejs npm
```
This command installs the Node.js runtime and npm package manager on your Google Cloud SUSE Arm64 VM.

### Install TypeScript globally
TypeScript (tsc) is the compiler that converts .ts files into JavaScript.
`ts-node` lets you run TypeScript files directly without pre-compiling them. It is useful for testing, scripting, and lightweight development workflows.

Install both globally using npm:

```console
sudo npm install -g typescript ts-node
```
The `-g` flag installs packages globally, making tsc and ts-node available system-wide.

This approach simplifies workflows for developers running multiple TypeScript projects on the same VM.

### Verify installations
Check that Node.js, npm, TypeScript, and ts-node are all installed correctly:

```console
node -v
npm -v
tsc -v
ts-node -v
```

The expected output is:

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

Node.js, npm, and TypeScript are now successfully installed and verified on your Google Cloud C4A (Arm64) virtual machine.
You’re ready to create and execute TypeScript scripts for testing, deployment, or performance benchmarking.
