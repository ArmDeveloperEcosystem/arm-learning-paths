---
title: "Build Nginx from source"
weight: 3
layout: "learningpathall"
---

## Before you begin

To build Nginx from source, first update the Ubuntu repository information:

```bash
sudo apt-get update
```

Next, install the needed tools and libraries:

```bash
sudo apt-get install wget unzip mercurial gcc libssl-dev make -y

```

## Build Nginx from source

Refer to [the official documentation](http://nginx.org/en/docs/configure.html) for details on to build Nginx from the source or follow the quick start steps as shown below.

### Quick start for building Nginx from source

Follow these steps to build Nginx from source.

Download and extract the latest source code of [PCRE](http://www.pcre.org/), the example shows version 10.40. 

```bash { pre_cmd="sudo apt remove -y nginx" }
wget https://github.com/PCRE2Project/pcre2/releases/download/pcre2-10.40/pcre2-10.40.zip
unzip pcre2-10.40.zip
```

Download and extract the [zlib](https://zlib.net/fossils/) library distribution (version 1.1.3 - 1.2.11):

```bash
wget https://zlib.net/fossils/zlib-1.2.11.tar.gz
tar -xvf zlib-1.2.11.tar.gz
```

Clone the Nginx source code:

```bash
hg clone http://hg.nginx.org/nginx
cd nginx/
```

The build is configured using the `configure` command. It defines various aspects of the system, including the methods Nginx is allowed to use for connection processing. At the end, it creates a Makefile.

```bash { cwd="./nginx" }
./auto/configure --prefix=/usr/share/nginx --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --with-http_ssl_module --modules-path=/etc/nginx/modules --with-stream=dynamic --with-pcre=../pcre2-10.40 --with-zlib=../zlib-1.2.11
```

There are many configuration options available in Nginx. To find all the configuration options available in Nginx check the [documentation](http://nginx.org/en/docs/configure.html).

After configuration, compile and install Nginx using make:

```bash { cwd="./nginx" }
make
sudo make install
```

Check the version to verify installation by using the command:

```bash
nginx -v
```

The output will look like

```output
nginx version: nginx/1.23.4
```

To enable the systemd service, use a file editor of your choice and create a file named `/lib/systemd/system/nginx.service` with the contents below:

```console
[Unit]
Description=The Nginx HTTP and reverse proxy server
After=syslog.target network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
PIDFile=/run/nginx.pid
ExecStartPre=/usr/sbin/nginx -t
ExecStart=/usr/sbin/nginx
ExecReload=/usr/sbin/nginx -s reload
ExecStop=/bin/kill -s QUIT $MAINPID
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

Start Nginx using systemd:

```console
sudo systemctl start nginx
```

To confirm Nginx is running, check the status:

```console
sudo systemctl status nginx
```

The output from this command will look like:

```output
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2023-04-11 14:36:35 UTC; 14min ago
```
Nginx is successfully running as shown.
