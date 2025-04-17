import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDMocpnEbmcPC80QsID5hA4677aL8LfWxw")

# Initialize model
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit config
st.set_page_config(page_title="Gemini Chatbot", layout="centered")

# Styling
st.markdown("""
    <style>
        .chat-container {
            max-width: 700px;
            margin: auto;
            padding: 20px;
        }
        .chat-bubble {
            padding: 10px 15px;
            border-radius: 10px;
            margin: 10px 0;
            max-width: 80%;
            word-wrap: break-word;
        }
        .user {
            background-color: #d1ecf1;
            margin-left: auto;
            text-align: right;
        }
        .assistant {
            background-color: #e2f0d9;
            margin-right: auto;
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>🤖 Gemini Chatbot</h2>", unsafe_allow_html=True)

# Initialize session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    role = "user" if msg["role"] == "user" else "assistant"
    st.markdown(
        f"<div class='chat-bubble {role}'>{msg['content']}</div>", unsafe_allow_html=True
    )

# Chat input
user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f"<div class='chat-bubble user'>{user_input}</div>", unsafe_allow_html=True)

    try:
        response = st.session_state.chat.send_message(user_input)
        answer = response.text
    except Exception as e:
        answer = f"Error: {str(e)}"

    st.markdown(f"<div class='chat-bubble assistant'>{answer}</div>", unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": answer})

st.markdown("</div>", unsafe_allow_html=True)
