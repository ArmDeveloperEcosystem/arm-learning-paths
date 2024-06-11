---
title: Train a model for text classification 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install dependencies

You will need to install Python and pip to use ThirdAI. The instructions below are for Ubuntu, but you can use other Linux distributions.

```bash { target="ubuntu:latest" }
sudo apt install python3-pip python3-venv -y
```

Create a virtual environment to avoid dependency conflicts: 

```bash
python3 -m venv thirdai
source thirdai/bin/activate
```

The prompt of your terminal now has (thirdai) as a prefix to indicate the virtual environment is active.

To start, you need to install the ThirdAI package: 

```bash
pip3 install thirdai
```

The full classification example below uses the Hugging Face datasets package to download data. 

To install datasets, run the following command:

```bash
pip3 install datasets
```

The data used is from the Amazon Polarity Sentiment dataset, a large-scale sentiment analysis dataset for product reviews. 

In the Amazon Polarity Sentiment dataset, each review is turned into a simple binary sentiment classification task, where a positive review has a label of 1 and a negative review has a label of 0. 

The dataset is called "polarity" because it focuses on binary sentiment classification, which is often referred to as "sentiment polarity". 

This dataset is often used in natural language processing tasks related to sentiment analysis, where the goal is to determine the sentiment expressed in a piece of text.

## Download dataset and train the model 

You are now ready to download the text classification dataset and train a classification model with ThirdAI. 

Using a file editor of your choice, create a file called `train.py` with the contents:


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
To train the model run the script:

```bash
python3 train.py
```

You see a progress bar which shows 5 epochs. 

The output is:

```output
Downloading readme: 100%|████████████████████████████████████████████| 6.81k/6.81k [00:00<00:00, 25.5MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 260M/260M [00:04<00:00, 52.1MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 258M/258M [00:05<00:00, 50.1MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 255M/255M [00:04<00:00, 53.4MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 254M/254M [00:04<00:00, 58.3MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 117M/117M [00:02<00:00, 43.3MB/s]
Generating train split: 100%|████████████████████████| 3600000/3600000 [00:10<00:00, 348213.25 examples/s]
Generating test split: 100%|████████████████████████████| 400000/400000 [00:06<00:00, 60559.24 examples/s]
train | epoch 0 | train_steps 1758 | train_categorical_accuracy=0.853649  | train_batches 1758 | time 11.421s

train | epoch 1 | train_steps 3516 | train_categorical_accuracy=0.909235  | train_batches 1758 | time 10.719s

train | epoch 2 | train_steps 5274 | train_categorical_accuracy=0.943465  | train_batches 1758 | time 10.626s

train | epoch 3 | train_steps 7032 | train_categorical_accuracy=0.958409  | train_batches 1758 | time 10.565s

train | epoch 4 | train_steps 8790 | train_categorical_accuracy=0.965971  | train_batches 1758 | time 10.550s

validate | epoch 0 | train_steps 8790 | val_categorical_accuracy=0.843548  | val_batches 196 | time 0.261s

```

With each epoch, the model refines its understanding of the training data, leading to increased accuracy. This means it is getting better at making correct predictions.

To examine the training data, open the `amazon_polarity_train.csv` file. Each line contains a phrase and is followed by either a 1, signifying a positive review, or a 0, representing a negative review.

The model file, named `sentiment_analysis.model`, is now ready and can be integrated into your applications.

You have successfully trained a text classification models for sentiment analysis on a real-world dataset with ThirdAI.
