---
title: Installing the Automated benchmark and benchstat runner
weight: 53

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the last section, you learned how to run benchmarks and benchstat manually.  In this section, you'll learn how to run them automatically, with enhanced visualization of the results.


## Introducing rexec_sweet.py

To make running benchmarks and `benchstat` easier, you can use the `rexec_sweet.py` script.  This script automates the process of running benchmarks on both your Arm-based and x86-based VMs, and then running `benchstat` to compare the results.

### Setting up the script

1. On your local machine, open a terminal, and create a directory to store the `rexec_sweet.py` script and related files. For example, you can create a directory called `rexec_sweet`:

```bash
mkdir rexec_sweet
cd rexec_sweet
```
   
2. Clone the `rexec_sweet.py` script from the GitHub repository:

```bash
git clone https://github.com/geremyCohen/go_benchmarks.git
cd go_benchmarks
```

3. Copy and paste this code into your terminal to run the installer for `rexec_sweet.py`:

```bash
./install.sh
```

If the install.sh script detects that you already have dependencies installed, it may ask you if you wish to reinstall them with the following prompt:

```output
$ ./install.sh
...
pyenv is already installed
virtualenv is already installed
pyenv-virtualenv is already installed
pyenv: /Users/gercoh01/.pyenv/versions/3.9.22 already exists
continue with installation? (y/N)
```

If you see this prompt, enter `N` (not `Y`!) to continue with the installation without modifying the existing installed dependencies.



4. Make sure the GCP VM instances you created in the previous section are running.  If not, start them now.

{{% notice Note %}}
The install script will prompt you to authenticate with Google Cloud Platform (GCP) using the gcloud command-line tool at the end of install. If after installing you have issues running the script and/or get GCP authentication errors, you can manually authenticate with GCP by running the following command: `gcloud auth login`
{{% /notice %}} 


Continue on to the next section to run the script.