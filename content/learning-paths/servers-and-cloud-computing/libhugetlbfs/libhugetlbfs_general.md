---
title: "Enable libhugetlbfs"
weight: 2
layout: "learningpathall"
---

##  Introduction to libhugetlbfs
In Linux, hugepages provide larger memory blocks compared to the default page size. You can use libhugetlbfs to provide memory for application text, data, `malloc()`, and shared memory with hugepages. 

Larger memory pages benefit applications that use considerable amounts of memory which, in turn, may cause reduced performance due to a high number of TLB misses. By enabling libhugetlbfs, workloads with sizable amounts of code, data, or heap sections may see significant performance improvement.

## Install Linux packages

On Ubuntu, install the necessary packages and create a symbolic link:

```console
sudo apt-get install libhugetlbfs-dev libhugetlbfs-bin -y
sudo ln -s /usr/bin/ld.hugetlbfs /usr/share/libhugetlbfs/ld
```

## Enable hugepages

These commands must be run as the root user (use `sudo su` if needed to become the root).

For example, to enable 1000 hugepages where the hugepages size is 2 Mb (total 2 Gb of memory) use:

```console
 echo 1000 > /proc/sys/vm/nr_hugepages
 ```

To confirm the hugepages are enabled enter:

```console
cat /proc/meminfo | grep HugePages_
```

The output will be:

```output
HugePages_Total:    1000
HugePages_Free:     1000
HugePages_Rsvd:        0
HugePages_Surp:        0
```

This confirms that 1000 hugepages are available.

## Add compile options to enable libhugetlbfs

When you build an application, add the following options to the compiler flags (gcc options) and rebuild the application. The options are used in the linking stage: 

```
-B /usr/share/libhugetlbfs -Wl,--hugetlbfs-align -no-pie -Wl,--no-as-needed
```

You can use the example application below to confirm that hugepages work on your system.

Copy the code into a file named `memory.c` and save the file:

```C
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

#define NUM_PAGES   100

void *memory;  // pointer to allocated memory

// signal handler for Control-C
void sigint_handler(int sig)
{
    printf("\nControl-C (SIGINT) signal caught!\n");

    // Free the memory
    free(memory);

    printf("Exiting...\n");
    exit(0);
}

int main()
{
    // Determine the system's page size using sysconf
    long page_size = sysconf(_SC_PAGESIZE);

    if (page_size == -1)
    {
        perror("sysconf error");
        return 1;
    }

    printf("System page size is %ld\n", page_size);

    // Register a signal handler for SIGINT
    signal(SIGINT, sigint_handler);

    // Calculate the total size to allocate for NUM_PAGES
    long total_size = NUM_PAGES * page_size;

    // Allocate the memory using malloc
    memory = malloc(total_size);

    if (memory == NULL)
    {
        perror("malloc error");
        return 1;
    }

    printf("Allocated %ld bytes (%d pages) of memory.\n", total_size, NUM_PAGES);

    // Print the process ID
    printf("Process ID: %d\n", getpid());

    // Wait for Control-C
    while (1)
        sleep(1);

    return 0;
}
```

Compile the code with:

```console
gcc -B /usr/share/libhugetlbfs -Wl,--hugetlbfs-align -no-pie -Wl,--no-as-needed -o memory memory.c
```

Without the extra compiler flags regular pages will be used, but with the extra flags hugepages will be used.

## Specify hugepages when starting the application

When an application is compiled with the extra flags, you still need to add
`HUGETLB_ELFMAP=RW` before starting the application. This specifies that both READ (such as code) and WRITE (such as data) memory will be placed in hugepages.

Make sure to run the application as root. 

The general format to run any application is:

```
HUGETLB_ELFMAP=RW [application]
```

Run the example:

```console
HUGETLB_ELFMAP=RW ./memory
```

The expected output is below (the process id will be different):

```output
System page size is 4096
Allocated 409600 bytes (100 pages) of memory.
Process ID: 3812
```

The application will wait for you to press Control-C.

Leave it running and open another terminal on your system to check if hugepages are being used.

Confirm hugepages are used by checking meminfo:

```console
cat /proc/meminfo | grep HugePages_
```

The output will be similar to:

```output
HugePages_Total:    1000
HugePages_Free:      996
HugePages_Rsvd:        1
HugePages_Surp:        0
```

This confirms that 4 hugepages are in use.

You can also confirm hugepages using the process ID of the application which is printed when run.

Substitute your printed process ID in the command:

```console
cat /proc/<pid>/smaps | less
```

The output is similar to:

```output
00200000-00400000 r-xp 00000000 00:22 31138                              /dev/hugepages/libhugetlbfs.tmp.PKNdde (deleted)
Size:               2048 kB
KernelPageSize:     2048 kB
MMUPageSize:        2048 kB
Rss:                   0 kB
Pss:                   0 kB
Pss_Dirty:             0 kB
Shared_Clean:          0 kB
Shared_Dirty:          0 kB
Private_Clean:         0 kB
Private_Dirty:         0 kB
Referenced:            0 kB
Anonymous:             0 kB
LazyFree:              0 kB
AnonHugePages:         0 kB
ShmemPmdMapped:        0 kB
FilePmdMapped:         0 kB
Shared_Hugetlb:        0 kB
Private_Hugetlb:    2048 kB
Swap:                  0 kB
SwapPss:               0 kB
Locked:                0 kB
THPeligible:    0
VmFlags: rd ex mr mw me de nr ht
```

The first 3 size values show hugepages.

Use Control-C to exit the application and free the allocated memory. After the application exits 1000 hugepages are available again.

## Use the debug variable to print more information

As a learning tool, you can use the `HUGETLB_DEBUG` variable to tell libhugetlbfs to print more information. 

Run again to see the additional information:

```console
HUGETLB_ELFMAP=RW HUGETLB_DEBUG=3  ./memory
```

The output is similar to:

```output
libhugetlbfs [ip-10-0-0-32:3809]: INFO: Found pagesize 2048 kB
libhugetlbfs [ip-10-0-0-32:3809]: INFO: Detected page sizes:
libhugetlbfs [ip-10-0-0-32:3809]: INFO:    Size: 2048 kB (default)  Mount: /dev/hugepages
libhugetlbfs [ip-10-0-0-32:3809]: INFO: Parsed kernel version: [6] . [2] . [0]
libhugetlbfs [ip-10-0-0-32:3809]: INFO: Feature private_reservations is present in this kernel
libhugetlbfs [ip-10-0-0-32:3809]: INFO: Feature noreserve_safe is present in this kernel
libhugetlbfs [ip-10-0-0-32:3809]: INFO: Feature map_hugetlb is present in this kernel
libhugetlbfs [ip-10-0-0-32:3809]: INFO: Kernel has MAP_PRIVATE reservations.  Disabling heap prefaulting.
libhugetlbfs [ip-10-0-0-32:3809]: INFO: Kernel supports MAP_HUGETLB
libhugetlbfs [ip-10-0-0-32:3809]: INFO: HUGETLB_SHARE=0, sharing disabled
libhugetlbfs [ip-10-0-0-32:3809]: INFO: HUGETLB_NO_RESERVE=no, reservations enabled
libhugetlbfs [ip-10-0-0-32:3809]: INFO: Segment 0 (phdr 2): 0x200000-0x200c44  (filesz=0xc44) (prot = 0x5)
libhugetlbfs [ip-10-0-0-32:3809]: INFO: Segment 1 (phdr 3): 0x5ffde8-0x600088  (filesz=0x290) (prot = 0x3)
libhugetlbfs [ip-10-0-0-32:3809]: DEBUG: Total memsz = 0xee4, memsz of largest segment = 0xc44
libhugetlbfs [ip-10-0-0-32:3809]: INFO: libhugetlbfs version: 2.23
libhugetlbfs [ip-10-0-0-32:3810]: INFO: Mapped hugeseg at 0xffff93600000. Copying 0xc44 bytes and 0 extra bytes from 0x200000...done
libhugetlbfs [ip-10-0-0-32:3809]: INFO: Prepare succeeded
libhugetlbfs [ip-10-0-0-32:3811]: INFO: Mapped hugeseg at 0xffff93400000. Copying 0x290 bytes and 0 extra bytes from 0x5ffde8...done
libhugetlbfs [ip-10-0-0-32:3809]: INFO: Prepare succeeded
System page size is 4096
Allocated 409600 bytes (100 pages) of memory.
Process ID: 3809
```

Use Control-C to stop the application. 

You can use this procedure to enable libhugetlbfs on any application.



