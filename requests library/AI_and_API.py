import requests
import json

# API endpoint and key
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=YourAPIKey"

# Headers for the request
headers = {
    'Content-Type': 'application/json'
}

# Payload (data to send in the request)
payload = {
    "contents": [{
        "parts": [{"text": "Explain how AI works"}]
    }]
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()

    # Extract the text response
    try:
        text_response = response_data["candidates"][0]["content"]["parts"][0]["text"]
        print("Text Response from API:")
        print(text_response)
    except KeyError:
        print("Error: Unable to extract text response from the API output.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)


#The response is :

# Text Response from API:
# Artificial intelligence (AI) is a broad field encompassing many techniques, but at its core, it involves creating systems that can perform tasks that typically require human intelligence.  These tasks include learning, problem-solving, decision-making, perception, and understanding language.  Here's a breakdown of how different AI approaches work:

# **1. Machine Learning (ML):** This is the most prevalent approach to AI today.  Instead of being explicitly programmed with rules, ML algorithms learn from data.  They identify patterns, relationships, and insights within the data to make predictions or decisions.  There are several types of ML:

# * **Supervised Learning:** The algorithm is trained on a labeled dataset, meaning the data is already tagged with the correct answers.  The algorithm learns to map inputs to outputs based on this labeled data. Examples include image classification (labeling images as cat or dog) and spam detection.

# * **Unsupervised Learning:** The algorithm is trained on an unlabeled dataset.  It identifies patterns and structures in the data without any pre-defined answers.  Examples include clustering (grouping similar data points together) and dimensionality reduction (reducing the number of variables while preserving important information).

# * **Reinforcement Learning:** The algorithm learns through trial and error by interacting with an environment.  It receives rewards for desirable actions and penalties for undesirable actions.  The goal is to learn a policy that maximizes the cumulative reward.  Examples include game playing (e.g., AlphaGo) and robotics.

# **2. Deep Learning (DL):** A subfield of ML that uses artificial neural networks with multiple layers (hence "deep").  These networks are inspired by the structure and function of the human brain.  Deep learning excels at tasks involving complex patterns and large datasets, such as image recognition, natural language processing, and speech recognition.  Key techniques include:

# * **Convolutional Neural Networks (CNNs):**  Excellent for processing grid-like data like images and videos.
# * **Recurrent Neural Networks (RNNs):**  Designed for sequential data like text and time series.
# * **Generative Adversarial Networks (GANs):**  Two networks compete against each other – one generates data, the other tries to distinguish real from generated data – leading to the generation of realistic synthetic data.


# **3. Expert Systems:** These AI systems mimic the decision-making ability of a human expert in a specific domain.  They use a knowledge base containing facts and rules to reason and make inferences.  While less prevalent now than ML, they remain useful in situations requiring clear, explainable reasoning.


# **4. Natural Language Processing (NLP):** This focuses on enabling computers to understand, interpret, and generate human language.  It uses techniques from ML and DL to perform tasks such as machine translation, text summarization, sentiment analysis, and chatbot development.


# **5. Computer Vision:** This allows computers to "see" and interpret images and videos.  It uses techniques from ML and DL to perform tasks such as object detection, image classification, and facial recognition.


# **In simple terms:** AI systems learn from data (or are explicitly programmed with rules), identify patterns, and use this knowledge to make predictions, decisions, or take actions. The specific techniques used depend on the task and the available data.  The field is constantly evolving, with new algorithms and approaches emerging regularly.

