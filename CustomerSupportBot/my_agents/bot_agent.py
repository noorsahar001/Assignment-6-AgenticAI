from agents import Agent, ModelSettings
from my_config.config import MODEL
from my_tools.tools import get_order_status


bot_agent = Agent(
    name = "Bot Agent",
    instructions = """You are helpful Customer Support Assistant.
    Answer FAQs and provide order updates.""",
    model=MODEL,
    tools=[get_order_status],
    tool_use_behavior="run_llm_again",
    model_settings=ModelSettings(
        tool_choice="auto",
    ),
)