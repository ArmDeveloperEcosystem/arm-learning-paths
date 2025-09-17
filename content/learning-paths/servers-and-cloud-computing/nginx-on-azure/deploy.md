---
title: Install NGINX
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---



## NGINX Installation on Ubuntu Pro 24.04 LTS

Install NGINX using `apt` on your Ubuntu Pro 24.04 LTS virtual machine, start the NGINX service, and allow **HTTP** traffic through the firewall. Then access the default welcome page using your virtual machine’s public IP address in a browser.

### Install NGINX

```console
sudo apt update
sudo apt install -y nginx
sudo systemctl enable nginx
sudo systemctl start nginx
```

### Verify NGINX

```console
sudo systemctl status nginx
```
You should see an output similar to:

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
Also, you can use the below command to see the installed version of NGINX:

```console
nginx -v
```
{{% notice Note %}}
There is an [Arm community blog](https://community.arm.com/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/improve-nginx-performance-up-to-32-by-deploying-on-alibaba-cloud-yitian-710-instances) that shows that NGINX version 1.20.1 deployed on Yitian 710 based ECS provides up to 32% more throughput in compared to the equivalent x86 based ECS instances.
 
The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends NGINX version 1.20.1 as the minimum recommended on the Arm platforms.
{{% /notice %}}

### Validation with curl
Validation with `curl` confirms that NGINX is correctly installed, running, and serving **HTTP** responses.

Run the following command to send a HEAD request to the local NGINX server:
```console
curl -I http://localhost/
```
The `curl -I http://localhost/` command sends a HEAD request to NGINX to check its **HTTP** response headers without downloading the page content.

You should see an output similar to:

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

Output summery:
- **HTTP/1.1 200 OK**: nginx is responding successfully.
- **Server: nginx/1.24.0**: Confirms it's running nginx.
- Confirms your web server is reachable on **localhost**.

### Allow HTTP Traffic in Firewall(Optional)

On **Ubuntu Pro 24.04 LTS** virtual machines, **UFW (Uncomplicated Firewall)** is used to manage firewall rules. By default, it allows only SSH (port 22) and blocks most other traffic.  

So even if Azure allows HTTP on port 80 (added to inbound ports during Virtual Machine creation), your Virtual Machine’s firewall may still block it until you run:

```console
sudo ufw allow 80/tcp
sudo ufw enable
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

### Accessing the NGINX Default Page

You can access the NGINX default page from your Virtual machine’s public IP. Run the following command to display your public URL:

Now you can access the NGINX default page in a browser. Run the following command to print your Virtual machine’s public URL, then open it in a browser:
```console
echo "http://$(curl -s ifconfig.me)/"
```

Open the printed URL in a browser. You should see the NGINX welcome page confirming a successful installation.

![NGINX](images/nginx-browser.png)

NGINX installation is complete. You can now proceed with the baseline testing ahead.

