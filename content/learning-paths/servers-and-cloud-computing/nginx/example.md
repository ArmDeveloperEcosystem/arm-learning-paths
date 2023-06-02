---
title: "Verifying Nginx setup with wget and curl"
weight: 6
layout: "learningpathall"
---


## Before you begin

Setup [two web servers](../basic_static_file_server) and setup a [Reverse Proxy and API gateway](../reverse_proxy_and_api_gateway)


## Use wget to get a a file from the server 

You will use the 3 machine setup from the previous section to `wget` a file from a server.

Switch to root:

```console
sudo su -
```
Create a file in each of the two web servers. The file should be placed in /usr/share/nginx/html

For example:

```console
cat > /usr/share/nginx/html/file.txt
Hello, this a text file to serve
```

Use Ctrl-D to end the cat command after one line of text has been entered. 

Do the same thing on the second web server.

If Nginx was running before you created the file on the two web servers, restart it on each web server and on the API gateway using the command:

```console
systemctl restart nginx
```

Run the `wget` command in the client instance, the <dns-name> is the DNS name of the reverse proxy machine. 

```console
wget https://<dns-name>/file.txt --no-check-certificate
```

## Use curl to retrieve a webpage

The default `index.html` is already on each web server. 

Run the `curl` command from another machine to retrieve the index.html.

Again, <dns-name> will be the DNS name of the reverse proxy machine.

```console
curl -k https://<dns-name>/index.html
```

Try to create a new html file in /usr/share/nginx/html folder in each web server.

Then restart the Nginx on each web server and the reverse proxy.
