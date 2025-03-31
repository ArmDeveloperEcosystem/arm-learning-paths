---
title: Test functionality and performance
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Use the multiarch service 

With your hybrid cluster running Ollama, you can now explore the advantages of running on Arm.

You may wish to access Ollama without regard to architecture.

To send a request to either architecture, based on availability, run:

```bash
./model_util.sh multiarch hello
```
The response indicates which pod handled the request, along with its deployment, node, and timestamp:

```commandline
Server response:
Ollama is running

Pod log output:
[pod/ollama-amd64-deployment-cbfc4b865-rf4p9/ollama-multiarch] 06:25:48
```

Use the command recall (up arrow) to repeat the command and observe responses from both amd64 and arm64 pods:

```output
[pod/ollama-amd64-... # amd64 pod was hit
[pod/ollama-arm64-... # arm64 pod was hit
```

With both architectures responding, you can now load an LLM to compare performance.

### Load the llama3.2 model into pods

{{% notice Note %}}
The llama3.2 model is used in this demonstration. [Ollama supports multiple different models](https://ollama-operator.ayaka.io/pages/en/guide/supported-models); you can modify the `model_util.sh` script to test others.
{{% /notice %}}

Ollama hosts and runs models, but you need to load a model before performing inference.  

To do this, run:

```bash
./model_util.sh amd64 pull
./model_util.sh arm64 pull
```

If each model returns ```{"status":"success"}``` for each command, the models loaded successfully.

### Perform inference

Once the models are loaded into both pods, you can perform inference either regardless of node architecture or individually, by architecture type (amd64 or arm64).

By default, the prompt hardcoded into the `model_util.sh` script is `Create a sentence that makes sense in the English language, with as many palindromes in it as possible`.

You can modify the prompt as desired.

Test inference on the amd64 pod:

```bash
./model_util.sh amd64 infer
```

Example output: 

```output
...
"prompt_eval_duration":79000000,"eval_count":72,"eval_duration":5484000000}
Tokens per second:  13.12

Pod log output:

[pod/ollama-amd64-deployment-cbfc4b865-k2gc4/ollama-multiarch] 2025-03-27T00:25:21
```

You can see tokens per second rate measured at 13.12 (from the log output example, your actual value might vary).

Next, run the same inference on the arm64 node with the following command:

```bash
./model_util.sh arm64 infer
```

You will notice the output streams faster on arm64 compared to amd64. Review the tokens-per-second metric to verify the performance difference.

```output
4202,72,426,13],"total_duration":13259950101,"load_duration":1257990283,"prompt_eval_count":32,"prompt_eval_duration":1431000000,"eval_count":153,"eval_duration":10570000000}
Tokens per second:  14.47

Pod log output:

[pod/ollama-arm64-deployment-678dc8556f-md222/ollama-multiarch] 2025-03-27T00:26:30
```

In this example, the output shows more than a 15% performance increase of arm64 over amd64.

## Evaluating Price and Performance

This Learning Path compared GKE amd64-based c4 against arm64-based c4a instances, both similarly specified for vCPU and memory. Typically, arm64 instances provide better cost efficiency. Check your cloud provider's pricing to confirm potential price performance advantages for your workloads.

## Summary

In this Learning Path, you learned how to:

1. Create a GKE cluster with amd64 and arm64 nodes.
2. Deploy a multi-architecture container image for both amd64 and arm64 Ollama deployments.
3. Compare inference performance between arm64 and amd64.

You can use these insights to evaluate Arm's potential advantages for your workloads.

Make sure to shutdown the test cluster and delete all resources.

