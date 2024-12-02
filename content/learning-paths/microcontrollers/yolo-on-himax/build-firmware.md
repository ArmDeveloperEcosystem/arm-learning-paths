---
title: Build the firmware
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section will walk you though the process of generating the firmware image file.

## Clone the Himax project

Himax has set up a repository containing a few examples for the Seeed Grove Vision AI V2 board. It contains third-party software and scripts to build and flash the image with the object detection application. By recursively cloning the Himax examples repo, git will include the necessary sub-repositories that have been configured for the project.

```bash
git clone --recursive https://github.com/HimaxWiseEyePlus/Seeed_Grove_Vision_AI_Module_V2.git
cd Seeed_Grove_Vision_AI_Module_V2
```

## Compile the firmware

For the object detection to activate, you need to edit the project's `makefile`, located in the `EPII_CM55M_APP_S` directory.

```bash
cd EPII_CM55M_APP_S
```

Use the `make` build tool to compile the source code. This should take up to 10 minutes depending on the number of CPU cores available on your host machine. The result is an `.elf` file written to the directory below.

```bash
make clean
make
```

## Generate the firmware image

The examples repository contains scripts to generate the image file. Copy the `.elf` file to the `input_case1_secboot` directory.

```bash
cd ../we2_image_gen_local/
cp ../EPII_CM55M_APP_S/obj_epii_evb_icv30_bdv10/gnu_epii_evb_WLCSP65/EPII_CM55M_gnu_epii_evb_WLCSP65_s.elf input_case1_secboot/
```

Run the script corresponding to the OS of your host machine. This will create a file named `output.img` in the `output_case1_sec_wlcsp` directory.


{{< tabpane code=true >}}
  {{< tab header="Linux" language="shell">}}
./we2_local_image_gen project_case1_blp_wlcsp.json
  {{< /tab >}}
  {{< tab header="MacOS" language="shell">}}
./we2_local_image_gen_macOS_arm64 project_case1_blp_wlcsp.json
  {{< /tab >}}
{{< /tabpane >}}

Your terminal output should end with the following.

```output
Output image: output_case1_sec_wlcsp/output.img
Output image: output_case1_sec_wlcsp/output.img

IMAGE GEN DONE
```

With this step, you are ready to flash the image onto the Himax development board.