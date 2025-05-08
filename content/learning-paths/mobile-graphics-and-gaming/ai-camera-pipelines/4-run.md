---

title: Run the pipelines
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the previous section, you built the AI Camera Pipelines. In this section, you'll run them to apply transformations to an input image.

## Background Blur

Run the background blur pipeline:

```bash
cd $HOME/ai-camera-pipelines
bin/cinematic_mode resources/test_input2.ppm test_output2.ppm resources/depth_and_saliency_v3_2_assortedv2_w_augment_mobilenetv2_int8_only_ptq.tflite
```

![example image alt-text#center](test_input2.png "Original picture")
![example image alt-text#center](test_output2.png "Picture with blur applied")

## Low-Light Enhancement

```bash
cd $HOME/ai-camera-pipelines
bin/low_light_image_enhancement resources/test_input2.ppm test_output2_lime.ppm resources/HDRNetLIME_lr_coeffs_v1_1_0_mixed_low_light_perceptual_l2_loss_int8_only_ptq.tflite
```

![example image alt-text#center](test_output2_lime.png "Picture with low-light enhancement applied")