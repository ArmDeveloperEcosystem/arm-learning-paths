---
title: Get started with Ray on Google Axion C4A
weight: 2

layout: "learningpathall"
---

## Explore Axion C4A Arm instances in Google Cloud

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse-V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

The C4A series provides a cost-effective alternative to x86 virtual machines while leveraging the scalability and performance benefits of the Arm architecture in Google Cloud.

To learn more, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).



## Explore Ray on Google Axion C4A (Arm Neoverse V2)

Ray is an open-source distributed computing framework designed to scale Python applications across multiple cores and nodes. It is widely used for machine learning, data processing, hyperparameter tuning, and model serving.

Ray provides a unified platform with components such as:

* **Ray Core** for parallel and distributed execution
* **Ray Train** for distributed machine learning
* **Ray Tune** for hyperparameter optimization
* **Ray Serve** for scalable model deployment

Running Ray on Google Axion C4A Arm-based infrastructure enables efficient parallel execution of workloads by leveraging multi-core CPUs and shared memory architecture. This results in improved performance per watt, reduced infrastructure costs, and better scalability for distributed applications.

Common use cases include distributed machine learning training, hyperparameter tuning, real-time inference serving, data processing pipelines, and building scalable backend services.

To learn more, visit the [Ray documentation](https://docs.ray.io/) and explore the [Ray GitHub repository](https://github.com/ray-project/ray).

## What you've accomplished and what's next

In this section, you:

* Explored Google Axion C4A Arm-based VMs and their performance advantages for distributed workloads
* Reviewed Ray components, including Ray Core, Ray Train, Ray Tune, and Ray Serve
* Understood how Arm architecture enables efficient parallel execution and scalability

Next, you'll create a firewall rule to enable remote access to the Ray Dashboard and APIs used in this Learning Path.
