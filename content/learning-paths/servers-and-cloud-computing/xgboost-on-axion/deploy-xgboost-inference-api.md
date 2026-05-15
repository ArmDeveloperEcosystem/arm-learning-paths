---
title: Deploy and access XGBoost inference API
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy XGBoost inference API on SUSE Linux

In this section, you'll deploy the trained XGBoost model as a Flask-based inference API on a GCP Axion Arm64 VM. You'll expose the API externally and access it from a browser using the VM public IP.

You'll use:

**Terminal A** → API server

**Terminal B** → API testing

## Connect to the VM
Connect to the VM where the trained XGBoost model and Python environment were created. This VM will host the inference API service.

```bash
ssh <your-user>@<your-vm-ip>
```

Navigate to the XGBoost project directory that contains the trained model files and scripts.

```bash
cd ~/xgboost-learning-path
```

Activate the Python virtual environment to load all required Python packages and dependencies.

```bash
source xgb-env/bin/activate
```

## Install Flask
Flask is used to create the lightweight REST API that serves XGBoost predictions through HTTP requests.

Create an updated requirements file containing all required Python dependencies.

```bash
cat > requirements.txt <<'EOF'
xgboost
numpy
pandas
scikit-learn
matplotlib
joblib
flask
EOF
```

Install all dependencies including Flask inside the Python virtual environment.

```bash
pip install -r requirements.txt
```

Verify that Flask is installed successfully.

```bash
pip list | grep Flask
```

The output is similar to:

```output
Flask            3.1.3
```

## Create inference API
In this step, you'll create a Flask-based API that loads the trained XGBoost model and exposes prediction endpoints over HTTP.

The `/` endpoint is used for browser validation, while the `/predict` endpoint handles prediction requests using JSON input data.

```bash
cat > inference_api.py <<'EOF'
from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("xgboost-model.pkl")

@app.route("/", methods=["GET"])
def home():
    return """
    <h1>XGBoost API Running on GCP Axion Arm64</h1>
    <p>Inference API Status : Active</p>
    <p>Use POST /predict endpoint for predictions.</p>
    """

@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.json["features"]

        prediction = model.predict(np.array([data]))

        return jsonify({
            "prediction": int(prediction[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
EOF
```

## Start the inference API
Start the Flask application so the API becomes accessible locally and externally through the VM public IP address.

```bash
python inference_api.py
```

The output is similar to:

```output
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://10.128.15.209:8080
```

Leave this terminal running because the Flask server must remain active to handle incoming requests.

## Access API from browser
The Flask API can now be accessed externally from your browser using the VM public IP and port `8080`.

Open:

```text
http://<VM-PUBLIC-IP>:8080
```

Example:

```text
http://35.xxx.xxx.xxx:8080
```

The output is similar to:

```output
XGBoost Inference API is Running
API Status: Active

This API is running on Google Cloud Axion Arm64.

Use the POST /predict endpoint to send prediction requests.
```

The following screenshot shows the XGBoost inference API successfully running and accessible from the browser.

![Browser window showing the XGBoost Inference API homepage running on a Google Cloud Axion Arm64 virtual machine. The page confirms that the inference API is active and accessible externally through port 8080 using the VM public IP address.#center](images/xgboost-api.png "XGBoost inference API running on Google Cloud Axion Arm64")

## Test inference locally
Open terminal B and activate the same Python virtual environment used for the API server.

```bash
cd ~/xgboost-learning-path
source xgb-env/bin/activate
```

In this step, you'll send a prediction request to the XGBoost API using `curl`. The input data is passed as JSON to the `/predict` endpoint.

```bash
curl -X POST http://127.0.0.1:8080/predict \
-H "Content-Type: application/json" \
-d '{"features":[17.99,10.38,122.8,1001.0,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019.0,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]}'
```

The output is similar to:

```output
{"prediction":0}
```
This confirms that the trained XGBoost model successfully received the input features and generated an inference response through the REST API.

## What you've accomplished

You've successfully:

* Deployed XGBoost inference API on GCP Axion Arm64
* Exposed the API externally
* Accessed the API using the VM public IP
* Performed inference using REST API requests
* Validated real-time predictions using Flask and XGBoost
