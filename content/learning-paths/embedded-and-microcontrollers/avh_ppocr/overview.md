---
# User change
title: "Overview of OCR"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Overview of optical character recognition (OCR)

Optical character recognition (OCR) aims at recognizing the text content in a fixed image area. It is one of the key applications in the field of computer vision (CV).

OCR has been widely used in many industry scenarios such as ticket information extraction, manufacturing product traceability, and government medical document processing. 

Text recognition is a sub-task of OCR. It’s the step after text detection in OCR’s two-stage algorithm which converts image information into text information. 

![Example of English text recognition #center](./Figure1.png "Figure 1. Example of English text recognition (Image source: https://iapr.org/archives/icdar2015/index.html)")


In this Learning Path, you will learn how to apply deep learning (DL) to the OCR text recognition task and setup a development flow from model training to application deployment. 

You will learn how to:
- Use [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) to obtain a trained English text recognition model
- Export the Paddle inference model 
- Compile the Paddle inference model with [TVMC](https://tvm.apache.org/docs/tutorial/tvmc_command_line_driver.html#sphx-glr-tutorial-tvmc-command-line-driver-py) for the target device
- Build a text recognition application and deploy it on the [Corstone-300 FVP](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) with [Arm Cortex-M55](https://www.arm.com/products/silicon-ip-cpu/cortex-m/cortex-m55).

This project is a collaboration between Arm and Baidu to improve PaddlePaddle model deployment to Arm Cortex-M devices. This gives developers more choices by increasing the number of deep learning models supported on Cortex-M.

## PP-OCRv3

PaddleOCR provides an OCR system named PP-OCR. This is a practical, ultra-lightweight OCR system created by the Baidu Paddle Team. 

It is a two-stage OCR system, in which the text detection algorithm is called [DB](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_en/algorithm_det_db_en.md), and the text recognition algorithm is called [CRNN](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_en/algorithm_rec_crnn_en.md). 

As seen in Figure 2, the overall pipeline of PP-OCRv3 is similar to PP-OCRv2 with some further optimizations to the detection model and recognition model. 

For example, the text recognition model introduces [SVTR](https://arxiv.org/abs/2205.00159) (Scene Text Recognition with a Single Visual Model) based on PP-OCRv2. The model also uses [GTC](https://arxiv.org/pdf/2002.01276.pdf) (Guided Training of CTC) to guide training and model distillation. For more details, please refer to this PP-OCRv3 [technical report](https://arxiv.org/abs/2206.03001v2).

![PP-OCRv3 pipeline diagram #center](./Figure2.png "Figure 2. PP-OCRv3 pipeline diagram (Image source: https://github.com/PaddlePaddle/PaddleOCR/blob/dygraph/doc/doc_en/PP-OCRv3_introduction_en.md)")

In the next section, you will deploy a trained PP-OCR text recognition model on the Arm Corstone-300 FVP.


