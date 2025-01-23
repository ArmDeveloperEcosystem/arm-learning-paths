---
title: "Install Daytona and run the server"
weight: 3

layout: "learningpathall"
---

## How do I install Daytona on Arm computers?

Installing Daytona on Arm-based computers is easy. 

The application is a single binary which you can place anywhere. 

To make it easy to run, you can add the location of the `daytona` binary to your search path.

You can install Daytona on a variety of operating systems, and these are described below.

### How do I install Daytona on macOS?

Use the following code:

```console
curl -sf -L https://download.daytona.io/daytona/install.sh | sudo bash
```

### How do I install Daytona on Arm Linux or Chrome OS?

Use the following code:

```console
curl -sf -L https://download.daytona.io/daytona/install.sh | sudo bash
```

### How do I install Daytona on Windows on Arm?

Copy the commands below and run them at a PowerShell Prompt:

```console
$architecture = if ($env:PROCESSOR_ARCHITECTURE -eq "AMD64") { "amd64" } else { "arm64" }
md -Force "$Env:APPDATA\bin\daytona"; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]'Tls,Tls11,Tls12';
Invoke-WebRequest -URI "https://download.daytona.io/daytona/v0.50/daytona-windows-$architecture.exe" -OutFile "$Env:APPDATA\bin\daytona\daytona.exe";
$env:Path += ";" + $Env:APPDATA + "\bin\daytona"; [Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::User);
```

You can also manually download the binary for a particular operating system and place it on your computer. 

See the [Daytona documentation](https://www.daytona.io/docs/installation/installation/) for further information. 

## How do I confirm that Daytona is installed? 

Print the version to confirm Daytona works on your computer:

```console
daytona --version
```

The output displays the installed version:

```output
Daytona version v0.50.0
```

## How do I start the Daytona server?

After installing Daytona, you need to start the Daytona server. 

{{% notice Note %}}
Always make sure that Docker is running before using Daytona.

Even if you plan to develop on remote computers, you will still need to have the server on your local machine.
{{% /notice %}}

There are three options that you can use to start the Daytona server.

Option 1: start the server in the background with a confirmation prompt:

```console
daytona server
```

Option 2: start the server in the background with no confirmation:

```console
daytona server -y
```

Option 3: start the server in the current terminal so you can see the output: 

```console
daytona serve
```

Running in the current terminal is the easiest way to learn about what Daytona is doing.

Below is the output from option 3:

```output
INFO[0000] Using default FRPS config
INFO[0000] Starting api server on port 3986
INFO[0000] Starting local container registry...
INFO[0000] Starting headscale server...
INFO[0002] Headscale server started
INFO[0002] Starting Daytona server
INFO[0002] Image already pulled
INFO[0010] Downloading default providers
INFO[0010] Downloading docker-provider
INFO[0011] Default providers downloaded
INFO[0011] Registering providers
INFO[0011] Provider docker-provider registered
INFO[0012] Setting preset targets for docker-provider
INFO[0012] Target local set
INFO[0012] Preset targets set for docker-provider
INFO[0012] Provider docker-provider initialized
INFO[0012] Provider requirement met: Docker is installed
INFO[0012] Provider requirement met: Docker is running
INFO[0012] Providers registered
INFO[0013] API REQUEST                                   URI=/health/ latency=1.322542ms method=GET status=200


    Daytona

   ## Daytona Server is running on port: 3986

   ===

   You may now begin developing
```

If you are curious, leave the Daytona server running in the terminal and watch the activity as you manage development environments.

## How do I stop the Daytona server?

If the server is running in the terminal, you can stop it by using Control-C.

If the server is running in the background, you can use the command below to stop it:

```console
daytona server stop
```

## How do I uninstall Daytona?

You can uninstall Daytona using:

```console
daytona purge
```

{{% notice Note %}}
If you experience difficulties with running Daytona on macOS, remove the directory `$HOME/Library/Application\ Support/daytona`
{{% /notice %}}

With Daytona installed and the server running, you are now ready to learn about configuring Daytona.
