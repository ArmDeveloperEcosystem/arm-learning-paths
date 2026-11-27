---
title: Download the Arm-optimized model and vision projector
weight: 3
layout: learningpathall
---

## Select the model and projector

Start with the Arm AI Portal to get the most from your Arm CPU. Its model cards help you choose an optimized model by comparing throughput, memory use, and accuracy on tested hardware. For this demo, use the [Arm CPU-optimized Qwen3.5-2B model](https://developer.arm.com/ai/models/hugging-face/Arm/qwen3-5-2b-q4-k-m-ggml-llama-cpp-vivo-x300/qwen3.5-2b-q4_k_m-gguf). Arm quantized the model to Q4_K_M GGUF for inference with llama.cpp on Arm CPUs. The portal reports text-generation measurements on a vivo X300. In this exercise, the Zena vSoC runs the model with a matching vision projector that turns a gear image into input the model can process.

This model is available under the Apache-2.0 license. See the [model card](https://huggingface.co/Arm/qwen3-5-2b-q4-k-m-ggml-llama-cpp-vivo-x300/blob/ef3036fe7fd026eb7b39493d950948d3c1caf19e/README.md) for details.

Download both files in the **Zena dashboard terminal**. Keep their filenames and directory so the launcher can find them. You can rerun these commands to resume an interrupted download.

```sh
model_dir=/root/qwen/models/arm-qwen3.5-2b
base=https://huggingface.co/Arm/qwen3-5-2b-q4-k-m-ggml-llama-cpp-vivo-x300/resolve/ef3036fe7fd026eb7b39493d950948d3c1caf19e

mkdir -p "$model_dir" &&
wget -c -P "$model_dir" "$base/Qwen__Qwen3.5-2B_llamacpp_optimized.gguf" &&
wget -c -P "$model_dir" "$base/mmproj-Qwen__Qwen3.5-2B_llamacpp_optimized.gguf"
```

Verify the downloads:

```bash
cd /root/qwen/models/arm-qwen3.5-2b
sha256sum -c <<'CHECKSUMS'
7c16a9ddfc8ad0928998a29691c49a7b882e512c6b4aad52bd6a344a7bc4f1ca  Qwen__Qwen3.5-2B_llamacpp_optimized.gguf
7a2220f894239140fa054dcee25f65759d9b9850fab932eaa13674d8c513169e  mmproj-Qwen__Qwen3.5-2B_llamacpp_optimized.gguf
CHECKSUMS
```

Both lines should end in `OK`.
