import streamlit as st
import requests

API_KEY = "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"  # <-- replace with your real key
model = "openai/gpt-3.5-turbo"

st.title("🧠 Gen-AI Chatbot (OpenRouter)")
question = st.text_input("Ask me anything:")

if question:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        st.write(response.json()["choices"][0]["message"]["content"])
    else:
        st.error("Error from API: " + response.text)