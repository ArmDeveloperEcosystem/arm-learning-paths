---
# User change
title: "Run the Parsec demo"

weight: 4

layout: "learningpathall"
---


There are a number of example applications which demonstrate the software stack running the reference hardware system modeled by a Fixed Virtual Platform (FVP). The Parsec demo is explained below. 

The [Parsec-enabled TLS demo](https://arm-auto-solutions.docs.arm.com/en/v1.1/design/applications/parsec_enabled_tls.html) illustrates a HTTPS session. A simple web page is transferred using a Transport Layer Security (TLS) connection.

Parsec, or Platform AbstRaction for SECurity, is an open-source initiative that provides a common API to hardware security and cryptographic services.

This enables applications to interact with the secure hardware of a device without needing to know the specific details of the hardware itself. The Parsec abstraction layer makes it easier to develop secure applications that can run on different devices and platforms.   

Follow the instructions below to run the Parsec demo.

## Run the Parsec SSL demo

From the command line, start a Tmux session.

```console
tmux new-session -s arm-auto-solutions
```

Tmux makes it possible to connect to the output from multiple hardware subsystems in the reference design. 

To run the software stack on the FVP run:

```console
cd  ~/arm-auto-solutions
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose"
```

This will run the entire software stack on a model of the hardware. 

At anytime you can use Tmux to interact with the different subsystems using `Ctrl-b` then `w` to bring up a list of windows. Use the arrow keys to select a window. 

After the software boots, you reach a Linux login prompt: `fvp-rd-kronos login:`

Enter `root` for the login name, no password is required. 

Make sure the initialization process is complete by running:

```console
systemctl is-system-running --wait
```

If the output is `running`, continue to the next step. If not, re-run the command until the output is `running`.

On the primary compute run the SSL server:

```console
ssl_server &
```

The output from the server is printed:

```output
  . Seeding the random number generator... ok
  . Loading the server cert. and key... ok
  . Bind on https://localhost:4433/ ... ok
  . Setting up the SSL data.... ok
  . Waiting for a remote connection ...
```

The SSL client runs in a standard Ubuntu 22.04 container and requests a web page from the SSL server. The client has been modified to use Parsec, making it more portable and abstracting the details of the hardware security services. 

Run the Parsec enabled SSL client: 

```console
docker run  --rm -v /run/parsec/parsec.sock:/run/parsec/parsec.sock -v /usr/bin/ssl_client1:/usr/bin/ssl_client1 --network host docker.io/library/ubuntu:22.04 ssl_client1
```

The container will be downloaded and run. The SSL client application named `ssl_client1` runs.

The client application requests a webpage from the SSL server and the output is:

```output
  . Seeding the random number generator... ok
  . Loading the CA root certificate ... ok (0 skipped)
  . Connecting to tcp/localhost/4433... ok
  . Performing the SSL/TLS handshake... ok
  . Setting up the SSL/TLS structure... ok
  . Performing the SSL/TLS handshake... ok
  < Read from client: 18 bytes read

GET / HTTP/1.0

  > Write to client: ok
  . Verifying peer X.509 certificate... ok
  > Write to server: 156 bytes written

HTTP/1.0 200 OK
Content-Type: text/html

<h2>Mbed TLS Test Server</h2>
<p>Successful connection using: TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256</p>

  . Closing the connection... ok
  . Waiting for a remote connection ... 18 bytes written

GET / HTTP/1.0

  < Read from server: 156 bytes read

HTTP/1.0 200 OK
Content-Type: text/html

<h2>Mbed TLS Test Server</h2>
<p>Successful connection using: TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256</p>
```

## Shutdown and clean up

You can shut down the simulated system:

```console
shutdown now
```

You will return to the command line.

Type `exit` to leave the Tmux session and `exit` again to leave the Multipass virtual machine. 

To delete the Multipass VM run the commands:

```console
multipass stop u20-32
multipass delete u20-32
multipass purge
```

You have run the Parsec example from the Arm Automotive Solutions Software Reference Stack.

There are many other example applications you can run, refer to the Further Reading section.