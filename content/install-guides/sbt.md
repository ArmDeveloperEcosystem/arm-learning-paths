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

[`sbt`](https://www.scala-sbt.org/) is a popular build tool for Scala and Java projects.

`sbt` supports the Arm architecture is available for Windows, macOS, and Linux.

{{% notice Note %}}
When the project was created, it was called *Simple Build Tool*, but quickly evolved to *sbt*. Some have incorrectly redefined it to *Scala Build Tool*, which does not reflect the fact that sbt works with Java-only projects. 

It is now called *sbt* in all lowercase letters, which emphasizes the fact that it is not an acronym.{{% /notice %}}

## What should I consider before installing sbt on Arm?

Before installing `sbt`, ensure you have Java installed on your system as `sbt` requires Java to run.

See the [Java install guide](/install-guides/java/) for more information.

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

You can install `sbt` using the Ubuntu package manager. 

First, you need to add the `sbt` repository:

```bash
sudo apt-get update
sudo apt-get install apt-transport-https curl -y
echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x99E82A75642AC823" | sudo apt-key add
```

Next, install `sbt`:

```bash
sudo apt-get update
sudo apt-get install sbt -y
```

Run the `sbt` version command to confirm the `sbt` and Java installation:

```bash
sbt --version
```

The version command also confirms you have a working Java setup. 

The version is printed and looks similar to:

```output
sbt version in this project: 1.10.7
sbt script version: 1.10.7
```

You are now ready to use `sbt`.
