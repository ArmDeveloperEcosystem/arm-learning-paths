---
title: Deploy the project
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the target

Before deploying the Template, confirm that the FRDM i.MX 93 board is reachable from your host and that it's ready for deployment:

```bash
topo health --target <user>@<target-ip>
```
Replace `<target-ip>` with the IP address or hostname of your board.

Resolve any errors before continuing.

The target section should include successful checks similar to:

```output
Host
----
Topo: ✅ (topo)
SSH: ✅ (ssh)
Curl: ✅ (curl)
Container Engine: ✅ (docker)

Target
------
Destination: ssh://<target-ip>
Connectivity: ✅
Container Engine: ✅ (docker)
Remoteproc Runtime: ✅ (remoteproc-runtime)
Remoteproc Shim: ✅ (containerd-shim-remoteproc-v1)
Hardware Info: ✅ (lscpu)
Subsystem Driver (remoteproc): ✅ (imx-rproc)
```

If `remoteproc-runtime` is missing, install it with Topo:

```bash
topo install remoteproc-runtime --target <user>@<target-ip>
```

Run the health check again:

```bash
topo health --target <user>@<target-ip>
```

## Reserve memory in the device tree

The web application and Cortex-M33 firmware exchange data through reserved physical memory. The target device tree must reserve memory for the model/input buffer and for Ethos-U65. We are now goint to modify the device tree and reboot the target so that this modifications take place. 

{{% notice Warning %}}
Back up the board's original device tree before modifying it. The exact boot partition can differ between Linux images, so check the paths on your board before copying files.
{{< /notice >}}

On your host, create a working directory and dump the live device tree from the target:

```bash
mkdir -p devicetree
ssh <user>@<target-ip> 'cat /sys/firmware/fdt' > devicetree/live.dtb
dtc -I dtb -O dts -o devicetree/live.dts devicetree/live.dtb
```

Open `devicetree/live.dts` in an editor.

Under `remoteproc-cm33`, add the CM33 power domain if it is not already present:

```dts
power-domains = <0x61>;
```

Under `reserved-memory`, add the model memory range:

```dts
model@c0000000 {
    reg = <0x00 0xc0000000 0x00 0x400000>;
    no-map;
};
```

Update the Ethos-U reserved-memory node so it is reserved and not reusable:

```dts
ethosu_region@A8000000 {
    compatible = "shared-dma-pool";
    reg = <0x00 0xa8000000 0x00 0x8000000>;
    no-map;
    phandle = <0x60>;
};
```

Add `iomem=relaxed` to `chosen.bootargs`. For example:

```dts
bootargs = "clk-imx93.mcore_booted console=ttyLP0,115200 earlycon root=/dev/mmcblk1p2 rootwait rw iomem=relaxed";
```

Build the patched device tree:

```bash
dtc -I dts -O dtb -o devicetree/patched.dtb devicetree/live.dts
```

Copy it to the board:

```bash
scp devicetree/patched.dtb <user>@<target-ip>:/tmp/patched.dtb
```

Install it on the board. Adjust the boot partition path if your image uses a different location:

```bash
ssh <user>@<target-ip>
cp /run/media/boot-mmcblk1p1/imx93-11x11-frdm.dtb \
   /run/media/boot-mmcblk1p1/imx93-11x11-frdm.dtb.bak
cp /tmp/patched.dtb \
   /run/media/boot-mmcblk1p1/imx93-11x11-frdm.dtb
sync
reboot
```

After the board reboots, run the Topo health check again from the host:

```bash
topo health --target <user>@<target-ip>
```

## Clone the Template

Clone the Template onto your host:

```bash
topo clone https://github.com/Arm-Examples/topo-imx93-npu-deployment.git
```

Topo prompts for optional build cache image arguments:

```output
EXECUTORCH_BASE_CACHE_IMAGE
IMX93_RUNNER_BUILD_CACHE_IMAGE
```

Accept the defaults unless you have your own cache images.

Enter the project directory:

```bash
cd topo-imx93-npu-deployment
```

## Deploy to the board

Deploy the project to your target:

```bash
topo deploy --target <user>@<target-ip>
```

If not pulling from the cache, the first build can take a long time and requires about 25 GB of free disk space. It downloads and builds ExecuTorch, the Arm GNU toolchain, MCUX SDK components, RPMsg-Lite, and the Cortex-M33 runner sources. Later builds are faster when Docker can reuse local cache layers or import the configured GHCR cache layers.

During deployment, Topo builds the required images, transfers them to the target, starts the Cortex-M33 firmware through `remoteproc-runtime`, and starts the web application.

When deployment succeeds, the output includes a successful service startup. You can also check the deployed services:

```bash
topo ps --target <user>@<target-ip>
```

## Open the web application

Open the web application in a browser:

```output
http://<target-ip>:3001
```

The application shows:

- an image selector
- a **Classify** button
- board prerequisite checks
- classification results
- an expandable analysis section with runtime details

Select an image from an ImageNet-supported class, then click **Classify**. A successful run returns top-1 and top-5 ImageNet classifications.

If you need to use a different target port, set `WEBAPP_PORT` when deploying:

```bash
WEBAPP_PORT=3002 topo deploy --target <user>@<target-ip>
```

Then open:

```output
http://<target-ip>:3002
```

You should see something similar to:


![Screenshot of the web interface running on an Arm-based target, showing an image and the model response. This confirms successful deployment and provides a visual reference for the expected result.#center](topo_npu_classifier.png "Image classification as seen in the web app")

## What you've accomplished

You have prepared an FRDM i.MX 93 board for shared-memory NPU inference, deployed the `topo-imx93-npu-deployment` Template with Topo, started Cortex-M33 firmware through `remoteproc-runtime`, and used a browser-based application to run MobileNetV2 classification with Ethos-U65 acceleration.
Next, you will review the toolchains used to build the model artifact, firmware runner, and web application. 
