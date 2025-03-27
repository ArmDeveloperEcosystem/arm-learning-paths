---
title: Testing functionality and performance
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that you have a hybrid cluster running Ollama, you can investigate the advantages of running on Arm.

### Use the multiarch service to run the application on any platform

You may wish to access Ollama without regard to architecture.

To send a request to either based on availability, run the following command:

```bash
./model_util.sh multiarch hello
```

You see a server response, and the pod that handled the request prefixed with the deployment, node, pod, and timestamp:

```commandline
Server response:
Ollama is running

Pod log output:
[pod/ollama-amd64-deployment-cbfc4b865-rf4p9/ollama-multiarch] 06:25:48
```

Use the up arrow (command recall) and run the command multiple times in a row. 

You see which exact pod was hit, amd64 or arm64, in the pod log output:

```output
[pod/ollama-amd64-... # amd64 pod was hit
[pod/ollama-arm64-... # arm64 pod was hit
```

You see both architectures responding to a "hello world" ping.  Next try to load an LLM and investigate the performance of the Ollama pods. 

### Load the llama3.2 model into pods

{{% notice Note %}}
The llama3.2 model is used in this demonstration.  Because [Ollama supports many different models](https://ollama-operator.ayaka.io/pages/en/guide/supported-models) you can modify the `model_util.sh` script to replace llama3.2 with other models.
{{% /notice %}}

Ollama will host and run models, but you need to first load the model before performing inference.  

To do this, run the commands below:

```bash
./model_util.sh amd64 pull
./model_util.sh arm64 pull
```

If the output ends with ```{"status":"success"}``` for each command, the model was pulled successfully.

### Perform inference

Once the models are loaded into both pods, you can perform inference regardless of node architecture or individually by architecture type (amd64 or arm64).

By default, the prompt hardcoded into the `model_util.sh` script is `Create a sentence that makes sense in the English language, with as many palindromes in it as possible`, but you can change it to anything you want to try. 

To see the inference performance on the amd64 pod:

```bash
./model_util.sh amd64 infer
```

The output is similar to: 

```output
...
"prompt_eval_duration":79000000,"eval_count":72,"eval_duration":5484000000}
Tokens per second:  13.12

Pod log output:

[pod/ollama-amd64-deployment-cbfc4b865-k2gc4/ollama-multiarch] 2025-03-27T00:25:21
```

You can see tokens per second rate measured at 13.12 (from the log output example, your actual value may vary a bit).

Next, run the same inference on the arm64 node with the following command:

```bash
./model_util.sh arm64 infer
```

Visually, you see the output streaming out faster on arm64 than on amd64. Look at the output to verify it is indeed faster.

```output
4202,72,426,13],"total_duration":13259950101,"load_duration":1257990283,"prompt_eval_count":32,"prompt_eval_duration":1431000000,"eval_count":153,"eval_duration":10570000000}
Tokens per second:  14.47

Pod log output:

[pod/ollama-arm64-deployment-678dc8556f-md222/ollama-multiarch] 2025-03-27T00:26:30
```
This shows more than a 15% performance increase of arm64 over amd64 on this workload!

### Notes on Evaluating Price/Performance

### Price performance notes

We chose GKE amd64-based c4 and arm64-based c4a instances to compare similar virtual machines. Advertised similarly for memory and vCPU performance, pricing for arm64 vs other architectures is generally less expensive.  If you're interested in learning more, browse your cloud providers' virtual machine pricing to see price/performance benefits of Arm processors for your workloads.

### Summary

In this Learning Path, you learned how to:

1. Bring up a GKE cluster with amd64 and arm64 nodes.
2. Use the same multi-architecture container image for both amd64 and arm64 Ollama deployments.
3. Compare inference performance on arm64 and amd64.

You can adopt this methodology on your own workloads to see if Arm provides a price performance advantage.

Make sure to shut down the test cluster and delete the resources you used. 

