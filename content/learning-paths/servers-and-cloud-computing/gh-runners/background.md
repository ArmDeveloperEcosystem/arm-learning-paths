---
title: Background
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this Learning Path, you will build a neural network with PyTorch. An Arm-based GitHub runner and GitHub Actions is used to run ML Ops workflows. Finally, you enable Arm software to speed up the inference, and compare the execution time for the neural network layers. With many concepts coming together in one tutorial, this section explains the main topics at a glance.

## GitHub Actions

Every repository on GitHub has a tab named _Actions_.

![#actions-gui](/images/actions-gui.png))

From here, you set up different _workflow files_ which automates CI/CD workloads in your code project. You use [YAML](https://yaml.org/) to define a workflow. You specify how a job is triggered, the running environment, and the workflow commands. The machine which the workflow runs in is called a _runner_.

## Arm-based GitHub runners

Arm-based GitHub runners are a powerful addition to your CI/CD toolkit. They leverage the efficiency and performance of Arm64 architecture, making your build systems faster and easier to scale. By using the Arm-based runners, you can optimize your workflows, reduce costs, and improve energy consumption. Additionally, the Arm-based runners are preloaded with essential tools, making it easier for you to develop and test your applications.

Getting started with Arm-based GitHub runners is straightforward. *First, you need to enable the Arm64 runners in your GitHub Actions settings. (TODO not sure exacly how they would go about this, let's update)* Then, create an Arm runner in your account. From there you use the `runs-on` syntax in your GitHub Actions workflow file to execute the workflow on Arm.

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

This setup allows you to take full advantage of the Arm64 architecture's capabilities. Whether you're working on cloud, edge, or automotive projects, these runners provide a versatile and robust solution.

## Machine Learning Operations (MLOps)

With machine learning use-cases evolving and scaling, comes an increased need for reliable workflows to maintain them. There are many regular tasks that can be automated in the ML lifecycle. Models need to be re-trained, while ensuring they still perform at their best capacity. New training data needs to be properly stored and pre-processed, and the models need to be deployed in a good production environment. Developer Operations (DevOps) refers to good practices for CI/CD. The domain-specific needs for ML, combined with state of the art DevOps knowledge, mounted the term MLOps.

## German Traffic Sign Recognition Benchmark (GTSRB)

In the field of computer vision, the GTSRB dataset which is free to use under the [Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/) license. It contains images of the traffic signs found in Germany. Thanks to the availability and real-world connection, it has become a well-known resource to showcase ML applications. Additionally, given that it is a benchmark, we can apply it in a MLOps context to compare model improvements. This makes it a great candidate for this Learning Path, where you compare the performance using two different backends of PyTorch.

With this background, let's review the code.