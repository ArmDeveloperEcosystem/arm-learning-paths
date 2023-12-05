---
title: Motivation
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why do you need Kubernetes?
Containerization offers an excellent way to package your applications with all required dependencies. Such an approach makes your applications portable. However, you still need to run, manage, and monitor running containers. In practice, the containers can become unresponsive or fail. In such cases, you will need to restart them manually. Also, you often use containers to spin up several instances of the same application or service to balance the load. Running many containers in parallel would require you to schedule containers on several physical or virtual machines. Moreover, you would also need to distribute the incoming traffic onto underlying containers.

Here is where the Kubernetes comes into play. Specifically, Kubernetes was created to help you automate many tasks you would otherwise need to perform manually, like restarting failed containers, scheduling them on different machines, and load balancing.

Kubernetes was initially created at Google based on their experience running distributed, containerized workloads on many machines. Kubernetes has been quickly recognized as a handy tool. Since it is open-source, cloud providers also provide managed Kubernetes services, which help you use this technology relatively easily to manage your containerized workloads.

At the top level, the Kubernetes cluster comprises the control plane and compute nodes. The control plane makes global decisions about the cluster (like scheduling containers), while the compute nodes are physical or virtual machines. These machines are equipped with container runtime (like Docker), which is necessary to run containers.

In this learning path, you will learn how to create a Kubernetes cluster in Azure. This cluster will use arm64-powered Virtual Machines as compute nodes. Then, you deploy the containerized People.WebApp to this cluster. 