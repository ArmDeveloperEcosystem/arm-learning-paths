---
title: How to Tune Arm 5G Server
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How to Tune Arm 5G Server

### Kernel Tuning

For kernel tuning, please refer to the previous section on setting kernel boot arguments and CPU scaling.

### DPDK Tuning

#### System level setting:

Core isolation from Linux scheduler, Disabling interrupts, Huge page usage to minimize TLB misses are important before running DPDK PMDs.

Make sure that each memory channel has at least one memory DIMM inserted with 8GB memory size.

Enable cache stashing on ampere to stash the packets coming through NIC to SLC cache (System Level Cache, aks Level 3 Cache).

Cache stashing feature enable/disable on Ampere dynamically (No reboot required). slc_inst_s0 is a program can be available upon request:
```console
   ./slc_inst_s0 1  -- enable SLC installation for all root ports on Socket 0                                                                                                                                                                                                                       
   ./slc_inst_s0 0  -- disable SLC installation for all root ports on Socket 0
```

Here are the grub settings from Ampere machine:

```console
      # cat /proc/cmdline
        BOOT_IMAGE=/boot/vmlinuz-5.15.0-46-lowlatency root=UUID=c0ef447a-8367-4d45-8991-47ece2fcb425 ro iommu.passthrough=1 default_hugepagesz=1G hugepagesz=1G hugepages=20  isolcpus=1-69 irqaffinity=0 rcu_nocbs=1-69 nohz_full=1-69 kpti=off nosoftlockup
```

#### NIC Rx/Tx threshold setting:

DPDK Ethernet PMDs does the packet processing in a batch of 32 packets. Tuning the NIC Rx/Tx threshold through DPDK EAL config might provide performance boost.

Refer to `testpmd` application at https://doc.dpdk.org/guides/testpmd_app_ug/run_app.html and look for "–rxd" and "–txd" options to set the descriptor threshold.         

#### Before running the 5G stack, check whether maximum no drop rate is achieved using DPDK testpmd application.

Refer to the same link above to run `testpmd` on Ampere. This will ensure that the Ethernet PMD is operating at optimal performance. 

### Allocate Cores to Different Tasks

It is critical to carefully allocate the cores to various tasks for 5G stack. Make sure all of processes have their own cores to run on, not to step over each other.

For multiple socket server, always use `numactl` to launch your program to associate with the cpu and the PCIe device your program will access on same node.

Use `taskset` command to launch your program on specific cores.

### Profiling/Tracing

#### Using perf tools like :

   - "perf record & report" can be used to identify bottleneck based on events on specific core
   - "perf stat" can be used to statistically measure the KPIs like IPC, Front End/Back End Stalls and L1/L2/LLC Cache misses.

An example perf script that is run on an Arm Neoverse based server is shown below:

```console
#!/bin/bash
# This script must be run for every use case captured in SoW. This script captures the perf events on all the CU and DU DPDK and worker cores for 10 sec at 100 msec interval.
if [ $# -eq 0 ]; then
    >&2 echo "Usage: $0 log_file (Nomenclature: numue_numcell_l4proto_direction_pktsize)"
    exit 1
fi
 
sleep_sec=5
interval=1000
 
#Note: Get the optimial core id from CU and DU sys_config.txt files for each use case
cu_worker_core_a=1
cu_dpdk_core_a=21 #Perf stat on this core hangs
du_dpdk_core_a=27
du_dpdk_core_b=28
du_dpdk_core_c=29
du_worker_core_a=26
cu_worker_core_b=31
 
perf stat -A --output $1_IPC_core_$cu_worker_core_a.txt -e r8,r11,r23,r24 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_IPC_core_$cu_dpdk_core_a.txt -e r8,r11,r23,r24 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_IPC_core_$du_dpdk_core_a.txt -e r8,r11,r23,r24 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_IPC_core_$du_dpdk_core_b.txt -e r8,r11,r23,r24 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_IPC_core_$du_dpdk_core_c.txt -e r8,r11,r23,r24 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_IPC_core_$du_worker_core_a.txt -e r8,r11,r23,r24 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_IPC_core_$cu_worker_core_b.txt -e r8,r11,r23,r24 -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
 
perf stat -A --output $1_BR_core_$cu_worker_core_a.txt -e r8,r21,r22 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_BR_core_$cu_worker_core_a.txt -e r8,r21,r22 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_BR_core_$du_dpdk_core_a.txt -e r8,r21,r22 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_BR_core_$du_dpdk_core_b.txt -e r8,r21,r22 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_BR_core_$du_dpdk_core_c.txt -e r8,r21,r22 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_BR_core_$du_worker_core_a.txt -e r8,r21,r22 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_BR_core_$cu_worker_core_b.txt -e r8,r21,r22 -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
 
perf stat -A --output $1_ITLB_core_$cu_worker_core_a.txt -e r8,r35,r26 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_ITLB_core_$cu_worker_core_a.txt -e r8,r35,r26 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_ITLB_core_$du_dpdk_core_a.txt -e r8,r35,r26 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_ITLB_core_$du_dpdk_core_a.txt -e r8,r35,r26 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_ITLB_core_$du_dpdk_core_a.txt -e r8,r35,r26 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_ITLB_core_$du_worker_core_a.txt -e r8,r35,r26 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_ITLB_core_$cu_worker_core_b.txt -e r8,r35,r26 -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
 
perf stat -A --output $1_DTLB_core_$cu_worker_core_a.txt -e r8,r34,r25 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_DTLB_core_$cu_worker_core_a.txt -e r8,r34,r25 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_DTLB_core_$du_dpdk_core_a.txt -e r8,r34,r25 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_DTLB_core_$du_dpdk_core_a.txt -e r8,r34,r25 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_DTLB_core_$du_dpdk_core_a.txt -e r8,r34,r25 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_DTLB_core_$du_worker_core_a.txt -e r8,r34,r25 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_DTLB_core_$cu_worker_core_b.txt -e r8,r34,r25 -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
 
perf stat -A --output $1_L1I_core_$cu_worker_core_a.txt -e r8,r14,r1 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_L1I_core_$cu_worker_core_a.txt -e r8,r14,r1 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_L1I_core_$du_dpdk_core_a.txt -e r8,r14,r1 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_L1I_core_$du_dpdk_core_a.txt -e r8,r14,r1 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_L1I_core_$du_dpdk_core_a.txt -e r8,r14,r1 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_L1I_core_$du_worker_core_a.txt -e r8,r14,r1 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_L1I_core_$cu_worker_core_b.txt -e r8,r14,r1 -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
 
perf stat -A --output $1_L1D_core_$cu_worker_core_a.txt -e r8,r4,r3,r40,r41 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_L1D_core_$cu_worker_core_a.txt -e r8,r4,r3,r40,r41 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_L1D_core_$du_dpdk_core_a.txt -e r8,r4,r3,r40,r41 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_L1D_core_$du_dpdk_core_a.txt -e r8,r4,r3,r40,r41 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_L1D_core_$du_dpdk_core_a.txt -e r8,r4,r3,r40,r41 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_L1D_core_$du_worker_core_a.txt -e r8,r4,r3,r40,r41 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_L1D_core_$cu_worker_core_b.txt -e r8,r4,r3,r40,r41 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
 
perf stat -A --output $1_L2_core_$cu_worker_core_a.txt -e r8,r16,r17,r20 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_L2_core_$cu_worker_core_a.txt -e r8,r16,r17,r20 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_L2_core_$du_dpdk_core_a.txt -e r8,r16,r17,r20 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_L2_core_$du_dpdk_core_a.txt -e r8,r16,r17,r20 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_L2_core_$du_dpdk_core_a.txt -e r8,r16,r17,r20 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_L2_core_$du_worker_core_a.txt -e r8,r16,r17,r20 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_L2_core_$cu_worker_core_b.txt -e r8,r16,r17,r20 -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
 
perf stat -A --output $1_L2_RD_WR_core_$cu_worker_core_a.txt -e r16,r17,r20,r50,r51 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_L2_RD_WR_core_$cu_worker_core_a.txt -e r16,r17,r20,r50,r51 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_L2_RD_WR_core_$du_dpdk_core_a.txt -e r16,r17,r20,r50,r51 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_L2_RD_WR_core_$du_dpdk_core_a.txt -e r16,r17,r20,r50,r51 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_L2_RD_WR_core_$du_dpdk_core_a.txt -e r16,r17,r20,r50,r51 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_L2_RD_WR_core_$du_worker_core_a.txt -e r16,r17,r20,r50,r51 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_L2_RD_WR_core_$cu_worker_core_b.txt -e r16,r17,r20,r50,r51 -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
 
perf stat -A --output $1_LLC_$cu_worker_core_a.txt -e r8,r36,r37,r13 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_LLC_$cu_worker_core_a.txt -e r8,r36,r37,r13 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_LLC_$du_dpdk_core_a.txt -e r8,r36,r37,r13 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_LLC_$du_dpdk_core_a.txt -e r8,r36,r37,r13 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_LLC_$du_dpdk_core_a.txt -e r8,r36,r37,r13 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_LLC_$du_worker_core_a.txt -e r8,r36,r37,r13 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_LLC_$cu_worker_core_b.txt -e r8,r36,r37,r13 -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
 
perf stat -A --output $1_Mem_access_$cu_worker_core_a.txt -e r8,r13,r66,r67 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_Mem_access_$cu_worker_core_a.txt -e r8,r13,r66,r67 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Mem_access_$du_dpdk_core_a.txt -e r8,r13,r66,r67 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Mem_access_$du_dpdk_core_a.txt -e r8,r13,r66,r67 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_Mem_access_$du_dpdk_core_a.txt -e r8,r13,r66,r67 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_Mem_access_$du_worker_core_a.txt -e r8,r13,r66,r67 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Mem_access_$cu_worker_core_b.txt -e r8,r13,r66,r67 -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
 
perf stat -A --output $1_Inst_Spec_LD_ST_$cu_worker_core_a.txt -e r8,r1b,r70,r71 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_Inst_Spec_LD_ST_$cu_worker_core_a.txt -e r8,r1b,r70,r71 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_LD_ST_$du_dpdk_core_a.txt -e r8,r1b,r70,r71 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_LD_ST_$du_dpdk_core_a.txt -e r8,r1b,r70,r71 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_LD_ST_$du_dpdk_core_a.txt -e r8,r1b,r70,r71 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_LD_ST_$du_worker_core_a.txt -e r8,r1b,r70,r71 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_LD_ST_$cu_worker_core_b.txt -e r8,r1b,r70,r71 -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
 
perf stat -A --output $1_Inst_Spec_DP_ASE_$cu_worker_core_a.txt -e r8,r1b,r73,r74 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_Inst_Spec_DP_ASE_$cu_worker_core_a.txt -e r8,r1b,r73,r74 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_DP_ASE_$du_dpdk_core_a.txt -e r8,r1b,r73,r74 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_DP_ASE_$du_dpdk_core_a.txt -e r8,r1b,r73,r74 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_DP_ASE_$du_dpdk_core_a.txt -e r8,r1b,r73,r74 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_DP_ASE_$du_worker_core_a.txt -e r8,r1b,r73,r74 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_DP_ASE_$cu_worker_core_b.txt -e r8,r1b,r73,r74 -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
 
perf stat -A --output $1_Inst_Spec_VFP_Crypto_$cu_worker_core_a.txt -e r8,r1b,r75,r76,r77 -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_Inst_Spec_VFP_Crypto_$cu_worker_core_a.txt -e r8,r1b,r75,r76,r77 -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_VFP_Crypto_$du_dpdk_core_a.txt -e r8,r1b,r75,r76,r77 -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_VFP_Crypto_$du_dpdk_core_a.txt -e r8,r1b,r75,r76,r77 -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_VFP_Crypto_$du_dpdk_core_a.txt -e r8,r1b,r75,r76,r77 -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_VFP_Crypto_$du_worker_core_a.txt -e r8,r1b,r75,r76,r77 -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_VFP_Crypto_$cu_worker_core_b.txt -e r8,r1b,r75,r76,r77 -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
 
perf stat -A --output $1_Inst_Spec_BR_$cu_worker_core_a.txt -e r8,r1b,r78,r79,r7a -I $interval -C "$cu_worker_core_a" -x "," sleep $sleep_sec
#perf stat -A --output $1_Inst_Spec_BR_$cu_worker_core_a.txt -e r8,r1b,r78,r79,r7a -I $interval -C "$cu_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_BR_$du_dpdk_core_a.txt -e r8,r1b,r78,r79,r7a -I $interval -C "$du_dpdk_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_BR_$du_dpdk_core_a.txt -e r8,r1b,r78,r79,r7a -I $interval -C "$du_dpdk_core_b" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_BR_$du_dpdk_core_a.txt -e r8,r1b,r78,r79,r7a -I $interval -C "$du_dpdk_core_c" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_BR_$du_worker_core_a.txt -e r8,r1b,r78,r79,r7a -I $interval -C "$du_worker_core_a" -x "," sleep $sleep_sec
perf stat -A --output $1_Inst_Spec_BR_$cu_worker_core_b.txt -e r8,r1b,r78,r79,r7a -I $interval -C "$cu_worker_core_b" -x "," sleep $sleep_sec
```

#### Take Advantage of Arm RAL and SVE/NEON 

Arm 5G RAN Acceleration Library (ArmRAL):
To learn more about getting started with the Arm 5G RAM Acceleration Library, refer to this [learning path]
(https://learn.arm.com/learning-paths/servers-and-cloud-computing/ran/)

Port Code to Arm Scalable Vector Extension (SVE)
To learn about porting your code to use Arm SVE, refer to this [learning path] (https://learn.arm.com/learning-paths/servers-and-cloud-computing/sve/)


