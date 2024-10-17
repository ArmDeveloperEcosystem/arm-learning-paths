---
# User change
title: "Implement the AWS Lambda Function"

weight: 4

layout: "learningpathall"
---
# Implementation
To implement the AWS Lambda function scroll down to the Code source section and paste the following code under `index.mjs`. The *.mjs* extension in AWS Lambda indicates that the file is an ECMAScript (ES) module.

```JavaScript
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, ScanCommand } from '@aws-sdk/lib-dynamodb';

const client = new DynamoDBClient({ region: "eu-central-1" });
const dynamoDb = DynamoDBDocumentClient.from(client);

const TABLE_NAME = 'SensorReadings';
const ATTRIBUTE_NAME = 'temperature'; // The name of the attribute (column) you want to average
const TIMESTAMP_ATTRIBUTE_NAME = '#ts'; // Placeholder for the attribute name for the timestamp

export const handler = async (event) => {
  const now = new Date();
  const N = 10; // Number of minutes
  const timeThreshold = new Date(now.getTime() - N * 60 * 1000);

  // Format the time threshold to ISO 8601 string
  const formattedTimeThreshold = timeThreshold.toISOString();
  
  // Look for records not older than the timeThreshold
  const params = {
    TableName: TABLE_NAME,
    FilterExpression: `${TIMESTAMP_ATTRIBUTE_NAME} >= :timeThreshold`,
    ExpressionAttributeNames: {
      '#ts': 'timestamp', // Map the placeholder to the actual attribute name
    },
    ExpressionAttributeValues: {
      ':timeThreshold': formattedTimeThreshold,
    },
  };

  try {
    const data = await dynamoDb.send(new ScanCommand(params));
    const items = data.Items;

    if (!items || items.length === 0) {
      return {
        statusCode: 200,
        body: JSON.stringify({ average: 0 }),
      };
    }
    
    const numericalValues = items.map(item => parseFloat(item[ATTRIBUTE_NAME])).filter(value => !isNaN(value));

    if (numericalValues.length === 0) {
      return {
        statusCode: 200,
        body: JSON.stringify({ average: 0 }),
      };
    }

    const sum = numericalValues.reduce((acc, value) => acc + value, 0);
    const average = sum / numericalValues.length;

    return {
      statusCode: 200,
      body: JSON.stringify({ average }),
    };

  } catch (error) {
    console.error('Error reading from DynamoDB', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Could not read from DynamoDB' }),
    };
  }
};
```
## Understanding the code 
In the code above, you first import the AWS SDK for JavaScript v3. Specifically, the following code imports the necessary classes from the AWS SDK for working with DynamoDB: 
* DynamoDBClient is the client for DynamoDB, part of the AWS SDK for JavaScript v3.
* DynamoDBDocumentClient provides a higher-level API for working with DynamoDB items as native JavaScript objects.
* ScanCommand is used to perform a scan operation on a DynamoDB table.

```JavaScript
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, ScanCommand } from '@aws-sdk/lib-dynamodb';
```

An instance of DynamoDBClient is then created, specifying the AWS region (eu-central-1 in this case):

```JavaScript
const client = new DynamoDBClient({ region: "eu-central-1" }); // Update to your region
const dynamoDb = DynamoDBDocumentClient.from(client);
```

The client initializes a new DynamoDB client for the specified region, while `dynamoDb` wraps the DynamoDB client in a document client for easier interaction with DynamoDB items.

Next, you have three constants as shown below:

```JavaScript
const TABLE_NAME = 'SensorReadings';
const ATTRIBUTE_NAME = 'temperature'; // The name of the attribute (column) you want to average
const TIMESTAMP_ATTRIBUTE_NAME = '#ts'; // Placeholder for the attribute name for the timestamp
```

- TABLE_NAME stores the name of the DynamoDB table from which to scan records.
- ATTRIBUTE_NAME stores the name of the attribute (column in a table) that contains the numerical values to average (in this example it is set to 'temperature').
- TIMESTAMP_ATTRIBUTE_NAME is a placeholder for the attribute name for the timestamp. This is used to avoid conflicts with reserved keywords in DynamoDB.

Next there is a declaration of the handler function, which is the entry point for the AWS Lambda function:

```JavaScript
export const handler = async (event) => {
  const now = new Date();
  const N = 10; // Number of minutes
  const timeThreshold = new Date(now.getTime() - N * 60 * 1000);

  // Format the time threshold to ISO 8601 string
  const formattedTimeThreshold = timeThreshold.toISOString();    

  // Subsequent declarations
}
```

The handler receives an event object which in this case is ignored. Then, the handler declares four constants (variables whose values cannot be reassigned):
* **now** - gets the current date and time.
* **N** - the number of minutes to look back from the current time.
* **timeThreshold** - calculates the time threshold by subtracting N minutes from the current time.
* **formattedTimeThreshold** - formats the time threshold to an ISO 8601 string.

When dealing with timestamps and comparing dates across different systems, such as IoT devices and servers, it is crucial to handle the time zones correctly to ensure accurate comparisons and calculations. IoT devices may operate in various time zones which can differ from the time zone of the server running the AWS Lambda function. To manage this, you will use the ISO 8601 format for timestamps. 

The ISO 8601 format is a standardized way to represent dates and times. It includes the date, time, and time zone information, ensuring consistency across different systems. The format looks like this: YYYY-MM-DDTHH:mm:ss.sssZ, where Z indicates the UTC (Coordinated Universal Time) time zone.

By formatting the time threshold to an ISO 8601 string, you ensure that both the IoT device’s timestamps and the server’s time threshold are in a consistent format. Comparing timestamps in a standardized format ensures that the time-based filtering logic works correctly.

Now you will configure the DynamoDB scan parameters:

```JavaScript
const params = {
  TableName: TABLE_NAME,
  FilterExpression: `${TIMESTAMP_ATTRIBUTE_NAME} >= :timeThreshold`,
  ExpressionAttributeNames: {
    '#ts': 'timestamp', // Map the placeholder to the actual attribute name
  },
  ExpressionAttributeValues: {
    ':timeThreshold': formattedTimeThreshold,
  },
};
```

Here, `FilterExpression` is used to filter the items to only those with a timestamp greater than or equal to the time threshold. Then, `ExpressionAttributeNames` maps the placeholder to the actual attribute name. Finally, `ExpressionAttributeValues` defines the value for the placeholder.

The AWS Lambda function then executes the scan command against the table with the specified parameters, as shown below:

```JavaScript
try {
  const data = await dynamoDb.send(new ScanCommand(params));
  const items = data.Items;  
  
  // Items processing

} catch (error) {
  console.error('Error reading from DynamoDB', error);
  return {
    statusCode: 500,
    body: JSON.stringify({ error: 'Could not read from DynamoDB' }),
  };
}
```

After executing the scan command you will get the list of items in the form of a JSON collection. You process them as follows:
```JavaScript
if (!items || items.length === 0) {
    return {
      statusCode: 200,
      body: JSON.stringify({ average: 0 }),
    };
}
  
const numericalValues = items.map(item => parseFloat(item[ATTRIBUTE_NAME])).filter(value => !isNaN(value));

if (numericalValues.length === 0) {
    return {
        statusCode: 200,
        body: JSON.stringify({ average: 0 }),
    };
}

const sum = numericalValues.reduce((acc, value) => acc + value, 0);
const average = sum / numericalValues.length;

return {
    statusCode: 200,
    body: JSON.stringify({ average }),
};
```

If no items are found, it will return 0 as the average value. Otherwise, it will convert the attribute values to numbers and this filters out any non-numeric values. Next, it will calculate the sum and average of the numerical values. Finally, this average value is returned to the caller.

