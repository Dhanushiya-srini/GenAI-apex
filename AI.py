# Import necessary packages
import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("API_KEY")  # Ensure this matches the key name in your .env file

# Check if API key is retrieved correctly
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    st.error("API Key not found. Please set the API_KEY in your environment variables.")

# Streamlit web app setup
st.set_page_config(page_title="Dhanushiya's Chatbot", page_icon="🌟")
st.title("Dhanushiya's Chatbot")
st.header("Welcome to Dhanushiya's Chatbot")
st.write("Ask me anything, I am here to help you!")

# User input for the question
question = st.text_input("Enter your question here")
submit = st.button("Proceed")

# Handle user input
if submit:
    if not api_key:
        st.error("API Key is missing! Please check your configuration.")
    elif question.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            result = model.generate_content(question)
            st.header("Answer for the question:")
            st.write(result.text)
        except Exception as e:
            st.error(f"Failed to generate a response: {e}")
