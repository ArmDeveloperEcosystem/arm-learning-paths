---
title: Train and test the neural network
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Fork repository

TODO: fix this section when the repo is publicly available

Clone the repository.

```bash
git clone ...
cd ...
```

## The code
The repository contains two main scripts. This section walks you through the code and explains what it does.

### Train model

`train_model.py` is a script which creates and and trains the model on the GTSRB dataset. Since it's a computer vision use-case, it utilizes `torchvision` in addition to the main PyTorch package.


#### Pre-processing

The GTSRB dataset is built into `torchvision`, which makes loading it easier. The first step is to define the transformations which are used when loading the training data and testing data. The transformations are part of the *pre-processing* step, which makes the data uniform and ready to run through the extensive math operations of your ML model. In accordance with best machine learning practices, we separate the data used for training and testing, to avoid over-fitting the neural network.

```python
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

train_set = torchvision.datasets.GTSRB(root='./data', split='train', download=True, transform=transform)
train_loader = DataLoader(train_set, batch_size=64, shuffle=True)

test_set = torchvision.datasets.GTSRB(root='./data', split='test', download=True, transform=transform)
test_loader = DataLoader(test_set, batch_size=64, shuffle=False)
```

#### Define the model

The next step is to define a class for the actual model, listing the different layers used. We also define the forward-pass function, which is used at training time to update the weights. Additionally, we define the loss function and optimizer for the model parameters are listed.

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

#### Training with PyTorch and saving the file

A loop is responsible for the actual training, pulling all these things together. The number of epochs is arbitrarily set to 10. When the training is finished, the model weights are saved to the `.pth` file format.

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

### Test model

The `test_model.py` script verifies how accurately the ML model can classify the traffic signs. It uses the PyTorch profiler to measure the CPU performance in terms of execution time. Using the profiler, you will be able to measure 
 and compare the model inference time using two different PyTorch backends. 
 
#### Load model and create test set
By loading the weights into the same class as before, we obtain the same model set up as in the last step. The `eval` function set the model up for evaluation. Just like before, we define transformations for the testing data and load it from the GTSRB dataset.

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
The testing snippet loops through the test samples, and records whether the model hits or misses. The accuracy and PyTorch profiler report is printed at the end of the script.

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

You should now have an overview of the code in the training and testing scripts. In the next section, you will learn how to setup the GitHub actions workflows to automate running these scripts.
