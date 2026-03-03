---
hide_from_navpane: true

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up an Nvidia Jetson with Jetpack

Nvidia Jetson boards (Nano, Xavier, Orin) provide GPU-accelerated inference for Edge Impulse models. This section covers prerequisites, dependency installation, and the component configuration for running the Edge Impulse Runner on a Jetson device with AWS IoT Greengrass.

### Prerequisites

Before you begin, make sure you have:

- An Nvidia Jetson board with a power supply.
- Jetpack 5.x or 6.0 already flashed onto the device. If you haven't done this yet, follow the [Nvidia Jetson flashing instructions](https://docs.nvidia.com/jetson/archives/r34.1/DeveloperGuide/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/flashing.html).
- A network connection (Ethernet or Wi-Fi) and SSH access to the device.
- Optional: a USB camera for live inference. Without a camera, the Runner uses a sample video file instead.

### Verify Jetpack version

After booting the Jetson, confirm which Jetpack version is installed:

```bash
cat /etc/nv_tegra_release
```

You should see output that indicates L4T (Linux for Tegra) version 34.x or later for Jetpack 5.x, or version 36.x for Jetpack 6.0.

### Connect over SSH

If you haven't already, connect to the Jetson from your computer. Replace the placeholder with the device's IP address:

```bash
ssh your-username@<your-jetson-ip-address>
```

If you're not sure of the IP address, you can check your router's admin page for connected devices, or run `hostname -I` on the Jetson if you have a monitor connected.

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

If you have a USB camera connected, confirm the system detects it:

```bash
ls /dev/video*
```

You should see at least `/dev/video0` in the output. If nothing appears, check that the camera is plugged in securely and try a different USB port.

### Jetpack 6.x note on GPU access

If your device is running Jetpack 6.x or later, the `render` group is required for the Greengrass service user to access the GPU. Both JSON configurations below already include `render` in the `ei_ggc_user_groups` field. If you're running Jetpack 5.x, you can remove `render` from that field, though leaving it in place doesn't cause issues.

### Save the component configuration

The JSON configurations below set up the Edge Impulse Greengrass component for the Jetson. Choose the configuration that matches your setup and save it to a text file on your local machine. You'll paste it into the Greengrass deployment configuration in a later step.

#### With a USB camera

This configuration captures live video from `/dev/video0` at 640x480 resolution. The `--force-variant float32` flag selects the float32 model variant, and `--silent` suppresses console output since the Runner runs as a background service.

```json
{
   "Parameters": {
      "node_version": "20.18.2",
      "vips_version": "8.12.1",
      "device_name": "MyNvidiaJetsonEdgeDevice",
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
      "ei_ggc_user_groups": "video audio input users system render",
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
      "device_name": "MyNvidiaJetsonEdgeDevice",
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
      "ei_ggc_user_groups": "video audio input users system render",
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

{{% notice Note %}}
When running a model compiled specifically for a Jetson GPU, the first invocation can take 2-3 minutes while the model loads into GPU memory. Subsequent invocations are much faster.
{{% /notice %}}

Your Nvidia Jetson is ready. Return to the [hardware setup page](/learning-paths/embedded-and-microcontrollers/edge_impulse_greengrass/hardwaresetup/) and continue to the next section to set up your Edge Impulse project.