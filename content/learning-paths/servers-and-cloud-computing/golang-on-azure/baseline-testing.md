---
title: Golang Baseline Testing 
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Baseline testing: run a Go web server on Azure Arm64

To validate your Go toolchain and runtime environment, build and run a lightweight web server. This confirms that compilation, networking, and runtime execution work correctly on your Ubuntu Pro 24.04 LTS Arm64 virtual machine on Azure Cobalt 100.

## Create the project directory

Create a folder for your Go web project and navigate to it:
```console
mkdir goweb && cd goweb
```

## Create an HTML page with Bootstrap styling

Next, create a simple web page that your Go server will serve. Open an editor and create `index.html`:
```console
nano index.html
```

Paste the following HTML code into the `index.html` file. This page uses Bootstrap for styling and includes a header, a welcome message, and a button that links to a Go-powered API endpoint.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Go Web on Azure ARM64</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #6dd5fa, #2980b9);
            color: white;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        .card {
            background: rgba(255, 255, 255, 0.9);
            color: #333;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card p-5">
            <h1 class="mb-3"> Go Web on Azure Arm64</h1>
            <p class="lead">This page is powered by Golang running on the Microsoft Azure Cobalt 100 processors.</p>
            <a href="/api/hello" class="btn btn-primary mt-3">Test API Endpoint</a>
        </div>
    </div>
</body>
</html>
```

Now, let’s create the Go program that will serve your static HTML page and expose a simple API endpoint.

Open an editor and create `main.go`:
```console
nano main.go
```
Paste the following code into the `main.go` file. This sets up a basic web server that serves files from the current folder, including the `index.html` you just created. When it runs, it will print a message showing the server address.

Paste the following code into `main.go`:
```go
package main
import (
    "encoding/json"
    "log"
    "net/http"
    "time"
)
func main() {
    // Serve index.html for root
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        if r.URL.Path == "/" {
            http.ServeFile(w, r, "index.html")
            return
        }
        http.FileServer(http.Dir(".")).ServeHTTP(w, r)
    })
    // REST API endpoint for JSON response
    http.HandleFunc("/api/hello", func(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(map[string]string{
            "message": "Hello from Go on Azure ARM64!",
            "time":    time.Now().Format(time.RFC1123),
        })
    })
    log.Println("Server running on http://0.0.0.0:80")
    log.Fatal(http.ListenAndServe(":80", nil))
}
```
{{% notice Note %}}Running on port 80 requires root privileges. Use sudo with the full Go path if needed.{{% /notice %}}

## Run the web server

Compile and start the server:
```console
sudo /usr/local/go/bin/go run main.go
```

Expected output:
```output
2025/08/19 04:35:06 Server running on http://0.0.0.0:80
```

On Ubuntu Pro 24.04 LTS virtual machines, UFW (Uncomplicated Firewall) is used to manage firewall rules. By default, it allows only SSH (port 22), while other inbound connections are blocked. 

Even if you have already configured Azure Network Security Group (NSG) rules to allow inbound traffic on port 80, the VM level firewall might still block HTTP requests until explicitly opened.

Run the following commands to allow HTTP traffic on port 80:

```console
sudo ufw allow 80/tcp
sudo ufw enable
```
After enabling UFW and allowing traffic on port 80, confirm that the firewall is now configured correctly by running:

```console
sudo ufw status
```
You should see output similar to: 
```output
Status: active

To                         Action      From
--                         ------      ----
80/tcp                     ALLOW       Anywhere
80/tcp (v6)                ALLOW       Anywhere (v6)
```

{{% notice Note %}}
If UFW is already active, `sudo ufw enable` might warn you about disrupting SSH. Proceed only if you understand the impact, or use an Azure VM serial console as a recovery option.
{{% /notice %}}

## Open the site in a browser

Print your VM’s public URL:
```console
echo "http://$(curl -s ifconfig.me)/"
```

Open this URL in your browser. You should see the styled HTML landing page served by your Go application.

![Go web server running on Azure Arm64 alt-text#center](images/go-web.png "Go web server running on Azure Arm64")

Reaching this page confirms that Go is installed, the environment is configured, and your Go web server works end-to-end on Azure Cobalt 100 (Arm64). You can now proceed to benchmarking tests.
