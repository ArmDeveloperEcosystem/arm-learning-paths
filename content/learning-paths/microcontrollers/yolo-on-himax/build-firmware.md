---
title: Build the firmware
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section explains the process of generating a firmware image file.

## Clone the Himax GitHub project

Himax maintains a repository containing a few examples that can be used with the Seeed Grove Vision AI V2 board. 

It contains third-party software and scripts to build and flash the image with the object detection application. By recursively cloning the Himax examples repository, git includes the necessary subrepositories that have been configured for the project.

Clone the repository:

```bash
git clone --recursive https://github.com/HimaxWiseEyePlus/Seeed_Grove_Vision_AI_Module_V2.git
cd Seeed_Grove_Vision_AI_Module_V2
```

## Compile the firmware

Use Make to compile the source code for object detection. 

This can take up to 10 minutes depending on the number of CPU cores available on your host machine. 

```bash
cd EPII_CM55M_APP_S
make
```

When the build is complete, you will have an `.elf` file at `obj_epii_evb_icv30_bdv10/gnu_epii_evb_WLCSP65/EPII_CM55M_gnu_epii_evb_WLCSP65_s.elf` 

## Generate the firmware image

The examples repository contains scripts to generate the image file. 

Copy the `.elf` file to the `input_case1_secboot` directory:

```bash
cd ../we2_image_gen_local/
cp ../EPII_CM55M_APP_S/obj_epii_evb_icv30_bdv10/gnu_epii_evb_WLCSP65/EPII_CM55M_gnu_epii_evb_WLCSP65_s.elf input_case1_secboot/
```

Run the script on your OS as shown below. This creates a file named `output.img` in the `output_case1_sec_wlcsp` directory:


{{< tabpane code=true >}}
  {{< tab header="Linux" language="shell">}}
./we2_local_image_gen project_case1_blp_wlcsp.json
  {{< /tab >}}
  {{< tab header="macOS" language="shell">}}
./we2_local_image_gen_macOS_arm64 project_case1_blp_wlcsp.json
  {{< /tab >}}
{{< /tabpane >}}

The script output ends with the following:

```output
Output image: output_case1_sec_wlcsp/output.img
Output image: output_case1_sec_wlcsp/output.img

IMAGE GEN DONE
```

You are now ready to flash the image onto the Himax development board.
