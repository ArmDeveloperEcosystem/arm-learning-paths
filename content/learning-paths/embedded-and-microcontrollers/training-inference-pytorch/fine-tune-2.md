---
title: Train and Test the Sentiment Classifier
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the Model

Navigate to the Arm examples directory in the ExecuTorch repository.

```bash
cd $HOME/executorch/examples/arm
```

Using a file editor of your choice, create a file named tiny_sentiment.py with the code shown below:

```python
#!/usr/bin/env python3

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import argparse
import os
import re
import json

class TinySentimentClassifier(nn.Module):
    def __init__(self, vocab_size=5000, embedding_dim=32):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.conv1 = nn.Conv1d(embedding_dim, 16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv1d(16, 8, kernel_size=3, padding=1)
        self.pool = nn.AdaptiveAvgPool1d(1)
        self.fc = nn.Linear(8, 2)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.embedding(x)
        x = x.transpose(1, 2)
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.pool(x).squeeze(-1)
        return self.fc(x)

class Vocabulary:
    def __init__(self):
        self.word2idx = {'<PAD>': 0, '<UNK>': 1}
        self.idx2word = {0: '<PAD>', 1: '<UNK>'}

    def add_word(self, word):
        if word not in self.word2idx:
            self.word2idx[word] = len(self.word2idx)
            self.idx2word[len(self.idx2word)] = word

    def encode_text(self, text, max_len=64):
        words = re.findall(r'\w+', text.lower())
        indices = [self.word2idx.get(word, 1) for word in words]
        if len(indices) > max_len:
            indices = indices[:max_len]
        else:
            indices += [0] * (max_len - len(indices))
        return torch.tensor(indices, dtype=torch.long)

    def save(self, path):
        vocab_data = {
            'word2idx': self.word2idx,
            'idx2word': {int(k): v for k, v in self.idx2word.items()}
        }
        with open(path, 'w') as f:
            json.dump(vocab_data, f)

    @classmethod
    def load(cls, path):
        vocab = cls()
        with open(path, 'r') as f:
            vocab_data = json.load(f)
        vocab.word2idx = vocab_data['word2idx']
        vocab.idx2word = {int(k): v for k, v in vocab_data['idx2word'].items()}
        return vocab

def train_model(model, train_loader, epochs=5, device='cpu'):
    print("\n" + "="*50)
    print("Starting Training...")
    print("="*50)
    
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        correct = 0
        total = 0
        
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
            _, predicted = output.max(1)
            total += target.size(0)
            correct += predicted.eq(target).sum().item()
            
            if batch_idx % 10 == 0:
                progress = (batch_idx + 1) / len(train_loader)
                bar_length = 30
                filled_length = int(bar_length * progress)
                bar = '=' * filled_length + '-' * (bar_length - filled_length)
                print(f'\rEpoch {epoch+1}/{epochs} [{bar}] {progress:.1%}', end='')
        
        print(f'\nEpoch {epoch+1}/{epochs}:')
        print(f'Loss: {total_loss/len(train_loader):.4f}')
        print(f'Accuracy: {100.*correct/total:.2f}%\n')

def predict_sentiment(model, vocab, text, device='cpu'):
    model.eval()
    with torch.no_grad():
        encoded = vocab.encode_text(text).unsqueeze(0).to(device)
        output = model(encoded)
        probabilities = torch.softmax(output, dim=1)
        prediction = torch.argmax(probabilities).item()
        confidence = probabilities[0][prediction].item()
    return prediction, confidence

def main():
    parser = argparse.ArgumentParser(description='TinyML Sentiment Classifier')
    parser.add_argument('--mode', choices=['train', 'test'], required=True,
                      help='Train the model or test with user input')
    parser.add_argument('--model-path', default='tiny_sentiment.pt',
                      help='Path to save/load the model')
    args = parser.parse_args()

    model_path = args.model_path
    vocab_path = f"{os.path.splitext(model_path)[0]}_vocab.json"

    # Training data
    sample_texts = [
        "This is amazing!", "Great product", "I love it",
        "Terrible experience", "Not good at all", "Disappointing",
        "Really enjoyed this", "Would recommend", "Best purchase ever",
        "Waste of money", "Don't buy this", "Regret buying"
    ]
    sample_labels = torch.tensor([1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0])

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"\nUsing device: {device}")

    if args.mode == 'train':
        # Initialize vocabulary
        vocab = Vocabulary()
        for text in sample_texts:
            for word in re.findall(r'\w+', text.lower()):
                vocab.add_word(word)

        # Create dataset and dataloader
        dataset = torch.utils.data.TensorDataset(
            torch.stack([vocab.encode_text(text) for text in sample_texts]),
            sample_labels
        )
        train_loader = DataLoader(dataset, batch_size=4, shuffle=True)

        # Initialize and train model
        model = TinySentimentClassifier(len(vocab.word2idx)).to(device)
        train_model(model, train_loader, epochs=10, device=device)

        # Save model and vocabulary separately
        torch.save(model.state_dict(), model_path)
        vocab.save(vocab_path)
        print(f"\nModel saved to {model_path}")
        print(f"Vocabulary saved to {vocab_path}")

    elif args.mode == 'test':
        # Check if files exist
        if not os.path.exists(model_path) or not os.path.exists(vocab_path):
            print(f"Error: Model or vocabulary files not found!")
            print(f"Please run training first using: python {__file__} --mode train")
            return

        # Load vocabulary and model
        vocab = Vocabulary.load(vocab_path)
        model = TinySentimentClassifier(len(vocab.word2idx)).to(device)
        model.load_state_dict(torch.load(model_path))
        model.eval()

        print("\n" + "="*50)
        print("TinyML Sentiment Classifier")
        print("="*50)
        print("Type 'quit' to exit")
        print("="*50 + "\n")

        while True:
            text = input("\nEnter text to analyze: ").strip()
            if text.lower() == 'quit':
                break

            prediction, confidence = predict_sentiment(model, vocab, text, device)
            sentiment = "Positive" if prediction == 1 else "Negative"
            print(f"\nSentiment: {sentiment}")
            print(f"Confidence: {confidence*100:.2f}%")

if __name__ == "__main__":
    main()
```
### How This Script Works:
- Generates a synthetic dataset of positive and negative sentiment samples.
- Encodes text into numerical format using an embedding layer.
- Trains a compact CNN model for sentiment classification.
- Saves the trained model and vocabulary for inference.
- Once training is complete, the model is saved as tiny_sentiment.pt, and vocabulary is saved to tiny_sentiment_vocab.json.


To train the model, run:
```bash
python ~/executorch/examples/arm/tiny_sentiment.py --mode train
```

The output should look like:
```bash
Using device: cpu

==================================================
Starting Training...
==================================================
Epoch 1/15 [====================----------] 66.7%
Epoch 1/15:
Loss: 0.6959
Accuracy: 49.31%

Epoch 2/15 [====================----------] 66.7%
Epoch 2/15:
Loss: 0.6935
Accuracy: 50.00%

.
.
.

Epoch 15/15 [====================----------] 66.7%
Epoch 15/15:
Loss: 0.6125
Accuracy: 81.60%


Model saved to tiny_sentiment.pt
Vocabulary saved to tiny_sentiment_vocab.json
```

To test the model with your own inputs, run:
```bash
python ~/executorch/examples/arm/tiny_sentiment.py --mode test
```

The output should look like:
```bash
Using device: cpu

==================================================
TinyML Sentiment Classifier
==================================================
Type 'quit' to exit
==================================================


Enter text to analyze: I love sun

Sentiment: Positive
Confidence: 55.88%

Enter text to analyze: I hate falling

Sentiment: Negative
Confidence: 52.36%
```
Do not forget to type 'quit' once you are done playing around with the model. You are now ready to optimize and convert the model using ExecuTorch.


IGNORE anything BELOW:
## Compile and build the executable

Start by setting some environment variables that are used by ExecuTorch.

```bash
export ET_HOME=$HOME/executorch
export executorch_DIR=$ET_HOME/build
```

IGNORE anything BELOW:

Then, generate a `.pte` file using the Arm examples. The Ahead-of-Time (AoT) Arm compiler will enable optimizations for devices like the Raspberry Pi and the Corstone-320 FVP. Run it from the ExecuTorch root directory.

Navigate to the root directory using:

```bash
cd ../../
```
You are now in $HOME/executorch and ready to create the model file for ExecuTorch.


```bash
cd $ET_HOME
python -m examples.arm.aot_arm_compiler --model_name=examples/arm/tiny_sentiment.py \
--delegate --quantize --target=ethos-u85-256 \
--so_library=cmake-out-aot-lib/kernels/quantized/libquantized_ops_aot_lib.so \
--system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Sram_Only
```

From the Arm Examples directory, you build an embedded Arm runner with the `.pte` included. This allows you to get the most performance out of your model, and ensures compatibility with the CPU kernels on the FVP. Finally, generate the executable `arm_executor_runner`.

```bash
cd $HOME/executorch/examples/arm/executor_runner


cmake -DCMAKE_BUILD_TYPE=Release \
-DCMAKE_TOOLCHAIN_FILE=$ET_HOME/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake \
-DTARGET_CPU=cortex-m85 \
-DET_DIR_PATH:PATH=$ET_HOME/ \
-DET_BUILD_DIR_PATH:PATH=$ET_HOME/cmake-out \
-DET_PTE_FILE_PATH:PATH=$ET_HOME/tiny_sentiment_arm_delegate_ethos-u85-256.pte \
-DETHOS_SDK_PATH:PATH=$ET_HOME/examples/arm/ethos-u-scratch/ethos-u \
-DETHOSU_TARGET_NPU_CONFIG=ethos-u85-256 \
-DPYTHON_EXECUTABLE=$HOME/executorch-venv/bin/python3 \
-DSYSTEM_CONFIG=Ethos_U85_SYS_DRAM_Mid  \
-B $ET_HOME/examples/arm/executor_runner/cmake-out

cmake --build $ET_HOME/examples/arm/executor_runner/cmake-out --parallel -- arm_executor_runner

```

Now, you can run the model on the Corstone-320 FVP.