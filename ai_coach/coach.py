import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def chat_with_ai(prompt, role="fitness"):
    if role == "fitness":
        system_prompt = "You are a friendly and experienced fitness and nutrition coach."
    else:
        system_prompt = "You are a helpful productivity coach who helps with tasks and time management."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
