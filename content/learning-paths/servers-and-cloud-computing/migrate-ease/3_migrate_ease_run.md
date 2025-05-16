---
# User change
title: "Install migrate-ease"

weight: 4

layout: "learningpathall"

---

# migrate-ease

[migrate-ease](https://github.com/migrate-ease/migrate-ease) is an open-source project designed to analyze codebases specifically for `x86_64` architectures and offers tailored suggestions aimed at facilitating the migration process to AArch64. This tool streamlines the transition, ensuring a smooth and efficient evolution of your software to leverage the benefits of aarch64 architecture.

## Pre-requisites
Before you use `migrate-ease`, certain pre-requisites need to be installed:
{{< tabpane code=true >}}
  {{< tab header="Ubuntu 22.04">}}
sudo apt-get install -y python3 python3-pip python3-venv unzip libmagic1 git
  {{< /tab >}}
  {{< tab header="Debian 13">}}
sudo apt-get install -y python3 python3-pip python3-venv unzip libmagic1 git
  {{< /tab >}}
  {{< tab header="Fedora 42">}}
sudo dnf install -y python3 python3-pip unzip git
  {{< /tab >}}
{{< /tabpane >}}

## Install and setup

Start by checking out the repository with the tool's source code:
```bash
git clone https://github.com/migrate-ease/migrate-ease
cd migrate-ease 
```

At the root directory of migrate-ease, create and activate a python virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the python packages dependencies and set the environment variable to point to it:
```bash
pip3 install -r requirements.txt
export PYTHONPATH=`pwd`
```

## Usage

You are now ready to use `migrate-ease` on your source code. You can use the tool either from the command-line or using a Web GUI. 
 
### Command-line usage

From the command-line, you can use the tool to scan your local codebases with different programming languages. The result from the code analysis is sent to console by default.

```bash
python3 -m {scanner_name} --arch {arch} {scan_path}
```
The result from the scan can also be exported as `txt`, `csv`, `json` or `html`. You will need to specify this using the `--output` option:

To generate a JSON report:
```bash
python3 -m {scanner_name} --output {result_file_name}.json --arch {arch} {scan_path}
```

Here's an explanation of each of the arguments passed to the scanner tool:

**Parameters**

`{scanner_name}`: The name of the scanner, which can be one of cpp, docker, go, java, python or rust.

`{result_file_name}`: The name of the exported results file (without the extension).

`{arch}`: The architecture type, `aarch64` is the default.

`{scan_path}`: The path to the code that needs to be scanned.

You can scan a remote git repository code base as well by passing the URL as shown in the example:
```bash
python3 -m {scanner_name} --output {result_file_name}.json --arch {arch} --git-repo {repo} {clone_path}
```
In the case of git repository scan, `{clone_path}` is a directory where the remote repo code is cloned into. This directory should be empty or must be created by the user.

There are more parameters for user to control the scan functionality. To see this information, use the built-in help as shown:
```bash
python3 -m {scanner_name} -h
```
Replace {scanner_name} with either cpp, docker, go, java, python or rust.

### As Web UI
Migrate-ease also provides a Web UI that supports scanning a git repo with cpp, docker, go, java, python and rust scanners in one time.
To start the web server, simply run:
```
python3 web/server.py
```

Once that is successfully done, you can access a web server hosted at http://localhost:8080

The web UI looks as following:
![example image alt-text#center](web_ui_index.jpg "Figure 1. Web UI to scan a git repo")

A git repo URL is required, and you can specify certain branch name to scan. Once the necessary information is filled, user can click "START SCAN" button to proceed project scanning.

Scanning progress will be shown in the console pane. Once all jobs are done, user will see a web page as following:
![example image alt-text#center](web_ui_result.jpg "Figure 2. Web UI of scan result")

You can download the result by clicking the "download" icon or view the result by clicking the "eye" icon.
