---
title: PMU library implementation
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## arch.h
```c
/*
 * Copyright (c) 2013-2023, Arm Limited and Contributors. All rights reserved.
 * Copyright (c) 2020-2022, NVIDIA Corporation. All rights reserved.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#ifndef ARCH_H
#define ARCH_H

/* Per-CPU PMCR_EL0 definitions */
#define PMCR_EL0_RESET_VAL          0x00ULL
#define PMCR_EL0_N_SHIFT            11ULL
#define PMCR_EL0_N_MASK             0x1fULL
#define PMCR_EL0_N_BITS             (PMCR_EL0_N_MASK << PMCR_EL0_N_SHIFT)
#define PMCR_EL0_LC_BIT             (1ULL << 6)
#define PMCR_EL0_C_BIT              (1ULL << 2)
#define PMCR_EL0_P_BIT              (1ULL << 1)
#define PMCR_EL0_E_BIT              (1ULL << 0)

#define GET_PMCR_N()

/* PMCCFILTR/PMEVTYPER<n> definitions */
#define PMEVTYPERX_EL0_P_BIT        (1ULL << 31)
#define PMEVTYPERX_EL0_NSH_BIT      (1ULL << 27)
#define PMEVTYPERX_EL0_M_BIT        (1ULL << 26)
#define PMEVTYPERX_EL0_DEFAULT      0x00ULL
#define PMEVTYPERX_EL0_EVT_MASK     0x3ffULL


/* MDCR_EL3 definitions */
#define MDCR_MPMX_BIT               (1ULL << 35)
#define MDCR_MCCD_BIT               (1ULL << 34)
#define MDCR_SCCD_BIT               (1ULL << 23)
#define MDCR_SPME_BIT               (1ULL << 17)

/* MDCR_EL2 definitions */
#define MDCR_EL2_HPME_BIT           (1ULL << 7)
#define MDCR_EL2_HPMN_MASK          0x1fULL

/* CurrentEL definitions */
#define MODE_EL_SHIFT               0x2U
#define MODE_EL_MASK                0x3U
#define MODE_EL_WIDTH               0x2U
#define MODE_EL3                    0x3U
#define MODE_EL2                    0x2U
#define MODE_EL1                    0x1U
#define MODE_EL0                    0x0U

#define GET_EL(mode)                (((mode) >> MODE_EL_SHIFT) & MODE_EL_MASK)

#endif /* ARCH_H */
```

## arch_helpers.h
```c
/*
 * Copyright (c) 2013-2022, Arm Limited and Contributors. All rights reserved.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#ifndef ARCH_HELPERS_H
#define ARCH_HELPERS_H

#include <inttypes.h>
#include "arch.h"

#define u_register_t uint64_t

/**********************************************************************
 * Macros which create inline functions to read or write CPU system
 * registers
 *********************************************************************/

#define _DEFINE_SYSREG_READ_FUNC(_name, _reg_name)				\
static inline u_register_t read_ ## _name(void)					\
{																\
	u_register_t v;												\
	__asm volatile ("mrs %0, " #_reg_name : "=r" (v));			\
	return v;													\
}

#define _DEFINE_SYSREG_WRITE_FUNC(_name, _reg_name)				\
static inline void write_ ## _name(u_register_t v)				\
{																\
	__asm volatile ("msr " #_reg_name ", %0" : : "r" (v));		\
	__asm volatile ("isb");										\
}

/* Define read function for system register */
#define DEFINE_SYSREG_READ_FUNC(_name) 			\
	_DEFINE_SYSREG_READ_FUNC(_name, _name)

/* Define read & write function for system register */
#define DEFINE_SYSREG_RW_FUNCS(_name)			\
	_DEFINE_SYSREG_READ_FUNC(_name, _name)		\
	_DEFINE_SYSREG_WRITE_FUNC(_name, _name)


/* AArch64 PMU registers */
DEFINE_SYSREG_RW_FUNCS(pmcr_el0)
DEFINE_SYSREG_RW_FUNCS(pmcntenset_el0)
DEFINE_SYSREG_RW_FUNCS(pmcntenclr_el0)
DEFINE_SYSREG_RW_FUNCS(pmselr_el0)
DEFINE_SYSREG_RW_FUNCS(pmccntr_el0)
DEFINE_SYSREG_RW_FUNCS(pmxevtyper_el0)
DEFINE_SYSREG_RW_FUNCS(pmccfiltr_el0)
DEFINE_SYSREG_RW_FUNCS(pmxevcntr_el0)
DEFINE_SYSREG_RW_FUNCS(pmovsclr_el0)

/* AArch64 secure registers */
DEFINE_SYSREG_RW_FUNCS(mdcr_el3)

/* AArch64 virtualization registers */
DEFINE_SYSREG_RW_FUNCS(mdcr_el2)

/* AArch64 secial-purpose registers */
DEFINE_SYSREG_READ_FUNC(CurrentEl)

static inline unsigned int get_current_el(void)
{
	return GET_EL(read_CurrentEl());
}

#endif /* ARCH_HELPERS_H */
```
## armv8_pmuv3_events.h
```c
#ifndef ARMV8_PMUV3_EVENTS_H
#define ARMV8_PMUV3_EVENTS_H

#include <inttypes.h>

/* Describe each PMU event */
struct pmu_event {
	const int number;
	const char *name;
};

/* Describe each selected PMU event for profiling */
struct pmu_event_selected {
	struct pmu_event event;
	//For Armv8.5 and after, all pmu event counters are 64-bit
	uint64_t preval;
	uint64_t postval;
};

#endif /* ARMV8_PMUV3_EVENTS_H */
```

## armv8_pmuv3_fn.c
```c
#include "arch_helpers.h"
#include "armv8_pmuv3_fn.h"
#include <stdio.h>

static void pmuv3_configCounter(struct pmu_event_selected* evt)
{
    int n, elx;
    uint64_t event_filter;

    elx = get_current_el();

    /* Set the filtering */
    switch (elx) {
        case MODE_EL3:
            event_filter = PMEVTYPERX_EL0_P_BIT | PMEVTYPERX_EL0_M_BIT; // EL3
            break;

        case MODE_EL2:
            event_filter = PMEVTYPERX_EL0_NSH_BIT; // None-secure EL2
            break;

        default:
            event_filter = PMEVTYPERX_EL0_DEFAULT; // By default, permit counting at EL0/EL1 
            break;
    }

    for (n = 0; evt[n].event.number != -1; n++) {
        write_pmselr_el0(n); // Select the event counter
        write_pmxevtyper_el0(event_filter); // Set the filter for each event counter
    }
    write_pmccfiltr_el0(event_filter); // Set the filter for cycle counter
	
    /* Set the event to be counted by each event counter */
    for (n = 0; evt[n].event.number != -1; n++) {
        write_pmselr_el0(n); // Select the event counter
        write_pmxevtyper_el0((read_pmxevtyper_el0() & ~PMEVTYPERX_EL0_EVT_MASK) | evt[n].event.number); // Set the event to count
    }

    /* Set the initial counter value to zero */
    write_pmcr_el0(read_pmcr_el0() | PMCR_EL0_C_BIT); // Reset the cycle counter to zero
    write_pmcr_el0(read_pmcr_el0() | PMCR_EL0_P_BIT); // Reset all the event counters to zero
}

static void pmuv3_enableCounter(struct pmu_event_selected* evt)
{
    int n;

    /* Enable each counter */
    for (n = 0; evt[n].event.number != -1; n++) {
        write_pmcntenset_el0(read_pmcntenset_el0() | (1ULL << n)); // Enable event counters
    }
    write_pmcntenset_el0(read_pmcntenset_el0() | (1ULL << 31)); // Enable cycle counter 

    /* Enable global counter bit */
    write_pmcr_el0(read_pmcr_el0() | PMCR_EL0_E_BIT);
}

static void pmuv3_disableCounter(struct pmu_event_selected* evt)
{
    int n;

    /* Disable each counter */ 
    for (n = 0; evt[n].event.number != -1; n++) {
        write_pmcntenclr_el0(read_pmcntenclr_el0() | (1ULL << n)); // Disable event counter 
    }
    write_pmcntenclr_el0(read_pmcntenclr_el0() | (1ULL << 31)); // Disable cycle counter

    /* Enable global counter bit */
    write_pmcr_el0(read_pmcr_el0() & ~PMCR_EL0_E_BIT);
}

static void pmuv3_snapshot(struct pmu_event_selected* evt)
{
    int n;

    /* Acquire the counting values for cycle counter and each event counters */
    for (n = 0; evt[n].event.number != -1; n++) {
        evt[n].preval = evt[n].postval;
        write_pmselr_el0(n); // Select the event counter
        evt[n].postval = read_pmxevcntr_el0(); // Event counter value
    }
    
    evt[n].preval = evt[n].postval;
    evt[n].postval = read_pmccntr_el0(); // Cycle counter value
}

static void pmuv3_dumpResult(struct pmu_event_selected* evt)
{
    int n;
    
    printf("************************************************************\n");
    printf("               [armv8_pmuv3] Profiling Result               \n");
    printf("************************************************************\n");
    printf("PMU EVENT, PREVAL, POSTVAL, DELTA\n");
    for (n = 0; evt[n].event.number != -1; n++) {
        printf("%s,%" PRIu64 ",%" PRIu64 ",%" PRIu64 "\n", evt[n].event.name, \
                                            evt[n].preval,                    \
                                            evt[n].postval,                   \
                                            evt[n].postval - evt[n].preval);
    }
    printf("%s,%" PRIu64 ",%" PRIu64 ",%" PRIu64 "\n", evt[n].event.name,   \
                                            evt[n].preval,                  \
                                            evt[n].postval,                 \
                                            evt[n].postval - evt[n].preval);
    printf("************************************************************\n");
}


static int pmuv3_init(struct pmu_event_selected* evt)
{
    int nr_sel = 0;
    int nr_sup = 0;
    int n, elx;

    /* Check the number of selected events. If it exceeds the hardware supporting number, then stop profiling. */
    for (n = 0; evt[n].event.number != -1; n++) {
        nr_sel++;
    }

    nr_sup = (int)((read_pmcr_el0() & PMCR_EL0_N_BITS) >> PMCR_EL0_N_SHIFT);

    if (nr_sel > nr_sup) {
        printf("[armv8_pmuv3] WARNING: Hardware supports %d PMU events while %d events are selected!\r\n", nr_sup, nr_sel);
        return -1;
    }
    
    /* For Armv8.0 CPU, long cycle count enable */ 
    write_pmcr_el0(read_pmcr_el0() | PMCR_EL0_LC_BIT); 

    /* Additional system registers setting to enable counting at EL2/EL3 */
    /* Note: For Armv8.5-A and later CPUs, you have to set more bit fields 
    in MDCR_EL2 and MDCR_EL3 to enable PMU. For details, refer to the CPU TRM. */
    elx = get_current_el();

    switch (elx) {
        case MODE_EL3:
            write_mdcr_el3(MDCR_SPME_BIT); // Enable event counting in secure state
            break;

        case MODE_EL2:
            write_mdcr_el2((read_mdcr_el2() & ~MDCR_EL2_HPMN_MASK) | nr_sup); // Set all event counters in range 1
            //write_mdcr_el2(MDCR_EL2_HPME_BIT); // Enable event counters in range 2, i.e. [MDCR_EL2.HPMN, PMCR.N-1]
            break;
    }
    return 0;
}

static void pmuv3_deinit(struct pmu_event_selected* evt)
{
    int n, elx;
    uint64_t overflow_status;

    /* Check the PMU counters overflow status */
    overflow_status = read_pmovsclr_el0();

    for (n = 0; evt[n].event.number != -1; n++) {
        if ((overflow_status & (1ULL << n)) !=0) {
            printf("[armv8_pmuv3] WARNING: Counter for PMU event %s overflowed in this profiling!\r\n", evt[n].event.name);
            write_pmovsclr_el0(1ULL << n); // Clear the overflow status
        }
    }
    
    if ((overflow_status & (1ULL << 31)) !=0) {
        printf("[armv8_pmuv3] WARNING: Cycle counter overflowed in this profiling!\r\n");
        write_pmovsclr_el0(1ULL << 31); // Clear the overflow status
    } 
        
    /* By default, counting at EL2/EL3 is prohibitted in case of leaking */
    elx = get_current_el();

    switch (elx) {
        case MODE_EL3:
            write_mdcr_el3(read_mdcr_el3() & ~MDCR_SPME_BIT); // Disable event counting in secure state
            break;
    }
}

int isProfiling = 0;

void pmuv3_startProfiling(struct pmu_event_selected* evt)
{
    if(pmuv3_init(evt) == -1) {
        isProfiling = 0;
        return;
    } 

    pmuv3_configCounter(evt);
    pmuv3_enableCounter(evt);
    pmuv3_snapshot(evt);
    isProfiling = 1;
}

void pmuv3_stopProfiling(struct pmu_event_selected* evt)
{
    if (isProfiling == 1) {
        pmuv3_disableCounter(evt);
        pmuv3_snapshot(evt);
        pmuv3_dumpResult(evt);
        pmuv3_deinit(evt);
        isProfiling =0;
    }
}
```

## armv8_pmuv3_fn.h
```c
#ifndef ARMV8_PMUV3_FN_H
#define ARMV8_PMUV3_FN_H

#include "armv8_pmuv3_events.h"

void pmuv3_startProfiling(struct pmu_event_selected* evt);
void pmuv3_stopProfiling(struct pmu_event_selected* evt);

#endif /* ARMV8_PMUV3_FN_H */
```
## jevents.py
```c
#!/usr/bin/env python3

""" Convert JSON PMU events to C code for specified CPU. """
import json
import os
import subprocess
import argparse

REPO_URL = 'https://github.com/ARM-software/data.git'
LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))

def repo_init(repo_url: str, download_path: str) -> list:
    
    """ Initialize the repository and return a list of supported CPU names. """
    repo_name = repo_url.split("/")[-1].split(".")[0]
    repo_local_path = os.path.join(download_path, repo_name)

    if not os.path.exists(repo_local_path):    
        subprocess.call(["git", "clone", repo_url, repo_local_path])
    
    all_files = os.listdir(os.path.join(repo_local_path, 'pmu'))
    file_names = [os.path.splitext(file)[0] for file in all_files]
    return file_names

def parse_json(json_file: str, c_file: str) -> None:
    
    """ Parse the JSON file and generate C code. """
    try:
        with open(json_file, 'r') as input_file:
            data = json.load(input_file)
            events = data.get("events", [])
            name_code_array = [{"name": event.get("name", hex(event["code"])), "number": event["code"]} for event in events]

        with open(c_file, 'w') as output_file:
            output_file.write("#include \"armv8_pmuv3_events.h\"\r\n")
            output_file.write("/* Selected PMU Events Table */\n")
            output_file.write("struct pmu_event_selected evt_select[] = {\n")
            output_file.write("    //{ .event.name = \"BR_PRED\", .event.number = 0x12 },\n")
            output_file.write("    /* Assign event number -1 to the event counting by the cycle counter and place it at the end of the table */\n")
            output_file.write("    { .event.name = \"CYCLES\", .event.number = -1 } \n")
            output_file.write("};\r\n")
            output_file.write("/* PMU Events Mapping Table */\n")
            output_file.write(f"const struct pmu_event pmu_events_map[] = {{\n")
            output_file.writelines([f'    {{ .name = "{nc["name"]}", .number = {hex(nc["number"])} }},\n' for nc in name_code_array])
            output_file.write("};\n")

        print(c_file + " is created.")
   
    except FileNotFoundError:
        print(f"JSON file '{json_file}' does not exist!")

if __name__ == '__main__':

    cpulist = repo_init(REPO_URL, LOCAL_PATH)
    
    parser = argparse.ArgumentParser(description='Convert PMU events in JSON format to C code for specified CPU.')
    parser.add_argument('--cpu', type=str, help='CPU name')
    parser.add_argument('--list', action='store_true', help='Display the list of supporting CPU names')

    args = parser.parse_args()

    if args.list:
        print(','.join(cpulist))
    elif args.cpu:
        json_file = os.path.join(LOCAL_PATH, "data", "pmu", args.cpu + ".json")
        c_file = os.path.join(LOCAL_PATH, "armv8_pmuv3_events.c")
        parse_json(json_file,c_file)
    else:
        parser.print_help()

```