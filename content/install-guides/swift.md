---

title: Swift
author: Jason Andrews

minutes_to_complete: 10
additional_search_terms:
- swift

layout: installtoolsall
multi_install: false
multitool_install_part: false
official_docs: https://www.swift.org/documentation/ 
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=Swift%20(Arm64)
test_images:
- ubuntu:latest
test_maintenance: true
tool_install: true
weight: 1
---

[Swift](https://swift.org/) is an open-source programming language initially developed by Apple for use with Apple's iOS, macOS, watchOS, and tvOS operating systems. It has since gained popularity as a general-purpose language suitable for a wide range of Linux and Windows applications. Swift is known for its safety, speed, and expressiveness, making it ideal for both beginners and experienced programmers.

Swift is available for macOS, Windows, and Linux, including Arm Linux distributions. In this guide, you'll learn how to install Swift on Ubuntu for Arm. 

## Before you begin

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

### Required software packages

Before you install Swift on Ubuntu 24.04, install the following packages: 

```bash
sudo apt update
sudo apt-get -y install \
          binutils \
          git \
          gnupg2 \
          libc6-dev \
          libcurl4-openssl-dev \
          libedit2 \
          libgcc-13-dev \
          libncurses-dev \
          libpython3-dev \
          libsqlite3-0 \
          libstdc++-13-dev \
          libxml2-dev \
          libz3-dev \
          pkg-config \
          tzdata \
          unzip \
          zlib1g-dev
```

## Dwnload and install Swift

Download Swift for Arm Linux:

{{% notice Note %}}
The following commands use Swift version 6.3.1 on Ubuntu 24.04. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find all available versions, see [Download Swift](https://www.swift.org/download/).
{{% /notice %}}

```bash
wget https://download.swift.org/swift-6.3.1-release/ubuntu2404-aarch64/swift-6.3.1-RELEASE/swift-6.3.1-RELEASE-ubuntu24.04-aarch64.tar.gz
```

Extract the archive:

```bash
sudo tar -xf swift-6.3.1-RELEASE-ubuntu24.04-aarch64.tar.gz -C /usr/local
```

Add the `bin/` directory to your search path:

```bash
echo 'export PATH="$PATH:/usr/local/swift-6.3.1-RELEASE-ubuntu24.04-aarch64/usr/bin"' >> ~/.bashrc
source ~/.bashrc
```

## Confirm Swift is working

To confirm Swift is working, print the version:

```bash
swift --version
```

The output is similar to:

```output
Swift version 6.3.1 (swift-6.3.1-RELEASE)
Target: aarch64-unknown-linux-gnu
```

You can also create and run a simple example program. 

Use a text editor to create a new file named `hello.swift` and add the following code:

```swift
print("Hello from Swift on Arm Linux!")
```

Compile and run the program:

```console
swift hello.swift
```

The output will be similar to:

```output
Hello from Swift on Arm Linux!
```

You can also compile and run the program using:

```console
swiftc hello.swift -o hello
./hello
```

The output will be the same:

```output
Hello from Swift on Arm Linux!
```

You are now ready to use the Swift programming language on your Arm Linux computer.

