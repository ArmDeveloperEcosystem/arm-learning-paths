---
# User change
title: "Train the Digit Recognizer"

weight: 5

layout: "learningpathall"
---

## Objective ##
We will now train a small CNN to classify Sudoku cell crops into 10 classes (0=blank, 1..9=digit), verify accuracy, then export the model to ONNX using the Dynamo exporter and sanity-check parity with ONNX Runtime. This gives us a portable model ready for Arm64 inference and later Android deployment.

## Creating a model
We use a tiny convolutional neural network (CNN) called DigitNet, designed to be both fast (so it runs efficiently on Arm64 and mobile) and accurate enough for recognizing 28×28 grayscale crops of Sudoku digits. It expects 1 input channel (in_channels=1) because we forced grayscale in the preprocessing step.

We start by creating a new file digitnet_model.py and defining the DigitNet class:
```python
import torch
import torch.nn as nn

class DigitNet(nn.Module):
    """
    Tiny CNN for Sudoku digit classification.
    Classes: 0..9 where 0 = blank.
    Input: (N,1,H,W) grayscale (default 28x28).
    """
    def __init__(self, num_classes: int = 10):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1), nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(),
            nn.AdaptiveAvgPool2d((1,1)),
            nn.Flatten(),
            nn.Linear(32, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)
```

We use a very compact convolutional neural network (CNN), which we call DigitNet, to recognize Sudoku digits. The goal is to have a model that is simple enough to run efficiently on Arm64 and mobile devices, but still powerful enough to tell apart the ten classes we care about (0 for blank, and digits 1 through 9).

The network expects each input to be a 28×28 grayscale crop, so it begins with a convolution layer that has one input channel and sixteen filters. This first convolution is responsible for learning very low-level patterns such as strokes or edges. Immediately after, a ReLU activation introduces non-linearity, which allows the network to combine those simple features into more expressive ones. A max-pooling layer then reduces the spatial resolution by half, making the representation more compact and less sensitive to small translations.

At this point, the feature maps are passed through a second convolutional layer with thirty-two filters. This stage learns richer patterns, for example combinations of edges that form loops or intersections that distinguish an “8” from a “0” or a “6”. Another ReLU activation adds the necessary non-linearity to these higher-level features.

Instead of flattening the entire feature map, we apply an adaptive average pooling operation that squeezes each of the thirty-two channels down to a single number. This effectively summarizes the information across the whole image and ensures the model produces a fixed-length representation regardless of the exact input size. After pooling, the features are flattened into a one-dimensional vector.

The final step is a fully connected layer that maps the thirty-two features to ten output values, one for each class. These values are raw scores (logits) that indicate how strongly the model associates the input crop with each digit. During training, a cross-entropy loss will turn these logits into probabilities and guide the model to adjust its weights.

In practice, this means that when you feed in a batch of grayscale Sudoku cells of shape [N, 1, 28, 28], DigitNet transforms them step by step into a batch of [N, 10] outputs, where each row contains the scores for the ten possible classes. Despite its simplicity, this small CNN strikes a balance between speed and accuracy that makes it ideal for Sudoku digit recognition on resource-constrained devices.

## Training a model
We will now prepare the self-containing script that trains the above model on the data prepared earlier. Start by creating the new file 03_Training.py and modify it as follows:
```python
import os, random, numpy as np
import torch as tr
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from tqdm import tqdm
from torch.export import Dim
import onnxruntime as ort  

from digitnet_model import DigitNet  

# Configuration
random.seed(0); np.random.seed(0); tr.manual_seed(0)
DEVICE = "cpu"           # keep CPU for portability
DATA_DIR = "data"        # data/train/0..9, data/val/0..9
ARTI_DIR = "artifacts"
os.makedirs(ARTI_DIR, exist_ok=True)

BATCH = 256
EPOCHS = 10
LR = 1e-3
WEIGHT_DECAY = 1e-4
LABEL_SMOOTH = 0.05

# Datasets (force grayscale to match model)
tfm_train = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),   # force 1-channel input
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,)),
    transforms.RandomApply([transforms.GaussianBlur(3)], p=0.15),
    transforms.RandomAffine(degrees=5, translate=(0.02,0.02), scale=(0.95,1.05)),
])
tfm_val = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),   # force 1-channel input
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,)),
])

train_ds = datasets.ImageFolder(os.path.join(DATA_DIR, "train"), transform=tfm_train)
val_ds   = datasets.ImageFolder(os.path.join(DATA_DIR, "val"),   transform=tfm_val)

train_loader = DataLoader(train_ds, batch_size=BATCH, shuffle=True,  num_workers=0)
val_loader   = DataLoader(val_ds,   batch_size=BATCH, shuffle=False, num_workers=0)

def evaluate(model: nn.Module, loader: DataLoader) -> float:
    model.eval()
    correct = total = 0
    with tr.no_grad():
        for x, y in loader:
            x, y = x.to(DEVICE), y.to(DEVICE)
            pred = model(x).argmax(1)
            correct += (pred == y).sum().item()
            total   += y.numel()
    return correct / total if total else 0.0

def main():
    # Sanity: verify loader channels
    xb, _ = next(iter(train_loader))
    print("Train batch shape:", xb.shape)  # expect [B, 1, 28, 28]

    model = DigitNet(num_classes=10).to(DEVICE)
    opt = tr.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)

    best_acc, best_state = 0.0, None
    for ep in range(1, EPOCHS + 1):
        model.train()
        for x, y in tqdm(train_loader, desc=f"epoch {ep}/{EPOCHS}"):
            x, y = x.to(DEVICE), y.to(DEVICE)
            opt.zero_grad()
            logits = model(x)
            loss = F.cross_entropy(logits, y, label_smoothing=LABEL_SMOOTH)
            loss.backward()
            opt.step()

        acc = evaluate(model, val_loader)
        print(f"val acc: {acc:.4f}")
        if acc > best_acc:
            best_acc = acc
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}

    if best_state is not None:
        model.load_state_dict(best_state)
    print(f"Best val acc: {best_acc:.4f}")

    # Save PyTorch weights (optional)
    tr.save(model.state_dict(), os.path.join(ARTI_DIR, "digitnet_best.pth"))

    # Export to ONNX with dynamic batch using the Dynamo API
    model.eval()
    dummy = tr.randn(1, 1, 28, 28)
    onnx_path = os.path.join(ARTI_DIR, "sudoku_digitnet.onnx")

    tr.onnx.export(
        model,                       # model
        dummy,                       # input tensor corresponds to arg name 'x'
        onnx_path,                   # output .onnx
        input_names=["input"],       # ONNX *display* name (independent of arg name)
        output_names=["logits"],
        opset_version=19,
        do_constant_folding=True,
        keep_initializers_as_inputs=False,
        dynamo=True,
        dynamic_shapes={"x": {0: Dim("N")}}   
    )

    print("Exported:", onnx_path)

    # quick parity with a big batch (proves dynamic batch works)
    sess = ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])
    x = tr.randn(512, 1, 28, 28)
    onnx_logits = sess.run(["logits"], {"input": x.numpy().astype(np.float32)})[0]
    pt_logits   = model(x).detach().numpy()
    print("Parity MAE:", np.mean(np.abs(onnx_logits - pt_logits)))

if __name__ == "__main__":
    main()
```

This file is a self-contained trainer for the Sudoku digit classifier. It starts by fixing random seeds for reproducibility and sets DEVICE="cpu" so the workflow runs the same on desktops and Arm64 boards. It expects the dataset from the previous step under data/train/0..9 and data/val/0..9, and creates an artifacts/ folder for all outputs.

The script builds two dataloaders (train/val) with a preprocessing stack that forces grayscale (Grayscale(num_output_channels=1)) so inputs match the model’s first convolution, converts to tensors, and normalizes to a centered range. Light augmentations on the training split—small affine jitter and occasional blur—mimic camera variability without distorting the digits. Batch size, epochs, and learning rate are set to conservative defaults so training is smooth on CPU; you can scale them up later.

Then, the script it instantiates DigitNet(num_classes=10) model. The optimizer is AdamW with mild weight decay to control overfitting. The loss is cross-entropy with label smoothing (e.g., 0.05), which reduces over-confidence and helps on easily confused shapes (like 6/8/9).

The training loop runs for a fixed number of epochs, iterating mini-batches from the training set. After each epoch, it evaluates on the validation split and logs the accuracy. The script keeps track of the best model state seen so far (based on val accuracy) and restores it at the end, ensuring the final model corresponds to your best epoch, not just the last one.

The file will create two artifacts:
1. digitnet_best.pth — the best PyTorch weights (handy for quick experiments, fine-tuning, or debugging later).
2. sudoku_digitnet.onnx — the exported ONNX model, produced with PyTorch’s Dynamo exporter and a dynamic batch dimension. Dynamic batch means the model accepts input of shape [N, 1, 28, 28] for any N, which is ideal for efficient batched inference on Arm64 and for Android integration.

Right after export, the script runs a parity test: it feeds the same randomly generated batch through both the PyTorch model and the ONNX model (executed by ONNX Runtime) and prints the mean absolute error between their logits. A tiny value confirms the exported graph faithfully matches your trained network.

## Running the script

{{% notice Note %}}
The Dynamo-based ONNX exporter requires PyTorch 2.1 or later. If you encounter errors related to `torch.export.Dim` or the `dynamo` parameter, ensure you have an up-to-date PyTorch installation:

```console
pip install --upgrade torch torchvision
```
{{% /notice %}}

To run the training script, type:

```console
python3 03_Training.py
```

The script will train, validate, export, and verify the digit recognizer in one go. After it finishes, you’ll have both a portable ONNX model and a PyTorch checkpoint ready for the next step—building the image processor that detects the Sudoku grid, rectifies it, segments cells, and performs batched ONNX inference to reconstruct the board for solving.

Here is a sample run:

```output
python3 03_Training.py 
Train batch shape: torch.Size([256, 1, 28, 28])
epoch 1/10: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 1597/1597 [03:24<00:00,  7.82it/s]
val acc: 0.8099
epoch 2/10: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 1597/1597 [03:18<00:00,  8.05it/s]
val acc: 0.8378
epoch 3/10: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 1597/1597 [03:17<00:00,  8.09it/s]
val acc: 0.8855
epoch 4/10: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 1597/1597 [03:20<00:00,  7.97it/s]
val acc: 0.9180
epoch 5/10: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 1597/1597 [03:20<00:00,  7.97it/s]
val acc: 0.9527
epoch 6/10: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 1597/1597 [03:22<00:00,  7.88it/s]
val acc: 0.9635
epoch 7/10: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 1597/1597 [03:22<00:00,  7.88it/s]
val acc: 0.9777
epoch 8/10: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 1597/1597 [03:21<00:00,  7.91it/s]
val acc: 0.9854
epoch 9/10: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 1597/1597 [03:21<00:00,  7.91it/s]
val acc: 0.9912
epoch 10/10: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 1597/1597 [03:21<00:00,  7.91it/s]
val acc: 0.9928
Best val acc: 0.9928
[torch.onnx] Obtain model graph for `DigitNet([...]` with `torch.export.export(..., strict=False)`...
[torch.onnx] Obtain model graph for `DigitNet([...]` with `torch.export.export(..., strict=False)`... ✅
[torch.onnx] Run decomposition...
[torch.onnx] Run decomposition... ✅
[torch.onnx] Translate the graph into ONNX...
[torch.onnx] Translate the graph into ONNX... ✅
Applied 1 of general pattern rewrite rules.
Exported: artifacts/sudoku_digitnet.onnx
Parity MAE: 1.0251999e-05
```

## Summary
By running the training script you train the DigitNet CNN on the Sudoku digit dataset, steadily improving accuracy across epochs until the model surpasses 99% validation accuracy. The process builds on the earlier steps where we first defined the model architecture in digitnet_model.py and then prepared a dedicated training script to handle data loading, augmentation, optimization, and evaluation. During training the best-performing model state is saved, and at the end it is exported to the ONNX format with dynamic batch support. A parity check confirms that the ONNX and PyTorch versions produce virtually identical outputs (mean error ~1e-5). You now have a validated ONNX model (artifacts/sudoku_digitnet.onnx) and a PyTorch checkpoint (digitnet_best.pth), both ready for integration into the Sudoku image processing pipeline. Before moving on to grid detection and solving, however, we will first run standalone inference to confirm the model’s predictions on individual digit crops.
