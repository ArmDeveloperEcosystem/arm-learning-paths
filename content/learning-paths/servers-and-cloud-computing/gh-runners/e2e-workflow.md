---
title: End-to-end workflow
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

So far, you've had a look at a basic workflow of one task that can be automated in the ML lifecycle. There are many more ways to use ML Ops. To showcase this, the repository contains a workflow bringing the steps together: training, testing, and finally deployment. A comparison between the two backends is collated, and the model is deployed to DockerHub using a Dockerfile. The workflow files for these steps are structured in the following way.

```yaml
name: Train, Test and Deploy Model

on:
  workflow_dispatch:
  push:
    branches: main

jobs:
  train-model:
    name: Train the Model
    runs-on: ubuntu-22.04-arm-os # Custom ARM64 runner
    container:
      image: armswdev/pytorch-arm-neoverse:r24.07-torch-2.3.0-openblas
      options: --user root
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Run training script
        run: python scripts/train_model.py
      - name: Upload Artifact
        uses: actions/upload-artifact@v4
        with:
          name: traffic_sign_net
          path: ${{ github.workspace }}/models/traffic_sign_net.pth
          retention-days: 5
  test-model-openblas:
    name: Test with OpenBLAS
    needs: train-model
    runs-on: ubuntu-22.04-arm-os
    container:
      image: armswdev/pytorch-arm-neoverse:r24.07-torch-2.3.0-openblas
      options: --user root
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Download model artifact
        uses: actions/download-artifact@v4
        with:
          name: traffic_sign_net
      - name: Test with OpenBLAS
        run: python scripts/test_model.py --model models/traffic_sign_net.pth | tee openblas.txt
      - name: Upload Artifact
        uses: actions/upload-artifact@v4
        with:
          name: openblas
          path: openblas.txt
          retention-days: 5
  test-model-onednn-acl:
    name: Test with Arm Compute Library
    needs: train-model
    runs-on: ubuntu-22.04-arm-os
    container:
      image: armswdev/pytorch-arm-neoverse:r24.07-torch-2.3.0-onednn-acl
      options: --user root
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Download model artifact
        uses: actions/download-artifact@v4
        with:
          name: traffic_sign_net
      - name: Test with oneDNN and Arm Compute Library
        run: python scripts/test_model.py --model models/traffic_sign_net.pth | tee acl.txt
      - name: Upload Artifact
        uses: actions/upload-artifact@v4
        with:
          name: acl
          path: acl.txt
          retention-days: 5
  compare-results:
    name: Compare Profiler Reports
    needs: [test-model-openblas, test-model-onednn-acl]
    runs-on: ubuntu-22.04-arm-os
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Download OpenBLAS artifact
        uses: actions/download-artifact@v4
        with:
          name: openblas
      - name: Download ACL artifact
        uses: actions/download-artifact@v4
        with:
          name: acl
      - name: Parse output
        run: python scripts/parse_output.py openblas.txt acl.txt
  deploy-to-dockerhub:
    name: Build and Push Docker Image to DockerHub
    needs: compare-results
    runs-on: ubuntu-22.04-arm-os
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to DockerHub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and Push Docker Image
        run: |
          docker buildx build --platform linux/arm64 -t ${{ secrets.DOCKER_USERNAME }}/gtsrb-image:latest --push .
```

These steps should look familiar from earlier parts of the learning path, and now they are put together to curate the lifecycle of our example. The training and testing steps are run like before. The output report is saved and parsed to show the improvement in inference time. The deployment step connects to DockerHub and pushes the model, which can then be downloaded by users from DockerHub. The steps depend on each other, requiring the previous one to run before the next is triggered. The dependencies should look like this after the job is run.

![#e2e-workflow](/images/e2e-workflow.png)

This way, you have full control over the environment and model, while keeping them accessible and up-to-date. Every time you push to the repository, this workflow is triggered automatically.

Navigate to the _Train, Test and Deploy_ workflow and trigger it to run.


The output of the profiler report should look something like this.

```output
-------------------------------------------------------------------------------------------------------------------------
                         ------------------        OpenBLAS results       ------------------

Accuracy of the model on the test images: 90.97%
-------------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                                 Name    Self CPU %      Self CPU   CPU total %     CPU total  CPU time avg    # of Calls
-------------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                      model_inference         2.98%     358.000us       100.00%      12.005ms      12.005ms             1
                     aten::max_pool2d         0.12%      15.000us        43.93%       5.274ms       2.637ms             2
        aten::max_pool2d_with_indices        43.81%       5.259ms        43.81%       5.259ms       2.630ms             2
                         aten::conv2d         0.11%      13.000us        28.37%       3.406ms       1.703ms             2
                    aten::convolution         0.18%      22.000us        28.26%       3.393ms       1.696ms             2
                   aten::_convolution         0.22%      27.000us        28.08%       3.371ms       1.685ms             2
    aten::_nnpack_spatial_convolution        27.75%       3.331ms        27.86%       3.344ms       1.672ms             2
                         aten::linear         0.11%      13.000us        15.53%       1.864ms     932.000us             2
                          aten::addmm        14.94%       1.794ms        15.17%       1.821ms     910.500us             2
                           aten::relu         0.14%      17.000us         9.07%       1.089ms     363.000us             3
-------------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
Self CPU time total: 12.005ms




                         ------------------  Arm Compute Library results  ------------------

Accuracy of the model on the test images: 90.97%
---------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                             Name    Self CPU %      Self CPU   CPU total %     CPU total  CPU time avg    # of Calls
---------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                  model_inference         5.30%     348.000us       100.00%       6.565ms       6.565ms             1
                     aten::conv2d         0.17%      11.000us        55.02%       3.612ms       1.806ms             2
                aten::convolution         0.35%      23.000us        54.85%       3.601ms       1.800ms             2
               aten::_convolution         0.76%      50.000us        54.50%       3.578ms       1.789ms             2
         aten::mkldnn_convolution        47.24%       3.101ms        53.16%       3.490ms       1.745ms             2
                 aten::max_pool2d         0.17%      11.000us        25.88%       1.699ms     849.500us             2
    aten::max_pool2d_with_indices        25.71%       1.688ms        25.71%       1.688ms     844.000us             2
                     aten::linear         0.21%      14.000us        10.43%     685.000us     342.500us             2
                      aten::addmm         9.55%     627.000us         9.78%     642.000us     321.000us             2
                      aten::clone         0.29%      19.000us         6.85%     450.000us     112.500us             4
---------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
Self CPU time total: 6.565ms




                         ------------------  Self CPU time total change   ------------------
Self CPU time total went from 12.005ms (OpenBLAS) to 6.565 (ACL): 54.69% change
```

Now you know how to set up MLOps workflows with GitHub Actions that run on Arm for managing all of the steps in your application's lifecycle.