
import streamlit as st
from agent import create_agent

def main():
    st.title("AI Agent - Web Search and Model Inference")

    user_input = st.text_input("Enter your query:")

    if user_input:
        response = create_agent(user_input)
        st.write(response)

if __name__ == "__main__":
    main()
