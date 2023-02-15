---
# User change
title: "PP-OCRv3"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# PP-OCRv3
PaddleOCR provides an OCR system named PP-OCR. This is a self-developed practical ultra-lightweight OCR system created by the Baidu Paddle Team. It is a two-stage OCR system, in which the text detection algorithm is called [DB](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_en/algorithm_det_db_en.md), and the text recognition algorithm is called [CRNN](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_en/algorithm_rec_crnn_en.md). As seen in Figure 2, the overall pipeline of PP-OCRv3 is similar to PP-OCRv2 with some further optimizations to the detection model and recognition model. For example, the text recognition model introduces [SVTR](https://arxiv.org/abs/2205.00159) (Scene Text Recognition with a Single Visual Model) based on PP-OCRv2. The model also uses [GTC](https://arxiv.org/pdf/2002.01276.pdf) (Guided Training of CTC) to guide training and model distillation. For more details, please refer to this PP-OCRv3 [technical report](https://arxiv.org/abs/2206.03001v2).

![PP-OCRv3 pipeline diagram #center](./Figure2.png "Figure 2. PP-OCRv3 pipeline diagram (Image source: https://github.com/PaddlePaddle/PaddleOCR/blob/dygraph/doc/doc_en/PP-OCRv3_introduction_en.md)")

