---
title: Run a vision retail shelf audit with MNN Omni
weight: 5
layout: learningpathall
---

## Introduction

This section shows how Armv9 can run lightweight operational vision reasoning locally without requiring cloud round trips, making it a practical fit for store-side restocking workflows.

The goal is not to produce SKU-level counting. Instead, you generate an operational signal that is useful for store staff:

- estimate shelf coverage for the **top**, **middle**, and **bottom** levels
- identify the **priority zone** that appears most sparse
- provide a short reason based on visible evidence
- return `NOT_SURE` when the image is unclear

This keeps the task practical for on-device multimodal inference. In many retail workflows, deciding **where to restock first** is more useful than attempting perfect item counting from a single photo.

By the end of this section, you will produce a structured shelf audit signal from a local image and verify that it can guide a restocking decision

## Prepare the image asset

Create a local directory for assets:

```bash
mkdir -p ~/mnn/assets
```

Download the tutorial image and verify that it is a valid JPEG file:

```bash
wget -P ~/mnn/assets https://upload.wikimedia.org/wikipedia/commons/e/e6/Pet_Food_Aisle.jpg
file ~/mnn/assets/Pet_Food_Aisle.jpg
```

You should see output similar to:

```text
JPEG image data, JFIF standard 1.02, resolution (DPI), density 72x72, segment length 16, Exif Standard: [TIFF image data, little-endian, direntries=12, description=                               , manufacturer=SONY, model=DSC-W50, orientation=upper-left, xresolution=203, yresolution=211, resolutionunit=2, software=Adobe Photoshop CS Macintosh, datetime=2007:04:10 17:45:47], progressive, precision 8, 2816x2112, components 3
```

This confirms that the image asset is ready for the vision prompt.

![image1 Pet Food Aisle](pet_food_aisle.jpg)

## Create the vision prompt

Next, create a prompt that instructs the model to audit only the main shelf on the left side of the image.

The prompt does four things:

- attaches the local image with `<img>...</img>`
- limits the analysis to the main left shelf
- asks for coverage estimates using `high`, `medium`, or `low`
- constrains the response to a single structured line

Create the prompt file:

```bash
cat > ~/mnn/prompt_picture_coverage.txt <<'EOF'
<img>/home/radxa/mnn/assets/Pet_Food_Aisle.jpg</img> You are an on-device retail shelf auditing assistant. Audit ONLY the main left shelf (ignore the aisle on the right, hanging toys, and floor items). Do NOT count every item. Estimate facing coverage for top/middle/bottom as high|medium|low and identify the sparsest zone. Output ONE line only using bullet-style segments separated by semicolons: Shelf audit; - Coverage: top=<high|medium|low>, middle=<high|medium|low>, bottom=<high|medium|low>; - Priority zone: <top|middle|bottom>-<left|center|right>; - Reason: <one short sentence>; - Notes: <NOT_SURE if unclear>.
EOF
```

If your username or home directory is different, replace `/home/radxa` with the correct local path.

## Run the vision demo

Run `llm_demo` with the model `config.json` file and the vision prompt:

```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json ~/mnn/prompt_picture_coverage.txt
```

You should see output similar to:

```text
config path is /home/radxa/mnn/Qwen2.5-Omni-7B-MNN/config.json
CPU Group: [ 1  2  3  4 ], 799999 - 1800968
CPU Group: [ 7  8 ], 799897 - 2199795
CPU Group: [ 5  6 ], 799897 - 2299896
CPU Group: [ 9  10 ], 799897 - 2399998
CPU Group: [ 0  11 ], 799897 - 2500100
The device supports: i8sdot:1, fp16:1, i8mm: 1, sve2: 1, sme2: 0
main, 274, cost time: 6046.771973 ms
Prepare for tuning opt Begin
Prepare for tuning opt End
main, 282, cost time: 766.086975 ms
prompt file is /home/radxa/mnn/prompt_picture_coverage.txt
Shelf audit; - Coverage: top=high, middle=high, bottom=medium; - Priority zone: top-left; - Reason: top and middle have more variety than bottom, and left is where most items are; - Notes: NOT_SURE if unclear. How does this sound? Let me know if you need further clarification or have other questions! I'm here to help with more details if you want! 😊
If you have any other questions about this shelf auditing, feel free to let me know! 😊
```

The exact wording can vary, but the response should still follow the requested structure.

## Why a coarse coverage estimate is enough for edge workflows

In many edge retail workflows, you do not need a perfectly precise inventory measurement to make a useful decision. A coarse estimate such as `High`, `Medium`, or `Low` coverage is often enough to identify which shelf area needs attention first and to generate a practical restocking signal.

This keeps the prompt and output simple, reduces post-processing requirements, and makes the result easier to validate during early on-device prototyping. For this Learning Path, the goal is not to build a full inventory counting system, but to show how local vision reasoning on Armv9 can produce an operationally useful input for a restocking workflow.

## Verify the result

Check that the output meets these conditions:

- it includes coverage estimates for **top**, **middle**, and **bottom**
- it identifies one **priority zone**, such as `middle-center`
- it provides a short reason tied to visible shelf sparsity
- it uses `NOT_SURE` only when the image is genuinely ambiguous

If the model returns extra conversational text, tighten the prompt further by repeating `Output ONE line only`.

## Next steps

You have now validated image-based multimodal inference with MNN Omni on Armv9.

In the next section, you extend this workflow by running an audio-based restock instruction demo using an `<audio>...</audio>` prompt.
