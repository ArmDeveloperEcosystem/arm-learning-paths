---
# User change
title: "Tensorflow"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## TensorFlow for machine learning	
				
To compare TensorFlow on the Raspberry Pi 4 and the Arm cloud server install it and run an example. 
		
Install `pip` and confirm `python` is `python3`. 

```bash
sudo apt install python-is-python3 python3-pip -y
```

Install TensorFlow. 

```bash			
pip install tensorflow-aarch64 tensorflow_io 
```
				
Run a [TensorFlow quickstart example](https://www.tensorflow.org/tutorials/quickstart/beginner) by following the instructions. 

## Quickstart example

To save time entering the commands from the TensorFlow example, the code is shared below. 

Copy it and save it in a file named example.py.

```python
import tensorflow as tf
print("TensorFlow version:", tf.__version__)

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
predictions

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)

probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])

probability_model(x_test[:5])

```

Run the example using `python`.

```bash
time python ./example.py
```

## Results 

The results below show the performance of the Raspberry Pi and the Arm server.

| System | Time to complete              |
|--------|------------------------------:|				
| Raspberry Pi 4 | 1 min 46 sec	|	
| Arm server (4 vCPU)  | 22 sec      |
