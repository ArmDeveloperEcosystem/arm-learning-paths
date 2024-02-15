---
title: "Build the cross-platform application"

weight: 3

layout: "learningpathall"
---

## Objective 
In this section you will build your application to run on both Arm64 and x64.

## Electron Builder
Start by installing the Electron Builder:

```console
npm install electron-builder --save-dev
```

The output will look similar to:
```output
added 191 packages, removed 12 packages, changed 18 packages, and audited 265 packages in 23s

28 packages are looking for funding
  run `npm fund` for details

4 vulnerabilities (3 moderate, 1 high)

To address all issues (including breaking changes), run:
  npm audit fix --force

Run `npm audit` for details.
```

Modify the `package.json` file in your project folder with the content shown below:

```JSON
{
  "name": "electron-sample-app",
  "version": "1.0.0",
  "description": "Electron application to retrieve data from API and display it in a table.",
  "main": "main.js",
  "scripts": {
    "start": "electron .",
    "build": "electron-builder"
  },
  "author": "Learning Path",
  "license": "MIT",
  "dependencies": {
    "axios": "^0.21.4",    
    "jquery": "^3.6.0"
  },
  "devDependencies": {
    "electron-builder": "^22.12.0",
    "electron": "^16.0.5"
  },
  "build": {
    "appId": "com.example.electron-sample-app",
    "productName": "Electron Sample Application",
    "directories": {
      "output": "dist"
    }, 
    "win": {
      "target": [
        "nsis", 
        "nsis:x64"
      ]
    }
  }
}
```

## Build the application
Finally, you can build the application using the following command:

```console
npm run build
```

The above command generates the following output:

```output
> electron-sample-app@1.0.0 build
> electron-builder

  • electron-builder  version=24.9.1 os=10.0.22631
  • loaded configuration  file=package.json ("build" field)
  • writing effective config  file=dist\builder-effective-config.yaml
  • packaging       platform=win32 arch=arm64 electron=16.2.8 appOutDir=dist\win-arm64-unpacked
  • default Electron icon is used  reason=application icon is not set
  • packaging       platform=win32 arch=x64 electron=16.2.8 appOutDir=dist\win-unpacked
  • downloading     url=https://github.com/electron/electron/releases/download/v16.2.8/electron-v16.2.8-win32-x64.zip size=85 MB parts=8
  • downloaded      url=https://github.com/electron/electron/releases/download/v16.2.8/electron-v16.2.8-win32-x64.zip duration=3.87s
  • building        target=nsis file=dist\Electron Sample Application Setup 1.0.0.exe archs=arm64, x64 oneClick=true perMachine=false
  • output file is locked for writing (maybe by virus scanner) => waiting for unlock...
  • building block map  blockMapFile=dist\Electron Sample Application Setup 1.0.0.exe.blockmap
  ```

  The Electron Builder will generate distributables of the application for Windows using two architectures x64 and Arm64. You will find them in the following folders:
  * x64: <project folder>\dist\win-unpacked
  * Arm64: <project folder>\dist\win-arm64-unpacked

  Each folder contains the executable `Electron Sample Application.exe`. Launch this executable from both folders. Then, open the Task Manager to check that both executables run as either x64 or Arm64 processes.

## Summary
In this learning path, you created the Electron application designed to retrieve and display data from a mock API in a user-friendly table format. Developed using web technologies such as HTML, CSS, and JavaScript, this application leverages the Electron framework to seamlessly run on Windows. With added support for both x64 and Arm64 architectures on Windows, this application demonstrates the flexibility and adaptability of Electron in building robust desktop solutions for a wide range of use cases.
