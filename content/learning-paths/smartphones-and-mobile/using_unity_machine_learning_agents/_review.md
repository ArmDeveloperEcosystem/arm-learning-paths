---
review:
    - questions:
        question: >
            Which machine learning paradigm did we use in this learning path?
        answers:
            - Imitation Learning
            - Unity ML Agents
            - Reinforcement Learning
        correct_answer: 3                    
        explanation: >
            We used reinforcement learning. (One of the paradigms supported by Unity ML Agents toolkit.)

    - questions:
        question: >
            We could specify a separate brain for each character within the game.
        answers:
            - True
            - False
        correct_answer: 1                    
        explanation: >
            Refer to "The Training Configurations", where we show an alternative yaml file which defines two separate brains; one for the "Paladin" and another for the "Vampire".
               
    - questions:
        question: >
            Using the training model in this learning path, how long can it take to train the model to a competent level for our game?
        answers:
            - Minutes
            - About an hour
            - Several hours
        correct_answer: 3          
        explanation: >
            Depending on the host machine, at time of writing it can take 6+ hours for the training model to reach 3,000,000 learning iterations.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
