---
title: Install Ruby on Rails
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Ruby on Rails
In this section, you’ll install Ruby, Rails, and essential supporting tools on a SUSE Arm64 your Google Cloud C4A instance running SUSE Enterprise Linux. The steps ensure your environment is ready to build, deploy, and optimize Ruby on Rails applications on Arm-based infrastructure.

### Update System Packages
Before installation, update all existing system packages. This ensures you have the latest security patches, compiler toolchains, and library versions compatible with Ruby.

```console
sudo zypper update
```

### Install Required Dependencies
Before installing Ruby, you need to install several core development libraries and tools. These packages ensure that Ruby and its native extensions compile and run correctly on your SUSE Arm64 environment.

```console
sudo zypper install git curl gcc make patch libyaml-devel libffi-devel libopenssl-devel readline-devel zlib-devel gdbm-devel bzip2 bzip2-devel
```

### Install rbenv
`rbenv` is a lightweight Ruby version manager that enables you to install and manage multiple Ruby versions on the same system. This is particularly useful for developers running different Rails applications that require specific Ruby versions.

```console
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
source ~/.bashrc
```
With these steps you have cloned the `rbenv` repository to manage Ruby versions. Your `PATH` is updated so your shell can find rbenv. It then initializes rbenv in your shell session. 

### Install ruby-build Plugin
`ruby-build` is an rbenv plugin that adds the `rbenv` install command, allowing you to compile and install specific Ruby versions from source. 

```console
git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build
```

### Install Ruby
Now that `rbenv` and `ruby-build` are set up, you can install Ruby and configure it as your system’s default version. This step compiles Ruby from source:

```console
rbenv install 3.4.6
rbenv global 3.4.6
ruby -v
```
With these commands you have: 
- Installed Ruby 3.4.6 from source
- Sets it as the default Ruby version for your user
- `ruby -v` verifies the installed Ruby version

You should see output similar to:
```output
ruby 3.4.6 (2025-09-16 revision dbd83256b1) +PRISM [aarch64-linux]
```
{{% notice Note %}}
Ruby 3.4.0 and later introduced major performance enhancements, especially in YJIT (Yet Another Ruby JIT), Ruby’s Just-In-Time compiler. These enhancements are particularly beneficial for Arm architectures, as YJIT has been optimized to deliver better performance on such platforms. To leverage these improvements, it is recommended that you upgrade to Ruby 3.4.0 or later.
You can view [this release note](https://www.ruby-lang.org/en/news/2024/12/25/ruby-3-4-0-released/)

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Ruby version 3.4.0, the minimum recommended on the Arm platforms.
{{% /notice %}}

### Install Bundler
Bundler is Ruby’s dependency management tool. It ensures that all required gems (libraries) for your Rails application are installed and consistent across development, test, and production environments.

Install Bundler globally:

```console
gem install bundler
```
This command installs Bundler for the active Ruby version managed by rbenv.

### Install Rails
Rails is a full-stack web framework built in Ruby, designed for rapid development using convention over configuration principles.
Installing Rails on your SUSE Arm64 VM enables you to build and deploy web applications natively on Google Cloud Axion (C4A) processors.

```console
gem install rails
```

### Verify Rails version
Confirms that Rails is installed and accessible from your environment:

```console
rails -v
```
You should see output similar to:
```output
Rails 8.0.3
```

You have now installed Ruby and Rails on your Google Cloud C4A Arm-based VM. You can now proceed with the baseline testing.
