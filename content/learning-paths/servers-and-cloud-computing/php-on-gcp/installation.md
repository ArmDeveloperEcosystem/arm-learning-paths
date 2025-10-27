---
title: Install PHP
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
In this section, you’ll install PHP, the Apache web server, and several commonly used PHP extensions on a SUSE Arm-based virtual machine. This setup forms the foundation for running and serving dynamic PHP applications on Arm-based machines.

## Update the system
Before installing any software, make sure your system has the latest packages and security patches:

```console
sudo zypper refresh
sudo zypper update -y
```

## Install PHP, Apache, and common extensions
Install PHP, PHP-FPM, Apache web server, and some commonly used PHP extensions by running:

```console
sudo zypper install -y php php-cli php-fpm php-mysql php-xml php-mbstring php-opcache apache2
```

Here’s what each package in the installation command does:

- `php`: provides the core PHP interpreter for running web applications
- `php-cli`: allows you to run PHP scripts from the command line, which is useful for testing and automation tasks
- `php-fpm`: installs the FastCGI Process Manager, which manages PHP worker processes and helps improve concurrency and performance
- `php-mysql`: enables PHP to connect to MySQL or MariaDB databases
- `php-xml`: adds support for parsing and manipulating XML data
- `php-mbstring`: enables multi-byte string handling, which is required by many web frameworks
- `php-opcache`: improves performance by caching precompiled PHP bytecode in memory, reducing runtime overhead
- `apache2`: installs the Apache HTTP web server, which serves PHP files using either mod_php or FastCGI


## Enable and start Apache
After installing Apache, enable and start the service so it runs automatically on boot and begins serving HTTP requests:
```console
sudo systemctl enable apache2
sudo systemctl start apache2
sudo systemctl status apache2
```
If everything starts correctly, the output is similar to:

```output
● apache2.service - The Apache Webserver
     Loaded: loaded (/usr/lib/systemd/system/apache2.service; enabled; vendor preset: disabled)
     Active: active (running) since Wed 2025-10-15 18:55:30 UTC; 3s ago
   Main PID: 4184 (httpd-prefork)
     Status: "Processing requests..."
      Tasks: 6
        CPU: 18ms
     CGroup: /system.slice/apache2.service
             ├─ 4184 /usr/sbin/httpd-prefork -DSYSCONFIG -C "PidFile /run/httpd.pid" -C "Include /etc/apache2/>
             ├─ 4225 /usr/sbin/httpd-prefork -DSYSCONFIG -C "PidFile /run/httpd.pid" -C "Include /etc/apache2/>
             ├─ 4226 /usr/sbin/httpd-prefork -DSYSCONFIG -C "PidFile /run/httpd.pid" -C "Include /etc/apache2/>
             ├─ 4227 /usr/sbin/httpd-prefork -DSYSCONFIG -C "PidFile /run/httpd.pid" -C "Include /etc/apache2/>
             ├─ 4228 /usr/sbin/httpd-prefork -DSYSCONFIG -C "PidFile /run/httpd.pid" -C "Include /etc/apache2/>
             └─ 4229 /usr/sbin/httpd-prefork -DSYSCONFIG -C "PidFile /run/httpd.pid" -C "Include /etc/apache2/>

Oct 15 18:55:30 pareena-php-test systemd[1]: Starting The Apache Webserver...
Oct 15 18:55:30 pareena-php-test systemd[1]: Started The Apache Webserver.
```

## Verify PHP installation
After installation, verify that PHP is installed correctly and view the installed version:

```console
php -v
```
The output is similar to:
```output
PHP 8.0.30 (cli) (built: Nov 25 2024 12:00:00) ( NTS )
Copyright (c) The PHP Group
Zend Engine v4.0.30, Copyright (c) Zend Technologies
with Zend OPcache v8.0.30, Copyright (c), by Zend Technologies

{{% notice success %}}
PHP is installed and ready for use on your Arm-based SUSE VM.
{{% /notice %}}
```
## What's next?

You've installed PHP, Apache, and essential PHP extensions on your SUSE Arm-based virtual machine. Apache is running and ready to serve dynamic PHP applications. You verified your PHP installation and confirmed that your environment is set up for web development on Arm.

You can move on to the baseline testing section, where you'll create and load a simple PHP web page to confirm that Apache and PHP are working together on your SUSE Arm-based virtual machine.
