---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Porting Advisor for Graviton

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- cloud
- sve
- neon
- Armv8
- Armv8-A
- Armv9
- Armv9-A


### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author_primary: Jason Andrews

### Link to official documentation
official_docs: https://github.com/aws/porting-advisor-for-graviton/

author_primary: Jason Andrews

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Porting Advisor for Graviton](https://github.com/aws/porting-advisor-for-graviton/) is a command line tool for assessing the portability of software to AWS Graviton processors. 

Porting Advisor analyzes source code for known patterns and dependencies, and generates a report with any incompatibilities.

Supported operating systems include Linux, Windows, and macOS. 

Porting Advisor analyzes C/C++, Python, Java, Fortran, and Go applications. 

## Before you begin

Follow the instructions below to install and use Porting Advisor on Ubuntu or [Amazon Linux 2023](https://aws.amazon.com/linux/amazon-linux-2023/). 

When the instructions are different, operating system specific tabs are provided. 

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

Porting Advisor has the following prerequisites: 
- Python 3.10 or above
- Python pip
- Python venv

If you want to analyze Java applications you will also need:
- Java 17 or above
- Maven

Install the prerequisites using the package manager:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
sudo apt update
sudo apt install python3-pip python-is-python3 python3-venv -y
  {{< /tab >}}
  {{< tab header="AL2023" language="bash">}}
sudo dnf install git -y
sudo dnf install python3.11 -y
  {{< /tab >}}
{{< /tabpane >}}

If you want to analyze Java applications:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
wget -O- https://apt.corretto.aws/corretto.key | sudo apt-key add - 
sudo add-apt-repository 'deb https://apt.corretto.aws stable main' -y
sudo apt-get update; sudo apt-get install -y java-17-amazon-corretto-jdk
sudo apt install maven -y
  {{< /tab >}}
  {{< tab header="AL2023" language="bash">}}
sudo dnf install java-17-amazon-corretto -y
sudo dnf install maven -y
  {{< /tab >}}
{{< /tabpane >}}

## Installation

Download Porting Advisor from GitHub:

```bash
git clone https://github.com/aws/porting-advisor-for-graviton.git
cd porting-advisor-for-graviton
```

Porting Advisor can be run as a Python script or as an executable. If you want to run the executable, you should still complete the run as a script section to confirm your environment is setup correctly.

### Run as a script

To setup to run as a python script, create a Python virtual environment:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
python3 -m venv .venv
  {{< /tab >}}
  {{< tab header="AL2023" language="bash">}}
python3.11 -m venv .venv
  {{< /tab >}}
{{< /tabpane >}}

Enter the Python virtual environment and install the required packages:

```bash
source .venv/bin/activate
pip install -r requirements.txt
pip install pyinstaller certifi
```

Confirm Porting Advisor runs as a script:

```console
python3 src/porting-advisor.py --help
```

The output should be a long help message starting with the usage information and explaining the options for Porting Advisor. 

```output
usage: porting-advisor [-h] [--issue-types ISSUE_TYPES] [--no-filter] [--no-progress] [--output OUTPUT]
                       [--output-format OUTPUT_FORMAT] [--quiet] [--target-os TARGET_OS] [--version]
                       [--logging-level {error,warning,info,debug}] [--log-file LOG_FILE] [--log-to-console]
                       DIRECTORY
```


### Run as an executable

Running Porting Advisor as an executable requires a build step. 

The executable is a good option if you want to run Porting Advisor on multiple machines. 

The executable can be copied to other machines and run without installing Python packages. 

Build the executable:

```bash
./build.sh
```

A success message will be printed when the build completes:

```output
*** Success: Executable saved at dist/porting-advisor-linux-aarch64 ***
```

The executable is in the `dist` directory with the filename printed in the output. 

Confirm Porting Advisor runs as an executable:

```bash
./dist/porting-advisor-linux-aarch64 --help
```

The output will be the same help message printed by the Python invocation.

You can copy the executable from the `dist` folder to any another machine (with the same operating system and architecture) and use Porting Advisor immediately. There is no need to install anything related to Python.

### Test a sample project

The Porting Advisor includes some small examples in the `sample-projects` directory of the GitHub repository. 

Run Porting Advisor on a Go sample with the executable:

```bash
./dist/porting-advisor-linux-aarch64 sample-projects/java-samples/
```

The recommendations for this application will be printed along with links on where to get more details.

```output
Porting Advisor for Graviton v1.1.1
Report date: 2024-06-25 08:47:06

2 files scanned.
detected java code. we recommend using Corretto. see https://aws.amazon.com/corretto/ for more details.
detected java code. min version 8 is required. version 11 or above is recommended. see https://github.com/aws/aws-graviton-getting-started/blob/main/java.md for more details.

Report generated successfully. Hint: you can use --output FILENAME.html to generate an HTML report.
```

Try out the other sample projects. 

You are ready to use Porting Advisor for Graviton on your own projects.

