# Importing necessary packages
import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables
load_dotenv()

# Configure Google API key
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

# Set the model for the AI mentor
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit web app setup
st.set_page_config(page_title="Dhanushiya's AI Mentor", page_icon="🧠")
st.title("Dhanushiya's AI Mentor")
st.header("Welcome to Dhanushiya's AI Mentor")
st.write("Have a conversation with your personalized AI mentor!")

# Initialize session state for conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Function to generate AI response
def generate_response(user_input):
    result = model.generate_content({
        "parts": [
            {
                "text": user_input
            }
        ]
    })
    return result.text

# User input
user_input = st.text_input("You:")
submit = st.button("Send")

# Handle user input
if submit:
    
    if user_input.strip() == "":
        st.warning("Please enter your message.")
    else:
        try:
            # Generate response from AI mentor
            ai_response = generate_response(user_input)
            
            # Update conversation history
            st.session_state.conversation.append({"user": user_input, "ai": ai_response})
        except Exception as e:
            st.error(f"Failed to generate a response: {e}")

# Display conversation history
if st.session_state.conversation:
    st.header("Conversation:")
    for entry in st.session_state.conversation:
        st.markdown(f"*You:* {entry['user']}")
        st.markdown(f"*AI Mentor:* {entry['ai']}")