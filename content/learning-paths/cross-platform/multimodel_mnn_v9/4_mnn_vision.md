---
title: Run a vision retail shelf audit with MNN Omni
weight: 5
layout: "learningpathall"
---

## Scenario

In this module you will implement a **smart retail shelf audit** using a single local image.

The model will:

- Inspect a **pet food aisle** image
- Estimate **facing coverage** for three shelf levels: **top / middle / bottom**
- Identify a **priority zone** that appears most sparse
- Use `NOT_SURE` where the image is ambiguous


## Assets

Create an `assets` directory:

```bash
mkdir -p ~/mnn_lp/assets
```

Download the tutorial image:

```bash
curl -L -o ~/mnn_lp/assets/pet_food_aisle.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/5/57/Pet_Food_Aisle.jpg"

file ~/mnn_lp/assets/pet_food_aisle.jpg
```

The `file` command confirms that this is a valid JPEG image.


## Prompt design

You will design a prompt that:

- Uses `<img>…</img>` to attach the local image
- Restricts the model to auditing **only the main left shelf**
- Requests coverage as **high/medium/low** for each level
- Asks for a single **priority zone** on the left shelf
- Encodes the output as a **single line** with `;`-separated segments

Create the prompt file (adjust `/home/radxa` to your actual user home if needed):

```bash
cat > ~/mnn_lp/prompt_picture_coverage.txt <<'EOF'
<img>/home/radxa/mnn_lp/assets/pet_food_aisle.jpg</img> You are an on-device retail shelf auditing assistant. Audit ONLY the main left shelf (ignore the aisle on the right, hanging toys, and floor items). Do NOT count every item. Estimate facing coverage for top/middle/bottom as high|medium|low and identify the sparsest zone. Output ONE line only using bullet-style segments separated by semicolons: Shelf audit; - Coverage: top=<high|medium|low>, middle=<high|medium|low>, bottom=<high|medium|low>; - Priority zone: <top|middle|bottom>-<left|center|right>; - Reason: <one short sentence>; - Notes: <NOT_SURE if unclear>.
EOF
```

Run the vision demo:

```bash
cd ~/mnn_lp/MNN/build
./llm_demo ~/mnn_lp/Qwen2.5-Omni-7B-MNN/config.json ~/mnn_lp/prompt_picture_coverage.txt
```


## Checkpoint

You have completed this module when the output:

- Includes coverage estimates for **top / middle / bottom**
- Identifies a **priority zone** such as `middle-center`
- Provides a **short reason** that clearly references visible sparsity on the shelf
- Uses `NOT_SURE` only where the image is genuinely unclear