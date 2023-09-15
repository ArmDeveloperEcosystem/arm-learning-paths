---
title: "Using PAPI for counting"
weight: 3
layout: "learningpathall"
---

## Installing PAPI

The [PAPI installation documentation](https://github.com/icl-utk-edu/papi/wiki/Downloading-and-Installing-PAPI) covers the installation of PAPI, so it will not be discussed here.

## Using PAPI to instrument counters

Below is an example of how to measure total instructions executed (INST_RETIRED: 0x08) and load instructions executed speculatively (LD_SPEC: 0x70) using PAPI. It is based on one of the examples within the [PAPI documentation]((https://github.com/icl-utk-edu/papi/wiki/)).

papi_example.c
``` c
#include <papi.h>
#include <stdio.h>
#include <stdlib.h>
#define TOT_EVENTS 2

// The function to counting through (called in main)
void code_to_measure(){
  int sum = 0;
  for(int i = 0; i < 1000000000; ++i){
    sum += 1;
  }
}

int main() {
  int retval, EventSet=PAPI_NULL;
  long_long values[TOT_EVENTS];  // Holds event counter results

  // Initialize the PAPI library 
  retval = PAPI_library_init(PAPI_VER_CURRENT);
  if (retval != PAPI_VER_CURRENT) {
    fprintf(stderr, "PAPI library init error!\n");
    exit(1);
  }

  // Create the Event Set
  if (PAPI_create_eventset(&EventSet) != PAPI_OK)
    fprintf(stderr, "Error creating event set");

  // Add Total Instructions Executed to the Event Set as preset event
  if (PAPI_add_event(EventSet, PAPI_TOT_INS) != PAPI_OK)
    fprintf(stderr, "Error adding total instructions event to event set");

  // Add Loads executed speculatively to the Event Set as native event
  if (PAPI_add_event(EventSet, 0x40000007) != PAPI_OK)
    fprintf(stderr, "Error adding speculative loads event to event set");

  // Start counting events in the Event Set
  if (PAPI_start(EventSet) != PAPI_OK)
    fprintf(stderr, "Error starting event counting");

  // Function to count through
  code_to_measure();

  // Stop the counting of events in the Event Set
  if (PAPI_stop(EventSet, values) != PAPI_OK)
    fprintf(stderr, "Error creating event set");

  // Read the events in the Event Set 
  if (PAPI_read(EventSet, values) != PAPI_OK)
    fprintf(stderr, "Error creating event set");

  printf("Instructions retired: %lld\n",values[0]);
  printf("Loads executed speculatively: %lld\n",values[1]);

  return 0;
}
```

At the top of the file, there is a function called `code_to_measure`. This is called in `main` and is the function that events will be counted through. At the top of `main`, there is a PAPI library initialization (`PAPI_library_init`). Under that initialization an EventSet is created (`PAPI_create_eventset`). The Event Set is a PAPI construct that allows for the grouping of a set of HW events that will be counted together. Once this Event Set is created, two events are added to the Event Set with a pair of calls to `PAPI_add_event`. The first call adds the PAPI preset event `PAPI_TOT_INS`. This preset event is mapped down to the Arm INST_RETIRED event (`0x08`). Preset events are included in PAPI as a convenience. It is also possible to add events using event codes. This is the case in the second call to `PAPI_add_event`. Here, the event code `0x40000007` is used. This is the PAPI event code for the Arm LD_SPEC event. However, the Arm event ID is actually `0x70`, not `0x40000007`. This is because the event code that needs to be passed into `PAPI_add_event` is a PAPI specific event code. The easiest way to get the PAPI event code is to use `papi_avail` utility as shown below.


``` console
# papi_avail -e LD_SPEC
Available PAPI preset and user defined events plus hardware information.
--------------------------------------------------------------------------------
PAPI version             : 7.0.1.0
Operating system         : Linux 5.19.0
Vendor string and code   : ARM_ARM (65, 0x41)
Model string and code    : ARM Neoverse N1 (1, 0x1)
CPU revision             : 1.000000
CPUID                    : Family/Model/Stepping 8/3340/3, 0x08/0xd0c/0x03
CPU Max MHz              : 3
CPU Min MHz              : 3
Total cores              : 64
SMT threads per core     : 1
Cores per socket         : 64
Sockets                  : 1
Cores per NUMA region    : 64
NUMA regions             : 1
Running in a VM          : no
Number Hardware Counters : 6
Max Multiplex Counters   : 384
Fast counter read (rdpmc): no
--------------------------------------------------------------------------------

Event name:                   LD_SPEC
Event Code:                   0x40000007
Number of Register Values:    0
Description:                 |Load instructions speculatively executed|

Unit Masks:
 Mask Info:                  |:u=0|monitor at user level|
 Mask Info:                  |:k=0|monitor at kernel level|
 Mask Info:                  |:h=0|monitor at hypervisor level|
 Mask Info:                  |:period=0|sampling period|
 Mask Info:                  |:freq=0|sampling frequency (Hz)|
 Mask Info:                  |:excl=0|exclusive access|
 Mask Info:                  |:mg=0|monitor guest execution|
 Mask Info:                  |:mh=0|monitor host execution|
 Mask Info:                  |:cpu=0|CPU to program|
 Mask Info:                  |:pinned=0|pin event to counters|
--------------------------------------------------------------------------------
```

As shown above, the PAPI event code for LD_SPEC is `0x40000007`. This code is mapped down to the Arm LD_SPEC event (`0x70`). After the events are added, `PAPI_start` is used to start the counters, and `PAPI_stop` is used to stop them. Any code that is executed in between these is the code that will be measured. In this example, it's the function `code_to_measre`. Finally, `PAPI_read` is called to read the counts for the events in the Event Set.

To compile `papi_example.c`, run the following command (also noted in the PAPI documentation).

``` bash
gcc papi_example.c -I/${PAPI_DIR}/include -L/${PAPI_DIR}/lib -lpapi -o papi_example
```

Below is the output of running this application. You will need to run this as root.

``` console
# ./papi_example
Instructions retired: 11000000451
Loads executed speculatively: 3000014538
```

The counter values may be different from what is shown above. This is because how and when events occur is intrinsic to the design of the CPU. The events are also dependent on the specific instructions emitted by the compiler which can change based on compiler options and the version of the compiler. Last, PAPI supports [multiplexing](https://github.com/icl-utk-edu/papi/wiki/PAPI-Multiplexing), so if you want to count more than the number of events the CPU supports, that is possible.