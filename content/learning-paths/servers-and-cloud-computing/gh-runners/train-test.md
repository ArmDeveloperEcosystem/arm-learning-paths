---
title: Train and test the neural network model
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you will fork the provided example GitHub repository which contains all the code to complete this learning path. You will then learn how to train and test the neural network model using the provided scripts.

## Fork the example repository
As you will be making modifications to the example and will run the GitHub Actions workflows within your own fork, you must make your own copy of the example repository.

In a web browser, navigate to the repository at:

```bash
https://github.com/Arm-Labs/gh_armrunner_mlops_gtsrb
```

Fork the repository, using the `Fork` button:

![#fork](/images/fork.png)

Create a fork within a GitHub Enterprise Organization where you have access to the Arm-based GitHub runners. 

You will now inspect and walk through the code included in the repository to train and test a NN model on the GTSRB dataset. 

### Train model
Within the `scripts` directory, open and view the contents of `train_model.py`.

`train_model.py` is a Python script which creates and and trains the model using PyTorch. This script will load the GTSRB dataset, define a neural network, and train the model on the dataset. Lets look at all the steps to train the model in more detail.

#### Pre-processing

First, you need to load the GTSRB dataset to prepare it for training. The GTSRB dataset is built into `torchvision`, which makes loading it easier. You will define the transformations which are used when loading the training data. The transformations are part of the *pre-processing* step, which makes the data uniform and ready to run through the extensive math operations of your ML model. In accordance with best machine learning practices, you will separate the data used for training and testing, to avoid over-fitting the neural network.

```python
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

train_set = torchvision.datasets.GTSRB(root='./data', split='train', download=True, transform=transform)
train_loader = DataLoader(train_set, batch_size=64, shuffle=True)
```

#### Define the model

The next step is to define a class for the actual model, listing the different layers used. You will define the forward-pass function, which is used at training time to update the weights. Additionally, you will define the loss function and optimizer for the model.

```python
class TrafficSignNet(nn.Module):
    def __init__(self):
        super(TrafficSignNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.fc1 = nn.Linear(64 * 6 * 6, 128)
        self.fc2 = nn.Linear(128, 43) # 43 classes in GTSRB dataset

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.max_pool2d(x, 2)
        x = torch.relu(self.conv2(x))
        x = torch.max_pool2d(x, 2)
        x = torch.flatten(x, 1)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = TrafficSignNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

#### Training with PyTorch and saving the model

A loop is responsible for the actual training, pulling all the steps together. The number of epochs is arbitrarily set to 10 for this example. When the training is finished, the model weights are saved to a `.pth` file format.

```python
num_epochs = 10
model.train()
for epoch in range(num_epochs):
    running_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        inputs, labels = data
        optimizer.zero_grad()

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        # Backward pass and optimization
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 100 == 99: # Print every 100 mini-batches
            print(f'Epoch [{epoch + 1}/{num_epochs}], Step [{i + 1}/{len(train_loader)}], Loss: {running_loss / 100:.4f}')
            running_loss = 0.0

torch.save(model.state_dict(), './models/traffic_sign_net.pth')
```
With this script, you have learnt how to load the GTSRB dataset, define a neural network, train the model on the dataset and save the trained model using PyTorch.

Lets now look at testing this trained model.

### Test model

The `test_model.py` Python script verifies how accurately the ML model you have trained, can classify the traffic signs. It uses the PyTorch profiler to measure the CPU performance in terms of execution time. Using the profiler, you will be able to compare the model inference time when you use two different PyTorch backends to test the model.

#### Load model and create test set
You will load the model that was saved after training and prepare it for evaluation on a test dataset. Just like training, you will define transformations for the testing data and load it from the GTSRB dataset.

```python
model_path = args.model if args.model else './models/traffic_sign_net.pth'

model = TrafficSignNet()
model.load_state_dict(torch.load(model_path))
model.eval()

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

test_set = torchvision.datasets.GTSRB(root='./data', split='test', download=True, transform=transform)
test_loader = DataLoader(test_set, batch_size=64, shuffle=False)
```

#### Testing and display profiling results
The testing snippet loops through the test data, passing each batch through the model and compares predictions to the actual labels to calculate accuracy. The accuracy is calculated as a percentage of correctly classified images. Both the accuracy and PyTorch profiler report is printed at the end of the script.

```python
correct = 0
total = 0
with torch.no_grad():
    for data in test_loader:
        images, labels = data
        with profile(activities=[ProfilerActivity.CPU], record_shapes=True) as prof:
            with record_function("model_inference"):
                outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy of the model on the test images: {100 * correct / total:.2f}%')
print(prof.key_averages().table(sort_by="cpu_time_total", row_limit=10))
```

You should now have an overview of the code for training and testing the model on the GTSRB dataset using PyTorch. In the next section, you will learn how to setup the GitHub Actions workflows to automate running both the training and testing scripts.
