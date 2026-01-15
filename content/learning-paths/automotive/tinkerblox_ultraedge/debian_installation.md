---
title: DEBIAN Installation - UltraEdge

weight: 4

layout: "learningpathall"
---

#### Installation Process

{{% notice Note %}}
REMOVE ME:  Need link information to "Uncloud" below...  
{{% /notice %}}

-   Copy device installation details from **Uncloud**.
-   Device Initialization

    1.  Copy the command below into the clipboard.
    2.  Open terminal on your device.
    3.  Paste the copied command into terminal to initialize the device.


 {{% notice Note %}}
REMOVE ME:  Not sure what "example code" means below... is this what the user needs to execute or is it just an example?
{{% /notice %}}

    Just an example code. You will find the exact to execute for your device in unclound
    ```bash
    sudo apt update && sudo apt install curl && sudo apt install jq -y && sudo DEVICE_ID="5b3ff290-0c88-4cd9-8ef7-08de0bded9df" KEY="TB.ApiKey-mlBZgDFc7qyM6ztPjILBCbFEqnVlbvjUpM1Q1IqNP6tA7wNdi97AQ==" sh -c "$(curl "https://tinkerbloxdev.blob.core.windows.net:443/tinkerbloxdev/binaries/installer.sh?sv=2025-01-05&st=2025-11-03T06%3A31%3A55Z&se=2025-11-03T06%3A56%3A55Z&sr=b&sp=r&sig=HNS70HgJyHlhCVQrqvpGdCcaf8%2FtVjdW4RNiiiIPCSUA%3D")"
    ```

-   Paste the copied content in the target terminal and execute.

#### Activation of Agent

On the first boot, the agent will automatically generate a file named
`activation_key.json` at the path:

    /opt/tinkerblox/activation_key.json

Share this `activation_key.json` file with the TinkerBlox team to
receive license key (which includes license metadata).

1.  Stop the agent using the following command:

        sudo systemctl stop ultraedge.service

2.  Replace the existing `activation_key.json` file in
    `/opt/tinkerblox/` with the licensed one provided by TinkerBlox.

3.  Start the agent:

        sudo systemctl start ultraedge.service

#### Manual Running

-   Binary path: `/usr/bin/EdgeBloXagent`

-   To start:

        EdgeBloXagent

-   To stop, press <span class="kbd">Ctrl</span> +
    <span class="kbd">C</span> once.

## MicroPac Installation

{{% notice Note %}}
REMOVE ME:  Is MicroPac only for Debian installations?  Not for YOCTO ones?
{{% /notice %}}

#### System Requirements

-   Linux host (aarch64)
-   Sudo permissions
-   Overlay filesystem support
-   Internet connection

#### Required Packages

    sudo apt-get update
    sudo apt-get install -y tar curl qemu-user-static binfmt-support

### Cross-Architecture Support

{{% notice Note %}}
REMOVE ME:  Might need a bit more detail on why this needs to be executed (below): 
{{% /notice %}}

To build MicroPac for different architectures:
    # Enable binfmt for armv7
    sudo update-binfmts --enable qemu-armv7

### Installation

-   The package is provided as a `.deb` file.

-   Install it on your host machine:

        sudo apt install ./<package_name>.deb

### MicroPac File Schema file creation/setup

{{% notice Note %}}
REMOVE ME:  Need more information on how to setup your project directory/where its located
{{% /notice %}}

Place a `MicroPacFile` in your project directory.

```console
    name: nginx
    version: 1.0.0.0
    target: aarch64
    applicationType: custom
    image: Alpine:3.21
    createdBy: developer@tinkerblox.io
    description: Nginx web server microservice

    buildSteps:
      # Install nginx and create necessary directories
      - run: apk add --no-cache nginx
      - run: mkdir -p /var/www/html /var/log/nginx /var/lib/nginx /var/tmp/nginx

      # Copy configuration files
      - copy: [nginx.conf, /etc/nginx/nginx.conf]
      - copy: [index.html, /var/www/html/index.html]
      - copy: [404.html, /var/www/html/404.html]

      # Copy startup script
      - workdir: /app
      - copy: [nginx_start.sh, .]
      - run: chmod +x ./nginx_start.sh

      # Set proper permissions
      #- run: chown -R nginx:nginx /var/www/html /var/log/nginx /var/lib/nginx /var/tmp/nginx

    entry: /app/nginx_start.sh
    mode: continuous-run

    env:
      NGINX_PORT: 8080
      APP_ENV: production

    network:
      mode: host
      name: nginx-net
```
### Configuration Fields

#### Required Fields

-   **name**: Application name (≤ 10 characters)
-   **version**: Application version
-   **target**: Target architecture
-   **applicationType**: Application type (python, binary, custom)
-   **image**: Base image
-   **entry**: Entry point command
-   **mode**: single-run

#### Optional Fields

-   **env**: Environment variable
-   **buildSteps**: Array of build instructions
-   **limits**: Resource limits (memory, cpu)
-   **mount**: Volume mount points
-   **network**: Network configuration
-   **createdBy**: maintainer of the application
-   **description**: description of the application

### Building the MicroPac

Navigate to your project directory and execute:

    sudo micropac-builder build

This generates a file named `<project_name>.mpac`.

{{% notice Note %}}
REMOVE ME:  Is there a way to confirm that Micropac is properly setup now?
{{% /notice %}}
