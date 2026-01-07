---
title: YOCTO Installation - UltraEdge

weight: 3

layout: "learningpathall"
---

# System Requirements

- Linux host system (64-bit recommended)
- Supported host architectures:
  - AArch64 (arm64)
  - ARMv7

- Supported Linux distributions(Tested):
  - Ubuntu 20.04 LTS (AArch64)
  - Ubuntu 22.04 LTS (AArch64)

- Minimum hardware requirements:
  - CPU: Quad-core processor or better
  - RAM: 8 GB minimum (16 GB recommended)
  - Disk space: At least 250 GB free (500 GB +recommended for multiple builds)

- Required software:
  - Git (for fetching Yocto layers)
  - Python (Yocto-supported version from host distro)
  - GNU build tools (gcc, make, etc.)

- Internet access:
  - Required for downloading source code, layers, and dependencies

#### Yocto Build Notes
- Builds are resource-intensive and may take several hours depending on hardware

#### Supported Targets / Boards
- ARM-based SoCs commonly supported by Yocto layers, such as:
  - NXP i.MX series
  - Generic ARMv7 / AArch64 reference platforms
  - Raspberry Pi (via meta-raspberrypi) (may be used for experimentation)

# YOCTO Build Instructions

In this section, we use the **NXP S32G-VNP-GLDBOX3** hardware platform to run EdgeBlox Agent. The following steps demonstrate how to build a Yocto-based Linux image for this board and prepare it for EdgeBlox deployment.

### Yocto Build Setup for NXP S32G-VNP-GLDBOX3

This section describes how to set up and build a Yocto-based Linux image for the
**NXP S32G-VNP-GLDBOX3** board using the **BSP 38.0** release from NXP’s
`auto_yocto_bsp` repository.

### Prerequisites

Before starting, ensure the following requirements are met:

- **Host System:** Ubuntu 20.04 (or a compatible Ubuntu version)
- **Hardware:** NXP S32G-VNP-GLDBOX3 board
- **Internet Access:** The board must have an active internet connection
- **Network Security:** Port `8883` must be whitelisted to allow MQTT over SSL communication

### Reference Links

- **NXP Auto Linux BSP Repository (BSP 38.0):**  
  https://github.com/nxp-auto-linux/auto_yocto_bsp/tree/release/bsp38.0

- **NXP GoldBox 3 Design Page:**  
  https://www.nxp.com/design/design-center/development-boards-and-designs/GOLDBOX-3

## Step-by-Step Setup Instructions

### 1. Install Required Packages

Install the tools and dependencies required to set up the Yocto build
environment on the host system.

```bash
sudo apt install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint3 xterm python3-subunit mesa-common-dev zstd liblz4-tool
sudo apt-get install chrpath diffstat gawk lz4 mtools
sudo apt-get install curl
sudo apt-get install git
sudo apt-get install python2
```
Verify the installed versions:

```Bash
python2 --version
curl --version
```
Note: Adding python 2 here due to BSP

### 2. Install the `repo` Tool

The `repo` tool is used to manage multiple Git repositories required for the Yocto build environment.

```Bash
mkdir -p ~/bin
curl https://storage.googleapis.com/git-repo-downloads/repo >
~/bin/repo
chmod a+x ~/bin/repo
export PATH=${PATH}:~/bin
```

### 3. Set Up the Yocto Build Environment

Create a working directory for the Yocto BSP and initialize the NXP Auto Linux BSP repository.

```Bash
mkdir fsl-auto-yocto-bsp
cd fsl-auto-yocto-bsp/
repo init -u https://github.com/nxp-auto-linux/auto_yocto_bsp -b release/bsp38.0
repo sync
```

### 4.Prepare the Host System
Run the host preparation script to ensure the system is configured correctly:

```Bash
sudo ./sources/meta-alb/scripts/host-prepare.sh
```

{{% notice Note %}}
In default installs of Ubuntu for your YOCTO build environment, you will get an error from the above command stating that the `/etc/sudoers` file needs to be updated.  Please follow those instructions as the script needs the additional permissions to fully setup properly. Otherwise, the subsequent `bitbake` commands below will fail. 
{{% /notice %}}

### 5. Configure Locale Settings
Set up the system locale to avoid build issues:

```Bash
sudo locale-gen en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LC_CTYPE=en_US.UTF-8
```

### 6. Start the Yocto Build
Run the BitBake command to build the fsl-image-base image for the S32G-VNP-GLDBOX3 board:

```Bash
bitbake fsl-image-base
```

## Yocto Build with edgeblox as Meta Layer

1. **Copy Layer:** Copy the `meta-edgeblox` folder into your Yocto source environment.
2. **Add Layer:** Add the layer to your build configuration:

### 1. Create and Add the Edgeblox Layer

Run the following commands to create the new layer and link it to your project:

```Bash
bitbake-layers create-layer ../meta-edgeblox
bitbake-layers add-layer ../meta-edgeblox
```

    Note: Open conf/bblayers.conf to verify that meta-edgeblox has been added to the BBLAYERS list.

### 2. Install Recipe Files

Navigate to the example recipes folder:

```Bash
cd poky/meta-edgeblox/recipes-example
```
Remove the default example folder.
Extract the contents of the meta-edgeblox.zip(provided by the Tinkerblox team via email **techsupport@tinkerblox.io**), and copy the recipes-example to your recipes-example folder 

### 3. Configure Layer Dependencies

Edit the poky/meta-edgeblox/conf/layer.conf file to include the necessary packages for the Edgeblox agent and environment:

```Plaintext
IMAGE_INSTALL:append = "  dpkg ldd libxcrypt binutils zlib cjson edgeblox-agent cgroup-lite rng-tools procps ca-certificates catatonit openssh htop  python3-cantools  python3-joblib  python3-numpy  python3-pandas python3-can python3-djangorestframework python3-dev python3-pip runit go node-exporter  util-linux "
```

Once you have configured the services and dependencies in your configuration files, initiate the build process using the BitBake command:

```bash
bitbake fsl-image-base
```
If any build errors occur, debug and resolve them accordingly.

If you encounter errors related to missing recipes, search for the required recipe using the following link:

```
https://layers.openembedded.org/layerindex/branch/master/recipes/
```

### 4. Enabling kernal configs in Yocto

Manual kernel configuration is required to support containerization features. Use the following command to access the kernel configuration menu:

```bash
bitbake virtual/kernel -c menuconfig
```

### 5. Enabling required Kernel Flags
Ensure the following configurations are enabled (=y):

Namespaces:

    CONFIG_NAMESPACES=y
    CONFIG_UTS_NS=y
    CONFIG_IPC_NS=y
    CONFIG_PID_NS=y
    CONFIG_NET_NS=y
    CONFIG_USER_NS=y

Control Groups (Cgroups):

    CONFIG_CGROUPS=y
    CONFIG_CGROUP_BPF=y
    CONFIG_CGROUP_SCHED=y
    CONFIG_CPUSETS=y
    CONFIG_MEMCG=y
    CONFIG_BLK_CGROUP=y
    CONFIG_CGROUP_HUGETLB=y

Storage & Security:

    CONFIG_OVERLAY_FS=y
    CONFIG_SECCOMP=y
    CONFIG_SECCOMP_FILTER=y

Networking Features:

    CONFIG_VETH=y (Virtual Ethernet)
    CONFIG_BRIDGE=y (Bridging)
    CONFIG_IPTABLES=y (Networking)

These are basic configurations need to run ultra edge agent in the device if any additional configiuration needed that needs to be configured.

### 6. Compile and build

Compile the configuration by using below commands and start building the image.

```bash
bitbake -c menuconfig virtual/kernel
bitbake -c savedefconfig virtual/kernel
bitbake virtual/kernel -f -c compile
bitbake fsl-image-base
```

<video width="800" controls>
  <source src="https://raw.githubusercontent.com/Tinkerbloxsupport/arm-learning-path-support/main/static/videos/yocto.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


### 7. Flashing the SD Card:

Replace <image-name> and <partition> (e.g., /dev/sdb) with your specific details. Warning: Ensure the device path is correct to avoid data loss.

```bash
sudo dd if=<image-name>.sdcard of=/dev/sdX bs=1M && sync
```

# Activation of Agent

On the first boot, the agent will automatically generate a file named
`activation_key.json` at the path:

    /opt/tinkerblox/activation_key.json

Share this `activation_key.json` file with the TinkerBlox team to
receive license key (which includes license metadata).

For device activation, contact the Tinkerblox support team to obtain
the licensed activation key via **techsupport@tinkerblox.io** 

1.  Stop the agent using the following command:

        sudo systemctl stop tbx-agent.service

2.  Replace the existing `activation_key.json` file in
    `/opt/tinkerblox/` with the licensed one provided by TinkerBlox.

3.  Start the agent:

        sudo systemctl start tbx-agent.service

#### Manual Running

-   Binary path: `/bin/tbx-agent`

-   To start:

        cd /bin
        ./tbx-agent

-   To stop, press <span class="kbd">Ctrl</span> +
    <span class="kbd">C</span> once.

<video width="800" controls>
  <source src="https://raw.githubusercontent.com/Tinkerbloxsupport/arm-learning-path-support/main/static/videos/Activation.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


# Installs and running Workloads

This section demonstrates how to deploy and manage a MicroPac-based
workload on an UltraEdge-enabled device.

This workflow uses the MicroBoost CLI to install, start, stop, and monitor MicroPac-based workloads running on UltraEdge.

### Building the workload using mpac builder

We are going to see how to build the .mpac file from a cross-architecture setup using **Micropac Builder**.

-   Verify QEMU installation:

        qemu-aarch64-static --version

-   Check binfmt registration:

        ls /proc/sys/fs/binfmt_misc/


Navigate to your project directory and Make sure the micropacfile is placed in your project directory,(refer debian_installation.md for more details).

-   Run below command:

        sudo micropac-builder build

After the build completes, the workload file your_service.mpac will be generated in your project directory.

Copy the your_service.mpac file to any root filesystem path of your NXP target to deploy it.


### Install the workloads in the device using below command

```
systemctl start runit-supervise
```

```
tinkerblox-cli microboost install -f /path/to/your_service.mpac
```

Now by using the microboost List command we can find the id of the service.

```
tinkerblox-cli microboost list
```

Copy the id and by using below command we can start,stop and status of the service.

```
tinkerblox-cli microboost start <id>
```

```
tinkerblox-cli microboost stop <id>
```

```
tinkerblox-cli microboost status <id>
```

To Uninstalls the Workload with the specified ID

```
tinkerblox-cli microboost uninstall <id>
```

<video width="800" controls>
  <source src="https://raw.githubusercontent.com/Tinkerbloxsupport/arm-learning-path-support/main/static/videos/microservice_installation.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
