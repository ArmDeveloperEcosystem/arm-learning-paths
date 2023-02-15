---
title: "Build Nginx from source"
weight: 3
layout: "learningpathall"
---

## Prerequisites

A physical machine or cloud instance with Ubuntu installed.

Update the Ubuntu repository information.

```bash
sudo apt-get update
```

Install the needed tools and libraries to build from source.

```bash
sudo apt-get install wget unzip mercurial gcc libssl-dev make -y

```

## Build Nginx from source

Refer to [the documentation](http://nginx.org/en/docs/configure.html) for more details on to build Nginx from the source.

### Quick start 

Follow these steps to build Nginx from source.

Download and extract the latest source code of PCRE from [here](http://www.pcre.org/), the example shows version 10.40. 

```bash { pre_cmd="sudo apt remove -y nginx" }
wget https://github.com/PCRE2Project/pcre2/releases/download/pcre2-10.40/pcre2-10.40.zip
unzip pcre2-10.40.zip
```

The zlib library distribution (version 1.1.3 - 1.2.11) needs to be downloaded from the [zlib](https://zlib.net/fossils/) site and extracted. 

```bash
wget https://zlib.net/fossils/zlib-1.2.11.tar.gz
tar -xvf zlib-1.2.11.tar.gz
```

Clone the Nginx source code:

```bash
hg clone http://hg.nginx.org/nginx
cd nginx/
```

The build is configured using the **configure** command. It defines various aspects of the system, including the methods Nginx is allowed to use for connection processing. In the end, it creates a Makefile.

```bash { cwd="./nginx" }
./auto/configure --prefix=/usr/share/nginx --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --with-http_ssl_module --modules-path=/etc/nginx/modules --with-stream=dynamic --with-pcre=../pcre2-10.40 --with-zlib=../zlib-1.2.11
```

There are many configuration options available in Nginx. To find all the configuration options available in Nginx check the [documentation](http://nginx.org/en/docs/configure.html).

After configuration, Nginx is compiled and installed using make:

```bash { cwd="./nginx" }
make
sudo make install
```

To verify if Nginx is installed or not check its version by using the command:

```bash
nginx -v
```

To enable the systemd service, create a file named **/lib/systemd/system/nginx.service** and add the below script in the file.

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

Now Nginx can be managed using systemd.

```console
sudo systemctl start nginx
```

To confirm Nginx is running use the status command.

```console
sudo systemctl status nginx
```
