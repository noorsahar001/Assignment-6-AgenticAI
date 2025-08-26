import logging
from my_agents.bot_agent import bot_agent
from my_agents.human_agent import human_agent
from my_guardrails.guards import check_offensive
from agents import Runner, set_tracing_disabled  

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

set_tracing_disabled(True)

def log_tool_invocation(tool_name: str, args: dict):
    logging.info(f"Tool Invoked: {tool_name} | Arguments: {args}")

def log_agent_handoff(agent_name: str):
    logging.info(f"Handoff to Agent: {agent_name}")

def main():
    runner = Runner()  

    while True:
        query = input("Ask your Question ('quit' to exit): ")
        if query.lower() == "quit":
            break
        
        safe_query = check_offensive(query)
        
        if "problem" in query.lower() or "not working" in query.lower():
            log_agent_handoff("Human Agent")
            response = runner.run_sync(human_agent, safe_query)
            print(response)

        elif "order" in query.lower():
            log_agent_handoff("Bot Agent (with tool)")
            log_tool_invocation("get_order_status", {"query": safe_query})
            response = runner.run_sync(bot_agent, safe_query)
            print(response)

        else:
            log_agent_handoff("Human Agent (fallback)")
            response = runner.run_sync(human_agent, safe_query)
            print(response)

if __name__ == "__main__":
    main()
