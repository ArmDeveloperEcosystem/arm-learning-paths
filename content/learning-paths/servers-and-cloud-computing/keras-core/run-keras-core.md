---
title: Run Keras Core
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Creating the script

Now that you have an overview of every single step in the ML pipeline and you
have all the dependencies installed, you are ready to run the full script.

Copy the following python code and save it in a text file named `ml.py`

```python
import keras_core as keras
from keras_core import layers, models

# Create the model
def create_model():
  inputs = keras.Input(shape=(784,), dtype="float16")

  x = layers.Dense(64, activation="relu")(inputs)
  outputs = layers.Dense(10)(x)

  return keras.Model(inputs=inputs, outputs=outputs, name="my_model")

model = create_model()

# Compile the model
model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.RMSprop(),
    metrics=["accuracy"],
)

# Load the MNIST dataset
(x_train_orig, y_train), (x_test_orig, y_test) = keras.datasets.mnist.load_data()

x_train = x_train_orig.reshape(60000, 784).astype("float32") / 255
x_test = x_test_orig.reshape(10000, 784).astype("float32") / 255

# Train the model
history = model.fit(
    x_train, y_train, batch_size=64, epochs=2, validation_split=0.2
)

# Evaluate the model
test_scores = model.evaluate(x_test, y_test, verbose=2)
print("Test loss:", test_scores[0])
print("Test accuracy:", test_scores[1])

# Generate prediction
prediction = model.predict(x_test)
print(prediction[0])
```

## Running the script

Run the script:

```bash
python ml.py
```

The output should be similar to:

```output
Using TensorFlow backend
Epoch 1/2
2023-11-15 16:22:34.193264: W external/local_tsl/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 150528000 exceeds 10% of free system memory.
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1700065354.901793   38650 device_compiler.h:186] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.
2023-11-15 16:22:34.902890: E external/local_xla/xla/stream_executor/stream_executor_internal.h:177] SetPriority unimplemented for this stream.
750/750 --------------- 3s 2ms/step - accuracy: 0.8429 - loss: 0.5899 - val_accuracy: 0.9395 - val_loss: 0.2154
Epoch 2/2
2023-11-15 16:22:36.516913: W external/local_tsl/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 150528000 exceeds 10% of free system memory.
750/750 --------------- 2s 2ms/step - accuracy: 0.9435 - loss: 0.1980 - val_accuracy: 0.9549 - val_loss: 0.1613
313/313 - 0s - 1ms/step - accuracy: 0.9529 - loss: 0.1620
Test loss: 0.16204574704170227
Test accuracy: 0.9528999924659729
313/313 --------------- 0s 1ms/step
[ -1.7050195  -9.559859   -0.8218317   1.4602187  -8.888759   -3.5577898
 -13.615452    8.073295   -3.2169065  -1.5467551]
```

The first thing the script prints is which backend it uses: by default it uses
TensorFlow.

Change the backend to PyTorch:

```bash
KERAS_BACKEND="torch" python ml.py
```

The output now prints PyTorch as the backend:

```output
Using PyTorch backend.
Epoch 1/2
750/750 --------------- 18s 24ms/step - accuracy: 0.8389 - loss: 0.5871 - val_accuracy: 0.9373 - val_loss: 0.2230
Epoch 2/2
750/750 --------------- 18s 23ms/step - accuracy: 0.9401 - loss: 0.2125 - val_accuracy: 0.9527 - val_loss: 0.1672
313/313 - 0s - 729us/step - accuracy: 0.9516 - loss: 0.1664
Test loss: 0.1663871705532074
Test accuracy: 0.9516000151634216
313/313 --------------- 0s 549us/step
[ -3.0308495 -11.1307      0.844439    2.6465333  -7.4379563  -0.7262192
 -11.41562     9.539099   -2.5394506  -1.046052 ]
```

Finally, try the JAX backend:

```bash
KERAS_BACKEND="jax" python ml.py
```

You will now see JAX as the backend:

```ouput
Using JAX backend.
Epoch 1/2
750/750 --------------- 1s 1ms/step - accuracy: 0.8374 - loss: 0.6037 - val_accuracy: 0.9411 - val_loss: 0.2104
Epoch 2/2
750/750 --------------- 1s 897us/step - accuracy: 0.9425 - loss: 0.1998 - val_accuracy: 0.9519 - val_loss: 0.1638
313/313 - 0s - 532us/step - accuracy: 0.9517 - loss: 0.1652
Test loss: 0.16517148911952972
Test accuracy: 0.95169997215271
313/313 --------------- 0s 360us/step
[ -3.0996692   -9.80861      0.7466699    3.2648473   -7.2216845
  -1.23106    -17.222641    10.103312    -3.3881965   -0.13131982]
```

Even if the backend changes, the accuracy is always about 
~0.95 and the predictions are consistent. 

When you run it with different backends, you might notice a difference in execution speeds.

