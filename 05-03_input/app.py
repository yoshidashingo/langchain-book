import streamlit as st

st.title("langchain-streamlit-app")

prompt = st.chat_input("What is up?")
print(prompt)
