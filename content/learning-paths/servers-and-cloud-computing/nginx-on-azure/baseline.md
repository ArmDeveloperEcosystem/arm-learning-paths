---
title: NGINX Baseline Testing 
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


### Baseline testing with a static website on NGINX
Once NGINX is installed and serving the default welcome page, the next step is to verify that it can serve your own content. A baseline test using a simple static HTML site ensures that NGINX is correctly configured and working as expected on your Ubuntu Pro 24.04 LTS virtual machine.

1. Create a Static Website Directory:

Prepare a folder to host your HTML content.
```console
mkdir -p /var/www/my-static-site
cd /var/www/my-static-site
```
2. Create an HTML file and Web page:

Create a simple HTML file to replace the default NGINX welcome page. Using a file editor of your choice create the file `index.html` with the content below:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Welcome to NGINX on Azure Ubuntu Pro</title>
  <style>
    body {
      background: linear-gradient(to right, #4facfe, #00f2fe);
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      color: white;
      text-align: center;
    }
    .box {
      background: rgba(0, 0, 0, 0.3);
      padding: 40px;
      border-radius: 12px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.4);
    }
    h1 {
      margin-bottom: 10px;
      font-size: 2.5rem;
    }
    p {
      font-size: 1.2rem;
    }
  </style>
</head>
<body>
  <div class="box">
    <h1> Welcome to NGINX on Azure Ubuntu Pro 24.04 LTS!</h1>
    <p>Your static site is running beautifully on ARM64 </p>
  </div>
</body>
</html>
```
3. Adjust Permissions:

Ensure that NGINX (running as the www-data user) can read the files in your custom site directory:

```console
sudo chown -R www-data:www-data /var/www/my-static-site
```
This sets the ownership of the directory and files so that the NGINX process can serve them without permission issues.

4. Update NGINX Configuration:

Point NGINX to serve files from your new directory by creating a dedicated configuration file under /etc/nginx/conf.d/.

```console
sudo nano /etc/nginx/conf.d/static-site.conf
```
Add the following configuration to it:

```console
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;

    root /var/www/my-static-site;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    access_log /var/log/nginx/static-access.log;
    error_log  /var/log/nginx/static-error.log;
}
```
This configuration block tells NGINX to:
  - Listen on port 80 (both IPv4 and IPv6).
  - Serve files from /var/www/my-static-site.
  - Use index.html as the default page.
  - Log access and errors to dedicated log files for easier troubleshooting.

Make sure the path to your `index.html` file is correct before saving.

5. Disable the default site:

By default, NGINX comes with a packaged default site configuration. Since you have created a custom config, it is good practice to disable the default to avoid conflicts:

```console
sudo unlink /etc/nginx/sites-enabled/default
```

6. Test the NGINX Configuration:

Before applying your changes, always test the configuration to make sure there are no syntax errors:

```console
sudo nginx -t
```
You should see output similar to:
```output
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```
If you see both lines, your configuration is valid.

7. Reload or Restart NGINX:

After testing the configuration, apply your changes by reloading or restarting the NGINX service:
```console
sudo nginx -s reload
sudo systemctl restart nginx
```

8. Test the Static Website in a browser:

Access your website at your public IP on port 80.

```console
http://<your-vm-public-ip>/
```

9. You should see the NGINX welcome page confirming a successful deployment:

![Static Website Screenshot](images/nginx-web.png)

This verifies the basic functionality of NGINX installation and you can now proceed to benchmarking the performance of NGINX on your Arm-based Azure VM.
