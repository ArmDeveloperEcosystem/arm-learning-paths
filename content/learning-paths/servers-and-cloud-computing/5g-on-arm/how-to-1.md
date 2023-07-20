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

     2. 5G with Inline L1 Accelerator

     3. 5G with L1 GPU Offload

     4. 5G with Lookaside Accelerator Offload

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

For full length PCIe cards, you need at least an 2U server, however not every 2U server will support full length/full width PCIe devices. Also, some PCIe full profile devices require more power to run properly, for example, Supermicro's ARM server seems to better accommodate some Inline L1 Accelerator cards.

For PCIe cards taking up two PCIe slots like Nvidia A100X, not every 2U will be right choice. Because A100X combines GPU and Mellanox NIC in one device, we need to make sure its NIC ports face out. At this moment, only Supermicro ARM server has designed its server with the full length PCIe cards such as Nvidia A100X converged card.

#### 5G Ready on Arm

This handbook attempt to provide the guide to make Arm servers ready for 5G development and deployment:

   1. Using existing PoC example to run the qualification to see if the server can pass with automation

   2. Using Performance PoC example to test to see if the server can meet our performance goal with automation



