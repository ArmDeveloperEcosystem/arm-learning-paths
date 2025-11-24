---
title: Establish a TypeScript performance baseline
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your TypeScript baseline
This section walks you through the baseline setup and validation of TypeScript on a Google Cloud C4A (Axion Arm64) virtual machine running SUSE Linux. The goal is to confirm that your TypeScript environment is functioning correctly, from initializing a project to compiling and executing a simple TypeScript file, ensuring a solid foundation before performance or benchmarking steps.

## Set up a TypeScript project
Before running any tests, you’ll create a dedicated project directory and initialize a minimal TypeScript environment.

## Create project folder

Start by creating a new folder to hold your TypeScript project files:

```console
mkdir ~/typescript-benchmark
cd ~/typescript-benchmark
```
This creates a workspace named `typescript-benchmark` in your home directory, ensuring all TypeScript configuration and source files are organized separately from system files and global modules.

### Initialize npm project

Next, initialize a new Node.js project. This creates a `package.json` file that defines your project metadata, dependencies, and scripts.

```console
npm init -y
```

## Install Node.js type definitions

To enable TypeScript to properly recognize Node.js built-in APIs (like fs, path, and process), install the Node.js type definitions package:

```console
npm install --save-dev @types/node
```

You should see output similar to:
```output
{
  "name": "typescript-benchmark",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": ""
}
```

## Perform baseline testing
With the TypeScript environment configured, you’ll now perform a baseline functionality test to confirm that TypeScript compilation and execution work correctly on your Google Cloud SUSE Arm64 VM.

### Create a simple TypeScript file

Create a file named `hello.ts` with the following content:

```typescript
const greet = (name: string): string => {
    return `Hello, ${name}!`;
};

console.log(greet("GCP SUSE ARM64"));
```
This simple function demonstrates TypeScript syntax, type annotations, and basic console output.

### Compile TypeScript

Use the TypeScript compiler (tsc) to transpile the .ts file into JavaScript:

```console
tsc hello.ts
```
This generates a new file named `hello.js` in the same directory.

### Run compiled JavaScript

Now, execute the compiled JavaScript using Node.js. This step verifies that:

- The TypeScript code was successfully compiled into valid JavaScript.
- The JavaScript code runs correctly in the Node.js runtime on your GCP SUSE VM.

Execute the compiled JavaScript file:

```console
node hello.js
```

You should see output similar to:

```output
Hello, GCP SUSE ARM64
```
You have successfully verified that your TypeScript environment is working correctly.
Next, you can proceed to TypeScript performance benchmarking to measure compilation and runtime performance on your Google Cloud Arm64 VM.
