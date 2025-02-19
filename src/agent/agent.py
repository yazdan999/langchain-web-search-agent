import openai

class Agent:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def handle_task(self, task: str):
        response = openai.Completion.create(
            engine="MODEL_NAME",
            prompt=task,
            max_tokens=100
        )
        return response.choices[0].text.strip()
