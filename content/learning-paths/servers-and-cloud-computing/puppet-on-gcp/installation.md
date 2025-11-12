---
title: Install Puppet
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Puppet on GCP VM
This guide walks you through installing Puppet on a **Google Cloud Platform (GCP) SUSE Linux Arm64 VM**, including all dependencies, Ruby setup, and environment preparation.

### Install build dependencies and Ruby from source
Installs all required tools and builds Ruby 3.1.4 from source to ensure compatibility with Puppet.

```console
sudo zypper install -y gcc make openssl-devel libyaml-devel zlib-devel readline-devel gdbm-devel ncurses-devel
cd /usr/local/src
sudo wget https://cache.ruby-lang.org/pub/ruby/3.1/ruby-3.1.4.tar.gz
sudo tar -xzf ruby-3.1.4.tar.gz
cd ruby-3.1.4
sudo ./configure
sudo make && sudo make install
```

### Verify Ruby
Checks that Ruby is correctly installed and available in your system path.

```console
ruby -v   
which ruby
```

```output
ruby 3.1.4p223 (2023-03-30 revision 957bb7cb81) [aarch64-linux]
/usr/local/bin/ruby
```

### Install Puppet dependencies
Installs essential Puppet libraries (`semantic_puppet, facter, hiera`) needed for automation tasks.

- **semantic_puppet** – Provides tools for handling Puppet-specific versioning, modules, and dependency constraints.
- **facter** – Collects system information (facts) such as OS, IP, and hardware details for Puppet to use in configuration decisions.
- **hiera** – Key-value lookup tool that manages configuration data outside of Puppet manifests for flexible data separation.

```console
wget https://github.com/puppetlabs/puppet/archive/refs/tags/8.10.0.tar.gz
tar -xvf 8.10.0.tar.gz
cd ~/puppet-8.10.0
sudo /usr/local/bin/gem install semantic_puppet -v "~> 1.0"
sudo gem install facter -v "~> 4.0"
sudo gem install hiera
```

{{% notice Note %}}
Puppet 8.8.1 version expands official support for Arm and AArch64, with new agent compatibility for AlmaLinux 9 (AARCH64), Rocky Linux 9 (AARCH64), and Ubuntu 24.04 (ARM). The release ensures compatibility with Ruby 3.3 and resolves multiple agent and catalog-related issues. Security is enhanced with an OpenSSL 3.0.14 upgrade, addressing CVE-2024-4603 and CVE-2024-2511 vulnerabilities.
You can view [this release note](https://help.puppet.com/osp/current/Content/PuppetCore/PuppetReleaseNotes/release_notes_puppet_x-8-8-1.htm)

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Puppet version 8.8.1, the minimum recommended on the Arm platforms.
{{% /notice %}}

### Build and install the Puppet gem
The **Puppet gem** provides the core Puppet framework, including its CLI, manifest parser, and resource management engine.

Build and install the Puppet 8.10.0 package from source into your Ruby environment.

```console
sudo gem build puppet.gemspec
sudo /usr/local/bin/gem install puppet-8.10.0.gem
```

### Verification
Confirm Puppet is successfully installed and ready to use on the system.

```console
puppet --version
```

Output:
```output
8.10.0
```
Puppet installation is complete. You can now go ahead with the baseline testing of Puppet in the next section.
