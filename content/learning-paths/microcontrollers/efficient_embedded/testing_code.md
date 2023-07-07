---
# User change
title: "Running the code on the board" 

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

You are now ready to build the code and run it on the target hardware.

## Compile the code

Click the `Build` button to compile source code, and link together.

![Build #center](Images/Build.png)


 ## Run and debug the code on the target

Ensure your board is connected to your host machine. Click `Download` to load it onto the Flash memory on the board.

![Flash #center](Images/Flash.png)

Once flashed onto the board, you can start a debug session.

![Debug #center](Images/Debug.png)

Open the `Call Stack + Locals` tab in the IDE. This will show the value of the variables `a` and `b`.

![CallStack #center](Images/CallStack.png)

Step through the program and notice how the values of `a` and `b` change.

![Callstack2 #center](Images/CallStack2.png)

You will see the string "Hello world!" copy across and then eventually turn into capitals.

![CallStack3 #center](Images/CallStack3.png)
