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
import torch
import torch.nn as nn
import torch.optim as optim
import json
import numpy as np
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split


class SentimentDataset(Dataset):
   def __init__(self, texts, labels, vocab=None, max_length=50):
       self.texts = texts
       self.labels = labels
       self.max_length = max_length
      
       if vocab is None:
           # Build vocabulary from training data
           self.vocab = {'<PAD>': 0, '<UNK>': 1}
           for text in texts:
               for word in text.lower().split():
                   if word not in self.vocab:
                       self.vocab[word] = len(self.vocab)
       else:
           self.vocab = vocab
  
   def __len__(self):
       return len(self.texts)
  
   def __getitem__(self, idx):
       text = self.texts[idx].lower().split()
       # Convert words to indices and pad/truncate to max_length
       indices = [self.vocab.get(word, self.vocab['<UNK>']) for word in text]
       if len(indices) < self.max_length:
           indices += [self.vocab['<PAD>']] * (self.max_length - len(indices))
       else:
           indices = indices[:self.max_length]
      
       return torch.tensor(indices), torch.tensor(self.labels[idx])


class SentimentClassifier(nn.Module):
   def __init__(self, vocab_size, embed_dim=100, hidden_dim=128, num_classes=2):
       super().__init__()
       self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
       self.conv1 = nn.Conv1d(embed_dim, hidden_dim, kernel_size=3, padding=1)
       self.conv2 = nn.Conv1d(hidden_dim, hidden_dim, kernel_size=3, padding=1)
       self.pool = nn.AdaptiveMaxPool1d(1)
       self.fc1 = nn.Linear(hidden_dim, hidden_dim)
       self.fc2 = nn.Linear(hidden_dim, num_classes)
       self.dropout = nn.Dropout(0.5)
      
   def forward(self, x):
       # x shape: (batch_size, seq_len)
       x = self.embedding(x)  # (batch_size, seq_len, embed_dim)
       x = x.transpose(1, 2)  # (batch_size, embed_dim, seq_len)
       x = torch.relu(self.conv1(x))
       x = self.dropout(x)
       x = torch.relu(self.conv2(x))
       x = self.pool(x).squeeze(-1)
       x = torch.relu(self.fc1(x))
       x = self.dropout(x)
       x = self.fc2(x)
       return x


def train_model(model, train_loader, val_loader, criterion, optimizer, num_epochs=20):
   device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
   model = model.to(device)
   best_val_acc = 0
  
   for epoch in range(num_epochs):
       # Training phase
       model.train()
       train_loss = 0
       train_correct = 0
       train_total = 0
      
       for inputs, labels in train_loader:
           inputs, labels = inputs.to(device), labels.to(device)
           optimizer.zero_grad()
           outputs = model(inputs)
           loss = criterion(outputs, labels)
           loss.backward()
           optimizer.step()
          
           train_loss += loss.item()
           _, predicted = outputs.max(1)
           train_total += labels.size(0)
           train_correct += predicted.eq(labels).sum().item()
      
       # Validation phase
       model.eval()
       val_loss = 0
       val_correct = 0
       val_total = 0
      
       with torch.no_grad():
           for inputs, labels in val_loader:
               inputs, labels = inputs.to(device), labels.to(device)
               outputs = model(inputs)
               loss = criterion(outputs, labels)
              
               val_loss += loss.item()
               _, predicted = outputs.max(1)
               val_total += labels.size(0)
               val_correct += predicted.eq(labels).sum().item()
      
       train_acc = 100. * train_correct / train_total
       val_acc = 100. * val_correct / val_total
      
       print(f'Epoch {epoch+1}/{num_epochs}:')
       print(f'Train Loss: {train_loss/len(train_loader):.4f}, Train Acc: {train_acc:.2f}%')
       print(f'Val Loss: {val_loss/len(val_loader):.4f}, Val Acc: {val_acc:.2f}%')
       print('-' * 60)
      
       # Save best model
       if val_acc > best_val_acc:
           best_val_acc = val_acc
           torch.save(model.state_dict(), 'best_sentiment_model.pt')


def main():
   # Sample balanced dataset (After successfully completing this LP, you can try your own samples)
   texts = [
       "I am very happy today",
       "This is wonderful",
       "I love this movie",
       "Great experience",
       "I am feeling fantastic",
       "This is awesome",
       "I am very sad today",
       "This is terrible",
       "I hate this movie",
       "Worst experience ever",
       "I am feeling depressed",
       "This is awful"
   ]
   labels = [1] * 6 + [0] * 6  # 1 for positive, 0 for negative
  
   # Split dataset
   train_texts, val_texts, train_labels, val_labels = train_test_split(
       texts, labels, test_size=0.2, random_state=42, stratify=labels
   )
  
   # Create datasets
   train_dataset = SentimentDataset(train_texts, train_labels)
   val_dataset = SentimentDataset(val_texts, val_labels, vocab=train_dataset.vocab)
  
   # Create dataloaders
   train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
   val_loader = DataLoader(val_dataset, batch_size=4)
  
   # Initialize model and training components
   model = SentimentClassifier(len(train_dataset.vocab))
   criterion = nn.CrossEntropyLoss()
   optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)
  
   # Train model
   train_model(model, train_loader, val_loader, criterion, optimizer)
  
   # Save vocabulary
   with open('sentiment_vocab.json', 'w') as f:
       json.dump(train_dataset.vocab, f)
  
   # Test mode
   model.eval()
   device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
   model = model.to(device)
  
   while True:
       text = input("Enter text to analyze (or 'quit' to exit): ")
       if text.lower() == 'quit':
           break
          
       # Preprocess input
       indices = [train_dataset.vocab.get(word.lower(), train_dataset.vocab['<UNK>'])
                 for word in text.split()]
       if len(indices) < train_dataset.max_length:
           indices += [train_dataset.vocab['<PAD>']] * (train_dataset.max_length - len(indices))
       else:
           indices = indices[:train_dataset.max_length]
          
       # Get prediction
       with torch.no_grad():
           input_tensor = torch.tensor(indices).unsqueeze(0).to(device)
           output = model(input_tensor)
           probabilities = torch.softmax(output, dim=1)
           prediction = torch.argmax(output).item()
           confidence = probabilities[0][prediction].item() * 100
          
       sentiment = "Positive" if prediction == 1 else "Negative"
       print(f"Sentiment: {sentiment}")
       print(f"Confidence: {confidence:.2f}%")


if __name__ == "__main__":
   main()
```


### How This Script Works:
- Generates a synthetic dataset of positive and negative sentiment samples.
- Encodes text into numerical format using an embedding layer.
- Trains a compact CNN model for sentiment classification.
- Saves the trained model and vocabulary for inference.
- Once training is complete, the model is saved as tiny_sentiment.pt, and vocabulary is saved to tiny_sentiment_vocab.json.



To train and test the model with your own inputs, run:
```bash
python ~/executorch/examples/arm/tiny_sentiment.py
```



{{% notice Note %}}
The output has been truncated 
{{% /notice %}}

The output should look like:
```bash
=== Sentiment Analysis Classifier ===
This program demonstrates text sentiment classification using PyTorch

Loading dataset...
Total examples: 12
Positive examples: 6
Negative examples: 6

Building vocabulary from training data...
Vocabulary size: 19 words

Initializing model...
Starting training...
Training on device: cpu

Epoch 1/20
Training: 100%|██████████| 3/3 [00:00<00:00, 62.94it/s, loss=0.2385, acc=44.44%]
Validation: 100%|███████| 1/1 [00:00<00:00, 633.87it/s, loss=0.2302, acc=66.67%]

Epoch Summary:
Train Loss: 0.7154, Train Acc: 44.44%
Val Loss: 0.6906, Val Acc: 66.67%
New best validation accuracy: 66.67%! Saving model...

.
.
.
Saving vocabulary...

=== Interactive Testing Mode ===
Enter text to analyze sentiment. Type 'quit' to exit.
==================================================
Enter text to analyze (or 'quit' to exit): I am happy

Processing text: "I am happy"
Tokenization: i am happy
Padding: Added 47 padding tokens

Analyzing sentiment...

Result:
Sentiment: Positive
Confidence: 76.67%
==================================================
Enter text to analyze (or 'quit' to exit): I am sad

Processing text: "I am sad"
Tokenization: i am sad
Padding: Added 47 padding tokens

Analyzing sentiment...

Result:
Sentiment: Negative
Confidence: 63.98%
==================================================
Enter text to analyze (or 'quit' to exit): quit
```

Do not forget to type 'quit' once you are done testing the model. You are now ready to optimize and convert the model using ExecuTorch.