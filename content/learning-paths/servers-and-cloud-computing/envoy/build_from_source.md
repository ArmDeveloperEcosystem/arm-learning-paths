---
title: "Build Envoy from source"
weight: 3
layout: "learningpathall"
---

## Building Envoy with Bazel

On Linux, run the following commands:

```console
sudo wget -O /usr/local/bin/bazel https://github.com/bazelbuild/bazelisk/releases/latest/download/bazelisk-linux-$([ $(uname -m) = "aarch64" ] && echo "arm64" || echo "amd64")
sudo chmod +x /usr/local/bin/bazel
```

## Install external dependencies

On Ubuntu, run the following:

```console
sudo apt update \
sudo apt-get install \
   autoconf \
   curl \
   libtool \
   patch \
   python3-pip \
   unzip \
   git \
   virtualenv
```

On Fedora (maybe also other red hat distros), run the following:

```console
dnf install \
    aspell-en \
    libatomic \
    libstdc++ \
    libstdc++-static \
    libtool \
    lld \
    patch \
    git \
    python3-pip
```

### Build envoy from the source code

For Alibaba Cloud Linux OS:

```console
sudo yum install llvm clang llvm-devel
git clone https://github.com/envoyproxy/envoy.git
bazel/setup_clang.sh /usr/
echo "build --config=clang" >> user.bazelrc
bazel build -c opt envoy.stripped --jobs=$(nproc)
```

On Ubuntu, download and extract the prebuilt Clang+LLVM package from [LLVM official site](http://releases.llvm.org/download.html). Then build envoy from source as shown:

```console
cd ~/
wget https://github.com/llvm/llvm-project/releases/download/llvmorg-17.0.1/clang+llvm-17.0.1-aarch64-linux-gnu.tar.xz
tar -xvf clang+llvm-17.0.1-aarch64-linux-gnu.tar.xz
git clone https://github.com/envoyproxy/envoy.git
cd envoy
bazel/setup_clang.sh ~/clang+llvm-17.0.1-aarch64-linux-gnu
echo "build --config=clang" >> user.bazelrc
bazel build -c opt envoy.stripped --jobs=$(nproc)
```

### Envoy Documentation

For more Envoy build documentations, you can refer to [Building Envoy with Bazel](https://github.com/envoyproxy/envoy/blob/main/bazel/README.md) and [Envoy Building](https://www.envoyproxy.io/docs/envoy/latest/start/building)
