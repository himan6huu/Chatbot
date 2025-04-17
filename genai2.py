import streamlit as st
import google.generativeai as genai
import fitz  # PyMuPDF

# Set your Gemini API Key
genai.configure(api_key="")

# Load the model
model = genai.GenerativeModel('gemini-1.5-flash')  # You can use 'gemini-pro' as well

# Initialize chat session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = []

st.set_page_config(page_title="Gemini Chatbot with PDF", page_icon="")
st.title("Gemini AI Chatbot with PDF Training")

# PDF upload functionality
uploaded_pdf = st.file_uploader("Upload your PDF", type="pdf")

# Extract text from uploaded PDF
if uploaded_pdf is not None:
    doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
    pdf_text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pdf_text += page.get_text()

    # Display first 1000 characters of PDF for reference
    st.write("Extracted PDF Text (first 1000 characters):")
    st.write(pdf_text[:1000])

    # Store extracted text for future use
    st.session_state.pdf_text = pdf_text

# Chat functionality
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])