---
title: Profile the firmware with PMU
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
Now, you can profile the firmware with PMU. For the specific code in the firmware you want to profile, a basic procedure is as follows.

1. Place start profiling point before the code. That is to configure, enable, and read the current value of each PMU counter as pre-profiling value.
2. Place stop profiling point after the code. That is to disable and read each PMU counter value as post-profiling value.
3. Rebuild the firmware, and run the code again. Calculate the difference between the pre-profiling and post-profiling value of each PMU counter. That is to collect the statistical profiling data.

In the PMU library, `armv8_pmuv3_fn.c` provide a reference implementation.

## Place profiling points in the firmware

You can simply add two functions named `pmuv3_startProfiling` and `pmuv3_stopProfiling` between the code you want to profile. For each profiling, pass one `pmu_event_selected` structure array as the parameter.

Depending on the number of PMU events you want to profile with, you need to profile once or multiple times. Here are two profiling examples.

### Example one

To profile the function `enable_mmu_el3` in TF-A with focusing on cache behavior, you can only select the `evt_select_cache` array for a single profiling. 

``` c
#include <armv8_pmuv3_fn.h>

extern struct pmu_event_selected evt_select_cache[];

void __init arm_bl31_plat_arch_setup(void)
{
    //...

	pmuv3_startProfiling(evt_select_cache);
	
	enable_mmu_el3(0);
	
	pmuv3_stopProfiling(evt_select_cache);

    //...
}
```

### Example two 

To know about the `crc32` workload characterization in U-Boot, you can select both the `evt_select_cache` and `evt_select_wlc` arrays. Thus, you need to profile the same code multiple times to collect all the profiling data. 

As the `do_mem_crc` function is called by a command, you can program the firmware once and repeat the profiling by entering the same command multiple times.

``` c
#include <armv8_pmuv3_fn.h>

extern struct pmu_event_selected evt_select_cache[];
extern struct pmu_event_selected evt_select_wlc[];

struct pmu_event_selected* pevt[] = {evt_select_cache,evt_select_wlc,NULL};
struct pmu_event_selected** p = pevt;

static int do_mem_crc(struct cmd_tbl *cmdtp, int flag, int argc,
		      char *const argv[])
{
	int ret = 0;

    // ...

    if(*p!=NULL) {
        pmuv3_startProfiling(*p);
    } else {
        p = pevt;
    }

    ret = hash_command("crc32", flags, cmdtp, flag, ac, av);
    
    if(*p!=NULL) {
        pmuv3_stopProfiling(*p);
        ++p;
    }

	return ret;
}
```

### Understand the profiling with PMU

The function `startProfiling` does the following things.
1. Necessary initialization for the PMU. It checks whether the number of event counters supported by the CPU's PMU is suitable for the selected events. Then, it sets the `MDCR_EL2` or `MDCR_EL3` to enable the PMU profiling at the current Exception level. This is because firmware typically runs at EL2/EL3 or in the secure state where profiling is prohibited to prevent information leakage.
2. Configure each PMU counter to profile at the current Exception level and for the selected PMU events.
3. Enable each PMU counter.
4. Read the current value of each PMU counter as the pre-profiling value.

The function `stopProfiling` does the following things.
1. Disable each PMU counter.
2. Read the current value of each PMU counter as the post-profiling values.
3. Dump the result of this profiling.
4. Necessary deinitialization for the PMU. That is to disable PMU working at the EL2/EL3 or in the secure state.
   
{{% notice Note %}}
In the PMU library, it is not considered that the code to profile may cause the PMU counters to overflow.
{{% /notice %}}

## Collect the statistical profiling result

Now you can rebuild the firmware and run it again to collect the statistical profiling result. 

For the examples mentioned in the previous part, we perform the profiling on the Juno r2 platform. The output of the profiling is as follows. 

### Example one

``` bash
************************************************************
               [armv8_pmuv3] Profiling Result
************************************************************
PMU EVENT, PREVAL, POSTVAL, DELTA
L1D_TLB_REFILL,0,2,2
L1D_CACHE_REFILL,0,8,8
L1D_CACHE,0,6,6
L2D_CACHE_REFILL,0,10,10
L2D_CACHE,0,10,10
CYCLES,1386,4293,2907
***********************************************************
```

As you can see from the output, it records the pre-profiling and post-profiling value of each selected PMU events and cycles in this profiling. Also, it caulate the differences, and record them in the column named `DELTA`.

For cortex-a53, the PMU event `L1D_TLB_REFILL` is included in the count for `L1D_CACHE_REFILL`. Thus, you may observe that the counting value for `L1D_CACHE_REFILL` is greater than that of `L1D_CACHE`.

### Example two

``` bash
CRC32 for 80000100 ... 80001123 ==> c3ac0b65
************************************************************
               [armv8_pmuv3] Profiling Result
************************************************************
PMU EVENT, PREVAL, POSTVAL, DELTA
L1D_TLB_REFILL,0,0,0
L1D_CACHE_REFILL,0,19,19
L1D_CACHE,11,80424,80413
L2D_CACHE_REFILL,0,80,80
L2D_CACHE,0,212,212
CYCLES,147,884986,884839
************************************************************

CRC32 for 80000100 ... 80001123 ==> c3ac0b65
************************************************************
               [armv8_pmuv3] Profiling Result
************************************************************
PMU EVENT, PREVAL, POSTVAL, DELTA
INST_RETIRED,13,208664,208651
LD_RETIRED,4,51346,51342
ST_RETIRED,5,23691,23686
MEM_ACCESS,15,80961,80946
BR_IMMED_RETIRED,10,43922,43912
BR_RETURN_RETIRED,0,0,0
CYCLES,170,890037,889867
************************************************************
```

As you can see from the output, the results of `cycles` for the two profiling sessions are almost the same

From the first profiling result, you can refer to the ARM-ARM to abstract some meaningful metrics as follows.

Metric                                         | Formula                       | Value
---------------------------------------------- | ----------------------------- | ------
Attributable Level 1 data cache refill rate    | L1D_CACHE_REFILL / L1D_CACHE  | <1%
Attributable Level 2 unified cache refill rate | L2D_CACHE_REFILL / L2D_CACHE  | 37.7%

From the second profiling result, you can calculate the Count instructions per cycle (IPC) as follows.

```
IPC = INST_RETIRED / CYCLES 
```

The IPC of this workload is 0.23. This is due to many `MEM_ACCESS` operations. You may also observe the workload appears to be computation-intensive.