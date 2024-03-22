---
title: Before you begin
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Login to the target system

First, ensure that you have logged into the target system (e.g. via Secure Shell) on which the Sysreport tool should run.

The Sysreport tool is a command-line tool only, so make sure you have access to a terminal program.

## Check Python is installed

Open a terminal and run the following command:

```console
python --version
```

If Python is installed correctly, a version number will be displayed:
```output
Python 3.9.5
```

## Install Sysreport

You can download a copy of the Sysreport tool by cloning the following GitHub repository:
```console
git clone https://github.com/ArmDeveloperEcosystem/sysreport.git
```

## Test Sysreport

Confirm that Sysreport has been cloned correctly by changing into the correct directory and running the tool:
```console
cd sysreport/src
python sysreport.py --help
```

If the tool is working correctly, the tool usage should be displayed:
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