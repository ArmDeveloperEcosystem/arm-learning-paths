---
title: Install Ruby on Rails
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Ruby on Rails
In this section, you will learn how to install Ruby, Rails, and related tools (like rbenv and Bundler) on a SUSE Arm-based virtual machine. This guide will also cover installing the necessary dependencies to compile Ruby and run Rails applications smoothly.


### Update System Packages
Updates all system packages to the latest versions to ensure stability and security.

```console
sudo zypper update
```

### Install Required Dependencies
These packages are essential for compiling Ruby and its native extensions.

```console
sudo zypper install git curl gcc make patch libyaml-devel libffi-devel libopenssl-devel readline-devel zlib-devel gdbm-devel bzip2 bzip2-devel
```

### Install rbenv
**rbenv** is a lightweight Ruby version manager that allows multiple Ruby versions on the same system.

```console
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
source ~/.bashrc
```
- Clones the rbenv repository to manage Ruby versions
- Updates `PATH` so your shell can find rbenv
- Initializes rbenv in your shell session

### Install ruby-build Plugin
**ruby-build** is an rbenv plugin that provides the `rbenv install` command to compile and install different Ruby versions from source.

```console
git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build
```

### Install Ruby
Installs Ruby and sets it as the default version for your environment.

```console
rbenv install 3.4.6
rbenv global 3.4.6
ruby -v
```
- Installs Ruby 3.4.6 from source
- Sets it as the default Ruby version for your user
- `ruby -v` verifies the installed Ruby version

You should see output similar to:
```output
ruby 3.4.6 (2025-09-16 revision dbd83256b1) +PRISM [aarch64-linux]
```
{{% notice Note %}}
Ruby 3.4.0 introduced significant performance enhancements, notably improvements to YJIT (Yet Another Ruby JIT), a Ruby just-in-time compiler. These enhancements are particularly beneficial for Arm architectures, as YJIT has been optimized to deliver better performance on such platforms. To leverage these improvements, it is recommended that you upgrade to Ruby 3.4.0 or later.
You can view [this release note](https://www.ruby-lang.org/en/news/2024/12/25/ruby-3-4-0-released/)

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Ruby version 3.4.0, the minimum recommended on the Arm platforms.
{{% /notice %}}

### Install Bundler
**Bundler** manages Ruby project dependencies and ensures consistent gem versions across environments.

```console
gem install bundler
```

### Install Rails
Rails is a full-stack web application framework for Ruby that simplifies building database-backed web applications with convention over configuration.

```console
gem install rails
rails -v
```
- Installs the Rails framework
- `rails -v` verifies the installed Rails version

You should see output similar to:
```output
Rails 8.0.3
```

Ruby/Rails installation is complete. You can now proceed with the baseline testing.
