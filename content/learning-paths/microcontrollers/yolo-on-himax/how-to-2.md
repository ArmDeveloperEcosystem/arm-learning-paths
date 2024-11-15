---
title: Build the firmware
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

TODO short intro / framing?

## Clone the Himax project

Himax has set up a repository containing a few examples for the Seeed Grove Vision AI V2 board. By recursively cloning the Himax examples repo, git will include the necessary sub-repositories that have been configured for the project.

```bash
git clone --recursive https://github.com/HimaxWiseEyePlus/Seeed_Grove_Vision_AI_Module_V2.git
cd Seeed_Grove_Vision_AI_Module_V2
```

## Compile the firmware

The make build tool is used to compile the source code. This should take up to 10 minutes depending on the number of CPU cores available.

```bash
cd EPII_CM55M_APP_S
make clean
make
```

## Generate the firmware image

The examples repository contains scripts to generate the image.

```bash
cd ../we2_image_gen_local/
cp ../EPII_CM55M_APP_S/obj_epii_evb_icv30_bdv10/gnu_epii_evb_WLCSP65/EPII_CM55M_gnu_epii_evb_WLCSP65_s.elf input_case1_secboot/
```

## Linux

```bash
./we2_local_image_gen project_case1_blp_wlcsp.json
```

## macOS
```console
./we2_local_image_gen_macOS_arm64 project_case1_blp_wlcsp.json
```

Your terminal output should end with the following.
```output
Output image: output_case1_sec_wlcsp/output.img
Output image: output_case1_sec_wlcsp/output.img

IMAGE GEN DONE
```

With this step, you are ready to flash the image onto the Himax development board.