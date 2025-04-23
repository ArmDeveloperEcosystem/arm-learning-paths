---
title: With Hint
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Providing hints with posix_fadvise

The `posix_fadvise()` system call gives the Linux kernel hints about expected file access patterns to optimize I/O. The function takes the following arguments. 
- `fd`: file descriptor of the file,  
- `offset`: where the advice starts (0 = beginning),  
- `len`: how many bytes the advice applies to (0 = to the end),  
- `advice`: the expected access pattern (`POSIX_FADV_SEQUENTIAL` suggests sequential reading).

For more information on all available arguments, see the [official documentation](https://man7.org/linux/man-pages/man2/posix_fadvise.2.html)

Copy and paste the code sample below a new file called `with_hint.cpp` which includes the `posix_fadvise()` function.

```cpp
#include <iostream>
#include <fcntl.h>
#include <unistd.h>
#include <vector>
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
    int fd = open("./smallfile.bin", O_RDONLY);
    if (fd == -1) {
        std::cerr << "Error opening file\n";
        return 1;
    }

    posix_fadvise(fd, 0, 0, POSIX_FADV_SEQUENTIAL);

    const size_t bufferSize = 4096; // 4 KB
    std::vector<char> buffer(bufferSize);

    ssize_t bytesRead;
    while ((bytesRead = read(fd, buffer.data(), bufferSize)) > 0) {
        volatile char temp = buffer[0];
        (void)temp;
        usleep(10); // Simulate processing delay
    }

    close(fd);
    return 0;
}


```

Compile with the following command.

```bash
g++ with_hint.cpp -o with_hint
```

Again, run the `perf stat` command to observe the rate of cache misses. 

```bash
sudo perf stat -e cache-references,cache-misses,minor-faults,major-faults -r 9 ./with_hint
```

```output
 Performance counter stats for './with_hint' (9 runs):

         108313825      cache-references                                                        ( +-  0.28% )
           4189713      cache-misses                     #    3.87% of all cache refs           ( +-  0.68% )
               227      minor-faults                                                            ( +-  0.36% )
                 8      major-faults                                                            ( +-  8.10% 

```

### Results

Here we observe that on this run with a single line of code we are able to reduce the cache miss rate from ~4.8% to ~3.8%. This can translate to more efficient and performant software, especially if your program is synchronous and has to wait for disk accesses. 

{{% notice Please Note%}}
Since this is only a hint to the operating system and it depends on other factors such as memory pressure, memory usage, other processes etc. the behaviour on your system may be different
{{% /notice %}}