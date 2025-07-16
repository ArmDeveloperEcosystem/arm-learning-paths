---
title: Deploy NGINX on Self-Hosted Runner Using GitHub Actions
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Deploy NGINX Using GitHub Actions
This workflow installs and starts the NGINX web server on a self-hosted runner whenever code is pushed to the main branch.

### Create the Workflow:

Create a workflow file at `.github/workflows/deploy-nginx.yaml` with the following content:

```yaml

name: Deploy NGINX

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: self-hosted
    steps:
      - name: Install NGINX
        run: |
          sudo apt update
          sudo apt install -y nginx

      - name: Start NGINX
        run: sudo systemctl start nginx
```
### Commit and Push:

 ```console
git add .
git commit -m "Add NGINX deploy workflow"
git push origin main
```
### Access the NGINX Server
Once the workflow completes, open your browser and navigate to:
```
http://<your-public-IP>
```
You should see the NGINX welcome page confirming a successful deployment.

![nginx](./images/nginx.png)
