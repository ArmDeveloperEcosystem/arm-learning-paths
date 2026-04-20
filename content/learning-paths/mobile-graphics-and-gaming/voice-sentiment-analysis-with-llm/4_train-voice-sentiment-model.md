---
title: Train the voice sentiment classification model
weight: 5
layout: learningpathall
---
In this section, you will train a model to classify voice sentiment directly from audio. The raw waveform is converted into audio-based features, then passed through a pre-trained HuBERT model with a classification head.

For this Learning Path, you train the model on the RAVDESS dataset using three sentiment classes: `neutral`, `happy`, and `angry`. This keeps the demo manageable while still showing a realistic transfer-learning workflow. You can extend the same approach to more sentiment classes or other datasets.

Before you begin, make sure you have completed the environment setup from the previous section and installed the required Python dependencies.

This example uses a simple per-sample training loop for clarity. On CPU, training can take 10 to 30 minutes or more depending on your machine. Apple Silicon `mps` and CUDA-enabled GPUs are often faster.

### Step 2.1 - Prepare the dataset

This step downloads the RAVDESS speech dataset, extracts it locally, and builds a dataframe that maps each audio file to a sentiment label. RAVDESS encodes emotion labels in the filename format, which we use to select the classes for this demo.

In practice, this turns a folder of audio files into a structured table that your training code can work with. Each row is one example, and each column stores details such as the file path, actor ID, and sentiment label.

```python
import os
import urllib.request
import zipfile
import pandas as pd

# Download and unpack the dataset into the local project directory.
RAVDESS_URL = "https://zenodo.org/records/1188976/files/Audio_Speech_Actors_01-24.zip?download=1"
output_dir = "data/ravdess"
os.makedirs(output_dir, exist_ok=True)

zip_path = f"{output_dir}/Audio_Speech_Actors_01-24.zip"
extract_dir = f"{output_dir}/Audio_Speech_Actors_01-24"

if not os.path.exists(zip_path):
    print("Downloading dataset...")
    urllib.request.urlretrieve(RAVDESS_URL, zip_path)

if not os.path.exists(extract_dir):
    zipfile.ZipFile(zip_path).extractall(extract_dir)

DATASET_PATH = "data/ravdess/Audio_Speech_Actors_01-24"
emotion_map = {1: "neutral", 3: "happy", 5: "angry"}
data = []

for actor in os.listdir(DATASET_PATH):
    actor_path = os.path.join(DATASET_PATH, actor)
    if not os.path.isdir(actor_path):
        continue

    for f in os.listdir(actor_path):
        if f.endswith(".wav"):
            # RAVDESS encodes emotion ID in the filename.
            emotion = int(f.split("-")[2])

            if emotion in emotion_map:
                data.append({
                    "emotion": emotion_map[emotion],
                    "actor": actor,
                    # Store absolute sample path for later loading.
                    "path": os.path.join(actor_path, f)
                })

df = pd.DataFrame(data)
print(df.head())
print(df["emotion"].value_counts())
```

At the end of this step, you should have a dataframe with the selected audio samples and their sentiment labels.

### Step 2.2 - Create train and validation splits

Next, split the dataset by speaker so the same speaker does not appear in both training and validation sets. This helps avoid data leakage and gives you a more realistic evaluation.
This matters because a speech model can accidentally learn speaker-specific traits instead of sentiment if the same speakers appear in both splits. Separating speakers gives you a better measure of how well the model generalizes.
The training split is the data the model learns from. The validation split is held back and used only to test how well the model performs on unseen examples.

```python
import random

# Split by speaker so the same actor is not in both training and validation.
actors = sorted(df["actor"].unique())
random.seed(42)
random.shuffle(actors)

val_count = max(1, int(0.2 * len(actors)))
val_actors = set(actors[:val_count])
train_actors = set(actors[val_count:])

train_df = df[df["actor"].isin(train_actors)].reset_index(drop=True)
val_df = df[df["actor"].isin(val_actors)].reset_index(drop=True)

print(f"Training samples: {len(train_df)}")
print(f"Validation samples: {len(val_df)}")
```

### Step 2.3 - Load the feature extractor and model

This step loads the HuBERT feature extractor and initializes a sequence classification model. The pre-trained HuBERT base model provides a strong starting point for transfer learning on speech sentiment classification.
The feature extractor prepares raw audio in the format expected by the model. The HuBERT model then uses those inputs to predict one of the target sentiment classes.

```python
from transformers import AutoFeatureExtractor, HubertForSequenceClassification

MODEL_NAME = "facebook/hubert-base-ls960"
# The label list defines the numeric class order used during training.
labels = ["angry", "happy", "neutral"]

# Use the HuBERT feature extractor that matches the pretrained checkpoint.
feature_extractor = AutoFeatureExtractor.from_pretrained(MODEL_NAME)

model = HubertForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=len(labels),
    id2label={i: label for i, label in enumerate(labels)},
    label2id={label: i for i, label in enumerate(labels)},
)
```

### Step 2.4 - Train and evaluate the model

This step performs the core training pass: load audio, extract features, compute loss, and update the model weights. For clarity, this example uses a simple per-sample training loop rather than batching with a `DataLoader`.
During training, the model compares its predictions with the correct labels and updates its weights to reduce the error. After each epoch, the validation loop checks how well the model performs on held-out speakers.

For better performance in a production training pipeline, you would typically use batching and a PyTorch `DataLoader`.

```python
import librosa
import torch

def load_audio(path):
    # Resample audio to 16 kHz, the sampling rate expected by HuBERT.
    return librosa.load(path, sr=16000)[0]

if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

model.to(device)

optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
EPOCHS = 4

for epoch in range(EPOCHS):
    print(f"Epoch {epoch + 1}/{EPOCHS}")
    # Switch back to training mode at the start of each epoch.
    model.train()

    for i, (_, row) in enumerate(train_df.iterrows(), start=1):
        audio = load_audio(row["path"])

        # Convert raw waveform into model input tensors.
        inputs = feature_extractor(
            audio,
            sampling_rate=16000,
            return_tensors="pt"
        )
        inputs = {k: v.to(device) for k, v in inputs.items()}

        # Convert the string label into a class index.
        label = torch.tensor([labels.index(row["emotion"])]).to(device)

        loss = model(**inputs, labels=label).loss

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if i % 50 == 0:
            print(f"Processed {i} training samples")

    model.eval()
    correct = 0

    with torch.no_grad():
        for _, row in val_df.iterrows():
            audio = load_audio(row["path"])
            inputs = feature_extractor(
                audio,
                sampling_rate=16000,
                return_tensors="pt"
            )
            inputs = {k: v.to(device) for k, v in inputs.items()}

            logits = model(**inputs).logits
            pred = logits.argmax(dim=-1).item()

            if pred == labels.index(row["emotion"]):
                correct += 1

    accuracy = correct / max(1, len(val_df))
    print(f"Validation accuracy: {accuracy:.2f}")
```

At the end of this step, you will have a trained model and a simple validation accuracy printed after each epoch. You should typically see validation accuracy improve over time, although the exact values will vary depending on randomness and hardware.

### Step 2.5 - Save the model

Save both the trained model and the feature extractor so they can be reused later for inference and ONNX export. Keeping them together helps avoid preprocessing mismatches.
This is an important final step because the model weights alone are not enough. You also need the matching feature extractor so inference uses the same preprocessing as training.

```python
import os

SAVE_DIR = "models/hubert_vsa_ravdess"
os.makedirs(SAVE_DIR, exist_ok=True)

# Save both the trained model and the preprocessing configuration.
model.save_pretrained(SAVE_DIR)
feature_extractor.save_pretrained(SAVE_DIR)
```

After this step, the trained model should be saved in `models/hubert_vsa_ravdess`.

## Full training script

The following script combines the previous steps into one runnable example. Save it as `train_sentiment_model.py` and run it from the root of your project.
Use this script if you want to run the full workflow without copying each block separately.

```python
import os
import random
import urllib.request
import zipfile

import librosa
import pandas as pd
import torch
from transformers import AutoFeatureExtractor, HubertForSequenceClassification

# Configuration for dataset download, training, and model export.
RAVDESS_URL = "https://zenodo.org/records/1188976/files/Audio_Speech_Actors_01-24.zip?download=1"
OUTPUT_DIR = "data/ravdess"
ZIP_PATH = f"{OUTPUT_DIR}/Audio_Speech_Actors_01-24.zip"
EXTRACT_DIR = f"{OUTPUT_DIR}/Audio_Speech_Actors_01-24"
MODEL_NAME = "facebook/hubert-base-ls960"
SAVE_DIR = "models/hubert_vsa_ravdess"
EPOCHS = 4

emotion_map = {1: "neutral", 3: "happy", 5: "angry"}
# The label list defines the numeric class order used during training.
labels = ["angry", "happy", "neutral"]

os.makedirs(OUTPUT_DIR, exist_ok=True)

if not os.path.exists(ZIP_PATH):
    print("Downloading dataset...")
    urllib.request.urlretrieve(RAVDESS_URL, ZIP_PATH)

if not os.path.exists(EXTRACT_DIR):
    zipfile.ZipFile(ZIP_PATH).extractall(EXTRACT_DIR)

data = []

for actor in os.listdir(EXTRACT_DIR):
    actor_path = os.path.join(EXTRACT_DIR, actor)
    if not os.path.isdir(actor_path):
        continue

    for f in os.listdir(actor_path):
        if f.endswith(".wav"):
            # RAVDESS stores the emotion label in the filename tokens.
            emotion = int(f.split("-")[2])
            if emotion in emotion_map:
                data.append(
                    {
                        "emotion": emotion_map[emotion],
                        "actor": actor,
                        "path": os.path.join(actor_path, f),
                    }
                )

df = pd.DataFrame(data)
print(df.head())
print(df["emotion"].value_counts())

actors = sorted(df["actor"].unique())
random.seed(42)
random.shuffle(actors)

val_count = max(1, int(0.2 * len(actors)))
val_actors = set(actors[:val_count])
train_actors = set(actors[val_count:])

train_df = df[df["actor"].isin(train_actors)].reset_index(drop=True)
val_df = df[df["actor"].isin(val_actors)].reset_index(drop=True)

print(f"Training samples: {len(train_df)}")
print(f"Validation samples: {len(val_df)}")

feature_extractor = AutoFeatureExtractor.from_pretrained(MODEL_NAME)
model = HubertForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=len(labels),
    id2label={i: label for i, label in enumerate(labels)},
    label2id={label: i for i, label in enumerate(labels)},
)

if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

model.to(device)

def load_audio(path):
    # Load and resample audio to the input rate expected by HuBERT.
    return librosa.load(path, sr=16000)[0]

optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)

for epoch in range(EPOCHS):
    print(f"Epoch {epoch + 1}/{EPOCHS}")
    # Switch back to training mode at the start of each epoch.
    model.train()

    for i, (_, row) in enumerate(train_df.iterrows(), start=1):
        audio = load_audio(row["path"])
        # Convert raw audio into tensors the model can consume.
        inputs = feature_extractor(
            audio,
            sampling_rate=16000,
            return_tensors="pt",
        )
        inputs = {k: v.to(device) for k, v in inputs.items()}
        # Map the label name to its numeric class ID.
        label = torch.tensor([labels.index(row["emotion"])]).to(device)

        loss = model(**inputs, labels=label).loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if i % 50 == 0:
            print(f"Processed {i} training samples")

    model.eval()
    correct = 0

    with torch.no_grad():
        for _, row in val_df.iterrows():
            audio = load_audio(row["path"])
            inputs = feature_extractor(
                audio,
                sampling_rate=16000,
                return_tensors="pt",
            )
            inputs = {k: v.to(device) for k, v in inputs.items()}

            logits = model(**inputs).logits
            pred = logits.argmax(dim=-1).item()

            if pred == labels.index(row["emotion"]):
                correct += 1

    accuracy = correct / max(1, len(val_df))
    print(f"Validation accuracy: {accuracy:.2f}")

os.makedirs(SAVE_DIR, exist_ok=True)
model.save_pretrained(SAVE_DIR)
feature_extractor.save_pretrained(SAVE_DIR)

print("Training complete. Model saved successfully.")
print(f"Saved model to {SAVE_DIR}")
```

Run the training script:

```bash
python train_sentiment_model.py
```

At this point, you have a trained voice sentiment classification model saved locally. In the next section, you will convert this model to ONNX format and compress it for more efficient inference.
