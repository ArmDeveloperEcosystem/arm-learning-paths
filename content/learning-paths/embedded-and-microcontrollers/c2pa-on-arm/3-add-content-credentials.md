---
title: Add Content Credentials to an image
description: Define provenance assertions and sign a JPEG with C2PA Tool's development credential while preserving the unsigned source image.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Add Content Credentials to an image

You will add Content Credentials to the image prepared in the previous chapter. You will save the
signed image as a separate file, preserving the unsigned original.

## Understand the development credential

The example uses the private key and signing certificate built into C2PA Tool. These test credentials
let you practise signing, but do not establish a production identity or trust by public validators.
Do not use them to sign production content.

## Create the manifest definition

A manifest definition tells C2PA Tool which information to include in the manifest. An [*assertion*](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html#_assertion)
is a structured statement about an asset. Assertions can describe creation and editing actions,
identify source assets used as ingredients, or record metadata. See the
[C2PA standard assertion summary](https://spec.c2pa.org/specifications/specifications/2.4/specs/ContentCredentials.html#_standard_c2pa_assertion_summary)
for the standard assertion types and links to their definitions. This example uses an actions assertion
to declare how the image was created.

The [*claim generator*](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html#claim-generator-definition) is the software that assembles the claim and its references to assertions for
signing. In this exercise, C2PA Tool performs that work using the example identity you supply below.

In your text editor, create a plain-text file named `manifest.json` in your `c2pa-demo` working directory
with these contents:

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

The manifest definition identifies the signing workflow and records the image's declared origin:

- **`claim_generator_info`** names your signing workflow `Arm Learning Path C2PA Example`, version
  `1.0.0`. This version identifies the tutorial workflow; it is separate from the installed C2PA Tool
  version.

- **`com.arm.learning_path.tool`** records the tool's name and version. Set `version` to the value
  reported by `c2patool --version`. The `com.arm` prefix identifies this as a custom field, following
  C2PA's [rules for extending claim-generator information](https://spec.c2pa.org/specifications/specifications/2.4/specs/ContentCredentials.html#_generator_info_map).

- **`assertions`** contains a `c2pa.actions.v2` assertion. Its `data.actions` array records a
  `c2pa.created` action, with `digitalSourceType` declaring digital capture as the image's origin.

  You supply this declaration for the exercise. C2PA Tool does not verify how the image was created.
  Signing makes changes to the declaration detectable, but does not establish that it is true.

  An action can also include `softwareAgent` to identify the software or hardware that performed it.
  You omit that field because the sample's original capture agent is unknown. C2PA Tool generates the
  claim, but did not capture the image.

You supply the provenance fields above. C2PA Tool generates the claim, content-binding data, and signature
when it builds the signed manifest; you do not write those cryptographic structures by hand.

C2PA Tool also offers a command-line shortcut: with an empty `assertions` array, `--create digitalCapture`
adds the creation action. If you omit `claim_generator_info`, the tool supplies its own name and
version instead of this example label. Keep the explicit claim-generator information to retain the
Learning Path label. You have already defined the creation action in `manifest.json`, so omit `--create` when signing the image.

## Sign the image

Run this command from your `c2pa-demo` directory. The output filename must not already exist. If it
does, move or rename that earlier output before you continue.

```console
c2patool image.jpg --manifest manifest.json --output image-signed.jpg
```

`--manifest manifest.json` supplies your definition. `--output image-signed.jpg` writes the
signed image to a separate file, leaving `image.jpg` unchanged.

The command exits with status 0 when signing succeeds. The expected development warning is:

```output
Note: Using default private key and signing certificate. This is only valid for development.
A permanent key and cert should be provided in the manifest definition or in the environment variables.
```

The command also prints the generated manifest report. Its generated identifiers differ between runs.
You will inspect that report in the next chapter.

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
expected trust result for this development certificate; it does not mean that signing failed.
The byte counts and percentages also printed by this command can vary.

## What you've accomplished and what's next

You have defined the provenance information, signed the image, and confirmed that the output contains
a manifest. Keep these three files for the remaining chapters:

| File | Purpose |
| --- | --- |
| `manifest.json` | Your claim-generator information and creation assertion |
| `image.jpg` | The unchanged unsigned source image |
| `image-signed.jpg` | The signed image containing the C2PA manifest |

Next, inspect the generated manifest and confirm that C2PA Tool reports a valid signature and content binding.
