---
title: "Install NGINX"
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Install and verify NGINX on Ubuntu Pro 24.04 LTS (Azure Arm64)

In this section, you install and configure NGINX, a high-performance web server and reverse proxy, on your Azure Arm64 (Cobalt 100) virtual machine. NGINX is widely used to serve static content, handle large volumes of connections efficiently, and act as a load balancer. Running it on your Azure Cobalt 100 virtual machine allows you to serve web traffic securely and reliably.

## Install NGINX (apt)

Install NGINX from Ubuntu’s repositories on Ubuntu Pro 24.04 LTS.

Run the following commands to install and enable NGINX:

```console
sudo apt update
sudo apt install -y nginx
sudo systemctl enable nginx
sudo systemctl start nginx
```

## Verify NGINX is running

Check the installed version of NGINX:

```console
nginx -v
```

Expected output:

```output
nginx version: nginx/1.24.0 (Ubuntu)
```

{{% notice Note %}}
The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends NGINX version 1.20.1 or later for Arm platforms.
{{% /notice %}}

You can also confirm that NGINX is running correctly by checking its systemd service status:

```console
sudo systemctl status nginx
```

Expected output:

```output
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: enabled)
     Active: active (running) since Mon 2025-09-08 04:26:39 UTC; 20s ago
       Docs: man:nginx(8)
   Main PID: 1940 (nginx)
      Tasks: 5 (limit: 19099)
     Memory: 3.6M (peak: 8.1M)
        CPU: 23ms
     CGroup: /system.slice/nginx.service
             ├─1940 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             ├─1942 "nginx: worker process"
             ├─1943 "nginx: worker process"
             ├─1944 "nginx: worker process"
             └─1945 "nginx: worker process"
```

If you see `Active: active (running)`, NGINX is successfully installed and running.

## Validate HTTP response with curl

You can validate that NGINX is serving HTTP responses using `curl`:

```console
curl -I http://localhost/
```

The **-I** option requests only the HTTP response headers without downloading the page body.

Expected output:

```output
HTTP/1.1 200 OK
Server: nginx/1.24.0 (Ubuntu)
Date: Mon, 08 Sep 2025 04:27:20 GMT
Content-Type: text/html
Content-Length: 615
Last-Modified: Mon, 08 Sep 2025 04:26:39 GMT
Connection: keep-alive
ETag: "68be5aff-267"
Accept-Ranges: bytes
```

**Output summary**

| Field            | What it tells you                                   | Example                      |
|------------------|------------------------------------------------------|------------------------------|
| `HTTP/1.1 200 OK`| NGINX responded successfully                        | `HTTP/1.1 200 OK`            |
| Server       | NGINX and version returned by the server            | `nginx/1.24.0 (Ubuntu)`      |
| Content-Type | MIME type of the response                           | `text/html`                  |
| Content-Length | Size of the response body in bytes               | `615`                        |
| Last-Modified| Timestamp of the file served                        | `Mon, 08 Sep 2025 04:26:39 GMT` |
| ETag         | Identifier for the specific version of the resource | `68be5aff-267`             |


This confirms that NGINX is functional at the system level, even before exposing it to external traffic.

## Allow HTTP traffic (port 80) in UFW and NSG

When you created your VM instance earlier, you configured the Azure **Network Security Group (NSG)** to allow inbound HTTP (**port 80**) traffic. On the VM itself, you must also allow traffic through the Ubuntu firewall (**UFW**). Run:

```console
sudo ufw allow 80/tcp
sudo ufw enable
```

Expected output:

```output
sudo ufw enable
Rules updated
Rules updated (v6)
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
```

Verify that HTTP is allowed with:

```console
sudo ufw status
```

Expected output:

```output
Status: active

To                         Action      From
--                         ------      ----
8080/tcp                   ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
8080/tcp (v6)              ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)
```

This ensures that both Azure and the VM-level firewalls permit HTTP requests.

## Access the NGINX welcome page

You can now access the NGINX welcome page from your VM’s public IP address. Run:

```console
echo "http://$(curl -s ifconfig.me)/"
```

Copy the printed URL and open it in your browser. You should see the default NGINX welcome page, which confirms that HTTP traffic is reaching your VM.

![NGINX default welcome page in a web browser on an Azure VM alt-text#center](images/nginx-browser.png)

At this stage, your NGINX installation is complete. You are ready to begin baseline testing and further configuration.
