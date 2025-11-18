import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# App title
st.title("🌾 Cropy — Smart Farming Assistant ")

# Validate API key
if not GEMINI_API_KEY:
    st.error("❌ Gemini API key not found. Please check your .env file.")
    st.stop()

# Configure Gemini
try:
    genai.configure(api_key=GEMINI_API_KEY)
    MODEL_NAME = "gemini-2.5-flash"  # ✅ confirmed supported
    model = genai.GenerativeModel(MODEL_NAME)
except Exception as e:
    st.error(f"⚠️ Error configuring Gemini: {str(e)}")
    st.stop()

# Session history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("Ask Cropy about farming 🌱")

# Send button
if st.button("Send"):
    if user_input:
        st.session_state.history.append({"role": "user", "content": user_input})

        # Build conversation context
        chat_context = "\n".join(
            [f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.history]
        )

        try:
            # Generate reply from Gemini 2.5 Flash
            response = model.generate_content(
                f"You are Cropy, a smart farming expert. Provide practical, accurate, and friendly farming guidance.\n\n{chat_context}\nAI Boy:"
            )
            reply = response.text
            st.session_state.history.append({"role": "assistant", "content": reply})
            st.markdown(f"**Cropy:** {reply}")
        except Exception as e:
            st.error(f"⚠️ Gemini Error: {str(e)}")

    else:
        st.warning("Please type your question!")

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.history = []
    st.success("Chat history cleared!")
