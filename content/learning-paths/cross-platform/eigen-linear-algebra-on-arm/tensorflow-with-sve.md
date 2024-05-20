---
title: Build and Run Tensorflow with SVE
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build Tensorflow with SVE enabled!

Now that you have seen that you can use Eigen with SVE enabled, it's time to build your own SVE-enabled Tensorflow!

Tensorflow is a very complicated software and even building it requires some effort. However, following the next instructions here should get you up and running with relative ease.

### Install Build Requirements for Tensorflow

You are going to follow the [Tensorflow Instructions to build from source](https://www.tensorflow.org/install/source), slightly modified.

Before you attempt to build Tensorflow, you need to install the build dependencies first.

The following packages are needed in a recent Debian/Ubuntu distribution, though you may have to change to the relevant packages if you're using a different distribution:

```bash
# apt -u install clang-17 python3-pip golang python3-virtualenv default-jdk-headless patchelf libhdf5-dev
```

Afterwards you will need to download `bazelisk`: a Go-based tool which you can use instead of `bazel` which is a bit trickier to install. You need to download the Linux arm64 version and rename that as `bazel` in your `$HOME/bin` directory and you will also need to add this directory to your `$PATH`.

```bash
$ mkdir ~/bin
$ wget https://github.com/bazelbuild/bazelisk/releases/download/v1.20.0/bazelisk-linux-arm64 -O ~/bin/bazel
$ chmod +x ~/bin/bazel
```

Some python packages need to be installed using `pip` and it's best that we do that in a virtual environment, using the `virtualenv` Python package.

After you create the environment, you will need to activate it.

```bash
$ virtualenv ~/python-venv
$ . ~/python-venv/bin/activate
```

Next, clone Tensorflow from its git repository to your system:

```bash
$ git clone https://github.com/tensorflow/tensorflow.git
$ cd tensorflow
```

Now you can configure Tensorflow, but in order to do that you will need to give answers to some questions, but in this case you can probably just select the defaults.

However, especially in the case of CPU flags, you need to pass the relevant SVE flags as you did before to make sure that Eigen selects the SVE backend.

```bash
(python-venv) $ python3 ./configure.py
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

And start the build, at which point you might want to take a walk or bake a cake as this is going to take quite a long while, even on fast systems.

```bash
$ bazel build //tensorflow/tools/pip_package:wheel --repo_env=WHEEL_NAME=tensorflow_cpu
```

When the build is over, you should have `tensorflow` `pip` package in this directory `bazel-bin/tensorflow/tools/pip_package/wheel_house` with a filename similar to this:

```bash
tensorflow_cpu-2.17.0-cp311-cp311-linux_aarch64.whl
```

You are finally able to install your custom Tensorflow build to your system, using `pip install`

```bash
$ pip install
```

Installing it will take a while as it will install all dependencies but when it finishes you should have Tensorflow ready to use! Time to test if it actually works!

```bash
$ python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))
tf.Tensor(492.89847, shape=(), dtype=float32)
```

If you get the above response then your Tensorflow installation was successful! Happy AI training!


```bash
