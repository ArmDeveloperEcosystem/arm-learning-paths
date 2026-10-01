---
title: Prepare the tools, device, and workload
description: Set up Streamline and an Android device, inspect useful Vulkan properties, and prepare your debuggable app for an NX capture.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Arm Performance Studio and open Streamline

Install the package for your host using the [Arm Performance Studio install guide](/install-guides/ams/). Open the Performance Studio Hub and launch Streamline. 

Confirm that you are using **Streamline 9.9 or newer**. On macOS, select **Streamline > About Streamline** to check the version. 

![About Streamline dialog showing version 9.9.0 over the Start view, with Android (adb) selected and no device selected#center](./images/streamline_startscreen.png "The About Streamline dialog confirms version 9.9.0. Use Streamline 9.9 or newer for ML for Vulkan workload profiling.")

Alternatively, nativate to the installation directory on Mac this is `/Applications/Arm Performance Studio 2026.5/streamline` and run the following command.

```bash
./Streamline-cli --version
```

You should the following output. 

```output
Streamline 9.9 (Build 9.9.0.v20260901_1940)
Copyright (c) 2010-2026 Arm Limited. All rights reserved
```


## Connect an Android device with ADB

Install the [Android SDK Platform Tools](https://developer.android.com/tools/releases/platform-tools) for your platform and add its directory to your host's `PATH`.

Enable **Developer options** on the Android device, typically by opening **Settings > About phone** and tapping **Build number** seven times. Then enable **USB debugging**, usually under **Settings > System > Developer options**. The exact labels and locations vary by manufacturer; see the [Android developer options guidance](https://developer.android.com/studio/debug/dev-options).

{{% notice For Xiaomi Devices %}}
You will also need to enable **Developer options > USB debugging (Security settings)** so Streamline can configure the Vulkan Timeline layer for Dispatch Graph profiling. Enabling this setting on the Xiaomi used here requires a **Xiaomi account and a SIM card**.

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

{{% notice Note%}}
If more than one device is listed, add `-s YOUR_DEVICE_SERIAL` after `adb` in each subsequent command.
{{% /notice %}}

In Streamline's **Start** view, select the **Android (adb)** radio button. Your connected device should appear under **Select device**. Select it to list its filtered debuggable applications.

Confirm the Perfetto service is running which is required for the Mali timeline view.

```bash
adb shell pidof traced || echo "Perfetto service not running"
```

If no process ID appears, try enabling the service, then repeat the check:

```bash
adb shell setprop persist.traced.enable 1
```

## Check GPU and Driver information

Mali NX profiling requires **Mali DDK r56p0 or later**. 

The GPU driver is supplied by the SoC manufacturer and shipped in the device manufacturer's software image. Application developers normally receive driver changes through device software updates. This walkthrough does not require a separate DDK release check: start by confirming that your app runs its intended workload on the device.

Run the followin command to dump the Vulkan properties and filter for the GPU and driver fields:

```bash
adb shell cmd gpu vkjson |
  grep -E '"(deviceName|driverName|driverInfo|driverVersion)"'
```

The Xiaomi 18 Fold used for this Learning Path returned the following values (repeated fields omitted):

```out
"driverInfo" : "v1.r56p0-15bet0.62068c9e2b6dab93feff4ddf773d9a12",
"driverName" : "Mali-G2-Ultra-NX MC16"
"deviceName" : "Mali-G2-Ultra-NX MC16",
"driverVersion" : 234881024.0,
```

If the command above does not identify your driver, use the Vulkan API to query [`VkPhysicalDeviceProperties::driverVersion`](https://docs.vulkan.org/refpages/latest/refpages/source/VkPhysicalDeviceProperties.html) and [`VkPhysicalDeviceDriverProperties::driverID`, `driverName`, and `driverInfo`](https://docs.vulkan.org/refpages/latest/refpages/source/VkPhysicalDeviceDriverProperties.html).

## Transfer application to device

Run these commands from your APK directory, replacing `YOUR_APP.apk` and `YOUR_PACKAGE` with your debuggable APK and package ID (for Moku, `station-arm64.apk` and `com.arm.station`). They install the app and check its APK path, debug access, and launch [activity](https://developer.android.com/guide/components/activities/intro-activities).

```bash
adb install -r YOUR_APP.apk
adb shell cmd package resolve-activity --brief YOUR_PACKAGE
```

The output from the final command should show the package and activity name which you can select for streamline capture through the GUI. 

```output
priority=0 preferredOrder=0 match=0x108000 specificIndex=-1 isDefault=false
com.arm.station/com.epicgames.unreal.GameActivity
```

After installation, your app will appear in the device launcher. The screenshot below shows its icon highlighted on the Xiaomi 18 Fold home screen, mirrored to the local machine using `scrcpy`.

![Xiaomi 18 Fold home screen mirrored in scrcpy, with the installed MOKU app icon outlined in green on the right#center](./images/installed_moku.png "The installed Moku app on the Xiaomi 18 Fold home screen. Select its highlighted icon to launch the workload.")

## Enable NX statistics collection

NX statistics supplement GPU timeline events with information about neural execution. For streamline capture, check and record the existing setting before changing it. If you will use the CLI sequence on the next page, let that sequence record and enable the setting instead:

```bash
adb shell getprop debug.mali.statistics_mode
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


{{% notice Note %}}
After profiling, you may want to reset NX statistics collection to the previous 'X' value:

```bash
adb shell setprop debug.mali.statistics_mode X
```
{{% /notice %}}

Finally, enable the Mali timeline layer.

```bash
adb shell setprop debug.vulkan.layers VK_LAYER_LGL_gpu_timeline
```

## What you've accomplished and what's next

You've connected the device and prepared your debuggable workload for NX statistics collection. You also know which Vulkan properties and features can help investigate compatibility.

Next, [capture Moku using the CLI or GUI](../capture-streamline-profile/).
