---
title: Website
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
In this section you will create the files for the static website.

### index.html
Start by creating a subfolder for the website. Make sure to create it under the folder, in which you created the serverless project( e.g. AwsServerlessDynamoDbLambdaS3).

Then, in the website folder create `index.html` and modify it as follows:
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IoTPage</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Temperature Service</h1>
        <button id="writeTemperatures">Write Temperatures</button>
        <button id="getAverageTemperature">Get Average Temperature</button>

        <div id="temperatureDisplay" class="display-box">Temperature will be displayed here</div>
    </div>
    <script src="index.js"></script>
</body>
</html>
```

This HTML code defines a simple web page titled **IoTPage** for interacting with the AWS Lambda Functions. The page includes a link to a stylesheet `styles.css` for styling the page, two buttons with IDs **writeTemperatures** and **getAverageTemperature** to allow users to interact with the temperature service. Also, the HTML includes a div with the ID `temperatureDisplay` serves as a placeholder to display the temperature results. Finally, the code includes an external JavaScript file `index.js` at the end of the body to add interactive functionality to the page.

### Styles
In the same folder as `index.html` create a `styles.css` file, and add the content below:

```CSS
body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f0f0f0;
    margin: 0;
}

.container {
    text-align: center;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 10px 0;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background-color: #45a049;
}

.display-box {
    margin-top: 20px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 4px;
    background-color: #fafafa;
}
```

The above file declares the same styles as used in this [Learning Path](/learning-paths/laptops-and-desktops/win_aws_iot_s3/).

### JavaScript
Finally, under the website folder add the `index.js` file, and add the content shown below:

```JavaScript
const writeTemperaturesButton = document.getElementById('writeTemperatures');
const getAverageTemperatureButton = document.getElementById('getAverageTemperature');

// Placeholders for endpoints
const writeTemperaturesUrl = 'WRITE_TEMPERATURES_URL';
const getAverageTemperatureUrl = 'GET_AVERAGE_TEMPERATURE_URL';

writeTemperaturesButton.addEventListener('click', async () => {
    try {
        const response = await fetch(writeTemperaturesUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const data = await response.json();
        alert(data.message);
    } catch (error) {
        console.error('Error writing temperatures:', error);
        alert('Failed to write temperatures.');
    }
});

getAverageTemperatureButton.addEventListener('click', async () => {
    try {
        const response = await fetch(getAverageTemperatureUrl);
        const data = await response.json();
        const temperature = data.averageTemperature.toFixed(2);
        document.getElementById('temperatureDisplay').innerText = `Average Temperature: ${temperature} °C`;
    } catch (error) {
        console.error('Error fetching average temperature:', error);
        alert('Failed to get average temperature.');
    }
});
```

This JavaScript code adds interactivity to a web page by enabling two buttons to trigger HTTP requests to specific API endpoints for managing temperature data. The code selects the two buttons from the HTML by their IDs: `writeTemperaturesButton` and `getAverageTemperatureButton``.

Two API endpoints, `writeTemperaturesUrl` and `getAverageTemperatureUrl`, are defined as placeholders for the actual API URLs that the buttons will call. These placeholders will be replaced by the actual values output by the Serverless Framework after the resource deployment.

The code then defines event listeners for the buttons:
 1. `writeTemperaturesButton` click event. When clicked, it sends a POST request to the writeTemperaturesUrl endpoint to write temperature data. If successful, it displays a message with the response data; if there’s an error, it logs the error and shows an alert.
 2. `getAverageTemperatureButton` click event. When clicked, it sends a GET request to the getAverageTemperatureUrl endpoint to retrieve the average temperature. If successful, it displays the average temperature in a specific div on the web page; if there’s an error, it logs the error and shows an alert.

This code interacts with a backend service (composed of AWS Lambda functions) to write new temperature data and fetch the average temperature, enhancing the functionality of the web page.

### prepare.js
You will now add the JavaScript code that reads the outputs of the Serverless Framework, and use them to replace the `writeTemperaturesUrl` and `getAverageTemperatureUrl` placeholders in the `index.js`.

To implement this functionality, create a new `prepare.js` file, and save it in the same folder as `serverless.yml`. Then, modify `prepare.js` as follows:
```JavaScript
import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

// Fetch Serverless outputs using the 'serverless info --verbose' command
const output = execSync('serverless info --verbose', { encoding: 'utf8' });

// Extract the required endpoints from the output
const writeTemperaturesRegex = /WriteTemperaturesEndpoint:\s*(https:\/\/[^\s]+)/;
const getAverageTemperatureRegex = /GetAverageTemperatureEndpoint:\s*(https:\/\/[^\s]+)/;

const writeTemperaturesMatch = output.match(writeTemperaturesRegex);
const getAverageTemperatureMatch = output.match(getAverageTemperatureRegex);

const writeTemperaturesEndpoint = writeTemperaturesMatch ? writeTemperaturesMatch[1] : 'https://your-api-id.execute-api.us-east-1.amazonaws.com/dev/write-temperatures';
const getAverageTemperatureEndpoint = getAverageTemperatureMatch ? getAverageTemperatureMatch[1] : 'https://your-api-id.execute-api.us-east-1.amazonaws.com/dev/get-average-temperature';

// Path to the index.html file
const indexJsFileName = 'index.js';
const filePath = path.join('website', indexJsFileName);

// Read the HTML file and replace the placeholders with the actual endpoint URLs
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(`Error reading ${indexJsFileName} file:`, err);
    return;
  }

  // Replace placeholders with actual endpoints
  const result = data
    .replace('WRITE_TEMPERATURES_URL', writeTemperaturesEndpoint)
    .replace('GET_AVERAGE_TEMPERATURE_URL', getAverageTemperatureEndpoint);

  // Write the updated content back to the file
  fs.writeFile(filePath, result, 'utf8', (err) => {
    if (err) {
      console.error(`Error writing  ${indexJsFileName} file:`, err);
      return;
    }
    console.log(`${indexJsFileName} updated with dynamic endpoints successfully.`);
  });
});
```

This script automates the process of dynamically inserting the correct API endpoints into the `index.js` file, which is essential for ensuring that the web application communicates correctly with the deployed backend services.

The code uses the following JavaScript modules:
 1. `fs` for file system operations.
 2. `path` for handling file paths.
 3. `execSync` from `child_process` to execute shell commands synchronously.

The code runs the `serverless info --verbose` command to retrieve deployment details (e.g., API endpoints) and stores the output in the output variable. Then, using regular expressions, it extracts the URLs for the `writeTemperatures` and `getAverageTemperature` API endpoints from the Serverless output. If the endpoints are not found, it assigns default placeholder URLs.

Subsequently, the code sets the path to `index.js` by joining the directory (website) with the file name `index.js`. Once this is done, the code reads the `index.js` file content and replaces the placeholder strings (WRITE_TEMPERATURES_URL and GET_AVERAGE_TEMPERATURE_URL) with the actual API endpoint URLs.

Finally, the code writes the updated content back to `index.js` and logs a success message if completed. If any errors occur during reading or writing, it logs the errors to the console.

### package.json
Finally, add the `package.json` file. Save it next to `serverless.yml`, and modify it as follows:

```JSON
{
  "name": "aws-serverless-dynamodb-lambda-s3",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "prepare": "node prepare.js"
  },
  "devDependencies": {
    "serverless-plugin-scripts": "^1.0.0",
    "serverless-s3-sync": "^3.0.0"
  }
}
```

This is the package file for a `Node.js` project that uses the Serverless Framework to deploy AWS resources, including DynamoDB, Lambda, and S3. The file specifies the name of the project (aws-serverless-dynamodb-lambda-s3), its version, and sets the type to module, which means the project uses ES module syntax (e.g., import and export).

The file then defines a script named prepare that runs `prepare.js` using Node.js to set up or configure resources before deployment (this script is used to dynamically update index.js).

Next, it lists the development dependencies required for the project:
* serverless-plugin-scripts - a Serverless plugin to run custom scripts during the deployment lifecycle.
* serverless-s3-sync - a Serverless plugin to synchronize local files with an S3 bucket during deployment.
