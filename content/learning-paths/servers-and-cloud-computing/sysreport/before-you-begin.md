---
title: Before you begin
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Sysreport is a command-line tool, so make sure you can log in to the target system using [Secure Shell (SSH)](/install-guides/ssh/) or have a local console and are comfortable working on the Linux command line.

## Confirm Python and Git are installed

Depending on how Python versions are managed on your system, the Python command below may vary. In this Learning Path, we'll assume that Python is invoked using the `python3` command.

To confirm Python is installed, run the following command:

```console
python3 --version
```

If Python is installed, a version number will be displayed:

```output
Python 3.9.5
```

If Python is not installed, use the package manager for your Linux distribution to install it. 

To confirm Git is installed, run the following command:

```console
git --version
```

If Git is installed, a version number will be displayed:

```output
git version 2.34.1
```

If Git is not installed, use the package manager for your Linux distribution to install it. 

## Install Sysreport

You can download Sysreport by cloning the GitHub repository:

```console
git clone https://github.com/ArmDeveloperEcosystem/sysreport.git
```

## Test Sysreport

Confirm Sysreport works correctly by changing into the `sysreport/src` directory and running the command: 

```console
cd sysreport/src
python3 sysreport.py --help
```

If Sysreport is working correctly, the usage message is displayed:

```output
usage: sysreport.py [-h] [--config] [--advice] [--no-advice] [--color]
                    [--no-color] [--vulnerabilities] [-v]

Check system configuration

optional arguments:
  -h, --help         show this help message and exit
  --config           list kernel build-time configuration
  --advice           show configuration advice
  --no-advice        don't show configuration advice
  --color            use ANSI color escape codes in output
  --no-color         disable ANSI color escape codes in output
  --vulnerabilities
  -v, --verbose      increase verbosity
```