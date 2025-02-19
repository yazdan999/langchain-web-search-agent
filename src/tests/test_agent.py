import pytest
from agent import Agent

@pytest.fixture
def agent():
    return Agent(api_key="test-api-key")

def test_agent_handle_task(agent):
    response = agent.handle_task("Tell me a joke.")
    assert isinstance(response, str)
    assert len(response) > 0
