---
title: Example without Hint
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup

For this demonstration, connect to an Arm-based AWS `c7g.xlarge` instance running Ubuntu 24.04. Results may vary depending on which instance and kernel version you are using. At the time of writing, kernel version `6.8.0-1024-aws` was used. 

First, you need to install the linux performance measure tool, `perf`. Please follow the [installation guide](https://learn.arm.com/install-guides/perf/) for your system. 

Additionally, install a `C++` compiler with the following command. 

```bash
sudo apt update && sudo apt install g++ -y
```

Next, to understand the current cache and memory usage. Run the following command to see the cache structure.

```bash
lscpu | grep cache
```

As per the output below, each of our 4 cores has 256 KiB of level 1 data and instruction cache along with 4 MiB of slower level 2 cache with shared data and instructions. Finally we have 32 MiB of level 3 cache which is shared among our 4 CPU cores. 

```output  
L1d cache:                            256 KiB (4 instances)
L1i cache:                            256 KiB (4 instances)
L2 cache:                             4 MiB (4 instances)
L3 cache:                             32 MiB (1 instance)
```

This information will be useful to ensure our working set size cannot all fit within on-CPU cache. 

Next, check the current memory usage of an idle system with the `free -h` command. 

```output
               total        used        free      shared  buff/cache   available
Mem:           7.6Gi       779Mi       6.4Gi       952Ki       597Mi       6.8Gi
Swap:             0B          0B          0B
```

As the output above shows, we have `7.6GiB` of total memory on this instance with `779 MiB` actively used by user and kernel processes. It may look confusing how the `free` and `available` columns show different values. `Free` is memory completely unused (6.4GiB) whereas `available` includes free memory plus reclaimable cache/buffers (6.8GiB), showing what’s ready for new processes if the file system cache is reclaimed. 


## Example

First, we need to create a file on the file system. Run the command below to create a file with random bytes in the current working directory. The command writes 64 blocks of 1 MB each to a file named `smallfile.bin`. Importantly, this file is too large to fit within our 64 MiB on-CPU cache. 

```bash
dd if=/dev/urandom of=smallfile.bin bs=1M count=64
```

Next, copy and paste the following `C++` file into a new file called `no_hints.cpp`. The sample below continuously reads the random binary file created above into a 4KiB buffer. The first byte is then read and a processing is simulated with a short delay. 

Importantly, with the `drop_cache()` function, we first drop the file file system cache in memory each time this program is run so that we are running from a cold start each time. 

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <unistd.h> // for usleep
#include <cstdlib>


int drop_cache() {
    int result = system("sync && echo 3 > /proc/sys/vm/drop_caches");
    if (result != 0) {
        std::cerr << "Failed to drop caches. Are you running as root?\n";
    }
    return result;
}

int main() {
    drop_cache();
    std::ifstream file("./smallfile.bin", std::ios::binary);
    if (!file) {
        std::cerr << "Error opening file\n";
        return 1;
    }

    const size_t bufferSize = 4096; // 4 KB
    std::vector<char> buffer(bufferSize);

    while (file.read(buffer.data(), bufferSize) || file.gcount()) {
        volatile char temp = buffer[0];
        (void)temp;
        usleep(10); // Simulate processing delay
    }

    file.close();
    return 0;
}

```

Compile without any optimisations with the following command. 

```bash
g++ no_hints.cpp -o no_hints
```

To observe the cache miss ratio we can use the `perf stat` command that prints out the cache miss statistics. Repeating this multiple times allows us to observe the variation in performance. 

```bash
sudo perf stat -e cache-references,cache-misses,minor-faults,major-faults -r 9 ./no_hints
```

```output
 Performance counter stats for './read_without_fadvise_small' (9 runs):

         113047762      cache-references                                                        ( +-  0.37% )
           5407145      cache-misses                     #    4.78% of all cache refs           ( +-  0.23% )
               229      minor-faults                                                            ( +-  0.39% )
                 9      major-faults                                                            ( +-  9.80% )

           1.70040 +- 0.00224 seconds time elapsed  ( +-  0.13% )
```