# AI Agent with LangChain, Python, Streamlit

This project demonstrates how to build an AI agent that performs simple web searches based on user inquiries using LangChain, Python, Streamlit, and integrates Amazon Bedrock for model inference.

## Features

- **Web Search**: The agent performs web searches using the predefined tool `DuckDuckGoSearchRun` based on the user's inquiry.
- **Model Inference**: The agent uses Amazon Bedrock for generating inferences from the search results.
- **Streamlit Interface**: A simple web interface built with Streamlit where users can interact with the AI agent by providing queries.

## Requirements

- Python 3.8 or higher
- Streamlit
- LangChain
- Amazon Bedrock SDK
- DuckDuckGo API (or relevant search tool setup)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ai-agent.git
   cd ai-agent
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Amazon Bedrock and DuckDuckGo API keys. Create a `.env` file in the root directory with the following variables:

   ```bash
   AMAZON_BEDROCK_API_KEY=your_amazon_bedrock_api_key
   DUCKDUCKGO_API_KEY=your_duckduckgo_api_key
   ```

5. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Project Structure

- `app.py`: Main Streamlit app where users input queries.
- `agent.py`: LangChain integration and model inference code.
- `utils.py`: Utility functions (e.g., setup for DuckDuckGoSearchRun and Amazon Bedrock).
- `.env`: Store your API keys and configurations.

## How it Works

1. **User Input**: The user enters a query through the Streamlit web interface.
2. **Web Search**: The query is passed to the `DuckDuckGoSearchRun` tool, which returns relevant search results.
3. **Model Inference**: The search results are sent to Amazon Bedrock for model inference, which processes and generates insights.
4. **Response**: The model's output is displayed on the Streamlit interface for the user.

## Example Usage

1. Open the Streamlit app by navigating to `http://localhost:8501` in your browser.
2. Enter a query in the input box (e.g., "What is the stock price of Apple?").
3. The agent will search the web, use the model for inference, and display the relevant information.

## Requirements for Deployment

- Amazon Web Services (AWS) account for using Amazon Bedrock.
- DuckDuckGo API setup or integration of any suitable web search tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.