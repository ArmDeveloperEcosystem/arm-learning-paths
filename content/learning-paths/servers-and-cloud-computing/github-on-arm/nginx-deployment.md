---
title: Deploy NGINX the GitHub Runner
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


This workflow installs and starts a basic NGINX web server on a self-hosted runner whenever code is pushed to the main branch.

In your instance's console, create a directory for the repository:

```console
mkdir test-repo && cd test-repo
echo "# test-repo" >> README.md
```

Then, create the GitHub Actions workflow file at `.github/workflows/deploy-nginx.yaml`.

```console
mkdir .github  && mkdir .github/workflows/
vim .github/workflows/deploy-nginx.yaml
```

Paste the following code block into the file and save it.

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

Now it's time to initiate your repository and push the changes.

```console
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/annietllnd/test-repo.git
git push -u origin main
```

This will trigger an actions job. The job will listen for a self-hosted runner to connect to the GitHub repository. Go back to the `actions-runner` directory and re-run the script from the previous section:

```bash
cd ..
./run.sh
```

You will see in the output of the command that it identifies the a job called `deploy`, and that it finishes after having run the two steps.

### Access the NGINX Server
Once the workflow completes, open your browser and navigate to your machine's external IP address. You will find the information in your instance overview, under **Network interfaces**.
```
http://<your-public-IP>
```
You should see the NGINX welcome page confirming a successful deployment.

![nginx](./images/nginx.png)

You should now know how to set up a self-hosted runner with an Arm-based Google Cloud instance, and use it to run GitHub Actions workflows. From here, you can modify the workflow file to try out different commands.
