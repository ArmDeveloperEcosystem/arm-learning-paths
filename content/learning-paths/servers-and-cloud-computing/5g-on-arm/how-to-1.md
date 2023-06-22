---
title: How to Choose Right 5G Servers
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How to Choose Right 5G Servers
---

#### We have done extensive 5G development and testing on Arm servers with various HW configurations and SW components:

     1. 5G-in-one-box (software only)

     2. 5G with Genevisio NXP L1 Accelerator

     3. 5G with Nvidia A100X (A100 GPU + BlueField2 NIC)

#### We have evaluated a variety of Arm server platforms from Foxconn, Gigabyte, WIWYNN, Supermicro and HPE

     1. Gigabyte (Mt. Snow 1P)

     2. WIWYNN (Mt. Jade 2P)

     3. Foxconn (Mt. Collins 2P)

     4. Supermicro (R12SPD 1P)

     5. HPE (ProLiant RL300 Gen11 (P59870-B21) 1P) 

#### Things to consider:

1P vs 2P systems:

For evaluation purpose, we recommend a 1P system which should be sufficient to run any 5G software stacks (L1/L2/L3) considering that the Arm CPU has at least 80 cores. 2P system would be great to run more processes on single box, however, we need to avoid socket communication, especially when some PCIe devices sit in a different node across from the CPU. 

1U vs 2U systems:

1U would be sufficient to run 5G CN Core software or pure 5G software stacks while 2U is definitely required for needing additional HW such as several PCIe cards or a full length PCIe card for L1 processing, for example, the Nvidia A100X and Genvisio.

#### Accommodating PCIe Accelerators

Due to nature of PCIe devices, we need to consider carefully for picking up right Arm server to accommodating the PCIe Accelerators we are going to use.

For full length PCIe cards, you need at least an 2U server, however not every 2U server will support full length/full width PCIe devices. Also, some PCIe full profile devices require more power to run properly, for example, Supermicro's ARM server seems to accommodate Genevisio card better.

For PCIe cards taking up two PCIe slots like Nvidia A100X, not every 2U will be right choice. Because A100X combines GPU and Mellanox NIC in one devices, we need to make sure its NIC ports face out. At this moment, only Supermicro ARM server has designed its server with A100X support in mind.

#### Available ARM Servers

1. Gigabytes/WIWYNN servers

   In genearal they are able to do what intends to do, we have used Gigabyte servers to do CORE server, edge server or 5G network in one box, which is so far working well.

   Its GPU version claims to support up to 3 GPUs, but we have tried that only one A100X can work, however it does not have proper orientation for A100X ethernet ports.

   Its GPU version does not work for some other PCIe devices we have tested.

2. Foxconn Mt Collins 2P is a powerful 2P system to accommodate more than 4 PCIe slots, however

   It can support A100X, but it can't have its NIC ports in right orientation.

   It seems to have some issues for different PCIe devices, so you need to make sure it can work for your hardware requirement.

3. Supermicro server

   SMC seems to have its solutions for some of PCIe devices we would have issues with other servers. At this moment it is the server can support all of various PCIe devices we intend to use such as Nvidia 100X with proper orientation for its ethernet ports. 

4. HPE server

   It is 1U server and can have only two PCIe slots, so pobably is ideal for 5GCN Core server.

   Another noticeble thing is that HPE server supports 220V only, you can't use in 110V outlet.

#### A few thoughts about Arm ServerReady

1. Current ServerReady is not strengthened enough to make sure the ODM/OEM is 100% ready for deployment in 5G space. In order to qualify an Arm server for 5G Ready, we need to make sure that they can work with the required hardware for 5G.

2. The Arm server needs to pass PCIe device detection as minimal requirement. That is the lspci command should be able to list these PCIe devices without issues.

3. It is important to work with Arm server ODM/OEM and their firmware team for any issues rised during evaulation so any issues can be fedback to the ODM/OEM to be addressed in timely fashion.

4. ArmServerReady should also mandate that standard IPMI interface must be supported because it is important standard.

#### 5G ServerReady
We like to develop our own methodology to qualify any server from ODM/OEM to be 5G ServerReady:

   1. Using existing PoC example to run the qualification to see if the server can pass with possible automation

   2. Using Performance PoC example to test to see if the server can meet our performance goal with possible automation

   3. Developing General Testing Scripts to check the requirement for configuration and compliance for 5G ServerReady

   4. Incorporate Testing equipment like Keysight and Viavi for 5G ServerReady tests

