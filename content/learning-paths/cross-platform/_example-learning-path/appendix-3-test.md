---
# User change
title: "Test your code"

weight: 9 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Test Learning Paths

This repository provides a framework to help testing instructions, code snippets and maintain content.

The framework allows you to parse Learning Path articles and generate instructions to be run on a Docker container instance. It checks for expected behavior and stores results in Junit XML files. It creates one XML file for each section in a Learning Path.

1. [Install dependencies](#install-dependencies)
2. [Edit Learning Path pages](#edit-learning-path-pages)
3. [Edit metadata](#edit-metadata)
4. [Run the framework](#run-the-framework)
5. [Result summary](#result-summary)
6. [Visualize results](#visualize-results)


## Install dependencies

The framework is located in the `tools` folder. From the project root folder, install the Python dependencies with:

```console
pip install -r tools/requirements.txt
```

Docker is also required. Refer to the [Docker Engine install guide](http://localhost:1313/install-guides/docker/docker-engine/) to install Docker on Ubuntu.

## Edit Learning Path pages

### Bash

#### Test instructions

Bash instructions can be tested:

```markdown
    Let's test hello world:

    ```bash
    echo "hello world"
    ```

    Or a series or other commands:

    ```bash
    pwd
    echo "hello world"
    ```
```

The framework will check the return code. If not 0, an error will be reported.

#### Specify expected return code

If a specific return code is expected, it can be specified as follows:

```markdown
    The file myfile.txt doesn't exist yet and this command returns 1:

    ```bash { ret_code="1" }
    test -f myfile.txt
    ```
```

#### Command output

When a command output is displayed in the instructions:

```markdown
    Let's check is this command return the expected output:

    ```bash { command_line="root@localhost | 2 }
    echo "hello world"
    hello world
    ```
```

The framework will check if the command returns the same output and report an error otherwise.

#### Context between instruction blocks

The framework understands instructions in the Learning Path share some context, and as such they will be run in order in the same container instance. Files for examples can be created and reused afterwards in the Learning Path:

```markdown
    Let's create a file:

    ```bash
    echo "Hello world" > myfile.txt
    ```

    And check if it exists:

    ```bash
    test -f myfile.txt
    ```
```

It is important to note that the framework does run each code block as a separate terminal session. As such, environment variables do not persist and it assumes the current directory is $HOME. If the current directory needs change, you can specify it as follows:

```markdown
    Let's create a file in a folder:

    ```bash
    mkdir myfolder
    cd myfolder
    echo "Hello world" > myfile.txt
    ```

    This command will fail:

    ```bash { ret_code="1" }
    test -f myfile.txt
    ```

    This command will pass:

    ```bash { cwd="myfolder" }
    test -f myfile.txt
    ```
```

For a command block, it is possible to specify multiple environment variables separated by `;`:

```
    ```bash { env="VAR1=hello;VAR2=world" }
    echo $VAR1 $VAR2
    ```
```

To make environment variables persistent, it is possible to store them in the .bashrc and load them for the command block with `env_source`:

```
    ```bash { env_source="~/.bashrc" }
    env
    ```
```

If you want to manage the environment with a tool such as [environment modules](https://modules.sourceforge.net/) to load the environment, you can use `env_source` with `pre_cmd` which will silently run a command before instructions in the code block:

```
    ```bash { env_source="/usr/share/modules/init/bash", pre_cmd="module load gcc-12" }
    gcc-12 --version
    ```
```


#### Ignore instructions

```markdown
    This console output below will be ignored by the framework:

    ```console
    hello world
    ```
```

### Source code

Besides bash instructions, source code can also be tested.

```
    Here is some C code:

    ```C { file_name="hello.c" }
    #include <stdio.h>
    int main() {
    printf("Hello World\n");
    return 0;
    }
    ```

    Let's install GCC:

    ```
    sudo apt install -y gcc
    ```

    And compile the code with:

    ```bash
    gcc -o hello hello.c
    ```

    Run the executable with:

    ```bash
    ./hello
    ```
```

The C code snippet above will be copied over the container in a file named "hello.c". The other bash command allows to build and run it.

## Edit metadata

To allow the framework to parse and test the Learning Path instructions, edit the metadata in `_index.md` and add the following:

```yaml
test_maintenance: true
test_images:
- ubuntu:latest
- fedora:latest
```

The `test_maintenance` field is a boolean that enables the framework.

The `test_images` field is a list of Docker container images the framework can pull to test the Learning Path instructions. Check [Docker Hub](https://hub.docker.com/) to explore available images. 

## Run the framework

From the project root folder, run:

```bash
./tools/maintenance.py -i content/learning-paths/servers-and-cloud-computing/mynewlearningpath
```

If the Learning Path contains sub-articles, the framework will run their instructions in order, depending on the sub-articles weight.

Specify the `.md` file directly for single file tool install articles.

```bash
./tools/maintenance.py -i content/install-guides/mytool.md
```

## Result summary

The framework patches the metadata in the Learning Path's `_index.md` file or the .md file of the tool install to add a summary of the test status.

```yaml
test_maintenance: true
test_images:
- ubuntu:latest
- fedora:latest
test_status:
- passed
- failed
```

The field `test_status` is a list that indicated whether all tests passed for a corresponding Docker container image or if at least one test failed. 

In the example above, the summary indicates that for this Learning Path all tests passed for the image `ubuntu:latest` but at least one test failed for the image `fedora:latest`. More information about the failures are stored in Junit XML files.

## Visualize results

Test results are stored in XML Junit files. One XML file is created by Learning Path sub-article.

It is possible to visualize the results in a web browser. The XML files can be converted with [xunit-viewer](https://www.npmjs.com/package/xunit-viewer). 

If not already installed, install [Node.js](https://nodejs.org/en/) and run:

```
npm i -g xunit-viewer
```

Then, launch the web server (e.g. on port 5050) on the folder where the XML Junit files have been created:

```
xunit-viewer -r content/learning-paths/servers-and-cloud-computing/mynewlearningpath/ -s -p 5050
```

## Advanced usage for embedded development
#### Using the Corstone-300 FVP

By default, the framework runs instructions on the Docker images specified by the [metadata](#edit-metadata). For embedded development, it is possible to build software in a container instance and then check its behaviour on the Corstone-300 FVP. 

For this, all container instances used by the test framework mount a volume in `/shared`. This is where software for the target FVP can be stored. To check the execution, the FVP commands just need to be identified as a `fvp` section for the framework. 

For example:

```markdown
    We have previously built software for Corstone-300 in /shared/trusted-firmware-m/cmake_build/bin. To run the software on the FVP:

    ```fvp { fvp_name="FVP_Corstone_SSE-300_Ethos-U55"; cwd="/shared/trusted-firmware-m/cmake_build" }
    FVP_Corstone_SSE-300_Ethos-U55 -a cpu0*="bin/bl2.axf" --data "bin/tfm_s_ns_signed.bin"@0x01000000
    ```
```

The `fvp_name` allows to specify the FVP to run on. Currently, only `FVP_Corstone_SSE-300_Ethos-U55` and `FVP_Corstone_SSE-300_Ethos-U65` are supported.

