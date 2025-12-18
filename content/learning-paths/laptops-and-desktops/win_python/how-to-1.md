---
# User change
title: "Platform-specificity of the Python packages"

weight: 2

layout: "learningpathall"
---

## Python on Arm
Arm-native build tools are provided to enable the developers to create Arm64 apps using different technologies, including C/C++, .NET or even Python. More specifically, Python can be useful to rapidly prototype complex solutions that can be used for many purposes, including scientific/numerical computing, signal and image processing, training and optimizing machine learning models. As many of those tasks require extensive computations, having the Arm support enables us to boost the application performance with an optimized power consumption.

The official Python implementation and its standard library is provided by CPython. It compiles code into bytecode before interpretation, enabling it to contain platform-specific code.

Starting from Python v3.11, native support for Arm devices running Windows 11 is available. To use this feature, you just install a dedicated Arm64 Python package. There is no change to your scripts. However, as described below, there can be some build or porting requirements for the dependent pip packages, especially when you rely on the platform-specific dependencies.

In this learning path you will see how this works for the popular NumPy package on Python 3.12.

## Before you begin
Before going further, let's make sure you have installed Python v3.12 using the following installation packages: 

1. [x64](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe)
2. [Arm64](https://www.python.org/ftp/python/3.12.0/python-3.12.0-arm64.exe)

Install Python v3.12 for Arm64 and x64. The installation process is the same as described in [Python on Windows on Arm](/install-guides/py-woa/).

To run the Python interpreter for x64, open the command prompt and type the following command:

```console
py -3.12-64
```

The output will be similar to the following one:

```output
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Press CTRL+Z or type **exit()** to leave the interpreter.

Similarly, you can use the Python interpreter for Arm64:

```console
py -3.12-arm64
```

The above command generates the following output:

```output
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:15:47) [MSC v.1935 64 bit (ARM64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Again, close it using the CTRL+Z or the **exit()** command.

{{% notice Note %}} By comparing the output of the two Python interpreters, we can see that both interpreters use the MSC v.1935 compiler for both x64 (labeled as AMD64) or Arm64 (labeled ARM64).{{% /notice %}}

## Python packages

Because x64 and Arm64-based Python use different underlying C compilers, the Python packages can have compatibility and porting issues. Traditionally, you install Python packages using pip, which automatically installs the dependencies. First, pip tries to find the platform-independent package (called the wheel). Then, it looks for the platform-specific package and eventually builds it from the source code.

If you are writing Python packages to take advantage of Arm64, you must ensure you compile your packages for Arm64, not x64. This is not a problem for pure (platform-independent) Python packages.

You will now see what this means in practice by installing the NumPy package using pip.

Open the command prompt and type the following command to ensure you use the latest pip version:

```console
py -3.12-arm64 -m pip install --upgrade pip
```

The output will look as follows:

```output
Requirement already satisfied: pip in c:\users\db\appdata\local\programs\python\python312-arm64\lib\site-packages (23.2.1)
Collecting pip
  Obtaining dependency information for pip from https://files.pythonhosted.org/packages/47/6a/453160888fab7c6a432a6e25f8afe6256d0d9f2cbd25971021da6491d899/pip-23.3.1-py3-none-any.whl.metadata
  Downloading pip-23.3.1-py3-none-any.whl.metadata (3.5 kB)
Downloading pip-23.3.1-py3-none-any.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 3.0 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.2.1
    Uninstalling pip-23.2.1:
      Successfully uninstalled pip-23.2.1  
Successfully installed pip-23.3.1
```

Repeat the same for x64:

```console
py -3.12-64 -m pip install --upgrade pip
```

Now, try to install the NumPy package, which you will use later on to implement the sample application. To install NumPy, type:

```console
py -3.12-arm64 -m pip install numpy
```

The command will generate the following output:

```output
Collecting numpy
  Downloading numpy-1.26.2.tar.gz (15.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.7/15.7 MB 3.2 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [21 lines of output]
      + C:\Users\db\AppData\Local\Programs\Python\Python312-arm64\python.exe C:\Users\db\AppData\Local\Temp\pip-install-z7o5tmzj\numpy_a28e0fc1b6724727af70f23c6ac2be78\vendored-meson\meson\meson.py setup C:\Users\db\AppData\Local\Temp\pip-install-z7o5tmzj\numpy_a28e0fc1b6724727af70f23c6ac2be78 C:\Users\db\AppData\Local\Temp\pip-install-z7o5tmzj\numpy_a28e0fc1b6724727af70f23c6ac2be78\.mesonpy-2y9byjdq\build -Dbuildtype=release -Db_ndebug=if-release -Db_vscrt=md --native-file=C:\Users\db\AppData\Local\Temp\pip-install-z7o5tmzj\numpy_a28e0fc1b6724727af70f23c6ac2be78\.mesonpy-2y9byjdq\build\meson-python-native-file.ini
      The Meson build system
      Version: 1.2.99
      Source dir: C:\Users\db\AppData\Local\Temp\pip-install-z7o5tmzj\numpy_a28e0fc1b6724727af70f23c6ac2be78
      Build dir: C:\Users\db\AppData\Local\Temp\pip-install-z7o5tmzj\numpy_a28e0fc1b6724727af70f23c6ac2be78\.mesonpy-2y9byjdq\build
      Build type: native build
      Project name: NumPy
      Project version: 1.26.2
      WARNING: Failed to activate VS environment: Could not find C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe

      ..\..\meson.build:1:0: ERROR: Unknown compiler(s): [['icl'], ['cl'], ['cc'], ['gcc'], ['clang'], ['clang-cl'], ['pgcc']]
      The following exception(s) were encountered:
      Running `icl ""` gave "[WinError 2] The system cannot find the file specified"
      Running `cl /?` gave "[WinError 2] The system cannot find the file specified"
      Running `cc --version` gave "[WinError 2] The system cannot find the file specified"
      Running `gcc --version` gave "[WinError 2] The system cannot find the file specified"
      Running `clang --version` gave "[WinError 2] The system cannot find the file specified"
      Running `clang-cl /?` gave "[WinError 2] The system cannot find the file specified"
      Running `pgcc --version` gave "[WinError 2] The system cannot find the file specified"

      A full log can be found at C:\Users\db\AppData\Local\Temp\pip-install-z7o5tmzj\numpy_a28e0fc1b6724727af70f23c6ac2be78\.mesonpy-2y9byjdq\build\meson-logs\meson-log.txt
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
```

We can see that the installation has failed. For Arm64, there is no platform-specific wheel. So, pip downloads and tries to build the package from the source code to create the local Arm64 package wheel. However, as you do not have the build tools yet, the installation was not successful.

Before going any further, try to install NumPy for x64 by invoking the following command:

```console
py -3.12-64 -m pip install numpy
```

For x64 there is a platform-specific wheel available so the installation is successful, which is confirmed by the command output:

```output
Collecting numpy
  Downloading numpy-1.26.2-cp312-cp312-win_amd64.whl.metadata (61 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 kB 467.6 kB/s eta 0:00:00
Downloading numpy-1.26.2-cp312-cp312-win_amd64.whl (15.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.5/15.5 MB 2.5 MB/s eta 0:00:00
Installing collected packages: numpy
Successfully installed numpy-1.26.2
```

## Arm build tools
To install the NumPy package, we will need to provide the Arm build tools. Install Visual Studio 2022 Community with the **Desktop development with C++** workload and **Arm build tools** as explained in this [installation guide](https://developer.arm.com/documentation/102528/0100/Install-Visual-Studio). 

After installing the build tools, restart your machine and install NumPy package with the following command:

```
py -3.12-arm64 -m pip install numpy 
```

Now, the installation will be successful and you will see the following output:

```output
Collecting numpy                                                                                                          Using cached numpy-1.26.2.tar.gz (15.7 MB)                                                                              Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: numpy
  Building wheel for numpy (pyproject.toml) ... done
  Created wheel for numpy: filename=numpy-1.26.2-cp312-cp312-win_arm64.whl size=16845040 sha256=01f831dde6b7d4dc7729bf1c894af3ea5f3808a401a6c059451b3e55f66e143e
  Stored in directory: c:\users\db\appdata\local\pip\cache\wheels\95\2f\43\2ca1fa1956ac9cb61ca696a9924ed5333df1d1b3ce9013f5d4
Successfully built numpy
Installing collected packages: numpy
Successfully installed numpy-1.26.2
```

## Summary
You have just learned how pip can build the package from the source code and when the platform-independent package (called the wheel) is unavailable. In the next section, you will use the NumPy package to build the application.
