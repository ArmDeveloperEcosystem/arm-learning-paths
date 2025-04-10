---
title: ROS - Robot Operating System
author: Odin Shen
minutes_to_complete: 30
official_docs: https://www.ros.org/blog/getting-started/

draft: true

test_images:
- ubuntu:latest
test_maintenance: true

additional_search_terms:
- linux

layout: installtoolsall
multi_install: false
multitool_install_part: false
tool_install: true
weight: 1
---

The Robot Operating System ([ROS](https://www.ros.org/)) is a set of software libraries and tools for building robot applications.
ROS 2 is the latest version, designed to enhance security, improve distributed system communication, and support real-time performance, addressing some of the limitations of ROS 1.

## Before you begin

ROS 2 is available for Ubuntu Linux 22.04, 24.04, and Windows.

This article provides a quick solution to install ROS 2 for Ubuntu on Arm. You can use Ubuntu 22.04 LTS or Ubuntu 24.04 LTS. 

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## What are the ROS 2 dependencies?

First, install the general dependencies:

```bash
sudo apt update
sudo apt install curl software-properties-common build-essential -y
```

## How do I Install ROS 2 for Ubuntu on Arm?

You can install ROS 2 using the APT package manager.

The Ubuntu package lists do not include ROS 2, so you need to add the repository. 

```bash
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
```

Install the ROS 2 dependencies:

```bash
sudo apt install -y \
        python3-pip \
        python3-rosdep \
        python3-colcon-common-extensions
```

There are two releases of ROS 2, Jazzy Jalisco and Humble Hawksbill, which you can install based on your Ubuntu version.

- For Ubuntu Linux 24.04, you should install Jazzy Jalisco.
- For Ubuntu Linux 22.04, you should install Humble Hawksbill.

## How can I install ROS 2?

Install ROS 2 based on your Ubuntu version:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu 24.04" language="bash">}}
    # Install ROS2 packages
    sudo apt install -y ros-jazzy-desktop
    # Initialize rosdep
    sudo rosdep init
    rosdep update
  {{< /tab >}}
  {{< tab header="Ubuntu 22.04" language="bash">}}
    # Install ROS2 packages
    sudo apt install -y ros-humble-desktop
    # Initialize rosdep
    sudo rosdep init
    rosdep update
  {{< /tab >}}
{{< /tabpane >}}

## How do I configure the environment?

Add ROS 2 setup to your shell startup script:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu 24.04" language="bash">}}
    echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
    source ~/.bashrc
  {{< /tab >}}
  {{< tab header="Ubuntu 22.04" language="bash">}}
    echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
    source ~/.bashrc
  {{< /tab >}}
{{< /tabpane >}}

Confirm ROS 2 is installed by using printenv:

```console
printenv ROS_DISTRO
```
The output should print either `jazzy` or `humble`, depending on your Ubuntu version.

## How can I test the ROS 2 installation? 

In one terminal run a `talker`:

```console
ros2 run demo_nodes_cpp talker
```

The output will continue to be similar to the one shown below, indicating that ROS 2 is publishing the “hello world” string along with a sequence number.

```output
[INFO] [1741389626.338343545] [talker]: Publishing: 'Hello World: 1'
[INFO] [1741389627.338329328] [talker]: Publishing: 'Hello World: 2'
[INFO] [1741389628.338317118] [talker]: Publishing: 'Hello World: 3'
[INFO] [1741389629.338322551] [talker]: Publishing: 'Hello World: 4'
[INFO] [1741389630.338318200] [talker]: Publishing: 'Hello World: 5'
[INFO] [1741389631.338334884] [talker]: Publishing: 'Hello World: 6'
[INFO] [1741389629.338322551] [talker]: Publishing: 'Hello World: 7'
[INFO] [1741389630.338318200] [talker]: Publishing: 'Hello World: 8'
[INFO] [1741389631.338334884] [talker]: Publishing: 'Hello World: 9'
...
```


Then, open another terminal and run the `listener`:

```console
ros2 run demo_nodes_cpp listener
```

If you see "I heard [Hello World: ]" in the second terminal as shown below, it means ROS 2 has been successfully installed.

```output
[INFO] [1741389927.137762134] [listener]: I heard: [Hello World: 1]
[INFO] [1741389928.125120177] [listener]: I heard: [Hello World: 2]
[INFO] [1741389929.125042010] [listener]: I heard: [Hello World: 3]
[INFO] [1741389930.125046472] [listener]: I heard: [Hello World: 4]
[INFO] [1741389931.125055785] [listener]: I heard: [Hello World: 5]
[INFO] [1741389932.125434760] [listener]: I heard: [Hello World: 6]
[INFO] [1741389933.125044887] [listener]: I heard: [Hello World: 7]
[INFO] [1741389934.125124370] [listener]: I heard: [Hello World: 8]
[INFO] [1741389935.125036222] [listener]: I heard: [Hello World: 9]
...
```

You are now ready to use ROS 2.

## Where can I learn more about ROS 2?

- Explore the [ROS 2 Tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)
- Learn about [ROS 2 Command Line Tools](https://docs.ros.org/en/jazzy/Concepts/About-Command-Line-Tools.html)
