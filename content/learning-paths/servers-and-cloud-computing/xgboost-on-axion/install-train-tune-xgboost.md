---
title: Install XGBoost and train machine learning models
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install and configure XGBoost on SUSE Linux

In this section, you'll install XGBoost on a Google Axion Arm64 VM running SUSE Linux with Python 3.11. You'll then train a machine learning model and tune model performance using hyperparameter optimization.

### Update system packages

Update all system packages before installing Python and machine learning dependencies. By updating packages, you can avoid package conflicts and ensure the latest security updates are applied:

```bash
sudo zypper refresh
sudo zypper update -y
```

### Install XGBoost dependencies

Install Python 3.11, development libraries, and build tools required for XGBoost:

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

Verify that Python 3.11 is installed correctly:

```bash
python3.11 --version
```

### Create a Python virtual environment

Create a dedicated project directory and an isolated Python virtual environment for the XGBoost Learning Path. Using a virtual environment keeps the XGBoost packages separate from the system Python installation:

```bash
mkdir -p ~/xgboost-learning-path
cd ~/xgboost-learning-path

python3.11 -m venv xgb-env
source xgb-env/bin/activate
```

The virtual environment helps isolate Python packages from the system installation.

### Upgrade pip

Upgrade pip, setuptools, and wheel to ensure compatibility with the latest Python packages and build dependencies:

```bash
pip install --upgrade pip setuptools wheel
```

### Create a requirements file

Create a requirements file listing the Python packages needed for XGBoost training and benchmarking:

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

### Install machine learning dependencies

Install all machine learning dependencies inside the virtual environment:

```bash
pip install -r requirements.txt
```

Verify that XGBoost is installed correctly:

```bash
python -c "import xgboost; print(xgboost.__version__)"
```

The output is similar to:

```output
3.2.0
```
## Train a machine learning model

After configuring XGBoost, you'll train and tune an XGBoost classification model.

### Create XGBoost training script
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

### Start model training

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

The model trained on the breast cancer dataset and saved both a JSON and a pickle file to the project directory.

### Verify generated model files
Verify that the trained model files were created successfully after training.

```bash
ls -lh
```

The output is similar to:

```output
drwxr-xr-x  5 user user 4.0K May 13 10:20 xgb-env
-rw-r--r--  1 user user  55  May 13 10:21 requirements.txt
-rw-r--r--  1 user user 1.2K May 13 10:22 train_xgboost.py
-rw-r--r--  1 user user  80K May 13 10:23 xgboost-model.json
-rw-r--r--  1 user user  80K May 13 10:23 xgboost-model.pkl
```

The `.json` and `.pkl` files are the trained model artifacts used later for inference API deployment.

## Use GridSearchCV to tune hyperparameters

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

The search tested 12 combinations (3 depths × 2 learning rates × 2 estimator counts) using 3-fold cross-validation. The best parameters shown are the combination that produced the highest cross-validated accuracy.

## Benchmark large-scale training

In this step, you'll benchmark XGBoost training performance using a larger synthetic dataset.

The benchmark simulates large-scale tabular machine learning workloads on the GCP Axion Arm64 processor.

### Create the benchmark script

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

### Run the benchmark script

Run the benchmark script to measure large-scale training performance on Arm64.

```bash
python benchmark_xgboost.py
```

The output is similar to:

```output
Benchmark completed in 9.36 seconds
```

The benchmark used a synthetic dataset of 500,000 samples and 50 features. Your result may vary depending on VM load at the time of the run.

## What you've accomplished and what's next

You've now installed XGBoost on a GCP Axion Arm64 VM, trained and saved a classification model on the breast cancer dataset, tuned hyperparameters with GridSearchCV, and benchmarked large-scale training performance. 

Next, you'll deploy the trained model as a Flask inference API and access it from your browser using the VM public IP.
