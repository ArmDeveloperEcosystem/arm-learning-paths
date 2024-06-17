---
title: Measure and accelerate the performance of Natural Language Processing (NLP) models from Hugging Face on Arm servers
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
The instructions in this Learning Path are for any Arm server running Ubuntu 22.04 LTS. For this example, you need an Arm server instance with at least four cores and 8GB of RAM. The instructions have been tested on AWS Graviton3 (c7g) instances.

To start, you need to install [PyTorch](/install-guides/pytorch) on your Arm machine. 
PyTorch is a widely-used Machine Learning framework for Python. You use PyTorch to deploy Natural Language Processing (NLP) models on your Arm machine.

## Overview

[Hugging Face](https://huggingface.co/) is an open source AI community where you can host your own AI models, train them, and collaborate with others in the community. You can browse through the thousands of models that are available for a variety of use cases like NLP, audio and computer vision. Hugging Face also has a huge collection of NLP models for tasks like translation, Sentiment Analysis, summarization, and text generation.

In this Learning Path, you will run a Sentiment Analysis pipeline from Hugging Face and deploy it on your Arm-based server. Sentiment Analysis is a type of NLP algorithm used to identify and classify the emotional tone of a piece of text. You will then proceed to benchmark and accelerate the execution time of different NLP Sentiment Analysis models on your Arm machine.

## Install Hugging Face Transformers library

The Hugging Face Transformers library provides APIs and tools that let you easily download and fine-tune pre-trained models. Hugging Face Transformers provide a powerful tool called pipelines which greatly simplify the use of these fine-tuned pre-trained models. You will use the Hugging Face Transformer library to build and run a Sentiment Analysis pipeline with different NLP models. 

To install the Transformers library, run the following command:

```bash
pip3 install transformers
```

## Build and run a sentiment analyzer using Hugging Face Transformers library  

You are now ready to use Python and the Hugging Face transformers library to build a simple sentiment analyzer on your Arm machine. Using a file editor of your choice, create a file named `basic-sentiment-analysis.py` with the code shown below:
```python
import time
import numpy as np
import torch
from transformers import pipeline

pipe = pipeline("sentiment-analysis")
data = ["I like the product a lot", "I wish I had not bought this"]
result=pipe(data)
print(result)
```

This example does the following:

* Imports the `pipeline` tool from the transformers library.
* Loads the `sentiment-analysis` pipeline.
* Passes some input text to the pipeline. 
* Runs sentiment analysis on that input text and prints both the label and the sentiment score.

Run this script:

```bash
python basic-sentiment-analysis.py
```

The output from this script should look like:

```output
No model was supplied, defaulted to distilbert/distilbert-base-uncased-finetuned-sst-2-english and revision af0f99b (https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).
Using a pipeline without specifying a model name and revision in production is not recommended.
[{'label': 'POSITIVE', 'score': 0.9997499585151672}, {'label': 'NEGATIVE', 'score': 0.9996662139892578}]
```

You have successfully performed Sentiment Analysis on the two strings of input text, all running on your Arm Neoverse CPU. The sentiment classification (positive or negative) is printed along with the sentiment score. As the output indicates in this simple example, no particular model was supplied to the sentiment-analysis pipeline, so a [default DistilBERT model](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english) is chosen. You can change the input text in your example and re-run the classification example.

Now that you have run this simple Sentiment Analysis example, let's add the ability to pass a particular model to the pipeline and benchmark the model execution. Copy the contents shown below into a file named `benchmark-sentiment-analysis.py`:

```python
import time
import numpy as np
import torch
from transformers import pipeline

def benchmark(pipe, input, runs=1000):
    # Warmup
    for i in range(100):
        result = pipe(input)
    # Benchmark runs
    times = []
    for i in range(runs):
        start = time.time()
        result = pipe(input)
        end = time.time()
        times.append(end - start)
    # Calculate mean and 99 percentile values
    mean = np.mean(times) * 1000
    p99 = np.percentile(times, 99) * 1000
    return "{:.1f}".format(mean), "{:.1f}".format(p99)


short_review = "I'm extremely satisfied with my new Ikea Kallax; It's an excellent storage solution for our kids. A definite must have."

long_review = "We were in search of a storage solution for our kids, and their desire to personalize their storage units led us to explore various options. After careful consideration, we decided on the Ikea Kallax system. It has proven to be an ideal choice for our needs. The flexibility of the Kallax design allows for extensive customization. Whether it's choosing vibrant colors, adding inserts for specific items, or selecting different finishes, the possibilities are endless. We appreciate that it caters to our kids preferences and encourages their creativity. Overall, the boys are thrilled with the outcome. A great value for money."

models = ["distilbert-base-uncased"]
for model in models:
    pipe = pipeline("sentiment-analysis", model=model)
    result = benchmark(pipe, short_review)
    print(f"{model} short sentence: {result}")
    result = benchmark(pipe, long_review)
    print(f"{model} long sentence: {result}")
    result = benchmark(pipe, [short_review] * 8)
    print(f"{model} short sentence batched: {result}")
    result = benchmark(pipe, [long_review] * 8)
    print(f"{model} long sentence batched: {result}")
```
In addition to what the simple script did, this new script does the following:

* Runs the [distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) model using the sentiment-analysis pipeline.
* Passes two inputs to the model, a short review and a long review. The short review consists of 32 tokens and the long review consists of 128 tokens when tokenized with [BertTokenizer](https://huggingface.co/docs/transformers/en/model_doc/bert#transformers.BertTokenizer).
* Measures the execution time for both the inputs as well as the batched form of the two inputs.
* The execution time is measured using the `benchmark` function. In this function, the pipeline is run 100 times as part of the warm-up phase to ensure consistent results. The mean and 99th percentile values are then measured for each execution run.

Run the benchmarking script:

```bash
python benchmark-sentiment-analysis.py
```

The results from running this script on an AWS Graviton3 `c7g.xlarge` instance with Arm Neoverse V1 CPUs is shown below. Your output should look similar:

```output
Some weights of DistilBertForSequenceClassification were not initialized from the model checkpoint at distilbert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight', 'pre_classifier.bias', 'pre_classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
distilbert-base-uncased short sentence: ('31', '32.2')
distilbert-base-uncased long sentence: ('81.7', '84.1')
distilbert-base-uncased short sentence batched: ('252.8', '261.4')
distilbert-base-uncased long sentence batched: ('655.2', '667.7')
```
You should see the mean and 99th percentile execution time printed for the four cases of execution. All times are in milliseconds.  

You can now run the same model and script but this time enable the use of [BFloat16 floating-point fast math kernels](/install-guides/pytorch#bfloat16-floating-point-number-format) with PyTorch and check how it impacts the performance of your model. Recent Arm CPUs like Arm Neoverse V1 and Arm Neoverse N2 include support for BFloat16 instructions. This setting enables General Matrix Multiplication (GEMM) kernels - a type of algorithm widely-used in Machine Learning models, to use BFloat16 Matrix Multiply Accumulate (MMLA) instructions when available on the CPU.

Set the environment variable:

```bash
export DNNL_DEFAULT_FPMATH_MODE=BF16
```

Run the same script again:

```bash
python benchmark-sentiment-analysis.py
```

The output from this run should now look like:

```output
Some weights of DistilBertForSequenceClassification were not initialized from the model checkpoint at distilbert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight', 'pre_classifier.bias', 'pre_classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
distilbert-base-uncased short sentence: ('25.7', '26.8')
distilbert-base-uncased long sentence: ('43.5', '45.5')
distilbert-base-uncased short sentence batched: ('207.6', '214.1')
distilbert-base-uncased long sentence batched: ('349.4', '360.9')
```
The execution time for all 4 cases should now be lower. By enabling BFloat16 fast math kernels, you should see up to 1.9x boost in performance on your AWS Graviton3 instances. 

You can explore running other NLP models like BERT and RoBERTa and benchmarking their performance. The only thing you will need to change in your script are the values being passed to the models list:

Change the line shown below in `benchmark-sentiment-analysis.py`:

```python
models = ["distilbert-base-uncased", "bert-base-uncased", "roberta-base"]
```

The output from the running all three models on an AWS Graviton3 c7g.xlarge instance without enabling BFloat16 fast math kernels is shown below:

```output
Some weights of DistilBertForSequenceClassification were not initialized from the model checkpoint at distilbert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight', 'pre_classifier.bias', 'pre_classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
distilbert-base-uncased short sentence: ('31', '32.2')
distilbert-base-uncased long sentence: ('81.7', '84.1')
distilbert-base-uncased short sentence batched: ('252.8', '261.4')
distilbert-base-uncased long sentence batched: ('655.2', '667.7')
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
bert-base-uncased short sentence: ('61', '63.3')
bert-base-uncased long sentence: ('161.7', '165.2')
bert-base-uncased short sentence batched: ('493', '504.4')
bert-base-uncased long sentence batched: ('1301.5', '1321.6')
Some weights of RobertaForSequenceClassification were not initialized from the model checkpoint at roberta-base and are newly initialized: ['classifier.dense.bias', 'classifier.dense.weight', 'classifier.out_proj.bias', 'classifier.out_proj.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
roberta-base short sentence: ('58.9', '61.2')
roberta-base long sentence: ('163.3', '168.4')
roberta-base short sentence batched: ('474.8', '490.4')
roberta-base long sentence batched: ('1309.7', '1329.4')
```

The output from running the same three models on an AWS Graviton3 c7g.xlarge instance with BFloat16 fast math kernels support enabled is shown below:

```output
Some weights of DistilBertForSequenceClassification were not initialized from the model checkpoint at distilbert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight', 'pre_classifier.bias', 'pre_classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
distilbert-base-uncased short sentence: ('25.7', '26.8')
distilbert-base-uncased long sentence: ('43.5', '45.5')
distilbert-base-uncased short sentence batched: ('207.6', '214.1')
distilbert-base-uncased long sentence batched: ('349.4', '360.9')
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
bert-base-uncased short sentence: ('49.8', '51.7')
bert-base-uncased long sentence: ('85.2', '88.6')
bert-base-uncased short sentence batched: ('398.8', '419')
bert-base-uncased long sentence batched: ('687.2', '729.6')
Some weights of RobertaForSequenceClassification were not initialized from the model checkpoint at roberta-base and are newly initialized: ['classifier.dense.bias', 'classifier.dense.weight', 'classifier.out_proj.bias', 'classifier.out_proj.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
roberta-base short sentence: ('50', '52.2')
roberta-base long sentence: ('85.6', '89')
roberta-base short sentence batched: ('401.7', '410.8')
roberta-base long sentence batched: ('691', '709.8')
```
With all three models, you should see a similar boost in performance by using the BFloat16 fast math kernels.


