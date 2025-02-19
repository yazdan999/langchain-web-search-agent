
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.agents import DuckDuckGoSearchRun
from langchain.llms import Bedrock
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Amazon Bedrock model
def get_bedrock_model():
    # You can adjust this part based on the model you're using on Bedrock
    model = Bedrock(api_key=os.getenv('AMAZON_BEDROCK_API_KEY'))
    return model

# Initialize DuckDuckGo Search tool
def get_duckduckgo_search_tool():
    search_tool = DuckDuckGoSearchRun(api_key=os.getenv('DUCKDUCKGO_API_KEY'))
    return search_tool

# LangChain agent function
def create_agent(query):
    # Define the tools available to the agent
    search_tool = get_duckduckgo_search_tool()
    bedrock_model = get_bedrock_model()

    tools = [
        Tool(
            name="DuckDuckGoSearchRun",
            func=search_tool.run,
            description="Search the web for information"
        ),
        Tool(
            name="AmazonBedrock",
            func=bedrock_model.predict,
            description="Generate text based on the search results"
        )
    ]

    # Initialize the agent with the tools
    agent = initialize_agent(
        tools, 
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        llm=bedrock_model,
        verbose=True
    )
    
    # Get the agent's response
    response = agent.run(query)
    return response
