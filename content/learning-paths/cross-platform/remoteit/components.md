---
layout: learningpathall
title: Remote.It Packages
weight: 2
---
## What is Remote.It?

[Remote.It](https://www.remote.it/) removes the requirement for a global public IP address or port forwarding which is used by legacy VPN solutions. Enabling connections to devices that cannot be supported by VPNs such as devices connecting over CGNAT 5G mobile or Starlink satellite networks. Eliminating VPN hardware cost and license while removing time spent planning, maintaining, and debugging IP allow lists, IP addresses, subnet collisions, route tables, and VLAN tags. By removing the use of public IP addresses, your devices remain invisible to the public and eliminate external attack surfaces from bots and malicious actors."

`Remote.It` provides four types of packages for [download](https://www.remote.it/download-list).

| Application type | Operating Systems               | Devices supported    |
| ---------------- | ------------------------------- | -------------------- |
| Desktop          | Windows, macOS, and Linux       | initiator and target |
| CLI              | Windows, macOS, and Linux       | initiator and target |
| Device package   | Linux, OpenWRT, and many others | target only          |
| Mobile           | Android, iOS                    | initiator (Android and iOS) and target (Android only)  |

Any software package marked as `initiator` can connect to other `target` devices. The target software packages can receive connections from other devices. Packages marked as both initiator and target can do both functions.

## Before you begin

You will need a second computer with SSH configured. This computer is called the target device. There are 3 software packages. The Device Package should not be installed on a device with the Remote.It `CLI` or `Desktop` since they are incompatible.

#### Device Package 

If the target device only needs to receive connections, you should install the device package. This is the smallest footprint package which is suitable for embedded devices with limited storage and resources. [Install Device Package](/learning-paths/cross-platform/remoteit/device-package)
This does not support Windows or macOS devices. Install the CLI or Desktop Application for these systems.

#### CLI

If the device will need to initiate a connection to another Remote.It target device without a GUI (command line only), you should install the CLI on the device. This will also allow the device to be a target as well. [Install CLI](/learning-paths/cross-platform/remoteit/cli)

#### Desktop

If the device will need to initiate a connection to another Remote.It target device and you prefer a GUI (Graphical User Interface) that you can use from the display of your device, you should install the Desktop on the device. This will also allow the device to be a target as well. [Download the Remote.It Desktop Application](https://link.remote.it/download/desktop)


{{% notice %}}
You can access the Remote.It Dashboard with a browser [https://app.remote.it](https://app.remote.it) or the [Remote.It Desktop Application](https://link.remote.it/download/desktop) to set up and make connections.
{{% /notice %}}
