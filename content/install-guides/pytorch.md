---
additional_search_terms:
- Python
- PyTorch
- linux

layout: installtoolsall
minutes_to_complete: 15
author_primary: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://pytorch.org/docs/stable/index.html
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
test_status:
- passed
title: PyTorch
tool_install: true
weight: 1
---

[PyTorch](https://pytorch.org/) is a popular end-to-end machine learning framework for Python. It's used to build and deploy neural networks, especially around tasks such as computer vision and natural language processing (NLP).

Follow the instructions below to install and use PyTorch on Arm Linux.

{{% notice Note %}}
Anaconda provides another way to install PyTorch. Refer to the [Anaconda install guide](/install-guides/anaconda/) to find out how to use PyTorch from Anaconda. The Anaconda version of PyTorch may be older than the version available using `pip`.
{{% /notice %}}

## Before you begin

Confirm you are using an Arm Linux system by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

PyTorch requires Python 3 and can be installed with `pip`.

For Ubuntu run:

```bash
sudo apt install python-is-python3 python3-pip -y
```

For Amazon Linux run:

```console
sudo dnf install python-pip -y
alias python=python3
```

## Download and install PyTorch

To install PyTorch run:

```bash
sudo pip install torch torchvision torchaudio
```

## Get started

Test PyTorch:

Use a text editor to copy and paste the code below into a text file named `pytorch.py`

```python
import torch
print(torch.__version__)
x = torch.rand(5,3)
print(x)
exit()
```

Run the example code:

```bash
python pytorch.py
```

The expected output is similar to:

```output
2.2.0
tensor([[0.7358, 0.4406, 0.3058],
        [0.7919, 0.9060, 0.2878],
        [0.4064, 0.4203, 0.1987],
        [0.7894, 0.6234, 0.8547],
        [0.6395, 0.5062, 0.1668]])
```

To get more details about the build options for PyTorch run:

```python
python -c "import torch; print(*torch.__config__.show().split(\"\n\"), sep=\"\n\")"
```

The output will be similar to:

```output
PyTorch built with:
  - GCC 10.2
  - C++ Version: 201703
  - Intel(R) MKL-DNN v3.3.2 (Git Hash 2dc95a2ad0841e29db8b22fbccaf3e5da7992b01)
  - OpenMP 201511 (a.k.a. OpenMP 4.5)
  - LAPACK is enabled (usually provided by MKL)
  - NNPACK is enabled
  - CPU capability usage: NO AVX
  - Build settings: BLAS_INFO=open, BUILD_TYPE=Release, CXX_COMPILER=/opt/rh/devtoolset-10/root/usr/bin/c++, CXX_FLAGS= -D_GLIBCXX_USE_CXX11_ABI=0 -fabi-version=11 -fvisibility-inlines-hidden -DUSE_PTHREADPOOL -DNDEBUG -DUSE_KINETO -DLIBKINETO_NOCUPTI -DLIBKINETO_NOROCTRACER -DUSE_QNNPACK -DUSE_PYTORCH_QNNPACK -DUSE_XNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -O2 -fPIC -Wall -Wextra -Werror=return-type -Werror=non-virtual-dtor -Werror=bool-operation -Wnarrowing -Wno-missing-field-initializers -Wno-type-limits -Wno-array-bounds -Wno-unknown-pragmas -Wno-unused-parameter -Wno-unused-function -Wno-unused-result -Wno-strict-overflow -Wno-strict-aliasing -Wno-stringop-overflow -Wsuggest-override -Wno-psabi -Wno-error=pedantic -Wno-error=old-style-cast -Wno-missing-braces -fdiagnostics-color=always -faligned-new -Wno-unused-but-set-variable -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -Wno-stringop-overflow, LAPACK_INFO=open, TORCH_VERSION=2.2.0, USE_CUDA=OFF, USE_CUDNN=OFF, USE_EIGEN_FOR_BLAS=ON, USE_EXCEPTION_PTR=1, USE_GFLAGS=OFF, USE_GLOG=OFF, USE_MKL=OFF, USE_MKLDNN=ON, USE_MPI=OFF, USE_NCCL=OFF, USE_NNPACK=ON, USE_OPENMP=ON, USE_ROCM=OFF, USE_ROCM_KERNEL_ASSERT=OFF,

```

The configuration output is an advanced option to check the tools and structure used to build PyTorch.

## BFloat16 floating-point number format

Recent Arm processors support the BFloat16 (BF16) number format in PyTorch. For example, AWS Graviton3 processors support BFloat16.

To check if your system includes BFloat16, use the `lscpu` command:

```bash
lscpu | grep bf16
```

If the `Flags` are printed, you have a processor with BFloat16.

```output
Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs paca pacg dcpodp svei8mm svebf16 i8mm bf16 dgh rng
```

If the result is blank, you do not have a processor with BFloat16.

BFloat16 provides improved performance and smaller memory footprint with the same dynamic range. You may see a slight drop in model inference accuracy with BFloat16, but the impact is acceptable for the majority of applications.

You can use an environment variable to enable BFloat16:

```console
export DNNL_DEFAULT_FPMATH_MODE=BF16
```

## LRU cache capacity

LRU cache capacity is used to avoid redundant primitive creation latency overhead.

This caching feature increases memory usage. If needed, you can lower the value to reduce memory usage.

You should tune the capacity to an optimal value for your use case.

Use an environment variable to set the value. The recommended starting value is:

```console
export LRU_CACHE_CAPACITY=1024
```

## Transparent huge pages

Transparent huge pages (THP) provide an alternative method of utilizing huge pages for virtual memory. Enabling THP may result in improved performance because it reduces the overhead of Translation Lookaside Buffer (TLB) lookups by using a larger virtual memory page size.

To check if THP is available on your system, run:

```bash
cat /sys/kernel/mm/transparent_hugepage/enabled
```

The setting in brackets is your current setting.

The most common output, `madvise`, is shown below:

```output
always [madvise] never
```

If the setting is `never`, you can change to `madvise` by running:

```bash
echo madvise | sudo tee /sys/kernel/mm/transparent_hugepage/enabled
```

With `madvise` you can use an environment variable to check performance with and without THP.

To enable THP for PyTorch:

```console
export THP_MEM_ALLOC_ENABLE=1
```

## Profiling example

Use a text editor to save the code below as `profile.py`:

```python
import torch
from torch.profiler import profile, record_function, ProfilerActivity

model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)

batch_size = 64

input = torch.randn(batch_size, 3, 224, 224)

with profile(activities=[ProfilerActivity.CPU]) as prof:
        with record_function("mymodel_inference"):
            for _ in range(10):
                model(input)

print(prof.key_averages().table(sort_by="self_cpu_time_total"))
```

Run the example and check the performance information printed:

```bash
python profile.py
```

The output will be similar to:

```output
STAGE:2024-02-13 18:20:01 1981:1981 ActivityProfilerController.cpp:314] Completed Stage: Warm Up
STAGE:2024-02-13 18:20:16 1981:1981 ActivityProfilerController.cpp:320] Completed Stage: Collection
STAGE:2024-02-13 18:20:16 1981:1981 ActivityProfilerController.cpp:324] Completed Stage: Post Processing
---------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                             Name    Self CPU %      Self CPU   CPU total %     CPU total  CPU time avg    # of Calls
---------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
         aten::mkldnn_convolution        78.50%       11.266s        86.21%       12.373s      61.863ms           200
                      aten::copy_         7.59%        1.089s         7.59%        1.089s       4.950ms           220
    aten::max_pool2d_with_indices         6.24%     896.186ms         6.24%     896.186ms      89.619ms            10
          aten::native_batch_norm         5.90%     846.534ms         5.94%     852.410ms       4.262ms           200
                 aten::clamp_min_         0.57%      82.128ms         0.57%      82.128ms     483.106us           170
                mymodel_inference         0.52%      74.722ms       100.00%       14.352s       14.352s             1
                       aten::add_         0.33%      47.261ms         0.33%      47.261ms     168.789us           280
                      aten::empty         0.12%      16.709ms         0.12%      16.709ms       7.595us          2200
                aten::convolution         0.04%       5.484ms        86.27%       12.381s      61.906ms           200
                      aten::relu_         0.04%       5.041ms         0.61%      87.169ms     512.759us           170
                      aten::addmm         0.03%       4.414ms         0.03%       4.571ms     457.100us            10
               aten::_convolution         0.02%       3.173ms        86.23%       12.376s      61.878ms           200
     aten::_batch_norm_impl_index         0.02%       2.194ms         5.96%     854.955ms       4.275ms           200
                      aten::clone         0.01%       2.030ms         7.64%        1.097s       5.485ms           200
                aten::as_strided_         0.01%       2.028ms         0.01%       2.028ms      10.140us           200
                        aten::sum         0.01%       1.553ms         0.01%       1.617ms     161.700us            10
                 aten::empty_like         0.01%       1.431ms         0.06%       9.319ms      23.297us           400
                     aten::conv2d         0.01%       1.322ms        86.28%       12.382s      61.912ms           200
                 aten::batch_norm         0.01%       1.138ms         5.97%     856.093ms       4.280ms           200
                 aten::contiguous         0.01%     880.000us         7.65%        1.098s       5.489ms           200
                    aten::resize_         0.00%     535.000us         0.00%     535.000us       2.675us           200
                       aten::div_         0.00%     409.000us         0.00%     684.000us      68.400us            10
                       aten::mean         0.00%     331.000us         0.02%       2.632ms     263.200us            10
<<some output omitted>>
---------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
Self CPU time total: 14.352s
```

Experiment with the 2 environment variables for BFloat16 and THP and observe the performance differences.

You can set each variable and run the test again and observe the new profile data and run time.

You are ready to use PyTorch on Arm Linux.

Now explore the many [machine learning articles and examples using PyTorch](https://pytorch.org/tutorials/).
