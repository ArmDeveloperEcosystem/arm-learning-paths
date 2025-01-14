---
title: Run the model on a Raspberry Pi 5
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---
This final section explains how to test the model by experimenting with different prompts and settings on the Raspberry Pi 5.

## Set up your Raspberry Pi 5

If you want to see how the LLM behaves in an embedded environment, you need a Raspberry Pi 5 running Raspberry Pi OS. 

Install Raspberry Pi OS using the [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html). There are numerous ways to prepare an SD card, but Raspberry Pi recommends [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on a Windows, Linux, or macOS computer with an SD card slot or SD card adapter.

Make sure to install the 64-bit version of Raspberry Pi OS.

The 8GB RAM Raspberry Pi 5 model is preferred for exploring an LLM.

## Collect the files into an archive

There are just a few files that you need to transfer to the Raspberry Pi 5. You can bundle them together and transfer them from the running container to the development machine, and then to the Raspberry Pi 5. 

You should still be in the container, in the `$HOME/executorch` directory. 

The commands below copy the needed files to a new directory. The model file is very large and takes time to copy.

Run the commands below to collect the files:

```bash
mkdir llama3-files
cp cmake-out/examples/models/llama2/llama_main ./llama3-files/llama_main
cp llama-models/models/llama3_1/Meta-Llama-3.1-8B/params.json ./llama3-files/params.json
cp llama-models/models/llama3_1/Meta-Llama-3.1-8B/tokenizer.model ./llama3-files/tokenizer.model
cp llama3_kv_sdpa_xnn_qe_4_32.pte ./llama3-files/llama3_kv_sdpa_xnn_qe_4_32.pte
cp ./cmake-out/examples/models/llama2/runner/libllama_runner.so ./llama3-files
cp ./cmake-out/lib/libextension_module.so ./llama3-files
```

Compress the files into an archive using the `tar` command:

```bash
tar czvf llama3-files.tar.gz ./llama3-files
```

Next, copy the compressed tar file out of the container to the development computer. This is done using the `docker cp` command from the development machine.

Open a new shell or terminal on the development machine where Docker is running the container. 

Find the `CONTAINER ID` for the running container:

```bash
docker ps
```

The output will display the container information:

```output
CONTAINER ID   IMAGE     COMMAND       CREATED       STATUS       PORTS     NAMES
88c34c899c8c   rpi-os    "/bin/bash"   7 hours ago   Up 7 hours             fervent_vaughan
```

Your `CONTAINER ID` will be different so substitute your value. 

Copy the compressed file out of the container:

```bash
docker cp 88c34c899c8c:/home/pi/executorch/llama3-files.tar.gz  .
```

## Transfer the archive to the Raspberry Pi 5

Now you can transfer the archive from the development machine to your Raspberry Pi 5. 

There are multiple ways to do this: via cloud storage services, with a USB thumb drive, or using SSH. Use any method that is convenient for you. 

For example, you can use `scp` running from a terminal in your Raspberry Pi 5 device as shown. Follow the same option as you did in the previous step.

```bash
scp llama3-files.tar.gz <pi-user>@<pi-ip>:~/
```

Substitute the username and the IP address of the Raspberry Pi 5. 

The file is very large so you can also consider using a USB drive.

## Run the model

Finally, log in to the Raspberry Pi 5 and run the model in a terminal using the same command as before.

Extract the file:

```bash
tar xvfz llama3-files.tar.gz 
```

Change to the new directory:

```bash
cd llama3-files
```

Run the Llama model:

```bash
LD_LIBRARY_PATH=. ./llama_main --model_path=llama3_kv_sdpa_xnn_qe_4_32.pte  --tokenizer_path=tokenizer.model --cpu_threads=4 \
--prompt="Write a python script that prints the first 15 numbers in the Fibonacci series. Annotate the script with comments explaining what the code does."
```

{{% notice Note %}}
The `llama_main` program uses dynamic linking, so you need to inform the dynamic linker to look for the 2 libraries in the current directory. 
{{% /notice %}}

From here, you can experiment with different prompts and command line options on your Raspberry Pi 5.

Make sure to exit your container and clean up any development resources you created. 