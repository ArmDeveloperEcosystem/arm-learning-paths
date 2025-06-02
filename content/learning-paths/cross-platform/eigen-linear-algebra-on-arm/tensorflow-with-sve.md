---
title: Build and Run TensorFlow with SVE
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build TensorFlow with SVE enabled

Now that you have seen that you can use Eigen with SVE enabled, it's time to build your own SVE-enabled TensorFlow.

TensorFlow is a complex application, and building it requires significant effort. However, following the instructions below, you should be able to build and run it. 

### Install Build Requirements for TensorFlow

You are going to follow the [TensorFlow Instructions to build from source](https://www.tensorflow.org/install/source) with some slight modifications.

Before you build TensorFlow, you need to install the build dependencies first.

The following packages are required for the recent Debian/Ubuntu distribution used here. You might have to change the packages if you're using a different Linux distribution:

```bash
sudo apt -u install gcc g++ python3-pip golang python3-virtualenv default-jdk-headless patchelf libhdf5-dev -y
```

You also need to download `bazelisk`: a Go-based tool which you can use instead of `bazel`. You need to download the Linux arm64 version and rename it as `bazel`, and add it to your search path. One way is to put the file in your `$HOME/bin` directory, and add this directory to your `$PATH`:

```bash
mkdir ~/bin
wget https://github.com/bazelbuild/bazelisk/releases/download/v1.20.0/bazelisk-linux-arm64 -O ~/bin/bazel
chmod +x ~/bin/bazel
export PATH=$PATH:$HOME/bin
```

Some python packages need to be installed using `pip` and it's best that you do that in a virtual environment, using the `virtualenv` Python package:

After you create the environment, you need to activate it:

```bash
virtualenv ~/python-venv
. ~/python-venv/bin/activate
```

Your shell prompt now shows the virtual environment, which should look like this: 

```output
(python-venv) $
```

Next, clone TensorFlow from its Git repository to your system:

```bash
git clone https://github.com/tensorflow/tensorflow.git
cd tensorflow
```

Now you can configure TensorFlow. Configuration requires you to answer some questions, but you can select the defaults.

You need to pass the relevant SVE flags as you did before to make sure that Eigen selects the SVE backend.

Here is the configuration transcript, only the first line is a command you can copy and run:

```bash { output_lines = "2-33" }
python3 ./configure.py
You have bazel 6.5.0 installed.
Please specify the location of python. [Default is /home/markos/python-venv/bin/python3]:

Found possible Python library paths:
  /home/markos/python-venv/lib/python3.11/site-packages                                                                                                                                                                       Please input the desired Python library path to use.  Default is [/home/markos/python-venv/lib/python3.11/site-packages]
Do you wish to build TensorFlow with ROCm support? [y/N]:
No ROCm support will be enabled for TensorFlow.

Do you wish to build TensorFlow with CUDA support? [y/N]:
No CUDA support will be enabled for TensorFlow.

Do you want to use Clang to build TensorFlow? [Y/n]: n
GCC will be used to compile TensorFlow.

Please specify the path to clang executable. [Default is /usr/lib/llvm-17/bin/clang]:


You have Clang 17.0.6 installed.

Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -Wno-sign-compare]: -march=armv9-a -msve-vector-bits=128 -DEIGEN_ARM64_USE_SVE


Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]:
Not configuring the WORKSPACE for Android builds.
                                                                                                                                                                                                                              Preconfigured Bazel build configs. You can use any of the below by adding "--config=<>" to your build command. See .bazelrc for more details.                                                                                         --config=mkl            # Build with MKL support.
        --config=mkl_aarch64    # Build with oneDNN and Compute Library for the Arm Architecture (ACL).
        --config=monolithic     # Config for mostly static monolithic build.                                                                                                                                                          --config=numa           # Build with NUMA support.
        --config=dynamic_kernels        # (Experimental) Build kernels into separate shared objects.
        --config=v1             # Build with TensorFlow 1 API instead of TF 2 API.
Preconfigured Bazel build configs to DISABLE default on features:                                                                                                                                                                     --config=nogcp          # Disable GCP support.                                                                                                                                                                                --config=nonccl         # Disable NVIDIA NCCL support.
```

Run `bazel` to start the build. 

{{% notice Note %}}
You might want to take a break and return later as this takes quite a long while, even on fast systems.
{{% /notice %}}

```bash
bazel build //tensorflow/tools/pip_package:wheel --repo_env=WHEEL_NAME=tensorflow_cpu
```

When the build is complete, you should have `tensorflow` `pip` package in this directory `bazel-bin/tensorflow/tools/pip_package/wheel_house` with a filename similar to this:

```output
tensorflow_cpu-2.17.0-cp311-cp311-linux_aarch64.whl
```

You are finally able to install your custom TensorFlow build to your system, using `pip install`:

```bash
pip install
```

Installing it will take a while as it will install all dependencies but when it finishes you should have TensorFlow ready to use! 

You can test it to see if it works by running:

```bash { output_lines = "2" }
python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))
tf.Tensor(492.89847, shape=(), dtype=float32)
```

If you get the above response then your TensorFlow installation was successful.

