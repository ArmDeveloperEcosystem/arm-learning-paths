---
title: Install the automated benchmark and Benchstat runner
weight: 53

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the last section, you learned how to run benchmarks and Benchstat manually. Now you'll automate that process and generate visual reports using a tools called `rexec_sweet`.

## What is rexec_sweet?

`rexec_sweet` is a Python project available on GitHub that automates the benchmarking workflow. It connects to your GCP instances, runs benchmarks, collects results, and generates HTML reports - all in one step.

It provides several key benefits:

- **Automation**: Runs benchmarks on multiple VMs without manual SSH connections
- **Consistency**: Ensures benchmarks are executed with identical parameters
- **Visualization**: Generates HTML reports with interactive charts for easier analysis

Before running the tool, ensure you've completed the "Install Go, Sweet, and Benchstat" step. All other dependencies are installed automatically by the installer.

## Set up rexec_sweet

Follow the steps below to set up `rexec_sweet`.

### Create a working directory

On your local machine, open a terminal, and create a new directory:

```bash
mkdir rexec_sweet
cd rexec_sweet
```
   
### Clone the repository

Get `rexec_sweet` from GitHub:

```bash
git clone https://github.com/geremyCohen/go_benchmarks.git
cd go_benchmarks
```

### Run the installer

Copy and paste this command into your terminal to run the installer:

```bash
./install.sh
```

If the installer detects that you already have dependencies installed, it might ask you if you want to reinstall them:

```output
pyenv: /Users/gercoh01/.pyenv/versions/3.9.22 already exists
continue with installation? (y/N)
```

If you see this prompt, enter `N` to continue with the installation without modifying the existing installed dependencies.

### Verify VM status

Make sure the GCP VM instances you created in the previous section are running. If not, start them now, and wait a few minutes for them to finish booting.

{{% notice Note %}}
The installer prompts you to authenticate with Google Cloud Platform (GCP) using the gcloud command-line tool at the end of install. If after installing you have issues running or you get GCP authentication errors, you can manually authenticate with GCP by running the following command: `gcloud auth login`
{{% /notice %}}   

Continue on to the next section to run the tool and see how it simplifies the benchmarking process.
