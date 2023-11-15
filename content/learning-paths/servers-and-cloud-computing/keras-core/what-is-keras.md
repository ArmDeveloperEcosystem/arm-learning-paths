---
title: What is Keras Core?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Keras Core
Keras is a multi backend framework that provides a high-level API to build
Machine Learning models.

![alt-text #center](images/keras-logo.png "Keras Logo")

It provides the common blocks used to create models, such as
* Model abstractions
* Layers
* Activation functions
* Objectives
* Optimizers
* Initializers
* etc..

In July 2023, Keras Core was announced as a full rewrite of the library as
multi backend architecture covering the following backends:

* TensorFlow: https://www.tensorflow.org
* PyTorch: https://pytorch.org
* JAX: https://jax.readthedocs.io/en/latest/

Keras API were integrated in TensorFlow (under `tf.keras`) and with Keras Core
API compatibility is maintained. This means that if you have a model that uses
Keras in TensorFlow, you will now get that model to be able to use PyTorch or
JAX out of the box.

You can read the full [announcement](https://keras.io/keras_core/announcement/).

## Keras model life-cycle overview
The life-cycle of a Keras model has the following steps:
* model creation
* model compilation
* model training
* model evaluation
* model prediction

![alt-text #center](images/keras-life-cycle.png "Keras model life-cycle overview")

In the following sections you will see how to use Keras to implement every
single step.

### Create models in Keras
A Model is a collections of *layers* organised in a graph. Keras supports two
main APIs to create graphs.

#### Sequential API

The sequential API is a list or chain of layers and it has a more user friendly
interface. There is a limitation to one output/input between layer.

Here an example of sequential API.

```python
import keras_core as keras
from keras_core import layers

def create_model():
  model = keras.Sequential()
  model.add(keras.Input(shape=(784,)))
  model.add(layers.Dense(64, activation="relu"))
  model.add(layers.Dense(10))
  return model

model = create_model()
```

Feel free to explore the official documentation of the sequential API: https://keras.io/guides/sequential_model/

#### Functional API

The functional API instead are for more "advanced" use as they allow non-linear
topology of the graph. They also allow to share layers in the graph and
multiple output/input between layers.

Here an example of functional API.

```python
import keras_core as keras
from keras_core import layers

def create_model():
  inputs = keras.Input(shape=(784,))
  x = layers.Dense(64, activation="relu")(inputs)
  outputs = layers.Dense(10)(x)

  return keras.Model(inputs=inputs, outputs=outputs, name="my_model")

model = create_model()
```

Feel free to explore the official documentation of the functional API: https://keras.io/guides/functional_api/

### Change the backend in Keras

Keras is a multi backend framework and it allows to change it at runtime. You
can change the backend via either an environment variable or using Python.

```bash
# Possible values are tensorflow, torch, jax
export KERAS_BACKEND=torch
```

```python
import os

os.environ["KERAS_BACKEND"] = "jax" # or tensorflow or torch
```

After you set the backend, it will be used in the next executions of Keras. The
default backend is `tensorflow`.


### Compile models in Keras

The compilation step in Keras means that the model will be configured for the
training step.
The compilation step is where you define:
* the optimizer such as SGD (Gradient Descend), Adam, RMSProp, etc... Available optimizers: https://keras.io/keras_core/api/optimizers/
* the loss function such as Categorical Cross-entropy, Mean Squared Error, etc... Available loss functions: https://keras.io/keras_core/api/losses/
* the metrics to guide training such as "accuracy", "crossentropy", etc... Available metrics: https://keras.io/keras_core/api/metrics/

This is an example how you can compile a model.

```python
model.compile(
  loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  optimizer=keras.optimizers.RMSprop(),
  metrics=["accuracy"],
)
```

You can compile step applies the same way for both functional or sequential API.

### Datasets

After the compilation of the model, you are ready to train the model. You will
need a *dataset*: it consists of data needed for training, evaluation and
testing of the model.

{{% notice Note %}}
Datasets are very specific to a model or an application. You need to have full
knowledge of the model input layout as it needs to be compatible with the
dataset structure. Keras provides some common datasets for experimentation
(E.g.: MNIST, CIFAR10, CIFAR100, IMDB, etc...)

The full list of datasets provided by Keras is available https://keras.io/keras_core/api/datasets/ 
{{% /notice %}}

As part of the ML development workflow, it is common to partition the dataset
into two parts, so that you can test a atrained model with data that is unknown
during the training phase.
You also need to *normalize* the dataset before using it for training.

In the following example you are using the MNIST dataset: it is a large
database of handwritten digits that is commonly used for training various image
processing systems.


![alt-text #center](images/mnist.png "Sample images from MNIST test dataset")

```python
import keras_core as keras

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train.reshape(60000, 784).astype("float32") / 255
x_test = x_test.reshape(10000, 784).astype("float32") / 255
```

The 784 come from the size of the image. Each image is a square of 28 pixels
hence 28x28=784.

### Train models in Keras

Once you have access to the dataset and you are ready to train the model which
is going to approximate the input data.
The resultant object `history` contains how the training is progressing over
incremental epochs (each round of sweeping over training data)
It will use the configuration and techniques set at `compile()` phase, and it
is guided by two pieces of information:
* **loss**: it is the value that the model is seeking to minimize
* **accuracy (or other metric)**: it is the ratio of correct predictions

To train the model, you need to call the `.fit()` method against the model
itself.

```python
history = model.fit(
  x_train, y_train, batch_size=64, epochs=2, validation_split=0.2
)
```

### Evaluate models in Keras

After the training step it is important to provide the model with unseen data
for evaluation in order to prevent problems such as overfitting.
You use the slice of the dataset that you kept for testing.

```python
test_scores = model.evaluate(x_test, y_test, verbose=2)
print(”Loss:", test_scores[0])
print(”Accuracy:", test_scores[1])
```

The returned test scores are the ones set at `compile()` time.

### Generate predictions in Keras
Once the model is training and accuracy levels are acceptable, the model can be
used to generate predictions.

```python
test_scores = model.predict(x_test)
```
In this case an array of 10 values is printed: every value represents the
percentage that the image represents the index of the value.


```output
[ -6.1369014  -8.772338   -1.5029577   0.8902472 -10.76559    -4.302728
 -15.749295    7.22214    -4.3954177  -3.5787518]
```

In the above case the biggest value is 7.22214 and is at position 7: the model
thinks that the input image is a 7.
