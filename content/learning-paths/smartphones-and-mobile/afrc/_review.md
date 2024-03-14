---
review:
    - questions:
        question: >
            Is AFRC always better than AFBC?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            AFRC guarantees the lowest memory footprint, but bandwidth reduction depends on the image being compressed.
            AFBC uses variable bitrates which require slightly more memory than uncompressed images, but can compress some blocks (e.g. solid color) better than AFRC.

    - questions:
        question: >
            Does AFRC completely replace AFBC?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            AFRC supports a subset of the texture formats supported by AFBC.
            AFRC is lossy, which might not be appropriate for attachments where uncompressed values are needed.
               
    - questions:
        question: >
            What is the `VK_EXT_image_compression_control` extension used for?
        answers:
            - Checking if AFBC was applied
            - Requesting AFRC
            - Checking if AFRC was applied
            - All of the above
        correct_answer: 4
        explanation: >
            The extension controls the type and level of compression applied to images.
            Additionally, it may also be used to check if a given image (e.g. the swapchain) is being automatically compressed with AFBC.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
