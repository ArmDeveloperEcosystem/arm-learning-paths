---
title: End-to-end workflow
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

So far, you've had a look at a basic workflow of one task that can be automated in the ML lifecycle. There are many more ways to use ML Ops. To showcase this, the repository contains a workflow bringing the steps together: training, testing, and finally deployment. A comparison between the two backends is collated, and the model is deployed to DockerHub using a Dockerfile.

Navigate to the _Train, Test and Deploy_ workflow and trigger it to run. The training and testing steps are run just like before. The output report is saved and parsed to show the improvement in inference time. The deployment step connects to DockerHub and pushes the model, which can then be downloaded by users from DockerHub. This way, you have full control over the environment and model, while keeping them accessible and up-to-date.

![#e2e-workflow](/images/e2e-workflow.png)

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

TODO: explain serve_model.py when updated, mention pulling from DockerHub?, update image with final workflow format
