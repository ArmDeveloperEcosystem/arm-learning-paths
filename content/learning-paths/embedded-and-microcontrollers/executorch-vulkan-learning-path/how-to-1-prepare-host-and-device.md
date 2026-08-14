---
title: Prepare the host and device
description: Install the Android toolchain, configure ADB access, and verify Vulkan support on the target phone.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Android SDK and NDK

Use Android Studio or the SDK Manager to install the following components:

- Android SDK Platform-Tools
- Android SDK Command-line Tools
- CMake
- NDK (Side by side)

This workflow used Android NDK `r28c`:

```text
28.2.13676358
```

Typical locations:

```text
$HOME/Android/Sdk
$HOME/Android/Sdk/ndk/28.2.13676358
```

Validate the NDK layout:

```bash
ls "$HOME/Android/Sdk/ndk/28.2.13676358"
test -f "$HOME/Android/Sdk/ndk/28.2.13676358/NOTICE" && echo "NDK OK"
test -f "$HOME/Android/Sdk/ndk/28.2.13676358/build/cmake/android.toolchain.cmake" && echo "Toolchain OK"
```

## Persist Android environment variables

Add the SDK and NDK paths to your shell startup file:

```bash
cat >> ~/.bashrc <<'EOF'
# Android SDK / NDK
export ANDROID_HOME="$HOME/Android/Sdk"
export ANDROID_NDK="$ANDROID_HOME/ndk/28.2.13676358"
export PATH="$ANDROID_HOME/platform-tools:$PATH"
export PATH="$ANDROID_HOME/cmdline-tools/latest/bin:$PATH"
EOF

source ~/.bashrc
```

Verify the configuration:

```bash
echo "$ANDROID_HOME"
echo "$ANDROID_NDK"
adb --version
test -f "$ANDROID_NDK/NOTICE" && echo "NDK OK"
test -f "$ANDROID_NDK/build/cmake/android.toolchain.cmake" && echo "Toolchain OK"
```

## Connect the Vivo over ADB

If `adb devices` shows `no permissions`, add the user to `plugdev`, install the generic Android udev helpers, and reload the rules:

```bash
sudo usermod -aG plugdev "$USER"
sudo apt install -y android-sdk-platform-tools-common
sudo udevadm control --reload-rules
sudo udevadm trigger
newgrp plugdev
```

The tested device reported this USB ID:

```text
Bus 002 Device 002: ID 2d95:6001 vivo vivo X300 Pro
```

Add a Vivo-specific rule if the default rules are not enough:

```bash
sudo tee /etc/udev/rules.d/51-vivo-android.rules >/dev/null <<'EOF'
SUBSYSTEM=="usb", ATTR{idVendor}=="2d95", MODE="0660", GROUP="plugdev", TAG+="uaccess"
EOF

sudo chmod 644 /etc/udev/rules.d/51-vivo-android.rules
sudo udevadm control --reload-rules
sudo udevadm trigger
```

Then restart ADB and accept the RSA prompt on the phone:

```bash
adb kill-server
adb start-server
adb devices
```

Expected final state:

```text
10AFB40J6Q0031C    device
```

## Verify Vulkan support on the phone

Check the Vulkan implementation:

```bash
adb shell getprop ro.hardware.vulkan
```

The measured device returned:

```text
mali
```

Then verify the relevant Android features:

```bash
adb shell pm list features | grep -i vulkan
```

Expected features include:

```text
feature:android.hardware.vulkan.compute
feature:android.hardware.vulkan.level=1
feature:android.hardware.vulkan.version=4206592
feature:android.software.vulkan.deqp.level=132711169
```

`vulkan_renderengine: false` from SurfaceFlinger does not block application-side Vulkan compute. The more important signal is that the device advertises `android.hardware.vulkan.compute`.
