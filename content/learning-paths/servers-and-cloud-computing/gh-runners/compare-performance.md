---
title: Modify project and compare performance
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section introduces how you can use Arm software in PyTorch to enhance the neural network performance.

## OneDNN with Arm Compute Library (ACL)

The Compute Library is a collection of low-level machine learning functions optimized for Arm's Cortex-A and Neoverse processors, and the Mali GPUs. The Arm-based GitHub runner uses Neoverse, which makes it possible to optimize your neural networks even further. In a nutshell, ACL implements kernels (which you may know as the operators or layers), which uses specific instructions that run faster on Aarch64.

ACL is integrated into PyTorch through the [oneDNN engine](https://github.com/oneapi-src/oneDNN), and is enabled by default in the [PyTorch pip package](https://pypi.org/project/torch/). PyTorch can be run with other backends as well. Two [Docker images](https://hub.docker.com/r/armswdev/pytorch-arm-neoverse) with different configurations of the framework are available to easily switch between the backends, as doing so with `pip` requires a deeper understanding of the PyTorch internals.

## Compare results

You can change what backend PyTorch uses for the neural network, and observe a performance uplift for some of the operators. This is done by updating the `container` in the workflow file. To make things easier, two different Docker images are hosted on [DockerHub](https://hub.docker.com/r/armswdev/pytorch-arm-neoverse). Up until this point the `r24.07-torch-2.3.0-openblas` container has been used. The other one uses `openDNN` with ACL.

First, trigger _Test Model_ and check the job's output. The PyTorch profiler will print a table of the results, which you can compare in the next step. It should look something like this for OpenBLAS.

```output
Accuracy of the model on the test images: 90.48%
-------------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                                 Name    Self CPU %      Self CPU   CPU total %     CPU total  CPU time avg    # of Calls
-------------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                      model_inference         2.35%     332.000us       100.00%      14.141ms      14.141ms             1
                     aten::max_pool2d         0.10%      14.000us        34.06%       4.817ms       2.409ms             2
        aten::max_pool2d_with_indices        33.97%       4.803ms        33.97%       4.803ms       2.401ms             2
                         aten::linear         0.08%      11.000us        32.98%       4.663ms       2.332ms             2
                          aten::addmm        32.58%       4.607ms        32.71%       4.626ms       2.313ms             2
                         aten::conv2d         0.08%      12.000us        22.37%       3.164ms       1.582ms             2
                    aten::convolution         0.13%      19.000us        22.29%       3.152ms       1.576ms             2
                   aten::_convolution         0.21%      29.000us        22.16%       3.133ms       1.567ms             2
    aten::_nnpack_spatial_convolution        21.88%       3.094ms        21.95%       3.104ms       1.552ms             2
                           aten::relu         0.11%      15.000us         8.17%       1.155ms     385.000us             3
-------------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
Self CPU time total: 14.141ms
```

Go to `test_model.yml` in the GitHub UI. Update the `container.image` parameter to `armswdev/pytorch-arm-neoverse:r24.07-torch-2.3.0-onednn-acl` and save the file:

```yaml
jobs:
  test-model:
    name: Test the Model
    runs-on: ubuntu-22.04-arm-os # Custom ARM64 runner
    container:
      image: armswdev/pytorch-arm-neoverse:r24.07-torch-2.3.0-onednn-acl
      options: --user root
    # Steps omitted
```

Trigger the _Test Model_ job again.

For the ACL results, observe that the **Self CPU time total** is lower compared to the output above. The names of the layers have changed as well, where the `aten::mkldnn_convolution` is the kernel optimized to run on Aarch64. That operator is the main reason our inference time is improved, made possible by ACL.

```output
Accuracy of the model on the test images: 90.48%
---------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                             Name    Self CPU %      Self CPU   CPU total %     CPU total  CPU time avg    # of Calls
---------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                  model_inference         4.63%     304.000us       100.00%       6.565ms       6.565ms             1
                     aten::conv2d         0.18%      12.000us        56.92%       3.737ms       1.869ms             2
                aten::convolution         0.30%      20.000us        56.74%       3.725ms       1.863ms             2
               aten::_convolution         0.43%      28.000us        56.44%       3.705ms       1.853ms             2
         aten::mkldnn_convolution        47.02%       3.087ms        55.48%       3.642ms       1.821ms             2
                 aten::max_pool2d         0.15%      10.000us        25.51%       1.675ms     837.500us             2
    aten::max_pool2d_with_indices        25.36%       1.665ms        25.36%       1.665ms     832.500us             2
                     aten::linear         0.18%      12.000us         9.26%     608.000us     304.000us             2
                      aten::clone         0.26%      17.000us         9.08%     596.000us     149.000us             4
                      aten::addmm         8.50%     558.000us         8.71%     572.000us     286.000us             2
---------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
Self CPU time total: 6.565ms

```