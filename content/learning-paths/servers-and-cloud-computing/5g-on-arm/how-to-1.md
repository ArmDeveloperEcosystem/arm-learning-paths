---
title: Choose the appropriate Arm server for running the 5G stack
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose the appropriate Arm 5G Servers
---

#### Extensive 5G development and testing on Arm servers has been done on the hardware configurations and software components listed below:

     1. 5G-in-one-box (software only)

     2. 5G with Inline L1 Accelerator

     3. 5G with L1 GPU Offload

     4. 5G with Lookaside Accelerator Offload

#### The Arm server platforms listed below have been evaluated to run the 5G stack on:

     1. Gigabyte (Mt. Snow 1P)

     2. WIWYNN (Mt. Jade 2P)

     3. Foxconn (Mt. Collins 2P)

     4. Supermicro (R12SPD 1P)

     5. HPE (ProLiant RL300 Gen11 (P59870-B21) 1P) 

#### Things to consider:

1P (Single Processor) vs 2P (Dual Processors) systems:

For evaluation purposes, a 1P system is recommended which should be sufficient to run any 5G software stacks (L1 physical layer/L2 datalink layer/L3 network layer) considering that the Arm CPU has at least 80 cores. 2P system would be great to run more processes on single box, however, socket communication should be avoided, especially when some PCIe devices sit in a different node across from the CPU. 

1U (One Rack Unit) vs 2U (Two Rack Units) systems:

1U is sufficient to run 5G CN (Core Network) software or pure 5G software stacks while 2U is required when you need additional hardware such as several PCIe cards or a full length PCIe card for L1 processing, for example, the Nvidia A100X and Genvisio.

#### Accommodating PCIe Accelerators

Due to the nature of PCIe devices, you need to carefully select the right Arm server to accommodate the PCIe Accelerators you are going to use.

For full length PCIe cards, you need at least an 2U server, however not every 2U server will support full length/full width PCIe devices. Also, some PCIe full profile devices require more power to run properly, for example, Supermicro's Arm server better accommodate some Inline L1 Accelerator cards.

For PCIe cards taking up two PCIe slots like Nvidia A100X, not every 2U will be right choice. Because A100X combines GPU and Mellanox NIC (Network Interface Card) in one device, you need to make sure its NIC ports face out. At this moment, only Supermicro Arm server has designed its server with the full length PCIe cards such as Nvidia A100X converged card.

#### 5G Ready on Arm

This learning path attempts to provide the guidance to make Arm servers ready for 5G development and deployment:

   1. Using existing PoC example to run the qualification to see if the server can pass with automation

   2. Using Performance PoC example to test to see if the server can meet performance goals with automation



