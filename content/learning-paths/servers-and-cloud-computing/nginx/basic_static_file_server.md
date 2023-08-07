---
title: "Setup a static file server"
weight: 4
layout: "learningpathall"
---

## Before you begin

This learning path leaves developing an understanding of how to use Nginx configurations files as an exercise for the reader. It's ok to go through this section even if you don't have an understanding of Nginx configuration files. However, once you are done here, you should read the [documentation on serving static content](https://docs.nginx.com/nginx/admin-guide/web-server/serving-static-content/) to better understand what is being shown below. This section walks through a bare minimum HTTPS file server setup. Tuning of a file server configuration will be explored in the advanced [Learn how to Tune Nginx](/learning-paths/servers-and-cloud-computing/nginx_tune) learning path.

## Setup a static file server

To setup a static file server you can configure Nginx, create a key and certificate, and start the server.

### Nginx configuration

SSH to the node you have selected to be the file server.

Using a text editor, add the following top level Nginx configuration to `/etc/nginx/nginx.conf` 

You will need to edit the file  with `sudo`.

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

  include /etc/nginx/conf.d/*.conf;
}
```

Here are the configuration file parameters:

* [`user`](https://nginx.org/en/docs/ngx_core_module.html#user): 
  * Sets the user that will own all worker processes. Worker processes should not be owned by root for security reasons. The main Nginx process will be owned by root.

* [`worker_processes`](https://nginx.org/en/docs/ngx_core_module.html#worker_processes):
  * Selects how many worker processes to launch. Auto will launch as many worker processes as there are logical CPUs on the system. Auto is the default and is recommended for the highest performance.

* [`pid`](https://nginx.org/en/docs/ngx_core_module.html#pid):
  * A file that stores the process ID of the main process.

* [`events`](https://nginx.org/en/docs/ngx_core_module.html#events):
  * A block used to manage how connections are handled.

* [`http`](https://nginx.org/en/docs/http/ngx_http_core_module.html#http):
  * A block that defines an HTTP(S) server.

* [`include`](https://nginx.org/en/docs/ngx_core_module.html#include):
  * Includes other files. You can also include other Nginx configuration files as shown above (`/etc/nginx/conf.d/*.conf`). This allows for organizing the Nginx configuration in a way that is clean and logical. The `mime.types` file is a default file that defines MIME types for various common file types. It's generally a good idea to include this default `mime.types` file.

* [`default_type`](https://nginx.org/en/docs/http/ngx_http_core_module.html#default_type):
  * A default mime type to use if a resource requested from the service doesn't match any type that is in the `mime.types` file. `application/octet-stream` defines a generic binary stream of data.

The above doesn't configure the file server. You can think of the above as a file that sets global configurations for Nginx. Additional blocks and directives are needed in order to create a file server. The additional configurations needed will be placed in `/etc/nginx/conf.d` since this location is included in the configuration above.

To complete the definition of the HTTPS file server use a text editor to add the following configuration information to `/etc/nginx/conf.d/fileserver.conf`

```console
# HTTPS server
server {
  listen 443 ssl;
  root /usr/share/nginx/html;
  index index.html index.htm;
  server_name $hostname;

  ssl_certificate /etc/nginx/ssl/ecdsa.crt;
  ssl_certificate_key /etc/nginx/ssl/ecdsa.key;
  ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384;
  location / {
    try_files $uri $uri/ =404;
  }
}
```

* [`server`](https://nginx.org/en/docs/http/ngx_http_core_module.html#server):
  * A block that defines a server.

* [`listen`](https://nginx.org/en/docs/http/ngx_http_core_module.html#listen):
  * Selects the port the server will listen on for HTTP requests. The additional parameter of `ssl` means that HTTP connections on this port will be encrypted. Note, you need to make sure that whatever port number is listed here is not blocked by any firewalls or security features of the network.

* [`root`](https://nginx.org/en/docs/http/ngx_http_core_module.html#root):
  * Selects the root directory from which files will be served.

* [`index`](https://nginx.org/en/docs/http/ngx_http_index_module.html#index):
  * Selects the file to be served relative to the root directory when the request ends in a `/` (the client isn't requesting a specific resource).

* [`server_name`](https://nginx.org/en/docs/http/ngx_http_core_module.html#server_name):
  * Name of the server. This is used for matching against the HTTP request's `Host` header. 

* [`ssl_certificate`](https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_certificate):
  * Location of the SSL/TLS certificate.

* [`ssl_certificate_key`](https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_certificate_key):
  * Location of the SSL/TLS private key.

* [`location`](https://nginx.org/en/docs/http/ngx_http_core_module.html#location):
  * Configurations can be placed here based on the request URI location. In this case, the location to serve from is the root directory (`/usr/share/nginx/html`).

* [`try_files`](https://nginx.org/en/docs/http/ngx_http_core_module.html#try_files):
  * Selects which files to check for based on the requested resource path in the URI. In this case, a 404 error is returned if the file is not found.

Since this is an HTTPS server, a public/private key pair and certificate is required. You can generate a self-signed certificate which contains the public key.

{{% notice Note %}}
For production use, you should generate certificates through a certificate authority. This example is for demonstration purposes. 
{{% /notice %}}

### Creating ECDSA key and certificate for the HTTPS file server

Install [OpenSSL](https://www.openssl.org/) using the Linux package manager to create the key and certificate.

Run the following commands to create the keys and certificate:

```console
mkdir /etc/nginx/ssl/
openssl ecparam -out ecdsa.key -name prime256v1 -genkey
openssl req -new -sha256 -key ecdsa.key -out server.csr
openssl x509 -req -sha256 -days 365 -in server.csr -signkey ecdsa.key -out ecdsa.crt
```

You will be prompted for several pieces of information including country, locality, organization name, and more.

Copy the key and certificate to the `ssl_certificate` and `ssl_certificate_key` locations specified in the Nginx configuration file `/etc/nginx/conf.d/fileserver.conf`:

```console
cp ecdsa.key /etc/nginx/ssl/ecdsa.key
cp ecdsa.crt /etc/nginx/ssl/ecdsa.crt
```

### Checking Nginx configuration and starting the server

Check the configuration for correct syntax and then start the Nginx server using the following command:

```console
nginx -t -v
```
The output will be similar to: 

```output
nginx version: nginx/1.23.4
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Start Nginx using the `service` command: 

```console
sudo service nginx start
```

### Create a sample file to serve

SSH to the file server and switch to the root user:

```console
sudo su -
```

Create a file to serve. The file should be placed in `/usr/share/nginx/html` (this is the `root` directive set in the configuration above).

For example:

```console
echo Hello, this is a text file to serve > /usr/share/nginx/html/file.txt
```

### Verify that files are being served

You can verify files are being served in two steps, a `localhost` test followed by an IP address or DNS name test.


1. SSH into the file server node and run the `wget` command to test `localhost`:

```console
wget --no-check-certificate https://localhost/file.txt
```

The `--no-check-certificate` tells `wget` not to check the certificate. A self-signed certificate check fails. In a production environment, this switch is not needed because the certificate will be signed by a 3rd party certificate authority.

2. SSH to a node that is not the file server node and run the command below.

Substitute your IP address or DNS name in the command.

```console
wget --no-check-certificate https://<ip_or_dns>/file.txt
```

You can also use `curl` to read the default index.html that Nginx creates when it is installed.

From the file server running Nginx run: 

```console
curl -k https://localhost/index.html
```

You can also omit the `index.html` part by running:

```console
curl -k https://localhost/
```

From a node that is not the file server node run:

```console
curl -k https://<ip_or_dns>/index.html
```

You can also omit the `index.html` part by running:

```console
curl -k https://<ip_or_dns>/
```

If the commands work, then the file server is setup properly.

Feel free to experiment with the file server configuration.

A good place to start reading more is the [documentation on serving static content](https://docs.nginx.com/nginx/admin-guide/web-server/serving-static-content/).