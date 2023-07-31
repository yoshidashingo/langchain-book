import streamlit as st

st.title("langchain-streamlit-app")

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = "こんにちは"
        st.markdown(response)
