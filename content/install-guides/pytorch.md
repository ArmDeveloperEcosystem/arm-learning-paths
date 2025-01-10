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

[PyTorch](https://pytorch.org/) is a popular end-to-end machine learning framework for Python. It is used to build and deploy neural networks, especially around tasks such as computer vision and natural language processing (NLP).

Follow the instructions below to install and use PyTorch on Arm Linux.

{{% notice Note %}}
Anaconda provides another way to install PyTorch. See the [Anaconda install guide](/install-guides/anaconda/) to find out how to use PyTorch from Anaconda. The Anaconda version of PyTorch might be older than the version available using `pip`.
{{% /notice %}}

## Before you begin

Confirm that you are using an Arm Linux system by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, then you are not using an Arm computer running 64-bit Linux.

PyTorch requires Python 3, and this can be installed with `pip`. 

For Ubuntu, run:

```console
sudo apt install python-is-python3 python3-pip python3-venv -y
```

For Amazon Linux, run:

```console
sudo dnf install python-pip -y
alias python=python3
```

## Download and install PyTorch

It is recommended that you install PyTorch in your own Python virtual environment. Set up your virtual environment:

```bash 
python -m venv venv
source venv/bin/activate
```

 In your active virtual environment, install PyTorch:

```bash
pip install torch torchvision torchaudio 
```

## Get started

Test PyTorch:

Use a text editor to copy and paste the code below into a text file named `pytorch.py`:

```console
import torch
print(torch.__version__)
x = torch.rand(5,3)
print(x)
exit()
```

Run the example code:

```console
python ./pytorch.py
```

The expected output is similar to:

```output
2.5.1
tensor([[0.1334, 0.7932, 0.4396],
        [0.9409, 0.6977, 0.5904],
        [0.6951, 0.8543, 0.0748],
        [0.0293, 0.7626, 0.8668],
        [0.8832, 0.5077, 0.6830]])
```

To get more information about the build options for PyTorch, run:

```console
python -c "import torch; print(*torch.__config__.show().split(\"\n\"), sep=\"\n\")"
```

The output will be similar to:

```output
PyTorch built with:
  - GCC 10.2
  - C++ Version: 201703
  - Intel(R) MKL-DNN v3.5.3 (Git Hash 66f0cb9eb66affd2da3bf5f8d897376f04aae6af)
  - OpenMP 201511 (a.k.a. OpenMP 4.5)
  - LAPACK is enabled (usually provided by MKL)
  - NNPACK is enabled
  - CPU capability usage: NO AVX
  - Build settings: BLAS_INFO=open, BUILD_TYPE=Release, CXX_COMPILER=/opt/rh/devtoolset-10/root/usr/bin/c++, CXX_FLAGS=-ffunction-sections -fdata-sections -D_GLIBCXX_USE_CXX11_ABI=0 -fabi-version=11 -fvisibility-inlines-hidden -DUSE_PTHREADPOOL -DNDEBUG -DUSE_KINETO -DLIBKINETO_NOCUPTI -DLIBKINETO_NOROCTRACER -DLIBKINETO_NOXPUPTI=ON -DUSE_PYTORCH_QNNPACK -DUSE_XNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -O2 -fPIC -Wall -Wextra -Werror=return-type -Werror=non-virtual-dtor -Werror=bool-operation -Wnarrowing -Wno-missing-field-initializers -Wno-type-limits -Wno-array-bounds -Wno-unknown-pragmas -Wno-unused-parameter -Wno-strict-overflow -Wno-strict-aliasing -Wno-stringop-overflow -Wsuggest-override -Wno-psabi -Wno-error=old-style-cast -Wno-missing-braces -fdiagnostics-color=always -faligned-new -Wno-unused-but-set-variable -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -Wno-stringop-overflow, LAPACK_INFO=open, TORCH_VERSION=2.5.1, USE_CUDA=OFF, USE_CUDNN=OFF, USE_CUSPARSELT=OFF, USE_EXCEPTION_PTR=1, USE_GFLAGS=OFF, USE_GLOG=OFF, USE_GLOO=ON, USE_MKLDNN=ON, USE_MPI=OFF, USE_NCCL=OFF, USE_NNPACK=ON, USE_OPENMP=ON, USE_ROCM=OFF, USE_ROCM_KERNEL_ASSERT=OFF,
```
The configuration output is an advanced option to check the tools and structure used to build PyTorch. 

## BFloat16 floating-point number format

Recent Arm processors support the BFloat16 (BF16) number format in PyTorch. For example, AWS Graviton3 processors support BFloat16. 

To check if your system includes BFloat16, use the `lscpu` command:

```console
lscpu | grep bf16
```

If the `Flags` are printed, you have a processor with BFloat16.

```output
Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs paca pacg dcpodp svei8mm svebf16 i8mm bf16 dgh rng
```

If the result is blank, you do not have a processor with BFloat16.

BFloat16 provides improved performance and smaller memory footprint with the same dynamic range. You might experience a drop in model inference accuracy with BFloat16, but the impact is acceptable for the majority of applications. 

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

Transparent huge pages (THP) provide an alternative method of utilizing huge pages for virtual memory. Enabling THP might result in improved performance because it reduces the overhead of Translation Lookaside Buffer (TLB) lookups by using a larger virtual memory page size. 

To check if THP is available on your system, run:

```console
cat /sys/kernel/mm/transparent_hugepage/enabled
```

The setting in brackets is your current setting. 

The most common output, `madvise`, is shown below:

```output
always [madvise] never
```

If the setting is `never`, you can change to `madvise` by running:

```console
echo madvise | sudo tee /sys/kernel/mm/transparent_hugepage/enabled
```

With `madvise` you can use an environment variable to check performance with and without THP.

To enable THP for PyTorch:

```console
export THP_MEM_ALLOC_ENABLE=1
```

## Profiling example

To profile a [Vision Transformer (ViT) model](https://huggingface.co/google/vit-base-patch16-224), first download the transformers and datasets libraries:

```
pip install transformers datasets
``` 

Use a text editor to save the code below as `profile-vit.py`:

```python
import torch
from transformers import ViTFeatureExtractor, ViTForImageClassification
from datasets import load_dataset
from PIL import Image
from torch.profiler import profile, record_function, ProfilerActivity

# Load the feature extractor and the model
model_name = 'google/vit-base-patch16-224'
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

# Load an example image
dataset = load_dataset("huggingface/cats-image",trust_remote_code=True)
image = dataset["test"]["image"][0]

# Preprocess the image
inputs = feature_extractor(images=image, return_tensors="pt")

# Perform the inference and profile it
with profile(activities=[ProfilerActivity.CPU]) as prof:
        with record_function("mymodel_inference"):
            for _ in range(10):
              with torch.no_grad():
                outputs = model(**inputs)

# Print the predicted class
predicted_class_idx = outputs.logits.argmax(-1).item()
print(f'Predicted class: {model.config.id2label[predicted_class_idx]}') # Should be Predicted class: Egyptian cat

# Print the profile
print(prof.key_averages().table(sort_by="self_cpu_time_total"))
```

Run the example and check the performance information printed:

```console
python ./profile-vit.py
```

The output will be similar to:

```output
Predicted class: Egyptian cat
-----------------------------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                                                 Name    Self CPU %      Self CPU   CPU total %     CPU total  CPU time avg    # of Calls
-----------------------------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                                          aten::addmm        72.23%     568.371ms        74.41%     585.512ms     802.072us           730
    aten::_scaled_dot_product_flash_attention_for_cpu         9.14%      71.904ms         9.55%      75.156ms     626.296us           120
                                    mymodel_inference         7.62%      59.982ms       100.00%     786.880ms     786.880ms             1
                                          aten::copy_         2.02%      15.868ms         2.02%      15.868ms      21.444us           740
                                           aten::gelu         1.75%      13.789ms         1.75%      13.789ms     114.906us           120
                             aten::mkldnn_convolution         1.11%       8.753ms         1.24%       9.748ms     974.775us            10
                                            aten::add         1.05%       8.225ms         1.05%       8.225ms      32.899us           250
                                         aten::linear         1.03%       8.135ms        76.77%     604.078ms     827.505us           730
                              aten::native_layer_norm         0.90%       7.103ms         1.13%       8.862ms      35.449us           250
                                           aten::view         0.89%       7.002ms         0.89%       7.002ms       2.882us          2430
                                     aten::as_strided         0.36%       2.836ms         0.36%       2.836ms       1.039us          2730
                                      aten::transpose         0.27%       2.088ms         0.49%       3.849ms       2.636us          1460
                                              aten::t         0.26%       2.028ms         0.56%       4.403ms       6.032us           730
                                          aten::empty         0.24%       1.900ms         0.24%       1.900ms       1.667us          1140
                                        aten::permute         0.21%       1.630ms         0.28%       2.178ms       4.537us           480
                   aten::scaled_dot_product_attention         0.15%       1.158ms         9.70%      76.313ms     635.943us           120
                                         aten::expand         0.14%       1.086ms         0.20%       1.567ms       2.118us           740
                                     aten::layer_norm         0.12%     919.655us         1.24%       9.782ms      39.127us           250
                                        aten::reshape         0.10%     779.594us         0.28%       2.168ms       3.012us           720
                                  aten::empty_strided         0.10%     764.348us         0.10%     764.348us       6.370us           120
                                            aten::cat         0.07%     522.874us         0.08%     667.299us      66.730us            10
                                     aten::empty_like         0.06%     481.816us         0.16%       1.268ms       9.752us           130
                                   aten::resolve_conj         0.06%     444.346us         0.06%     444.346us       0.304us          1460
                                        aten::dropout         0.03%     210.185us         0.03%     210.185us       0.841us           250
                                          aten::slice         0.02%     183.588us         0.03%     223.618us       5.590us            40
                                   aten::_convolution         0.02%     142.170us         1.26%       9.890ms     988.992us            10
                                    aten::convolution         0.01%     101.953us         1.27%       9.992ms     999.187us            10
                                    aten::as_strided_         0.01%      87.084us         0.01%      87.084us       8.708us            10
                                         aten::narrow         0.01%      85.382us         0.02%     144.425us       7.221us            20
                                         aten::select         0.01%      78.064us         0.01%      84.743us       8.474us            10
                                         aten::conv2d         0.01%      59.841us         1.28%      10.052ms       1.005ms            10
                                        aten::flatten         0.01%      57.181us         0.01%     110.388us      11.039us            10
                                          aten::clone         0.01%      53.829us         0.10%     774.429us      77.443us            10
                                     aten::contiguous         0.00%      36.610us         0.10%     811.039us      81.104us            10
                                        aten::resize_         0.00%      14.708us         0.00%      14.708us       1.471us            10
-----------------------------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
Self CPU time total: 786.880ms
```

Experiment with the two environment variables for BFloat16 and THP and observe the performance differences. 

You can set each variable and run the test again and observe the new profile data and run time. 

## Profiling example with dynamic quantization

You can improve the performance of model inference with the `torch.nn.Linear` layer using dynamic quantization. This technique converts weights to 8-bit integers before inference and dynamically quantizes activations during inference, without the requirement for fine-tuning. However, it might impact the accuracy of your model.

Use a text editor to save the code below as `profile-vit-dq.py`:
```python
import torch
from transformers import ViTFeatureExtractor, ViTForImageClassification
from datasets import load_dataset
from PIL import Image
from torch.profiler import profile, record_function, ProfilerActivity

# Load the feature extractor and the model
model_name = 'google/vit-base-patch16-224'
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

# Load an example image
dataset = load_dataset("huggingface/cats-image",trust_remote_code=True)
image = dataset["test"]["image"][0]

# Preprocess the image
inputs = feature_extractor(images=image, return_tensors="pt")

# Dynamically quantize the linear layers of the model
quantized_model = torch.ao.quantization.quantize_dynamic(model,{torch.nn.Linear},dtype=torch.qint8)

# Perform the inference and profile it
with profile(activities=[ProfilerActivity.CPU]) as prof:
        with record_function("mymodel_inference"):
            for _ in range(10):
              with torch.no_grad():
                outputs = quantized_model(**inputs)

# Print the predicted class
predicted_class_idx = outputs.logits.argmax(-1).item()
print(f'Predicted class: {model.config.id2label[predicted_class_idx]}') # Should be Predicted class: Egyptian cat

# Print the profile
print(prof.key_averages().table(sort_by="self_cpu_time_total"))
```

Run the example and check the performance information printed:

```console
python ./profile-vit-dq.py
```

The output will be similar to:

```output
-----------------------------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                                                 Name    Self CPU %      Self CPU   CPU total %     CPU total  CPU time avg    # of Calls
-----------------------------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                            quantized::linear_dynamic        48.94%     310.055ms        62.53%     396.145ms     542.664us           730
                                    mymodel_inference        17.86%     113.146ms       100.00%     633.541ms     633.541ms             1
    aten::_scaled_dot_product_flash_attention_for_cpu        11.38%      72.074ms        11.91%      75.484ms     629.034us           120
                                        aten::aminmax        11.36%      71.957ms        11.47%      72.689ms      99.574us           730
                                           aten::gelu         2.37%      15.007ms         2.37%      15.007ms     125.062us           120
                                            aten::add         1.36%       8.594ms         1.36%       8.594ms      34.376us           250
                                           aten::view         1.29%       8.156ms         1.29%       8.156ms       3.356us          2430
                             aten::mkldnn_convolution         1.17%       7.436ms         1.35%       8.531ms     853.089us            10
                              aten::native_layer_norm         1.06%       6.737ms         1.35%       8.525ms      34.098us           250
                                          aten::empty         0.58%       3.682ms         0.58%       3.682ms       1.969us          1870
                                        aten::reshape         0.37%       2.334ms         1.35%       8.550ms       5.937us          1440
                                           aten::item         0.30%       1.915ms         0.46%       2.939ms       2.013us          1460
                                        aten::permute         0.30%       1.891ms         0.44%       2.814ms       5.863us           480
                                     aten::as_strided         0.27%       1.709ms         0.27%       1.709ms       1.346us          1270
                   aten::scaled_dot_product_attention         0.18%       1.121ms        12.09%      76.605ms     638.373us           120
                                      aten::transpose         0.17%       1.049ms         0.28%       1.776ms       2.432us           730
                            aten::_local_scalar_dense         0.16%       1.024ms         0.16%       1.024ms       0.701us          1460
                                     aten::layer_norm         0.14%     865.667us         1.48%       9.390ms      37.561us           250
                                  aten::empty_strided         0.13%     811.964us         0.13%     811.964us       6.766us           120
                                          aten::copy_         0.12%     757.890us         0.12%     757.890us      75.789us            10
                                          aten::fill_         0.12%     731.780us         0.12%     731.780us       0.501us          1460
                                            aten::cat         0.08%     517.355us         0.11%     666.830us      66.683us            10
                                     aten::empty_like         0.08%     479.161us         0.21%       1.316ms      10.122us           130
                                             aten::to         0.05%     296.406us         0.05%     296.406us       0.406us           730
                                        aten::dropout         0.05%     290.613us         0.05%     290.613us       1.162us           250
                                          aten::slice         0.03%     166.971us         0.03%     211.308us       5.283us            40
                                   aten::_convolution         0.02%     135.499us         1.37%       8.666ms     866.639us            10
                                         aten::narrow         0.01%      92.295us         0.02%     149.475us       7.474us            20
                                    aten::convolution         0.01%      88.323us         1.38%       8.755ms     875.471us            10
                                    aten::as_strided_         0.01%      85.516us         0.01%      85.516us       8.552us            10
                                         aten::select         0.01%      80.835us         0.01%      87.621us       8.762us            10
                                         aten::expand         0.01%      60.005us         0.01%      68.156us       6.816us            10
                                         aten::conv2d         0.01%      59.163us         1.39%       8.814ms     881.388us            10
                                          aten::clone         0.01%      50.346us         0.14%     856.423us      85.642us            10
                                        aten::flatten         0.01%      40.956us         0.01%      94.727us       9.473us            10
                                     aten::contiguous         0.00%      27.603us         0.14%     884.026us      88.403us            10
                                        aten::resize_         0.00%      14.615us         0.00%      14.615us       1.462us            10
-----------------------------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
Self CPU time total: 633.541ms
```

You should see the `quantized::linear_dynamic` layer being profiled. You can see the improvement in the model inference performance using dynamic quantization. 

You are now ready to use PyTorch on Arm Linux.

Continue learning by exploring the many [machine learning articles and examples using PyTorch](https://pytorch.org/tutorials/).
