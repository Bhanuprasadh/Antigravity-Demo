import streamlit as st
from rag_engine import get_chat_engine
import os

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 RAG Chatbot with Gemini & ChromaDB")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_engine" not in st.session_state:
    try:
        print("Calling get_chat_engine()...")
        st.session_state.chat_engine = get_chat_engine()
        print("get_chat_engine() returned.")
        st.success("RAG Engine Initialized!")
    except Exception as e:
        print(f"Error initializing RAG Engine: {e}")
        st.error(f"Error initializing RAG Engine: {e}")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    if "chat_engine" in st.session_state:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            try:
                response = st.session_state.chat_engine.chat(prompt)
                response_text = response.response
                response_placeholder.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                response_placeholder.error(f"An error occurred: {e}")
