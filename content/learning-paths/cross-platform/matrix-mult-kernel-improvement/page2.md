---
title: KleidiAI interaction with frameworks
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## High-level KleidiAI details
This section aims to provide an abstracted overview of KleidiAI's components before diving into the specifics. The KleidiAI source files are publiclly accessible in the [KleidiAI GitLab repository](https://gitlab.arm.com/kleidi/kleidiai). Navigate there in your web browser to follow along and understand KleidiAI's structure.

KlediAI's micro-kernels are located in the `src` directory; navigate there now. There are a set of enabling functions in the `kai_common.h` file; click on the `matmul` directory to view the micro-kernels themselves. Here you will find a set of `.c` and `.h` with long names (the names contain meaning which are explained when reviewing each file). There is also and one directory labeled `matmul_clip_f32_qa8dxP_qs4cxP`. 

![KleidiAI stuff](KleidiAI-src.jpg "Figure 3. KleidiAI src directory")

There are essentially two types of KleidiAI micro-kernels:
1. Quantizing/Packing routines    - the four files in this directory.
2. Matrix Multiplication routines - the numerous files in the `matmul_clip_f32_qa8dxP_qs4cxP` directory.


{{% notice Matrix multiplication kernel selection %}}
Note that only one matrix multiply micro-kernel will be used for your given AI application. Each AI model and workload (for example using a [Gemma](https://huggingface.co/blog/gemma) model running text generation), has unique characteristics that certain KleidiAI matrix multiplication micro-kernels are better architected to optimize for. The ML Framework provider selects the optimal micro-kernel on your behalf.
{{% /notice %}}

Before deep-diving into KleidiAI's code, it is helpful to see how KleidiAI micro-kernels interact with an GenAI model and ML Framework at a high-level. The steps below describe in words how KleidiAI speeds up matrix multiplication. The example is of a user asking a chatbot app a question on their smartphone. This is the example application stack to analyze:

| Stack Component    | Description |
| -------- | ------- |
| Model     | Gemma-2b in 16-bit floating point format  |
| ML Framework | MediaPipe     |
| Backend    | XNNPack    |
| Specalized micro-kernels | KleidiAI |
| Software OS  | Android |
| Chatbot app  | Custom application |
| Hardware platform | Google Pixel 8 Pro |

This description is high-level yet generally representative of how AI models and frameworks integrate with KleidiAI:

### Stage 1: Input
* A user inputs their question into the chatbot, such as "What is the capital of the United States?"
* The chatbot app uses MediaPipe to convert that text into a series of tokens representing the question as a matrix of 16-bit floating point numbers. 
* MediaPipe invokes the LLM inference with the tokenized input, feeding it into the first neural network layer of the Gemma-2B model.
* XNNPack starts executing the inference, managing the mathmatical operations inside the LLM's neural network layers. 
* KleidiAI is called to accelerate the essential matrix multiplication operations propogating the input through the neural network.

### Stage 2: KleidiAI Quantizing & Packing micro-kernels
* XNNPack sends two matricies into KleidiAI for quantizing/packing to prepare for efficient matrix multiplication:
    * Left-hand side matrix (LHS): The previous layer's inputs. Processed in `kai_run_lhs_quant_pack_qa8dxP_f32`.
    * Right-hand side matrix (RHS): The connection weights between the layers. Processed in `kai_run_rhs_pack_nxk_qs4cxP_qs4cxS1S0`.
* KleidiAI quantizes the two matricies from FP16. Inputs are quantized into INT8. Weights are quantized into INT4.
* KleidiAI packs each individual input and weight number into an INT8 memory space to take advantage of the *i8mm* architecture feature.

### Stage 3: KleidiAI Matrix Multiplication micro-kernels
* XNNPack sends the prepared matricies into KleidiAI for matrix multiplication, selecting the matmul routine `kai_run_matmul_clip_f32_qa8dxP4X8_qs4cxP4X8_4x4x32_neon_i8mm`.
* KlediAI performs matrix multiplication, executing Arm SMMLA instructions (Signed Matrix Multiply Accumulate).
* KleidiAI KleidiAI unpacks and dequantizes the result back into the original FP16 number format sends the final matrix to XNNPack.

### Stage 4: Finish Inference and Output
* XNNPack completes the inference by sending the output matrix of each neural network layer into the next, continuing through all layers of the Gemma-2b, calling KleidiAI when needed.
* XNNPack sends the inference result, a final matrix, to MediaPipe.
* MediaPipe decodes the numerical matrix into a series of tokens representing the answer to the original question.
* The chatbot app receives these tokens from MediaPipe and displays the answer to the user as it streams in from multiple inferences. 
* The user sees the answer on the screen: “The capital of the USA is Washington, D.C.”


## Review 
Note that this overview leaves out details for the sake of brevity, but is helpful for a conceptual understanding of how KleidiAI interacts with ML Frameworks and Generative AI models.

There are several notes on the above process that will help you understand KleidiAI better.


### Quantization - INT8 vs INT4
AI model quantization affects several factors like inference speed. The clearest tradeoff is between model size and accuracy.

On model size: The example above used the default Gemma-2b model has 2.5 billion parameters each stored in 16 bit format, which equates to 5Gb of memory minimum to store the model. Quantizing the model to INT8 reduces the size by 2x. Quantizing to INT4 reduces the size by 4x. This reduction is crucial for deploying AI models on memory-constrained devices like smartphones.

On model accuracy: Quantization reduces percision. INT8 allows for 256 distinct values, while INT4 allows only 16. This reduced precision, if not managed properly, can lead to a decrease in model accuracy and an increase in perplexity.

KleidiAI optimizes for size, accuracy, and execution speed. KleidiAI quantizes model parameters (including weights) to INT4, while inputs propogating through the model during infernces are quantized to INT8.
    


{{% notice Why are models quantized to INT4 but inputs are INT8 %}}
After training, weights typically stay within a range suitable for INT4 quantization without introducing large errors. Furthermore, model sizes are halved by selecting INT4 over INT8 quantization, a significant benefit to both memory storage and throughput.

In contrast, neural network activations (described as 'inputs' so far) are highly variable and not as evenly distributed across the full data range. For example, a common activation function - ReLU - outputs zero for any negative input and leaves any positive input unchanged. This results in a number distribution with many small values but also occasional large values. Having only 16 distinct values (INT4) would result in large quantiztion errors. 

Therefore, KleidiAI strategically selected INT4 quantization for model parameters and INT8 for inputs propogating through the neural network.
{{% /notice %}}


{{% notice What LLM size to select %}}
Most models are trained in 32-bit or 16-bit floating point formats and are by default availible to download at that size. To realize the benefits of lower memory footprint, select a pre-quantized version of your desired AI model, ideally in INT4 format. You can quantize models yourself through various tools, but the quickest and easiest way is to locate a pre-quantized version of the same model.

KleidiAI will dynamically quantize models to INT4 if neccecary.
{{% /notice %}}




### Packing rationale
The goal of KleidiAI's quantization/packing micro-kernels is to prepare the incoming matricies for efficient matrix multiplication. KleidiAI leverages the Arm *SMMLA* instruction, which operates on 8-bit integers. The role of packing after quantization is to organize two INT4 model weights into a single 8-bit memory space. KleidiAI's packing/quantization routines follow a specific packing organization that KleidiAI's matrix multiplication routines leverage for accelerating matmul operations. 

The power of KleidiAI comes from its deep understanding of AI workload requirements, quantization techniques, data packing strategies, and advanced Arm instructions to squeeze the most performance out of AI models on Arm CPUs.

### Next section - C++ example code

The next section dives into the technical specifics of how KleidiAI delivers these performance uplifts by steping through a C++ example.

