from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from src.infrastructure.openai_connection import ConnectionAzureOpenai
from src.tools.tool_viacep import ToolViaCep
from src.tools.tool_agentql import ToolsAgentQL

class Agent:
    def __init__(self, input: str):
        self.memory = InMemorySaver()
        self.tools = [ToolViaCep.tool, ToolsAgentQL.tool()]
        self.llm = ConnectionAzureOpenai.llm_azure_openai()
        self.input = input

    def single_agent(self):
        react_agent = create_react_agent(
            self.llm,
            tools=self.tools,
            checkpointer=self.memory
        )
        return react_agent
