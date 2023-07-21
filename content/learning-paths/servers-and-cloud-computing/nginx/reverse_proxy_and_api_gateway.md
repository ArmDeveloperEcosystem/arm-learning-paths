---
title: "Setup Reverse Proxy and API Gateway"
weight: 5
layout: "learningpathall"
---

## Before you begin

Setup at least two [file servers](../basic_static_file_server) using the instructions in the previous section. If you wish, you can use your own custom configured file servers instead.

In this section, a third node is setup that will run a Reverse Proxy & API Gateway (this will also be referred to a RP/APIGW). This RP/APIGW will use the two file servers as the upstream servers it will load balance across. The configuration shown here is a bare minimum. Tuning will be explored in an advanced learning path. Once you are done here, you should review the [Nginx documentation](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) on Reverse Proxies. There are also some [Nginx blogs](https://www.nginx.com/blog/deploying-nginx-plus-as-an-api-gateway-part-1/) that discuss the deployment of API Gateways.

## Setup a Reverse Proxy and API Gateway

### Nginx configuration

SSH into the node that will run the RP/APIGW.

Using a file editor of your choice, add the following top level Nginx configuration to `/etc/nginx/nginx.conf`. You will need to open the file editor with `sudo`.

If the file already has a configuration in it, remove it and add the below.

```console
user www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
}
http {
  include /etc/nginx/mime.types;
  default_type application/octet-stream;

  ##
  # Virtual Host Configs
  ##
  include /etc/nginx/conf.d/*.conf;
}
```

These directives have already been discussed in the [Setup a static file server](../basic_static_file_server) section.

The above doesn't configure the RP/APIGW. You can think of the above as a file that sets global configurations for Nginx. Additional blocks and directives are needed in order to create the RP/APIGW. The additional configurations needed will be placed in `/etc/nginx/conf.d` since this location is included in the configuration above.

Next, to complete the definition of the RP/APIGW; add the following configuration to `/etc/nginx/conf.d/loadbalance.conf`:

```console
# Upstreams for https
upstream ssl_file_server_com {
  server <fileserver_1_ip_or_dns>:443;
  server <fileserver_2_ip_or_dns>:443;
}

# HTTPS reverse proxy and API Gateway
server {
  listen 443 ssl;
  root /usr/share/nginx/html;
  index index.html index.htm;
  server_name $hostname;

  ssl_certificate /etc/nginx/ssl/ecdsa.crt;
  ssl_certificate_key /etc/nginx/ssl/ecdsa.key;
  ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384;

  # API Gateway Path
  location ~ ^/api_old/.*$ {
    rewrite ^/api_old/(.*)$ /api_new/$1 last;
  }
  location /api_new {
    internal;
    proxy_pass https://ssl_file_server_com;
  }

  # Reverse Proxy Path
   location / {
   proxy_pass https://ssl_file_server_com;
  }
}
```

Much of what is in this file should look familiar if you followed the instructions in the [Setup a static file server](../basic_static_file_server) section. Only what is new will be discussed here. 

First, there is the block called `upstream`. This lists all of the upstream file servers the RP/APIGW will load balance across. This block of servers is given the name `ssl_file_server_com`. Next, there are three `location` blocks. The first two configure the API Gateway functionality and the third one configures a Reverse Proxy. The difference between a Reverse Proxy and an API Gateway is that an API Gateway rewrites a client's requested URI, and then routes that rewritten request to the upstreams. This rewriting of the URI allows for separating a public API from a private API. The API Gateway in this configuration will look for `/api_old/` at the beginning of the URI, and replace it with `/api_new/`. Once the rewrite happens, the second location block will handle forwarding the rewritten URI to the upstream server (notice the reference to `ssl_file_server_com` here). The third location block simply forwards all other requests that don't start with `/api_new/` to the upstream server without a URI rewrite.

### Creating ECDSA key and certificate for the RP/APIGW file server

Please refer to the section [Setup a static file server](../basic_static_file_server) for instruction on how to generate the keys and certificate that will be used by the RP/APIGW.

### Checking Nginx configuration and starting the server

Check the configuration for correct syntax and then start the Nginx RP/APIGW using the following command:

```console
nginx -t -v
```
The output from this command will look like:

```output
nginx version: nginx/1.23.4
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Start Nginx (see [Install Nginx via a package manager & check configuration](../install_from_package) for a sample service file):

```console
sudo service nginx start
```

### Create sample file for APIGW path

SSH into each of the upstream file servers and switch to root.

```console
sudo su -
```
Create files to serve for the RP and APIGW paths. The files should be placed in `/usr/share/nginx/html` (this is what the `root` directive was set to in file server configuration in the [previous section](../basic_static_file_server)).

```console
echo Hello, this is a text file to serve > /usr/share/nginx/html/file.txt
mkdir -p /usr/share/nginx/html/api_new
cp /usr/share/nginx/html/file.txt /usr/share/nginx/html/api_new/apigw_file.txt
```

### Verify the RP/APIGW


This can be done in two steps. First SSH into the RP/APIGW node and try to download a file using `localhost`, then SSH into a different node and try to download the file using the IP address or DNS name of the RP/APIGW. Doing it this way allows for figuring out if adjustments to the network configuration are needed.

SSH into the RP/APIGW node. Then run the `wget` command shown below. 

```console
# Reverse Proxy Path
wget --no-check-certificate https://localhost/file.txt

# API Gateway Path
wget --no-check-certificate https://localhost/api_old/apigw_file.txt
```

The switch `--no-check-certificate` tells `wget` to not bother with checking the certificate. This is because it's a self-signed certificate, so the check will fail. In a production environment, this switch is not needed (and not recommended) because the certificate will be signed by a 3rd party certificate authority. In that case, the certificate will be verified by `wget`.

Next, SSH into a node that is not the RP/APIGW node and run the below.

```console
# Reverse Proxy Path
wget --no-check-certificate https://<rpapigw_ip_or_dns>/file.txt

# API Gateway Path
wget --no-check-certificate https://<rpapigw_ip_or_dns>/api_old/apigw_file.txt
```
If the above works, then the RP/APIGW is setup properly.

Feel free to experiment with the file server configuration. The Nginx documentation, guides, and blogs can be used as a reference. 