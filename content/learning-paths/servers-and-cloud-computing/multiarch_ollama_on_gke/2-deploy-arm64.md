---
title: Deploy ollama Arm64 to the cluster
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
At this point we have a what many people in their K8s Arm journey start with -- a workload running on an x86 cluster!  As mentioned earlier, the easiest way to experiment with Arm in your K8s cluster is to run both architectures simultaneously, so you'll be shown how to do that next.

### Adding arm-pool
To add Arm nodes to the cluster:

1. From the Clusters menu, select *ollama-on-arm*
2. Select *Add node pool*
3. For *Name*, enter *arm-pool*
4. For *Size*, enter *1*
5. Check *Specify node locations* and select *us-central1-a*

![YAML Overview](images/arm_node_config-1.png)

6. Select the *Nodes* tab to navigate to the *Configure node settings* screen
7. Select *C4A* : *c4a-standard-4* for Machine *Configuration/Type*.

![YAML Overview](images/arm_node_config-2.png)

8. Select *Create*
9. After provisioning completes, select the newly created *arm-pool* from the *Clusters* screen to take you to the *Node pool details* page.

Note the taint GKE applies by default to the Arm Node of *NoSchedule* (if arch=arm64):

![arm node taint](images/taint_on_arm_node.png)

The nodeSelector in both Deplopyment YAMLs not only defines which architectures to run on, [but in the arm64 use case](https://cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment#schedule-with-node-selector-arm), it also adds the required toleration automatically.


```yaml
nodeSelector:
    kubernetes.io/arch: arm64 # or amd64
```

### Deployment and Service
We can now deploy the arm-based deployment.

1. Copy the following YAML, and save it to a file called x86_ollama.yaml:

```yaml
foo
```


