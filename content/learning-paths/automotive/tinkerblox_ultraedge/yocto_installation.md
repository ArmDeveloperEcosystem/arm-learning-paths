---
title: YOCTO Installation - UltraEdge

weight: 3

layout: "learningpathall"
---

### System Requirements

-   Linux host (Aarch64 (arm64),armv7)

{{% notice Note %}}
REMOVE ME:  We need alot more detail here for YOCTO builds... what are the supported boards/etc... 
{{% /notice %}}

#### YOCTO Build Instructions

{{% notice Note %}}
REMOVE ME:  We need alot more detail here for YOCTO builds... where to pull images/BSPs/etc... how to configure the layers/packages/etc...
{{% /notice %}}

1.  Copy the `meta-tinkerblox` folder to your Yocto build environment.

2.  Add the layer:

        bitbake-layers add-layer <path-to-meta-tinkerblox>


{{% notice Note %}}
REMOVE ME:  We need alot more detail here for YOCTO builds... what does the build process look like. Where are the build completion artifacts. How to flash to the specific board/etc... 
{{% /notice %}}

3.  Build and flash the firmware to the target hardware.

#### Activation of Agent

On the first boot, the agent will automatically generate a file named
`activation_key.json` at the path:

    /opt/tinkerblox/activation_key.json

{{% notice Note %}}
REMOVE ME:  need contact information to the Tinkerblox team below... 
{{% /notice %}}

Share this `activation_key.json` file with the TinkerBlox team to
receive license key (which includes license metadata).

1.  Stop the agent using the following command:

        sudo systemctl stop ultraedge.service

2.  Replace the existing `activation_key.json` file in
    `/opt/tinkerblox/` with the licensed one provided by TinkerBlox.

3.  Start the agent:

        sudo systemctl start ultraedge.service

#### Manual Running

-   Binary path: `/opt/tinkerblox/Ultraedge/EdgeBloXagent`

-   To start:

        cd /opt/tinkerblox/Ultraedge
        ./EdgeBloXagent

-   To stop, press <span class="kbd">Ctrl</span> +
    <span class="kbd">C</span> once.