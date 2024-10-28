---
title: Pulumi
minutes_to_complete: 5
official_docs: https://www.pulumi.com/docs/
author_primary: Jason Andrews

test_images:
- ubuntu:latest

### FIXED, DO NOT MODIFY
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: FALSE            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Pulumi](https://www.pulumi.com/) is a multi-language infrastructure as code tool. Pulumi is [open source](https://github.com/pulumi/pulumi) and makes it easy to deploy cloud infrastructure.

## Before you begin

Pulumi is available for a variety of operating systems and Linux distributions and has multiple ways to install it.

This article provides a quick solution to install Pulumi on Linux.

## Installation {#install}

Run the following command to download and install Pulumi on Linux:

```bash
curl -fsSL https://get.pulumi.com | sh
```

The installer output will be similar to:

```output
=== Installing Pulumi v3.77.1 ===
+ Downloading https://github.com/pulumi/pulumi/releases/download/v3.77.1/pulumi-v3.77.1-linux-arm64.tar.gz...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  129M  100  129M    0     0  11.1M      0  0:00:11  0:00:11 --:--:-- 11.1M
+ Extracting to /home/ubuntu/.pulumi/bin
+ Adding $HOME/.pulumi/bin to $PATH in /home/ubuntu/.bashrc

=== Pulumi is now installed! 🍹 ===
+ Please restart your shell or add /home/ubuntu/.pulumi/bin to your $PATH
+ Get started with Pulumi: https://www.pulumi.com/docs/quickstart
```

The installer updates `$HOME/.bashrc` to setup the environment. Start a new shell or run the following command:

```bash
source $HOME/.bashrc
```

Confirm `pulumi` is now in the search path:

```bash { env_source="~/.bashrc" | "2"}
which pulumi
/home/ubuntu/.pulumi/bin/pulumi
```

Print the version:

```bash { env_source="~/.bashrc" | "2"}
pulumi version
v3.78.0
```

You are ready to use Pulumi on your Linux machine.

## Get started {#start}

Pulumi keeps your projects and state information in Pulumi Cloud, making it easy to access them from anywhere. If you want to use Pulumi Cloud visit [app.pulumi.com](https://app.pulumi.com/) and sign up.

It's not necessary to use Pulumi Cloud to get started, you can store project information on your local computer.

Below is a simple example to try out Pulumi.

The example demonstrates using Docker to pull a container image from Docker Hub to your local machine using Python.

To run the example, you need to install Docker. Refer to the [Docker install guide](/install-guides/docker/) for instructions.

You also need Python. Make sure you have `python` and `pip` installed.

For `Ubuntu 22.04` on Arm you can run the commands below to install:

```bash { env_source="~/.bashrc" }
sudo apt install python-is-python3 -y
sudo apt install python3-pip -y
```

Create a new directory for the example:

```bash { env_source="~/.bashrc" }
mkdir pulumi-test ; cd pulumi-test
```

Log in to your local machine, a shortcut to use `~/.pulumi` to store project data.

```bash { env_source="~/.bashrc" }
pulumi login --local
```

For the example you need to create 3 files:
- Python required package list in `requirements.txt`
- Pulumi project information in `Pulumi.yaml`
- Python code in `__main__.py`

Use a text editor to copy the code below to a file named `requirements.txt`.

```python
pulumi>=3.0.0
pulumi-docker>=4.0.0
```

Use a text editor to copy the lines below to a file named `Pulumi.yaml`

```yaml
name: alpine-pull
runtime: python
description: A pulumi application pull the alpine image
```

Use a text editor to copy the lines below to a file named `__main__.py`

```python
import pulumi
import pulumi_docker as docker

# Pull the latest Alpine image:
image = docker.RemoteImage("alpineImage", name="alpine:latest", keep_locally=True)

# Print the digest:
pulumi.export('digest', image.repo_digest)
```

With the three files created, install the required Python packages:

```bash { env_source="~/.bashrc" }
pip install -r requirements.txt
```

Run the Python script to pull the container image:

```bash { env_source="~/.bashrc" }
pulumi up
```

There are 4 prompts to respond to:

1. Confirm you want to create a new stack. (just hit return)

2. Enter a name for the stack.

3. When prompted, enter a passphrase for the stack (twice).

4. Answer `yes` to the final question to create the stack.

An example output for `pulumi up` is shown below:

```output
Please choose a stack, or create a new one:  [Use arrows to move, type to filterPlease choose a stack, or create a new one: <create a new stack>
Please enter your desired stack name: test1
Created stack 'test1'
Enter your passphrase to protect config/secrets:
Re-enter your passphrase to confirm:
Previewing update (test1):
     Type                         Name               Plan
 +   pulumi:pulumi:Stack          alpine-pull-test1  create
 +   └─ docker:index:RemoteImage  alpineImage        create


Outputs:
    digest: output<string>

Resources:
    + 2 to create

Do you want to perform this update? yes
Updating (test1):
     Type                         Name               Status
 +   pulumi:pulumi:Stack          alpine-pull-test1  created (0.07s)
 +   └─ docker:index:RemoteImage  alpineImage        created (0.03s)


Outputs:
    digest: "alpine@sha256:7144f7bab3d4c2648d7e59409f15ec52a18006a128c733fcff20d3a4a54ba44a"

Resources:
    + 2 created

Duration: 1s

```

After the Python script runs you have the container on your machine. Confirm this using the `docker images` command:

```console
docker images
```

The output will be similar to:

```output
REPOSITORY   TAG       IMAGE ID       CREATED      SIZE
alpine       latest    f6648c04cd6c   2 days ago   7.66MB
```

