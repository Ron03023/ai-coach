import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def chat_with_ai(user_input, role):
    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"You are a helpful {role} coach."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content



