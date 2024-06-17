---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Python for Windows on Arm

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- python
- windows
- woa
- windows on arm
- open source windows on arm

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://www.python.org/doc/

author_primary: Jason Andrews

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Python has native support for [Windows on Arm](https://learn.microsoft.com/en-us/windows/arm/overview). Starting with version 3.11, an official installer is available. The latest version at time of writing is 3.12.0.

A number of developer ready Windows on Arm [devices](../../learning-paths/laptops-and-desktops/intro/find-hardware/) are available.

Windows on Arm instances are available with Microsoft Azure. For more information, see [Deploy a Windows on Arm virtual machine on Microsoft Azure](../../learning-paths/cross-platform/woa_azure/).

## Download and install

The installer can be downloaded from the [Python website](https://www.python.org/downloads/windows/). Locate the `ARM64` installer.

You can also download from a PowerShell terminal.
```command
curl https://www.python.org/ftp/python/3.12.0/python-3.12.0-arm64.exe -O python-3.12.0-arm64.exe
```

Once downloaded, run the installer `exe` file on a Windows on Arm machine. 

The installer will start. 

Check `Add python.exe to PATH` if you want to easily invoke python from any directory.

![Install #center](/install-guides/_images/py1-woa.png)

`Setup was successful` is displayed when complete.

![Complete #center](/install-guides/_images/py2-woa.png)

## Invoke python

At a Windows Command prompt or a PowerShell prompt use `python` or `py` to start the interpreter.
```cmd
py
```
```output
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:15:47) [MSC v.1935 64 bit (ARM64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Enter `exit()` to leave interpreter.
```python
exit()
```

## Test an example

To confirm python is working, save the code below into a file `uname.py`.

#### uname.py
```python
import platform
print("Python version", platform.python_version())
print("Machine is", platform.uname().system, platform.uname().release, platform.uname().machine)
```

Run the code.
```console
py uname.py
```
Running on a Windows on Arm machine produces the output similar to:
```output
Python version 3.12.0
Machine is Windows 11 ARM64
```

## Installing packages

Python `pip` can be used to install packages. 

For example, to install [Flask](https://palletsprojects.com/p/flask/):
```console
pip install Flask
```

Save the code below as `hello.py`:

#### hello.py
```python
import platform
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1><b>Hello from %s %s %s %s</b></h1>" % (platform.system(), platform.release(), platform.version(), platform.machine())

if __name__ == "__main__":
    app.run(host="0.0.0.0")
```

Run the application:
```console
python hello.py
```

The output will be similar to:
```output
 * Serving Flask app 'hello'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.8.0.10:5000
Press CTRL+C to quit
```
Open a browser to the URL printed by the application. In this example:
```url
http://127.0.0.1:5000
```
The output is displayed in the browser window.

![Complete #center](/install-guides/_images/flask-woa.png)

The accesses are reported in the command prompt:
```output
127.0.0.1 - - [<timestamp>] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [<timestamp>] "GET /favicon.ico HTTP/1.1" 404 -
10.8.0.10 - - [<timestamp>] "GET / HTTP/1.1" 200 -
10.8.0.10 - - [<timestamp>] "GET /favicon.ico HTTP/1.1" 404 -
```
Use `Ctrl+C` to kill the application.

## Using IDLE

Python `IDLE` is included in the installation. IDLE is a simple IDE for python development. You can locate it in your start menu.

![IDLE #center](/install-guides/_images/idle.png)

You can create and run Python applications in this environment.

For example, use `File` > `Open...` (`Ctrl+O`) to open the above `uname.py`.

Then select `Run` > `Run module` (`F5`) to execute.

![IDLE uname #center](/install-guides/_images/py3-woa.png)



You are now ready to use Python on your Windows on Arm device. 
