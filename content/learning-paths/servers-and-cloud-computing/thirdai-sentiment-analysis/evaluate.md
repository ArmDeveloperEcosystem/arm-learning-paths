---
title: Evaluate the model 
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Evaluate the model

Now that you have the trained model, you can see how well it performs on the test set.

Use a text editor to copy the contents below into a file called `evaluate.py`:

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

The test data is in the file `amazon_polarity_test.csv` and contains review data with the same format as the training data.

There are also 2 individual text strings which show how to evaluate a single string.

Run the evaluation script to see how the model performs:

```bash
python3 evaluate.py
```

The output is:

```output
validate | epoch 0 | train_steps 8790 | val_categorical_accuracy=0.843548  | val_batches 196 | time 0.272s

1
0
```

This example performs the following tasks:
- Load the trained model from the saved file.
- Run the evaluation on the test dataset and report accuracy metrics.
- Give an example of how to handle a prediction in a real time inference setting.

The first output line provides the accuracy results and run time for the 40,000 text strings of test data. 

The 1 and 0 which follow are the results for the two provided strings, with a 1 indicating positive sentiment, and a 0 indicating negative sentiment.

You have successfully evaluated a text classification model for sentiment analysis using ThirdAI. This model, capable of classifying text as positive or negative, can be easily integrated into any application.
