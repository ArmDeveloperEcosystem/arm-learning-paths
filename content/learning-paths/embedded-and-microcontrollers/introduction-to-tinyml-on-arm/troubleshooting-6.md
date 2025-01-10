---
title: Troubleshooting and Best Practices
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

TODO can these be incorporated in the LP?

## Troubleshooting
- If you encounter permission issues, try running the commands with sudo.
- Ensure your Grove - Vision AI Module V2 is properly connected and recognized by your computer.
- If Edge Impulse CLI fails to detect your device, try unplugging, hold the **Boot button** and replug the USB cable. Release the button once you replug.

## Best Practices
- Always cross-compile your code on the host machine to ensure compatibility with the target Arm device.
- Utilize model quantization techniques to optimize performance on constrained devices like the Grove - Vision AI Module V2.
- Regularly update your development environment and tools to benefit from the latest improvements in TinyML and edge AI technologies

You've now set up your environment for TinyML development, and tested a PyTorch and ExecuTorch Neural Network.