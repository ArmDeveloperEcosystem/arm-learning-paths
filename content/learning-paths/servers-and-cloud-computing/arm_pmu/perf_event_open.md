---
title: "Using perf_event_open for counting"
weight: 4
layout: "learningpathall"
---

##  Using perf_event_open to read counters

[perf_event_open](https://www.man7.org/linux/man-pages/man2/perf_event_open.2.html) is a Linux system call specifically for interacting with HW counters. In this section, two examples will be explored. The first example shows how to read a single counter, the second example shows how to read a group of multiple counters without multiplexing. perf_event_open does not support multiplexing, you will need to implement that yourself.

### Configure a single counter

There is an example of how to use the perf_event_open system call for reading a single counter at the bottom of its [man page](https://www.man7.org/linux/man-pages/man2/perf_event_open.2.html). The example below is based on that example.

perf_event_example1.c
``` c
#include <linux/perf_event.h> /* Definition of PERF_* constants */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/syscall.h> /* Definition of SYS_* constants */
#include <unistd.h>
#include <inttypes.h>

// The function to counting through (called in main)
void code_to_measure(){
  int sum = 0;
    for(int i = 0; i < 1000000000; ++i){
      sum += 1;
    }
}

// Executes perf_event_open syscall and makes sure it is succesful or exit
static long perf_event_open(struct perf_event_attr *hw_event, pid_t pid, int cpu, int group_fd, unsigned long flags){
  int fd;
  fd = syscall(SYS_perf_event_open, hw_event, pid, cpu, group_fd, flags);
  if (fd == -1) {
    fprintf(stderr, "Error creating event");
    exit(EXIT_FAILURE);
  }

  return fd;
}

int main() {
  int fd;
  uint64_t  val;
  struct perf_event_attr  pe;

  // Configure the event to count
  memset(&pe, 0, sizeof(struct perf_event_attr));
  pe.type = PERF_TYPE_HARDWARE;
  pe.size = sizeof(struct perf_event_attr);
  pe.config = PERF_COUNT_HW_INSTRUCTIONS;
  pe.disabled = 1;
  pe.exclude_kernel = 1;   // Do not measure instructions executed in the kernel
  pe.exclude_hv = 1;  // Do not measure instructions executed in a hypervisor

  // Create the event
  fd = perf_event_open(&pe, 0, -1, -1, 0);

  //Reset counters and start counting
  ioctl(fd, PERF_EVENT_IOC_RESET, 0);
  ioctl(fd, PERF_EVENT_IOC_ENABLE, 0);
  // Example code to count through
  code_to_measure();
  // Stop counting
  ioctl(fd, PERF_EVENT_IOC_DISABLE, 0);

  // Read and print result
  read(fd, &val, sizeof(val));
  printf("Instructions retired: %"PRIu64"\n", val);

  // Clean up file descriptor
  close(fd);

  return 0;
}
```

This example is setup to count the number of instructions executed through the `code_to_measure` function. Just like in the case with PAPI, the counter is started right before the call to `code_to_measure`, and then the counter is stopped and read just after the call to `code_to_measure`. The event being counted is `PERF_COUNT_HW_INSTRUCTIONS` which maps to the Arm PMU INST_RETIRED (ID: 0x08) event. The documentation on perf_event_open lists the different preset events that can be used. It is also possible to use a raw event code if a preset doesn't exist. This will be shown in the next example. The data structure `perf_event_attr` is how the event to count is configured. This data structure has numerous fields. In the example above, the data structure is setup so that instructions executed in the kernel (or Arm exception level EL1), and instructions executed in the hypervisor (or Arm exception level EL2) will not be counted. This means that this example is only counting user space instructions executed (or Arm exception level EL0). It's strongly recommended that the man page be reviewed to understand the configuration options for event counting.

The above example can be compiled by running GCC as shown below.

``` bash
gcc perf_event_example1.c -o perf_event_example1
```

An example output of running the binary is shown below.

``` console
$ sudo ./perf_event_example1 
Instructions retired: 11000000029
```

The counter values may be different from what is shown above. This is because how and when events occur is intrinsic to the design of the CPU. The events are also dependent on the specific instructions emitted by the compiler which can change based on compiler options and the version of the compiler.

### Configure more than one counter (no multiplexing)

The man page example doesn't discuss how to group counters together so that they are measured at the same time. Counting as group makes it possible to calculate ratios like Instructions Per Cycle (IPC). Below is an example of how to do this.

perf_event_example2.c
``` c
#include <linux/perf_event.h> /* Definition of PERF_* constants */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/syscall.h> /* Definition of SYS_* constants */
#include <unistd.h>
#include <inttypes.h>
#define TOTAL_EVENTS 6

// The function to counting through (called in main)
void code_to_measure(){
  int sum = 0;
  for(int i = 0; i < 1000000000; ++i){
    sum += 1;
  }
}

// Executes perf_event_open syscall and makes sure it is succesful or exit
static long perf_event_open(struct perf_event_attr *hw_event, pid_t pid, int cpu, int group_fd, unsigned long flags){
  int fd;
  fd = syscall(SYS_perf_event_open, hw_event, pid, cpu, group_fd, flags);
  if (fd == -1) {
    fprintf(stderr, "Error creating event");
    exit(EXIT_FAILURE);
  }

  return fd;
}

// Helper function to setup a perf event structure (perf_event_attr; see man perf_open_event)
void configure_event(struct perf_event_attr *pe, uint32_t type, uint64_t config){
  memset(pe, 0, sizeof(struct perf_event_attr));
  pe->type = type;
  pe->size = sizeof(struct perf_event_attr);
  pe->config = config;
  pe->read_format = PERF_FORMAT_GROUP | PERF_FORMAT_ID;
  pe->disabled = 1;
  pe->exclude_kernel = 1;
  pe->exclude_hv = 1;
}

// Format of event data to read
// Note: This format changes depending on perf_event_attr.read_format
// See `man perf_event_open` to understand how this structure can be different depending on event config
// This read_format structure corresponds to when PERF_FORMAT_GROUP & PERF_FORMAT_ID are set
struct read_format {
  uint64_t nr;
  struct {
    uint64_t value;
    uint64_t id;
  } values[TOTAL_EVENTS];
};

int main() {
  int fd[TOTAL_EVENTS];  // fd[0] will be the group leader file descriptor
  int id[TOTAL_EVENTS];  // event ids for file descriptors
  uint64_t pe_val[TOTAL_EVENTS]; // Counter value array corresponding to fd/id array. 
  struct perf_event_attr pe[TOTAL_EVENTS];  // Configuration structure for perf events (see man perf_event_open)
  struct read_format counter_results;

  // Configure the group of PMUs to count
  configure_event(&pe[0], PERF_TYPE_HARDWARE, PERF_COUNT_HW_CPU_CYCLES);
  configure_event(&pe[1], PERF_TYPE_HARDWARE, PERF_COUNT_HW_INSTRUCTIONS);
  configure_event(&pe[2], PERF_TYPE_HARDWARE, PERF_COUNT_HW_STALLED_CYCLES_FRONTEND);
  configure_event(&pe[3], PERF_TYPE_HARDWARE, PERF_COUNT_HW_STALLED_CYCLES_BACKEND);
  configure_event(&pe[4], PERF_TYPE_RAW, 0x70);  // Count of speculative loads (see Arm PMU docs)
  configure_event(&pe[5], PERF_TYPE_RAW, 0x71);  // Count of speculative stores (see Arm PMU docs)

  // Create event group leader
  fd[0] = perf_event_open(&pe[0], 0, -1, -1, 0);
  ioctl(fd[0], PERF_EVENT_IOC_ID, &id[0]);
  // Let's create the rest of the events while using fd[0] as the group leader
  for(int i = 1; i < TOTAL_EVENTS; i++){
    fd[i] = perf_event_open(&pe[i], 0, -1, fd[0], 0);
    ioctl(fd[i], PERF_EVENT_IOC_ID, &id[i]);
  }

  // Reset counters and start counting; Since fd[0] is leader, this resets and enables all counters
  // PERF_IOC_FLAG_GROUP required for the ioctl to act on the group of file descriptors
  ioctl(fd[0], PERF_EVENT_IOC_RESET, PERF_IOC_FLAG_GROUP);
  ioctl(fd[0], PERF_EVENT_IOC_ENABLE, PERF_IOC_FLAG_GROUP);

  // Example code to count through
  code_to_measure();

  // Stop all counters
  ioctl(fd[0], PERF_EVENT_IOC_DISABLE, PERF_IOC_FLAG_GROUP);

  // Read the group of counters and print result
  read(fd[0], &counter_results, sizeof(struct read_format));
  printf("Num events captured: %"PRIu64"\n", counter_results.nr);
  for(int i = 0; i < counter_results.nr; i++) {
    for(int j = 0; j < TOTAL_EVENTS ;j++){
      if(counter_results.values[i].id == id[j]){
        pe_val[i] = counter_results.values[i].value;
      }
    }
  }
  printf("CPU cycles: %"PRIu64"\n", pe_val[0]);
  printf("Instructions retired: %"PRIu64"\n", pe_val[1]);
  printf("Frontend stall cycles: %"PRIu64"\n", pe_val[2]);
  printf("Backend stall cycles: %"PRIu64"\n", pe_val[3]);
  printf("Loads executed speculatively: %"PRIu64"\n", pe_val[4]);
  printf("Stores executed speculatively: %"PRIu64"\n", pe_val[5]);

  // Close counter file descriptors
  for(int i = 0; i < TOTAL_EVENTS; i++){
    close(fd[i]);
  }

  return 0;
}
```

Only relevant differences between this example and the previous example will be discussed. 

Towards the top of the code listing there is a data structure called `read_format`. It is setup to contain `TOTAL_EVENTS` (6 in this case) of an inner structure called `values`. This struct is populated when the group of 6 counters is read. Note that the `read_format` structure can take different forms depending on how the `perf_event_attr` structure is configured. See the man page for more information on this. Aside from `read_format`, there is also the `perf_event_attr` structure which allows configuration of each of the 6 events. This is why the `perf_event_attr` structure array called `pe` is a size of `TOTAL_EVENTS` (or 6 in this case). This means there is 1 `perf_event_attr` structure per event to count. Note, it's possible to reuse one `perf_event_attr` strucuture for setting up all events, but that is not what is done in this example. The events to count are configured using the `configure_event` function. In this example, there are 6 events to count, four are the preset events of `PERF_COUNT_HW_CPU_CYCLES`, `PERF_COUNT_HW_INSTRUCTIONS`, `PERF_COUNT_HW_STALLED_CYCLES_FRONTEND`, and `PERF_COUNT_HW_STALLED_CYCLES_BACKEND`. The last two are raw events `0x70` and `0x71` which correspond to loads executed speculatively (LD_SPEC) and stores executed speculative (ST_SPEC). Recall, these event codes (`0x70` and `0x71`) can be found in the TRM for the CPU. These last two are an example of how an event that might not have a present can be counted. Of these 6 events, one needs to be selected as the group leader. When this is done, whenever an action on the group leader is taken (like start counting), that action is taken on all of the counters in the group. This grouping mechanism is explained in the man page. The last thing that is different in this example is the `ioctl` calls that reset, start, and stop the group of counters. There is an additional flag called `PERF_IOC_FLAG_GROUP`. This is required to trigger the entire group to count. If this is missing, then only the group leader will be counted. The rest of this example is for you to study and understand.

The above example can be compiled by running GCC as shown below.

``` bash
gcc perf_event_example2.c -o perf_event_example2
```

An example output of running the binary is shown below.

``` console
$ sudo ./perf_event_example2
Num events captured: 6
CPU cycles: 5737075586
Instructions retired: 11000000029
Frontend stall cycles: 7531
Backend stall cycles: 1128970536
Loads executed speculatively: 3000014393
Stores executed speculatively: 2000009529
```

The counter values may be different from what is shown above. This is because how and when events occur is intrinsic to the design of the CPU. The events are also dependent on the specific instructions emitted by the compiler which can change based on compiler options and the version of the compiler. If you want to measure more counters than what is supported on the CPU, you will need to implement multiplexing yourself. If you choose to do this, be sure to set the `PERF_FORMAT_TOTAL_TIME_ENABLED` and `PERF_FORMAT_TOTAL_TIME_RUNNING` fields in the `perf_event_attr.read_format` structure. This is done by ORing these flags into the same line you see `PERF_FORMAT_GROUP` and `PERF_FORMAT_ID` above. If this is done, the `read_format` structure will need to be changed to include the time enabled and time running fields, see the man page for more. As noted previously, if this multiplexing is implemented, the resulting counts should be taken as an estimate.