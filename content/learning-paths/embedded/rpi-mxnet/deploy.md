 ---
# User change
title: "Install on Raspberry Pi"

weight: 4

layout: "learningpathall"

---


## Copy the image to your local machine

If you are working on an Arm cloud instance or remote server, download the new Raspberry Pi image with the compiled MXNet to your local machine using `scp`

Use the IP address of your Arm server and the name of your SSH key in the command below to download the image:

```console
scp -i <your-key.pem> ubuntu@<your-ip-addr>:~/2023-02-21-raspios-bullseye-arm64-lite.img .
```

## Write an SD card 

Write the image to an SD card and insert it into your Raspberry Pi. Refer to the [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html) for more information about how to write the image to an SD card. There are numerous ways to prepare an SD card, but Raspberry Pi Imager is recommended from a Windows, Linux, or macOS computer with an SD card slot or SD card adapter.

The first boot will resize the file system based on the size of the SD card you are using. 

You will also be prompted to change the default user from `pi` to a new name you select. 

Log in to the Raspberry Pi using the new user name and password. 

## Test MXNet

Because the user name was changed, the last step of the MXNet install must be run again. 

```console
cd incubator-mxnet/python/
sudo pip3 install -e . 
```

Confirm MXNet loads on the Raspberry Pi using the same commands used on the Arm server. 

Using a text editor copy and paste the code below into a text file named `test.py`

```console
import mxnet
print(mxnet.__version__)
```

Run the example code:

```console
python3 ./test.py
```

The version of MXNet should be printed. 

The expected output format is below. Your version may be slightly different. 

```output
2.0.0
```

You have significantly reduced MXNet compile time, transferred the result to an SD card, and confirmed MXNet can immediately run on a Raspberry Pi. 