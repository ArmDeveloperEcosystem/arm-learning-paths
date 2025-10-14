---
title: Run the Buildkite Pipeline
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run the Buildkite Pipeline for Multi-Arch Builds

Follow these steps to run your pipeline on an Arm-based Buildkite agent.

### Ensure the Agent is Running

Before your pipeline can execute, the Buildkite agent must be running and connected to your Buildkite account:

```console
# If running manually
sudo /root/.buildkite-agent/bin/buildkite-agent start

# Or if using systemd
sudo systemctl start buildkite-agent
sudo systemctl status buildkite-agent
```
- The agent listens for jobs from Buildkite and executes your pipeline steps.
- Using `systemctl` ensures the agent starts automatically on VM boot.
- You should see logs showing “Registered agent” to confirm it’s online.

### Trigger the Pipeline

Trigger via Buildkite UI

- Open your pipeline in **Buildkite** → **Pipeline** page
- Click **“New Build”**  
- Select branch → **Start Build**

![Buildkite Dashboard alt-text#center](images/build-p.png "Figure 1: Trigger Pipeline")

- Triggering the pipeline tells Buildkite to start running the steps you defined in your YAML file.
- The pipeline steps will run on the ARM-based agent you set up.

### Monitor the Build

You can see the logs of your build live in the Buildkite UI.
Steps include:

- Docker login
- Buildx builder creation
- Multi-arch Docker image build and push

![Buildkite Dashboard alt-text#center](images/log.png "Figure 2: Monitor Build")

### Verify Multi-Arch Image

After the pipeline completes successfully, you can go to Docker Hub and verify the pushed multi-arch images:

![Docker-Hub alt-text#center](images/multi-arch-image.png "Figure 3: Docker image")

### Run the Flask Application on Arm
```console
docker pull <DOCKER_USERNAME>/multi-arch-app:latest
docker run --rm -p 80:5000 <DOCKER_USERNAME>/multi-arch-app:latest
```

This command runs the Flask application inside a container, exposing it on port 5000 inside the container and mapping it to port 80 on the host machine.

You can now visit the VM’s Public IP to access the Flask application.

```console
http://<VM_IP>
```
You should see output similar to:

![Buildkite Dashboard alt-text#center](images/browser.png "Figure 4: Verify Docker Images")

Your pipeline is working, and you have successfully built and ran the Flask application using your Arm-based Buildkite agent.
