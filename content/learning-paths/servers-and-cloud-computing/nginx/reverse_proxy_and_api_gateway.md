---
title: "Setup Reverse Proxy and API Gateway"
weight: 5
layout: "learningpathall"
---

## Before you begin

Setup two [basic web servers](../basic_static_file_server) using the instructions in the previous section.
You will setup the third machine that will serve as a reverse proxy.

This section creates 2 upstream web servers behind the reverse proxy or API Gateway. You can create as many upstream web servers as you wish, but the example here assumes two are already created.

## Setup a Reverse Proxy and API Gateway

The steps below are used to setup Reverse Proxy and API Gateway.

Switch to root:

```console
sudo su -
```

Use a file editor of you choice and add the following code in `/etc/nginx/nginx.conf`:

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

Add the code shown below in `/etc/nginx/conf.d/default.conf`.

If the file already has information in it, remove and add the code shown.

Replace `$hostname` with the DNS name of the machine. For AWS this would take the form of, ec2-23-20-129-140.compute-1.amazonaws.com

Replace <private_ip_1> and <private_ip_2> with the private IP of the upstream web servers that you created in the previous step.

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


Create ECDSA key and certificate for the files `ecdsa.rt` and `ecdsa.key`.

Install OpenSSL, which is required to create the key and certificate:

```console
apt-get install openssl -y
```

Run the following commands to create the keys and certificate:

```console
mkdir /etc/nginx/ssl/
openssl ecparam -out ecdsa.key -name prime256v1 -genkey
openssl req -new -sha256 -key ecdsa.key -out server.csr
openssl x509 -req -sha256 -days 365 -in server.csr -signkey ecdsa.key -out ecdsa.crt
```

You will be prompted for several things including Country Name, Locality Name, Organization Name. Hit enter to use the default for all except **Common Name**. For **Common Name** enter the the IP address or DNS name of your machine.

Copy the key and certificate to the location specified in the Nginx configuration files:

```console
cp ecdsa.key /etc/nginx/ssl/ecdsa.key
cp ecdsa.crt /etc/nginx/ssl/ecdsa.crt
```
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
dd if=/dev/urandom of=/usr/share/nginx/html/1kb bs=1024 count=1
mkdir -p /usr/share/nginx/html/api_new
cp /usr/share/nginx/html/1kb /usr/share/nginx/html/api_new
```

Verify the reverse proxy server is running by opening the URL in your browser:

The file will be downloaded.

Here <dns-name> will be the DNS name of the machine:

```console
https://<dns-name>/1kb
```
Open the URL in your browser and now the other file will be downloaded from the API gateway:

```console
https://<dns-name>/api_old/1kb
```

{{% notice Note %}}
Make sure that port 443 or port 80 are open in the security group for the IP address of your machine.
{{% /notice %}}
