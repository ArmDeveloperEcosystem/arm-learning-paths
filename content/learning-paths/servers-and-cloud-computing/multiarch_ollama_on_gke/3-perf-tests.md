---
title: Testing Functionality and Performance
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
Now that you have a hybrid arm64/amd64 cluster running ollama, you can kick the tires a bit on the ollama app its hosts, and see for yourself the price/performance advantages of running on arm64 yourself!

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

Click up arrow and enter a few times, or write a loop -- due to the sessionAffinity:None settings on the service, it should distribute the load to both architectures based on availability.

Now you've seen both architectures responding to a "hello world" ping.  But what about real world price/performance stats?  Load a model(s) into the ollama pods, and see for yourself!

### Load the llama3.2 model into pods

{{% notice Note %}}
The llama3.2 model is used in this demonstration.  As [ollama supports many different models](https://ollama-operator.ayaka.io/pages/en/guide/supported-models) you are invited to modify the model_util.sh script to add/replace llama3.2 with the model(s) of your choice.
{{% /notice %}}

ollama will host and run models, but you need to first load the model (llama3.2 in this case) before performing inference against it.  To do this, run both commands shown below:

```commandline
# for amd64
./model_util.sh amd64 pull

# for arm64
./model_util.sh arm64 pull
```
If the output ends with ```{"status":"success"}``` for each command, the model was pulled successfuly.

### Seeing is believing!

Once the models are loading into both pods, you can perform inference regardless of node architecture (multiarch), or individually by architecture type (amd64 or arm64).  

To see the performance first on the amd64 pod:

```commandline
./model_util.sh amd64 infer
```
should output something similar to:

```commandline
...
1023,13],"total_duration":15341522988,"load_duration":16209080,"prompt_eval_count":32,"prompt_eval_duration":164000000,"eval_count":93,"eval_duration":15159000000}
Total duration of 15.15.
Tokens per second:  6.13


Pod log output:
[pod/ollama-arm64-deployment-678dc8556f-mj7gm/ollama-multiarch] 06:29:14
```

Objectively, you can see a total duration of about 15s, with a tokens per second rate of 6.13.  

Next, run the same inference, but on the arm64 node, with the following command:

```commandline
./model_util.sh arm64 infer
```

Visually, you should see the output streaming out a lot faster on arm64 than on amd64.  To be more objective, taking a look at the output can help us verify it was indeed faster on arm64 vs amd64:

```commandline
4202,72,426,13],"total_duration":13259950101,"load_duration":1257990283,"prompt_eval_count":32,"prompt_eval_duration":1431000000,"eval_count":153,"eval_duration":10570000000}

Total duration of 10.57.
Tokens per second:  14.47


Pod log output:
[pod/ollama-arm64-deployment-678dc8556f-mj7gm/ollama-multiarch] 06:46:35
```
The logs prove it, not only did it run about 30% faster, but tokens per second increase by over 100%!

### Faster and Cheaper, pick two!

We chose GKE c4 and c4a instances so we could compare apples to apples.  Advertised similarly for memory and vCPU, pricing for arm64 vs other architectures is generally less expensive than that of its arm64 counterparts.  If you're interested in learning more, browse your cloud providers' VM Instance price pages for more information on the price/performance benefits of Arm CPUs for your workloads.

### Conclusion

In this learning path, you learned how to:

1. Bring up a GKE cluster with amd64 and arm64 nodes.
2. Use the same multiarchitecture container image for both amd64 and arm64 ollama deployments.
3. See how inference on arm64 is faster (and often cheaper) than that of amd64.

What's next?  You can:

#TODO CTAs from Slide Preso, TBD























