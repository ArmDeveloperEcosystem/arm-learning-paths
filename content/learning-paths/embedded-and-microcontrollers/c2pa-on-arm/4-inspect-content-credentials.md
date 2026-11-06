---
title: Inspect Content Credentials
description: Inspect a signed JPEG with C2PA Tool and ExifTool to connect its stored provenance with signature, content-binding, and signer-trust results.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Display the manifest report

Now that you've created a signed copy of the sample image, you can inspect the credentials of the copy. 

Inspect the signed image to see the recorded provenance and the reported signature, content-binding,
and signer-trust results. 

Run the Coalition for Content Provenance and Authenticity (C2PA) Tool to display its JSON manifest report:

```console
c2patool image-signed.jpg
```

C2PA Tool validates the manifest while reading it. The tool includes those results in the report alongside
the recorded provenance fields.

To save the report as a JSON file, redirect the output:

```console
c2patool image-signed.jpg > report.json
```

This writes the report to `report.json` in your working directory, replacing that file if
it already exists. You can open the file in a text editor if necessary. The signed image remains unchanged.

## Find the active manifest

Find `active_manifest`, locate the same label under `manifests`, and inspect
`claim_generator_info`:

```output
"claim_generator_info": [
  {
    "name": "Arm Learning Path C2PA Example",
    "version": "1.0.0",
    "com.arm.learning_path.tool": {
      "name": "c2patool",
      "version": "0.27.21"
    },
    "org.contentauth.c2pa_rs": "0.90.21"
  }
]
```

The name and `1.0.0` example version match the values that you supplied in `manifest.json`. The custom
`com.arm.learning_path.tool` field records the separate tool name and version that you supplied. 

C2PA Tool adds `org.contentauth.c2pa_rs` to identify its underlying library. `0.90.21` is the library version in the
tested tool. 

Manifest labels, instance IDs, and UUIDs differ between runs.

## Inspect the assertions

The `assertions` array contains a `c2pa.actions.v2` assertion:

```output
"actions": [
  {
    "action": "c2pa.created",
    "digitalSourceType": "http://cv.iptc.org/newscodes/digitalsourcetype/digitalCapture"
  }
]
```

This is a declaration supplied by the claim generator. It's not independent proof of how the depicted scene
was produced or whether the scene is truthful.

## Inspect the hard binding

Under `validation_results`, `activeManifest`, and `success`, find:

```output
{
  "code": "assertion.dataHash.match",
  "explanation": "data hash valid"
}
```

For this JPEG and tool version, the data-hash assertion provides the hard binding between the manifest
and the image. `assertion.dataHash.match` reports that C2PA Tool successfully checked that binding.

## Inspect the signature and credential

Under `manifests`, open the object whose label matches `active_manifest`, then locate
`signature_info`. 

The expected output includes:

```output
"signature_info": {
  "alg": "Es256",
  "issuer": "C2PA Test Signing Cert",
  "common_name": "C2PA Signer"
}
```

Under `validation_results.activeManifest.success`, find `claimSignature.validated` to confirm
that the claim signature verifies. 

Under `validation_results.activeManifest.failure`, the expected output includes:

```output
{
  "code": "signingCredential.untrusted",
  "explanation": "signing certificate untrusted"
}
```

Keep the following checks separate:

- `claimSignature.validated` indicates that the cryptographic signature on the claim is verified.
- `assertion.dataHash.match` reports that C2PA Tool successfully checked the hard binding to the image.
- `signingCredential.untrusted` indicates that the validator trust policy doesn't accept the certificate.

A verifying signature doesn't, on its own, establish who controls the corresponding private key.

## Interpret the result

For this fixture, C2PA Tool also prints:

```output
"validation_state": "Valid"
```

`Valid` refers to the structural and cryptographic integrity of the C2PA manifest store. C2PA Tool
can read its structure and successfully check the claim signature, referenced assertion hashes,
and binding to the image. 

The result describes the integrity of the provenance record and its connection to this image. It doesn't describe the truth of the image or the recorded assertions.

Read this summary together with the individual status codes. Here, `signingCredential.untrusted`
means that the signing certificate isn't accepted by the configured trust policy of the tool. This is despite
the integrity checks succeeding.

The tool distinguishes `Valid` from `Trusted`, which additionally requires acceptance of the signing credential under that policy.

You might also find `signingCredential.ocsp.skipped` under
`validation_results.activeManifest.informational`. This means that online certificate-status
fetching through the Online Certificate Status Protocol (OCSP) was skipped. 

The `Valid` result doesn't establish that an online revocation check succeeded. Read the result alongside the individual
status codes.

## Locate the C2PA structures inside the JPEG

The JSON report is a readable interpretation of the embedded data, not its storage format. In this
JPEG, the C2PA manifest store is carried in application metadata segments called APP11 segments.
A large store can span several segments. Within that store, JPEG Universal Metadata Box
Format (JUMBF) organises the data into nested, labelled containers called boxes. Each manifest contains an
assertion store, a claim, and a claim signature. For more information, see the
[C2PA JPEG storage specification](https://spec.c2pa.org/specifications/specifications/2.4/specs/ContentCredentials.html#_embedding_manifests_into_jpeg).

ExifTool is a command-line utility for reading and writing file metadata. Use its read-only
inspection commands to connect the fields in `report.json` with the structures stored in
`image-signed.jpg`. For installation instructions, see the [ExifTool install guide](/install-guides/exiftool/).

Start by listing the JUMBF labels:

```console
exiftool -a -G3 -s -JUMDLabel image-signed.jpg
```

`-a` includes repeated labels, `-G3` shows their document hierarchy, and `-s` prints tag names.

Look for the following labels:

| Label | What to identify |
| --- | --- |
| `c2pa` | The manifest store |
| `urn:c2pa:…` | The manifest label matching `active_manifest` in `report.json` |
| `c2pa.assertions` | The assertion store, containing `c2pa.actions.v2` and the `c2pa.hash.data` assertion that provides the hard binding to this JPEG |
| `c2pa.claim.v2` | The claim that references the assertions and signature |
| `c2pa.signature` | The claim-signature container |

## Trace the stored assertions, hard binding, and claim

ExifTool verbose listing lets you trace how the following components connect within the nested JUMBF boxes of the image:

- Recorded actions
- Hard-binding parameters
- Claim references  

This view exposes the stored metadata behind the fields in the C2PA Tool report. You can save the metadata to `metadata.txt` and explore it in a text editor:

```console
exiftool -v2 image-signed.jpg > metadata.txt
```

The following entries help connect the stored metadata with the C2PA Tool report:

- `JPEG APP11` contains the JUMBF structure whose outer label is `c2pa`, identifying the embedded
  manifest store.
- Under `c2pa.actions.v2`, the decoded `c2pa.created` action and `digitalSourceType` correspond to
  the declaration in `manifest.json` and the action shown in `report.json`.
- Under `c2pa.hash.data`, `Alg = sha256` identifies the hard-binding hash algorithm.
  `ExclusionsStart` and `ExclusionsLength` describe the byte range omitted from hashing. The stored
  hash appears as binary data without its value expanded.
- Under `c2pa.claim.v2`, assertion references point into `c2pa.assertions`. The `signature`
  reference ends in `c2pa.signature`, the label of the claim-signature container.

The claim and action values are stored in CBOR, a compact binary encoding that ExifTool decodes for
this listing. This view reveals the stored structures and their connections. It doesn't verify the
C2PA signature or content binding. The image remains unchanged.

## What you've accomplished and what's next

You've inspected the recorded provenance, distinguished signature and content-binding results from
signer trust, and traced the report's fields to the structures inside the JPEG. The development
credential remains untrusted; reading these records does not establish that their assertions are true.

Keep `image-signed.jpg` unchanged, along with `report.json` and `metadata.txt`. 

Next, you'll use an external validator to examine the same signed image. You'll interpret the results of the validator under its trust policy.
