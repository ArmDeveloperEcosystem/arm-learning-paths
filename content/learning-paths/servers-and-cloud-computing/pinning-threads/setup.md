---
title: Setup
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup

In this example we will be using an AWS Graviton 3 `m7g.4xlarge` instance running Ubuntu 22.04 LTS, based on the Arm Neoverse V1 architecture. If you are unfamiliar with creating a cloud instance, please refer to our [getting started learning path](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/).

This learning path is expected to work on any linux-based Arm instance with 4 or more CPU cores. The `m7g.4xlarge` instance has a uniform processor architecture so there is neglible different in memory or CPU core performance across the cores. On Linux, this can easily be checked with the following command. 

```bash
lscpu | grep -i numa
```

For our `m7g.4xlarge` all 16 cores are in the same NUMA (non-uniform memory architecture) node.

```out
NUMA node(s):                            1
NUMA node0 CPU(s):                       0-15
```

First we will demonstrate how we can pin threads easily using the `taskset` utility available in Linux. This is used to set or retrieve the CPU affinity of a running process or set the affinity of a process about to be launched. This does not require any modifications to the source code. 


## Install Prerequisites

Run the following commands:

```bash
sudo apt update && sudo apt install g++ cmake python3.12-venv -y 
```

Install Google's Microbenchmarking support library. 

```bash
# Check out the library.
git clone https://github.com/google/benchmark.git
# Go to the library root directory
cd benchmark
# Make a build directory to place the build output.
cmake -E make_directory "build"
# Generate build system files with cmake, and download any dependencies.
cmake -E chdir "build" cmake -DBENCHMARK_DOWNLOAD_DEPENDENCIES=on -DCMAKE_BUILD_TYPE=Release ../
# or, starting with CMake 3.13, use a simpler form:
# Build the library.
sudo cmake --build "build" --config Release --target install -j $(nproc)
```
If you have issues building and installing, please refer to the [official installation guide](https://github.com/google/benchmark).

Finally, you will need to install the Linux perf utility for measuring performance. We recommend using our [install guide](https://learn.arm.com/install-guides/perf/). As you may need to build from source.

## Example 1

To demonstrate a use case of CPU affinity, we will create a program that heavily utilizes all the available CPU cores. Create a file named `use_all_cores.cpp` and paste in the source code below. In this example, we are repeatedly calculating the [Leibniz equation](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80) to compute the value of Pi. This is a computationally inefficient algorithm to calculate the value of Pi and we are splitting the work across many threads. 

```bash
cd ~
touch use_all_cores.cpp && chmod 755 use_all_cores.cpp
```


```cpp
#include <vector>
#include <iostream>
#include <chrono>
#include <thread>
#include <future>

using namespace std;


double multiplethreaded_leibniz(int terms, bool use_all_cores){

    int NUM_THREADS = 2; // use 2 cores by default
    if (use_all_cores){
        NUM_THREADS = std::thread::hardware_concurrency(); // e.g., 16 for a 16-core, single-threaded processor
    }
    std::vector<double> partial_results(NUM_THREADS);


    auto calculation = [&](int thread_id){
        // Lambda function that does the calculation of the Leibniz equation
        double denominator = 0.0;
        double term = 0.0;

        for (int i = thread_id; i < terms; i += NUM_THREADS){
            if (i % 32768 == 0){
                this_thread::sleep_for(std::chrono::nanoseconds(20));
            }
            denominator = (2*i) + 1;
            if (i%2==0){
                partial_results[thread_id] += (1/denominator);
            } else{
                partial_results[thread_id] -= (1/denominator);
            }
        }
    };


    std::vector<thread> threads;
    for (int i = 0; i < NUM_THREADS; i++){
        threads.push_back(std::thread(calculation, i));
    }

    for (auto& thread: threads){
        thread.join();
    }

    // Accumulate and return final result
    double final_result = 0.0;
    for (auto& partial_result: partial_results){
        final_result += partial_result;
    }
    final_result = final_result * 4;

    return final_result;
}

int main(){

    double result = 0.0;

    auto start = std::chrono::steady_clock::now();
    for (int i = 0; i < 5; i++){
        result = multiplethreaded_leibniz((1<<29),true);
        std::cout << "iteration\t" << i << std::endl;
    }
    auto end = std::chrono::steady_clock::now();

    auto duration = std::chrono::duration_cast<chrono::milliseconds>(end-start);
    std::this_thread::sleep_for(chrono::seconds(5)); // Wait until Python script has finished before printing Answer
    std::cout << "Answer = " << result << "\t5 iterations took " << duration.count() << " milliseconds" << std::endl;

    return 0;
}
```

Compile the program with the following command. 

```bash
g++ -O2 --std=c++11 use_all_cores.cpp -o prog
```

In a separate terminal we can use the `top` utility to quickly view the utilization of each core. For example, run the following command and press the number `1`. Then we can run the program by entering `./prog`.

```bash
top -d 0.1 # then press 1 to view per core utilization
```

![CPU-utilization](./CPU-util.jpg)

As the screenshot above shows, you should observe all cores on your system being periodically utilized up to 100% and then down to idle until the program exits. In the next section we will look at how to bind this program to specific CPU cores when running alongside a single-threaded Python script.
