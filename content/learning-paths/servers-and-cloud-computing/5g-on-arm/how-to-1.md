---
title: How to Choose Right 5G Servers
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How to Choose Right 5G Servers
---

#### We have done extensive 5G development on Arm servers with various HW configurations and SW components:

     1. 5G-in-one-box (software only)

     2. 5G with Genevisio L1 Accerlator

     3. 5G with Nvidia A100X (A100 GPU + BlueField2 NIC)

#### We have evaluated variety of Arm server platforms from Foxconn, Gigabyte, SuperMicro and HPE

     1. Gigabyte (Mt. Snow 1P)

     2. WIWYNN (Mt. Jade 2P)

     3. Foxconn (Mt. Collins 2P)

     4. SuperMicro (R12SPD 1P)

     5. HPE (ProLiant RL300 Gen11 (P59870-B21) 1P) 

#### Things to consider:

1P vs 2P systems:

For evlaution purpose, 1P system should be sufficient to run any 5G software (L1/L2/L3) considering that the Arm CPU has at least 80 cores. 2P system would add more overhead introduced by numa system. So for simplicity, we would recommend 1P system.

1U vs. 2U systems:

1U would be sufficient to run 5G CN Core software while 2U is definitely required for using additional HW such as PCIe card for L1 processing, e.g. the Nvidia A100X and Genvisio.

#### Accommodate PCIe Accerlators

Please note due to nature of PCIe devices, we need to consider carefully for picking up right Arm server to accommodating the PCIe Accerlators.

For full length PCIe cards, you need at least 2U server, however not every 2U server will support full length/full width PCIe devices. Also some PCIe full profile devices requirea little bit higher voltage to run properly, SuperMicro ARM server seems to accommondate Genevisio card better, the second Arm server we tested and it was working is FoxConn ARM server, but it is an 2P system, a bit overkill to start with.

For PCIe cards taking up two PCIe slots like Nvidia A100X, not every 2U will be right choice. Because A100X combines GPU and Mellanox NIC in one devices, we need to make sure its NIC ports face out. At this moment, only SuperMicro ARM server has designed its server with A100X support in mind.

#### Available ARM Servers

1. Gigabytes/WIWYNN servers

   In genearal they are able to do what intends to do, supporting Nvidia A100X, but it was not designed for A100X for the NIC ports outfit.

   We have used Gigabyte servers to do CORE server, edge server or 5G network in one box (Altran), which is so far great

   However certain Gigabytes/WIWYNN models have issue to support the requirement of supporting NXP Genevisio PCIe card, Intel QAT and two Intel NIC X710 cards due to its limited estate space

   the GPU version G242-P3X claims to support up to 3 GPUs, but we tried, it is only one A100X can work

   the GPU version does not work for Genevisio card

2. Foxconn Mt Collins 2P is a powerful 2P system to accommodate more than 4 PCIe slots, however

   It can't accommodate A100X for having its NIC ports in right orientation

   It has three riser cages, but the right one (from its back panel view) is useless and in the both left and middle ones, there are only middle and bottom slots work, the top one slots never work

   the bottom ones can't fit a full length PCIe card as its wiring and other stuff is in conflict with the PCIe card on the bottom slot

   When inserting A100X or Genevisio card or Intel NIC 710 card, the server will generate tons of PCIe AER warning messages (even though it claims it is corrected, but not sure what extent of its impact)
 
   It never be able to detect Intel NIC 710 4-port card

   2P server might not be necessary in our use case here. Additionally it introduces the overhead of numa system.

3. SuperMicro server

   SMC initially has PCIe power issues with A100X and GeneVisio cards. After put down extra power cables from SuperMicro (both the GPU power cable and the Y-shape cable to boost the 12V to its PCIe riser cards, both GeneVisio and A100X can be functional.

   It can detect Intel NIC 710 4-port, make it only Arm server being able to do that!

   Also it is tricky to play with SuperMicro to host various PCIe card 

   It uses OpenBMC as its BMC, we have trouble to login into its BMC UI, however its motherboard has Password printed and use that password we can use ipmitool or its UI to operate/access the server

4. HPE server

   Its BMC needs to enable IPMI i/f from its UI, however ipmi SOL is "not supported", but you can get serial console by... ssh-ing into the iLO and then using "vsp" (virtual serial port). There's also another one for physical, and both seem to work, but "vsp" is recommended by HP.
 
   We had issue when boot with USB Ubuntu from VGA or remote access, after adding "console=tty0" to the kernel boot argument, we are able to access via VGA

   this server can have only two PCIe slots, so not much we can play with for 5G server. Probably ideal for 5GCN Core server.

#### A few thoughts about Arm ServerReady

1. current ServerReady is not strengthened enough to make sure the ODM/OEM have 100% ready for deployment in 5G space. For example, in the case of Foxconn, we were struggling to make it accommodating to support our 5G PoC requirement and it's quite fragile.

        i. We have to try all combination of PCIe cards with different PCIe slots to finalize only one combination work

        ii. the motherboard layout design was bad for accommodating full profile/full length PCIe card, especially for the slots in the bottom.

        iii. and the top slots never work, wasting two precious locations

2. must make ServerReady pass PCIe card detection as required (not necessary to test its driver to work), but at least the PCIe slots on server should bind to PCIe standard in voltage spec. verify by "lspci -t -nn -v "

3. must require ODM/OEM who apply for ServerReady to have a support team ready for at least one-year period after passing certification, in case the customers run into any issue with their server during evaluation. 

4. ArmServerReady should also mandate standard IPMI interface must be supported because it is important to have integration of IPMI into automation testing

#### 5G ServerReady
We like to develop our own methodology to qualify any server from ODM/OEM to be 5G ServerReady:

   1. Using existing PoC example to run the test to see if the server can pass (hopefully with automation)

   2. Using Performance PoC example to test to see if the server can meet our performance goal (hopefully with automation)

   3. Developing General Testing Scripts to check the requirement for configuration and compliance for 5G ServerReady

   4. Incorporate Testing equipment like Keysight and Viavi for 5G ServerReady tests

