---
title: Deploy MLflow models as REST APIs
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy and register a model

In this section, you'll learn about model versioning, alias assignment, and serving the model as an API.

Continue using the same terminals from the previous section: terminal A to run scripts, start model serving, and test the API, and terminal B to keep the MLflow tracking server running.

## Set tracking URI

In terminal A, run:

```bash
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
```

This tells the MLflow client which tracking server to connect to. Without it, the client defaults to a local directory and won't find the models registered on your server.

## Create alias script

Navigate to the demo directory:

```bash
cd ~/mlflow-learning-path/demo
```

Create a script to select the best model automatically:

```bash
cat > set_prod.py <<'EOF'
import os
from mlflow import MlflowClient

tracking_uri = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")
client = MlflowClient(tracking_uri=tracking_uri)

versions = client.search_model_versions("name='iris-model'")

best_v = None
best_acc = -1

for v in versions:
    run = client.get_run(v.run_id)
    acc = run.data.metrics.get("accuracy", -1)
    if acc > best_acc:
        best_acc = acc
        best_v = v.version

client.set_registered_model_alias("iris-model", "production", best_v)
print("Production version:", best_v)
EOF
```
The script queries all registered versions of `iris-model`, finds the version with the highest `accuracy` metric, and assigns it the `production` alias. The alias is how `mlflow models serve` identifies which model version to load.

## Assign production model

Run the script:

```bash
python set_prod.py
```
The output is similar to:

```output
Production version: 1
```

## Deploy the model as a REST API

With terminal B still running the MLflow tracking server, use terminal A to start the model serving API. `mlflow models serve` loads the aliased model from the registry and starts a uvicorn HTTP server that exposes a `/invocations` endpoint for inference.

In terminal A, navigate to the project directory and set the tracking URI:

```bash
cd ~/mlflow-learning-path
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
```

Start the model server in the background using `&` so Terminal A stays free for testing:

```bash
mlflow models serve \
  -m "models:/iris-model@production" \
  -p 6000 \
  --no-conda &
```

The following key flags configure the model server: 

- `-m "models:/iris-model@production"` — loads the model version with the `production` alias from the registry
- `-p 6000` — serves on port 6000
- `--no-conda` — uses the active virtual environment instead of creating a new conda environment

The output is similar to:

```output
2026/05/04 13:42:12 INFO mlflow.models.flavor_backend_registry: Selected backend for flavor 'python_function'
2026/05/04 13:42:12 INFO mlflow.pyfunc.backend: === Running command 'exec uvicorn --host 127.0.0.1 --port 6000 --workers 1 mlflow.pyfunc.scoring_server.app:app'
INFO:     Started server process [4527]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:6000 (Press CTRL+C to quit)
```
## View registered models

In the MLflow UI at `http://<VM-IP>:5000`, select the **Models** tab. You should see the `iris-model` entry with multiple registered versions and the `production` alias assigned to the best-performing one.


![MLflow Model Registry showing iris-model with multiple registered versions and the production alias visible next to the best-performing version in the versions table#center](images/mlflow-model.png "MLflow Model Registry with production alias assigned")

## Test the model API with sample data

The `/invocations` endpoint accepts data in the `dataframe_records` format — a list of JSON objects where each object represents one row, with column names as keys. The model returns a prediction for each row. Send a single Iris flower measurement from terminal A to test inference:

```bash
curl -X POST http://127.0.0.1:6000/invocations \
  -H "Content-Type: application/json" \
  -d '{
    "dataframe_records": [
      {
        "sepal length (cm)": 5.1,
        "sepal width (cm)": 3.5,
        "petal length (cm)": 1.4,
        "petal width (cm)": 0.2
      }
    ]
  }'
```

The output is similar to:

```output
INFO:     127.0.0.1:41158 - "POST /invocations HTTP/1.1" 200 OK
{"predictions": [0]}
```

The prediction `0` corresponds to Iris setosa, which is the correct class for these measurements. The Iris dataset has three classes: `0` = setosa, `1` = versicolor, `2` = virginica.

## What you've accomplished

You have now completed the full MLflow lifecycle on a Google Cloud C4A Axion Arm VM running SUSE Linux.

Starting from a freshly provisioned Arm-based VM, you installed MLflow and its dependencies in an isolated Python virtual environment, then started the MLflow tracking server backed by a local SQLite database. You trained a logistic regression model on the Iris dataset across three hyperparameter configurations, with each run automatically logged to the MLflow Tracking UI.

In the final section, you selected the best-performing model version by accuracy, assigned it a `production` alias, served it as a REST API, and validated the workflow by sending a live inference request. You've now experienced the complete machine learning lifecycle on Arm-based infrastructure, from experiment tracking and model versioning to production deployment.

