import streamlit as st
import requests
import json

st.title('Chatbot Interface')

# User input
user_input = st.text_input("Enter your question here:")

if st.button('Send'):
    # Send the user message to FastAPI server
    response = requests.post(
        "http://localhost:8000/chatbot", 
        json={"input": user_input, "chat_history": []}
    )

    if response.status_code == 200:
        # Get the chatbot response
        data = response.json()
        chatbot_response = data.get('response', '')

        # Display the chatbot response
        st.text_area("Chatbot response:", value=chatbot_response, height=200, max_chars=None, key=None)
    else:
        st.write(f"Error: {response.status_code}")
