---
title: Test PAC/BTI availability on your devices via MQTT

weight: 7

layout: "learningpathall"
---

### Introduction

In this section, you run a test through the AWS IoT Core MQTT test client to check PAC/BTI availability on each platform.

### Dispatching the test invocation command

1. In the AWS Console, go to **IoT Core** -> **Greengrass devices** -> **Core devices** and record both core device names.

![Core devices](images/test-1.png "Core devices list")

2. In the AWS Console, open **IoT Core** -> **MQTT test client** and select **Subscribe to a topic**.

Enter the following topic:
```json
Topic: arm/demo/+/security/pacbti/attack/result
```
Select **Subscribe**.

![Subscribe](images/test-2.png "Subscribe to the result topic")

3. While still in MQTT test client, select **Publish to a topic** and enter the following, replacing **YOUR_CORE_DEVICE_NAME** with your Thor device name:

```json
Topic name:  **arm/demo/YOUR_CORE_DEVICE_NAME/security/pacbti/attack/trigger**

Message payload:
{
  "action": "run_attack",
  "request_id": "demo-001"
}
```

Select **Publish**.

![Publish to Thor device](images/test-3.png "Publish to Thor device")

### Reading the results

In the subscriptions area of the MQTT test client window, you should see results resembling this for your Thor device:

```output
{
  "binary": "/greengrass/v2/work/danson-com.arm.demo.PacBtiDemo/build/armv9-protected/vuln_demo",
  "build_flavor": "armv9-protected",
  "device": "thor",
  "executed_at": "2026-04-30T21:33:18.796870+00:00",
  "exploit_run": {
    "returncode": 252,
    "stderr": "",
    "stdout": ""
  },
  "exploit_succeeded": false,
  "interpretation": "Exploit did not reach malicious_success(); on PAC/BTI builds a crash or early termination is expected.",
  "machine": "aarch64",
  "marker_found": false,
  "normal_run": {
    "returncode": 0,
    "stderr": "",
    "stdout": "Usage: vuln_demo <hex_payload>\n"
  },
  "protections": {
    "has_autiasp": true,
    "has_bti": true,
    "has_paciasp": true,
    "has_retaa": true
  },
  "trigger": {
    "payload": {
      "action": "run_attack",
      "request_id": "demo-001"
    },
    "source_topic": "arm/demo/Dougs_Jetson_Thor/security/pacbti/attack/trigger"
  }
}
```

This result indicates the Thor device (Armv9) reports PAC and BTI capabilities.

Now test the RPi5. In **Publish to a topic**, replace **YOUR_CORE_DEVICE_NAME** with your RPi5 core device name:


```json
Topic name:  **arm/demo/YOUR_CORE_DEVICE_NAME/security/pacbti/attack/trigger**

Message payload:
{
  "action": "run_attack",
  "request_id": "demo-001"
}
```

Select **Publish**.

![Publish to RPi5 device](images/test-4.png "Publish to RPi5 device")

Your output should be similar to the following:

```output
{
  "binary": "/greengrass/v2/work/danson-com.arm.demo.PacBtiDemo/build/armv8-unprotected/vuln_demo",
  "build_flavor": "armv8-unprotected",
  "device": "rpi5-desktop-16",
  "executed_at": "2026-04-30T21:33:53.526756+00:00",
  "exploit_run": {
    "returncode": 0,
    "stderr": "",
    "stdout": ""
  },
  "exploit_succeeded": true,
  "interpretation": "Exploit reached malicious_success()",
  "machine": "aarch64",
  "marker_found": true,
  "normal_run": {
    "returncode": 0,
    "stderr": "",
    "stdout": "Usage: vuln_demo <hex_payload>\n"
  },
  "protections": {
    "has_autiasp": false,
    "has_bti": false,
    "has_paciasp": false,
    "has_retaa": false
  },
  "trigger": {
    "payload": {
      "action": "run_attack",
      "request_id": "demo-001"
    },
    "source_topic": "arm/demo/Dougs_RPi5_Hailo_16/security/pacbti/attack/trigger"
  }
}

This result indicates the RPi5 device (Armv8) does not report PAC and BTI capabilities and thus is vulnerable to some attacks that PAC/BTI inhibits.

### What we learned

Armv9 devices provide additional control-flow protection features for pointer integrity. You also used AWS IoT Greengrass to deploy and run a custom validation workflow across multiple edge devices.