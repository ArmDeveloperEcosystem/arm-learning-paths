---
# User change
title: "Control Arm Virtual Hardware with API"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
In this section you will learn how to control Arm Virtual Hardware via the [AVH API](https://app.avh.arm.com/api/docs). This can be used stand-alone, or as part of your overall CI/CD workflow.

Applications to interface with the API can be written in JavaScript, Python, or C. This example uses JavaScript.

You shall extend the workflow from the previous section to automatically transmit the `chip-tool` commands.

## Set up API Token as GitHub secret

In either `Arm Virtual Hardware` browser, navigate to `Profile` > `API`.

Generate and copy your `API Token`. This is a unique key that enables remote access to your instance(s).

In the GitHub browser, go to your forked repository, and navigate to `Settings` > `Secrets` > `Actions`.

Create a `New repository secret`. Name the secret:
```console
API_TOKEN
```
Paste the above `API Token` as the secret value.

The secret name must be exactly `API_TOKEN`, as this is used by the workflow later.

## Modify the workflow

In the `lighting-app` instance console, edit the previously created workflow.
```console
cd ~/connectedhomeip
nano .github/workflows/cicd_demo.yml
```
**Append** this `job` to the file:
```yml
  chip_tool:
    needs: rebuild_lighting_app
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install Node
        uses: actions/setup-node@aa759c6c94d3800c55b8601f21ba4b2371704cb7

      - name: Install AVH API and Websocket
        run: npm install @arm-avh/avh-api websocket --save

      - name: Run script
        env:
          API_TOKEN: ${{ secrets.API_TOKEN }}
        run: node .github/workflows/chip_tool.js
```
Save and exit.

This job invokes the following `JavaScript` which will transmit the `on/off` commands to the `chip-tool` instance via the `Websocket` interface.

Create a script:
```console
nano .github/workflows/chip_tool.js
```
containing the below:
```js
const readline = require('readline')
const { ArmApi, ApiClient } = require('@arm-avh/avh-api');
const W3CWebSocket = require('websocket').w3cwebsocket;

const BearerAuth = ApiClient.instance.authentications['BearerAuth']
const api = new ArmApi()

function delay(time) {
	return new Promise(resolve => setTimeout(resolve, time));
}

async function main() {
	console.log('Logging in...');
	const apiToken = process.env.API_TOKEN
	const authInfo = await api.v1AuthLogin({ apiToken });
	BearerAuth.accessToken = authInfo.token
	
	console.log("Locate instance named chip-tool...");
	console.log("[User must edit JavaScript if instance has different name (or >10000 instances)]");
	let instances = await api.v1GetInstances()
	for(let i=0; i<10000; i++){
		var instance = instances[i];
		if (instance.name == "chip-tool") break;
	}
	
	console.log("Open Websocket...");
	let url = await api.v1GetInstanceConsole(instance.id);
	var mySocket = await new W3CWebSocket(url.url);
	
	mySocket.onopen = function() {
		console.log(`WebSocket open.`);};
	mySocket.onerror = function() {
		console.log('WebSocket Connection Error.')};

	// Log in - comment the lines below if user has already logged in using the UI console
	mySocket.send("pi\n");
	await delay(1000);
    mySocket.send("raspberry\n");
    await delay(1000);
	
	console.log("Wait 60s to ensure lighting-app is initialized...");
	await delay(60000);
	
	console.log("Turn light on...");
	mySocket.send("/home/pi/connectedhomeip/examples/chip-tool/out/debug/chip-tool onoff on 0x11 1\n");
	
	console.log("Wait 5 seconds...");
	await delay(5000);
	
	console.log("Turn light off...");
	mySocket.send("/home/pi/connectedhomeip/examples/chip-tool/out/debug/chip-tool onoff off 0x11 1\n");
	
	console.log("Wait 5 seconds...");
	await delay(5000);
	
	console.log("Turn light on again...");
	mySocket.send("/home/pi/connectedhomeip/examples/chip-tool/out/debug/chip-tool onoff on 0x11 1\n");
	
	console.log("Wait 5 seconds...");
	await delay(5000);
	
	console.log("Turn light off again...");
	mySocket.send("/home/pi/connectedhomeip/examples/chip-tool/out/debug/chip-tool onoff off 0x11 1\n");
	
	console.log("Wait 5 seconds...");
	await delay(5000);
	
	console.log('Closing WebSocket...');
	mySocket.close();
		mySocket.onclose = function() {
		console.log(`WebSocket closed.`);};
	mySocket.onerror = function() {
		console.log('WebSocket Error.')};
	
	return;
}

main().catch((err) => {
    console.error(err);
});
```
Note that the JavaScript refers to instance name `chip-tool`, and `API_TOKEN` secret. The `job` refers to the script `chip_tool.js`, as well as the `API_TOKEN` secret. If these were named differently, you will need to update the script(s) appropriately.

When all edits are complete, push the changes back to GitHub:
```console
cd ~/connectedhomeip
git add .
git commit -m "added chip-tool automation"
git push
```
You will again be prompted for your GitHub username and Personal Access Token (password).

A new run of the Action will be triggered.

## Follow progress in GitHub Actions

Navigate to the `Actions` tab of your GitHub repository, and open the current workflow to follow progress. Observe that there are now three `jobs`, with the jobs to run `lighting-app` and `chip-tool` executing in parallel. You can follow progress in GitHub Actions log, and observe `chip-tool` toggling `lighting-app` automatically. You will also see the commands appear in the `chip-tool` console.

Congratulations! You have entirely automated the process to build and test your applications.

## Next Steps

You have built up a rudimentary CI/CD environment to start `Matter` development. Through the powerful AVH API and workflow methodology of GitHub Actions and other similar technologies, it is possible to construct an intelligent and always available CI/CD scheme, instantiating (and terminating) Virtual Hardware targets as required for your unit tests in a highly scalable way.
