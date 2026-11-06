---
title: Validate Content Credentials with a web validator
description: Validate the signed JPEG with the CAI web validator and compare its provenance display and issuer warning with the C2PA Tool report.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Validate the signed image with the CAI web validator

You'll open the signed image `image-signed.jpg` in the
[Content Authenticity Initiative (CAI) web validator](https://verify.contentauthenticity.org/). The CAI web validator is
a browser-based tool for inspecting and validating Content Provenance and Authenticity (C2PA) Content Credentials. 
The site calls this tool **Verify**. You'll read the recorded provenance and compare the validation results with your
C2PA Tool report.

According to its [open-source project](https://github.com/contentauth/verify-site), the validator uses
WebAssembly to read and validate C2PA data in your browser. The website can still make network
requests, so this doesn't mean that it operates entirely offline.

To validate the image with the CAI web validator:

1. Open the [CAI web validator](https://verify.contentauthenticity.org/) in your browser. The start page says
   **Inspect content to dig deeper** and lists JPEG among its supported formats.
2. Select **Select a file from your device**, as shown in the screenshot that follows.
3. Select `image-signed.jpg` from your `c2pa-demo` directory and open it. You can also drag the file
   onto the page.
4. Wait for the image and its Content Credentials panel to appear.

If you use another computer, copy `image-signed.jpg` without modifying or recompressing it.

<a id="figure-1"></a>

![CAI web validator start page with Select a file from your device and JPEG in the supported formats. Use this control to open image-signed.jpg.#center](images/verify-select-file.jpg "Select the signed JPEG in the CAI web validator")

## Inspect the validation result

In the Content Credentials panel, look for **Unrecognized** beside `image-signed.jpg`, as shown in
the screenshot that follows. The orange notice indicates that the CAI web validator doesn't recognize the issuer of the credential under its
trust policy. As explained in [Understand the development credentials](/learning-paths/embedded-and-microcontrollers/c2pa-on-arm/3-add-content-credentials/#understand-the-development-credential),
the built-in signing certificate is for development. It doesn't establish a production identity.

<a id="figure-2"></a>

![The CAI web validator shows image-signed.jpg with an Unrecognized status and an orange notice about its issuer.#center](images/verify-unrecognized.jpg "Figure 2. Expected result for the development credential")

{{% notice Note %}}
If no Content Credentials appear, check that you selected `image-signed.jpg`, not `image.jpg`.
If you transferred the file, retry with a copy of the original signed output.
{{% /notice %}}

## Read the recorded provenance

Scroll through the Content Credentials panel. Read **Content summary**, then expand **Process**
for the recorded action and app or device name. Expand **About this Content Credential** to find
**Issued by**, as shown in the following screenshot.

<a id="figure-3"></a>

![The CAI web validator's details panel shows captured media, the Created action, C2PA Signer, and issuer C2PA Test Signing Cert. Locate the creation and issuer fields in this panel.#center](images/verify-credential-details.jpg "Figure 3. Recorded provenance and test-certificate issuer")

## Compare the result with your C2PA Tool report

Open `report.json` and locate the active manifest as described in
[Find the active manifest](/learning-paths/embedded-and-microcontrollers/c2pa-on-arm/4-inspect-content-credentials/#find-the-active-manifest).
Use its `assertions` and `signature_info` fields for the provenance comparison, and
`validation_results` for signer trust:

| Information | C2PA Tool report | CAI web validator view |
| --- | --- | --- |
| Declared origin | `digitalSourceType` ending in `/digitalCapture` | Content summary: This is captured media. |
| Creation action | `action: "c2pa.created"` | Process → Actions: Created |
| Signing certificate's common name | `signature_info.common_name: "C2PA Signer"` | Process → App or device used: C2PA Signer |
| Signing certificate's issuer | `signature_info.issuer: "C2PA Test Signing Cert"` | About this Content Credential → Issued by: C2PA Test Signing Cert |
| Signer trust | `signingCredential.untrusted` | Unrecognized issuer |

The captured-media summary and **Created** action reflect the declaration that you provided earlier.

**App or device used** shows `C2PA Signer` and matches the common name of the development signing certificate. It doesn't match the custom `Arm Learning Path C2PA Example` label. This is expected because the C2PA Tool generated the claim. It didn't capture the photograph.

The web panel displays the provenance of the image without separate signature or binding status codes.
As confirmed in [Interpret the result](/learning-paths/embedded-and-microcontrollers/c2pa-on-arm/4-inspect-content-credentials/#interpret-the-result),
both checks pass for this image. **Unrecognized** refers to signer trust. You'll later modify a copy of the image to see how a content-binding failure changes the validation result.

Validating Content Credentials on its own doesn't establish that the depicted scene or the recorded
assertions are true. Successful signature and binding checks show that the signed provenance record
is intact and bound to this image. Establishing credential trust also requires the validator to accept
the signing credential under its trust policy. 

To decide whether to believe the content, consider the following factors:

- The identity and reliability of the signer
- The recorded history
- Any corroborating evidence

## What you've accomplished and what's next

You can now read the web validator provenance summary and interpret its issuer warning alongside
the detailed C2PA Tool results. Keep `image-signed.jpg` unchanged. 

Next, you'll modify a separate copy and inspect the resulting content-binding failure.
