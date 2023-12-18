---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add additional context if desired


review:
    - questions:
        question: >
            Which statement will add the runAnimation method to handle the clicked event of the QPushButton?
        answers:
            - "handle(runAnimationButton, &QPushButton::clicked, view, &XFormView::runAnimation)"
            - "addHandler(runAnimationButton, &QPushButton::clicked, view, &XFormView::runAnimation)"
            - "connect(runAnimationButton, &QPushButton::clicked, view, &XFormView::runAnimation)"
            - "addSignal(runAnimationButton, &QPushButton::clicked, view, &XFormView::runAnimation)"            
        correct_answer: 3
        explanation: >
            In Qt you use the connect method to define signals (event handlers)

    - questions:
        question: >
            Which Qt class enables you to transform images?
        answers:
            - "QTransformer"
            - "QTransform"
            - "QTransfer"
        correct_answer: 2                     
        explanation: >
            QTransform provides methods that enables you to rotate (QTransform.rotate), scale (QTransform.scale), and shear (QTransform.shear) the image

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
