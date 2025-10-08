---
title: TypeScript Baseline Testing on Google Axion C4A Arm Virtual Machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Baseline Setup for TypeScript
This guide covers the **baseline setup and testing** of TypeScript on a **Google Axion C4A virtual machine** running SUSE Linux. The objective is to ensure that the TypeScript environment is installed correctly, that basic compilation works, and that a simple TypeScript script can run on the VM.

### Set Up a TypeScript Project
Before testing, we need a project folder with all necessary TypeScript dependencies.  

**1. Create project folder**

Create a dedicated folder for your TypeScript project:

```console
mkdir ~/typescript-benchmark
cd ~/typescript-benchmark
```
This ensures all files are organized in one place, separate from system files.

**2. Initialize npm project**

Initialize a Node.js project with default settings:

```console
npm init -y
```
The above command creates a  `package.json` file, which manages your project dependencies and scripts.

**3. Install Node.js type definitions**

These definitions allow TypeScript to understand Node.js APIs, enabling type checking and code autocompletion.

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

### Baseline Testing
After setting up the project, we perform baseline testing to verify that TypeScript is working correctly on the GCP SUSE VM.

**1. Create a Simple TypeScript File**

Create a file named `hello.ts` with the following content:

```typescript
const greet = (name: string): string => {
    return `Hello, ${name}!`;
};

console.log(greet("GCP SUSE ARM64"));
```
This simple function demonstrates TypeScript syntax, type annotations, and basic console output.

**2. Compile TypeScript**

The TypeScript compiler (`tsc`) converts `hello.ts` into `hello.js`, which can be executed by Node.js.

```console
tsc hello.ts
```

**3. Run compiled JavaScript**

After compiling the TypeScript file into JavaScript (`hello.js`), you need to execute it using `Node.js`. This step verifies that:

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
This verifies the basic functionality of the TypeScript installation before proceeding to the benchmarking.
