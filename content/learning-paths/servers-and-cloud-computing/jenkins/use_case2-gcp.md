---
title: Jenkins Use Case 2 – Docker-based CI Pipeline on Arm64
weight: 11

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Jenkins Use Case – Docker-based CI Pipeline on Arm64
This use case demonstrates how to use **Jenkins on a GCP SUSE Arm64 VM** to build and run a **Docker container natively on Arm64**. It validates Docker installation, Jenkins–Docker integration, and Arm-native container execution.

### Prerequisites
Before starting, ensure the following components are already available and working:

* Jenkins is installed and running on a GCP SUSE Arm64 VM

* Jenkins web UI is accessible

* Docker installed on the VM

* Jenkins user added to Docker group

### Install Docker on SUSE Linux (Arm64)
This step installs Docker using the SUSE package manager so containers can be built and run on the VM.

```bash
sudo zypper refresh
sudo zypper install -y docker
```

### Enable and start Docker service
Docker must be running as a background service to accept commands from Jenkins.

```console
sudo systemctl enable docker
sudo systemctl start docker
```

### Allow Jenkins to Use Docker
By default, Jenkins does not have permission to access Docker. This step grants Docker access to the Jenkins user.

**Add Jenkins user to Docker group:**

```console
sudo usermod -aG docker jenkins
```

### Restart services
Restarting services ensures the new permissions take effect.

```console
sudo systemctl restart docker
sudo systemctl restart jenkins
```

### Verify Docker access as Jenkins
This step confirms that Jenkins can successfully run Docker commands.

```console
sudo -u jenkins docker version
```

### Prepare Jenkins Workspace
All demo files must be created inside the Jenkins workspace so the pipeline can access them during execution.

### Switch to Jenkins user

```console
sudo -u jenkins bash
```

### Navigate to Jenkins job workspace
This directory matches the Jenkins job name and is where pipeline files are stored.

```console
cd /var/lib/jenkins/workspace/docker-Arm-ci
```

`docker-Arm-ci` must match your Jenkins job name.

### Create Docker demo directory
This directory will hold the Dockerfile used in the pipeline.

```console
mkdir docker-demo
cd docker-demo
```

### Create Arm64 Dockerfile
This Dockerfile uses an Arm64-native base image and prints a message when the container runs.

```bash
cat <<EOF > Dockerfile
FROM Arm64v8/alpine:latest
CMD ["echo", "Hello from Arm64 Docker container"]
EOF
```

**Dockerfile details:**

- Uses an Arm64-native base image
- Prints a message when the container runs

### Exit Jenkins shell
Return to your normal user account after preparing the workspace.

```console
exit
```

### Create Jenkins Pipeline Job
This section configures Jenkins to build and run the Docker container automatically.

#### Step 1: Open Jenkins UI

```console
http://<VM_PUBLIC_IP>:8080
```

#### Step 2: Create a new Pipeline job
Create a Jenkins job that defines the Docker-based CI workflow.

* Open Jenkins UI
  
* Click **New Item**

* Job name: `docker-Arm-ci`

* Select **Pipeline**

* Click **OK**

![ Jenkins UI alt-text#center](images/new-item.png "Figure 1: Create Item")

#### Step 3: Jenkins Pipeline Script (Docker Arm Validation)
This pipeline checks the system architecture, builds an Arm64 Docker image, and runs the container.

* Scroll to the **Pipeline** section and select:

* **Definition:** Pipeline script

Paste the following into the Pipeline script section:

```groovy
pipeline {
  agent any

  stages {
    stage('Environment Check') {
      Steps {
        sh 'uname -m'
        sh 'docker version'
      }
    }

    stage('Build Docker Image') {
      Steps {
        sh '''
          cd docker-demo
          docker build -t Arm64-docker-test .
        '''
      }
    }

    stage('Run Docker Container') {
      Steps {
        sh '''
          docker run --rm Arm64-docker-test
        '''
      }
    }
  }
}
```

Click **Save**.

![ Jenkins UI alt-text#center](images/docker-pipeline.png "Figure 2: Create Pipeline")


#### Step 4: Execute the Pipeline
Run the pipeline to verify Docker-based CI execution on Arm64.

* On the job page, click **Build Now**

* Click the build number
  
![ Jenkins UI alt-text#center](images/docker-build.png "Figure 3: Execute Job")

#### Step 4: View console output
Review the logs to confirm that each pipeline stage completed successfully.

* Click the build number (for example, `#1`)

* Click **Console Output**

![ Jenkins UI alt-text#center](images/docker-output.png "Figure 3: Output")

### The output confirms

- Jenkins is running on Arm64
- Docker is Arm-native
- Jenkins can build and run containers
- End-to-end Docker CI works on Arm

### Use Case Summary

This use case validates Docker-based CI pipelines using Jenkins on a GCP SUSE Arm64 VM. Docker installation, Jenkins–Docker integration, Arm-native image builds, and container execution are successfully verified. The system is now ready for Arm-native containerized CI/CD workloads.
