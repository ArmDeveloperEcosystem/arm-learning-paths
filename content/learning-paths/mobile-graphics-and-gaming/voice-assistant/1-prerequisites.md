---
title: Set up your environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install dependencies

In this Learning Path, you'll compile and run an Android Voice Assistant application. 

Begin by installing the latest version of [Android Studio](https://developer.android.com/studio) on your development machine.

Next, install the following command-line tools:
- `cmake`; a cross-platform build system.
- `git`; a version control system that you use to clone the Voice Assistant codebase.
- `adb`; Android Debug Bridge, used to communicate with and control Android devices.

Install these tools with the appropriate command for your OS:

{{< tabpane code=true >}}
  {{< tab header="Linux/Ubuntu" language="bash">}}
sudo apt update
sudo apt install git adb cmake -y
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
brew install git android-platform-tools cmake
  {{< /tab >}}
{{< /tabpane >}}
