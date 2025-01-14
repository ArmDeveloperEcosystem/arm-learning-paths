---
review:
    - questions:
        question: >
            What is the primary purpose of using RAG in an LLM chatbot?
        answers:
            - To reduce the size of the model
            - To enhance the chatbot's responses with contextually relevant information
            - To increase the training speed of the model
            - To simplify the deployment process
        correct_answer: 2
        explanation: >
            RAG (Retrieval Augmented Generation) enhances the chatbot's responses by retrieving and incorporating contextually relevant information from a vector database.

    - questions:
        question: >
            Which framework is used to create the web interface for the RAG-based LLM server?
        answers:
            - Django
            - Flask
            - Streamlit
            - FastAPI
        correct_answer: 3
        explanation: >
            Streamlit is used to create the web interface for the RAG-based LLM server, allowing users to interact with the backend.

    - questions:
        question: >
            What is the role of FAISS in the RAG-based LLM server?
        answers:
            - To train the LLM model
            - To store and retrieve vectorized documents
            - To handle HTTP requests
            - To manage user authentication
        correct_answer: 2
        explanation: >
            FAISS is used to store and retrieve vectorized documents, enabling the RAG-based LLM server to provide contextually relevant responses.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 6                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
