---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Access via API

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- download

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://anypoint.mulesoft.com/exchange/portals/arm-3/f5af04c7-2f93-4d1e-8355-a60625973e1f/product-entitlement-customer-experience-api/

### PAGE SETUP
weight: 3                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false              # Set to true to be listed in main selection page, else false
multi_install: false             # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
The Product Download Hub has an API to enable end users to automate management and download of their Arm products. It is currently a beta-level feature, but is available for users to experiment with today.

## Entitlements and Download Manager

The easiest way to manage access is with the [Entitlements and Download Manager](https://pypi.org/project/edmgr/). This Python based utility can be used to interrogate the PDH database, and download the required packages. It can be used from Windows command line or a Linux terminal.

To install the utility use:
```cmd
python -m pip install edmgr
```
For a complete list of available commands, use:
```cmd
edmgr --help
```
For a complete list of options for a given command, use:
```cmd
edmgr <command> --help
```

## Generate user token

To confirm your identity, generate and copy your token from the below:
```url
https://developer.arm.com/downloads/token
```
The token is a very long text string, and is valid for one hour.

You are now ready to interact with PDH.

## Login manager to PDH

Using the token above, register your identity with the `edmgr` utility.
```cmd
edmgr login token <your_token>
```

## Determine the Product ID

To generate a list of products you are entitled to download use:
```cmd
edmgr entitlements
```
This may be a long list. You can filter this by using the [Product Code](https://developer.arm.com/downloads/product-code-mappings) of the item you wish to download.

For example, the `Product Code` of [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) is `DS000B`.

```cmd
edmgr entitlements -p <ProductCode>
```

From this output, you will get a six-digit numeric `ID` of the product you wish to download. We shall refer to this as `ProductID` to avoid confusion.

For example, the `ProductID` of Arm Development Studio is `169189`.

## Determine the Release ID

For a given product, there will likely be multiple versions available for download. To see a list of these, use the `ProductID` as follows:
```cmd
edmgr releases -e <ProductID>
```
From this table, an `ID` will be shown for each available version. We shall refer to this as the `ReleaseID`.

For example, the `ReleaseID` of Arm Development Studio, version 2022.2, is `d2650553-3806-4c0e-92d7-2e46fd468074`.

## Determine the Artifact ID

Finally, we must determine the `ArtifactID`, which is the specific package we wish to download. For example, with Arm Development Studio you may wish to download the Linux installer.

To determine the `ArtifactID`, we need the `ProductID` and `ReleaseID` from above:
```cmd
edmgr artifacts -e <ProductID> -r <ReleaseID>
```
The `ID` given in the output are the available `ArtifactID`s for this item.

To continue our example, the Development Studio 2022.2 Linux installer artifact is `7db814ee-c1e3-4d68-a65d-a7e6b437e1ef`.

## Download the artifact

The package can now be downloaded. We must specify the various `ID`s from above. Use `-d` to specify a directory to store the downloaded package.
```cmd
edmgr download-artifacts -e <ProductID> -r <ReleaseID> -a <ArtifactID> -d <directory>
```
## Logout

When done, you can logout, deleting the cached token.
```cmd
edmgr logout
```

## Use JSON format output for scripting

The default output format of the above is a human readable table. Add the `-f json` option to output in JSON format, which is better suited for automation. This can be applied to all relevant steps, for example.
```cmd
edmgr entitlements -f json
```
This output can be used to implement scripts to manage your downloads. A simple Python example may be:

```python
import json
import os

# Set Product Code for Arm Development Studio
ProductCode="DS000B"

# Determine ProductID
cmd1="edmgr entitlements -p "+ProductCode+" -f json > "+ProductCode+".json"
os.system(cmd1)
f1 = open(""+ProductCode+".json", "r")
data1 =  json.loads(f1.read())
f1.close()
ProductID = data1[0]['id']
# Output ProductID for debug purposes
print("ProductID =", ProductID)

# Determine Release ID
cmd2="edmgr releases -e "+ProductID+" -f json > "+ProductID+".json"
os.system(cmd2)
f2 = open(""+ProductID+".json", "r")
data2 =  json.loads(f2.read())
f2.close()
ReleaseID = data2[0]['id']
# Output ReleaseID for debug purposes
print ("ReleaseID =", ReleaseID)

# Determine Artifact ID
cmd3="edmgr artifacts -e "+ProductID+" -r "+ReleaseID+" -f json > "+ReleaseID+".json"
os.system(cmd3)
f3 = open(""+ReleaseID+".json", "r")
data3 =  json.loads(f3.read())
f3.close()
ArtifactID = data3[0]['id']
# Output ArtifactID for debug purposes
print ("ArtifactID =", ArtifactID)

# Download Artifact to current directory
cmd4="edmgr download-artifacts -e "+ProductID+" -r "+ReleaseID+" -a "+ArtifactID+" -d ."
os.system(cmd4)
print("Download complete")

# Tidy up (optional)
os.system("rm -rf *.json")
os.system("ls -l")
os.system("edmgr logout")
```
