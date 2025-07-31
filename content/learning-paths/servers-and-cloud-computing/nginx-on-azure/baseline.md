---
title: Nginx Baseline Testing 
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


### Baseline testing with a static website on Nginx
Perform baseline testing of Nginx on Azure Linux 3.0 by deploying a custom static HTML page. This verifies that Nginx is correctly serving content on the Arm64 platform.

1. Create a Static Website Directory:

Prepare a folder to host your HTML content.
```console
mkdir -p ~/my-static-site
```
2. Create an HTML file and Web page:

Create a HTML file `nano my-static-site/index.html` with the content below to design a visually appealing static landing page.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Welcome to NGINX on Azure Linux</title>
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
    <h1> Welcome to NGINX on Azure Linux 3.0!</h1>
    <p>Your static site is running beautifully on ARM64 </p>
  </div>
</body>
</html>
```
3. Create NGINX Config File to Serve Static Website:

Point Nginx to serve your static HTML content.
```console
sudo nano /etc/nginx/conf.d/static-site.conf
```
Now, add the following configuration:

```nginx
server {
    listen 80;
    server_name localhost;

    location / {
        root /home/azureuser/my-static-site;
        index index.html;
    }

    access_log /var/log/nginx/static-access.log;
    error_log /var/log/nginx/static-error.log;
}
```
Make sure `/home/azureuser/my-static-site` is the correct path to your **index.html**.

4. Test the Nginx Configuration:

```console
sudo nginx -t
```
You should see an output similar to:
```output
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

5. Reload or Restart Nginx:

Apply configuration changes and restart the web server.
```console
sudo nginx -s reload
sudo systemctl restart nginx
```

6. Test the Static Website on browser:

Access your website at your public IP on port 80.
```console
http://<your-vm-public-ip>/
```
Make sure port 80 is open in your Azure Network Security Group (NSG).

7. You should see the Nginx welcome page confirming a successful deployment:

![Static Website Screenshot](images/web-page.png)

This verifies the basic functionality of Nginx installation before proceeding to the benchmarking.
