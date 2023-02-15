---
title: "Setup a web server"
weight: 4
layout: "learningpathall"
---

## Prerequisites

A physical machine or cloud instance with Ubuntu and Nginx installed

## Setup a basic web server

Refer to the [documentation](https://docs.nginx.com/nginx/admin-guide/web-server/serving-static-content/) for additional details.

### Quick start 

Setup a basic web server.

Switch to root.

```console
sudo su -
```

Add the following code in **/etc/nginx/nginx.conf**

If the file already has information in it, remove and add the code below.

```console
user www-data;
worker_processes auto;
worker_rlimit_nofile 1000000;
pid /run/nginx.pid;
events {
 worker_connections 1024;
 accept_mutex off;
 multi_accept off;
}
http {
 ##
 # Basic Settings
 ##
 sendfile on;
 tcp_nopush on;
 tcp_nodelay on;
 keepalive_timeout 75;
 keepalive_requests 1000000000;
 types_hash_max_size 2048;
 include /etc/nginx/mime.types;
 default_type application/octet-stream;

 ##
 # Virtual Host Configs
 ##
 include /etc/nginx/conf.d/*.conf;
 include /etc/nginx/sites-enabled/*;
}
```

Add the following code in **/etc/nginx/conf.d/default.conf**

Replace **$hostname** with the DNS name of the machine. For AWS this would take the form of, ec2-23-20-129-140.compute-1.amazonaws.com

```console
# HTTPS server
server {
 listen 443 ssl reuseport backlog=60999;
 root /usr/share/nginx/html;
 index index.html index.htm;
 server_name $hostname;
 ssl on;
 ssl_certificate /etc/nginx/ssl/ecdsa.crt;
 ssl_certificate_key /etc/nginx/ssl/ecdsa.key;
 ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384;
 location / {
     limit_except GET {
         deny all;
     }
     try_files $uri $uri/ =404;
 }
}
```

Follow the [instructions](../key_and_certification) to create ECDSA key and certificate for the files ecdsa.crt and ecdsa.key in the code above. 

Come back to this point when done.

Check the configuration for correct syntax and then start the Nginx server using the commands below.

```console
nginx -t -v
```

Start Nginx using systemd.

```console
systemctl start nginx
```

To verify the web server is running, open the URL for the web server in a browser. 

You should see the content of your index.html file displayed.

The <dns-name> is the DNS name of the machine. 

```console
https://<dns-name>/
```

The browser will show the Nginx welcome message: 

![file_server_screenshot](https://user-images.githubusercontent.com/67620689/194551227-3590f90c-8c58-4f1d-bed6-71527cec7c62.PNG)

Make sure that port 443 or port 80 is open in the security group from the IP address of the browser.
