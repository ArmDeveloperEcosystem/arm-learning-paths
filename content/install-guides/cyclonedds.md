---
title: Cyclone DDS
author: Odin Shen
minutes_to_complete: 20
official_docs: https://cyclonedds.io/

draft: true

additional_search_terms:
- linux
- automotive

test_images:
- ubuntu:latest
test_maintenance: true

layout: installtoolsall
multi_install: false
multitool_install_part: false
tool_install: true
weight: 1
---

The [Eclipse Cyclone DDS](https://cyclonedds.io/) is an open-source implementation of the Data Distribution Service ([DDS](https://en.wikipedia.org/wiki/Data_Distribution_Service)) standard, designed for high-performance, real-time, and scalable communication in autonomous systems, robotics, industrial IoT, and aerospace applications.

It is part of the Eclipse Foundation and is widely used in Robotic Operating System (ROS) 2 as a key middleware framework for inter-process communication.

## Before you begin

This article provides a quick solution to install Cyclone DDS on Arm Linux.

Confirm you are using an Arm Linux machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

You need to install the following before building Cyclone DDS:

- C and C++ compilers (GCC)
- Git
- CMake 
- OpenSSL

For Ubuntu Linux run the commands below. For other Linux distributions, use the package manager to install the above software.

```bash
sudo apt update
sudo apt install -y gcc g++ git cmake libssl-dev
```

## How do I build Cyclone DDS?

You can install Cyclone DDS by building the source code.

Clone the GitHub repository to create a build folder.

```bash
cd $HOME
git clone https://github.com/eclipse-cyclonedds/cyclonedds.git
```

Once downloaded, you can build and install Cyclone DDS.

Enable `BUILD_EXAMPLES` and `BUILD_TESTING` so you can run the examples to verify the installation. 

Here are the build and install commands:

```console
cd cyclonedds
mkdir build ; cd build
cmake -DBUILD_EXAMPLES=ON -DBUILD_TESTING=ON ..
cmake --build .
sudo cmake --build . --target install
```

Cyclone DDS is now installed in `/usr/local`

{{% notice Note %}}
If you don't want to install Cyclone DDS in the default location of `/usr/local` you can specify another location 
by adding `-DCMAKE_INSTALL_PREFIX=<install-prefix>` to the first `cmake` command with your alternate location.
{{% /notice %}}

## How can I test Cyclone DDS?

To verify the installation, you can run the Hello World example from the build directory.

Open two terminals and navigate to the `bin/` directory in each. 

Run the commands shown below in each tab in each of your two terminals:

{{< tabpane code=true >}}
  {{< tab header="Publisher" language="bash">}}
    cd $HOME/cyclonedds/build/bin/
    ./HelloworldPublisher
  {{< /tab >}}
  {{< tab header="Subscriber" language="bash">}}
    cd $HOME/cyclonedds/build/bin/
    ./HelloworldSubscriber
  {{< /tab >}}
{{< /tabpane >}}

If you observe the following output from each of terminal, Cyclone DDS is running correctly on your Arm Linux machine.

{{< tabpane code=true >}}
  {{< tab header="Publisher" language="log">}}
    === [Publisher]  Waiting for a reader to be discovered ...
    === [Publisher]  Writing : Message (1, Hello World)
  {{< /tab >}}
  {{< tab header="Subscriber" language="log">}}
    === [Subscriber] Waiting for a sample ...
    === [Subscriber] Received : Message (1, Hello World)
  {{< /tab >}}
{{< /tabpane >}}

You are now ready to use Cyclone DDS. 