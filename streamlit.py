import streamlit as st
import requests

st.title("Chatbot for Utkarsh Classes")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

def get_response(user_input):
    response = requests.post("http://localhost:5000/chat", json={"message": user_input})
    return response.json().get("response")

user_input = st.text_input("You: ")
if st.button("Send"):
    if user_input:
        response = get_response(user_input)
        st.session_state['chat_history'].append(f"You: {user_input}")
        st.session_state['chat_history'].append(f"Bot: {response}")

for message in st.session_state['chat_history']:
    st.write(message)
