import streamlit as st
from bot import simple_chatbot
st.set_page_config(page_title="Simple NLP Chatbot", layout="centered")
st.title(" Simple Chatbot with NLP")
st.markdown("Type a message below and let's chat!")
#Store chat messages
if "messages" not in st.session_state:
  st.session_state.messages = []
# Input box
user_input=st.text_input("You:", key="input")
if user_input:
  st.session_state.messages.append(("You", user_input))
#Get bot response
  response = simple_chatbot(user_input)
  st.session_state.messages.append(("Bot", response))
# Display conversation
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"👤 {sender}: {msg}")
    else:
        st.markdown(f"🤡{sender}:* {msg}")