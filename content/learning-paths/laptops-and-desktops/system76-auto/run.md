---
# User change
title: "Run the Parsec demo"

weight: 7

layout: "learningpathall"
---

## Run the Parsec SSL demo

From the command line, start a Tmux session:

```console
tmux new-session -s arm-auto-solutions
```

Tmux makes it possible to connect to the output from multiple hardware subsystems in the reference design. 

To run the software stack on the FVP, run:

```console
cd  ~/arm-auto-solutions
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose"
```

This runs the entire software stack on a model of the hardware. 

Anytime during the process you can use Tmux to interact with the different subsystems using Ctrl+B then W to bring up a list of windows. Press the arrow keys to select a window. 

After the software boots, you should see a Linux login prompt: `fvp-rd-kronos login:`

Enter `root` for the login name. No password is required. 

Make sure the initialization process is complete by running:

```console
systemctl is-system-running --wait
```

If the output is `running`, continue to the next step. If not, rerun the command until the output is `running`.

On the primary compute, run the SSL server:

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

The SSL client runs in a standard Ubuntu 22.04 container and requests a web page from the SSL server. The client has been modified to use Parsec, making it more portable, and able to abstract the details of the hardware security services. 

Run the Parsec-enabled SSL client: 

```console
docker run  --rm -v /run/parsec/parsec.sock:/run/parsec/parsec.sock -v /usr/bin/ssl_client1:/usr/bin/ssl_client1 --network host docker.io/library/ubuntu:22.04 ssl_client1
```

The container will then download and run. The SSL client application named `ssl_client1` also starts running.

The client application requests a webpage from the SSL server and you should see this output:

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

You can shut down the simulated system by using the following command:

```console
shutdown now
```

This will return you to the command line.

Type `exit` to leave the Tmux session, and `exit` again to leave the Multipass virtual machine. 

To delete the Multipass VM, run the commands:

```console
multipass stop u20-32
multipass delete u20-32
multipass purge
```

You have run the Parsec example from the Arm Automotive Solutions Software Reference Stack.

There are many other example applications you can run. See the Further Reading section at the end of the Learning Path for more information.