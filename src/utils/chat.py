from src.agent.single_agent import Agent
from src.utils.message_template import pretty_print_messages

def chat():
    """
    Chat with your agent using ViaCEP and AgentQL tools
    """
    agent = Agent("chat").single_agent()
    config = {"configurable": {"thread_id": "1"}}

    print("chat Started! Write 'exit' or 'quit' to leave.")
    print("You can ask about ZIP codes of brazil or request url data extraction from websites.")
    print("-" * 60)

    while True:
   
        try:
            user_input = input("User: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat.")
                break

            for step in agent.stream(
                {"messages": [{"role": "user", "content": user_input}]},
                config=config,
                stream_mode="updates",
            ):
                pretty_print_messages(step, last_message=True)

        except Exception as e:
            print(f"An error occurred: {e}")
            break