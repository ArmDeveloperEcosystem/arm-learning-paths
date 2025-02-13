---
title: ModelScope - Open-Source Pre-trained AI models hub
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

To follow the instructions for this Learning Path, you will need an Arm based server running Ubuntu 22.04 LTS or later version with at least 8 cores, 16GB of RAM, and 30GB of disk storage.

## Introduce ModelScope
[ModelScope](https://github.com/modelscope/modelscope/) is an open-source platform that makes it easy to use AI models in your applications. 
It provides a wide variety of pre-trained models for tasks like image recognition, natural language processing, and audio analysis. With ModelScope, you can easily integrate these models into your projects with just a few lines of code.

Key benefits of ModelScope include:

* **Model Diversity:** 
    Access a wide range of models for various tasks, including ASR, natural language processing, and computer vision.

* **Ease of Use:** 
    ModelScope provides a user-friendly interface and APIs for seamless model integration.

* **Community Support:** 
    Benefit from a vibrant community of developers and researchers contributing to and supporting ModelScope.


## Arm CPU Acceleration
ModelScope fully supports Pytorch 1.8+ and other machine learning frameworks, which can be efficiently deployed on Arm Neoverse CPUs, taking advantage of Arm's performance and power-efficiency characteristics.

Arm provides optimized software and tools, such as Kleidi, to accelerate AI inference on Arm-based platforms. This makes Arm Neoverse CPUs an ideal choice for running ModelScope models in edge devices and other resource-constrained environments.

You can learn more about [Faster PyTorch Inference using Kleidi on Arm Neoverse](https://community.arm.com/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/faster-pytorch-inference-kleidi-arm-neoverse) from Arm community website.


## Install ModelScope and PyTorch

First, ensure your system is up-to-date and install the required tools and libraries:

```bash
sudo apt-get update -y
sudo apt-get install -y curl git wget python3 python3-pip python3-venv python-is-python3 ffmpeg
```

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

In your active virtual environment, install modelscope:

```bash
pip3 install modelscope
```

Install PyTorch and related python dependencies: 
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip3 install numpy packaging addict datasets simplejson sortedcontainers transformers ffmpeg

```
{{% notice Note %}}
In this learning path you will execute models on the Arm Neoverse CPU, so you will only need to install the PyTorch CPU package.
{{% /notice %}}

## Create a sample example

You can now run an example to understand how to use ModelScope for understanding Chinese semantics.

There is a fundamental difference between Chinese and English writing. 
The relationship between Chinese characters and their meanings is somewhat analogous to the difference between words and phrases in English. 
Some Chinese characters, like English words, have clear meanings on their own, such as “人” (person), “山” (mountain), and “水” (water).

However, more often, Chinese characters need to be combined with other characters to express more complete meanings, just like phrases in English. 
For example, “祝福” (blessing) can be broken down into “祝” (wish) and “福” (good fortune); “分享” (share) can be broken down into “分” (divide) and “享” (enjoy); “生成” (generate) is composed of “生” (produce) and “成” (become).

For computers to understand Chinese sentences, you will need to understand the rules of Chinese characters, vocabulary, and grammar to accurately understand and express meaning.

In this simple example, you will use a general-domain Chinese [word segmentation model](https://www.modelscope.cn/models/iic/nlp_structbert_word-segmentation_chinese-base) to break down Chinese sentences into individual words, facilitating analysis and understanding by computers.

Using a file editor of your choice, copy the code shown below into a file named `segmentation.py`:

```python
from modelscope.pipelines import pipeline

word_segmentation = pipeline (
    'word-segmentation',
    model='damo/nlp_structbert_word-segmentation_chinese-base'
)
text = '一段新年祝福的文字跟所有人分享'
result = word_segmentation(text)

print(result)
```

This piece of code specifies a model and provides a Chinese sentence for the model to segment.
"A New Year’s greeting message to share with everyone."

Run the model inference on the sample text:

```bash
python3 segmentation.py
```

The output should look like this:
```output
2025-01-28 00:30:29,692 - modelscope - WARNING - Model revision not specified, use revision: v1.0.3
Downloading Model to directory: /home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base
2025-01-28 00:30:32,828 - modelscope - WARNING - Model revision not specified, use revision: v1.0.3
2025-01-28 00:30:33,332 - modelscope - INFO - initiate model from /home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base
2025-01-28 00:30:33,333 - modelscope - INFO - initiate model from location /home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base.
2025-01-28 00:30:33,334 - modelscope - INFO - initialize model from /home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base
You are using a model of type bert to instantiate a model of type structbert. This is not supported for all configurations of models and can yield errors.
2025-01-28 00:30:35,522 - modelscope - WARNING - No preprocessor field found in cfg.
2025-01-28 00:30:35,522 - modelscope - WARNING - No val key and type key found in preprocessor domain of configuration.json file.
2025-01-28 00:30:35,522 - modelscope - WARNING - Cannot find available config to build preprocessor at mode inference, current config: {'model_dir': '/home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base'}. trying to build by task and model information.
2025-01-28 00:30:35,527 - modelscope - INFO - cuda is not available, using cpu instead.
2025-01-28 00:30:35,529 - modelscope - WARNING - No preprocessor field found in cfg.
2025-01-28 00:30:35,529 - modelscope - WARNING - No val key and type key found in preprocessor domain of configuration.json file.
2025-01-28 00:30:35,529 - modelscope - WARNING - Cannot find available config to build preprocessor at mode inference, current config: {'model_dir': '/home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base', 'sequence_length': 512}. trying to build by task and model information.
/home/ubuntu/venv/lib/python3.10/site-packages/transformers/modeling_utils.py:1044: FutureWarning: The `device` argument is deprecated and will be removed in v5 of Transformers.
  warnings.warn(
{'output': ['生成', '一', '段', '新年', '祝福', '的', '文字', '跟', '所有', '人', '分享']}
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
