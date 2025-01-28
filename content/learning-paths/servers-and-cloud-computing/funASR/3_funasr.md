---
title: Building ASR Applications with ModelScope
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

[FunASR](https://github.com/modelscope/FunASR) is an open-source toolkit specifically designed for speech recognition research and development. It provides a comprehensive set of tools and functionalities for building and deploying ASR applications.


## Installing FunASR
Install FunASR using pip:
```bash
pip3 install funasr
```
{{% notice Note %}}
The following content is based on tests conducted using FunASR version 1.2.3. Variations may exist in different versions.
{{% /notice %}}

## Performing Speech Recognition
FunASR offers a simple interface for performing speech recognition tasks. You can easily transcribe audio files or implement real-time speech recognition using FunASR's functionalities.

!!!! start from english wav

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

介紹 model, device, hub....
測試網路上的短語音


This code will use paraformer model to infleune the wave file, the result will looks like:

```output
python funasr_test1.py
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

The output shows "he tried to think how it could be" as expected. 
Now, we can further test on Chinese model.

```python
from funasr import AutoModel

model = AutoModel(
    model="paraformer-zh",
    device="cpu",
    hub="ms"
)
res = model.generate(input="https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example.wav")

text_content = res[0]['text'].replace(" ","")
print(f"Result: \n{text_content}")
~                                    
```

```output
Downloading Model to directory: /home/ubuntu/.cache/modelscope/hub/iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch
2025-01-28 01:11:21,098 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
ckpt: /home/ubuntu/.cache/modelscope/hub/iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch/model.pt
/home/ubuntu/venv/lib/python3.10/site-packages/funasr/train_utils/load_pretrained_model.py:68: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  src_state = torch.load(path, map_location=map_location)
  0%|                                                                                                                       | 0/1 [00:00<?, ?it/s]/home/ubuntu/venv/lib/python3.10/site-packages/funasr/models/paraformer/model.py:249: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with autocast(False):
rtf_avg: 0.263: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.55it/s]
Result: 
每一天都要快乐哦
```

The output shows "每一天都要快乐哦" as expected, FunAsr also 記錄每個字的 timestamp, 協助之後字幕的需求。 

延伸這個範例與前一節的分割結合，

```python
from funasr import AutoModel
from modelscope.pipelines import pipeline

model = AutoModel(
    model="paraformer-zh",
    device="cpu",
    hub="ms"
)

word_segmentation = pipeline (
    'word-segmentation',
    model='damo/nlp_structbert_word-segmentation_chinese-base'
)

res = model.generate(input="https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example.wav")
text_content = res[0]['text'].replace(" ","")
seg_result = word_segmentation(text_content)

print(f"Result: \n{seg_result}")
```


```output
Downloading Model to directory: /home/ubuntu/.cache/modelscope/hub/iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch
2025-01-28 01:18:28,747 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
ckpt: /home/ubuntu/.cache/modelscope/hub/iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch/model.pt
/home/ubuntu/venv/lib/python3.10/site-packages/funasr/train_utils/load_pretrained_model.py:68: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  src_state = torch.load(path, map_location=map_location)
2025-01-28 01:18:34,062 - modelscope - WARNING - Model revision not specified, use revision: v1.0.3
Downloading Model to directory: /home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base
2025-01-28 01:18:37,407 - modelscope - WARNING - Model revision not specified, use revision: v1.0.3
2025-01-28 01:18:37,993 - modelscope - INFO - initiate model from /home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base
2025-01-28 01:18:37,993 - modelscope - INFO - initiate model from location /home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base.
2025-01-28 01:18:37,995 - modelscope - INFO - initialize model from /home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base
You are using a model of type bert to instantiate a model of type structbert. This is not supported for all configurations of models and can yield errors.
2025-01-28 01:18:40,052 - modelscope - WARNING - No preprocessor field found in cfg.
2025-01-28 01:18:40,052 - modelscope - WARNING - No val key and type key found in preprocessor domain of configuration.json file.
2025-01-28 01:18:40,052 - modelscope - WARNING - Cannot find available config to build preprocessor at mode inference, current config: {'model_dir': '/home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base'}. trying to build by task and model information.
2025-01-28 01:18:40,057 - modelscope - INFO - cuda is not available, using cpu instead.
2025-01-28 01:18:40,058 - modelscope - WARNING - No preprocessor field found in cfg.
2025-01-28 01:18:40,058 - modelscope - WARNING - No val key and type key found in preprocessor domain of configuration.json file.
2025-01-28 01:18:40,058 - modelscope - WARNING - Cannot find available config to build preprocessor at mode inference, current config: {'model_dir': '/home/ubuntu/.cache/modelscope/hub/damo/nlp_structbert_word-segmentation_chinese-base', 'sequence_length': 512}. trying to build by task and model information.
  0%|                                                                                                                       | 0/1 [00:00<?, ?it/s]/home/ubuntu/venv/lib/python3.10/site-packages/funasr/models/paraformer/model.py:249: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with autocast(False):
rtf_avg: 0.257: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.58it/s]
/home/ubuntu/venv/lib/python3.10/site-packages/transformers/modeling_utils.py:1044: FutureWarning: The `device` argument is deprecated and will be removed in v5 of Transformers.
  warnings.warn(
Result: 
{'output': ['每', '一', '天', '都', '要', '快乐', '哦']}
```



## Paraformer

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

The output shows "飞机穿过云层眼下一片云海有时透过稀薄的云雾依稀可见南国葱绿的群山大地" as expected, FunAsr also 記錄每個字的 timestamp, 協助之後字幕的需求



## 標點符號
```python
import os
import requests
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

inference_pipeline = pipeline(
    task=Tasks.auto_speech_recognition,
    model='iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch', model_revision="v2.0.4", device="cpu", hub="ms",
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

```output
rtf_avg: 0.047: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.45it/s]
rtf_avg: -0.026: 100%|██████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 37.57it/s]
rtf_avg: 0.049, time_speech:  8.875, time_escape: 0.439: 100%|██████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.27it/s]

Result: 
飞机穿过云层，眼下一片云海，有时透过稀薄的云雾，依稀可见南国葱绿的群山大地。
```


## Sentiment Analysis
FunASR also supports sentiment analysis of speech, allowing you to determine the emotional tone of spoken language. This can be valuable for applications like customer service and social media monitoring.

```python
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

inference_pipeline = pipeline(
    task=Tasks.emotion_recognition,
    model="iic/emotion2vec_plus_large", device="cpu", hub="ms"
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


## Keyword Enhancement
FunASR allows you to enhance the recognition accuracy of specific keywords. This is particularly useful for applications that require high accuracy for certain terms or phrases.




## Combining Arm CPUs with ModelScope
Arm CPUs, with their high performance and low power consumption, provide an ideal platform for running ModelScope's AI models, especially in edge computing scenarios. Arm's comprehensive software ecosystem supports the development and deployment of ModelScope models, enabling developers to create innovative and efficient applications.


https://community.arm.com/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/neoverse-n2-delivers-leading-price-performance-on-asr

## Conclusion
ModelScope and FunASR empower developers to build robust Chinese ASR applications. By leveraging the strengths of Arm CPUs and the optimized software ecosystem, developers can create innovative and efficient solutions for various use cases. Explore the capabilities of ModelScope and FunASR, and unlock the potential of Arm technology for your next Chinese ASR project.