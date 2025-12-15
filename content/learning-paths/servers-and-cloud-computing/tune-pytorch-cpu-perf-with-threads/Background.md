---
title: Background Information
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Background Information

A well-known tradeoff in parallel programming is choosing the right granularity of work. When multiple threads are created to perform a task, the amount of actual computation must justify the cost of coordinating those threads. For example, if a computation is split across many threads, the overhead of creating those threads and synchronizing their results through shared memory can easily outweigh any performance gains if each thread does too little work. The same principle applies to generative AI systems. 

When distribution work across multiple threads, the communication and synchronisation overhead results in more overall work required. This introduces a tradeoff between latency, time to execute a single request, and throughput, number of requests processed in a given time interval. PyTorch looks to automatically find the correct number of threads, however as we will demonstrate, in some cases you may wish to manually fine tune. 

## Multi-threading with PyTorch on CPU


The diagram below is taken from the [PyTorch documentation](https://docs.pytorch.org/docs/2.8/notes/cpu_threading_torchscript_inference.html). When running inference, PyTorch uses a thread pool. In PyTorch, we have inter-op parallelism, which is spawning threads to run separate operations in a graph in parallel (e.g., 1 thread for a matmul and another thread for a softmax). Additionally there's intra-op parallelism can be used to spawn multiple threads to work on the same operation. 

![threading-in-pytorch](./pytorch-threading.jpg)

In PyTorch, the `torch.set_num_threads()` [API](https://docs.pytorch.org/docs/stable/generated/torch.set_num_threads.html) is used to set the maximum number of threads to spawn in the Application Thread Pool. As of PyTorch 2.8.0, the default number of threads is equal to the number of CPU cores (see [PyTorch CPU Threading Documentation](https://docs.pytorch.org/docs/2.8/notes/cpu_threading_torchscript_inference.html)). PyTorch looks to find the ideal number of threads as described with the following code snippet taken from the PyTorch source code, [ParallemOpenMP.h](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/ParallelOpenMP.h).

```cpp
int64_t num_threads = omp_get_num_threads();
    if (grain_size > 0) {
      num_threads = std::min(num_threads, divup((end - begin), grain_size));
    }

...
inline int64_t divup(int64_t x, int64_t y) {
  return (x + y - 1) / y;
}
```

In PyTorch build with OpenMP, we can set the application thread pool once at runtime using the `OMP_NUM_THREADS` environment variable. The basic demonstration below will show that the default argument on many core systems may not be ideal for your workload. In the use case of running a language model with a low parameter count on a many-core CPU system, this default configuration may not be the most performant configuration. 

## Basic Example

Create a new file called `pytorch_omp_example.py` and paste in the Python script below. We are performing a matrix multiplication in eager mode on two 256-by-256 random matrices. This is clearly a very small operation but we will observe the default behaviour and print the parallel configuration using the `torch.__config__.parallel_info()` function. 

```python
import os
import time
import torch


def main():
    print(f"PyTorch version: {torch.__version__}")

    # Read OMP_NUM_THREADS from the environment
    omp_threads = os.environ.get("OMP_NUM_THREADS")
    print(f"OMP_NUM_THREADS in environment: {omp_threads}")

    # If it's set and looks like a number, use it to set PyTorch's intra-op threads
    if omp_threads and omp_threads.isdigit():
        torch.set_num_threads(int(omp_threads))

    # Show how many threads PyTorch will actually use for intra-op parallelism
    print(f"torch.get_num_threads(): {torch.get_num_threads()}\n")

    # A simple operation to illustrate parallelism:
    size = 256  
    a = torch.randn(size, size)
    b = torch.randn(size, size)

    start = time.time()
    c = a @ b  # matrix multiplication (runs in a parallel region on CPU)
    end = time.time()

    print(f"Result shape: {c.shape}")
    print(f"Matrix multiply time: {end - start:.5f} seconds")
    print(f"\nThreading Information = {torch.__config__.parallel_info()}")

if __name__ == "__main__":
    main()
```


Running the python script above you will observe the following output. As you can see the number of threads is set to core count of 96 and the time to execute is 2.24 ms. 

```bash
python pytorch_omp_example.py
```

```output
PyTorch version: 2.10.0.dev20251124
OMP_NUM_THREADS in environment: None
torch.get_num_threads(): 96

Result shape: torch.Size([256, 256])
Matrix multiply time: 0.00224 seconds

Threading Information = ATen/Parallel:
        at::get_num_threads() : 96
        at::get_num_interop_threads() : 96
OpenMP 201511 (a.k.a. OpenMP 4.5)
        omp_get_max_threads() : 96
Intel(R) MKL-DNN v3.11.0 (Git Hash 0b8a866c009b03f322e6526d7c33cfec84a4a97a)
std::thread::hardware_concurrency() : 96
Environment variables:
        OMP_NUM_THREADS : [not set]
ATen parallel backend: OpenMP
```

Now when reduce the number of OpenMP threads using the `OMP_NUM_THREADS` value and observe a reduction is matrix multiply time to 0.64 ms. 

```bash
OMP_NUM_THREADS=16 python pytorch_omp_example.py
```

```output
PyTorch version: 2.10.0.dev20251124
OMP_NUM_THREADS in environment: 16
torch.get_num_threads(): 16

Result shape: torch.Size([256, 256])
Matrix multiply time: 0.00064 seconds

Threading Information = ATen/Parallel:
        at::get_num_threads() : 16
        at::get_num_interop_threads() : 96
OpenMP 201511 (a.k.a. OpenMP 4.5)
        omp_get_max_threads() : 16
Intel(R) MKL-DNN v3.11.0 (Git Hash 0b8a866c009b03f322e6526d7c33cfec84a4a97a)
std::thread::hardware_concurrency() : 96
Environment variables:
        OMP_NUM_THREADS : 16
ATen parallel backend: OpenMP
```

We will now move on from this trivial example to a LLM. 