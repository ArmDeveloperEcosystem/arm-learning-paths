---
title: MLOps background
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview 

In this Learning Path, you will learn how to automate an MLOps workflow using Arm-hosted GitHub runners and GitHub Actions. 

You will perform the following tasks:
- Train and test a neural network model with PyTorch.
- Compare the model inference time using two different PyTorch backends.
- Containerize the model and save it to DockerHub.
- Deploy the container image and use API calls to access the model.

## GitHub Actions

GitHub Actions is a platform that automates software development workflows, which includes Continuous Integration and Continuous Delivery (CI/CD). 

Every repository on GitHub has an **Actions** tab as shown below:

![#actions-gui](images/actions-gui.png)

GitHub Actions runs workflow files to automate processes. Workflows run when specific events occur in a GitHub repository. 

[YAML](https://yaml.org/) defines a workflow. 

Workflows specify:

* How a job is triggered.
* The running environment.
* The commands to run. 

The machine running the workflows is called a _runner_.

## Arm-hosted GitHub runners

Hosted GitHub runners are provided by GitHub, so you do not need to set up and manage cloud infrastructure. Arm-hosted GitHub runners use the Arm architecture so you can build and test software without the necessity for cross-compiling or instruction emulation.

Arm-hosted GitHub runners enable you to:

* Optimize your workflows.
* Reduce cost.
* Improve energy consumption. 

Additionally, the Arm-hosted runners are preloaded with essential tools, which makes it easier for to develop and test your applications.

Arm-hosted runners are available for Linux and Windows. This Learning Path uses Linux.

{{% notice Note %}}
You must have a Team or Enterprise Cloud plan to use Arm-hosted runners.
{{% /notice %}}

Getting started with Arm-hosted GitHub runners is straightforward. Follow the steps in [Create a new Arm-hosted runner](/learning-paths/cross-platform/github-arm-runners/runner/#how-can-i-create-an-arm-hosted-runner) to create a runner in your organization.

Once you have created the runner, use the `runs-on` syntax in your GitHub Actions workflow file to execute the workflow on Arm. 

Below is an example workflow that executes on an Arm-hosted runner named `ubuntu-22.04-arm-os`:

```yaml
name: Example workflow
on:
  workflow_dispatch:
jobs:
  example-job:
    name: Example Job
    runs-on: ubuntu-22.04-arm-os # Custom ARM64 runner
    steps:
      - name: Example step
        run: echo "This line runs on Arm!"
```


## Machine Learning Operations (MLOps)

Machine learning use cases require reliable workflows to maintain both performance and quality of output. 

There are tasks that can be automated in the ML lifecycle, such as: 
- Model training and retraining.
- Model performance analysis.
- Data storage and processing.
- Model deployment.

Developer Operations (DevOps) refers to good practices for collaboration and automation, including CI/CD. MLOps describes the area of practice where the ML application development intersects with ML system deployment and operations.

## German Traffic Sign Recognition Benchmark (GTSRB)

This Learning Path explains how to train and test a PyTorch model to perform traffic sign recognition. 

You will learn how to use the GTSRB dataset to train the model. The dataset is free to use under the [Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/) license. It contains thousands of images of traffic signs found in Germany. It has become a well-known resource to showcase ML applications. 

The GTSRB dataset is also effective for comparing the performance and accuracy of both different models, and different PyTorch backends. 

Continue to the next section to learn how to set up an end-to-end MLOps workflow using Arm-hosted GitHub runners.
