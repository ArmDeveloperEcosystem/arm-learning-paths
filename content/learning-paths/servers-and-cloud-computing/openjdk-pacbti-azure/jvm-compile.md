---
title: Compile OpenJDK from source
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install build prerequisites

Install these prerequisites in a terminal on your Cobalt 100 VM. Also install a bootstrap JVM to build the PAC/BTI-enabled JVM:

```bash
sudo apt update
sudo apt install -y zip git build-essential wget curl autoconf 
sudo apt install -y libcups2-dev libasound2-dev libfontconfig1-dev alsa-ucm-conf ubuntu-drivers-common 
sudo apt install -y libx11-dev libxext-dev libxrender-dev libxrandr-dev libxtst-dev libxt-dev
sudo apt install -y openjdk-25-jdk
```

## Download the OpenJDK source

Download OpenJDK. Since the bootstrap JVM is v25, build v26 with PAC/BTI support enabled:

```bash
cd $HOME
git clone https://github.com/openjdk/jdk
cd jdk
git checkout jdk-26+35
```

## Configure the OpenJDK source build

Configure the OpenJDK source build and enable branch protection support:

```bash
bash configure --enable-branch-protection 
```

## Build the JVM

Run the build to create the JVM. This process can take more than 30 minutes:

```bash
make images
```

## Register the JVM with the system

Run the following commands to register the newly created JDK/JVM with the system:

```bash
cd $HOME/jdk
WD=$(pwd)/build/linux-aarch64-server-release
cd /usr/lib/jvm
sudo ln -s ${WD}/jdk ./java-26-openjdk-arm64
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-26-openjdk-arm64/bin/java 3000
cd
```

Confirm the newly installed JVM:

```bash
java --version
```

Output should be similar to:

```output
openjdk 26-internal 2026-03-17
OpenJDK Runtime Environment (build 26-internal-adhoc.ubuntu.jdk)
OpenJDK 64-Bit Server VM (build 26-internal-adhoc.ubuntu.jdk, mixed mode)
```

## What you've learned and what's next

You've compiled OpenJDK from source with branch protection enabled, registered the resulting JVM with the system, and confirmed the installation with `java --version`.

Next, you'll run a test script to verify that PAC/BTI is active in the JVM you just built.
