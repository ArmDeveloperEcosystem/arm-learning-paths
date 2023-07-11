---
title: "Setup a web server"
weight: 4
layout: "learningpathall"
---

## Setup a basic web server

Follow the steps below to start a basic web server.

Switch to root:

```console
sudo su -
```

Using a file editor of your choice, add the following code in `/etc/nginx/nginx.conf`.

If the file already has information in it, remove and add the code below:

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

Add the following code in `/etc/nginx/conf.d/default.conf`:

Replace `$hostname` with the DNS name of the machine. For AWS this would take the form of, `ec2-23-20-129-140.compute-1.amazonaws.com`

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

Create ECDSA key and certificate:

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
Now, check the configuration for correct syntax and then start the Nginx server using the commands below:

```console
nginx -t -v
```
The output from this command will look like:

```output
nginx version: nginx/1.23.4
nginx: [warn] the "ssl" directive is deprecated, use the "listen ... ssl" directive instead in /etc/nginx/conf.d/default.conf:7
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Start Nginx using systemd:

```console
systemctl start nginx
```

To verify the web server is running, open the URL for the web server in a browser. 

You should see the content of your index.html file displayed.

The <dns-name> is the DNS name of your machine. 

```console
https://<dns-name>/
```

The browser will show the Nginx welcome message: 

![nginx #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/81ceb173-a9f3-40ec-b661-e39493aa1fa6)

{{% notice Note %}}
Make sure that port 443 or port 80 are open in the security group for the IP address of your machine.
{{% /notice %}}

Refer to the [official documentation](https://docs.nginx.com/nginx/admin-guide/web-server/serving-static-content/) for additional details regarding setting up a web server.
