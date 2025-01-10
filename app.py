import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from utkarsh_info import get_initial_prompt
from crawler_utils import get_website_content, create_context_from_markdown

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Configure the API key for the Generative AI model
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize session states
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'current_mode' not in st.session_state:
    st.session_state['current_mode'] = 'utkarsh'
if 'chat_session' not in st.session_state:
    st.session_state['chat_session'] = None

def initialize_chat_session(context_prompt):
    generation_config = {
        "temperature": 0.9,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
    )
    
    chat = model.start_chat(history=[])
    chat.send_message(context_prompt)
    return chat

# Initialize default Utkarsh chat session if not exists
if st.session_state['chat_session'] is None:
    st.session_state['chat_session'] = initialize_chat_session(get_initial_prompt())

# Sidebar for mode selection and custom URL input
with st.sidebar:
    st.header("Chatbot Configuration")
    mode = st.radio("Select Mode", ['Utkarsh Classes', 'Custom Website'])
    
    if mode == 'Custom Website':
        st.markdown("---")
        st.header("Custom Website Configuration")
        url_input = st.text_input("Enter Website URL:", 
                                 placeholder="https://example.com")
        if st.button("Create Custom Chatbot"):
            with st.spinner("Extracting website content..."):
                website_content = get_website_content(url_input)
                context_prompt = create_context_from_markdown(website_content)
                st.session_state['chat_session'] = initialize_chat_session(context_prompt)
                st.session_state['current_mode'] = 'custom'
                st.session_state['chat_history'] = []
                st.success("Custom chatbot created successfully!")
    
    if st.button("Reset to Utkarsh Mode"):
        st.session_state['chat_session'] = initialize_chat_session(get_initial_prompt())
        st.session_state['current_mode'] = 'utkarsh'
        st.session_state['chat_history'] = []
        st.success("Reset to Utkarsh mode successfully!")

# Main chat interface
st.title("🤖 AI Assistant")
if st.session_state['current_mode'] == 'custom':
    st.caption("Custom Website Mode")
else:
    st.caption("Utkarsh Classes Mode")
st.markdown("---")

# Chat interface
chat_container = st.container()
with chat_container:
    # Display chat history
    for message in st.session_state['chat_history']:
        role = message['role']
        content = message['content']
        
        if role == 'user':
            st.markdown(f"**You:** {content}")
        else:
            st.markdown(f"**Assistant:** {content}")
    
    # User input
    user_input = st.text_input("Ask a question:", key="user_input")
    
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        send_button = st.button("Send", key="send_button")
    with col2:
        clear_button = st.button("Clear Chat")
    
    if send_button and user_input:
        # Add user message to chat history
        st.session_state['chat_history'].append({
            "role": "user",
            "content": user_input
        })
        
        # Get bot response
        response = st.session_state['chat_session'].send_message(user_input)
        
        # Add bot response to chat history
        st.session_state['chat_history'].append({
            "role": "assistant",
            "content": response.text
        })
        
        # Clear input and rerun
        st.rerun()

    if clear_button:
        st.session_state['chat_history'] = []
        st.rerun()

# Footer
st.markdown("---")
if st.session_state['current_mode'] == 'utkarsh':
    st.markdown("*Powered by Utkarsh Classes & Edutech Pvt Ltd*")
else:
    st.markdown("*Powered by AI Assistant*") 