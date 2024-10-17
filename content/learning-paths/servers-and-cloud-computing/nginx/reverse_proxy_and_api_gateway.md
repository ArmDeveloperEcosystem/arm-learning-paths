---
title: "Setup a reverse proxy and API gateway"
weight: 5
layout: "learningpathall"
---

## Before you begin

You will need to setup two [file servers](/learning-paths/servers-and-cloud-computing/nginx/basic_static_file_server/) using the instructions in the previous section before moving forward.

In this section, a third node is setup that will run a Reverse Proxy & API Gateway (this will also be referred to a RP/APIGW). This RP/APIGW will use the two file servers as the upstream servers it will load balance across. The configuration shown here is a bare minimum. Tuning will be explored in the advanced [Learn how to Tune Nginx](/learning-paths/servers-and-cloud-computing/nginx_tune) learning path. Once you complete this section, you should review the [Nginx documentation](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) on Reverse Proxies. There are also some [Nginx blogs](https://www.nginx.com/blog/deploying-nginx-plus-as-an-api-gateway-part-1/) that discuss the deployment of API Gateways.

## Setup a reverse proxy and API gateway

### Nginx configuration

SSH to the node that will run the RP/APIGW.

Use a text editor to add the text below to  the file `/etc/nginx/nginx.conf`

You will need to open the editor with `sudo`.

If the file already contains configuration data, replace it with the content below.

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

The above information does not configure the RP/APIGW. The file above sets the global configurations for Nginx. Additional blocks and directives are needed in order to create the RP/APIGW. The additional configurations needed are placed in `/etc/nginx/conf.d` because this location is included in the configuration file above.

Use a text editor to define the RP/APIGW by adding the following configuration information to the file `/etc/nginx/conf.d/loadbalance.conf`:

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

The block called `upstream` lists the upstream file servers the RP/APIGW will load balance across. Substitute your IP addresses or DNS names.

There are three `location` blocks. The first two configure the API gateway functionality and the third one configures a reverse proxy. The difference between a reverse proxy and an API gateway is that an API gateway rewrites a client's requested URI, and then routes that rewritten request to the upstream servers. The rewriting of the URI allows for separating a public API from a private API. The API gateway in this configuration looks for `/api_old/` at the beginning of the URI, and replaces it with `/api_new/`. 

Once the rewrite happens, the second location block handles forwarding the rewritten URI to the upstream server (note the reference to `ssl_file_server_com`). 

The third location block simply forwards all other requests that don't start with `/api_new/` to the upstream server without a URI rewrite.

### Creating ECDSA key and certificate for the RP/APIGW file server

Refer to the section [Setup a static file server](/learning-paths/servers-and-cloud-computing/nginx/basic_static_file_server) to generate the keys and certificate that will be used by the RP/APIGW.

### Checking Nginx configuration and starting the server

Check the configuration for correct syntax and then start the Nginx RP/APIGW using the following command:

```console
nginx -t -v
```

The output from this command will be similar to: 

```output
nginx version: nginx/1.23.4
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Start Nginx, refer to [Install Nginx via a package manager and check the build configuration](/learning-paths/servers-and-cloud-computing/nginx/install_from_package/) for a sample service file:

```console
sudo service nginx start
```

### Create sample file for APIGW path

SSH to each of the upstream file servers and switch to root.

```console
sudo su -
```

Create files to serve for the RP and APIGW paths. The files should be placed in `/usr/share/nginx/html` (this is what the `root` directive was set to in file server configuration in the previous section.

```console
echo Hello, this is a text file to serve > /usr/share/nginx/html/file.txt
mkdir -p /usr/share/nginx/html/api_new
cp /usr/share/nginx/html/file.txt /usr/share/nginx/html/api_new/apigw_file.txt
```

### Verify the RP/APIGW

This can be done in two steps. 

You can verify files are being served in two steps, a `localhost` test followed by an IP address or DNS name test.

1. SSH to the RP/APIGW node. Then run the `wget` commands shown below.

Check the reverse proxy path:
```console
wget --no-check-certificate https://localhost/file.txt
```

Check the API gateway:

```console
wget --no-check-certificate https://localhost/api_old/apigw_file.txt
```

2. SSH to a node that is not the RP/APIGW node and run the commands below.

Check the reverse proxy path:

```console
wget --no-check-certificate https://<rpapigw_ip_or_dns>/file.txt
```

Check the API gateway:
```console
wget --no-check-certificate https://<rpapigw_ip_or_dns>/api_old/apigw_file.txt
```

If the above commands work, then the RP/APIGW is setup properly.

Feel free to experiment with the file server configuration. 

You can review the [Nginx documentation](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) on reverse proxies. 
