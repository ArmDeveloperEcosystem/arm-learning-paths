---
title: Spin up the GKE Cluster
weight: 1

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

Arm CPUs are widely used in traditional ML and AI use cases. In this Learning Path, you learn how to run [ollama](https://ollama.com/) on Arm-based CPUs in a hybrid architecture (x86 and Arm) K8s cluster.

To demonstrate this in a real life scenario, you're going to bring up a Kubernetes cluster with an x86 node, and add an Arm node.  Each node will be running a single ollama pod, so we'll have two pods total (one running x86, and one running Arm).  You'll run three services, one that only targets x86 pods, one that only targets Arm pods, and one that targets both x86 and Arm pods.

TODO:  IMAGE

Once you have all three services running, you'll be empowered to experiment with migration options, price/performance, applying the knowledge to other workloads in your environment as you see fit. 

## Cost to Run

TODO
 
### Create the cluster

1. From within GCP Console, navigate to [Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list/overview) and click *Create*.

2. Select *Standard*->*Configure*

![Select and Configure Cluster Type](images/select_standard.png)

The *Cluster basics* tab appears.

3. For *Name*, enter *ollama-on-arm*
4. For *Region*, enter *us-central1*.

![Select and Configure Cluster Type](images/cluster_basics.png)

{{% notice Note %}}
Although this will work in all regions and zones where C4 and C4a instance types are supported, for this demo, we use *us-central1* and *us-central1-1a* regions and zones.  In addition, with simplicity and cost savings in mind, only one node per architecture is used.. 
{{% /notice %}}

5. Click on *NODE POOLS*->*default-pool*
6. For *Name*, enter *x86-pool*
7. For size, enter *1*
8. Select *Specify node locations*, and select *us-central1-a*

![Configure x86 Node pool](images/x86-node-pool.png)


8. Click on *NODE POOLS*->*Nodes*
9. For *Series*, select *C4*
10. For *Machine Type*, select *c4-standard-4*

{{% notice Note %}}
We've chosen node types that will support one pod per node.  If you wish to run multiple pods per mode, assume each node should provide ~10GB per pod. 
{{% /notice %}}

![Configure x86 node type](images/configure-x86-note-type.png)

11. *Click* the *Create* button at the bottom of the screen.

It will take a few moments, but when the green checkmark is showing next to the ollama-on-arm cluster, you're ready to continue to the next lesson!


