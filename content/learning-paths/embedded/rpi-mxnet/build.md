 ---
# User change
title: "Build MXNet"

weight: 3

layout: "learningpathall"

---

## Build MXNet

You should now be inside the Raspberry Pi OS file system as root with the `#` prompt. 

Install required software to build MXNet.

```console
apt update
apt upgrade -y
apt-get -y install git cmake ninja-build gfortran liblapack* libblas* libopencv* libopenblas* python3-dev python3-pip python-dev virtualenv
pip3 install Cython
```

Instead of `root` change to user `pi` to build the application. 

```console
su pi
```

Change to the home directory for user `pi`, this is the default user for Raspberry Pi OS. 

```console
cd $HOME
```

Clone the MXNet application from GitHub. 

```console
git clone https://github.com/apache/incubator-mxnet.git --recursive
cd incubator-mxnet
```

Create a new directory for the build. 

```console
mkdir build
cd build
```

Run the build commands, `cmake` to configure the build and `ninja` to do the compilation. 

```console
 cmake \
-DUSE_SSE=OFF \
-DUSE_CUDA=OFF \
-DUSE_OPENCV=ON \
-DUSE_OPENMP=ON \
-DUSE_SIGNAL_HANDLER=ON \
-DBUILD_CYTHON_MODULES=ON \
-DCMAKE_BUILD_TYPE=Release \
-GNinja ..
```

Use the `-j` option with the number of available CPUs.

```console
ninja -j8
```

Wait for the compile to complete. The required time to finish depends on the machine speed and number of CPUs available. More CPUs will shorten the compile time.

When the compile is complete, install the application. 

```console
cd ../python
sudo pip3 install -e . 
```

Test the result with Python. 

Using a text editor copy and paste the code below into a text file named `test.py`

```console
import mxnet
print(mxnet.__version__)
```

Run the example code:

```console
python3 ./test.py
```

The version of MXNet should be printed. 

The expected output format is below. Your version may be slightly different. 

```output
2.0.0
```

## Summary 

Building MXNet takes about 20 minutes on an AWS c6g.2xlarge EC2 instance.

A native build on a Raspberry Pi 4 can be done using the steps above. Setting the number of jobs too high will result in out of memory failures. With `-j4` and the build fails, even on a Raspberry Pi with Gb RAM. With `-j1` the build completes, but takes over 6 hours.

Continue to the next section to download the new image and install it on a Raspberry Pi for testing. 

