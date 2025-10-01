---
title: Install PHP
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install PHP 
In this section, you will learn how to install PHP along with the Apache web server and common PHP extensions on a SUSE Arm-based virtual machine.

### Update the system
Before installing any software, make sure your system is up-to-date with the latest packages and security patches.

```console
sudo zypper refresh
sudo zypper update -y
```

### Install PHP, Apache, and common extensions
Now install PHP, PHP-FPM, Apache web server, and some commonly used PHP extensions.

```console
sudo zypper install -y php php-cli php-fpm php-mysql php-xml php-mbstring php-opcache apache2
```
- **php** → Core PHP package.  
- **php-cli** → Allows running PHP scripts from the command line.  
- **php-fpm** → FastCGI Process Manager for PHP.  
- **php-mysql** → Enables PHP to connect with MySQL databases.  
- **php-xml** → Allows working with XML files in PHP.  
- **php-mbstring** → Helps PHP handle multi-byte strings.  
- **php-opcache** → Improves PHP performance by caching compiled code.  
- **apache2** → Installs the Apache web server.  

### Enable and start Apache:
Once Apache is installed, you need to start it and make sure it runs automatically on boot.

```console
sudo systemctl enable apache2
sudo systemctl start apache2
sudo systemctl status apache2
```

### Verify PHP installation
Check if PHP is installed correctly and see the version installed.

```console
php -v
```
You should see output similar to:
```output
PHP 8.0.30 (cli) (built: Nov 25 2024 12:00:00) ( NTS )
Copyright (c) The PHP Group
Zend Engine v4.0.30, Copyright (c) Zend Technologies
with Zend OPcache v8.0.30, Copyright (c), by Zend Technologies
```
PHP installation is complete. You can now proceed with the baseline testing.
