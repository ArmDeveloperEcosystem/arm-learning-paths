---
title: Access via API
minutes_to_complete: 15
official_docs: https://anypoint.mulesoft.com/exchange/portals/arm-3/f5af04c7-2f93-4d1e-8355-a60625973e1f/product-entitlement-customer-experience-api/
author: Ronan Synnott
weight: 3    

### FIXED, DO NOT MODIFY
tool_install: false              # Set to true to be listed in main selection page, else false
multi_install: false             # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
The Product Download Hub has an API to enable end users to automate management and download of their Arm products.

## Entitlements and Download Manager

The easiest way to manage access is with the [Entitlements and Download Manager](https://pypi.org/project/edmgr/). This Python based utility can be used to interrogate the download database, and fetch the required packages.

It can be used from Windows command line or a Linux terminal. These instructions are for Linux (Ubuntu 22.04LTS).

### Install pre-requisites
```command
sudo apt update
sudo apt install -y python-is-python3 python3-pip
```
### Install edmgr
```command
sudo pip install edmgr
```
## Generate user token
In a browser, login to PDH and copy your token from the below:
```url
https://developer.arm.com/downloads/token
```
The token is a very long text string, and is valid for one hour.

## Login manager to PDH {#login}

Using the token above, register your identity with the `edmgr` utility.
```cmd
edmgr login token <your_token>
```
A successful login will output:
```output
Token saved in <save_location>
```

## Determine the Product ID

To generate a list of products you are entitled to download use:
```cmd
edmgr entitlements
```
This may be a long list. You can filter by using the [Product Code](https://developer.arm.com/downloads/product-code-mappings) of the item you wish to download.

For example, the `Product Code` of [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) is `DS000B`.

```cmd
edmgr entitlements -p <ProductCode>
```

From this output, you will get a six-digit numeric `ID` of the product you wish to download. This is the `ProductID`.

## Determine the Release ID

For a given product, there will likely be multiple versions available for download. To see a list of these, use the `ProductID` as follows:
```cmd
edmgr releases -e <ProductID>
```
From this table, an `ID` will be shown for each available version. This ID is referred to as the `ReleaseID`.

For example, you can return the `ReleaseID` of `Arm Development Studio 2023.1` of the form `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.

## Determine the Artifact ID

Finally, you must determine the `ArtifactID`, which is the specific package to download.

To determine the `ArtifactID`, you need the `ProductID` and `ReleaseID` from above:
```cmd
edmgr artifacts -e <ProductID> -r <ReleaseID>
```
The `ID` given in the output are the available `ArtifactID`s for this item.

To continue the example, the `Arm Development Studio 2023.1 Linux installer` `ArtifactID` is of the form `yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy`.

## Download the artifact

The package can now be downloaded. You must specify the various `ID`s from above. Use `-d` to specify a directory to store the downloaded package.
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
This output can be used to implement scripts to manage your downloads. A Python script to download the latest `Arm Development Studio` is shown below.

### pdh.py

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

# Determine ReleaseID
cmd2="edmgr releases -e "+ProductID+" -f json > "+ProductID+".json"
os.system(cmd2)
f2 = open(""+ProductID+".json", "r")
data2 =  json.loads(f2.read())
f2.close()
ReleaseID = data2[0]['id']
# Output ReleaseID for debug purposes
print ("ReleaseID =", ReleaseID)

# Determine ArtifactID
cmd3="edmgr artifacts -e "+ProductID+" -r "+ReleaseID+" -f json > "+ReleaseID+".json"
os.system(cmd3)
f3 = open(""+ReleaseID+".json", "r")
data3 =  json.loads(f3.read())
f3.close()
ArtifactID1 = data3[0]['id']
ArtifactID2 = data3[1]['id']
# Output ArtifactID for debug purposes
print ("Two artifacts available (Windows and Linux installers)")
print ("ArtifactID1 =", ArtifactID1)
print ("ArtifactID2 =", ArtifactID2)

# Download Artifacts to current directory
cmd4="edmgr download-artifacts -e "+ProductID+" -r "+ReleaseID+" -a "+ArtifactID1+" -d ."
os.system(cmd4)
cmd5="edmgr download-artifacts -e "+ProductID+" -r "+ReleaseID+" -a "+ArtifactID2+" -d ."
os.system(cmd5)
print("Download complete")

# Tidy up (optional)
os.system("rm -rf *.json")
os.system("ls -l")
os.system("edmgr logout")
```
which can be executed (after [logging in](#login)) with:
```cmd
python pdh.py
```
You should see output similar to:
```output
ProductID = pppppp
ReleaseID = xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Two artifacts available (Windows and Linux installers)
ArtifactID1 = yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy
ArtifactID2 = zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz
Downloading <windows_installer>
...
All done!
Downloading <linux_installer>
...
All done!
Download complete
```
