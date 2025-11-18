import streamlit as st
from openai import OpenAI
from utils.config import OPENAI_API_KEY

st.title("Cropy— Smart Farming Assistant")

client = OpenAI(api_key=OPENAI_API_KEY)

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask AI Boy about farming 🌾")

if st.button("Send"):
    if user_input:
        st.session_state.history.append({"role": "user", "content": user_input})
        messages = [{"role": "system", "content": "You are AI Boy, a farming expert."}] + st.session_state.history
        response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        reply = response.choices[0].message.content
        st.session_state.history.append({"role": "assistant", "content": reply})
        st.write(f"**AI Boy:** {reply}")
    else:
        st.warning("Please type your question!")

if st.button("Clear Chat"):
    st.session_state.history = []
