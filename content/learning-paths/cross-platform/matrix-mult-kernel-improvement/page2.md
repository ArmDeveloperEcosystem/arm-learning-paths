---
title: KleidiAI micro-kernel overview
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## High-level KleidiAI details
This section aims to provide an abstracted overview of KleidiAI's components before diving into the specifics. The KleidiAI source files are publiclly accessible in this [GitLab repository](https://www.google.com). Navigate there in your web browser to follow along and understand KleidiAI's structure.

KlediAI's micro-kernels are located in the `src` directory; navigate there now. There are a set of enabling functions in the `kai_common.h` file; click on the `matmul` directory to view the micro-kernels themselves. Here you will find a set of `.c` and `.h` with long names (the names contain meaning which we will cover in context below), and one directory labeled `matmul_clip_f32_qa8dxP_qs4cxP`. 

![KleidiAI stuff](KleidiAI-src.jpg "Figure 3. KleidiAI src directory")

There are essentially two types of KleidiAI micro-kernels:
1. Pack/Quantize kernels
2. Matrix Multiplication kernels 

The files directly in the `matmul` directory are the *packing / quantizing* micro-kernel varients. The remaining files in the `matmul_clip_f32_qa8dxP_qs4cxP` directory make up the *matrix multiplication* micro-kernel varients.

Note that only one pack/quantize micro-kernel and one matrix multiply micro-kernel will be used at a time. There are multiple variets of each micro-kernel type to find an ideal speedup for a given workload. Each model and workload (for example using a [Gemma](https://huggingface.co/blog/gemma) model running text generation), has unique characteristics that certain micro-kernels are better architected to optimize for.

Before deep-diving into KleidiAI's code, it is helpful to see how KleidiAI micro-kernels interact with an GenAI model and ML Framework at a high-level. The steps below describe in words how KleidiAI modfies two input matricies to speed up matrix multiplication. The example is of an LLM chatbot (like Gemma) using the XNNPack framework, but is representative of how any ML framework integrates with KleidiAI:

### Stage 1: Input
* A user inputs their question into the chatbot, such as "What is the capital of the United States?"
* The chatbot app converts that text into a series of tokens representing that question in numerical form. 
* The LLM inference is invoked with the tokenized input, in the form of a matrix of numbers sent into the first neural network layer. 
* The input tokens, and model parameters, are commonly represented as 32-bit or 16-bit Floating Point numbers from typical off-the-shelf LLMs like Gemma or Llama.
* The XNNPack framework takes over, managing the details of the mathmatical operations inside the LLM's neural network layers. 
* XNNPack starts executing the inference. KleidiAI is called upon to perform matrix multiplication to propogate information from one neural network layer to the next.

### Stage 2: KleidiAI Quantizing & Packing micro-kernels
* XNNPack calls the KleidiAI micro-kernels to quantize and pack the input matricies: `kai_run_lhs_quant_pack_qa8dxP_f32` and `kai_run_rhs_pack_nxk_qs4cxP_qs4cxS1S0`.
* **Quantization:** KleidiAI takes in the input matricies (the previous layer's inputs and connection weights) and dynamically quantizes them from their native format, such as FP32, into INT8 for weights and INT4 for inputs.
* **Packing:** KleidiAI organizes the input matricies by packing two INT4 input numbers into an INT8 memory space. The INT8 weight numbers are also put into an INT8 memory space.
* These quantizing/packing steps ensure an LLM in any format can take advantage of the *i8mm* feature for rapid matrix multiplication.

### Stage 3: KleidiAI Matrix Multiplication micro-kernels
* XNNPack calls the KleidiAI micro-kernels to perform matrix multiplication, such as `kai_run_matmul_clip_f32_qa8dxP4X8_qs4cxP4X8_4x4x32_neon_i8mm`.
* **MatMul:** KlediAI loads the input matricies into CPU registers and performs matrix multiplication via Arm SMMLA instructions (Signed Matrix Multiply Accumulate).
* **Revert Matricies:** KleidiAI unpacks and dequantizes the result back to the native number format and sends the output matrix to XNNPack.

### Stage 4: Finish Inference and Output
* XNNPack sends the output matrix of that neural network layer into the next layer, and continues managing the entire model inference through all the LLM layers, calling KleidiAI to accelerate matrix multiplication operations, until a final output matrix is created.
* XNNPack sends the final output matrix to the chatbot app, which decodes the numerical matrix into a series of tokens representing the original question's answer.
* The chatbot then displays those tokens to the user as they stream in from multiple inferences. The end result will be something like: "The capital of the USA is Washington, D.C."
    
### Review 
Note that this overview leaves out details for the sake of brevity, but is helpful for a conceptual understanding of how KleidiAI interacts with ML Frameworks and Generative AI models.

{{% notice What LLM size to select %}}
You will likely select a pre-quantized LLM that already represents inputs and parameters in INT8 or INT4 data size to reduce the LLM memory footprint on device. KleidiAI micro-kernels will work across any LLM quantization type. Note that deploying FP32 or FP16 on a smartphone will work, but the slight advantage in perplexity is typically not worth the dramatic increase in LLM memory size. Using a pre-quantized INT4 LLM is recommended where possible. 
{{% /notice %}}

{{% notice Why model weights are quantized to INT8 but inputs are INT4 %}}
This decision optimizes a balance between computation efficiency and model accuracy. Weights represent the learned information that defines how the model interprets inputs. Because the same weights are used for any incoming inference, any inaccuracies due to lower precision can consistently and negatively impact the model's performance. 

In contrast, each inference creates new input data through network layers; if there is a small error in one input due to lower percision it only affects the result for that input, not the entire model. As a consequence, it is safer and less impactful to model accuracy to reduce the precision for inputs than for weights. This is one reason why KleidiAI increases computational efficiency while maintaining model accuracy: By quantizing weights to INT8 and inputs to INT4.
{{% /notice %}}


The next section dives into the technical specifics of how KleidiAI delivers such drastic performance uplifts by steping through a C++ example.

