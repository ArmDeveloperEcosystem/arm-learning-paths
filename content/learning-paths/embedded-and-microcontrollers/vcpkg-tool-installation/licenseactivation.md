---
title: Activate a license
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Activate a license

Arm tools are license managed. The [Arm Compiler for Embedded (ACfE)](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) comes with the necessary executables to manage licenses. Before you can compile with ACfE, you need to install a license.

[Keil MDK v6](https://www.keil.arm.com) comes with a free-to-use, non-commercial license that is easy to activate.

### Activate an MDK-Community license

```shell
armlm activate -product KEMDK-COM0 -server https://mdk-preview.keil.arm.com
```

### [Optional] Check your license

```bash { output_lines = "2-9" }
armlm inspect
1 active product in your local cache:

Keil MDK Community
    Product code: KEMDK-COM0
    Order Id: Community
    License valid until: 2033-05-31
    Local cache expires: 6 days and 0 hours
    License server: https://mdk-preview.keil.arm.com
```

### Deactivate an MDK-Community license

```bash { output_lines = "2-8" }
armlm deactivate -product  KEMDK-COM0

Deactivation of Keil MDK Community was successful.

License server records are unchanged by this action. A license seat may still be allocated to you depending on the last time the local cache was refreshed on this or other devices.

Please consult the documentation at https://lm.arm.com for more information on deactivation.
```

### Reactivate an MDK-Community license

```bash { output_lines = "2-3" }
armlm reactivate -product KEMDK-COM0
Reactivation of Keil MDK Community was successful. It has been renewed and added to your local license store.
```

{{% notice Tip %}}
Refer to the [User-based Licensing User Guide](https://developer.arm.com/documentation/102516/latest/User-based-licensing-overview) for more information how to activate commercial licenses.
{{% /notice %}}

Now, you are ready to build projects with Arm Compiler for Embedded.