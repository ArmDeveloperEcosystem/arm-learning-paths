---
# User change
title: Enable AWS connectivity

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
A key requirement of any IoT device is connectivity. The example projects implement cloud connector code.

Here we shall enable AWS connectivity. See the [README.md](https://github.com/ARM-software/open-iot-sdk/blob/main/v8m/README.md#setting-up-aws-connectivity) for full details.

## Default build

Confirm that you can build and run the `keyword` example.
```console
./ats.sh build-n-run keyword
```
The results are output (alongside other data) in the terminal:
```output
ML_HEARD_ON
ML_HEARD_OFF
...
```
We can also send this output to an AWS [thing](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) using [MQTT](https://mqtt.org/).

## Set up your thing

Open your AWS console in your browser.

In the same AWS region where you created your Virtual Hardware instance, navigate to `IoT Core`.

### Create IoT policy {#policy}

An AWS IoT policy defines how your `thing` can be accessed.

Select `Manage` > `Security` > `Policies`.

Click `Create policy` and give it a meaningful name.

In the `Policy document` section, create 4 statements (use `Add new statement` button to add more) where:

* `Policy effect` = `Allow`

`Policy action` = one each of:
* `iot:Connect`
* `iot:Publish`
* `iot:Receive`
* `iot:Subscribe`

`Policy resource` will be unique to you, of the form:
* `arn:aws:iot:<region>:<account-id>:*`

Click `Create` to define the policy.

### Create an AWS thing {#thing}

Select `Manage` > `All devices` > `Things`, and click on `Create things`.

Select `Create a single thing` and give it a meaningful name. Click `Next` leaving all other options as default.

Select `Auto-generate a new certificate` and click `Next`.

Select the `Policy` created [above](#policy) and click `Create thing`.

When prompted, download the `device certificate` (`.crt`) and public and private `keys` (`.pem.key`) for your `thing`. Click `Done`.

### Observe MQTT data {#mqtt}

In your AWS console, click on your `thing`.
* Select the `Activity` tab and open `MQTT test client`.
* Subscribe to `thingname/ml/inference` (where `thingname` is the name given [above](#thing)).
    * You can subscribe to `#` as a catch-all wildcard if you prefer.
* Click `Edit` and enable `MQTT payload display` > `Display payloads as strings (more accurate)`. Click `Confirm`.

## Modify code with above credentials

The examples need to be encoded with the above credentials.

Return to your Virtual Hardware terminal.

Using your preferred text editor, modify these files as described.

### bsp/default_credentials/aws_clientcredential.h

Modify these macros with the unique values for your AWS thing.

```C
#define clientcredentialMQTT_BROKER_ENDPOINT         "endpointid.amazonaws.com"
```
where `endpointid.amazonaws.com` is unique to you, and is given in `IoT Core` > `Settings` > `Endpoint` on your AWS console.

```C
#define clientcredentialIOT_THING_NAME               "thingname"
```
where `thingname` is the `thing` created [above](#thing).

Save the file when done.

### bsp/default_credentials/aws_clientcredential_keys.h

Modify these macros with the unique values for your AWS thing.

```C
#define keyCLIENT_CERTIFICATE_PEM \
...
```
with the contents of the `.crt` certificate file downloaded [above](#thing). You will need to start and end each line of the certificate with quotations and escape commands:
```output
"-----BEGIN CERTIFICATE-----\n"\
"1234123412341234123412341234123412341234123412341234123412341234\n"\
"5678567856785678567856785678567856785678567856785678567856785678\n"\
...
"-----END CERTIFICATE-----"
```

Similarly add the public and private keys (`.pem.key`), modified as above.
```C
#define keyCLIENT_PRIVATE_KEY_PEM \
...
#define keyCLIENT_PUBLIC_KEY_PEM \
...
```
Save the file when done.

## Run with MQTT connectivity

Rebuild and run the `keyword` application.
```console
./ats.sh build-n-run keyword
```
The messages are shown in the terminal as well as in [MQTT test client](#mqtt).
```output
ML_HEARD_ON
109 27329 [ML_MQTT] [INFO] Publish to the MQTT topic <thingname>/ml/inference.
...
```
![keyword #center](Images/keyword.png)

## Repeat with speech example

Build and run the `speech` example.
```console
./ats.sh build-n-run speech
```
Observe the output on the terminal and your MQTT console.
```output
INFO - Complete recognition: turn down the temperature in the bedroom
134 14506 [ML_MQTT] [INFO] Publish to the MQTT topic <thingname>/ml/inference.
```
![speech #center](Images/speech.png)
