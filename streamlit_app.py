import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import os
import openai

openai.api_key = "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"

# Create title and logo
st.title("Chatbot")
st.image("logo.png")
# Create sidebar for settings
sidebar = st.sidebar
# Create a dropdown menu for selecting the model
model = sidebar.selectbox(
    "Select the language model",
    ("gpt-3.5-turbo", "gpt-4.0-turbo")
)
# Create a slider for adjusting the temperature
temperature = sidebar.slider(
    "Adjust the temperature",
    0.0, 1.0, 0.7, 0.01
)
# Create a text input for user message
user_message = st.text_input("User")
# Create a button for generating chatbot response
if st.button("Send"):
    # Generate chatbot response using OpenAI API
    response = openai.Completion.create(
        model=model,
        prompt=f"User: {user_message}\nChatbot:",
        temperature=temperature,
        max_tokens=50,
        stop="\n"
    )
    # Display chatbot response
    st.write(f"Chatbot: {response['choices'][0]['text']}")