---
title: Install and configure Gerrit on a Google Axion C4A virtual machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Gerrit 

Install and configure Gerrit Server on a Google Cloud Platform (GCP) Linux VM (Ubuntu 24.04 LTS-based VM). 

To ensure a successful setup, follow each step in order and check the output after each command. By doing this, you catch issues early and confirm that Gerrit is installed and running correctly.

### Set up your environment

Before installing Gerrit, update the system and install the required tools:

```console
sudo apt update && sudo apt upgrade -y
sudo apt install -y wget default-jdk git net-tools
```

### Download the Gerrit server package

Download the Gerrit server package for ARM64 architecture.

```console
mkdir -p ${HOME}/gerrit
wget -O gerrit.war https://gerrit-releases.storage.googleapis.com/gerrit-3.14.0.war
java -jar gerrit.war init -d ${HOME}/gerrit --dev --batch --install-all-plugins
```

### Verify service status

Verify the status of the service:

```console
ps -ef | grep Gerrit
```

The output is similar to:

```output
doug_an+   11807       1 18 21:01 ?        00:00:14 GerritCodeReview -Dflogger.backend_factory=com.google.common.flogger.backend.log4j.Log4jBackendFactory#getInstance -Dflogger.logging_context=com.google.gerrit.server.logging.LoggingContext#getInstance -jar /home/doug_anson_arm_com/gerrit/bin/gerrit.war daemon -d /home/doug_anson_arm_com/gerrit --run-id=1781730091.11737
```

## Check whether required ports are open

To confirm Gerrit is ready to accept connections, check that the required ports are open and listening. If you see `LISTEN` next to these ports, Gerrit is running and network services are available.

Gerrit uses port `8080` for its web console function.

Run the following command to verify the ports are active:

```console
netstat -a | grep http | grep LISTEN
```

The output is similar to:

```output
tcp6       0      0 [::]:http-alt           [::]:*                  LISTEN   
```

If you see `LISTEN` for the `http-alt` port, Gerrit is ready for baseline testing and further configuration. This confirms that the core Gerrit services are running and accessible on your Arm-based GCP VM.

## Confirm that the Gerrit dashboard is accessible

Using a browser and the "Public IP Address" saved off when the VM instance was created, go to the following URL in the browser: 

```output
http://my_vm_public_ip_address:8080
```

The output is similar to:

![Gerrit web console dashboard showing the main interface with navigation menu and project/change options available.#center](images/gerrit-dashboard.png "Gerrit dashboard")

## What you've accomplished and what's next

You've now installed and configured Gerrit on your Arm-based GCP C4A VM. 

Next, you'll benchmark Gerrit performance on the VM. 
