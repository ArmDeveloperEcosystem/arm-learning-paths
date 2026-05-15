---
title: Install XGBoost and train machine learning models
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install and configure XGBoost on SUSE Linux

In this section, you'll install XGBoost on a GCP Arm64 (Axion) virtual machine (VM) running SUSE Linux with Python 3.11. You'll then train machine learning models and tune model performance using hyperparameter optimization.

You'll use:

**Terminal A** → Setup and training

**Terminal B** → Benchmarking and tuning

Open both terminals connected to the VM before starting.

## Connect to the VM

Connect to the GCP Axion Arm64 virtual machine using SSH. This VM will be used for XGBoost training, benchmarking, and inference deployment.

```bash
ssh <your-user>@<your-vm-ip>
```

## Update the system
Update all system packages before installing Python and machine learning dependencies. This helps avoid package conflicts and ensures the latest updates are applied.

```bash
sudo zypper refresh
sudo zypper update -y
```

## Install required dependencies
Install Python 3.11, development libraries, and build tools required for XGBoost and machine learning workloads.

```bash
sudo zypper install -y \
  python311 \
  python311-pip \
  python311-devel \
  gcc \
  gcc-c++ \
  make \
  git \
  wget
```

Verify that Python 3.11 is installed correctly.

```bash
python3.11 --version
```

## Create Python environment
Create a dedicated project directory and isolated Python virtual environment for the XGBoost learning path.

```bash
mkdir -p ~/xgboost-learning-path
cd ~/xgboost-learning-path

python3.11 -m venv xgb-env
source xgb-env/bin/activate
```

The virtual environment helps isolate Python packages from the system installation.

## Upgrade pip tools:
Upgrade pip, setuptools, and wheel to ensure compatibility with the latest Python packages and build dependencies.

```bash
pip install --upgrade pip setuptools wheel
```

## Create requirements file
Create a requirements file containing all Python packages required for XGBoost training and benchmarking.

```bash
cat > requirements.txt <<'EOF'
xgboost
numpy
pandas
scikit-learn
matplotlib
joblib
EOF
```

## Install dependencies:
Install all machine learning dependencies inside the Python virtual environment.

```bash
pip install -r requirements.txt
```

Verify that XGBoost is installed correctly.

```bash
python -c "import xgboost; print(xgboost.__version__)"
```

The output is similar to:

```output
3.2.0
```

## Create XGBoost training script
In this step, you'll create a machine learning training script using the Breast Cancer dataset from Scikit-learn.

The script trains an XGBoost classification model, measures training time, evaluates accuracy, and saves the trained model for inference.

```bash
cat > train_xgboost.py <<'EOF'
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import xgboost as xgb
import joblib
import time

data = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(
    data.data,
    data.target,
    test_size=0.2,
    random_state=42
)

model = xgb.XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    tree_method="hist",
    eval_metric="logloss"
)

start = time.time()

model.fit(X_train, y_train)

end = time.time()

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy : {accuracy:.4f}")
print(f"Training Time  : {end - start:.2f} seconds")

model.save_model("xgboost-model.json")

joblib.dump(model, "xgboost-model.pkl")

print("Model saved successfully")
EOF
```

## Train the model
Run the training script to start XGBoost model training on the Arm64 processor.

```bash
python train_xgboost.py
```

The output is similar to:

```output
Model Accuracy : 0.9561
Training Time  : 0.04 seconds
Model saved successfully
```

This confirms that the XGBoost model trained successfully and the model artifacts were generated.

## Verify generated model files
Verify that the trained model files were created successfully after training.

```bash
ls -lh
```

The output is similar to:

```output
requirements.txt
train_xgboost.py
xgb-env
xgboost-model.json
xgboost-model.pkl
```

The `.json` and `.pkl` files will be used later for inference API deployment.

## Hyperparameter tuning
In this step, you'll optimize model performance using GridSearchCV and multiple hyperparameter combinations.

The script tests different values for tree depth, learning rate, and estimators to identify the best-performing model configuration.

Create the tuning script:

```bash
cat > tune_xgboost.py <<'EOF'
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
import xgboost as xgb

data = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(
    data.data,
    data.target,
    test_size=0.2,
    random_state=42
)

params = {
    "max_depth": [4, 6, 8],
    "learning_rate": [0.01, 0.1],
    "n_estimators": [100, 200]
}

model = xgb.XGBClassifier(
    tree_method="hist",
    eval_metric="logloss"
)

grid = GridSearchCV(
    model,
    params,
    cv=3,
    n_jobs=-1
)

grid.fit(X_train, y_train)

print("\nBest Parameters:")
print(grid.best_params_)
EOF
```

Run the hyperparameter tuning workflow.

```bash
python tune_xgboost.py
```

The output is similar to:

```output
Best Parameters:
{'learning_rate': 0.1, 'max_depth': 4, 'n_estimators': 100}
```

This identifies the best hyperparameter combination for the dataset.

## Benchmark large-scale training
In this step, you'll benchmark XGBoost training performance using a larger synthetic dataset.

The benchmark simulates large-scale tabular machine learning workloads on the GCP Axion Arm64 processor.

Create benchmark script:

```bash
cat > benchmark_xgboost.py <<'EOF'
from sklearn.datasets import make_classification
import xgboost as xgb
import time

X, y = make_classification(
    n_samples=500000,
    n_features=50,
    n_informative=25,
    random_state=42
)

model = xgb.XGBClassifier(
    n_estimators=300,
    max_depth=8,
    tree_method="hist",
    eval_metric="logloss"
)

start = time.time()

model.fit(X, y)

end = time.time()

print(f"\nBenchmark completed in {end - start:.2f} seconds")
EOF
```

## Run benchmark
Run the benchmark script to measure large-scale training performance on Arm64.

```bash
python benchmark_xgboost.py
```

The output is similar to:

```output
Benchmark completed in 9.36 seconds
```

This validates that the Arm64-based Axion processor can efficiently handle large-scale XGBoost workloads.

## What you've accomplished and what's next

You've successfully:

* Installed XGBoost on GCP Axion Arm64
* Configured Python 3.11 environment
* Trained XGBoost models on Arm processors
* Tuned hyperparameters
* Benchmarked large-scale datasets

Next, you'll deploy the trained model as an inference API and access it from your browser using the VM public IP.
