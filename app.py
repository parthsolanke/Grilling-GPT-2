import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"  # server URL


def query_model(query):
    payload = {"query": query}
    response = requests.post(API_URL, json=payload)
    return response.json()["response"]


st.title("Chat with SaulGPT2")

user_input = st.text_input("You:", "")
if st.button("Send"):
    if user_input:
        bot_response = query_model(user_input)
        st.text("Bot:", bot_response)
    else:
        st.warning("Please enter a query.")
