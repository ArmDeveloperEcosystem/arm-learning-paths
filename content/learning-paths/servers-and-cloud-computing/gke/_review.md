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
            You can recover a deleted GKE cluster from GCP.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Clusters that have been deleted cannot be recovered unless you have created backup of it.

    - questions:
        question: >
            Can you delete node pools without affecting the whole cluster?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            You can create, upgrade, and delete node pools individually without affecting the whole cluster, but you can't configure a single node in the node pool; any configuration change affects all nodes in the node pool.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

