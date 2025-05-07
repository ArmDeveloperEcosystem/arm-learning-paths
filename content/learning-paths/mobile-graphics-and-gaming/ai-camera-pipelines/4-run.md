---

title: Run the Pipelines
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the previous section, we built the AI Camera Pipelines. In this section, you will run the AI Camera pipelines to transform an image.

## Background Blur

```BASH
cd $HOME/ai-camera-pipelines
bin/cinematic_mode resources/test_input2.ppm test_output2.ppm resources/depth_and_saliency_v3_2_assortedv2_w_augment_mobilenetv2_int8_only_ptq.tflite
```

![example image alt-text#center](test_input2.png "Figure 3: Original picture")
![example image alt-text#center](test_output2.png "Figure 4: Picture with blur applied")

## Low Light Enhancement

```BASH
cd $HOME/ai-camera-pipelines
bin/low_light_image_enhancement resources/test_input2.ppm test_output2_lime.ppm resources/HDRNetLIME_lr_coeffs_v1_1_0_mixed_low_light_perceptual_l2_loss_int8_only_ptq.tflite
```

![example image alt-text#center](test_output2_lime.png "Figure 5: Picture with low light enhancement applied")