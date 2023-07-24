---
title: "Install Nginx via a package manager & check build config"
weight: 2
layout: "learningpathall"
---

## Before you begin

There are two versions of Nginx. An open source version, and a licensed version called Nginx Plus. This learning path will use the open source version of Nginx. The open source version of Nginx will be referred to as simply Nginx.
 
If you plan to build Nginx from source, you can skip to the next section. However, it might be helpful to first take a look at a prebuilt install of Nginx first. This can help you understand how to configure a source build of Nginx.

## About Nginx documentation

There are two sets of documentation on Nginx. [Documentation](https://nginx.org/en/docs/) on [nginx.org](https://nginx.org) and [documentation](https://docs.nginx.com/nginx/) on [nginx.com](https://www.nginx.com/). The nginx.org documentation mostly covers the open source version of Nginx, while the nginx.com documentation mostly covers Nginx plus. Even if working with the open source version (like in this learning path), you should explore the documentation on nginx.com. It includes an [Admin Guide](https://docs.nginx.com/nginx/admin-guide/) that can be helpful regardless of which version you are working with. In fact, in this learning path, links to both sets of documentation will be made.

Exploring the documentation is very helpful. Key insights can be gained that will help with deployment, configuration, and performance.

## Install Nginx prebuilt using a package manager

To install via a package manager, you can follow either the [nginx.org install instructions](http://nginx.org/en/linux_packages.html) or the [nginx.com install instructions](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/). Both yield the same result.

### Getting the Nginx Build Config

It can be useful to know the build configuration of the installed version of Nginx. Especially if you plan to build Nginx from source and are unsure of how to configure the build.

Run the following command to get the complete build options for the prebuilt install:

```bash
nginx -V
```
The output from this command will look like the below:

```output
nginx version: nginx/1.18.0
built with OpenSSL 3.0.2 15 Mar 2022
TLS SNI support enabled
configure arguments: --with-cc-opt='-g -O2 -ffile-prefix-map=/build/nginx-glNPkO/nginx-1.18.0=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -fPIC -Wdate-time -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now -fPIC' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --modules-path=/usr/lib/nginx/modules --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-compat --with-debug --with-pcre-jit --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_v2_module --with-http_dav_module --with-http_slice_module --with-threads --add-dynamic-module=/build/nginx-glNPkO/nginx-1.18.0/debian/modules/http-geoip2 --with-http_addition_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_sub_module
```

This shows key pieces of information that can help you understand the features and expected performance of Nginx. For example, the output above lists the version of Nginx, the version of OpenSSL, and GCC compile flags like `-O2` (listed in the `--with-cc-opt` switch). The version information is important because making sure you are running the latest version of Nginx and OpenSSL typically results in the highest performance on Arm. Last, this information can be used as a starting point for configuring a build from source. This is discussed in the next section.

### Getting the Nginx Service file

If you plan to build Nginx, it might be helpful to get a copy of the Nginx service file that is installed with the prebuilt. It is typically located at `/lib/systemd/system/nginx.service`. Changes to the file can be made as needed. Below is a sample service file that could be used.

```
[Unit]
Description=The NGINX HTTP and reverse proxy server
After=syslog.target network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
PIDFile=/run/nginx.pid
ExecStartPre=/usr/share/nginx/sbin/nginx -t
ExecStart=/usr/share/nginx/sbin/nginx
ExecReload=/usr/share/nginx/sbin/nginx -s reload
ExecStop=/bin/kill -s QUIT $MAINPID
ExecStopPost=/bin/rm -f /run/nginx.pid
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```