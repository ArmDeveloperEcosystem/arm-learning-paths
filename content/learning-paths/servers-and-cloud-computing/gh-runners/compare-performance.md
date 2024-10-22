---
title: Compare the performance of PyTorch backends
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Continuously monitoring the performance of your machine learning models in production is crucial to maintaining effectiveness over time. The performance of your ML model can change due to various factors ranging from data-related issues to environmental factors.

In this section, you will change the PyTorch backend being used to test the trained model. You will learn how to measure and continuously monitor the inference performance using your workflow.

## OneDNN with Arm Compute Library (ACL)

In the previous section, you used the PyTorch 2.3.0 Docker Image compiled with OpenBLAS from DockerHub to run your testing workflow. PyTorch can be run with other backends. You will now modify the testing workflow to use PyTorch 2.3.0 Docker Image compiled with OneDNN and the Arm Compute Library. 

The [Arm Compute Library](https://github.com/ARM-software/ComputeLibrary) is a collection of low-level machine learning functions optimized for Arm's Cortex-A and Neoverse processors and Mali GPUs. Arm-hosted GitHub runners use Arm Neoverse CPUs, which make it possible to optimize your neural networks to take advantage of processor features. ACL implements kernels, which are also known as operators or layers, using specific instructions that run faster on AArch64.

ACL is integrated into PyTorch through [oneDNN](https://github.com/oneapi-src/oneDNN), an open-source deep neural network library.

## Modify the test workflow and compare results

Two different PyTorch docker images for Arm Neoverse CPUs are available on [DockerHub](https://hub.docker.com/r/armswdev/pytorch-arm-neoverse). 

Up until this point, you used the `r24.07-torch-2.3.0-openblas` container image to run workflows. The oneDNN container image is also available to use in workflows. These images represent two different PyTorch backends which handle the PyTorch model execution.

### Change the Docker image to use oneDNN

In your browser, open and edit the file `.github/workflows/test_model.yml`.

Update the `container.image` parameter to `armswdev/pytorch-arm-neoverse:r24.07-torch-2.3.0-onednn-acl` and save the file by committing the change to the main branch:

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

### Run the test workflow

Trigger the **Test Model** job again by clicking the **Run workflow** button on the **Actions** tab.

The test workflow starts running. 

Navigate to the workflow run on the **Actions** tab, click into the job, and expand the **Run testing script** step. 

You see a change in the performance results with OneDNN and ACL kernels being used. 

The output is similar to:

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

For the ACL results, notice that the **Self CPU time total** is lower compared to the OpenBLAS run in the previous section. 

The names of the layers have also changed, where the `aten::mkldnn_convolution` is the kernel optimized to run on the Arm architecture. That operator is the main reason the inference time is improved, made possible by using ACL kernels.

In the next section, you will learn how to automate the deployment of your model.
