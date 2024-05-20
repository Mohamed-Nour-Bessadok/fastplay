import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
import requests
import json

st.set_page_config(page_title="Friendly Assistant")
st.title("Your Friendly Company Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Conversation
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    else:
        with st.chat_message("AI"):
            st.markdown(message.content)

user_input = st.chat_input("Enter your question here:")
if user_input is not None and user_input != "":
    st.session_state.chat_history.append(HumanMessage(user_input))
    
    with st.chat_message("Human"):
        st.markdown(user_input)
    
    try:
        response = requests.post(
            "http://localhost:8000/chatbot", 
            json={"input": user_input, "chat_history": []}
        )
        response.raise_for_status()  # Raise an error for bad status codes
        
        response_json = response.json()
        #st.write("Parsed JSON Response:", response_json)
        
        # Extract the correct field from the nested response
        ai_response = response_json.get("response", {}).get("output", "No response from the AI")
        
        with st.chat_message("AI"):
            st.markdown(ai_response)
        
        st.session_state.chat_history.append(AIMessage(content=ai_response))  # Ensure `content` is a string
    except requests.exceptions.RequestException as e:
        error_message = f"An error occurred: {e}"
        with st.chat_message("AI"):
            st.markdown(error_message)
        st.session_state.chat_history.append(AIMessage(content=error_message))  # Ensure `content` is a string
