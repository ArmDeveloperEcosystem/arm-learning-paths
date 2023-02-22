---
layout: learningpathall
title: Remote.It Packages
weight: 2
---

Remote.It provides four types of packages for [download](https://www.remote.it/download-list).

| Application type | Operating Systems               | Devices supported    |
| ---------------- | ------------------------------- | -------------------- |
| Desktop          | Windows, macOS, and Linux       | initiator and target |
| CLI              | Windows, macOS, and Linux       | initiator and target |
| Device package   | Linux, OpenWRT, and many others | target only          |
| Mobile           | Andoid, iOS                     | initiator (Android and iOS) and target (Android only)  |

Any software package marked as initiator can connect to other target devices. The target software packages can receive connections from other devices. Packages marked as both initiator and target can do both functions.

## Before you begin

You will need a second computer with SSH configured. This computer is called the target device. There are 3 software packages. The Device Package should not be installed on a device with the Remote.It CLI or Desktop since they are incompatible.

#### Device Package 

If the target device only needs to receive connections, you should install the device package. This is the smallest footprint package which is suitable for embedded devices with limited storage and resources. [Install Device Package](/learning-paths/cross-platform/remoteit/device-package)
This does not support Windows or MacOS devices. Install the CLI or Desktop Application for these systems.

#### CLI

If the device will need to initiate a connection to another Remote.It target device without a GUI (command line only), you should install the CLI on the device. This will also allow the device to be a target as well. [Install CLI](/learning-paths/cross-platform/remoteit/cli)

#### Desktop

If the device will need to initiate a connection to another Remote.It target device and you prefer a GUI (Graphical User Interface) that you can use from the display of your device, you should install the Desktop on the device. This will also allow the device to be a target as well. [Download the Remote.It Desktop Application](https://link.remote.it/download/desktop)



{{% notice %}}
You can access the Remote.It Dashboard with a browser [https://app.remote.it](https://app.remote.it) or the [Remote.It Desktop Application](https://link.remote.it/download/desktop) to set up and make connections.
{{% /notice %}}
