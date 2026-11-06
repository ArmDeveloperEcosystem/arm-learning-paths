---
title: Create and verify C2PA Content Credentials on Arm

description: Use C2PA Tool on an Arm device to sign and inspect a sample image, then validate its Content Credentials and detect a content-binding failure.

minutes_to_complete: 55

who_is_this_for: This is an introductory topic for developers who want to add and validate Coalition for Content Provenance and Authenticity (C2PA) Content Credentials on Arm devices.

learning_objectives:
    - Understand what C2PA is, the content provenance problem it addresses, and why provenance matters.
    - Add Content Credentials to a sample image on an Arm device.
    - Inspect the manifest, interpret content-binding, signature, and trust results.
    - Validate Content Credentials with an external validator.
    - Identify a content-binding failure after a controlled change to the image.

prerequisites:
    - The current stable release of [C2PA Tool](/install-guides/c2patool/) installed on your Arm device
    - An installation of [ExifTool](/install-guides/exiftool/) on your Arm device
    - An installation of [libjpeg-turbo](/install-guides/libjpeg-turbo/) on your Arm device
    - Familiarity with running command-line tools

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-06T22:44:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3c4eb3393184df9c9b267a0d8a02ec557f2c3ea6fb38a4abb51ba68e9ff21895
  summary_generated_at: '2026-11-06T22:44:33Z'
  summary_source_hash: 3c4eb3393184df9c9b267a0d8a02ec557f2c3ea6fb38a4abb51ba68e9ff21895
  faq_generated_at: '2026-11-06T22:44:33Z'
  faq_source_hash: 3c4eb3393184df9c9b267a0d8a02ec557f2c3ea6fb38a4abb51ba68e9ff21895
  summary: >-
    You'll create and verify C2PA Content Credentials for a sample image on an Arm device.
    First, you'll prepare an unsigned image and sign a separate copy with the C2PA Tool development
    credential. Then, you'll inspect the manifest and distinguish signature, content-binding, and
    signer-trust results. You'll compare the provenance of the image in the Content Authenticity Initiative (CAI) web validator.
    Finally, you'll modify a copy and identify the resulting content-binding failure.
#   faqs:
#   - question: Which files do I need before signing the image?
#     answer: >-
#       Keep the unsigned `image.jpg` and your `manifest.json` definition in the same `c2pa-demo`
#       directory. Run the signing command from that directory so you can use their filenames
#       without full paths.
#   - question: How do I read the C2PA Tool result for the signed image?
#     answer: >-
#       Check `claimSignature.validated` for the signature and `assertion.dataHash.match` for the
#       image binding. You'll also see `signingCredential.untrusted` because the example uses a
#       development certificate. Read these codes alongside the `Valid` validation state.
#   - question: Does signing overwrite my original image?
#     answer: >-
#       No. You write the signed copy to `image-signed.jpg`, leaving the unsigned `image.jpg`
#       unchanged.
#   - question: What should I compare in the CAI web validator?
#     answer: >-
#       Open `image-signed.jpg` and compare its displayed origin, creation action, and issuer
#       with your C2PA Tool report. You'll see an **Unrecognized** issuer warning for the
#       development credential. The web panel doesn't show separate signature or binding
#       status codes.
#   - question: How do I identify a content-binding failure after changing the image?
#     answer: >-
#       Check `image-modified.jpg` in the web validator for an **Invalid** status. In the
#       C2PA Tool report, `assertion.dataHash.mismatch` identifies the failed image binding,
#       while `claimSignature.validated` shows that the unchanged claim signature still verifies.
# END generated_summary_faq

author:
    - Kostiantyn Perehuda
    - Yogesh Deshpande

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Security
armips:
    - Cortex-A
tools_software_languages:
    - Content Credentials
    - C2PA Tool
    - ExifTool
    - libjpeg-turbo
operatingsystems:
    - Linux
    - macOS
    - Windows

further_reading:
    - resource:
        title: C2PA technical specification
        link: https://c2pa.org/specifications/
        type: documentation
    - resource:
        title: C2PA Tool source repository
        link: https://github.com/contentauth/c2patool
        type: repository

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
