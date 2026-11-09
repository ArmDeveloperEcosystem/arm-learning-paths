---
title: Create a signed copy of an image with Content Credentials
description: Define provenance assertions and sign a JPEG with C2PA Tool's development credential while preserving the unsigned source image.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a signed copy of the sample image

Now that you've downloaded a sample image, you'll add Content Credentials to the image. You'll save the
signed image as a separate file, preserving the unsigned original.

### Create the manifest definition

A manifest definition tells the Coalition for Content Provenance and Authenticity (C2PA) Tool which information to include in the manifest. An [assertion](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html#_assertion)
is a structured statement about an asset. Assertions can describe creation and editing actions,
identify source assets used as ingredients, or record metadata. 

For the standard assertion types and their definitions, see the
[C2PA standard assertion summary](https://spec.c2pa.org/specifications/specifications/2.4/specs/ContentCredentials.html#_standard_c2pa_assertion_summary). This example uses an actions assertion to declare how the image was created.

The [claim generator](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html#claim-generator-definition) is the software that assembles the claim and its references to assertions for
signing. C2PA Tool performs that work using the example identity that you'll provide.

In your text editor, create a file named `manifest.json` in your `c2pa-demo` working
directory with the following contents:

```json
{
  "claim_generator_info": [
    {
      "name": "Arm Learning Path C2PA Example",
      "version": "1.0.0",
      "com.arm.learning_path.tool": {
        "name": "c2patool",
        "version": "0.27.21"
      }
    }
  ],
  "assertions": [
    {
      "label": "c2pa.actions.v2",
      "data": {
        "actions": [
          {
            "action": "c2pa.created",
            "digitalSourceType": "http://cv.iptc.org/newscodes/digitalsourcetype/digitalCapture"
          }
        ]
      }
    }
  ]
}
```

On Windows, enable **File name extensions** in File Explorer. Confirm that the filename is `manifest.json`, rather than `manifest.json.txt`.

The manifest definition identifies the signing workflow and records the declared origin of the image:

- `claim_generator_info` names your signing workflow `Arm Learning Path C2PA Example`, version
  `1.0.0`. This version identifies the Learning Path workflow. It's separate from the installed C2PA Tool
  version.

- `com.arm.learning_path.tool` records the name and version of the tool. Set `version` to the value
  reported by `c2patool --version`. The `com.arm` prefix identifies this as a custom field, following
  the C2PA [rules for extending claim-generator information](https://spec.c2pa.org/specifications/specifications/2.4/specs/ContentCredentials.html#_generator_info_map).

- `assertions` contains a `c2pa.actions.v2` assertion. Its `data.actions` array records a
  `c2pa.created` action, with `digitalSourceType` declaring digital capture as the origin of the image.

  You'll supply this declaration to complete the Learning Path. C2PA Tool doesn't verify how the image was created.
  
  Signing makes changes to the declaration detectable. Signing doesn't establish that it's true.

  An action can also include `softwareAgent` to identify the software or hardware that performed it.
  You omit that field because the original capture agent of the sample is unknown. C2PA Tool generates the
  claim but doesn't capture the image.

C2PA Tool generates the claim, content-binding data, and signature when it builds the signed manifest. You don't write those cryptographic structures manually.

C2PA Tool also offers a command-line shortcut: with an empty `assertions` array, `--create digitalCapture`
adds the creation action. If you omit `claim_generator_info`, the tool supplies its own name and
version instead of this example label. Keep the explicit claim-generator information to retain the
Learning Path label. You've already defined the creation action in `manifest.json`, so omit `--create` when signing the image.

### Understand the development credentials

The example development credentials use the private key and signing certificate that are built into C2PA Tool. These credentials
let you practice signing, but don't establish a production identity or trust by public validators.
Don't use them to sign production content. Use the development credentials to complete the Learning Path for consistent validation results.

For production, C2PA Tool supports an external signer. The signer supplies the certificate chain and uses
the corresponding private key without exposing it to the tool. When you have such a signer,
the command takes this form:

```console
c2patool image.jpg --manifest manifest.json --signer-path /path/to/production-signer --output image-production-signed.jpg
```

This is an illustrative alternative. Don't run the command.

`/path/to/production-signer` is a placeholder for an executable implementing the
[C2PA Tool signer protocol](https://github.com/contentauth/c2patool/blob/main/docs/signing.md). It's
not a certificate file. 

The signer supplies its certificate chain and signing algorithm, and it manages access to the private key. Don't copy production private keys into the manifest definition.

For production conformance requirements, see [C2PA Conformance Program](/learning-paths/embedded-and-microcontrollers/c2pa-on-arm/1-understand-the-c2pa/#c2pa-conformance-program).

### Sign the image

Sign the image in the `c2pa-demo` directory. Ensure that a file with the same name as the output doesn't already exist. If it does, move or rename the existing file before you continue:

```console
c2patool image.jpg --manifest manifest.json --output image-signed.jpg
```

`--manifest manifest.json` supplies your definition. `--output image-signed.jpg` writes the
signed image to a separate file, leaving `image.jpg` unchanged.

The command exits with status `0` when signing succeeds. 

The output includes the following development warning:

```output
Note: Using default private key and signing certificate. This is only valid for development.
A permanent key and cert should be provided in the manifest definition or in the environment variables.
```

The command also prints the generated manifest report. Its generated identifiers differ between runs.
You'll inspect the report later.

## Confirm that the signed file contains a manifest

Inspect the signed image to check that a manifest is present:

```console
c2patool image-signed.jpg --info
```

The expected output includes:

```output
Validation issues:
   signingCredential.untrusted
One manifest
```

`One manifest` confirms that the output contains a C2PA manifest. `signingCredential.untrusted` is the
expected trust result for this development certificate. It doesn't mean that signing failed.

The byte counts and percentages printed by this command can vary.

## What you've accomplished and what's next

You've defined the provenance information, signed the image, and confirmed that the output contains
a manifest. 

Keep the following three files to complete the rest of the Learning Path:

| File | Purpose |
| --- | --- |
| `manifest.json` | Your claim-generator information and creation assertion |
| `image.jpg` | The unchanged unsigned source image |
| `image-signed.jpg` | The signed image containing the C2PA manifest |

Next, you'll inspect the generated manifest and confirm that C2PA Tool reports a valid signature and content binding.
