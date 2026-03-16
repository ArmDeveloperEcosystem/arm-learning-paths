---
title: Install Dynatrace OneAgent on Azure Ubuntu Arm64 virtual machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Dynatrace OneAgent on Azure Ubuntu Arm64

To install Dynatrace OneAgent on an Azure Ubuntu 24.04 LTS Arm64 virtual machine, follow these steps.

At the end of the installation, Dynatrace is:

* Installed and running as a host monitoring agent
* Connected to the Dynatrace SaaS environment
* Monitoring system processes and services automatically
* Verified on Arm64 (aarch64) architecture

## Update the system and install required tools

Update the operating system and install the tools required for downloading the Dynatrace installer.

```console
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl wget unzip ca-certificates
```

## Verify Arm64 architecture

Confirm that the virtual machine is running on the Arm64 architecture.

```console
uname -m
```

output is similar to:
```output
aarch64
```
This confirms the system is using the Arm64 architecture required for Cobalt 100 processors.

## Create your Dynatrace trial environment

Fill in the required information:

- First name
- Last name
- Work email address
- Company name
- Country

After submitting the form, Dynatrace creates a new SaaS monitoring environment for you.

This process usually takes 1–2 minutes.

## Access your Dynatrace environment

After the environment is created, you will receive an email with a link similar to:

```console
https://<ENVIRONMENT-ID>.live.dynatrace.com
```

**Example:**

```text
https://qzo72404.live.dynatrace.com
```
The Environment ID uniquely identifies your Dynatrace tenant and is required for agent installation.

![Dynatrace environment login page showing the SaaS environment URL alt-txt#center](images/dynatrace-env-id.png "Dynatrace SaaS environment login")

## Navigate to Deployment

From the Dynatrace dashboard:

- Select Deploy Dynatrace
- Choose OneAgent
- Select Linux

![Dynatrace deployment page showing OneAgent setup options alt-txt#center](images/oneagent1.png "Dynatrace OneAgent deployment setup page")

This page generates the installation command tailored for your environment.

## Select ARM Architecture

In the installer page:

- Cloud platform → Linux
- Select architecture → ARM64
- Select monitoring mode:
  >Full-stack monitoring

![Dynatrace installer configuration page showing ARM64 architecture selection alt-txt#center](images/oneagent-arch.png "Dynatrace OneAgent ARM64 architecture selection")

## Copy OneAgent Installer Command

Dynatrace generates an installer command that includes your environment ID and API token.:

```console
wget -O Dynatrace-OneAgent-Linux-arm.sh \
"https://<ENV>.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=arm" \
--header="Authorization: Api-Token <API_TOKEN>"
```

**Example:**

```text
wget -O Dynatrace-OneAgent-Linux-arm.sh \
"https://qzo72404.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=arm" \
--header="Authorization: Api-Token DT_API_TOKEN"
```
- The API token allows secure access to the Dynatrace installer.

Run this command on the virtual machine to download the installer.

**Verify signature**

For security, verify the installer signature using Dynatrace’s root certificate.

```console
wget https://ca.dynatrace.com/dt-root.cert.pem ; ( echo 'Content-Type: multipart/signed; protocol="application/x-pkcs7-signature"; micalg="sha-256"; boundary="--SIGNED-INSTALLER"'; echo ; echo ; echo '----SIGNED-INSTALLER' ; cat Dynatrace-OneAgent-Linux-x86-1.331.49.20260227-104933.sh ) | openssl cms -verify -CAfile dt-root.cert.pem > /dev/null
```
Run it on the VM.

![Dynatrace UI displaying the generated OneAgent installer command alt-txt#center](images/onagent-install.png "Dynatrace OneAgent installation command")

## Install OneAgent as the privileged user

Run:

```console
sudo /bin/sh Dynatrace-OneAgent-Linux-x86-1.331.49.20260227-104933.sh --set-monitoring-mode=fullstack --set-app-log-content-access=true
```

The output is similar to: 
```output
2026-03-12 05:59:21 UTC Starting Dynatrace ActiveGate AutoUpdater...
2026-03-12 05:59:21 UTC Checking if Dynatrace ActiveGate AutoUpdater is running ...
2026-03-12 05:59:21 UTC Dynatrace ActiveGate AutoUpdater is running.
2026-03-12 05:59:21 UTC Cleaning autobackup...
2026-03-12 05:59:21 UTC Removing old installation log files...
2026-03-12 05:59:21 UTC
2026-03-12 05:59:21 UTC --------------------------------------------------------------
2026-03-12 05:59:21 UTC Installation finished successfully.
```

The installer performs several tasks automatically:

- Downloads monitoring components
- Configures kernel instrumentation
- Installs the OneAgent system service
- Registers the host with your Dynatrace environment

## Verify OneAgent Service

Check that the Dynatrace monitoring service is running.

This confirms the monitoring agent started successfully.
```console
sudo systemctl status oneagent
```

The output is similar to: 
```output
● dynatracegateway.service - Dynatrace ActiveGate service
     Loaded: loaded (/etc/systemd/system/dynatracegateway.service; enabled; preset: enabled)
     Active: active (running) since Thu 2026-03-12 05:59:07 UTC; 1min 7s ago
    Process: 20280 ExecStart=/opt/dynatrace/gateway/dynatracegateway start (code=exited, status=0/SUCCESS)
   Main PID: 20316 (dynatracegatewa)
```

This confirms the monitoring agent started successfully.

## Verify Dynatrace Processes

This confirms the monitoring agent started successfully.

```console
ps aux | grep oneagent
```

The output is similar to: 
```output
dtuser     17754  0.0  0.0 307872  4388 ?        Ssl  05:48   0:00 /opt/dynatrace/oneagent/agent/lib64/oneagentwatchdog -bg -config=/opt/dynatrace/oneagent/agent/conf/watchdog.conf
dtuser     17761  0.2  0.3 1183000 59136 ?       Sl   05:48   0:06 oneagentos -Dcom.compuware.apm.WatchDogTimeout=900 -watchdog.restart_file_location=/var/lib/dynatrace/oneagent/agent/watchdog/watchdog_restart_file -Dcom.compuware.apm.WatchDogPipe=/var/lib/dynatrace/oneagent/agent/watchdog/oneagentos_pipe_17754
dtuser     17793  0.0  0.2 689184 34408 ?        Sl   05:48   0:01 oneagentloganalytics -Dcom.compuware.apm.WatchDogTimeout=900 -Dcom.compuware.apm.WatchDogPipe=/var/lib/dynatrace/oneagent/agent/watchdog/oneagentloganalytics_pipe_17754
dtuser     17795  0.1  0.2 361936 42940 ?        Sl   05:48   0:04 oneagentnetwork -Dcom.compuware.apm.WatchDogTimeout=900 -Dcom.compuware.apm.WatchDogPipe=/var/lib/dynatrace/oneagent/agent/watchdog/oneagentnetwork_pipe_17754
dtuser     17883  0.0  0.0  28212  5340 ?        Sl   05:49   0:00 /opt/dynatrace/oneagent/agent/lib64/oneagentebpfdiscovery --log-dir /var/log/dynatrace/oneagent/os/ --log-no-stdout --log-level info
azureus+   23847  0.0  0.0   9988  2772 pts/0    S+   06:33   0:00 grep --color=auto oneagent
```

This confirms the monitoring agent started successfully.

## Confirm Host Detection in Dynatrace

Return to the Dynatrace web interface.

Navigate to:

```text
Infrastructure & Operations
→ Hosts
```

You should see:

```outout
Host name: <vm-name>
OS: Linux
Architecture: ARM64
Monitoring mode: Full Stack
```

![Dynatrace hosts dashboard showing detected ARM64 virtual machine alt-txt#center](images/dynatrace-host.png "Dynatrace host monitoring dashboard")

## Check Automatic Process Discovery

Dynatrace automatically discovers running applications and services.

View them under:

```text
Hosts → Processes
```

Dynatrace identifies services such as:

- system processes
- web servers
- databases
- container runtimes

![Dynatrace process monitoring dashboard showing automatically discovered services alt-txt#center](images/dynatrace-process.png "Dynatrace process discovery view")

## What you've accomplished and what's next

You've successfully installed Dynatrace OneAgent on your Azure Ubuntu Arm64 virtual machine. Your installation includes:

- Dynatrace OneAgent is installed and running as a system service
- Automatic startup enabled through systemd
- Secure connection to the Dynatrace SaaS platform
- Full-stack monitoring of system resources and processes
- Arm64-native monitoring on Azure Cobalt 100 processors

Next, you'll install Dynatrace ActiveGate to enable additional capabilities such as Kubernetes monitoring, secure data routing, and extension support.
