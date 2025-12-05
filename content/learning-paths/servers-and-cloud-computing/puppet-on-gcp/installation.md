---
title: Install Puppet on a GCP VM
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your environment and install Puppet
This section walks you through installing Puppet on a Google Cloud Platform (GCP) SUSE Linux arm64 VM. You'll set up all required dependencies, build Ruby from source, and prepare the environment for Puppet automation.

## Install dependencies and Ruby
To get started, you'll install the required development tools and libraries, then build Ruby 3.1.4 from source. This approach prepares your environment for Puppet and helps prevent compatibility problems.

To install the necessary packages for Ruby use this command:

```console
sudo zypper install git curl gcc make patch libyaml-devel libffi-devel libopenssl-devel readline-devel zlib-devel gdbm-devel bzip2 bzip2-devel
```


{{% notice Note %}}If you see a version conflict for `ncurses-devel` during the `zypper` install, choose the option that allows downgrading `ncurses-devel` to the required version (usually "Solution 1"). Confirm the downgrade by entering "y" when prompted. This step can be confusing at first, but it's a common requirement for building Ruby from source on SUSE Linux.{{% /notice %}}

Next, install ruby:

```console
cd ~
sudo wget https://cache.ruby-lang.org/pub/ruby/3.1/ruby-3.1.4.tar.gz
sudo tar -xzf ruby-3.1.4.tar.gz
cd ruby-3.1.4
sudo ./configure
sudo make && sudo make install
```

## Verify Ruby
Check that Ruby is correctly installed and available in your system PATH:

```console
ruby -v   
which ruby
```
The expected output is:

```output
ruby 3.1.4p223 (2023-03-30 revision 957bb7cb81) [aarch64-linux]
/usr/local/bin/ruby
```

## Install Puppet dependencies
Install the core Puppet libraries to enable automation and configuration management on your Arm-based GCP VM.

First, download and extract the Puppet source code:

```console
cd ~
sudo wget https://github.com/puppetlabs/puppet/archive/refs/tags/8.10.0.tar.gz
sudo tar -xvf 8.10.0.tar.gz
cd ~/puppet-8.10.0
```

Next, install the required Ruby gems for Puppet:

```console
sudo /usr/local/bin/gem install semantic_puppet -v "~> 1.0"
sudo gem install facter -v "~> 4.0"
sudo gem install hiera
```

- `semantic_puppet` manages Puppet-specific versioning and module dependencies
- `facter` collects system information, such as operating system, IP address, and hardware details, for Puppet to use
- `hiera` separates configuration data from Puppet manifests, making your automation setup more flexible

These libraries ensure Puppet runs smoothly and can manage your Arm-based SUSE Linux VM effectively.

These libraries are required for Puppet to work correctly on your Arm-based GCP VM.



< notice Note %>Puppet version 8.8.1 introduces expanded support for Arm and AArch64 platforms. This release adds agent compatibility for AlmaLinux 9 (AARCH64), Rocky Linux 9 (AARCH64), and Ubuntu 24.04 (ARM). It works with Ruby 3.3 and fixes several agent and catalog issues. Security is improved with OpenSSL 3.0.14, addressing recent vulnerabilities (CVE-2024-4603 and CVE-2024-2511).</notice%>

For more information, see the [official Puppet release notes](https://help.puppet.com/osp/current/Content/PuppetCore/PuppetReleaseNotes/release_notes_puppet_x-8-8-1.htm).

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Puppet 8.8.1 as the minimum version for Arm platforms.
## Build and install the Puppet gem
The Puppet gem provides the core Puppet framework, including its CLI, manifest parser, and resource management engine.

Build and install the Puppet 8.10.0 package from source into your Ruby environment.

```console
sudo gem build puppet.gemspec
sudo /usr/local/bin/gem install puppet-8.10.0.gem
```

## Verify Puppet installation 
Confirm Puppet is successfully installed and ready to use on the system.

```console
puppet --version
```

Output:
```output
8.10.0
```
Puppet installation is complete. You can now go ahead with the baseline testing of Puppet in the next section.
