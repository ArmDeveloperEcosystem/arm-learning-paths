---
title: Measure and accelerate the performance of Natural Language Processing (NLP) models from Hugging Face on Arm servers
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
The instructions in this learning path are for any Arm server running Ubuntu 22.04 LTS.

To start, you will need to install [PyTorch](/install-guides/pytorch) on your Arm machine. 
PyTorch is a widely used machine learning framework for Python. You will use PyTorch to deploy a Natural Language Processing (NLP) model on your Arm machine.

## Overview

[Hugging Face](https://huggingface.co/) is an open source AI community where you can host your own AI models, train them and collaborate with others in the community. You can browse through the thousands of models that are available for a variety of use cases like NLP, audio and computer vision. Hugging Face also has a huge collection of NLP models for tasks like translation, sentiment analysis, summarization and text generation.

In this learning path, you will download three popular [RoBERTa sentiment analysis](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) NLP models from Hugging Face and deploy it using PyTorch on your Arm machine. Sentiment analysis is a type of NLP algorithm used to identify and classify the emotional tone of a piece of text. This model has been trained with over 124 million tweets. 

## Install Hugging Face Transformers library

The Hugging Face Transformers library provides APIs and tools that let you easily download and fine-tune pre-trained models. Hugging Face Transformers provide a powerful tool called pipelines which greatly simplify the use of these fine-tuned pre-trained models. You will use Hugging Face Transformer Sentiment Analysis pipeline to run the three models. 

To install the Transformers library, run the following command:

```bash
pip3 install transformers
```

## Build and run a sentiment analyzer using Hugging Face Transformers libary 

You are now ready to use python and the Hugging Face transformers library to build a simple sentiment analyzer on your Arm machine. Using a file editor of your choice, create a file named `basic-sentiment-analysis.py` with the code shown below:
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

* Imports `pipeline` tool from the transformers library
* Loads the `sentiment-analysis` pipeline
* Passes text to the pipeline 
* Runs sentiment analysis and prints both the label and the sentiment score

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

You have successfully performed sentiment analysis on the two strings of input text, all running on your Arm Neoverse CPU. You can change the input text in your example and re-run the classification example. As the output indicates in this simple example, no particular model was supplied to the sentiment-analysis pipeline, so a default model is chosen. 

Now that you have run this simple sentiment analysis example, let's add the ability to pass a particular model to the pipeline and benchmark the model execution. Copy the contents shown below into a file named `benchmark-sentiment-analysis.py`:

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

long_review = "We were in search of a storage solution for our kids, and their desire to personalize their storage units led us to explore various options. After careful consideration, we decided on the Ikea Kallax system. It has proven to be an ideal choice for our needs. The flexibility of the Kallax design allows for extensive customization. Whether it's choosing vibrant colors, adding inserts for specific items, or selecting different finishes, the possibilities are endless. We appreciate that it caters to our kids preferences and encourages their creativity. Overall, the boys are thrilled wit the outcome. A great value for money."

models = ["distilbert-base-uncased"]
for model in models:
    pipe = pipeline("sentiment-analysis", model=model)
    result = benchmark(pipe, short_review)
    print(f"{model} short sentence: {result}")

```

Run this python script:

```bash
python benchmark-sentiment-analysis.py
```

The output should look similar to:

```output
STAGE:2024-02-27 17:26:22 18170:18170 ActivityProfilerController.cpp:314] Completed Stage: Warm Up
STAGE:2024-02-27 17:26:22 18170:18170 ActivityProfilerController.cpp:320] Completed Stage: Collection
STAGE:2024-02-27 17:26:22 18170:18170 ActivityProfilerController.cpp:324] Completed Stage: Post Processing
---------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                       Name    Self CPU %      Self CPU   CPU total %     CPU total  CPU time avg    # of Calls
---------------------------  ------------  ------------  ------------  ------------  ------------  ------------
                aten::addmm        56.56%      29.355ms        57.96%      30.085ms     406.554us            74
            model_inference        15.24%       7.910ms       100.00%      51.903ms      51.903ms             1
                  aten::bmm         4.86%       2.521ms         7.37%       3.823ms     159.292us            24
               aten::select         2.55%       1.323ms         2.58%       1.337ms       1.535us           871
                 aten::view         1.98%       1.030ms         1.98%       1.030ms       3.962us           260
               aten::linear         1.97%       1.022ms        62.89%      32.640ms     441.081us            74
    aten::native_layer_norm         1.87%     968.000us         2.07%       1.072ms      42.880us            25
                 aten::gelu         1.76%     912.000us         1.76%     912.000us      76.000us            12
                aten::copy_         1.36%     706.000us         1.36%     706.000us       6.660us           106
               aten::expand         0.95%     492.000us         0.98%     509.000us       4.138us           123
---------------------------  ------------  ------------  ------------  ------------  ------------  ------------
Self CPU time total: 51.903ms

1) negative 0.7236
2) neutral 0.2287
3) positive 0.0477
```
In addition to the classification output from the model, you can now see the execution time for the different operators. 

You can experiment with the [BFloat16 floating-point number format](/install-guides/pytorch#bfloat16-floating-point-number-format) and [Transparent huge pages](/install-guides/pytorch#transparent-huge-pages) settings with PyTorch and see how that impacts the performance of your model.

You have successfully run and profiled a sentiment analysis NLP model from Hugging Face on your Arm machine. You can explore running other models and use cases just as easily.



