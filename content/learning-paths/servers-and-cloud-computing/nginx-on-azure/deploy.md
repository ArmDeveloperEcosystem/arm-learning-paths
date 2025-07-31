---
title: Install Nginx on Microsoft Azure Virtual Machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---



## Nginx Installation on Azure Linux 3.0

Install Nginx using `dnf`, start the service, and allow **HTTP/HTTPS** in the firewall. Then access the default welcome page using your virtual machine’s public IP in a browser.

### Install Nginx

```console
sudo dnf install -y nginx 
sudo systemctl enable nginx 
sudo systemctl start nginx
```

### Verify Nginx

```console
sudo systemctl status nginx 
```
You should see an output similar to:

```output
● nginx.service - Nginx High-performance HTTP server and reverse proxy
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: disabled)
    Drop-In: /usr/lib/systemd/system/service.d
             └─10-timeout-abort.conf
     Active: active (running) since Wed 2025-07-30 04:29:02 UTC; 2h 8min ago
   Main PID: 684 (nginx)
      Tasks: 2 (limit: 19091)
     Memory: 153.1M (peak: 155.2M)
        CPU: 30.234s
     CGroup: /system.slice/nginx.service
             ├─684 "nginx: master process /usr/sbin/nginx"
             └─685 "nginx: worker process"
```
Also, you can use the below command to see the installed version of Nginx:

```console
nginx -v
```
### Validation with curl
Validation with `curl` confirms that Nginx is correctly installed, running, and serving **HTTP** responses.

Run the following command to send a HEAD request to the local Nginx server:
```console
curl -I http://localhost/
```
The `curl -I http://localhost/` command sends a HEAD request to Nginx to check its **HTTP** response headers without downloading the page content.

You should see an output similar to:

```output
HTTP/1.1 200 OK
Server: nginx/1.25.4
Date: Wed, 30 Jul 2025 06:59:19 GMT
Content-Type: text/html
Content-Length: 615
Last-Modified: Tue, 29 Apr 2025 21:56:30 GMT
Connection: keep-alive
ETag: "68114b0e-267"
Accept-Ranges: bytes
```

Output summery:
- **HTTP/1.1 200 OK**: Nginx is responding successfully.
- **Server: nginx/1.25.4**: Confirms it's running Nginx.
- Confirms your web server is reachable on **localhost**.

### Allow HTTP Traffic in Firewall 

Allowing **HTTP** and **HTTPS** traffic in the firewall ensures that your Nginx web server can receive requests from web browsers. 
```console
sudo firewall-cmd --permanent --add-service=http 
sudo firewall-cmd --permanent --add-service=https 
sudo firewall-cmd --reload 
```
Now you can access the NGINX default page in a browser:

```console
http://<your-vm-public-ip>/ 
```
You should see the Nginx page confirming a successful installation of Nginx.
![nginx](./nginx-browser.png)

Nginx installation is complete. You can now proceed with the baseline testing.
