---
title: Overview
weight: 2
layout: learningpathall
---

## Overview

[MNIST](https://en.wikipedia.org/wiki/MNIST_database), widely classified as the "Hello World" of machine learing, is a dataset containing 70,000 28x28 pixel grayscale images of handwritten digits 0-9. It is commonly used for training image processing systems.

In this Learning Path, you will run an MNIST digit-classification model on the Arm Ethos-U85 NPU. You can either use the provided `.pte` model or follow an optional walkthrough to train and export your own MNIST model. 

## Hardware Overview - Alif Ensemble E8 Series

The Alif Ensemble E8 DevKit features two dual-core Arm processors (Cortex-A32 and Cortex-M55) and three neural processing units (NPUs): two Ethos-U55 and one Ethos-U85.

<div style="text-align:center;">
  <img src="/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/alif-ensemble-e8-board-soc-highlighted.jpg" alt="Alif Ensemble E8 Board SoC highlighted" title="Arm Ethos-U NPU location" style="max-width:800px; width:100%;" />
  <div style="font-style:italic;">Arm Ethos-U NPU location</div>
</div>

### Connecting to the DevKit

- Unplug all USB cables from the DevKit before changing any jumpers.

- Verify that the jumpers are in their factory default positions, as shown in the Alif Ensemble E8 DevKit (DK-E8) User Guide on [alifsemi.com](https://alifsemi.com/support/kits/ensemble-e8devkit/).

- Connect a USB-C cable from your computer to the PRG USB port on the bottom edge of the DevKit.

![PRG USB Port Location alt-text#center](prg-usb-port.png "Connect USB-C cable to the PRG USB port")
- Confirm that a green LED illuminates near the E1 device and the UART switch (SW4).

Leave SW4 in its default position. This routes the on-board USB UART to SEUART, which the Alif Security Toolkit (SETOOLS) uses for programming.

#### Verify USB connection

Check that your computer recognizes the DevKit:

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash">}}
ls /dev/cu.*
  {{< /tab >}}

  {{< tab header="Linux" language="bash">}}
ls /dev/ttyACM* /dev/ttyUSB* 2>/dev/null
  {{< /tab >}}

  {{< tab header="Windows" language="powershell">}}
Get-CimInstance Win32_SerialPort | Select-Object DeviceID,Name,Description
  {{< /tab >}}
{{< /tabpane >}}

{{% notice Important %}}
Close any terminal application that’s connected to SEUART, such as PuTTY, minicom, or screen, before you use the Security Toolkit (SETOOLS). The DevKit exposes only one SEUART interface, so SETOOLS can’t access the port if another application is already using it.
{{% /notice %}}

You should see a SEGGER J-Link device. If you are unsure which entry belongs to the DevKit, run the command before and after connecting the board and compare the output. In the case where no device appears, check that the USB cable is connected to the **PRG USB** port and that the cable supports data, not only charging.