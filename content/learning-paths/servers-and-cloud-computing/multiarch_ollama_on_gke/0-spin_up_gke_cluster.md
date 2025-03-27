---
title: Spin up the GKE Cluster
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Project overview

Arm CPUs are widely used in Kubernetes AI/ML use cases. In this Learning Path, you learn how to run [Ollama](https://ollama.com/) on Arm-based CPUs in a hybrid architecture (amd64 and arm64) K8s cluster.

To demonstrate this, you can bring up an initial Kubernetes cluster (depicted as "*1. Initial Cluster (amd64)*" in the image below) with an amd64 node running an Ollama Deployment and Service.

Next, as depicted by "*2. Hybrid Cluster amd64/arm64*", you'll add the arm64 node, and apply an arm64 deployment and service to it, so that you can now test both architectures together, and separately, to investigate performance. 

When you are satisfied with the arm64 performance over amd64, its easy to delete the amd64-specific node, deployment, and service, to complete the migration, as depicted in "*3. Migrated Cluster (arm64)*".

![Project Overview](images/general_flow.png)

Once you've seen how easy it is to add arm64 nodes to an existing cluster, you can apply the knowledge to experiment with arm64 nodes on other workloads in your environment.
 
### Create the cluster

1. From within the GCP Console, navigate to [Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list/overview) and click *Create*.

2. Select *Standard*->*Configure*

![Select and Configure Cluster Type](images/select_standard.png)

The *Cluster basics* tab appears.

3. For *Name*, enter *ollama-on-multiarch*
4. For *Region*, enter *us-central1*.

![Select and Configure Cluster Type](images/cluster_basics.png)

{{% notice Note %}}
Although this will work in all regions and zones where C4 and C4a instance types are supported, the `us-central1` and `us-central1-1a` regions and zones are used. For simplicity and cost savings, only one node per architecture is used. 
{{% /notice %}}

5. Click on *NODE POOLS*->*default-pool*
6. For *Name*, enter *amd64-pool*
7. For size, enter *1*
8. Select *Specify node locations*, and select *us-central1-a*

![Configure amd64 Node pool](images/x86-node-pool.png)


8. Click on *NODE POOLS*->*Nodes*
9. For *Series*, select *C4*
10. For *Machine Type*, select *c4-standard-8*

![Configure amd64 node type](images/configure-x86-note-type.png)

11. *Click* the *Create* button at the bottom of the screen.

It will take a few moments, but when the green checkmark is showing next to the `ollama-on-multiarch` cluster, you're ready to continue to test your connection to the cluster.

### Connect to the cluster

Before continuing, make sure you have *kubectl* and *gcloud* installed.  You can verify by running each command, for example, entering *gcloud* and enter:

```bash
gcloud
```
should return
```output
ERROR: (gcloud) Command name argument expected.
... 
```
and entering *kubectl* and enter should return:

```output
kubectl controls the Kubernetes cluster manager.

 Find more information at: https://kubernetes.io/docs/reference/kubectl/
...
```
If you get something similar to:

```output
command not found
```

Please follow prerequisite instructions on the first page to install the missing utilities.

With prerequisites out of the way, you will next setup your newly created K8s cluster credentials using the gcloud utility.  Enter the following in your command prompt (or cloud shell), and make sure to replace "YOUR_PROJECT_ID" with the ID of your GCP project:

```bash
export ZONE=us-central1
export CLUSTER_NAME=ollama-on-multiarch
export PROJECT_ID=YOUR_PROJECT_ID
gcloud container clusters get-credentials $CLUSTER_NAME --zone $ZONE --project $PROJECT_ID
```

If you get the message:

```output
CRITICAL: ACTION REQUIRED: gke-gcloud-auth-plugin, which is needed for continued use of kubectl, was not found or is not executable. Install gke-gcloud-auth-plugin for use with kubectl by following https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin
```
This command will resolve it:

```bash
gcloud components install gke-gcloud-auth-plugin
```

Finally, test the connection to the cluster with this command:

```commandline
kubectl cluster-info
```

If you receive a non-error response, you're successfully connected to the K8s cluster.