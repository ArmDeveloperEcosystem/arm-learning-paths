---
title: Jenkins Baseline Testing
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Jenkins Baseline Validation on Azure Ubuntu Arm64
This document validates a **working Jenkins LTS setup** on an **Azure Ubuntu 24.04 Arm64 VM** after installation is complete.
It focuses on **service health, network access, ARM verification, and a first pipeline run**.

### Network Verification
This section verifies that Jenkins is reachable over the network and properly exposed on the expected port.

Ensure Jenkins is listening on port **8080** and that the port is allowed at both the Azure and VM levels.

#### Verify Jenkins is listening on port 8080
Confirm that the Jenkins service is actively listening on port 8080 on the VM.

```console
ss -lntp | grep 8080
```

Expected output indicates Jenkins is listening:
```output
LISTEN 0 50 *:8080 *:*
```

#### Azure Network Security Group (NSG)
Ensure inbound access to Jenkins is allowed at the Azure networking layer.

Verify that an inbound NSG rule exists with the following configuration:

* **Port**: 8080
* **Protocol**: TCP
* **Action**: Allow
* **Source**: Internet (or your IP range)

### Retrieve Initial Admin Password
This step retrieves the automatically generated Jenkins administrator password required for first-time login.

```console
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

Copy and securely store this password for UI access.

### Verify Jenkins User and Home Directory
Validate that the Jenkins service user exists and that the Jenkins home directory is correctly configured.

```console
id jenkins
ls -ld /var/lib/jenkins
```

You should see an output similar to:
```output
drwxr-xr-x 12 jenkins jenkins 4096 Dec 16 06:11 /var/lib/jenkins
```

### Verify Jenkins Process
Confirm that the Jenkins process is running and managed by the system.

```console
ps -ef | grep jenkins
```

You should see an output similar to:
```output
jenkins    11986       1  9 06:04 ?        00:00:38 /usr/bin/java -Djava.awt.headless=true -jar /usr/share/java/jenkins.war --webroot=/var/cache/jenkins/war --httpPort=8080
azureus+   15126    2233  0 06:11 pts/0    00:00:00 grep --color=auto jenkins
```

### Verify ARM Architecture
Ensure the VM is running on Arm64 architecture.

```console
uname -m
```

You should see an output similar to: 
```text
aarch64
```

### Access Jenkins UI
This step confirms browser-based access to the Jenkins web interface.

**Open Jenkins in a local browser:**

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

### Execute First Jenkins Pipeline
This section confirms Jenkins can run jobs successfully on Arm.

#### Step 1: Open Jenkins Dashboard
Navigate to the Jenkins dashboard and authenticate using the configured credentials.

```text
http://<VM_PUBLIC_IP>:8080
```

**Log in using your Jenkins credentials:**

![ Jenkins UI alt-text#center](images/jenkins-login-page.png "Figure 4: Jenkins Login Page")

#### Step 2: Create a New Pipeline Job
Create a basic pipeline job to validate execution capability.

1. Click **New Item** (left sidebar)

2. Enter item name:

```text
armbaseline-pipeline
```

3. Select **Pipeline**

4. Click **OK**

![ Jenkins UI alt-text#center](images/jenkins-item.png "Figure 5: New Item")

#### Step 3: Add the Pipeline Script
Configure a simple pipeline to validate ARM architecture and Java availability.

Scroll to the **Pipeline** section.

* **Definition**: Pipeline script

Paste the following script:

```groovy
pipeline {
  agent any

  stages {
    stage('ARM Validation') {
      steps {
        sh 'echo "Architecture:"'
        sh 'uname -m'

        sh 'echo "Java Version:"'
        sh 'java -version'
      }
    }
  }
}
```

Click **Save**.

![Jenkins UI alt-text#center](images/jenkins-pipeline.png "Figure 6: Create Pipeline ")

#### Step 4: Run the Pipeline
Trigger the pipeline execution and observe build progress.

1. On the job page, click **Build Now**

2. A build number will appear under **Build History**

![ Jenkins UI alt-text#center](images/jenkins-job.png "Figure 7: Run Pipeline")

#### Step 5: View Console Output
Review the pipeline logs to confirm successful execution.

1. Click the build number (for example, `#1`)

2. Click **Console Output**

![Jenkins UI alt-text#center](images/jenkins-output.png "Figure 8: Console Output ")

### Baseline Validation Result

Successful execution confirms:

* Jenkins LTS is running correctly
* Java 17 is properly configured
* Jenkins jobs execute natively on ARM64

### Baseline Summary

This baseline validates a successful Jenkins LTS setup on Azure Ubuntu Arm64 using Java 17. Service health, UI accessibility, system verification, and ARM-native pipeline execution are confirmed.
The system is now ready for CI/CD workloads on Arm architecture.
