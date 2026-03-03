---
hide_from_navpane: true

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up a Qualcomm Dragonwing QC6490 with Ubuntu

The Qualcomm Dragonwing QC6490 is an Arm-based platform that supports both the on-board Qualcomm camera module and USB-attached cameras for live inference with Edge Impulse. This section covers prerequisites, dependency installation, and the component configuration for running the Edge Impulse Runner on a QC6490 device with AWS IoT Greengrass.

### Prerequisites

Before you begin, make sure you have:

- A Qualcomm Dragonwing QC6490 development board with a power supply.
- Ubuntu flashed onto the device per the [Qualcomm QC6490 quick start guide](https://docs.qualcomm.com/doc/80-90441-1/topic/qsg-landing-page.html).
- A network connection (Ethernet or Wi-Fi) and SSH access to the device.
- Optional: the on-board Qualcomm camera module or a USB camera for live inference. Without a camera, the Runner uses a sample video file instead.

### Connect over SSH

Connect to the QC6490 from your computer. Replace the placeholder with the device's IP address:

```bash
ssh your-username@<your-qc6490-ip-address>
```

If you're not sure of the IP address, check your router's admin page for connected devices, or run `hostname -I` on the QC6490 if you have a monitor connected.

### Verify Ubuntu is running

Confirm the device is running Ubuntu on aarch64:

```bash
uname -a
```

The output should show `aarch64` as the architecture and an Ubuntu kernel version.

### Install dependencies

Update the package list and install the build tools, Node.js, and GStreamer plugins that the Edge Impulse Runner requires:

```bash
sudo apt update
sudo apt install -y curl unzip
sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
```

Greengrass Nucleus Classic is Java-based, so you also need a JDK:

```bash
sudo apt install -y default-jdk
```

Install any available security updates:

```bash
sudo apt upgrade -y
```

### Verify the camera (optional)

The QC6490 supports two types of cameras. The type you have determines which JSON configuration to use later.

**On-board Qualcomm camera**: This uses the `qtiqmmfsrc` GStreamer element, which is specific to Qualcomm platforms. If your board has a built-in camera module, it should be available without additional setup.

**USB-attached camera**: If you're using a USB camera instead, confirm the system detects it:

```bash
ls /dev/video*
```

You should see at least `/dev/video0` in the output. If nothing appears, check that the camera is plugged in securely and try a different USB port.

### Save the component configuration

The JSON configurations below set up the Edge Impulse Greengrass component for the QC6490. This platform has three configuration options depending on your camera setup. Choose the one that matches your hardware and save it to a text file on your local machine. You'll paste it into the Greengrass deployment configuration in a later step.

#### With the on-board Qualcomm camera

This configuration uses the `qtiqmmfsrc` GStreamer element to capture video from the on-board camera at 1280x720 resolution. The `--force-variant float32` flag selects the float32 model variant, and `--silent` suppresses console output since the Runner runs as a background service.

```json
{
   "Parameters": {
      "node_version": "20.18.2",
      "vips_version": "8.12.1",
      "device_name": "MyQC6490UbuntuEdgeDevice",
      "launch": "runner",
      "sleep_time_sec": 10,
      "lock_filename": "/tmp/ei_lockfile_runner",
      "gst_args": "qtiqmmfsrc:name=camsrc:camera=0:!:video/x-raw,width=1280,height=720:!:videoconvert:!:jpegenc",
      "eiparams": "--greengrass --force-variant float32 --silent",
      "iotcore_backoff": "-1",
      "iotcore_qos": "1",
      "ei_bindir": "/usr/local/bin",
      "ei_sm_secret_id": "EI_API_KEY",
      "ei_sm_secret_name": "ei_api_key",
      "ei_poll_sleeptime_ms": 2500,
      "ei_local_model_file": "__none__",
      "ei_shutdown_behavior": "__none__",
      "ei_ggc_user_groups": "video audio input users",
      "install_kvssink": "no",
      "publish_inference_base64_image": "no",
      "enable_cache_to_file": "no",
      "cache_file_directory": "__none__",
      "enable_threshold_limit": "no",
      "metrics_sleeptime_ms": 30000,
      "default_threshold": 65.0,
      "threshold_criteria": "ge",
      "enable_cache_to_s3": "no",
      "s3_bucket": "__none__"
   }
}
```

#### With a USB-attached camera

This configuration uses the standard `v4l2src` GStreamer element to capture video from a USB camera at 640x480 resolution. Use this if your QC6490 board doesn't have a built-in camera module, or if you prefer to use an external USB camera.

```json
{
   "Parameters": {
      "node_version": "20.18.2",
      "vips_version": "8.12.1",
      "device_name": "MyQC6490UbuntuEdgeDevice",
      "launch": "runner",
      "sleep_time_sec": 10,
      "lock_filename": "/tmp/ei_lockfile_runner",
      "gst_args": "v4l2src:device=/dev/video0:!:video/x-raw,width=640,height=480:!:videoconvert:!:jpegenc",
      "eiparams": "--greengrass --force-variant float32 --silent",
      "iotcore_backoff": "-1",
      "iotcore_qos": "1",
      "ei_bindir": "/usr/local/bin",
      "ei_sm_secret_id": "EI_API_KEY",
      "ei_sm_secret_name": "ei_api_key",
      "ei_poll_sleeptime_ms": 2500,
      "ei_local_model_file": "__none__",
      "ei_shutdown_behavior": "__none__",
      "ei_ggc_user_groups": "video audio input users",
      "install_kvssink": "no",
      "publish_inference_base64_image": "no",
      "enable_cache_to_file": "no",
      "cache_file_directory": "__none__",
      "enable_threshold_limit": "no",
      "metrics_sleeptime_ms": 30000,
      "default_threshold": 65.0,
      "threshold_criteria": "ge",
      "enable_cache_to_s3": "no",
      "s3_bucket": "__none__"
   }
}
```

#### Without a camera

This configuration reads inference input from a local sample video file. The `ei_local_model_file` field points to a pre-downloaded model, and `ei_shutdown_behavior` is set to `wait_on_restart` so the Runner pauses after the video ends and waits for a restart command.

```json
{
   "Parameters": {
      "node_version": "20.18.2",
      "vips_version": "8.12.1",
      "device_name": "MyQC6490UbuntuEdgeDevice",
      "launch": "runner",
      "sleep_time_sec": 10,
      "lock_filename": "/tmp/ei_lockfile_runner",
      "gst_args": "filesrc:location=/home/ggc_user/data/testSample.mp4:!:decodebin:!:videoconvert:!:videorate:!:video/x-raw,framerate=2200/1:!:jpegenc",
      "eiparams": "--greengrass",
      "iotcore_backoff": "-1",
      "iotcore_qos": "1",
      "ei_bindir": "/usr/local/bin",
      "ei_sm_secret_id": "EI_API_KEY",
      "ei_sm_secret_name": "ei_api_key",
      "ei_poll_sleeptime_ms": 2500,
      "ei_local_model_file": "/home/ggc_user/data/currentModel.eim",
      "ei_shutdown_behavior": "wait_on_restart",
      "ei_ggc_user_groups": "video audio input users system",
      "install_kvssink": "no",
      "publish_inference_base64_image": "no",
      "enable_cache_to_file": "no",
      "cache_file_directory": "__none__",
      "enable_threshold_limit": "no",
      "metrics_sleeptime_ms": 30000,
      "default_threshold": 50,
      "threshold_criteria": "ge",
      "enable_cache_to_s3": "no",
      "s3_bucket": "__none__"
   }
}
```

Your Qualcomm Dragonwing QC6490 is ready. Return to the [hardware setup page](/learning-paths/embedded-and-microcontrollers/edge_impulse_greengrass/hardwaresetup/) and continue to the next section to set up your Edge Impulse project.