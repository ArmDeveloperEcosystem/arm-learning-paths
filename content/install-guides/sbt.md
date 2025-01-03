---
title: sbt

author_primary: Jason Andrews
minutes_to_complete: 10

additional_search_terms:
- Scala
- Java

layout: installtoolsall
multi_install: false
multitool_install_part: false
official_docs: https://www.scala-sbt.org/download.html
test_images:
- ubuntu:latest
test_link: null
test_maintenance: false
tool_install: true
weight: 1
---

[sbt](https://www.scala-sbt.org/) is a popular build tool for Scala and Java projects.

sbt is available for Windows, macOS, Linux and supports the Arm architecture.

## What should I consider before installing sbt on Arm?

Before installing sbt, ensure you have Java installed on your system as sbt requires Java to run.

Check the [Java install guide](/install-guides/java/) for more information.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:
```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## How do I install sbt for Ubuntu on Arm?

sbt can be installed using the Ubuntu package manager. 

First, you will need to add the sbt repository:

```bash
sudo apt-get update
sudo apt-get install apt-transport-https curl -y
echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x99E82A75642AC823" | sudo apt-key add
```

Next, install sbt:

```bash
sudo apt-get update
sudo apt-get install sbt -y
```

Confirm the sbt and Java installation by running the sbt version command:

```bash
sbt --version
```

The version command also confirms you have a working Java. 

The version is printed and looks similar to:

```output
sbt version in this project: 1.10.7
sbt script version: 1.10.7
```

You are ready to use sbt.
