import os
import streamlit as st
import boto3
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools import DuckDuckGoSearchRun
from langchain.llms import Bedrock

# Load environment variables
load_dotenv()

# Initialize Amazon Bedrock model
def get_bedrock_model():
    client = boto3.client("bedrock-runtime", region_name="us-east-1")  # Change region if needed
    return Bedrock(client=client, model_id="anthropic.claude-v2")  # Use the right model ID

# Initialize DuckDuckGo Search tool
def get_duckduckgo_search_tool():
    return DuckDuckGoSearchRun()  # No API key needed

# LangChain agent function
def create_agent(query):
    # Define the tools available to the agent
    search_tool = get_duckduckgo_search_tool()
    bedrock_model = get_bedrock_model()

    tools = [
        Tool(
            name="DuckDuckGoSearchRun",
            func=search_tool.run,
            description="Search the web for information."
        )
    ]

    # Initialize the agent
    agent = initialize_agent(
        tools=tools, 
        llm=bedrock_model,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    # Get the agent's response
    response = agent.run(query)
    return response

# Streamlit UI
st.title("AI Web Search Agent")
query = st.text_input("Enter your search query:")

if query:
    st.write("🔍 Searching...")
    response = create_agent(query)
    st.write("### AI Response")
    st.write(response)
