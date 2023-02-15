---
# User change
title: "2e) How to test your code (optional)"

weight: 9 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Test Learning Paths

This repository provides a framework to help testing instructions, code snippets and maintain content.

The framework allows to parse Learning Path articles and generate instructions to be run on a Docker container instance. It checks for expected behaviour and stores results in Junit XML files. It creates one XML file by Learning Path sub-article.

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

Docker is also required. Check the instructions [here](https://docs.docker.com/engine/install/ubuntu/) to install Doker on Ubuntu.

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

The framework will check the return code. If different than 0, an error will be reported.

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

The framework will check if the command return the same output and report an error otherwise.

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

But the framework does run each code block as a separate terminal session. As such, environment variables don't persist and it assumes the current directory is $HOME. If the current directory needs to be changed, it can be specified as follows:

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

If you want to manage the environement with a tool such as [environment modules](https://modules.sourceforge.net/) to load the enviroment, you can couple `env_source` with `pre_cmd` which will silently run a command before instructions in the code block:

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
./tools/maintenance.py -i content/learning-paths/server-and-cloud/mynewlearningpath
```

If the Learning Path contains sub-articles, the framework will run their instructions in order, depending on the sub-articles weight.

Specify the `.md` file directly for single file tool install articles.

```bash
./tools/maintenance.py -i content/install-tools/mytool.md
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

In the example above, the summary indicates that for this learning path all tests passed for the image `ubuntu:latest` but at least one test failed for the image `fedora:latest`. More information about the failures are stored in Junit XML files.

## Visualize results

Test results are stored in XML Junit files. One XML file is created by Learning Path sub-article.

It is possible to visualize the results in a web browser. The XML files can be converted with [xunit-viewer](https://www.npmjs.com/package/xunit-viewer). 

If not already installed, install nodejs and:

```
npm i -g xunit-viewer
```

Then, launch the web server (e.g. on port 5050) on the folder where the XML Junit files have been created:

```
xunit-viewer -r content/learning-paths/server-and-cloud/mynewlearningpath/ -s -p 5050
```


