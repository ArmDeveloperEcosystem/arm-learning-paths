---
title: Testing Functionality and Performance
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
Now that you have a hybrid arm64/amd64 cluster running Ollama, you can kick the tires a bit and see for yourself the advantages of running on arm64 yourself!

### Using the multiarch service to run the application on any platform
In a real world scenario, you may wish to access ollama without regard to architecture, only with regard to availability.  As you are now running ollama on both amd64 and arm64, both architectures' endpoints are available via the multiarch service.

To send a request to either based on availability, try the following command:

```commandline
./model_util.sh multiarch hello
```

You should see a server response, and the pod that handled the request prefixed with the deployment, node, pod, and timestamp:

```commandline
Server response:
Ollama is running

Pod log output:
[pod/ollama-amd64-deployment-cbfc4b865-rf4p9/ollama-multiarch] 06:25:48
```

Click up arrow and enter a few times, or write a loop -- due to the sessionAffinity:None settings on the service, it should distribute the load to both architectures based on availability.  You can see which exact pod was hit by whether amd64 or arm64 is seen in the Pod log output:

```commandline
[pod/ollama-amd64-... # amd64 pod was hit
[pod/ollama-arm64-... # arm64 pod was hit
```

Now you've seen both architectures responding to a "hello world" ping.  But what about real world price/performance stats?  Load a model(s) into the ollama pods, and see for yourself!

### Load the llama3.2 model into pods

{{% notice Note %}}
The llama3.2 model is used in this demonstration.  As [Ollama supports many different models](https://ollama-operator.ayaka.io/pages/en/guide/supported-models) you are invited to modify the model_util.sh script to add/replace llama3.2 with the model(s) of your choice.
{{% /notice %}}

Ollama will host and run models, but you need to first load the model (llama3.2 in this case) before performing inference against it.  To do this, run both commands shown below:

```commandline
# for amd64
./model_util.sh amd64 pull

# for arm64
./model_util.sh arm64 pull
```
If the output ends with ```{"status":"success"}``` for each command, the model was pulled successfully.

### Seeing is believing!

Once the models have loaded into both pods, you can perform inference regardless of node architecture (multi-arch), or individually by architecture type (amd64 or arm64).

By default, the prompt hardcoded into the modelUtil.sh script is *Create a sentence that makes sense in the English language, with as many palindromes in it as possible*, but feel free to edit that if you wish.

To see the inference performance first on the amd64 pod:

```bash
./model_util.sh amd64 infer
```
should output something similar to:

```commandline
...
"prompt_eval_duration":79000000,"eval_count":72,"eval_duration":5484000000}
Tokens per second:  13.12

Pod log output:

[pod/ollama-amd64-deployment-cbfc4b865-k2gc4/ollama-multiarch] 2025-03-27T00:25:21
```

Objectively, you can see tokens per second rate measured at 6.13 (from my log output example, your actual value may vary a bit).

Next, run the same inference, but on the arm64 node, with the following command:

```bash
./model_util.sh arm64 infer
```

Visually, you should see the output streaming out a lot faster on arm64 than on amd64.  To be more objective, taking a look at the output can help us verify it was indeed faster on arm64 vs amd64:

```commandline
...
"prompt_eval_duration":70000000,"eval_count":144,"eval_duration":9861000000}
Tokens per second:  14.60

Pod log output:

[pod/ollama-arm64-deployment-678dc8556f-md222/ollama-multiarch] 2025-03-27T00:26:30
```
This shows more than a 15% performance increase of arm64 over amd64 on this workload!

### Notes on Evaluating Price/Performance

GKE amd64-based c4-standard-8, and arm64-based c4a-standard-4 instances are chosen to better compare apples to apples (core-wise; each has four cores).  Often compared similarly for memory and vCPU performance, pricing for arm64 vs other architectures is generally less expensive than that of its arm64 counterparts.  If you're interested in learning more, browse your cloud providers' VM Instance price pages for more information on the price/performance benefits of Arm CPUs for your workloads.

### Conclusion

In this learning path, you learned how to:

1. Bring up a GKE cluster with amd64 and arm64 nodes.
2. Use the same multi-architecture container image for both amd64 and arm64 Ollama deployments.
3. See inference on an arm64 node occur faster than that of a comparable amd64 node.

What's next?  You can:

* Evaluate Price/Performance by following the steps of this Learning Path on your own workloads.
* See if a full migration to Arm nodes makes sense, or to continue in a hybrid configuration.
* Phase in Arm-specific DevOps tool/operations support.
* Shut the test cluster down if you aren't using it to save money on unused cloud resources.
