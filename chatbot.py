import streamlit as st
import requests

try:
    API_KEY = st.secrets["OPENROUTER_API_KEY"]
except Exception as e:
    st.error(f"API key not found: {e}")
    st.stop()

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
