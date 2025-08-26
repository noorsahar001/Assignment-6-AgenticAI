from agents import Agent, ModelSettings
from my_config.config import MODEL

human_agent = Agent(
    name = "Human Agent", 
    instructions = """You are a human Agent.
    Handle complex or escalated customer queries""",
    model=MODEL,
     model_settings=ModelSettings(
        tool_choice="required",
    ),
)