---
title: Text Classification with ThirdAI on Arm Servers.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

![alt-text #center](thirdai_logo.png)

## Background

ThirdAI is a multi-purpose library that provides a high-level API to build machine learning models.

It provides APIs to support common machine learning problems, such as:
- Text Classification and NLP (Natural Language Processing)
- Search and Recommendation
- Time-series Forecasting and Predictions
- Tabular Classification 
- Graph Classification

In the following sections you will see how you can use ThirdAI's library for Text Classification tasks on your Arm servers.

## Install dependencies

To start, you will need to install the ThirdAI package. 

```bash
pip3 install thirdai
```

The full classification example script used in this learning path uses the datasets package to download the data initially. To install datasets, run the following command:

```bash
pip3 install datasets
```


## Train the model 

You are now ready to download the text classification dataset and train a classification model with ThirdAI. Using a file editor of your choice, create a file called `train.py`:


```python
import pandas as pd
from datasets import load_dataset
from thirdai.demos import to_udt_input_batch
from thirdai import bolt
import thirdai
thirdai.licensing.activate("KVN9-JVRJ-FAAN-4UPE-KVXT-KV4F-LMWK-CM9E")

def load_data(output_filename, split, return_inference_batch=False):
    data = load_dataset('amazon_polarity')
    
    df = pd.DataFrame(data[split])
    df = df[['title', 'label']]    
    df.to_csv(output_filename, index=False, sep='\t')
    
    if return_inference_batch:
        inference_batch = to_udt_input_batch(df[["title"]].sample(frac=1).iloc[:5])
        return inference_batch

train_filename = "amazon_polarity_train.csv"
test_filename = "amazon_polarity_test.csv"

load_data(train_filename, split='train')
inference_batch = load_data(test_filename, split='test', return_inference_batch=True)

model = bolt.UniversalDeepTransformer(
    data_types={
        "title": bolt.types.text(),
        "label": bolt.types.categorical(n_classes=2)
    },
    target="label",
    delimiter='\t'
)

model.train(train_filename, epochs=5, learning_rate=0.01, metrics=["categorical_accuracy"])

save_location = "sentiment_analysis.model"
model.save(save_location)

model = bolt.UniversalDeepTransformer.load(save_location)

model.evaluate(test_filename, metrics=["categorical_accuracy"])

```

This example does the following:
- Downloads a sentiment classification dataset using the huggingface `datasets` library
- Formats the data for the model to understand
- Creates a UniversalDeepTransformer and configures it for text classification
- Trains the model and logs training metrics
- Saves the model to `sentiment_analysis.model` for futher deployment

Run this script:

```bash
python3 train.py
```

You should see a progress bar which should go for 5 epochs. If so, you have successfully performed sentiment analysis on a real-world dataset with ThirdAI.

## Evaluate the model

Now that you have the model, let's see how well it performs on the test set.

Copy the contents below into a file called `evaluate.py`

```python
from thirdai import bolt
import numpy as np
import thirdai
thirdai.licensing.activate("KVN9-JVRJ-FAAN-4UPE-KVXT-KV4F-LMWK-CM9E")

save_location = "sentiment_analysis.model"
model = bolt.UniversalDeepTransformer.load(save_location)

test_filename = "amazon_polarity_test.csv"
model.evaluate(test_filename, metrics=["categorical_accuracy"])

activations = model.predict({"title": "I love this product"})
predicted_class = model.class_name(np.argmax(activations))
print(predicted_class)

activations = model.predict({"title": "I hate this product"})
predicted_class = model.class_name(np.argmax(activations))
print(predicted_class)
```

This example does this following:
- Loads the trained model from the save location
- Runs the evaluation on the test dataset and reports accuracy metrics
- Gives an example of how to handle a prediction in areal time inference setting

You have successfully trained, evaluated, and deployed a text classification model for sentiment analysis using ThirdAI. You can explore running other models and use cases just as easily. 