---
title: ModelScope - Open-Source AI Pre-trained AI models hub
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

To follow the instructions for this Learning Path, you will need an Arm server running Ubuntu 22.04 LTS or later version with at least 16 cores, 16GB of RAM, and 50GB of disk storage.

## Introduce ModelScope
ModelScope is an open-source platform offering a vast collection of pre-trained AI models, including those specifically designed for ASR. Key benefits of ModelScope include:

* **Model Diversity:** 
    Access a wide range of models for various tasks, including ASR, natural language processing, and computer vision.

* **Ease of Use:** 
    ModelScope provides a user-friendly interface and APIs for seamless model integration.

* **Community Support:** 
    Benefit from a vibrant community of developers and researchers contributing to and supporting ModelScope.


## Arm CPU Acceleration
ModelScope fully support Pytorch 1.8+ and other machine learing framework which can be efficiently deployed on Arm Neoverse CPUs, taking advantage of Arm's performance and power-efficiency characteristics. 

Arm provides optimized software and tools, such as the Kleidi, to accelerate AI inference on Arm-based platforms. 

This makes Arm Neoverse CPUs an ideal choice for running ModelScope models in edge devices and other resource-constrained environments.

You can learn more about [Faster PyTorch Inference using Kleidi on Arm Neoverse](https://community.arm.com/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/faster-pytorch-inference-kleidi-arm-neoverse) from Arm community website.


## Installing ModelScope

First, ensure your system is up-to-date and install the required tools and libraries:

```bash
sudo apt-get update -y
sudo apt-get install -y curl git wget python3 python3-pip python3-venv python-is-python3 
```

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

Install related packages: 
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip3 install numpy packaging addict datasets simplejson sortedcontainers transformers

```
{{% notice Note %}}
This learning path will use execute model in Arm Neoverse, so we only need install PyTorch CPU package.
{{% /notice %}}

## Create a sample example.

After completing the installation, we will use an example related to Chinese semantic understanding to illustrate how to use ModelScope.

There is a fundamental difference between Chinese and English writing. The relationship between Chinese characters and their meanings is somewhat analogous to the difference between words and phrases in English. Some Chinese characters, like English words, have clear meanings on their own, such as "人" (person), "山" (mountain), and "水" (water).

However, more often, Chinese characters need to be combined with other characters to express more complete meanings, just like phrases in English. For example, "祝福" (blessing) can be broken down into "祝" (wish) and "福" (good fortune); "分享" (share) can be broken down into "分" (divide) and "享" (enjoy); "生成" (generate) is composed of "生" (produce) and "成" (become).

For computers to understand Chinese sentences, we need to understand the rules of Chinese characters, vocabulary, and grammar to accurately understand and express meaning.

Here ia a simple example using a general-domain Chinese word segmentation [model(https://www.modelscope.cn/models/iic/nlp_structbert_word-segmentation_chinese-base)], which can break down Chinese sentences into individual words, facilitating analysis and understanding by computers.

```python
from modelscope.pipelines import pipeline

word_segmentation = pipeline ('word-segmentation',model='damo/nlp_structbert_word-segmentation_chinese-base')
text = '一段新年祝福的文字跟所有人分享 ...'
result = word_segmentation(text)

print(result)
```

The output will be like this:
```output
{'output': ['一', '段', '新年', '祝福', '的', '文字', '跟', '所有', '人', '分享']}
```

The segmentation model has correctly identified the following words:

- 一 (one): This is a numeral.

- 段 (piece): This is a measure word used for text.

- 新年 (New Year): This is a noun phrase meaning "New Year."

- 祝福 (blessings): This is a noun meaning "blessings" or "good wishes."

- 的 (of): This is a possessive particle.

- 文字 (text): This is a noun meaning "text" or "written words."

- 跟 (with): This is a preposition meaning "with."

- 所有 (all): This is a quantifier meaning "all."

- 人 (people): This is a noun meaning "people."

- 分享 (share): This is a verb meaning "to share."


The segmentation model has successfully identified the word boundaries and separated the sentence into meaningful units, which is essential for further natural language processing tasks like machine translation or sentiment analysis.

