---
title: Jenkins Use Case 1 – Arm-Native Go CI Pipeline on Jenkins (GCP SUSE Arm64)
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Jenkins Use Case - Arm-Native Go CI Pipeline on Jenkins (GCP SUSE Arm64)
This use case demonstrates how to validate **Arm-native CI execution** on a **GCP SUSE Arm64 VM** using Jenkins.
A simple Go application is built and executed to confirm that Jenkins, Go, and the underlying system are running natively on **aarch64**.

### Network Verification
Ensure Jenkins is listening on port **8080** and accessible.

```console
ss -lntp | grep 8080
```

You should see an output similar to:
```output
LISTEN 0 50 *:8080 *:*
```
Also, confirm that the VM firewall and GCP firewall rules allow inbound traffic on port **8080**.

### Retrieve Initial Admin Password
Jenkins generates a one-time administrator password during the first startup. This step retrieves that password so you can log in to the UI.

```console
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

Copy and securely store this password for UI access.

### Access Jenkins UI
This step verifies that the Jenkins web interface is accessible from your browser.

Open Jenkins using the VM’s public IP address:

```text
http://<VM_PUBLIC_IP>:8080
```

### Complete UI Setup
Complete the initial Jenkins setup using the web interface.

1. Paste the initial admin password

![ Jenkins UI alt-text#center](images/initial-setup.png "Figure 1: Initial-Jenkins_page")

2. Select **Install suggested plugins**

![ Jenkins UI alt-text#center](images/jenkins-plugins.png "Figure 2: New Item")

3. Create an admin user

![ Jenkins UI alt-text#center](images/jenkins-admin.png "Figure 3: Install Plugins")

4. Finish setup and reach the Jenkins dashboard

### Prepare Go Application on the VM
This section prepares a simple Go application that will be built and executed by Jenkins.

#### Install Go
Install the Go programming language on the SUSE Arm64 VM.

```console
sudo zypper install -y go
```

Verify Go installation:

```console
go version
```

You should see an output similar to:
```output
go version go1.x.x linux/Arm64
```

#### Create a Sample Go Application
Create a small Go program to use in the Jenkins pipeline.

```console
mkdir -p ~/go-demo
cd ~/go-demo
```

Create `main.go`:

```console
cat <<EOF > main.go
package main

import "fmt"

func main() {
    fmt.Println("Hello from Go on Arm64 via Jenkins")
}
EOF
```

**Initialize the Go module:**

```console
go mod init go-demo
```

Test the application locally to ensure it works:

```console
go run main.go
```

### Create Jenkins Pipeline Job
This section creates a Jenkins pipeline to build and run the Go application automatically.

#### Step 1: Create New Job
Create a new Jenkins pipeline job.

* Open Jenkins UI

* Click **New Item**

* Job name: `go-Arm-ci`

* Select **Pipeline**

* Click **OK**

![ Jenkins UI alt-text#center](images/jenkins-go.png "Figure 4: Create Job")

#### Step 2: Configure Pipeline Script
Define the steps Jenkins will execute during the build.

In the **Pipeline** section:

* Set **Definition** to **Pipeline script**

* Paste the following script:

```groovy
pipeline {
  agent any

  stages {
    stage('Environment Check') {
      steps {
        sh 'uname -m'
        sh 'go version'
      }
    }

    stage('Build Go App') {
      steps {
        sh '''
          cd $WORKSPACE
          cp -r /home/gcpuser/go-demo .
          cd go-demo
          go build -o app
        '''
      }
    }

    stage('Run Binary') {
      steps {
        sh '''
          cd $WORKSPACE/go-demo
          ./app
        '''
      }
    }
  }
}
```

Click **Save**.

![ Jenkins UI alt-text#center](images/go-pipeline.png "Figure 5: Create Job")

#### Step 3: Run the Pipeline
Trigger the pipeline to verify execution.

* On the job page, click **Build Now**

* Click the build number

![ Jenkins UI alt-text#center](images/go-build.png "Figure 6: Run Job")

#### Step 4: View Console Output
Review the console logs to confirm that the Go application was built and executed successfully.

* Click the build number (for example, `#1`)

* Click **Console Output**

![Jenkins UI alt-text#center](images/jenkins-output.png "Figure 8: Console Output ")


### Validation Criteria

This use case confirms:

* Jenkins jobs execute successfully on Arm64
* Go toolchain runs natively on aarch64
* Jenkins workspace and filesystem handling are correct
* End-to-end CI execution works on GCP SUSE Arm64

### Use Case Summary

This use case validates an Arm-native Jenkins CI pipeline by building and executing a Go application on a GCP SUSE Arm64 VM.
It confirms correct Jenkins configuration, Go module handling, and native Arm execution suitable for cloud-native CI workloads.
