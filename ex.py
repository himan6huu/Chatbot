import streamlit as st

st.title("This is first application")
st.header("hello this is streamlit app")
st.subheader("This is a subheader")
st.text("Welcome to the world of Streamlit!")

name = st.text_input("enter your name")
if st.button("Submit"):
    st.write("hello ", name)

if st.checkbox("Show Secret Message"):
    st.write("You discovered a hidden message!")

option = st.selectbox(
    "Choose your favorite language:",
    ["Python", "Java", "C++", "JavaScript"],
)
st.write("You selected:", option)

age = st.slider("Select your age:", 1, 100, 25)
st.write("Your age is", age)