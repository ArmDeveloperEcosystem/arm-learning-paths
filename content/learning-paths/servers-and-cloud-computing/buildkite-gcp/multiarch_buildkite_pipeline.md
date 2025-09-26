---
title: Create a Flask app, configure the Dockerfile, and set up the Buildkite pipeline
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

You can now create an application to get containerized with Docker. This guide covers building a Flask-based simple Python application.

Make sure you have a GitHub repository ready where you can execute the upcoming steps, including creating the Dockerfile and app.py file.

### Create Dockerfile

Inside your GitHub repo, add a file named `Dockerfile` with this content:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
```

### Create app.py

In the same repo, add a file named `app.py`:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Arm-based Buildkite runner!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

This Python code defines a simple Flask web server that listens on all interfaces (0.0.0.0) at port 5000 and responds with "Hello from Arm-based Buildkite runner!" when the root URL (/) is accessed.
It is essentially a basic “Hello World” web app running on an ARM-based environment.

### Push Repo to GitHub

Before triggering the pipeline, your GitHub repository should have:

- `Dockerfile` (defines your multi-arch image)
- `app.py` (your Python microservice)

Commit and push your repo with both `Dockerfile` and `app.py`.

```console
git add .
git commit -m "ADD COMMIT MESSAGE"
git push origin main
```

### Adding Docker Credentials as Buildkite Secrets

Make sure to add your Docker credentials as secrets in the Buildkite UI.
- Navigate to: **Buildkite → Agents → Secrets**
- Here you can add `DOCKER_USERNAME` and `DOCKER_PASSWORD`.


![Buildkite Dashboard alt-text#center](images/secrets.png "Figure 1: Set Secrets")

### Create Buildkite Pipeline for Multiarch

In Buildkite, define your pipeline YAML (through the UI):

1. Go to **Buildkite Dashboard → Pipelines → New Pipeline**.
2. Fill out the form:

   - **Git Repository:** Enter your repository URL (SSH or HTTPS).  
   - **Pipeline Name:** Enter the desired name for your pipeline.

![Buildkite Dashboard alt-text#center](images/pipeline.png "Figure 2: Create Pipeline")

3. In the **Steps (YAML Steps)** section, paste your pipeline YAML.

```yaml
steps:
  - label: "Build and Push Multiarch App"
    env:
      DOCKER_CONFIG: "~/.docker"
    commands:
      - echo "Testing env hook..."
      - env | grep DOCKER
      - ~/.buildkite-agent/bin/buildkite-agent secret get "DOCKER_PASSWORD" | docker login -u "$(~/.buildkite-agent/bin/buildkite-agent secret get "DOCKER_USERNAME")" --password-stdin
      - docker buildx rm mybuilder || true
      - docker buildx create --use --name mybuilder
      - docker buildx inspect --bootstrap
      - docker buildx build --platform linux/amd64,linux/arm64 -t "$(~/.buildkite-agent/bin/buildkite-agent secret get "DOCKER_USERNAME")/multi-arch-app:latest" --push . 
    agents:
      queue: buildkite-queue1
```   

![Buildkite Dashboard alt-text#center](images/yaml.png "Figure 3: YAML steps")
4. Click **Create Pipeline**.

5. Trigger a new build by clicking **New Build** on your pipeline’s dashboard.

![Buildkite Dashboard alt-text#center](images/build-p.png "Figure 4: Create Build")

Once your files and pipeline are ready, you can validate that your Buildkite agent is running and ready to execute jobs.
