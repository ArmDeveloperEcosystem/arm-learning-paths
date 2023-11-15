---
title: Install the required dependencies
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
Irrespective of the kind of Arm machine you use, the instructions for this
learning paths are going to be the same.
You need to login via SSH into your remote server or open a terminal on your
local VM or physical machine. This learning path uses Ubuntu 22.04 LTS.

## Install the latest version of Python (optional)
Ubuntu 22.04 offers pre-installed Python 3.10 binaries. You can just use this
version or alternatively, you can install the latest version of Python.
A quick way to install the most recent version of Python is via
[Deadsnakes PPA](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa).

Add the Deadsnakes repository:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
```

Install Python 3.12.

```bash
sudo apt install python3.12 python3.12-venv
```

Check that Python 3.12 works as expected, shown in the output below:

```output
~$ python3.12
Python 3.12.0 (main, Oct 21 2023, 17:42:12) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```

## Install the web server and the database
This learning path uses Nginx as the web server and PostgreSQL as the database for the Django application.

To install Nginx using a package manager on Ubuntu:

```bash
sudo apt install nginx
```

To install PostgreSQL using a package manager on Ubuntu, you can follow the [postgresql.org install instructions](https://www.postgresql.org/download/linux/ubuntu/).

You can also use a different web server and database. If you do, you will have to change the appropriate configuration files in the later sections.

## Install tree package
As you will use the `tree` command in later sections to inspect your directory file tree structure, ensure you have the package installed first:

```bash
sudo apt install tree
```

## Create the virtual environment
A good practice is always to use a virtual environment when dealing with python
code. This is because it allows you to run multiple applications with different
dependencies in the same OS without conflicts.

Create and activate the virtual environment:

```bash
python3.12 -m venv venv
source venv/bin/activate
```

The prompt of your terminal has `(venv)` as a prefix and this means the virtual
environment is now active. From this point on, you will run all the commands inside your virtual environment.

## Install python dependencies
With the active virtual environment, you can now install the Python dependencies
for running your Django application.

```bash
pip install django gunicorn psycopg[binary]
```

After the installation, verify that you have the right packages installed:

```bash
pip list
```
The output should look similar to (version numbers might change):

```output
Package           Version
----------------- -------
asgiref           3.7.2
Django            4.2.7
gunicorn          21.2.0
packaging         23.2
pip               23.3.1
psycopg           3.1.12
psycopg-binary    3.1.12
sqlparse          0.4.4
typing_extensions 4.8.0
```

To verify you are able to run Django and gunicorn, try importing them
with Python as shown below:

```python
(venv) ~$ python
Python 3.12.0 (main, Oct 21 2023, 17:42:12) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> import gunicorn
>>> django.VERSION
(4, 2, 7, 'final', 0)
>>> gunicorn.version_info
(21, 2, 0)
```

In order to have a production-like installation, you need `gunicorn` which is a
Python WSGI (Web Server Gateway Interface) HTTP server for UNIX and is
compatible with Django.

{{% notice Note %}}
Whenever you are in the virtual environment, just type
`python` (without appending any version) as it will point to the python binary used
to create the virtual environment.
{{% /notice %}}
