---
title: "Setup Reverse Proxy and API Gateway"
weight: 5
layout: "learningpathall"
---

## Prerequisites

A physical machine or cloud instance with Ubuntu and Nginx installed.

Setup two [basic web servers](../basic_static_file_server) using the previous step, this is the third machine that will serve as a reverse proxy.

This section creates 2 upstream web servers behind the reverse proxy or API Gateway. You can create as many upstream web servers as you wish, but the code assumes two are already created.

## Setup a Reverse Proxy and API Gateway

The steps below are used to setup Reverse Proxy and API Gateway.

### Quick start 

Switch to root.

```console
sudo su -
```

Add the following code in **/etc/nginx/nginx.conf**:

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

If the file already has information in it, remove and add the code below.

Replace **$hostname** with the DNS name of the machine. For AWS this would take the form of, ec2-23-20-129-140.compute-1.amazonaws.com

Replace <private_ip_1> and <private_ip_2> are the private IP of the upstream web servers that were created in the previous step.

```console
# Upstreams for https
upstream ssl_file_server_com {
 server <private_ip_1>:443;
 server <private_ip_2>:443;
 keepalive 1024;
}

# HTTPS reverse proxy and API Gateway
server {
 listen 443 ssl reuseport backlog=60999;
 root /usr/share/nginx/html;
 index index.html index.htm;
 server_name $hostname;
 ssl on;
 ssl_certificate /etc/nginx/ssl/ecdsa.crt;
 ssl_certificate_key /etc/nginx/ssl/ecdsa.key;
 ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384;

 # API Gateway Path
 location ~ ^/api_old/.*$ {
 limit_except GET {
 deny all;
 }
 rewrite ^/api_old/(.*)$ /api_new/$1 last;
 }
 location /api_new {
 internal;
 proxy_pass https://ssl_file_server_com;
 proxy_http_version 1.1;
 proxy_set_header Connection "";
 }

 # Reverse Proxy Path
 location / {
 limit_except GET {
 deny all;
 }
 proxy_pass https://ssl_file_server_com;
 proxy_http_version 1.1;
 proxy_set_header Connection "";
 }
}
```


Follow the [instructions](../key_and_certification) to create ECDSA key and certificate for the files ecdsa.rt and ecdsa.key in the code above.

Come back to this point when done.

Check the configuration for correct syntax run and then start Nginx server using the commands below.

```console
nginx -t -v
```

Start Nginx using systemd.

```console
systemctl start nginx
```

Verify the reverse proxy and API gateway.

Run the following commands on the two upstream web servers to generate the files to be served.

```console
# Create 1kb file in RP use case directory
dd if=/dev/urandom of=/usr/share/nginx/html/1kb bs=1024 count=1
# Copy files into the APIGW use case directory
mkdir -p /usr/share/nginx/html/api_new
cp /usr/share/nginx/html/1kb /usr/share/nginx/html/api_new
```

Verify the reverse proxy server is running by opening the URL in your browser.

The file will be downloaded.

Here <dns-name> will be the DNS name of the machine. 

```console
https://<dns-name>/1kb
```

Open the URL in your browser and now the other file will be downloaded from the API gateway.


```console
https://<dns-name>/api_old/1kb
```

Make sure that port 443 or port 80 is open in the security group from the IP address of the browser.
