import os
import streamlit as st
from streamlit_chat import message
import cohere

# Set up your Cohere API key
cohere_api_key = "NdQnF5BowGdcep3c6v4ID9VMAnacUG9Prfutr3tT"

if not cohere_api_key:
    raise ValueError("COHERE_API_KEY environment variable not found")

co = cohere.Client(cohere_api_key)

# Function to get a response from Cohere
def get_response(prompt):
    response = co.generate(
        model='command',  # Use the appropriate model name
        prompt=prompt,
        max_tokens=50
    )
    return response.generations[0].text.strip()

# Function to clear the chat
def clear_chat():
    st.session_state.messages = [{"role": "assistant", "content": "Say something to get started!"}]

# Streamlit app setup
st.title("Llama2 Clarifai Tutorial")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Say something to get started!"}]

with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])
    user_prompt = a.text_input(
        label="Your message:",
        placeholder="Type something...",
        label_visibility="collapsed",
    )
    b.form_submit_button("Send", use_container_width=True)

# Display messages
for msg in st.session_state.messages:
    message(msg["content"], is_user=msg["role"] == "user")

# Handle user input
if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    message(user_prompt, is_user=True)

    # Get response from Cohere
    response = get_response(user_prompt)
    msg = {"role": "assistant", "content": response}
    
    st.session_state.messages.append(msg)
    message(msg["content"])

# Clear chat button
if len(st.session_state.messages) > 1:
    st.button('Clear Chat', on_click=clear_chat)
