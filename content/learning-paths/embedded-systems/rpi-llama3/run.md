---
title: Run the model on the edge device (optional)
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download files and run on your Raspberry Pi

Open a new terminal in your AWS instance to copy over the files. Replace `CONTAINER` with the name of the container, and the bracketed file names with the absolute paths to the corresponding files.

```bash
docker cp CONTAINER:<cmake-out/examples/models/llama2/llama_main> .
docker cp CONTAINER:<llama3/Meta-Llama-3-8B/> .
docker cp CONTAINER:<llama3_kv_sdpa_xnn_qe_4_32.pte> .
```
If you don't know the container name, you can list it using:
```bash
docker container ls
```
Now you can transfer the files from the AWS instance to your Raspberry Pi 5. There are multiple ways to do this: via cloud storage services, with a USB thumb drive or using SSH. Use any method that is convenient for you. Transfer the two files and the directory you downloaded from the Docker container. 

Finally, run the model using the same command as before:

```bash
llama_main --model_path=<model pte file> \
--tokenizer_path=<tokenizer.model> --prompt="what is the meaning of life?"
```