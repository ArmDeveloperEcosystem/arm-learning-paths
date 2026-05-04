---
title: Integrate ML Models with OpenCV on GCP Axion (Arm)
weight: 6
 
### FIXED, DO NOT MODIFY
layout: learningpathall
---
 
## Integrate ML Models with OpenCV on GCP Axion (Arm)
This section extends the OpenCV learning path by integrating a machine learning model with an OpenCV pipeline. You will train a simple ML model, load it inside an OpenCV-based Python script, generate a visual prediction output, and view the result in a browser.
 
This guide assumes that you have already completed the OpenCV installation, Python virtual environment setup, and browser visualization setup from the previous section.
 
## Learning Objectives
 
- Install ML dependencies in the existing OpenCV environment
- Train a simple machine learning model
- Integrate the ML model with an OpenCV pipeline
- Generate visual prediction output using OpenCV
- View the ML pipeline result in a browser
 
## Prerequisites
Before starting this section, make sure you have:
 
- A running GCP Axion Arm-based VM
- SUSE Linux running on the VM
- Python 3.11 installed
- OpenCV project directory created at `~/opencv-project`
- Python virtual environment created at `~/opencv-project/cv-env`
- OpenCV installed in the virtual environment
- Port `8000` allowed in the GCP firewall if you want to view output from a browser
 
## Terminal usage
Use two terminals for this section:
 
- **Terminal A:** Train the ML model and run the OpenCV + ML pipeline
- **Terminal B:** Run the browser HTTP server
 
## Go to the project directory
Run the following commands in Terminal A.
 
```bash
cd ~/opencv-project
source cv-env/bin/activate
```
 
**Verify Python and OpenCV:**
 
```bash
python --version
python - <<'PYEOF'
import cv2
print("OpenCV version:", cv2.__version__)
PYEOF
```
 
Expected output is similar to:
```output
Python 3.11.10
OpenCV version: 4.13.0
```
 
## Install ML dependencies
Install `scikit-learn` to train a simple model and `joblib` to save and load the model.
 
```bash
pip install scikit-learn joblib
```
**Verify the installation:**
 
```bash
python - <<'PYEOF'
import sklearn
import joblib
print("scikit-learn version:", sklearn.__version__)
print("joblib imported successfully")
PYEOF
```
 
## Train a simple ML model
Create a training script that uses the Iris dataset and trains a Random Forest classifier.
 
```bash
cat > train_ml_model.py <<'EOF'
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib
 
iris = load_iris()
X = iris.data
y = iris.target
 
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
 
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
 
model.fit(X_train, y_train)
 
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
 
joblib.dump(model, "iris_model.joblib")
joblib.dump(iris.target_names, "iris_labels.joblib")
 
print("ML model trained successfully")
print("Model file: iris_model.joblib")
print("Label file: iris_labels.joblib")
print(f"Accuracy: {accuracy:.2f}")
EOF
```
 
**Run the script:**
 
```bash
python train_ml_model.py
```
 
The output is similar to:
 
```output
ML model trained successfully
Model file: iris_model.joblib
Label file: iris_labels.joblib
Accuracy: 1.00
```
 
**Verify that the model files were created:**
 
```bash
ls -lh iris_model.joblib iris_labels.joblib
```
## Create the OpenCV + ML pipeline
Create a script that loads the trained model, runs prediction, and uses OpenCV to generate a visual output image.
 
```bash
cat > opencv_ml_pipeline.py <<'EOF'
import cv2
import numpy as np
import joblib
 
model = joblib.load("iris_model.joblib")
labels = joblib.load("iris_labels.joblib")
 
# Sample input format:
# [sepal length, sepal width, petal length, petal width]
sample = np.array([[5.1, 3.5, 1.4, 0.2]])
 
prediction = model.predict(sample)[0]
predicted_label = labels[prediction]
 
img = np.zeros((500, 900, 3), dtype=np.uint8)
 
cv2.putText(
    img,
    "OpenCV + ML Pipeline on GCP Axion",
    (50, 80),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)
 
cv2.putText(
    img,
    "Platform: Arm64",
    (50, 150),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 255, 255),
    2
)
 
cv2.putText(
    img,
    f"Input Features: {sample.tolist()[0]}",
    (50, 230),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.75,
    (255, 255, 255),
    2
)
 
cv2.putText(
    img,
    f"Prediction: {predicted_label}",
    (50, 320),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 0),
    2
)
 
cv2.putText(
    img,
    "ML model executed successfully with OpenCV visualization",
    (50, 410),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (0, 200, 255),
    2
)
 
cv2.imwrite("ml_output.jpg", img)
 
print("OpenCV + ML pipeline completed")
print("Prediction:", predicted_label)
print("Output image saved as ml_output.jpg")
EOF
```
 
**Run the pipeline:**
 
```bash
python opencv_ml_pipeline.py
```
 
The output is similar to:
 
```output
OpenCV + ML pipeline completed
Prediction: setosa
Output image saved as ml_output.jpg
```
 
Verify the output file:
```bash
ls -lh ml_output.jpg
```
 
## Start the browser server
Open Terminal B and run:
 
```bash
cd ~/opencv-project
source cv-env/bin/activate
python -m http.server 8000
```
 
The output is similar to:
 
```output
Serving HTTP on 0.0.0.0 port 8000 ...
```
Keep this terminal running.
 
## View the ML output in browser
Open the following URL in your browser:
 
```text
http://<VM-PUBLIC-IP>:8000/ml_output.jpg
```
Replace `<VM-PUBLIC-IP>` with the external IP address of your GCP Axion VM.
 
**You should see an image showing:**
 
```output
OpenCV + ML Pipeline on GCP Axion
Platform: Arm64
Input features
Prediction result
ML execution confirmation
```
![OpenCV ML pipeline output showing prediction result on GCP Axion Arm VM#center](images/opencv-ml.png "OpenCV ML pipeline output")
 
## Troubleshooting
**Issue:** `ModuleNotFoundError: No module named 'sklearn'`
 
Make sure the virtual environment is activated and install the dependency again.
 
```bash
cd ~/opencv-project
source cv-env/bin/activate
pip install scikit-learn joblib
```
 
**Issue:** `iris_model.joblib` not found
 
Run the training script before running the ML pipeline.
```bash
python train_ml_model.py
```
 
**Issue:** Browser cannot access the output image
 
Check that the HTTP server is running in Terminal B.
```bash
python -m http.server 8000
```
 
Also make sure port `8000` is allowed in the GCP firewall.
 
**Issue:** Output image does not update
 
Run the ML pipeline again after changing the sample input.
```bash
python opencv_ml_pipeline.py
```
Then refresh the browser page.
 
**Clean up generated files**
 
Use this only if you want to remove generated ML and output files.
 
```bash
rm -f iris_model.joblib iris_labels.joblib ml_output.jpg
```
 
## What you've learned
In this section, you learned how to:
 
- Install ML libraries in an OpenCV environment
- Train a machine learning model on an Arm-based GCP Axion VM
- Save and load a trained model using `joblib`
- Integrate ML inference with an OpenCV pipeline
- Generate browser-viewable ML prediction output
