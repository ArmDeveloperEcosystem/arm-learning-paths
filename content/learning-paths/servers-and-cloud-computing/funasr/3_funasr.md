---
title: Building ASR Applications with ModelScope
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is FunASR?

[FunASR](https://github.com/modelscope/FunASR) is an open-source toolkit designed for speech recognition research and application development. It provides a comprehensive set of tools and functionalities for building and deploying ASR applications.


## Installing FunASR
Install FunASR using the following pip command:

```bash
pip3 install funasr==1.2.3
```
{{% notice Note %}}
The examples in this Learning Path use FunASR version 1.2.3. Results might vary with other versions.
{{% /notice %}}

## Speech Recognition
FunASR offers a simple interface for performing speech recognition tasks. You can easily transcribe audio files or implement real-time speech recognition using FunASR's functionalities. In this Learning Path, you will learn how to leverage FunASR to implement a speech recognition application.

To get started, let's use an English speech sample for audio transcription. Create a file named `funasr_test1.py` and add the following code:

```python
from funasr import AutoModel

model = AutoModel(
    model="paraformer", 
    device="cpu", 
    hub="ms"
)
res = model.generate(input="https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_en.wav")
print(f"\nResult: \n{res[0]['text']}")
```

### Code Breakdown

Before running this script, you can break it down:

The imported `AutoModel()` class serves as an interface for loading various AI models.

#### Key Parameters

* `model="paraformer"`: Specifies the model you want to load. In this example you will load the Paraformer model, which is an end-to-end automatic speech recognition (ASR) model optimized for real-time transcription.
    
* `device="cpu"`: Specifies that the model runs on the CPU. It does not require a GPU.

* `hub="ms"`: Indicates that the model is sourced from the "ms" (ModelScope) hub.

#### Processing the Audio

* `model.generate()`: function processes an audio file and generates a transcribed text output.

* `input="..."`: The input is a `.wav` audio file URL, which is a .wav file containing an English audio sample.

Since the output contains extensive data, this example focuses on extracting and displaying only the transcribed text found in res[0]['text'].

For this initial test, a two-second English audio clip from the internet will be used for Paraformer model to process the `.wav` file.

Run this Python script on your Arm-based server:

```bash
python funasr_test1.py
```

The output will look like:

```output
funasr version: 1.2.3.
Check update of funasr, and it would cost few times. You may disable it by set `disable_update=True` in AutoModel
You are using the latest version of funasr-1.2.3
Downloading Model to directory: /home/ubuntu/.cache/modelscope/hub/iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch
2025-01-27 21:24:31,014 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
2025-01-27 21:24:31,637 - modelscope - INFO - Got 9 files, start to download ...
Downloading [config.yaml]: 100%|█████████████████████████████████████████████████████████████████████| 2.45k/2.45k [00:01<00:00, 1.81kB/s]
Downloading [fig/struct.png]: 100%|██████████████████████████████████████████████████████████████████| 48.7k/48.7k [00:01<00:00, 31.7kB/s]
Downloading [example/asr_example.wav]: 100%|████████████████████████████████████████████████████████████| 173k/173k [00:01<00:00, 106kB/s]
Downloading [configuration.json]: 100%|████████████████████████████████████████████████████████████████████| 472/472 [00:01<00:00, 278B/s]
Downloading [am.mvn]: 100%|██████████████████████████████████████████████████████████████████████████| 10.9k/10.9k [00:01<00:00, 6.30kB/s]
Downloading [README.md]: 100%|███████████████████████████████████████████████████████████████████████| 19.2k/19.2k [00:01<00:00, 10.5kB/s]
Downloading [seg_dict]: 100%|████████████████████████████████████████████████████████████████████████| 7.90M/7.90M [00:02<00:00, 3.46MB/s]
Downloading [tokens.json]: 100%|█████████████████████████████████████████████████████████████████████| 91.5k/91.5k [00:01<00:00, 59.3kB/s]
Downloading [model.pt]: 100%|██████████████████████████████████████████████████████████████████████████| 840M/840M [00:22<00:00, 38.8MB/s]
Processing 9 items: 100%|██████████████████████████████████████████████████████████████████████████████| 9.00/9.00 [00:22<00:00, 2.52s/it]
2025-01-27 21:24:54,363 - modelscope - INFO - Download model 'iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch' successfully.ng [model.pt]:   2%|█▌                                                                       | 18.0M/840M [00:02<00:42, 20.4MB/s]
rtf_avg: 0.118: 100%|███████████████████████████████████████████████████████████████████████████████████████| 1/1 
[00:00<00:00,  3.80it/s]

Result:
he tried to think how it could be
```

The transcribed test shows "he tried to think how it could be". This is the expected result for the audio sample.

Now you can try an example that uses a Chinese speech recognition model. Copy the code shown below in a file named `funasr_test2.py`:

```python
import os
from funasr import AutoModel

model = AutoModel(
    model="paraformer-zh",
    device="cpu",
    hub="ms"
)

wav_file = os.path.join(model.model_path, "example/asr_example.wav")
res = model.generate(input=wav_file)

text_content = res[0]['text'].replace(" ","")
print(f"Result: \n{text_content}")

print(res)
```

This example uses an audio file from the FunASR package for speech recognition, you can see that the loaded model has been replaced with a Chinese speech recognition model that has a `-zh` suffix. 

FunASR will process each sound in the audio with appropriate character recognition.

You have also modified the output format from the previous example. In addition to recognizing the Chinese characters, you will add timestamps indicating the start and end times of each character. This is used for applications like subtitle generation and sentiment analysis.

Run the Python script:

```bash
python3 funasr_test2.py
```

The output should look like:

```output
Downloading Model to directory: /home/ubuntu/.cache/modelscope/hub/iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch
2025-01-28 02:04:44,829 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
ckpt: /home/ubuntu/.cache/modelscope/hub/iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch/model.pt
/home/ubuntu/venv/lib/python3.10/site-packages/funasr/train_utils/load_pretrained_model.py:68: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  src_state = torch.load(path, map_location=map_location)
  0%|                                                                                                                       | 0/1 [00:00<?, ?it/s]/home/ubuntu/venv/lib/python3.10/site-packages/funasr/models/paraformer/model.py:249: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with autocast(False):
rtf_avg: 0.180: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.24it/s]
Result: 
[{'key': 'asr_example', 'text': '欢 迎 大 家 来 到 么 哒 社 区 进 行 体 验', 'timestamp': [[990, 1230], [1290, 1530], [1610, 1830], [1830, 2010], [2010, 2170], [2170, 2410], [2430, 2570], [2570, 2810], [2850, 3050], [3050, 3290], [3390, 3570], [3570, 3810], [3910, 4110], [4110, 4345]]}]
```

The output shows "欢迎大家来到达摩社区进行体验" which means "Welcome everyone to the Dharma community to explore and experience!" as expected.

You can also see that the spacing between the third and sixth characters is short. This is because they are combined with other characters, as discussed in the previous section.

You can now build a speech processing pipeline. The output of the speech recognition module serves as the input for the semantic segmentation model, enabling you to validate the accuracy of the recognized results. Copy the code shown below in a file named `funasr_test3.py`:

```python
from funasr import AutoModel
from modelscope.pipelines import pipeline
import os

model = AutoModel(
    model="paraformer-zh",
    device="cpu",
    hub="ms"
)

word_segmentation = pipeline (
    'word-segmentation',
    model='damo/nlp_structbert_word-segmentation_chinese-base'
)

wav_file = os.path.join(model.model_path, "example/asr_example.wav")
res = model.generate(input=wav_file)

text_content = res[0]['text'].replace(" ","")
seg_result = word_segmentation(text_content)

print(f"Result: \n{seg_result}")
```
Run this Python script:

```bash
python3 funasr_test3.py
```

The output should look like:

```output
Downloading Model to directory: /home/ubuntu/.cache/modelscope/hub/iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch
2025-01-28 02:06:11,421 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
ckpt: /home/ubuntu/.cache/modelscope/hub/iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch/model.pt
/home/ubuntu/venv/lib/python3.10/site-packages/funasr/train_utils/load_pretrained_model.py:68: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  src_state = torch.load(path, map_location=map_location)
2025-01-28 02:06:16,778 - modelscope - WARNING - Model revision not specified, use revision: v1.0.3
Downloading Model to directory: /home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base
2025-01-28 02:06:20,486 - modelscope - WARNING - Model revision not specified, use revision: v1.0.3
2025-01-28 02:06:20,970 - modelscope - INFO - initiate model from /home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base
2025-01-28 02:06:20,970 - modelscope - INFO - initiate model from location /home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base.
2025-01-28 02:06:20,971 - modelscope - INFO - initialize model from /home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base
You are using a model of type bert to instantiate a model of type structbert. This is not supported for all configurations of models and can yield errors.
2025-01-28 02:06:23,029 - modelscope - WARNING - No preprocessor field found in cfg.
2025-01-28 02:06:23,029 - modelscope - WARNING - No val key and type key found in preprocessor domain of configuration.json file.
2025-01-28 02:06:23,029 - modelscope - WARNING - Cannot find available config to build preprocessor at mode inference, current config: {'model_dir': '/home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base'}. trying to build by task and model information.
2025-01-28 02:06:23,034 - modelscope - INFO - cuda is not available, using cpu instead.
2025-01-28 02:06:23,035 - modelscope - WARNING - No preprocessor field found in cfg.
2025-01-28 02:06:23,036 - modelscope - WARNING - No val key and type key found in preprocessor domain of configuration.json file.
2025-01-28 02:06:23,036 - modelscope - WARNING - Cannot find available config to build preprocessor at mode inference, current config: {'model_dir': '/home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base', 'sequence_length': 512}. trying to build by task and model information.
  0%|                                                                                                                       | 0/1 [00:00<?, ?it/s]/home/ubuntu/venv/lib/python3.10/site-packages/funasr/models/paraformer/model.py:249: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with autocast(False):
rtf_avg: 0.180: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.23it/s]
/home/ubuntu/venv/lib/python3.10/site-packages/transformers/modeling_utils.py:1044: FutureWarning: The `device` argument is deprecated and will be removed in v5 of Transformers.
  warnings.warn(
Result: 
{'output': ['欢迎', '大家', '来到', '达摩', '社区', '进行', '体验']}
```

The segmentation of the sentence “欢迎大家来到达摩社区进行体验” into ‘欢迎’, ‘大家’, ‘来到’, ‘达摩’, ‘社区’, ‘进行’, ‘体验’. 

Each segment represents a meaningful unit in the sentence, preserving the grammatical structure and readability.
- “欢迎” (welcome) and “大家” (everyone) form a natural greeting.
- “来到” (come to) introduces the location “达摩社区” (Damo Community) as a whole.
- “进行” (carry out) and “体验” (experience) together indicate the purpose of visiting.

Good, the result is exactly what you are looking for.

## Paraformer: Fast and Accurate Parallel Transformer for Non-autoregressive End-to-End Speech Recognition

[Paraformer](https://aclanthology.org/2020.wnut-1.18/) is a novel architecture for automatic speech recognition (ASR) designed for both speed and accuracy. Unlike traditional models, it leverages a parallel transformer architecture, enabling simultaneous processing of multiple parts of the input speech. This parallel processing capability leads to significantly faster inference, making Paraformer well-suited for real-time ASR applications where responsiveness is crucial.  

Furthermore, Paraformer has demonstrated state-of-the-art accuracy on several benchmark datasets, showcasing its effectiveness in accurately transcribing speech. This combination of speed and accuracy makes Paraformer a promising advancement in the field of ASR, opening up new possibilities for high-performance speech recognition systems.

Paraformer has been fully integrated into FunASR. Copy the sample program shown below into a file named `paraformer.py`.

This example uses a PyTorch-optimized Paraformer model from ModelScope. The program first checks if the test audio file has been downloaded.


```python
import os
import requests
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

inference_pipeline = pipeline(
    task=Tasks.auto_speech_recognition,
    model='iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch',
    device="cpu",
    hub="ms",
    model_revision="v2.0.4"
)

url = 'https://github.com/liangstein/Chinese-speech-to-text/blob/master/3.wav?raw=true'
filename = 'paraformer1.wav'

if not os.path.exists(filename):
    # If the file does not exist, download it
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    print(f"File {filename} downloaded.")
else:
    print(f"File {filename} already exists.")

rec_result = inference_pipeline(input=filename)

print(f"\nResult: \n{rec_result[0]['text']}")
```
Run this Python script

```bash
python3 paraformer.py
```

The output should look like:

```output
2025-01-28 00:03:24,373 - modelscope - INFO - Use user-specified model revision: v2.0.4
Downloading Model to directory: /home/ubuntu/.cache/modelscope/hub/iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch
2025-01-28 00:03:27,738 - modelscope - INFO - Use user-specified model revision: v2.0.4
2025-01-28 00:03:28,251 - modelscope - INFO - initiate model from /home/ubuntu/.cache/modelscope/hub/iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch
2025-01-28 00:03:28,252 - modelscope - INFO - initiate model from location /home/ubuntu/.cache/modelscope/hub/iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch.
2025-01-28 00:03:28,253 - modelscope - INFO - initialize model from /home/ubuntu/.cache/modelscope/hub/iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch
ckpt: /home/ubuntu/.cache/modelscope/hub/iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch/model.pt
/home/ubuntu/venv/lib/python3.10/site-packages/funasr/train_utils/load_pretrained_model.py:68: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  src_state = torch.load(path, map_location=map_location)
2025-01-28 00:03:31,830 - modelscope - WARNING - No preprocessor field found in cfg.
2025-01-28 00:03:31,830 - modelscope - WARNING - No val key and type key found in preprocessor domain of configuration.json file.
2025-01-28 00:03:31,831 - modelscope - WARNING - Cannot find available config to build preprocessor at mode inference, current config: {'model_dir': '/home/ubuntu/.cache/modelscope/hub/iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch'}. trying to build by task and model information.
2025-01-28 00:03:31,831 - modelscope - WARNING - No preprocessor key ('funasr', 'auto-speech-recognition') found in PREPROCESSOR_MAP, skip building preprocessor.
File test1.wav already exists.
  0%|                                                                                                                       | 0/1 [00:00<?, ?it/s]/home/ubuntu/venv/lib/python3.10/site-packages/funasr/models/paraformer/model.py:249: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with autocast(False):
/home/ubuntu/venv/lib/python3.10/site-packages/funasr/models/paraformer/cif_predictor.py:212: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with autocast(False):
rtf_avg: 0.048: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.33it/s]

Result: 
飞机穿过云层眼下一片云海有时透过稀薄的云雾依稀可见南国葱绿的群山大地
```

The output shows "飞机穿过云层眼下一片云海有时透过稀薄的云雾依稀可见南国葱绿的群山大地" as expected.


## Punctuation Restoration

In the previous example, the speech of each word was correctly recognized, but it lacked punctuation. The lack of punctuation hinders our understanding of the speaker's intended expression.

You can add a [Punctuation Restoration model](https://aclanthology.org/2020.wnut-1.18/) responsible for punctuation as the next step in processing your audio workload.

In addition to using the Paraformer model, you will add two more ModelScope models:
- VAD ([Voice Activity Detection](https://modelscope.cn/models/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch/summary)) and 
- PUNC ([Punctuation Restoration](https://modelscope.cn/models/iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch/files)) 

This ensures the punctuation aligns with the semantics of the speech recognition. Copy the updated code shown below in a file named `paraformer-2.py`:

```python
import os
import requests
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

inference_pipeline = pipeline(
    task=Tasks.auto_speech_recognition,
    model='iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch', 
    model_revision="v2.0.4", 
    device="cpu", 
    hub="ms",
    vad_model='iic/speech_fsmn_vad_zh-cn-16k-common-pytorch', vad_model_revision="v2.0.4",
    punc_model='iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch', punc_model_revision="v2.0.4",
    # spk_model="iic/speech_campplus_sv_zh-cn_16k-common",
    # spk_model_revision="v2.0.2",
)

url = 'https://github.com/liangstein/Chinese-speech-to-text/blob/master/3.wav?raw=true'
filename = 'paraformer1.wav'

if not os.path.exists(filename):
    # If the file does not exist, download it
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    print(f"File {filename} downloaded.")
else:
    print(f"File {filename} already exists.")

rec_result = inference_pipeline(input=filename)

print(f"\nResult: \n{rec_result[0]['text']}")
```

{{% notice Note %}}
vad_model_revision & punc_model_revision are optional parameters. In most cases, your models should work without specifying the version.
{{% /notice %}}

Run the updated Python script:

```bash
python3 paraformer-2.py
```


The entire speech sample is correctly segmented into four parts based on semantics.

```output
rtf_avg: 0.047: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.45it/s]
rtf_avg: -0.026: 100%|██████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 37.57it/s]
rtf_avg: 0.049, time_speech:  8.875, time_escape: 0.439: 100%|██████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.27it/s]

Result: 
飞机穿过云层，眼下一片云海，有时透过稀薄的云雾，依稀可见南国葱绿的群山大地。
```

Now you can translate this recognized result, and you can easily see that the four sentences represent different meanings.

"飞机穿过云层" means: The airplane passed through the clouds.

"眼下一片云海" means: beneath the eyes was a sea of clouds.

"有时透过稀薄的云雾" means: sometimes, through the thin clouds.

"依稀可见南国葱绿的群山大地" means: "one could vaguely see the green mountains and land of the southern country.


## Sentiment Analysis
FunASR also supports sentiment analysis of speech, allowing you to determine the emotional tone of the spoken language. 

This can be valuable for applications like customer service and social media monitoring.

You can use a mature speech emotion recognition model [emotion2vec+](https://modelscope.cn/models/iic/emotion2vec_plus_large) from ModelScope as an example.

The model identifies which of the following emotions is the closest match for the emotion expressed in the speech:
* Neutral.
* Happy.
* Sad.
* Angry.
* Unknown.

This script recognizes three different speech samples in various languages and emotions as examples.

Copy the code shown below in a file named `sentiment.py`:

```python
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

inference_pipeline = pipeline(
    task=Tasks.emotion_recognition,
    model="iic/emotion2vec_plus_large", 
    device="cpu", 
    hub="ms"
)

# Define a function to process the audio file and print the results
def process_audio_file(audio_path):
    # Run the inference pipeline
    rec_result = inference_pipeline(
        audio_path,
        granularity="utterance",
        extract_embedding=False
    )

    # Extract labels and scores
    labels = rec_result[0]['labels']
    scores = rec_result[0]['scores']

    # Sort labels by scores
    sorted_labels = [f"{label} ({score:.2f})" for label, score in sorted(zip(labels, scores), key=lambda pair: pair[1], reverse=True)]

    # Print results
    print(f"Result: {sorted_labels}")

# Process the first audio file, Chinese neutral
print(f"Neutral Chinese Speech")
process_audio_file(
    'https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav'
)

# Process the second audio file, Young happy
print(f"Happy young English voice")
process_audio_file(
    'https://utoronto.scholaris.ca/bitstreams/05a3e499-7129-4a04-9efc-893f7af21d94/download'
)

# Process the third audio file, Older angry
print(f"Angry Older English Voice")
process_audio_file(
    'https://utoronto.scholaris.ca/bitstreams/5ce257a3-be71-41a8-8d88-d097ca15af4e/download'
)

```
Run this script:

```bash
python3 sentiment.py
```

`emotion2vec+` accurately detects emotions through intonation, even without semantic understanding.

The output should look like:

```output
Neutral Chinese Speech
rtf_avg: 0.100: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.80it/s]
Result: ['中立/neutral (1.00)', '难过/sad (0.00)', '开心/happy (0.00)', '生气/angry (0.00)', '<unk> (0.00)']
Happy young English voice
rtf_avg: 1.119: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:02<00:00,  2.22s/it]
Result: ['开心/happy (1.00)', '生气/angry (0.00)', '难过/sad (0.00)', '中立/neutral (0.00)', '<unk> (0.00)']
Angry Older English Voice
rtf_avg: 1.444: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:02<00:00,  2.18s/it]
Result: ['生气/angry (1.00)', '中立/neutral (0.00)', '开心/happy (0.00)', '难过/sad (0.00)', '<unk> (0.00)']
```

You can notice that the emotions of all three speech samples are correctly recognized:
- [Neutral Chinese Speech](https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav)
- [Happy English Speech](https://utoronto.scholaris.ca/bitstreams/05a3e499-7129-4a04-9efc-893f7af21d94/download)
- [Angry English Speech](https://utoronto.scholaris.ca/bitstreams/5ce257a3-be71-41a8-8d88-d097ca15af4e/download)


## Enhance PyTorch Inference Performance on Arm Neoverse

In addition to FunASR providing comprehensive models that unlock numerous speech application possibilities, optimizing the computing platform is equally crucial.

Thanks to the Arm Neoverse SMMLA and FMMLA instruction set and deep optimizations in PyTorch, we have further reduced the execution time of the original model on the CPU.

You can learn more about [Accelerating popular Hugging Face models using Arm Neoverse
](https://community.arm.com/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/accelerating-sentiment-analysis-on-arm-neoverse-cpus) from the Arm community blog.

Let's re-test the same example based on fully optimized PyTorch package again.

### Ensure Python 3.10 is installed
First, make sure you are using Python 3.10. 

If your current Python environment is below version 3.10, please upgrade to Python 3.10.

```bash
sudo apt install python3.10 -y
```

Conversely, if your current version is above 3.10, please proceed with the installation as well.

```bash
sudo apt install python3.10 -y
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2
sudo update-alternatives --config python3
python --version
```

{{% notice Note %}}
The `update-alternatives` command is a utility in Debian-based Linux distributions, such as Ubuntu and Debian, that manages symbolic links for different software versions. It simplifies the process of switching between multiple installed versions of the same program.
{{% /notice %}}

The Python version should now be 3.10.

```output
Python 3.10.16
```

### Install PyTorch and Optimized Libraries

Now, you can install PyTorch and optimized libraries by following instructions:

```bash
git clone --recursive https://github.com/pytorch/ao.git
cd ao
git checkout 174e630af2be8cd18bc47c5e530765a82e97f45b
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/PyTorch-arm-patches/main/0001-Feat-Add-support-for-kleidiai-quantization-schemes.patch
git apply --whitespace=nowarn 0001-Feat-Add-support-for-kleidiai-quantization-schemes.patch
cd ../

git clone --recursive https://github.com/pytorch/torchchat.git
cd torchchat
git checkout 925b7bd73f110dd1fb378ef80d17f0c6a47031a6
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/PyTorch-arm-patches/main/0001-modified-generate.py-for-cli-and-browser.patch
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/PyTorch-arm-patches/main/0001-Feat-Enable-int4-quantized-models-to-work-with-pytor.patch
git apply 0001-Feat-Enable-int4-quantized-models-to-work-with-pytor.patch
git apply --whitespace=nowarn 0001-modified-generate.py-for-cli-and-browser.patch
pip install -r requirements.txt

wget https://github.com/ArmDeveloperEcosystem/PyTorch-arm-patches/raw/main/torch-2.5.0.dev20240828+cpu-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
pip install --force-reinstall torch-2.5.0.dev20240828+cpu-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
cd ..
pip uninstall torchao && cd ao/ && rm -rf build && python setup.py install
```

{{% notice Note %}}
See this Learning Path [Run a Large Language Model Chatbot on Arm servers](/learning-paths/servers-and-cloud-computing/pytorch-llama/pytorch-llama/) for further information.
{{% /notice %}}

Once you have installed the optimized PyTorch, enable bfloat16 fast math kernels by setting DNNL_DEFAULT_FPMATH_MODE.

Using AWS Graviton3 as an example, this enables GEMM kernels that use bfloat16 MMLA instructions available in the hardware.


### Update the FunASR application with benchmark function

Now you can test the FunASR model again.

By reusing the previously-named `paraformer-2.py` file and add benchmark function, copy the updated code shown below in a file named `paraformer-3.py`:

```python
import os
import time
import numpy as np
import requests
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

# Initialize the ASR pipeline
def load_pipeline(device="cpu"):
    return pipeline(
        task=Tasks.auto_speech_recognition,
        model="iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
        model_revision="v2.0.4",
        device=device,
        hub="ms",
        vad_model="iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
        vad_model_revision="v2.0.4",
        punc_model="iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
        punc_model_revision="v2.0.4",
    )

# Benchmark function to measure execution time
def benchmark(pipe, audio_path, runs=10):
    """Measures inference time (mean & P99 percentile)."""
    # Warmup (5 runs to stabilize performance)
    for _ in range(5):
        _ = pipe(input=audio_path)

    # Benchmark runs
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        _ = pipe(input=audio_path)
        end = time.perf_counter()
        times.append(end - start)

    # Compute statistics
    mean_time = np.mean(times) * 1000  # Convert to milliseconds
    p99_time = np.percentile(times, 99) * 1000
    return f"{mean_time:.2f} ms (Mean), {p99_time:.2f} ms (P99)"

# Function to download the audio file if not exists
def download_audio(url, filename):
    if not os.path.exists(filename):
        print(f" Downloading {filename}...")
        r = requests.get(url, allow_redirects=True)
        with open(filename, 'wb') as f:
            f.write(r.content)
        print(f" File {filename} downloaded.")
    else:
        print(f" File {filename} already exists.")

# Define audio file URL & local filename
audio_url = "https://github.com/liangstein/Chinese-speech-to-text/blob/master/3.wav?raw=true"
audio_filename = "paraformer1.wav"

# Download the audio file if needed
download_audio(audio_url, audio_filename)

# Initialize the pipeline
device = "cpu"  # Change to "cuda" if using GPU
inference_pipeline = load_pipeline(device)

# Run inference
print("\n Running Speech-to-Text Inference...")
rec_result = inference_pipeline(input=audio_filename)
print(f"\n Transcription Result: \n{rec_result[0]['text']}")

# Measure execution time
exec_time = benchmark(inference_pipeline, audio_filename)
print(f"\n Execution Time: {exec_time}")
```

The `benchmark()` function measures inference performance, calculating the mean execution time and the 99th percentile latency (P99).

Run the updated Python script:

```bash
python3 paraformer-3.py
```

The output should look like:

```output
 Transcription Result: 
飞机穿过云层，眼下一片云海，有时透过稀薄的云雾，依稀可见南国葱绿的群山大地。
rtf_avg: 0.010: 100%|
 Execution Time: 816.62 ms (Mean), 798.76 ms (P99)
```

The model took 0.816 seconds to complete execution.

### Enable bfloat16 Fast Math Kernels

Now enable bfloat16 and run Python script again:

```bash
export DNNL_DEFAULT_FPMATH_MODE=BF16
python3 paraformer-3.py
```

The output should look like:
```output
 Transcription Result: 
飞机穿过云层，眼下一片云海，有时透过稀薄的云雾，依稀可见南国葱绿的群山大地。
rtf_avg: 0.010: 100%|
 Execution Time: 738.04 ms (Mean), 747.57 ms (P99)
```

Here you can see that the execution time is now 0.7 seconds, reflecting an improvement compared to earlier results.

## Conclusion
Arm CPUs paired with an optimized software ecosystem enable developers to build innovative, efficient ASR solutions. Discover the potential of ModelScope and FunASR, and harness Arm technology for your next Chinese ASR project.
