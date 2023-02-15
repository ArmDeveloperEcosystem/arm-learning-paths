---
title: "Verifying Nginx setup with wget and curl"
weight: 6
layout: "learningpathall"
---


## Prerequisites

Two [web servers](../basic_static_file_server)
A [Reverse Proxy and API gateway](../reverse_proxy_and_api_gateway)

## To wget a file from the server

This section continues with the 3 machine setup from the previous step.

### Quick start 

Switch to root.

```console
sudo su -
```

Create a file in each of the two web servers.

The file should be placed in /usr/share/nginx/html

```console
cat > /usr/share/nginx/html/file.txt
Hello, this a text file to serve
```

Use Ctrl-D to end the cat command after one line of text has been entered. 

Do the same thing on the second web server.

If Nginx was running before file creation restart it on each web server and on the API gateway using the command:

```console
systemctl restart nginx
```

Run the following wget command in the client instance, the <dns-name> is the DNS name of the reverse proxy machine. 

```console
wget https://<dns-name>/file.txt --no-check-certificate
```

## To curl to retrieve a webpage

The default index.html is already on each web server. Use curl to retrieve it.

### Quick start

Run the following curl from another machine to retrieve the index.html

Again, <dns-name> will be the DNS name of the reverse proxy machine.

```console
curl -k https://<dns-name>/index.html
```

Try to create a new html file in /usr/share/nginx/html folder in each web server.

Then restart the Nginx on each web server and the reverse proxy.
