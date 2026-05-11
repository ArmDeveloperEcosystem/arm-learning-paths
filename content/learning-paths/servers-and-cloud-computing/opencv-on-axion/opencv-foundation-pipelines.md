---
title: Build OpenCV Pipelines on GCP Axion (Arm)
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build OpenCV Pipelines on GCP Axion (Arm)

This section guides you through setting up OpenCV on an Arm-based VM and building **image and video processing pipelines with browser visualization**.

## Learning Objectives

- Install OpenCV on Arm  
- Build image pipeline  
- Build video pipeline  
- Visualize output in browser  


## Update your system
Refresh package metadata to ensure latest packages are available.

```bash
sudo zypper refresh
```

## Install dependencies
Install Python and build tools required to run OpenCV pipelines.

```bash
sudo zypper install -y \
python311 python311-pip python311-devel \
gcc gcc-c++ make cmake \
```

## Create project
Create a dedicated workspace for your OpenCV project.

```bash
mkdir -p ~/opencv-project
cd ~/opencv-project
```

## Setup Python environment
Create an isolated Python environment to avoid dependency conflicts.

```bash
python3.11 -m venv cv-env
source cv-env/bin/activate
```

## Install Python packages
Install OpenCV and required Python libraries.

```bash
pip install --upgrade pip
pip install numpy opencv-python-headless flask
```

## Quick OpenCV Test

Before building pipelines, verify that OpenCV is working correctly.

This step creates a simple image using OpenCV and saves it for browser viewing.

```bash
python3.11 - <<EOF
import cv2
import numpy as np

# Create a blank image
img = np.zeros((300,300,3), dtype=np.uint8)

# Add text using OpenCV
cv2.putText(img, "OpenCV OK", (30,150),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (255,255,255), 2)

# Save output
cv2.imwrite("test.jpg", img)

print("Test image created")
EOF
```

## Verify OpenCV setup

Open in browser:

```text
http://<VM-IP>:8000/test.jpg
```

You should see an image with text:

```text
OpenCV OK
```

![OpenCV test image showing "OpenCV OK" text rendered using OpenCV on Arm VM#center](images/opencv-test.png "OpenCV verification output")

## Start browser server (used in all steps)
Start a simple HTTP server to view output images in browser.

```bash
python -m http.server 8000
```

Open:

```text
http://<VM-IP>:8000/
```

## Image Pipeline

**Create script**

This script reads an image, processes it, and saves the result for browser viewing.

```bash
vi image_pipeline.py
```

```python
import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Image not found")
    exit()

img = cv2.resize(img, (800,600))

cv2.putText(img, "IMAGE PIPELINE", (20,40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

cv2.imwrite("latest.jpg", img)
```

### What this script does

- Loads an image using OpenCV
- Applies basic processing (resize + text overlay)
- Saves output as `latest.jpg`
- This file is used for browser visualization

## Generate sample ARM image

Instead of downloading external images, generate a sample image locally. This ensures the guide works in all environments without internet dependency.

```bash
python3.11 - <<EOF
import cv2
import numpy as np

# Create blank image
img = np.zeros((600,800,3), dtype=np.uint8)

# Add ARM-themed labels
cv2.putText(img, "ARM PROCESSOR", (150,250),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 3)

cv2.putText(img, "OpenCV PIPELINE", (150,350),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

# Save image
cv2.imwrite("input.jpg", img)

print("Generated input.jpg")
EOF
```

## What this step does

- Creates an image using NumPy
- Uses OpenCV to draw text
- Saves it as input.jpg
- Removes dependency on external downloads

## Execute image pipeline
Run the pipeline using generated image.

```bash
python image_pipeline.py
```

## Verify
Open the processed image in browser.

```text
http://<VM-IP>:8000/latest.jpg
```

## You should see:

- ARM PROCESSOR text
- OpenCV processing applied

![Processed image showing ARM PROCESSOR text with OpenCV transformations on Arm VM#center](images/opencv-image.png "OpenCV image pipeline output")

## Video Pipeline

**Create synthetic video:**

This script generates a sample video so you don’t depend on external files.

```bash
vi create_video.py
```

```python
import cv2
import numpy as np

out = cv2.VideoWriter("video.mp4",
                      cv2.VideoWriter_fourcc(*'mp4v'),
                      20,
                      (640,480))

for i in range(200):
    frame = np.zeros((480,640,3), dtype=np.uint8)
    cv2.putText(frame, f"Frame {i}", (100,240),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    out.write(frame)

out.release()
```

### What this script does

- Creates a synthetic video
- Generates frames dynamically
- Writes them into video.mp4
- Helps simulate real video input

## Create video pipeline

```bash
vi video_pipeline.py
```

```python
import cv2
import time

cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    cv2.putText(frame, "VIDEO PIPELINE", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imwrite("latest.jpg", frame)

    time.sleep(0.05)
```

## Run video pipeline

```bash
python video_pipeline.py
```

## Correct browser visualization
Do NOT open latest.jpg directly. Instead, create a live viewer.

### Create live viewer

```bash
vi index.html
```

```html
<html>
<head>
<title>Video Pipeline</title>
</head>
<body>

<h2>Live Video Feed</h2>

<img id="img" src="latest.jpg" width="640">

<script>
setInterval(function(){
    document.getElementById("img").src =
        "latest.jpg?t=" + new Date().getTime();
}, 200);
</script>

</body>
</html>
```

## Verify
Open the continuously updating frame in browser.

```text
http://<VM-IP>:8000/index.html
```

You should see a live video effect where:

- Frames update automatically in the browser
- OpenCV processes each frame in real-time
- "VIDEO PIPELINE" text is overlaid on the video

![Processed image showing ARM PROCESSOR text with OpenCV transformations on Arm VM#center](images/opencv-video.png "OpenCV image pipeline output")

## What you've learned

- Installed OpenCV on Arm
- Built image processing pipeline
- Built video pipeline
- Implemented browser-based visualization

## Next

You will:

- Integrate ML (YOLO)
- Enable real-time detection
- Optimize performance for Arm
