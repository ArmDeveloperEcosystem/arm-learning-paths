---
title: Install the model and build the inspection application
weight: 4
layout: learningpathall
---

## Select the model and projector

In the Arm AI Portal, look for **Qwen3.5 2B Q4_K_M**. Arm provides this pre-optimized GGUF for llama.cpp. The Portal evaluation covers text generation on vivo X300. Here you will use the package on a virtual SoC to inspect an image. The language model generates the response, and the matching F16 projector converts the gear image into input the language model can process. [Arm AI Portal](https://developer.arm.com/ai)

The Qwen team provides the original **Qwen3.5-2B** model. Arm publishes the Q4_K_M conversion and accompanying projector under the **Apache License 2.0**. [Original model](https://huggingface.co/Qwen/Qwen3.5-2B) · [Arm model card](https://huggingface.co/Arm/qwen3-5-2b-q4-k-m-ggml-llama-cpp-vivo-x300/blob/ef3036fe7fd026eb7b39493d950948d3c1caf19e/README.md) · [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

Download both files directly from Hugging Face in the **guest shell**. Keep their published filenames so the application launcher can find them.

```bash
mkdir -p /root/qwen/models/arm-qwen3.5-2b
cd /root/qwen/models/arm-qwen3.5-2b
repo=https://huggingface.co/Arm/qwen3-5-2b-q4-k-m-ggml-llama-cpp-vivo-x300
revision=ef3036fe7fd026eb7b39493d950948d3c1caf19e
model=Qwen__Qwen3.5-2B_llamacpp_optimized.gguf
wget -O "$model" "$repo/resolve/$revision/$model"
wget -O "mmproj-$model" "$repo/resolve/$revision/mmproj-$model"
```

Verify the files against the checksums measured on the guest.

```bash
sha256sum -c <<'CHECKSUMS'
7c16a9ddfc8ad0928998a29691c49a7b882e512c6b4aad52bd6a344a7bc4f1ca  Qwen__Qwen3.5-2B_llamacpp_optimized.gguf
7a2220f894239140fa054dcee25f65759d9b9850fab932eaa13674d8c513169e  mmproj-Qwen__Qwen3.5-2B_llamacpp_optimized.gguf
CHECKSUMS
```

Both lines should end in `OK`.

## Compile the demo

Build the detector, dashboard server, controls API, and video bridge from the application directory you copied to the guest.

```bash
cd /root/gear-inspection-demo
make -j4
```
