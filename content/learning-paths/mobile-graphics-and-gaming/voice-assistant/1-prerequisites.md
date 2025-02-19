---
title: Prerequisites
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install software required for this Learning Path

In this learning path, you will compile an Android application, so you first need to download and install the latest version of [Android Studio](https://developer.android.com/studio) on your computer.

You then need to ensure you have the following tools:
- `cmake`, the software build system
- `git`, the version control system for cloning the Voice Assistant codebase
- `adb`, the Android Debug Bridge, a command-line tool to communicate with a device and perform various commands on it

These tools can be installed by running the following command (depending on your machine's OS):

{{< tabpane code=true >}}
  {{< tab header="Linux/Ubuntu" language="bash">}}
sudo apt install git adb cmake
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
brew install git android-platform-tools cmake
  {{< /tab >}}
{{< /tabpane >}}