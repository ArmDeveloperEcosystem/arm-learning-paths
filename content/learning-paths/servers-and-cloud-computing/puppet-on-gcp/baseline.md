---
title: Puppet Baseline Testing on Google Axion C4A Arm Virtual Machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Puppet Baseline Testing on GCP SUSE VMs
In this guide, you will perform baseline testing of Puppet on a GCP SUSE Arm64 VM to verify that the installation works correctly. You will check Puppet and Facter versions, run basic Puppet commands, apply a simple manifest, and confirm that system facts are collected accurately.

### Verify Puppet Installation
Verify that Puppet and Facter are correctly installed and respond to version checks:

Version Check:
```console
puppet --version
```
Output:
```output
8.10.0
```
Version Check:
```console
facter --version
```
Output:
```output
4.10.0
```
Version Check:
```console
ruby -v
```
Output:
```output
ruby 3.1.4p223 (2023-03-30 revision 957bb7cb81) [aarch64-linux]
```

### Run a Simple Puppet Command
Check that Puppet responds to commands by running puppet help. If the help menu appears, Puppet is working correctly.

```console
puppet help
```

Output:

```console
Usage: puppet <subcommand> [options] <action> [options]

Available subcommands:

  Common:
    agent             The puppet agent daemon
    apply             Apply Puppet manifests locally
    config            Interact with Puppet's settings.
    help              Display Puppet help.
    lookup            Interactive Hiera lookup
    module            Creates, installs and searches for modules on the Puppet Forge.
    resource          The resource abstraction layer shell


  Specialized:
    catalog           Compile, save, view, and convert catalogs.
    describe          Display help about resource types
    device            Manage remote network devices
    doc               Generate Puppet references
    epp               Interact directly with the EPP template parser/renderer.
    facts             Retrieve and store facts.
    filebucket        Store and retrieve files in a filebucket
    generate          Generates Puppet code from Ruby definitions.
    node              View and manage node definitions.
    parser            Interact directly with the parser.
    plugin            Interact with the Puppet plugin system.
    script            Run a puppet manifests as a script without compiling a catalog
    ssl               Manage SSL keys and certificates for puppet SSL clients

See 'puppet help <subcommand> <action>' for help on a specific subcommand action.
See 'puppet help <subcommand>' for help on a specific subcommand.
Puppet v8.10.0
```

### Test a Simple Puppet Manifest
Create and run a basic Puppet script to make sure Puppet can apply configurations. If it successfully creates the test file, your Puppet agent functions as expected.

```bash
cd ~
cat <<EOF > test.pp
file { '/tmp/puppet_test.txt':
  ensure  => file,
  content => "Hello from Puppet on SUSE ARM64!\n",
}
EOF
```
```console
puppet apply test.pp
```

You should see an output similar to:
```output
Notice: Compiled catalog for danson-puppet-2.c.arm-deveco-stedvsl-prd.internal in environment production in 0.01 seconds
Notice: /Stage[main]/Main/File[/tmp/puppet_test.txt]/ensure: defined content as '{sha256}bcf972b61979afe69626549b3f3f30798aeb50b359e76603a36e96b2abbe73c0'
Notice: Applied catalog in 0.01 seconds
```

**Then verify:**

Open the file created by Puppet to confirm the content matches your script. This step validates that Puppet executed your manifest correctly.

```console
cat /tmp/puppet_test.txt
```

Output:
```output
Hello from Puppet on SUSE ARM64!
```

### Check Facter Integration
Run `facter` commands to verify that it collects accurate system details like OS and CPU type. This ensures Puppet can gather the facts it needs for automation decisions.

OS Check:
```console
facter os
```
Output:
```output
{
  architecture => "aarch64",
  distro => {
    codename => "n/a",
    description => "SUSE Linux Enterprise Server 15 SP6",
    id => "SUSE",
    release => {
      full => "15.6",
      major => "15",
      minor => "6"
    }
  },
  family => "Suse",
  hardware => "aarch64",
  name => "SLES",
  release => {
    full => "15.6",
    major => "15",
    minor => "6"
  },
  selinux => {
    enabled => false
  }
}
```
Architecture Check:
```console
facter architecture
```
Output:
```output
aarch64
```
Processors Check:
```console
facter processors
```
Output:
```output
{
  cores => 4,
  count => 4,
  extensions => [
    "aarch64"
  ],
  isa => "aarch64",
  models => [

  ],
  physicalcount => 1,
  threads => 1
}
```
With these checks complete, proceed to the Puppet benchmarking section to run workload‑focused tests on the GCP SUSE VMs.
