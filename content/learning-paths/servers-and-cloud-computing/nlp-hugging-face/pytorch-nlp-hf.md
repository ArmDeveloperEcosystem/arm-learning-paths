---
title: Run a Natural Language Processing (NLP) model from Hugging Face on Arm servers
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

In this learning path, you will download a popular [RoBERTa sentiment analysis](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) NLP model from Hugging Face and deploy it using PyTorch on your Arm machine. Sentiment analysis is a type of NLP algorithm used to identify and classify the emotional tone of a piece of text. This model has been trained with over 124 million tweets. 

## Install dependencies

The Hugging Face Transformers library provides APIs and tools that let you easily download and fine-tune pre-trained models. Hugging Face Transformers support multiple machine learning frameworks like PyTorch, TensorFlow and JAX. You will use Transformers with PyTorch to download the model from Hugging Face.

To install the Transformers library for PyTorch, run the following command:

```bash
pip install 'transformers[torch]'
```

The full classification example script used in this learning path uses SciPy, an open source Python library to process the inference output from the NLP model. To install SciPy, run the following command:

```bash 
pip install scipy
```

## Run the sentiment analysis NLP model 

You are now ready to download this model and run a full classification example from Hugging Face on your machine. Using a file editor of your choice, create a file named `sentiment-analysis.py`:

```python
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
import transformers
transformers.logging.set_verbosity_error()
# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
# PT
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
text = "Covid cases are increasing fast!"
text = preprocess(text)
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
scores = output[0][0].detach().numpy()
scores = softmax(scores)
# Print labels and scores
ranking = np.argsort(scores)
ranking = ranking[::-1]
for i in range(scores.shape[0]):
    l = config.id2label[ranking[i]]
    s = scores[ranking[i]]
    print(f"{i+1}) {l} {np.round(float(s), 4)}")
```
This example does the following:

* Downloads and creates an instance of the RoBERTa sentiment analysis model 
* Creates a `tokenizer` which prepares the inputs as tensors for the model 
* Pre-processes the input text to the model
* Encodes the input text to the model
* Passes the encoded input text to the model and performs the sentiment analysis
* Obtains the output classification score

Run this script:

```bash
python sentiment-analysis.py
```

The output from this script should look like:

```output
1) negative 0.7236
2) neutral 0.2287
3) positive 0.0477
```

You should see three lines, each with a rank, sentiment label (negative / neutral / positive), and confidence score. The first line is the model’s strongest guess. The three probabilities should sum to 1. In this example, the model is confident the sentiment is negative.

You have successfully performed sentiment analysis on the input text, all running on your Arm AArch64 CPU. You can change the input text in your example and re-run the classification example.

Now that you have run the model, let's add the ability to profile the model execution. You can use the [PyTorch Profiler](https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) to analyze the execution time on the CPU. Copy the contents shown below into a file named `sentiment-analysis-profile.py`:

```python
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
import transformers
transformers.logging.set_verbosity_error()
import torch
from torch.profiler import profile, record_function, ProfilerActivity
# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
# PT
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
text = "Covid cases are increasing fast!"
text = preprocess(text)
encoded_input = tokenizer(text, return_tensors='pt')
with torch.profiler.profile(activities=[torch.profiler.ProfilerActivity.CPU],
                            record_shapes=True) as prof:
    with record_function("model_inference"):
        output = model(**encoded_input)

# print basic stats
print(prof.key_averages().table(sort_by="self_cpu_time_total", row_limit=10))

scores = output[0][0].detach().numpy()
scores = softmax(scores)
# Print labels and scores
ranking = np.argsort(scores)
ranking = ranking[::-1]
for i in range(scores.shape[0]):
    l = config.id2label[ranking[i]]
    s = scores[ranking[i]]
    print(f"{i+1}) {l} {np.round(float(s), 4)}")
```

Run this python script:

```bash
python sentiment-analysis-profile.py
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
In addition to the classification output from the model, you can now see the execution time for the different operators. The table shows how much time each operation takes on the CPU, both by itself and including any child operations. 

You can experiment with the [BFloat16 floating-point number format](/install-guides/pytorch#bfloat16-floating-point-number-format) and [Transparent huge pages](/install-guides/pytorch#transparent-huge-pages) settings with PyTorch and see how that impacts the performance of your model.

You have successfully run and profiled a sentiment analysis NLP model from Hugging Face on your Arm machine. You can explore running other models and use cases just as easily.



