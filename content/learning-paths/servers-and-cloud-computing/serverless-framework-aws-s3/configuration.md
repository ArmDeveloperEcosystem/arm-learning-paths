---
title: Service declaration
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Service Declaration
In this section, you will declare a serverless service composed of the following AWS resources:
  * DynamoDB Table - this stores hypothetical sensor data, including timestamps and randomly-generated temperatures.
  * Two AWS Lambda Functions - the first function writes temperatures to the DynamoDB table, and the second retrieves the average temperature value.
  * IAM Role - a set of permissions that enable the AWS Lambda functions to write to and read data from the DynamoDB table.
  * S3 Bucket - a bucket that hosts the static website.

Additionally, the service uses the Serverless S3 Sync plugin to deploy the static website to the S3 bucket. The website contains two buttons and a text box: the buttons allow the user to invoke the Lambda functions, and the text box displays the average temperature stored in the DynamoDB table.

You will also add JavaScript code that reads the API endpoints of the two AWS Lambda functions and dynamically updates the static website.

### Declare a service
To create a new serverless service, open the command prompt or terminal and enter the following:

```console
serverless
```

In the wizard that appears, proceed as follows:
1.	Select the **AWS / Node.js / Simple Function** template.
2.	In the *Name Your Project* field, type **AwsServerlessDynamoDbLambdaS3**.
3.	In the *Please login/register* or *enter your license key* section, select **Login/Register** and sign in to the Serverless Framework.
4.	In the *Create Or Select An Existing App* section, select **Skip Adding An App**.

The tool generates the project composed of the following files:
*	`serverless.yml` - this contains the declaration of the infrastructure and services for a serverless application.
*	`handler.js` - you use this file to implement the core functionality of your serverless application, handling business logic and interactions with other services. Here, you will use this file to implement Lambda functions.

### serverless.yml
To define the AWS resources, open `serverless.yml` and modify it as follows:
```YAML
org: <KEEP_YOUR_ORG_NAME>

service: AwsServerlessDynamoDbLambdaS3

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

    WebsiteBucket:
      Type: AWS::S3::Bucket
      Properties:
        BucketName: iot-temperature-service-${self:provider.stage}-website
        WebsiteConfiguration:
          IndexDocument: index.html
          ErrorDocument: error.html
        OwnershipControls: 
          Rules: 
            - ObjectOwnership: BucketOwnerEnforced 
        PublicAccessBlockConfiguration:
          BlockPublicAcls: false
          BlockPublicPolicy: false
          IgnorePublicAcls: false
          RestrictPublicBuckets: false

    WebsiteBucketPolicy:
      Type: AWS::S3::BucketPolicy
      Properties:
        Bucket: !Ref WebsiteBucket
        PolicyDocument:
          Statement:
            - Effect: Allow
              Principal: "*"
              Action: "s3:GetObject"
              Resource: 
                !Sub "arn:aws:s3:::${WebsiteBucket}/*"

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
    WebsiteURL:
      Description: "URL of the S3 hosted website"
      Value:
        Fn::Join:
          - ""
          - - "http://"
            - Ref: WebsiteBucket
            - ".s3-website-${self:provider.region}.amazonaws.com"

plugins:
  - serverless-s3-sync
  - serverless-plugin-scripts

custom:
  s3Sync:
    - bucketName: iot-temperature-service-${self:provider.stage}-website
      localDir: website

  scripts:
    hooks:
      "before:deploy:deploy": npm run prepare

package:
  exclude:
    - node_modules/**
```
This declaration builds upon the configuration you created in the Learning Path entitled [Deploy and integrate AWS Lambda with DynamoDB using the Serverless Framework](/learning-paths/servers-and-cloud-computing/serverless-framework-aws-lambda-dynamodb/). Specifically, it includes a declaration for a DynamoDB table, an IAM role, and two Lambda functions:
 * `writeTemperatures` - its handler is set to handler.writeTemperatures. This function is triggered through an HTTP POST event.
 * `getAverageTemperature` - its handler is set to handler.getAverageTemperature. This function is triggered through an HTTP GET event.

There are a few new additions. Under the *Resources* section, you have the S3 Bucket configuration, which specifies the following:
* `WebsiteBucket` - creates an S3 bucket named `iot-temperature-service-${self:provider.stage}-website`, where `${self:provider.stage}` dynamically inserts the deployment stage (for example, dev, prod).
* `WebsiteConfiguration` - configures the S3 bucket to host a static website, specifying `index.html` as the main page and error.html as the error page.
* `OwnershipControls` - ensures that the bucket enforces ownership for all objects.
* `PublicAccessBlockConfiguration` - disables public access block settings, allowing the bucket to serve content publicly.
* `WebsiteBucketPolicy` - sets a bucket policy that grants public read access to all objects within the S3 bucket.

These settings are required to make the website publicly available.

Next, you define outputs for the Serverless deployment:
* `WriteTemperaturesEndpoint` and `GetAverageTemperatureEndpoint` - these provide the full URLs of the API Gateway endpoints for the two AWS Lambda functions.
* `WebsiteURL` - generates the URL for the S3-hosted static website.

In the Plugins section, you define:
* `serverless-s3-sync` - syncs local files from the website directory to the specified S3 bucket during deployment.
* `serverless-plugin-scripts` - allows custom scripts to be run before deployment.

Then, you specify custom settings for the plugins:
* `custom`: defines custom settings for the S3 sync plugin.
* `s3Sync`: specifies the local directory (website) to be synced to the S3 bucket.

Lastly, you exclude the `node_modules` directory from the deployment package using `package.exclude` to reduce the package size.
  
### handler.js
You will now implement the two AWS Lambda functions. Open the file `handler.js`, and replace its contents with the following code:

```JavaScript
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, BatchWriteCommand, ScanCommand  } from '@aws-sdk/lib-dynamodb';

const client = new DynamoDBClient({ region: "us-east-1" });
const dynamoDb = DynamoDBDocumentClient.from(client);
const tableName = process.env.DYNAMODB_TABLE;

// Helper function to create response
export const createResponse = (statusCode, body) => {
  return {
    statusCode: statusCode,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': true
    },
    body: JSON.stringify(body),
  };
};

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
    return createResponse(200, { message: 'Temperature records written successfully!' });
  } catch (error) {
    return createResponse(500, { message: 'Failed to write temperature records', error: error.message });
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

    return createResponse(200, { averageTemperature });
  } catch (error) {
    return createResponse(500, { message: 'Failed to retrieve temperature records', error: error.message });
  }
};
```

The code defines the two AWS Lambda functions that interact with a DynamoDB table:
 1. `writeTemperatures` - writes a batch of random temperature records to the DynamoDB table.
 2. `getAverageTemperature` - retrieves the last N temperature records from the table, calculates the average, and returns it.

They are the same as in [Deploy and integrate AWS Lambda with DynamoDB using the Serverless Framework](/learning-paths/servers-and-cloud-computing/serverless-framework-aws-lambda-dynamodb/). The only difference is that you now have a helper function, **createResponse**, which is a utility function used to standardize HTTP responses for AWS Lambda functions. This function formats the response to ensure it includes the necessary HTTP status code, headers, and body, making it easier to handle CORS (Cross-Origin Resource Sharing) and JSON responses consistently across different Lambda functions. CORS is configured because the S3 bucket domain might differ from the AWS Lambda function endpoints.

The service configuration is now ready, and you can move on to prepare the website and supporting files.
