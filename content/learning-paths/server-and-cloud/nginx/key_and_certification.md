---
title: "Create ECDSA key and certificate"
weight: 7
layout: "learningpathall"
---


## Create ECDSA key and certificate

This section shows how to generate an ECDSA key and certificate for Nginx. It is a sub-step of other other sections of the learning paths.

### Quick start 

Install OpenSSL.

```console
apt-get install openssl -y
```

Run the following commands to create the keys and certificate and then copy them to the location specified in the Nginx configuration files.

```console
mkdir /etc/nginx/ssl/
openssl ecparam -out ecdsa.key -name prime256v1 -genkey
openssl req -new -sha256 -key ecdsa.key -out server.csr
openssl x509 -req -sha256 -days 365 -in server.csr -signkey ecdsa.key -out ecdsa.crt
cp ecdsa.key /etc/nginx/ssl/ecdsa.key
cp ecdsa.crt /etc/nginx/ssl/ecdsa.crt
```

When promoted for the COMMON_NAME, enter the IP address or DNS name.

When done, use the browser back button to return to the Nginx step you were working on.
