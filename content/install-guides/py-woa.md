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

Python has native support for [Windows on Arm](https://learn.microsoft.com/en-us/windows/arm/overview). Starting with version 3.11, an official installer is available. The latest version is 3.13.0.

A number of developer-ready Windows on Arm [devices](/learning-paths/laptops-and-desktops/intro/find-hardware/) are available.

Windows on Arm instances are available with Microsoft Azure. For further information, see [Deploy a Windows on Arm virtual machine on Microsoft Azure](/learning-paths/cross-platform/woa_azure/).

## How do I download and install Python for Windows on Arm?

To download and install Python for Windows on Arm, there is more than one option:

* You can download the installer from the [Python website](https://www.python.org/downloads/windows/). Locate the `ARM64` installer.

* You can download from a PowerShell terminal, by running the following:
```command
curl https://www.python.org/ftp/python/3.13.0/python-3.13.0-arm64.exe --output python-3.13.0-arm64.exe
```

Once you have downloaded Python, run the installer `exe` file on a Windows on Arm machine. 

The installer will start. 

Tick the checkbox **Add python.exe to PATH** to enable you to easily invoke Python from any directory.

![Install #center](/install-guides/_images/py1-woa.png)

**Setup was successful** is displayed when complete.

![Complete #center](/install-guides/_images/py2-woa.png)

## How do I start Python on Windows? 

To start Python on Windows, at a Windows Command prompt or a PowerShell prompt, use `python` or `py` to start the interpreter:

```cmd
py
```

The interpreter starts with an output similar to:

```output
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 10:17:29) [MSC v.1941 64 bit (ARM64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Enter `exit()` to leave the interpreter:

```python
exit()
```

## How can I run a Python example?

To run a Python example, and confirm that Python is working, use a text editor to save the code below to a file named `uname.py`.

```python
import platform
print("Python version", platform.python_version())
print("Machine is", platform.uname().system, platform.uname().release, platform.uname().machine)
```

Run the code:

```console
py uname.py
```

Running on a Windows on Arm machine produces an output similar to:

```output
Python version 3.13.0
Machine is Windows 11 ARM64
```

## How do I install Python packages?

To install Python packages, you can use Python `pip`. 

For example, to install [Flask](https://palletsprojects.com/p/flask/):
```console
pip install Flask
```

Use a text editor to save the code below as `hello.py`:

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
Using the URL that the application prints, open a browser. Here is an example:
```url
http://127.0.0.1:5000
```
The output is displayed in the browser window.

![Complete #center](/install-guides/_images/flask-woa.png)

The accesses are reported in the command window:

```output
127.0.0.1 - - [<timestamp>] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [<timestamp>] "GET /favicon.ico HTTP/1.1" 404 -
10.8.0.10 - - [<timestamp>] "GET / HTTP/1.1" 200 -
10.8.0.10 - - [<timestamp>] "GET /favicon.ico HTTP/1.1" 404 -
```

Use **Ctrl + C** to stop the application.

## Is Python IDLE available?

Python `IDLE` is included in the installation. IDLE is a simple IDE for Python development. You can locate it in the start menu.

You can create and run Python applications in this environment.

For example, use **File**, then **Open...** (or **Ctrl + O**) to open the above `uname.py`.

Then select **Run** and **Run module** (or **F5**) to execute.

![IDLE uname #center](/install-guides/_images/py3-woa.png)


You are now ready to use Python on your Windows on Arm device. 
