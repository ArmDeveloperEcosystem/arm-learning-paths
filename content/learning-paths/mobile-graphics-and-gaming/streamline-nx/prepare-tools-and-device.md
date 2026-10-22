---
title: Prepare the tools, device, and workload
description: Set up Streamline and an Android device, inspect useful Vulkan properties, and prepare your debuggable app for an NX capture.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Arm Performance Studio and open Streamline

Install the package for your host using the [Arm Performance Studio install guide](/install-guides/ams/). Open the Performance Studio Hub and launch Streamline.

Confirm that you are using **Streamline 9.9 or newer**. On macOS, select **Streamline > About Streamline** to check the version. An older installation can support general GPU profiling without supporting this NX workflow.

![About Streamline dialog showing version 9.9.0 over the Start view, with Android (adb) selected and no device selected#center](./images/streamline_startscreen.png "The About Streamline dialog confirms version 9.9.0. Use Streamline 9.9 or newer for ML for Vulkan workload profiling.")

## Connect an Android device with ADB

Install the [Android SDK Platform Tools](https://developer.android.com/tools/releases/platform-tools) for your platform and add its directory to your host's `PATH`.

Enable **Developer options** on the Android device, typically by opening **Settings > About phone** and tapping **Build number** seven times. Then enable **USB debugging**, usually under **Settings > System > Developer options**. The exact labels and locations vary by manufacturer; see the [Android developer options guidance](https://developer.android.com/studio/debug/dev-options).

Connect the device with a USB data cable, unlock it, and accept the debugging authorization prompt.

{{% notice Xiaomi devices %}}
On the Xiaomi used here, **Developer options > USB debugging (Security settings)** must also be enabled so Streamline can configure the Vulkan Timeline layer for Dispatch Graph profiling.

![Xiaomi Developer options with USB debugging (Security settings) enabled, allowing permission grants and simulated input through ADB#center](./images/xiaomi_additional_permission.png "Enable the additional debugging permissions for Vulkan Timeline layer setup.")
{{% /notice %}}

In a terminal, check the host tool and device connection:

```bash
adb devices -l
```

You should see a device serial number and product details for each attached device. A wireless ADB connection uses `<IP address>:<port number>` instead of a USB serial number.

```out
List of devices attached
10.72.66.137:33735     device product:lhasa model:2608BPX34C device:lhasa transport_id:3
```

Your selected device must appear with status `device`. If it is `unauthorized`, accept the prompt.

{{% notice Note %}}
If more than one device is listed, add `-s YOUR_DEVICE_SERIAL` after `adb` in each subsequent command.
{{% /notice %}}

In Streamline's **Start** view, select the **Android (adb)** radio button. Your connected device should appear under **Select device**. Select it to list its filtered debuggable applications.

Confirm that the Perfetto service is running. It is required for Mali Timeline events and is separate from USB debugging authorization:

```bash
adb shell pidof traced || echo "Perfetto service not running"
```

The expected output is a process ID. If no process ID appears, first record the current setting:

```bash
adb shell getprop persist.traced.enable
```

Then try enabling the service and repeat the process check:

```bash
adb shell setprop persist.traced.enable 1
adb shell pidof traced
```

Do not continue without a running service. If it cannot be enabled, consult the [Streamline Android target setup guide](https://support.arm.com/documentation/101813/9-9). If you changed this persistent setting, restore its recorded value after profiling.

## Check GPU and driver information

For a brief check against the hardware and driver prerequisites, dump the Vulkan properties and filter for the GPU and driver fields. Run this example in a Bash-compatible host terminal:

```bash
adb shell cmd gpu vkjson |
  grep -E '"(deviceName|driverName|driverInfo|driverVersion)"'
```

The Xiaomi 18 Fold used for this Learning Path returned the following values (repeated fields omitted):

```output
"driverInfo" : "v1.r56p0-15bet0.62068c9e2b6dab93feff4ddf773d9a12",
"driverName" : "Mali-G2-Ultra-NX MC16"
"deviceName" : "Mali-G2-Ultra-NX MC16",
"driverVersion" : 234881024.0,
```

## Confirm your installed workload

An installed, debuggable application is a prerequisite; this Learning Path does not build or supply an APK. Replace `YOUR_PACKAGE` with your application's package ID. Check debug access and resolve its launch [activity](https://developer.android.com/guide/components/activities/intro-activities):

```bash
adb shell run-as YOUR_PACKAGE id
adb shell cmd package resolve-activity --brief YOUR_PACKAGE
```

The first command should print the application's UID and group information. If it reports that the package is not debuggable, obtain a debuggable build before continuing. The final command should return the package/activity component to select in Streamline. For example, Moku returns:

```output
com.arm.station/com.epicgames.unreal.GameActivity
```

Unlock the device and launch your own app once. Confirm that its intended ML workload runs, and note any navigation or application-specific arguments required to reach it. Streamline can launch the app again when capture starts.

The screenshot below illustrates an installed app using Moku; use your own application's launcher icon.

![Xiaomi 18 Fold home screen mirrored in scrcpy, with the example MOKU app icon outlined in green on the right#center](./images/installed_moku.png "Moku is the example installed app; launch your own debuggable application to verify its workload.")

## Enable NX statistics collection

NX statistics supplement GPU timeline events with information about neural execution. Record the existing setting, including whether the output is blank, before changing it:

```bash
adb shell getprop debug.mali.statistics_mode
```

Then enable per-unit statistics and verify the new setting:

```bash
adb shell setprop debug.mali.statistics_mode 2
adb shell getprop debug.mali.statistics_mode
```

The final query should return `2`. This property configures statistics collection; it does not identify the DDK. If the property cannot be set, stop here and consult the device's profiling setup documentation rather than assuming statistics are enabled.

The modes described in the [Streamline ML workload setup guide](https://support.arm.com/documentation/101816/9-9/Getting-started-with-Streamline/Configure-your-system-to-profile-ML-for-Vulkan-workloads) are:

| Mode | Collected data |
| --- | --- |
| `0` | NX statistics disabled |
| `1` | Per-section cycle counts |
| `2` | Per-unit counters; the documented default |


The GUI capture on the next page automatically deploys and enables the Mali Timeline layer. You do not need to set `debug.vulkan.layers` manually for this workflow. After analysis, [restore any settings you changed](../analyze-neural-workloads/#restore-device-settings) to their recorded values rather than unconditionally disabling statistics.

## What you've accomplished and what's next

You've connected the device, checked Perfetto, and prepared your own debuggable workload for NX statistics collection.

Next, [capture your workload using the Streamline GUI](../capture-streamline-profile/).
