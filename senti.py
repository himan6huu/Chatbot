import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Load VADER sentiment analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Streamlit UI
st.set_page_config(page_title="Sentiment Analyzer", layout="centered")
st.title("Sentiment Analysis App (NLTK + Streamlit)")
st.write("Enter some text to see if it's Positive, Negative, or Neutral.")

# Input text
user_input = st.text_area("Your Text", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        sentiment = sia.polarity_scores(user_input)
        score = sentiment['compound']

        # Show results
        if score >= 0.05:
            st.success("Sentiment: Positive")
        elif score <= -0.05:
            st.error("Sentiment: Negative")
        else:
            st.info("Sentiment: Neutral")