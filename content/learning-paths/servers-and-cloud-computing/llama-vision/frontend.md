---
title: Deploy Vision Chatbot LLM frontend server
weight: 5

layout: learningpathall
---

## Frontend Script for Vision Chatbot LLM Server

After activating the virtual environment in a new terminal, you can use the following `frontend.py` script to input image, text prompt and interact with the backend. This script uses the Streamlit framework to create a web interface for the vision chatbot LLM server.

Create a `frontend.py` script with the following content:

```python
import streamlit as st
import requests, time, base64, json

st.title("LLM Vision Chatbot on Arm")
st.write("Upload an image and input the prompt. The model will generate response based on the image as context.")

# File uploader for image and text input for prompt
uploaded_image = st.file_uploader("**Upload an image**", type=["png", "jpg", "jpeg"])
user_prompt = st.text_area("**Enter your prompt or question about the image**", "")

# Placeholder for the generated answer and metrics
output_area = st.empty()
metrics_area = st.empty()

if st.button("Generate Response"):
    if uploaded_image is None or user_prompt.strip() == "":
        st.warning("Please provide both the image and prompt before submitting.")
    else:
        # Prepare the request (OpenAI-compatible format with image in base64)
        image_bytes = uploaded_image.read()
        b64_image = base64.b64encode(image_bytes).decode('utf-8')
        # Construct request payload similar to OpenAI ChatCompletion
        payload = {
            "messages": [
                {"role": "user", "content": user_prompt}
            ],
            "image": b64_image,       # custom field for image
            "stream": True,           # token streaming
        }

        # Initialize streaming request to backend
        backend_url = "http://localhost:5000/v1/chat/completions"
        generated_text = ""
        # Make POST request with streaming response
        try:
            with requests.post(backend_url, json=payload, stream=True) as resp:
                # Iterate over the streamed lines from the response
                for line in resp.iter_lines(decode_unicode=True):
                    if line is None or line.strip() == "":
                        continue  # skip empty keep-alive lines
                    # OpenAI SSE format lines begin with "data: "
                    if line.startswith("data: "):
                        data = line[len("data: "):]
                        if data.strip() == "[DONE]":
                            break  # stream finished
                        # Parse the JSON chunk
                        chunk = json.loads(data)
                        # The first chunk contains the role, subsequent contain content
                        delta = chunk["choices"][0]["delta"]
                        if "role" in delta:
                            # Initial role announcement (assistant) – skip it
                            continue
                        if "content" in delta:
                            token = delta["content"]
                            # Append token to the output text
                            generated_text += token
                            # Update the output area with the new partial text
                            output_area.markdown(f"**Assistant:** {generated_text}")

        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to backend: {e}")
```

## Run the Frontend Server

You are now ready to run the frontend server for the Vision Chatbot.
Use the following command in a new terminal to start the Streamlit frontend server:

```python
python3 -m streamlit run frontend.py
```

You should see output similar to the following as the frontend server starts successfully:

```output
Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.0.0.10:8501
  External URL: http://35.223.133.103:8501
```
In the next section you will view your running application within your local browser.
