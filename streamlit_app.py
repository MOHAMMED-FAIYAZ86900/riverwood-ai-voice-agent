import streamlit as st
from src.llm_engine import generate_response

st.title("Riverwood AI Voice Agent")

user_input = st.text_input("Ask something")

if user_input:
    response = generate_response(user_input, [])
    st.write("AI:", response)