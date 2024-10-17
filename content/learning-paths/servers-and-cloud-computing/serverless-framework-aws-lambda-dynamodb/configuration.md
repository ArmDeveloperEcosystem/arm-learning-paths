---
title: Service declaration
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Service Declaration
In this section, you will declare the serverless service composed of the following AWS resources:  
	1. DynamoDB Table: This will store hypothetical sensor data, including timestamps and randomly generated temperatures.  
	2. Two AWS Lambda Functions: The first function will write temperatures to the DynamoDB table, and the second will retrieve the average temperature value.  
	3. IAM Role: A set of permissions that enable the AWS Lambda functions to write and read data from the DynamoDB table.  

### Declare a service
To create a new serverless service, open the command prompt or terminal and type the following:

```console
serverless
```

In the wizard that appears, proceed as follows:
1.	Select the **AWS / Node.js / Simple Function** template.
2.	In the *Name Your Project field*, type **AwsServerlessDynamoDbLambda**.
3.	In the *Please login/register* or enter your license key section, select **Login/Register** and sign in to the Serverless Framework.
4.	In the *Create Or Select An Existing App section*, select **Skip Adding An App**.

The tool will generate the project composed of the following files:
1.	`serverless.yml` - this contains the declaration of the infrastructure and services for a serverless application.
2.	`handler.js` - you use this file to implement the core functionality of your serverless application, handling business logic and interactions with other services. Here, you will use this file to implement Lambda functions.

### serverless.yml
To define the AWS resources, open `serverless.yml` and modify it as follows:
```YAML
org: <KEEP_YOUR_ORG_NAME>

service: AwsServerlessDynamoDbLambda

provider:
  name: aws
  runtime: nodejs20.x
  region: us-east-1
  stage: dev
  environment:
    DYNAMODB_TABLE: SensorReadings
  iam:
    role:
      statements:
        - Effect: Allow
          Action:
            - dynamodb:BatchWriteItem
            - dynamodb:PutItem
            - dynamodb:UpdateItem
            - dynamodb:GetItem
            - dynamodb:Scan
            - dynamodb:Query
          Resource:
            - arn:aws:dynamodb:${self:provider.region}:*:table/${self:provider.environment.DYNAMODB_TABLE}

functions:
  writeTemperatures:
    handler: handler.writeTemperatures
    events:
      - http:
          path: write-temperatures
          method: post

  getAverageTemperature:
    handler: handler.getAverageTemperature
    events:
      - http:
          path: get-average-temperature
          method: get

resources:
  Resources:
    SensorReadingsTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: ${self:provider.environment.DYNAMODB_TABLE}
        AttributeDefinitions:
          - AttributeName: id
            AttributeType: S
          - AttributeName: timestamp
            AttributeType: N
        KeySchema:
          - AttributeName: id
            KeyType: HASH
          - AttributeName: timestamp
            KeyType: RANGE
        ProvisionedThroughput:
          ReadCapacityUnits: 1
          WriteCapacityUnits: 1
  Outputs:
    WriteTemperaturesEndpoint:
      Description: "Endpoint for the writeTemperatures function"
      Value:
        Fn::Join:
          - ""
          - - "https://"
            - Ref: "ApiGatewayRestApi"
            - ".execute-api.${self:provider.region}.amazonaws.com/${self:provider.stage}/write-temperatures"
    GetAverageTemperatureEndpoint:
      Description: "Endpoint for the getAverageTemperature function"
      Value:
        Fn::Join:
          - ""
          - - "https://"
            - Ref: "ApiGatewayRestApi"
            - ".execute-api.${self:provider.region}.amazonaws.com/${self:provider.stage}/get-average-temperature"
```

The first section of the above file includes the following: 
* org: <KEEP_YOUR_ORG_NAME> - this specifies the organization name in the Serverless Framework’s dashboard.
* service: AwsServerlessDynamoDbLambda - defines the name of the service. This name is used to organize and identify the resources created by this Serverless service.

In the Serverless Framework a service is the fundamental unit of organization. It represents a single project or application and encapsulates all the functions, resources, and configurations necessary to deploy and manage that project in a serverless environment. A service can consist of multiple functions, each with its own triggers and configuration, and can define the necessary cloud resources such as databases, storage, and other infrastructure components.

After the service definition, there is the provider section which specifies the cloud provider (e.g., AWS) and general settings such as runtime, region, and environment variables. Here, the provider section contains the following:
* name: aws - this specifies that the provider is AWS.
* runtime: nodejs20.x - sets the runtime environment for the Lambda functions to Node.js 20.x.
* region: us-east-1 - defines the AWS region where the service will be deployed.
* stage: dev - sets the deployment stage to dev.

Next, you have the environment section which includes one item:
* DYNAMODB_TABLE: SensorReadings. This defines an environment variable DYNAMODB_TABLE with the value SensorReadings which will be used to name the DynamoDB table.

In the IAM section you define one role. This role specifies a list of actions that are allowed (dynamodb:BatchWriteItem, dynamodb:PutItem, dynamodb:UpdateItem, dynamodb:GetItem, dynamodb:Scan, dynamodb:Query) on a given resource. The resource is specified using Amazon Resource Name (ARN). 

ARN is a unique identifier used to identify resources in AWS. ARNs are used throughout AWS to uniquely identify resources such as EC2 instances, S3 buckets, DynamoDB tables, Lambda functions, IAM roles, and more. 

Here, you use ARN to identify the DynamoDB table that role actions are allowed on, using the ${self:provider.region} and ${self:provider.environment.DYNAMODB_TABLE} variables to dynamically insert the region and table name.

The `serverless.yml` defines two AWS Lambda functions:
1. writeTemperatures. Its handler is set to handler.writeTemperatures. This function will be triggered through the HTTP POST event.
2. getAverageTemperature with handler.getAverageTemperature handler. This function will be triggered through the GET POST event.

In the resources section you define a DynamoDB table resource with the following attributes id as a string and timestamp as a number. Additionally, set the read and write capacity units to 1 each (provisioned throughput).

Finally, the outputs section is used to display the endpoints of both Lambda functions. You will use those endpoints to trigger AWS Lambda functions.

### handler.js
You will now implement the two AWS Lambda functions. Open the `handler.js`, and replace its contents with the following code:

```JavaScript
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, BatchWriteCommand, ScanCommand  } from '@aws-sdk/lib-dynamodb';

const client = new DynamoDBClient({ region: "us-east-1" });
const dynamoDb = DynamoDBDocumentClient.from(client);
const tableName = process.env.DYNAMODB_TABLE;

// Function to write random temperature records
export const writeTemperatures = async (event) => {
  const records = [];
  const N = 20;
  for (let i = 0; i < N; i++) {
    const record = {
      id: `temp-${Date.now()}-${i}`,
      timestamp: Date.now(),
      temperature: (Math.random() * 30) + 20, // Random fractional temperature between 20 and 50
    };
    records.push({
      PutRequest: {
        Item: record,
      },
    });
  }

  const params = {
    RequestItems: {
      [tableName]: records,
    },
  };

  try {
    await dynamoDb.send(new BatchWriteCommand(params));
    return {
      statusCode: 200,
      body: JSON.stringify({
        message: 'Temperature records written successfully!',
      }),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({
        message: 'Failed to write temperature records',
        error: error.message,
      }),
    };
  }
};

// Function to retrieve last N temperature records, average them, and return the result
export const getAverageTemperature = async (event) => {
  const N = 10;

  const params = {
    TableName: tableName,
    Limit: N,
    ScanIndexForward: false    
  };

  try {
    const data = await dynamoDb.send(new ScanCommand(params));
    const temperatures = data.Items.map(item => item.temperature);
    const averageTemperature = temperatures.reduce((sum, value) => sum + value, 0) / temperatures.length;

    return {
      statusCode: 200,
      body: JSON.stringify({
        averageTemperature,
      }),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({
        message: 'Failed to retrieve temperature records',
        error: error.message,
      }),
    };
  }
};
```

The code defines the two AWS Lambda functions that interact with a DynamoDB table:
	1.	writeTemperatures - writes a batch of random temperature records to the DynamoDB table.
	2.	getAverageTemperature - retrieves the last N temperature records from the table, calculates the average, and returns it.

The first section of the code (see below):
```JavaScript
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, BatchWriteCommand, ScanCommand } from '@aws-sdk/lib-dynamodb';
```
imports the following components: 
* DynamoDBClient and DynamoDBDocumentClient: these are used to interact with DynamoDB. The DynamoDBClient is the base client for AWS SDK operations, while DynamoDBDocumentClient provides a higher-level abstraction for working with documents in DynamoDB.
* BatchWriteCommand and ScanCommand: these are commands used to perform batch writes and scans on DynamoDB tables.

After this, you have the following statements:
```JavaScript
const client = new DynamoDBClient({ region: "us-east-1" });
const dynamoDb = DynamoDBDocumentClient.from(client);
const tableName = process.env.DYNAMODB_TABLE;
```

These statements initialize a new DynamoDBClient targeting the us-east-1 AWS region, create a DynamoDBDocumentClient from the base DynamoDBClient to work with DynamoDB documents. The final statement fetches the table name from the environment variable DYNAMODB_TABLE. This variable is set automatically by the Serverless Framework when you deploy the resources (it comes from the serverless.yml)

Next, there is a definition of the `writeTemperatures` function: 
```JavaScript
export const writeTemperatures = async (event) => {
  const records = [];
  const N = 20;
  for (let i = 0; i < N; i++) {
    const record = {
      id: `temp-${Date.now()}-${i}`,
      timestamp: Date.now(),
      temperature: (Math.random() * 30) + 20, // Random fractional temperature between 20 and 50
    };
    records.push({
      PutRequest: {
        Item: record,
      },
    });
  }

  const params = {
    RequestItems: {
      [tableName]: records,
    },
  };

  try {
    await dynamoDb.send(new BatchWriteCommand(params));
    return {
      statusCode: 200,
      body: JSON.stringify({
        message: 'Temperature records written successfully!',
      }),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({
        message: 'Failed to write temperature records',
        error: error.message,
      }),
    };
  }
};
```

The purpose of the above function is to write 20 random temperature records (in a range of 20-50 degree Celsius) to the DynamoDB table. To do this, the function uses a loop to create 20 records with the following:
* id - a unique identifier combining the current timestamp and loop index.
* timestamp - the current time in milliseconds.
* temperature - a random fractional value between 20 and 50.

Then, the function uses `BatchWriteCommand` to send the records to the table. Also it catches and returns errors with an appropriate HTTP status code.

The second function, `getAverageTemperature`, is defined as follows:
```JavaScript
export const getAverageTemperature = async (event) => {
  const N = 10;

  const params = {
    TableName: tableName,
    Limit: N,
    ScanIndexForward: false    
  };

  try {
    const data = await dynamoDb.send(new ScanCommand(params));
    const temperatures = data.Items.map(item => item.temperature);
    const averageTemperature = temperatures.reduce((sum, value) => sum + value, 0) / temperatures.length;

    return {
      statusCode: 200,
      body: JSON.stringify({
        averageTemperature,
      }),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({
        message: 'Failed to retrieve temperature records',
        error: error.message,
      }),
    };
  }
};
```
The `getAverageFunction` retrieves the last 10 temperature records and calculates their average. To do this, the function uses the `ScanCommand` to fetch items from the table, limiting it to 10 records. The retrieved records are mapped to extract temperatures and then the function calculates the average using the reduce JavaScript function. The `getAverageTemperature` returns the average temperature in the response body. 

The above code demonstrates a common pattern in serverless applications where functions interact with AWS services like DynamoDB to store and retrieve data.

### package.json
To make the code function properly, we need to add the package.json file (save it next to handler.js) as follows:
```JSON
{
    "type": "module"
}
```

The "type": "module" field in the package.json file is necessary when using ES Modules in a Node.js application. It is needed for AWS Lambda for two reasons:
1. To enable ES Module Syntax. By default, Node.js treats files as CommonJS modules. The "type": "module" declaration in package.json tells Node.js to interpret .js files as ES Modules. This allows you to use modern JavaScript features such as import and export statements which are part of the ES Module specification.
2. To enable compatibility with AWS Lambda. AWS Lambda supports Node.js runtimes that can interpret both CommonJS and ES Modules. However, to use ES Module syntax directly, you need to explicitly set the module type in your package.json. Without "type": "module", Node.js will throw errors if you try to use import and export syntax, as it defaults to CommonJS which uses require and module.exports.

You are now ready to deploy the serverless application.
