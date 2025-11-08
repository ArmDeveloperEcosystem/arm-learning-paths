---
title: Install Ruby on Rails on SUSE Linux
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you'll install Ruby, Rails, and essential supporting tools on your Google Cloud C4A instance running SUSE Enterprise Linux. The steps ensure your environment is ready to build, deploy, and optimize Ruby on Rails applications on Arm-based infrastructure.

## Update system packages
Start by updating your system packages to ensure you have the latest security patches and development tools needed for Ruby installation:

```console
sudo zypper update
```
## Install required dependencies
Install essential development libraries and tools that Ruby needs to compile and run properly on your SUSE Arm64 system:

```console
sudo zypper install git curl gcc make patch libyaml-devel libffi-devel libopenssl-devel readline-devel zlib-devel gdbm-devel bzip2 bzip2-devel
```

## Install rbenv
`rbenv` is a lightweight Ruby version manager that enables you to install and manage multiple Ruby versions on the same system. This is particularly useful for developers running different Rails applications that require specific Ruby versions. 

Use rbenv to manage multiple Ruby versions and ensure compatibility across different Rails projects:

```console
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
source ~/.bashrc
```
These commands configure rbenv for your environment by doing the following:
- Cloning the rbenv repository to your home directory.
- Adding rbenv to your PATH so the shell can find it.
- Configuring rbenv to initialize automatically in new shell sessions.
## Install ruby-build plugin
Install the `ruby-build` plugin to enable rbenv to compile and install Ruby versions from source:

```console
git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build
```

This plugin adds the `rbenv install` command, which you'll use to download, compile, and install specific Ruby versions optimized for your Arm64 architecture.
## Install Ruby

Now that rbenv and ruby-build are configured, install Ruby 3.4.6 and set it as your default version:

```console
rbenv install 3.4.6
rbenv global 3.4.6
ruby -v
```

This process accomplishes several tasks:
- Downloads and compiles Ruby 3.4.6 from source, optimized for your Arm64 architecture.
- Sets Ruby 3.4.6 as the default version system-wide for your user account.
- Verifies the installation by displaying the active Ruby version.

The compilation process can take several minutes as Ruby builds natively for your Arm processor.

You should see output similar to:
```output
ruby 3.4.6 (2025-09-16 revision dbd83256b1) +PRISM [aarch64-linux]
```
{{% notice Note %}}
Ruby 3.4.0 and later introduced major performance enhancements, especially in YJIT (Yet Another Ruby JIT), Ruby’s Just-In-Time compiler. These enhancements are particularly beneficial for Arm architectures, as YJIT has been optimized to deliver better performance on such platforms. To leverage these improvements, upgrade to Ruby 3.4.0 or later.
For further information, see the [Ruby 3.4.0 release notes](https://www.ruby-lang.org/en/news/2024/12/25/ruby-3-4-0-released/).

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Ruby version 3.4.0.
{{% /notice %}}

## Install Bundler
Bundler is Ruby’s dependency management tool. It ensures that all required gems (libraries) for your Rails application are installed and consistent across development, test, and production environments.

Install Bundler globally:

```console
gem install bundler
```
This command installs Bundler for the active Ruby version managed by `rbenv`.
## Install Rails

Rails is a web framework for Ruby that makes building web applications faster and easier. Install Rails to start creating web applications on your Arm-based system:

```console
gem install rails
```

This command downloads and installs the latest version of Rails, along with all its dependencies, optimized for your Arm64 architecture.
## Verify your Rails installation

Check that Rails installed correctly and is accessible in your environment:

```console
rails -v
```

The output is similar to:
```output
Rails 8.0.3
```

This confirms Rails is ready to use for building web applications on your Arm-based system.

## What you've accomplished

You’ve completed the installation of Ruby and Rails on your Google Cloud C4A Arm-based SUSE Linux VM. Your environment is now ready for Arm-native Rails development, with all dependencies, version management, and performance enhancements in place. You’re prepared to start building, testing, and optimizing Ruby on Rails applications on Arm infrastructure.