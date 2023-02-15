---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Python for Windows on Arm

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- python

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: 

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Python has native support for Windows on Arm.

Starting with version 3.11, an official installer is available.

## Download and install

[Download the installer](https://www.linaro.org/blog/windows-on-arm-now-supported-in-python-3-11-release/) to get started.

Once downloaded, run the installer exe file on a Windows on Arm machine. 

The installer will start. 

Check "Add python.exe to PATH" if you want to easily invoke python from any directory.

![Install](/install-tools/_images/py1-woa.png)

Wait for the installer to complete and show the message, "Setup was successful".

![Complete](/install-tools/_images/py2-woa.png)


## Invoke python

At a Windows Command prompt or a PowerShell prompt run python. 

Both python or py can be used to start the interpreter.

```cmd
C:\>py
Python 3.11.0 (main, Oct 24 2022, 18:15:22) [MSC v.1933 64 bit (ARM64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```


## Test an example

To confirm python is working, save the code below into a file uname.py 

```python
import platform

print("Python version", platform.python_version())

print("Machine is", platform.uname().system, platform.uname().release, platform.uname().machine)
```

Run the code.

```console
py uname.py
```

Running on a Windows on Arm machine produces the output:

```console
Python version 3.11.0
Machine is Windows 10 ARM64
```

## Installing packages

Python pip can be used to install packages. 

For example, to install Flask:

```console
pip install Flask
```

Save the code below as hello.py

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

Run the application.

```console
python hello.py
```

The output is:

```console
C:\>python hello.py
 * Serving Flask app 'hello'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.68.95:5000
Press CTRL+C to quit
```

Open a browser to the URL printed by the application http://127.0.0.1:5000

The output is in the browser.

![Complete](/install-tools/_images/flask-woa.png)


## Using IDLE

Python IDLE is included in the installation. IDLE is a simple IDE for python development.

![Complete](/install-tools/_images/py3-woa.png)

For more information check the [Linaro Windows on Arm project](https://www.linaro.org/windows-on-arm/python/)
