---
title: Environment Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Arm has developed a suite of [Neoverse Reference Designs](https://developer.arm.com/Tools%20and%20Software/Neoverse%20Reference%20Design) compute sub-systems.
They are supported by free-of-charge [Arm Ecosystem FVPs](https://developer.arm.com/downloads/-/arm-ecosystem-fvps), and complete [software stacks](https://gitlab.arm.com/infra-solutions) to illustrate how these systems boot to Linux.
This learning path is based on the `Neoverse N2` Reference Design (`RD-N2`).

## Before you begin

You can use either a AArch64 or x86_64 host machine running Ubuntu Linux 22.04. 64GB of free disk space and 32GB of RAM is minimum requirement to sync and build the platform software stack. 48GB of RAM is recommended.
Follow the instructions to setup your environment with the detailed steps in [Setup the Neoverse Reference Design software stack workspace](https://neoverse-reference-design.docs.arm.com/en/latest/platforms/common/setup-workspace.html).



### Install repository

You will start by obtaining the repo tool to simplify the checkout of source code that spans multiple repositories. Additional instructions are available [here](https://source.android.com/docs/setup/download#installing-repo).

### Repo tool

First, let's refresh the list of available packages and install repo.
```bash { command_line="ubuntu@ip-10-0-0-164:~/src | 3-49" }
sudo apt-get update
sudo apt-get install repo
Hit:1 http://eu-west-1.ec2.archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://eu-west-1.ec2.archive.ubuntu.com/ubuntu jammy-updates InRelease                                   
Hit:3 http://eu-west-1.ec2.archive.ubuntu.com/ubuntu jammy-backports InRelease                                 
Hit:4 https://ppa.launchpadcontent.net/ubuntu-toolchain-r/test/ubuntu jammy InRelease                          
Hit:5 http://security.ubuntu.com/ubuntu jammy-security InRelease           
Reading package lists... Done


Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libtinyxml2-9 libz3-4 python3-pygments
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  repo
0 upgraded, 1 newly installed, 0 to remove and 30 not upgraded.
Need to get 118 kB of archives.
After this operation, 371 kB of additional disk space will be used.
Get:1 http://eu-west-1.ec2.archive.ubuntu.com/ubuntu jammy/multiverse amd64 repo all 2.17.3-3 [118 kB]
Fetched 118 kB in 0s (1422 kB/s)
Selecting previously unselected package repo.
(Reading database ... 160164 files and directories currently installed.)
Preparing to unpack .../archives/repo_2.17.3-3_all.deb ...
Unpacking repo (2.17.3-3) ...
Setting up repo (2.17.3-3) ...
Processing triggers for man-db (2.10.2-1) ...
Scanning processes...                                                                                                                                                                                                                         
Scanning candidates...                                                                                                                                                                                                                        
Scanning linux images...                                                                                                                                                                                                                      

Restarting services...
Service restarts being deferred:
 /etc/needrestart/restart.d/dbus.service
 systemctl restart docker.service
 systemctl restart getty@tty1.service
 systemctl restart libvirtd.service
 systemctl restart networkd-dispatcher.service
 systemctl restart systemd-logind.service
 systemctl restart unattended-upgrades.service
 systemctl restart user@1000.service

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
```
Verify installation with:
```bash { command_line="ubuntu@ip-10-0-0-164:~/src | 2-9" }
repo version
<repo not installed>
repo launcher version 2.17
       (from /usr/bin/repo)
git 2.34.1
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
OS Linux 6.2.0-1009-aws (#9~22.04.3-Ubuntu SMP Tue Aug  1 21:11:51 UTC 2023)
CPU x86_64 (x86_64)
Bug reports: https://bugs.chromium.org/p/gerrit/issues/entry?template=Repo+tool+issue
```

### Fetch source code

Create a new directory into which you will download the source code and build the stack. Then obtain the manifest.

To obtain the manifest, choose a tag of the platform reference firmware. [RD-INFRA-2023.09.29](https://neoverse-reference-design.docs.arm.com/en/latest/releases/RD-INFRA-2023.09.29/release_note.html) is used here. See the [release notes](https://neoverse-reference-design.docs.arm.com/en/latest/releases/index.html) for more information.

Specify the platform you want the manifest for. In the [manifest repo](https://git.gitlab.arm.com/infra-solutions/reference-design/infra-refdesign-manifests) there are a number of available platforms. As per these [instructions](https://neoverse-reference-design.docs.arm.com/en/latest/platforms/common/setup-workspace.html#platform-manifest-names) select `pinned-rdn2.xml`

```bash { command_line="ubuntu@ip-10-0-0-164:~ | 4-17" }
mkdir rd-infra
cd rd-infra/
repo init -u https://git.gitlab.arm.com/infra-solutions/reference-design/infra-refdesign-manifests.git -m pinned-rdn2.xml -b refs/tags/RD-INFRA-2023.12.22
Downloading Repo source from https://gerrit.googlesource.com/git-repo

... A new version of repo (2.40) is available.
... New version is available at: /home/ubuntu/rd-infra/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.


Your identity is: Tomas Pilar <tom.pilar@arm.com>
If you want to change this, please re-run 'repo init' with --config-name

repo has been initialized in /home/ubuntu/rd-infra
```

Let's look at what the manifest that we configured contains
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra | 2-15" }
cat .repo/manifest.xml 
<?xml version="1.0" encoding="UTF-8"?>
<!--
DO NOT EDIT THIS FILE!  It is generated by repo and changes will be discarded.
If you want to use a different manifest, use `repo init -m <file>` instead.

If you want to customize your checkout by overriding manifest settings, use
the local_manifests/ directory instead.

For more information on repo manifests, check out:
https://gerrit.googlesource.com/git-repo/+/HEAD/docs/manifest-format.md
-->
<manifest>
  <include name="pinned-rdn2.xml" />
</manifest>
```

The `manifest.xml` file just points to `pinned-rdn2.xml` so let us examine that one
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra | 2-28" }
cat .repo/manifests/pinned-rdn2.xml 
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
  <remote fetch="https://git.gitlab.arm.com/infra-solutions/reference-design/" name="arm"/>
  <remote fetch="https://github.com/" name="github"/>
  <remote fetch="https://git.savannah.gnu.org" name="gnugit"/>
  <remote fetch="https://git.kernel.org" name="kernel"/>
  <remote fetch="https://git.trustedfirmware.org" name="tforg"/>

  <project remote="arm" name="platsw/scp-firmware" path="scp" revision="refs/tags/RD-INFRA-2023.12.22"/>
  <project remote="arm" name="platsw/trusted-firmware-a" path="tf-a" revision="refs/tags/RD-INFRA-2023.12.22"/>
  <project remote="arm" name="platsw/edk2" path="uefi/edk2" revision="refs/tags/RD-INFRA-2023.12.22"/>
  <project remote="arm" name="platsw/edk2-platforms" path="uefi/edk2/edk2-platforms" revision="refs/tags/RD-INFRA-2023.12.22"/>
  <project remote="arm" name="platsw/linux" path="linux" revision="refs/tags/RD-INFRA-2023.12.22"/>
  <project remote="arm" name="scripts/build-scripts" path="build-scripts" revision="refs/tags/RD-INFRA-2023.12.22"/>
  <project remote="arm" name="scripts/model-scripts" path="model-scripts" revision="refs/tags/RD-INFRA-2023.12.22"/>
  <project remote="arm" name="scripts/container-scripts" path="container-scripts" revision="refs/tags/RD-INFRA-2023.12.22"/>
  <project remote="arm" name="valsw/kvm-unit-tests" path="validation/sys-test/kvm-unit-tests" revision="refs/tags/RD-INFRA-2023.12.22"/>
  <project remote="arm" name="platsw/buildroot" path="buildroot" revision="refs/tags/RD-INFRA-2023.12.22"/>

  <project remote="tforg" name="TF-A/tf-a-tests.git" path="validation/comp-test/trusted-firmware-tf" revision="6f9e14a0e3a9e14051cf6235a49b06bae32823d9"/>
  <project remote="github" name="acpica/acpica" path="tools/acpica" revision="refs/tags/R06_28_23"/>
  <project remote="github" name="ARMmbed/mbedtls.git" path="mbedtls" revision="refs/tags/mbedtls-2.28.0"/>
  <project remote="github" name="mirror/busybox" path="busybox" revision="refs/tags/1_36_0"/>
  <project remote="gnugit" name="git/grub.git" path="grub" revision="refs/tags/grub-2.04"/>
  <project remote="kernel" name="pub/scm/linux/kernel/git/jejb/efitools" path="tools/efitools" revision="refs/tags/v1.9.2"/>
  <project remote="kernel" name="pub/scm/linux/kernel/git/will/kvmtool" path="kvmtool" revision="e17d182ad3f797f01947fc234d95c96c050c534b"/>
</manifest>
```

The manifest defines repositories of firmware sources, build and model scripts, and linux along with some tooling.

Fetch the sources with the `repo sync` command. This will take a few minutes to complete.
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra | 2-14" }
repo sync -c -j $(nproc) --fetch-submodules --force-sync --no-clone-bundle
... A new version of repo (2.40) is available.
... New version is available at: /home/ubuntu/rd-infra/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.

Fetching: 100% (17/17), done in 2m23.399s
Fetching: 100% (16/16), done in 26.300s
Fetching: 100% (8/8), done in 11.914s
Fetching: 100% (1/1), done in 0.592s
Updating files: 100% (79368/79368), done.testsUpdating files:  26% (21084/79368)
Checking out: 100% (42/42), done in 13.164s
repo sync has finished successfully.
```
Now we should have all the code.
### Docker setup

Use a `docker` container for the build to improve reliability and reduce dependency on the host OS setup. The reference firmware build system can function in host OS without a container, but this way we don't have to worry about host OS incompatibility in this workbook.

Install docker:
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra | 2-54" }
sudo apt-get install docker.io
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libtinyxml2-9 libz3-4 python3-pygments
Use 'sudo apt autoremove' to remove them.
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  docker.io
0 upgraded, 1 newly installed, 0 to remove and 30 not upgraded.
Need to get 28.9 MB of archives.
After this operation, 113 MB of additional disk space will be used.
Get:1 http://eu-west-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 docker.io amd64 24.0.5-0ubuntu1~22.04.1 [28.9 MB]
Fetched 28.9 MB in 0s (64.8 MB/s) 
Preconfiguring packages ...
Selecting previously unselected package docker.io.
(Reading database ... 160030 files and directories currently installed.)
Preparing to unpack .../docker.io_24.0.5-0ubuntu1~22.04.1_amd64.deb ...
Unpacking docker.io (24.0.5-0ubuntu1~22.04.1) ...
Setting up docker.io (24.0.5-0ubuntu1~22.04.1) ...
Job for docker.service failed because the control process exited with error code.
See "systemctl status docker.service" and "journalctl -xeu docker.service" for details.
invoke-rc.d: initscript docker, action "start" failed.
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: activating (auto-restart) (Result: exit-code) since Fri 2024-01-12 13:30:46 UTC; 3ms ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
    Process: 2169953 ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock (code=exited, status=1/FAILURE)
   Main PID: 2169953 (code=exited, status=1/FAILURE)
        CPU: 69ms
Processing triggers for man-db (2.10.2-1) ...
Scanning processes...                                                                                                                                                                                                                         
Scanning candidates...                                                                                                                                                                                                                        
Scanning linux images...                                                                                                                                                                                                                      

Restarting services...
Service restarts being deferred:
 /etc/needrestart/restart.d/dbus.service
 systemctl restart getty@tty1.service
 systemctl restart libvirtd.service
 systemctl restart networkd-dispatcher.service
 systemctl restart systemd-logind.service
 systemctl restart unattended-upgrades.service
 systemctl restart user@1000.service

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.

```
You must add your username to the docker group and re-login to be able to talk to the docker daemon. Instructions [here](https://docs.docker.com/engine/install/linux-postinstall/).

```bash { command_line="ubuntu@ip-10-0-0-164:~/src | 3" }
sudo groupadd docker
sudo usermod -aG docker $USER
logout
```

You may need to restart the docker service as well
`**ubuntu@ip-10-0-0-164**:**~**$ sudo service docker restart`

Then you can test your access
```bash { command_line="ubuntu@ip-10-0-0-164:~ | 2" }
docker image list
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
```
### Container setup
Set up a container to perform the build in. A container execution script is provided. See the help for more information.
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra | 3-17" }
cd container-scripts/
./container.sh -h
Usage: ./container.sh [OPTIONS] [COMMAND]

If no options are provided the script uses the default values
defined in the 'Defaults' section.

Available options are:
  -v  <path> absolute path to mount into the container;
  -f  <file> docker file name;
  -i  <name> docker image name;
  -o  overwrites a previous built image;
  -h  displays this help message and exits;

Available commands are:
  build  builds the docker image;
  run    runs the container in interactive mode;
```

Build the default configuration:
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra/container-scripts | 2-25" }
./container.sh build
Building docker image: rdinfra-builder ...
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  26.62kB
Step 1/26 : FROM ubuntu:jammy-20230624
jammy-20230624: Pulling from library/ubuntu
3153aa388d02: Pull complete 
Digest: sha256:0bced47fffa3361afa981854fcabcd4577cd43cebbb808cea2b1f33a3dd7f508
Status: Downloaded newer image for ubuntu:jammy-20230624
 ---> 5a81c4b8502e
Step 2/26 : ARG USER
 ---> Running in 7cd15e880e82
Removing intermediate container 7cd15e880e82
 ---> 2e728e239299
Step 3/26 : ARG UID
 ---> Running in 35dc732345d3
Removing intermediate container 35dc732345d3
 ---> e8c950c9068c
Step 4/26 : ARG GID
 ---> Running in a11903e99aa3
...
...
```

This proceeds with 2.1 MB (!!) of plain text output (full text attached) until the container build is finished:
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra/container-scripts | 2-14" }

...
...
 ---> f41782a8f1d8
Step 25/26 : ENV PATH="${PATH}:/home/$USER/.local/bin"
 ---> Running in 27394a03b9a8
Removing intermediate container 27394a03b9a8
 ---> 30e52c685e65
Step 26/26 : CMD ["/bin/bash"]
 ---> Running in 72103ad91f00
Removing intermediate container 72103ad91f00
 ---> 8729adb0b96c
Successfully built 8729adb0b96c
Successfully tagged rdinfra-builder:latest
```

Verify the container was built:
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra/container-scripts | 2-4" }
docker image list
REPOSITORY        TAG              IMAGE ID       CREATED         SIZE
rdinfra-builder   latest           8729adb0b96c   8 minutes ago   3.07GB
ubuntu            jammy-20230624   5a81c4b8502e   6 months ago    77.8MB
```

Looks like a standard ubuntu container based on the latest release with the rdinfra-builder container built on top of it. Let's enter the container and look around:
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra/container-scripts | 2-3" }
docker run -it rdinfra-builder:latest /bin/bash
ubuntu@923218f076f5:/$ ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

We exit the container like any login shell. We can also use the container script to check it out:
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra/container-scripts | 2" }
./container.sh run
Running docker image: rdinfra-builder ...
```

Mount the source checkout into the container so we can do a build without having to copy the source in and build the targets out:
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra/container-scripts | 3-4" }
./container.sh -v /home/ubuntu/rd-infra/ run
ls /home/ubuntu/rd-infra/
Running docker image: rdinfra-builder ...
buildroot  build-scripts  busybox  container-scripts  grub  kvmtool  linux  mbedtls  model-scripts  scp  tf-a  tools  uefi  validation
```

{{% notice Host based builds %}}
If you do choose to build this on the host, you need to get all the pre-requisites that would otherwise be installed in the container during its creation.

The build system provides a script for this that you must run as `root`:
```bash
sudo ./build-scripts/rdinfra/install_prerequisites.sh
```
{{% /notice %}}

