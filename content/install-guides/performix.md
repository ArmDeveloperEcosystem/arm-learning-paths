---
title: Arm Performix
description: Install Arm Performix on a desktop host and connect to remote Arm Linux targets for graphical performance profiling with hardware counters.

additional_search_terms:
  - performix
  - performance
  - profiling
  - analysis
  - neoverse
  - optimization
  - perf
  - top-down

minutes_to_complete: 30

author: Pareena Verma

### Link to official documentation
official_docs: https://developer.arm.com/documentation/110163/latest

weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

## What is Arm Performix?

Arm Performix is a desktop application that simplifies hardware-specific optimization by offering curated analysis pathways for performance-critical factors in applications, libraries, runtimes, and source code. Its capabilities include:

* Performance profiling using hardware performance monitoring counters
* Top-down methodology analysis for identifying performance bottlenecks
* System-wide and per-process profiling
* SSH-based remote target connections with optional support for jump nodes (also known as bastions)

## Which host and target platforms does Arm Performix support?

The Arm Performix desktop application supports the following host platforms:

* **Windows**: Windows 10 or later on Arm64 or x64 architecture
* **macOS**: macOS on Arm64 (Apple Silicon) or x64 architecture
* **Linux**: Debian-based distribution on Arm64 or x64 architecture

You also need a target system on which to profile your application or workload. The following target platforms are supported:

* **Linux with Arm64 architecture**: Full support for Amazon Linux 2023, Ubuntu 22.04, or Ubuntu 24.04
* **Windows with Arm64 architecture**: Partial support - Code Hotspots recipe only
* **Linux with x64 architecture**: Partial support - Code Hotspots recipe only

## How do I download and install Arm Performix?

Arm Performix is distributed as platform-specific installer packages.
The installation includes the GUI, the CLI tool (`apx`) and an MCP server.

### How do I install Arm Performix on Windows?

Download the Windows installer package for your architecture from the [Arm Performix download page](https://developer.arm.com/servers-and-cloud-computing/arm-performix).

Alternatively, download using PowerShell. These commands require PowerShell and do not work in the Windows Command Prompt (CMD):

{{< tabpane code=true >}}
{{< tab header="Arm64" >}}
curl -o ArmPerformix-windows-arm64.exe https://artifacts.tools.arm.com/arm-performix/app/latest/windows/arm64/ArmPerformix-windows-arm64.exe
{{< /tab >}}
{{< tab header="x64" >}}
curl -o ArmPerformix-windows-x64.exe https://artifacts.tools.arm.com/arm-performix/app/latest/windows/x64/ArmPerformix-windows-x64.exe
{{< /tab >}}
{{< /tabpane >}}

After downloading the `.exe` file, locate it in your Downloads folder and double-click it to start the installation wizard.

Review the License Agreement and select **I Agree**.

Choose whether to install Arm Performix for all users or just yourself, then select **Next**.

If you choose **Anyone who uses this computer (all users)**, a User Access Control dialog opens. Enter an administrator username and password, then select **Yes**.

Choose the installation directory. You can accept the default or select **Browse** to choose a different location.

Select **Install**.

When the installation finishes, select **Finish** to close the wizard.

### How do I install Arm Performix on Linux?

Download the Linux installer package for your architecture from the [Arm Performix download page](https://developer.arm.com/servers-and-cloud-computing/arm-performix).

Alternatively, download using `wget`:

{{< tabpane code=true >}}
{{< tab header="Arm64" >}}
wget -P $HOME https://artifacts.tools.arm.com/arm-performix/app/latest/linux/arm64/ArmPerformix-linux-arm64.deb
{{< /tab >}}
{{< tab header="x64" >}}
wget -P $HOME https://artifacts.tools.arm.com/arm-performix/app/latest/linux/x64/ArmPerformix-linux-amd64.deb
{{< /tab >}}
{{< /tabpane >}}

After downloading the `.deb` file, navigate to the directory where you downloaded it:

```bash
cd $HOME
```

Update the package list:

```bash
sudo apt update
```

Install the package:

{{< tabpane code=true >}}
{{< tab header="Arm64" >}}
sudo dpkg -i ArmPerformix-linux-arm64.deb
{{< /tab >}}
{{< tab header="x64" >}}
sudo dpkg -i ArmPerformix-linux-amd64.deb
{{< /tab >}}
{{< /tabpane >}}

The `dpkg` command may report missing dependency errors. Run the following command to automatically fetch and install any missing dependencies:

```bash
sudo apt-get install -f
```

Navigate to the Arm Performix installation directory:

```bash
cd "/opt/Arm Performix/assets/apx/"
```

Verify the installation by checking the version:

```bash
./apx version
```

The output shows the installed version number:

```output
Daemon process started; to stop call `apx daemon stop`.
Arm Performix CLI version: 1.0.0
Arm Performix daemon version: 1.0.0
```

### How do I install Arm Performix on macOS?

Download the macOS installer package for your architecture from the [Arm Performix download page](https://developer.arm.com/servers-and-cloud-computing/arm-performix).

Alternatively, download using `curl`:

{{< tabpane code=true >}}
{{< tab header="Arm64" >}}
curl -Lo ArmPerformix-darwin-arm64.pkg https://artifacts.tools.arm.com/arm-performix/app/latest/darwin/arm64/ArmPerformix-darwin-arm64.pkg
{{< /tab >}}
{{< tab header="x64" >}}
curl -Lo ArmPerformix-darwin-arm64.pkg https://artifacts.tools.arm.com/arm-performix/app/latest/darwin/x64/ArmPerformix-darwin-x64.pkg
{{< /tab >}}
{{< /tabpane >}}

After downloading the `.pkg` file, navigate to the directory where you downloaded it and double-click the file to start the installer.

Review the license agreement and select **Agree**.

Choose the installation destination. By default, Arm Performix installs on your system drive.

Select **Install** and enter your macOS administrator password when prompted.

Wait while the installer copies the files.

When the installation finishes, select **Close** to exit the installer.

## What comes next after installing Arm Performix?

After completing these installation steps, you can simply launch the GUI or CLI to get started.

For further guidance on using Arm Performix, including connecting to your target for the first time or setting up the MCP server to use Arm Performix with an AI agent, please refer to the [Arm Performix User Guide](https://developer.arm.com/documentation/110163/latest/).

## How do I uninstall Arm Performix?

To remove Arm Performix from your system, use the appropriate method for your platform:

* For Windows, open **Settings** > **Apps**, find **Arm Performix**, and select **Uninstall**.
* For macOS, drag the Arm Performix application from **Applications** to the **Trash**.
* For Linux, remove the package:

```bash
sudo apt remove arm-performix
```
