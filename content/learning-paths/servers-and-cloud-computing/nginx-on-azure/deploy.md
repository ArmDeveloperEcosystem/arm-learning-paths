---
title: Install NGINX
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---



## NGINX Installation on Ubuntu Pro 24.04 LTS

In this section, you will install and configure NGINX, a high-performance web server and reverse proxy on your Arm-based Azure instance. NGINX is widely used to serve static content, handle large volumes of connections efficiently, and act as a load balancer. Running it on your Azure Cobalt-100 virtual machine will allow you to serve web traffic securely and reliably.

### Install NGINX

Run the following commands to install and enable NGINX:

```console
sudo apt update
sudo apt install -y nginx
sudo systemctl enable nginx
sudo systemctl start nginx
```

### Verify NGINX

Check the installed version of NGINX:

```console
nginx -v
```
The output should look like:

```output
nginx version: nginx/1.24.0 (Ubuntu)
```
{{% notice Note %}}

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends NGINX version 1.20.1 as the minimum recommended on the Arm platforms.

{{% /notice %}}

You can confirm that NGINX is running correctly by checking its systemd service status:
```console
sudo systemctl status nginx
```
You should see output similar to:

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
If you see Active: active (running), NGINX is successfully installed and running.


### Validation with curl
Validation with `curl` confirms that NGINX is correctly installed, running, and serving **HTTP** responses.

Run the following command to send a HEAD request to the local NGINX server:
```console
curl -I http://localhost/
```
The -I option tells curl to request only the HTTP response headers, without downloading the page body.

You should see output similar to:

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

Output summary:
- HTTP/1.1 200 OK: Confirms that NGINX is responding successfully.
- Server: nginx/1.24.0: Shows that the server is powered by NGINX.
- Content-Type, Content-Length, Last-Modified, ETag: Provide details about the served file and its metadata.

This step verifies that your NGINX installation is functional at the system level, even before exposing it to external traffic. It’s a quick diagnostic check that is useful when troubleshooting connectivity issues.

### Allowing HTTP Traffic

When you created your VM instance earlier, you configured the Azure Network Security Group (NSG) to allow inbound HTTP (port 80) traffic. This means the Azure-side firewall is already open for web requests.
On the VM itself, you still need to make sure that the Uncomplicated firewall (UFW) which is used to manage firewall rules on Ubuntu allows web traffic. Run:


```console
sudo ufw allow 80/tcp
sudo ufw enable
```
The output from this command should look like:

```output
sudo ufw enable
Rules updated
Rules updated (v6)
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
```
You can verify that HTTP is now allowed with:

```console
sudo ufw status
```
You should see an output similar to: 
```output
Status: active

To                         Action      From
--                         ------      ----
8080/tcp                   ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
8080/tcp (v6)              ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)
```
This ensures that both Azure and the VM-level firewalls are aligned to permit HTTP requests.

### Accessing the NGINX Default Page

You can now access the NGINX default page from your Virtual machine’s public IP address. Run the following command to display your public URL:

```console
echo "http://$(curl -s ifconfig.me)/"
```
Copy the printed URL and open it in your browser. You should see the default NGINX welcome page, which confirms a successful installation and that HTTP traffic is reaching your VM.

![NGINX](images/nginx-browser.png)

At this stage, your NGINX installation is complete. You are now ready to proceed with baseline testing and further configuration.
